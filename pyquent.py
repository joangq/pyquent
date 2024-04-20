from lark import Lark # pip install lark-parser
from transformer import SequentTransformer
import argparse

class Pyquent:
    def __init__(self, unicode=False):
        with open('grammar.lark') as f:
            sequent_grammar = f.read()
        
        self.unicode = unicode

        self.parser = Lark(sequent_grammar, start='start', parser='lalr')
    
    def parse(self, text):
        return self.parser.parse(text)
    
    def transform(self, tree):
        return SequentTransformer().set_unicode(self.unicode).transform(tree)
    
    def __call__(self, 
                 text, 
                 output=None, 
                 show_repr=False, 
                 unicode=False, 
                 pretty=False, 
                 latex=False) -> list:
        
        tree = self.parse(text)
        output = self.transform(tree)
        
        result = list()
        if show_repr:
            result.append(repr(output))
        
        if pretty:
            result.append(str(output))

        if latex:
            result.append(output.to_latex())
        
        return result

class Parser(argparse.ArgumentParser):
    def __init__(self):
        super(Parser, self).__init__()

        self.add_argument('default_input', nargs='?', default=None)
        self.add_argument('-i', '--input', nargs='?', default=None)
        self.add_argument('-o', '--output', nargs='?', default=None)
        self.add_argument('-r', '--show-repr', action='store_true')
        self.add_argument('-p', '--pretty', action='store_true')
        self.add_argument('-u', '--unicode', action='store_true')
        self.add_argument('-x', '--latex', action='store_true')
    
    def parse_args(self):
        self.args = super(Parser, self).parse_args().__dict__
        return self


if __name__ == '__main__':
    parser = Parser().parse_args()
    args = parser.args

    if all(v is None for v in args.values()):
        parser.print_help()
        exit(1)
    
    default_input = args.get('default_input', None)
    input = args.get('input', None)
    output = args.get('output', None)
    show_repr = args.get('show_repr', False)
    pretty = args.get('pretty', False)
    unicode = args.get('unicode', False)
    latex = args.get('latex', False)

    if default_input is not None:
        pyquent = Pyquent(unicode)
        for x in pyquent(default_input, output, show_repr, unicode, pretty, latex):
            print(x)