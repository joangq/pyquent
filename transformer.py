from lark import Transformer, Token
from utils import greek

def to_latex_safe(s):
    if isinstance(s, str):
        g = greek.get(s, None)
        if g:
            if len(g) == 1:
                return '\\'+s
            else:
                return '\\'+g
        else:
            return s
    else:
        return s.to_latex()

class Sequent:
    def __init__(self, antecedent, succedent):
        self.antecedent = antecedent
        self.succedent = succedent
    
    def __str__(self):
        return f"{', '.join(map(str, self.antecedent))} ⊢ {', '.join(map(str, self.succedent))}".strip()
    
    def __repr__(self):
        inner = f"{', '.join(map(repr, self.antecedent))} ⊢ {', '.join(map(repr, self.succedent))}".strip()
        return f'Sequent({inner})'
    
    def to_latex(self):
        return f"{', '.join(map(to_latex_safe, self.antecedent))} \\vdash {', '.join(map(to_latex_safe, self.succedent))}"
    
class Implication:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} => {self.right}"
    
    def __repr__(self):
        return f'Implication({repr(self.left)}, {repr(self.right)})'
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\Rightarrow {to_latex_safe(self.right)}"

class Conjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} ∧ {self.right}"
    
    def __repr__(self):
        return f'Conjunction({repr(self.left)}, {repr(self.right)})'
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\land {to_latex_safe(self.right)}"

class Disjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} ∨ {self.right}"
    
    def __repr__(self):
        return f'Disjunction({repr(self.left)}, {repr(self.right)})'
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\lor {to_latex_safe(self.right)}"

class Negation:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        inner = str(self.value) if isinstance(self.value, str) else f"({self.value})"
        return f"¬{inner}"
    
    def __repr__(self):
        return f'Negation({repr(self.value)})'
    
    def to_latex(self):
        inner = to_latex_safe(self.value) if isinstance(self.value, str) else f"({to_latex_safe(self.value)})"
        return f"\\neg {inner}"

class Iff:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} <=> {self.right}"
    
    def __repr__(self):
        return f'Iff({repr(self.left)}, {repr(self.right)})'
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\Leftrightarrow {to_latex_safe(self.right)}"

class SequentTransformer(Transformer):
    def set_unicode(self, unicode):
        self.unicode = unicode
        # FIXME: This functionality got broken whilst changing the grammar
        # and the LaTeX support. It should be added again.
        return self

    def atom(self, items):
        return str(items[0])
    
    def implication(self, items):
        return Implication(items[0], items[2])
    
    def conjunction(self, items):
        return Conjunction(items[0], items[2])
    
    def disjunction(self, items):
        return Disjunction(items[0], items[2])
    
    def negation(self, items):
        return Negation(items[1])
    
    def iff(self, items):
        return Iff(items[0], items[2])

    def formula(self, items):
        # return " ".join(map(str, items))
        return items[0]

    def formulas(self, items):
        return items

    def sequent(self, items):
        if len(items) < 2:
            raise ValueError("Invalid sequent")
        
        first = items[0]

        if isinstance(first, Token) and first.type == "TURNSTILE":
            antecedent = []
            _, succedent = items
        else:
            antecedent, _, succedent = items

        return Sequent(antecedent, succedent)