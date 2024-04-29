from .transformer import GrammarTransformer
from lark import (
    Lark,
    Tree as LarkTree,
    Token as LarkToken
)

class Pyquent:
    def __init__(self):
        with open('pyquent/grammar/grammar.lark') as f:
            self.grammar = f.read()
        
        self.transformer = GrammarTransformer()
        self.parser = Lark(self.grammar, 
                           parser='lalr', 
                           start=self.transformer.start)
    
    def parse(self, text) -> LarkTree:
        return self.parser.parse(text)

    def transform(self, tree: LarkTree|str):
        if isinstance(tree, LarkToken):
            return GrammarTransformer.VAR(tree)
        if isinstance(tree, str):
            return self.transform(self.parse(tree))
        
        return self.transformer.transform(tree)
    
    def __call__(self,
                 text: str,
                 output: str=None,
                 show_repr: bool=False,
                 unicode: bool=False,
                 pretty: bool=False,
                 latex: bool=False) -> list:
        
        tree = self.parse(text)
        _result = self.transform(tree)

        result = list()
        if show_repr:
            result.append(repr(_result))
        
        if pretty:
            result.append(str(_result))
        
        if latex:
            result.append(_result.to_latex())
        
        return result