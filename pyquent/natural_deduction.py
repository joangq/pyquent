from typing import Optional, Callable

DEFAULT_FORMAT = "\displaystyle{{\\frac{{{premises}}}{{{conclusion}}}{rule}}}"

def parse_with(obj: dict|list|str, parser: Callable, format: str, separator=',\;') -> str:
    match obj:
        case string if isinstance(obj, str):
            return parser(string)
        
        case xs if isinstance(obj, list):
            return separator.join(parse_with(x, parser, format) for x in xs)
        
        case dictionary if isinstance(obj, dict):
            return dict_to_latex(dictionary, parser, format)
        
        case _:
            raise ValueError(f'Unsupported type: {type(obj)}. It must be a string, list, or dictionary.')

def dict_to_latex(d, parser: Optional[Callable]=None, format=DEFAULT_FORMAT) -> str:
    if not d:
        return ''

    if not parser:
        parser = lambda x: x

    if not isinstance(d, dict):
        raise ValueError('Non-dict entries are not supported.')

    rule = d.get('rule', '')
    if rule: del d['rule']
    
    key = next(iter(d.keys()))


    value = next(iter(d.values()))

    try:
        if isinstance(key, tuple):
            parsed_key = [parse_with(x, parser, format) for x in key]
            parsed_key = ',\;'.join(parsed_key[:-1]) + '\;' + parsed_key[-1]
        else:
            parsed_key = parser(key)
    except Exception as e:
        raise ValueError(f'Error parsing key: {key}') from e
    

    parsed_value = parse_with(value, parser, format)

    return format.format(premises=parsed_value, conclusion=parsed_key, rule=rule)