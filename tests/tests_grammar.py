import unittest
from pyquent import Pyquent
from pyquent.transformer import (
    grammar_map,
    Sequent, 
    Substitution, 
    TypedVar, 
    Var, 
    Let, 
    Forall, 
    Application, 
    TypeScheme, 
    TypeSchemeArrow, 
    TypedExpr, 
    Parens, 
    IfThenElse, 
    Abstraction, 
    TypeArrow, 
    IsZero, 
    Zero, 
    Product, 
    Mu, 
    Pred
)

class TestGrammar(unittest.TestCase):
    pyquent = Pyquent()
    
    def test_grammar(self):
        terms = {x
                 for rule in self.pyquent.parser.rules
                 for x in [rule.origin.name, rule.alias]
                 if x is not None}

        defined_transformers = set(map(str.lower, grammar_map.keys()))

        self.assertIn('var', defined_transformers)

        EXCLUDED = {
            'start', # The transformer starts from here, hence we don't transform it.
            'expr',  # All the cases are covered by sub-terms.
            'type',  # It's either VAR or an alias term.
            'term',  # It's either 'atom' or 'neg'.
            'var',   # It's not in the set of {*rules, *aliases}
        }

        result = set.symmetric_difference(terms, defined_transformers)

        self.assertEqual(result, EXCLUDED)


    def test_cases(self):
        tests = [
            (r"Gamma |- M : tau{X:=sigma}", 
            Sequent(left=Substitution(TypedVar(Var('M'), Var('tau')), Var('X'), Var('sigma')), 
                    right=Var('Gamma'))),

            (r"Gamma |- let x = N in M:sigma", 
            Sequent(left=Let(Var('x'), Var('N'), TypedVar(Var('M'), Var('sigma'))), 
                    right=Var('Gamma'))),

            (r"Gamma |- M: forall X . b", 
            Sequent(left=TypedVar(Var('M'), Forall(Var('X'), Var('b'))), 
                    right=Var('Gamma'))),

            (r"Gamma |- M N : [ sigma ]", 
            Sequent(left=Application(Var('M'), TypedVar(Var('N'), TypeScheme(Var('sigma')))), 
                    right=Var('Gamma'))),

            (r"Gamma |- M N : forall X . [sigma -> sigma]", 
            Sequent(left=Application(Var('M'), TypedVar(Var('N'), Forall(Var('X'), TypeSchemeArrow(Var('sigma'), Var('sigma'))))), 
                    right=Var('Gamma'))),

            (r"Gamma |- (if A then B else C) : tau", 
            Sequent(left=TypedExpr(Parens(IfThenElse(Var('A'), Var('B'), Var('C'))), Var('tau')), 
                    right=Var('Gamma'))),

            (r"Gamma |- (λx . M) : sigma -> tau", 
            Sequent(left=TypedExpr(Parens(Abstraction(Var('x'), Var('M'))), TypeArrow(Var('sigma'), Var('tau'))), 
                    right=Var('Gamma'))),

            (r"isZero(zero)", 
            IsZero(Zero())),

            (r"a*b", 
            Product(Var('a'), Var('b'))),

            (r"µ f . lambda n. if isZero(n) then 1 else n * f pred(n)", 
            Mu(Var('f'), Abstraction(Var('n'), IfThenElse(IsZero(Var('n')), Var('1'), Product(Var('n'), Application(Var('f'), Pred(Var('n')))))))),

            (r"((a:c)*b):b", 
            TypedExpr(Parens(Product(Parens(TypedVar(Var('a'), Var('c'))), Var('b'))), Var('b'))),
        ]

        for case, expected in tests:
            with self.subTest(test=case):
                result = self.pyquent.parse(case)
                transformed_res = self.pyquent.transform(result)
                self.assertEqual(transformed_res, expected)
        