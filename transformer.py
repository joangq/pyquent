from lark import Transformer, Token

class Sequent:
    def __init__(self, antecedent, succedent, unicode=False):
        self.antecedent = antecedent
        self.succedent = succedent
    
    def __str__(self):
        return f"{', '.join(map(str, self.antecedent))} ⊢ {', '.join(map(str, self.succedent))}".strip()
    
    def __repr__(self):
        inner = f"{', '.join(map(repr, self.antecedent))}, {', '.join(map(repr, self.succedent))}".strip()
        return f'Sequent({inner})'
    
class Implication:
    def __init__(self, left, right, unicode=False):
        self.symbol = "⇒" if unicode else "=>"
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} {self.symbol} {self.right}"
    
    def __repr__(self):
        return f'Implication({repr(self.left)}, {repr(self.right)})'

class Conjunction:
    def __init__(self, left, right, unicode=False):
        self.symbol = "∧" if unicode else "and"
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} {self.symbol} {self.right}"
    
    def __repr__(self):
        return f'Conjunction({repr(self.left)}, {repr(self.right)})'

class Disjunction:
    def __init__(self, left, right, unicode=False):
        self.symbol = "∨" if unicode else "or"
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} {self.symbol} {self.right}"
    
    def __repr__(self):
        return f'Disjunction({repr(self.left)}, {repr(self.right)})'

class Negation:
    def __init__(self, value, unicode=False):
        self.symbol = "¬" if unicode else "not "
        self.value = value
    
    def __str__(self):
        inner = str(self.value) if isinstance(self.value, str) else f"({self.value})"
        return f"{self.symbol}{inner}"
    
    def __repr__(self):
        return f'Negation({repr(self.value)})'

class Iff:
    def __init__(self, left, right, unicode=False):
        self.symbol = "⇔" if unicode else "<=>"
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.left} {self.symbol} {self.right}"
    
    def __repr__(self):
        return f'Iff({repr(self.left)}, {repr(self.right)})'

class SequentTransformer(Transformer):
    def set_unicode(self, unicode):
        self.unicode = unicode
        return self

    def atom(self, items):
        return str(items[0])
    
    def implication(self, items):
        return Implication(items[0], items[2], self.unicode)
    
    def conjunction(self, items):
        return Conjunction(items[0], items[2], self.unicode)
    
    def disjunction(self, items):
        return Disjunction(items[0], items[2], self.unicode)
    
    def negation(self, items):
        return Negation(items[1], self.unicode)
    
    def iff(self, items):
        return Iff(items[0], items[2], self.unicode)

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

        return Sequent(antecedent, succedent, self.unicode)