from lark import Transformer, Token
from pyquent.utils import latex_greek

def to_latex_safe(x):
    if 'to_latex' in dir(x):
        return x.to_latex()

    if isinstance(x, str) or isinstance(x, Token):
        return latex_greek(str(x))

class Conjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[2]
        return cls(left, right)
    
    def __str__(self):
        return f"({str(self.left)} ∧ {str(self.right)})"
    
    def __repr__(self):
        return f"Conjunction({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\land {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right
    
class Disjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[2]
        return cls(left, right)
    
    def __str__(self):
        return f"({str(self.left)} ∨ {str(self.right)})"
    
    def __repr__(self):
        return f"Disjunction({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\lor {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Implication:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[2]
        return cls(left, right)
    
    def __str__(self):
        return f"({str(self.left)} ⇒ {str(self.right)})"
    
    def __repr__(self):
        return f"Implication({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\Rightarrow {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Biconditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[2]
        return cls(left, right)
    
    def __str__(self):
        return f"({str(self.left)} ⇔ {str(self.right)})"
    
    def __repr__(self):
        return f"Biconditional({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\Leftrightarrow {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Negation:
    def __init__(self, expr):
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        expr = args[1]
        return cls(expr)
    
    def __str__(self):
        return f"¬{str(self.expr)}"
    
    def __repr__(self):
        return f"Negation({repr(self.expr)})"
    
    def to_latex(self):
        return f"\\neg {to_latex_safe(self.expr)}"
    
    def __eq__(self, other):
        return self.expr == other.expr

class IfThenElse:
    def __init__(self, cond, true, false):
        self.cond = cond
        self.true = true
        self.false = false
    
    @classmethod
    def from_args(cls, args):
        cond = args[0]
        true = args[1]
        false = args[2]
        return cls(cond, true, false)
    
    def __str__(self):
        return f"(if {str(self.cond)} then {str(self.true)} else {str(self.false)})"
    
    def __repr__(self):
        return f"IfThenElse({repr(self.cond)}, {repr(self.true)}, {repr(self.false)})"
    
    def to_latex(self):
        return f"\\text{{if }} {to_latex_safe(self.cond)} \\text{{ then }} {to_latex_safe(self.true)} \\text{{ else }} {to_latex_safe(self.false)}"
    
    def __eq__(self, other):
        return self.cond == other.cond and self.true == other.true and self.false == other.false

class Substitution:
    def __init__(self, expr, var, sub):
        self.expr = expr
        self.var = var
        self.sub = sub
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        var = args[1]
        sub = args[2]
        return cls(expr, var, sub)
    
    def __str__(self):
        return f"{str(self.expr)}{{{str(self.var)} := {str(self.sub)}}}"
    
    def __repr__(self):
        return f"Substitution({repr(self.expr)}, {repr(self.var)}, {repr(self.sub)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.expr)}\\{{ {to_latex_safe(self.var)} := {to_latex_safe(self.sub)} \\}}"
    
    def __eq__(self, other):
        return self.expr == other.expr and self.var == other.var and self.sub == other.sub

class Application:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[1]
        return cls(left, right)
    
    def __str__(self):
        return f"({str(self.left)} {str(self.right)})"
    
    def __repr__(self):
        return f"Application({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Abstraction:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        var = args[1]
        expr = args[2]
        return cls(var, expr)
    
    def __str__(self):
        return f"(λ{str(self.var)} . {str(self.expr)})"
    
    def __repr__(self):
        return f"Abstraction({repr(self.var)}, {repr(self.expr)})"
    
    def to_latex(self):
        return f"\\lambda {to_latex_safe(self.var)} . {to_latex_safe(self.expr)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.expr == other.expr

class TypedAbstraction:
    def __init__(self, var, type, expr):
        self.var = var
        self.type = type
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        var = args[1]
        type = args[2]
        expr = args[3]
        return cls(var, type, expr)
    
    def __str__(self):
        return f"(λ{str(self.var)}: {str(self.type)} . {str(self.expr)})"
    
    def __repr__(self):
        return f"TypedAbstraction({repr(self.var)}, {repr(self.type)}, {repr(self.expr)})"
    
    def to_latex(self):
        return f"\\lambda {to_latex_safe(self.var)}: {to_latex_safe(self.type)} . {to_latex_safe(self.expr)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.type == other.type and self.expr == other.expr

class TypedVar:
    def __init__(self, var, type):
        self.var = var
        self.type = type
    
    @classmethod
    def from_args(cls, args):
        var = args[0]
        type = args[1]
        return cls(var, type)
    
    def __str__(self):
        return f"{str(self.var)} : {str(self.type)}"
    
    def __repr__(self):
        return f"TypedVar({repr(self.var)}, {repr(self.type)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.var)} : {to_latex_safe(self.type)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.type == other.type

class TypeScheme:
    def __init__(self, type):
        self.type = type
    
    @classmethod
    def from_args(cls, args):
        type = args[0]
        return cls(type)
    
    def __str__(self):
        return f"[{str(self.type)}]"
    
    def __repr__(self):
        return f"TypeScheme({repr(self.type)})"
    
    def to_latex(self):
        return f"[{to_latex_safe(self.type)}]"
    
    def __eq__(self, other):
        return self.type == other.type

class TypeSchemeArrow:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[1]
        return cls(left, right)
    
    def __str__(self):
        return f"[{str(self.left)} -> {str(self.right)}]"
    
    def __repr__(self):
        return f"TypeSchemeArrow({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"[{to_latex_safe(self.left)} \\rightarrow {to_latex_safe(self.right)}]"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class TypedExpr:
    def __init__(self, expr, type):
        self.expr = expr
        self.type = type
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        type = args[1]
        return cls(expr, type)
    
    def __str__(self):
        return f"{str(self.expr)} : {str(self.type)}"
    
    def __repr__(self):
        return f"TypedExpr({repr(self.expr)}, {repr(self.type)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.expr)} : {to_latex_safe(self.type)}"
    
    def __eq__(self, other):
        return self.expr == other.expr and self.type == other.type

class TypeArrow:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[1]
        return cls(left, right)
    
    def __str__(self):
        return f"{str(self.left)} -> {str(self.right)}"
    
    def __repr__(self):
        return f"TypeArrow({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\rightarrow {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Zero:
    @classmethod
    def from_args(cls, args):
        if len(args) != 0:
            raise ValueError("Zero takes no arguments")
        return cls()

    def __str__(self):
        return "0"
    
    def __repr__(self):
        return "Zero()"
    
    def to_latex(self):
        return "0"
    
    def __eq__(self, other):
        return isinstance(other, Zero)

class IsZero:
    def __init__(self, expr):
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        return cls(expr)
    
    def __str__(self):
        return f"isZero({str(self.expr)})"
    
    def __repr__(self):
        return f"IsZero({repr(self.expr)})"
    
    def to_latex(self):
        return f"\\text{{isZero}}({to_latex_safe(self.expr)})"
    
    def __eq__(self, other):
        return self.expr == other.expr

class Succ:
    def __init__(self, expr):
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        return cls(expr)
    
    def __str__(self):
        return f"succ({str(self.expr)})"
    
    def __repr__(self):
        return f"Succ({repr(self.expr)})"
    
    def to_latex(self):
        return f"\\text{{succ}}({to_latex_safe(self.expr)})"
    
    def __eq__(self, other):
        return self.expr == other.expr

class Pred:
    def __init__(self, expr):
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        return cls(expr)
    
    def __str__(self):
        return f"pred({str(self.expr)})"
    
    def __repr__(self):
        return f"Pred({repr(self.expr)})"
    
    def to_latex(self):
        return f"\\text{{pred}}({to_latex_safe(self.expr)})"
    
    def __eq__(self, other):
        return self.expr == other.expr

class Product:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    @classmethod
    def from_args(cls, args):
        left = args[0]
        right = args[2]
        return cls(left, right)
    
    def __str__(self):
        return f"{str(self.left)} × {str(self.right)}"
    
    def __repr__(self):
        return f"Product({repr(self.left)}, {repr(self.right)})"
    
    def to_latex(self):
        return f"{to_latex_safe(self.left)} \\times {to_latex_safe(self.right)}"
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

class Mu:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        var = args[1]
        expr = args[2]
        return cls(var, expr)
    
    def __str__(self):
        return f"µ {str(self.var)} . {str(self.expr)}"

    def __repr__(self):
        return f"Mu({repr(self.var)}, {repr(self.expr)})"

    def to_latex(self):
        return f"\\mu {to_latex_safe(self.var)} . {to_latex_safe(self.expr)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.expr == other.expr

class Let:
    def __init__(self, var, expr, body):
        self.var = var
        self.expr = expr
        self.body = body
    
    @classmethod
    def from_args(cls, args):
        var = args[0]
        expr = args[1]
        body = args[2]
        return cls(var, expr, body)
    
    def __str__(self):
        return f"let {str(self.var)} = {str(self.expr)} in {str(self.body)}"
    
    def __repr__(self):
        return f"Let({repr(self.var)}, {repr(self.expr)}, {repr(self.body)})"
    
    def to_latex(self):
        return f"\\text{{let }} {to_latex_safe(self.var)} = {to_latex_safe(self.expr)} \\text{{ in }} {to_latex_safe(self.body)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.expr == other.expr and self.body == other.body

class Forall:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        var = args[0]
        expr = args[1]
        return cls(var, expr)
    
    def __str__(self):
        return f"(∀{str(self.var)} . {str(self.expr)})"
    
    def __repr__(self):
        return f"Forall({repr(self.var)}, {repr(self.expr)})"
    
    def to_latex(self):
        return f"\\forall {to_latex_safe(self.var)} . {to_latex_safe(self.expr)}"
    
    def __eq__(self, other):
        return self.var == other.var and self.expr == other.expr

class Sequent:
    def __init__(self, right, left=None):
        self.right = right

        if left is not None:
            self.left = left
    
    @classmethod
    def from_args(cls, args):
        if len(args) == 3:
            left = args[0]
            right = args[2]
            return cls(left=left, right=right)
        else:
            right = args[1]
            return cls(right=right)
    
    def __str__(self):
        if hasattr(self, "left"):
            return f"{str(self.left)} ⊢ {str(self.right)}"
        else:
            return f"⊢ {str(self.right)}"
    
    def __repr__(self):
        if hasattr(self, "left"):
            return f"Sequent(left={repr(self.left)}, right={repr(self.right)})"
        else:
            return f"Sequent(right={repr(self.right)})"
    
    def to_latex(self):
        if hasattr(self, "left"):
            return f"{to_latex_safe(self.left)} \\vdash {to_latex_safe(self.right)}"
        else:
            return f"\\vdash {to_latex_safe(self.right)}"
        
    def __eq__(self, other):
        if hasattr(self, "left"):
            return self.left == other.left and self.right == other.right
        else:
            return self.right == other.right

class Parens:
    def __init__(self, expr):
        self.expr = expr
    
    @classmethod
    def from_args(cls, args):
        expr = args[0]
        return cls(expr)
    
    def __str__(self):
        return f"({str(self.expr)})"
    
    def __repr__(self):
        return f"Parens({repr(self.expr)})"
    
    def to_latex(self):
        return f"({to_latex_safe(self.expr)})"
    
    def __eq__(self, other):
        return self.expr == other.expr

class Atom:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_args(cls, value):
        value = value
        return cls(value)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Atom({repr(self.value)})"
    
    def to_latex(self):
        return to_latex_safe(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
class Var:
    def __init__(self, value):
        self.value = str(value)
        self.bottom = False

        if self.value == 'bottom':
            self.bottom = True
            self.value = '⊥'
    
    @classmethod
    def from_args(cls, value):
        return cls(value)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Var({repr(self.value)})"
    
    def to_latex(self):
        if self.bottom:
            return "\\bot"
        return latex_greek(self.value)
    
    def __eq__(self, other):
        return self.value == other.value

grammar_map = {
    "land": Conjunction,
    "lor": Disjunction,
    "implies": Implication,
    "iff": Biconditional,
    "neg": Negation,
    "ifthenelse": IfThenElse,
    "substitution": Substitution,
    "application": Application,
    "abstraction": Abstraction,
    "typed_abstraction": TypedAbstraction,
    "typed_var": TypedVar,
    "type_scheme": TypeScheme,
    "type_scheme_arrow": TypeSchemeArrow,
    "typed_expr": TypedExpr,
    "type_arrow": TypeArrow,
    "zero": Zero,
    "iszero": IsZero,
    "succ": Succ,
    "pred": Pred,
    "prod": Product,
    "mu": Mu,
    "let": Let,
    "forall": Forall,
    "sequent": Sequent,
    "parens": Parens,
    "atom": Atom,
    "VAR": Var
}

class GrammarTransformer(Transformer): 
    start = 'start'
    # Transformer methods are dynamically added here
    ...

for key, value in grammar_map.items():
    from_args = getattr(value, 'from_args', None)

    if from_args is None:
        raise ValueError(f"Class {value} does not have a from_args method")
    
    setattr(GrammarTransformer, key, from_args)