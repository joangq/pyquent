from utils import DefaultInitMeta
from typing import Optional

class Node(metaclass=DefaultInitMeta):
    def __init__(self, value, rule: Optional[str] = None):
        self.value = value
        self.rule = rule

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __iter__(self):
        yield self.value
        yield self.rule

    __match_args__ = ('value', 'rule')

class Terminal(Node): ...
class Inference(Node): ...

def latexify(key, value, parser: callable, rule='') -> str:
        match value:
            case d if isinstance(value, dict):
                if 'rule' in d: rule = d['rule']
                inner_latex = r'\;\;'.join(latexify(k, v, parser) for k, v in d.items())
                key = parser(key)
                return fr'\frac{{{inner_latex}}}{{{key}}}'+rule
            
            case Terminal(value, rule):
                value = parser(value)
                key = parser(key)
                return fr'\frac{{{value}}}{{{key}}}'+rule
            
            case Inference(value, rule):
                value = parser(value)
                key = parser(key)
                return latexify(key, value | {'rule': rule})
            
            case _:
                value = parser(value)
                key = parser(key)
                return fr'\frac{{{value}}}{{{key}}}'+rule

def dict_to_latex(d, parser: Optional[callable]=None) -> str:
    if not d:
        return ''
    
    if not parser:
        parser = lambda x: x

    if isinstance(d, Terminal):
        return latexify(d.value, '', parser, rule=d.rule)
    
    if isinstance(d, Inference):
        for k,v in d.value.items():
            return latexify(k, v, parser, rule=d.rule)
    
    for key, value in d.items():
        return latexify(key, value, parser, rule=d.get('rule', ''))
