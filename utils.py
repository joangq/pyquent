class DefaultInitMeta(type):
    def __new__(cls, name, bases, attrs):
        if '__init__' not in attrs:
            def __init__(self, *args, **kwargs):
                super(self.__class__, self).__init__(*args, **kwargs)
            attrs['__init__'] = __init__
        return super().__new__(cls, name, bases, attrs)

# -------------------------------------------------------------------------

class bijection:
    def __init__(self, d: None|dict = None):
        if d:
            self.forward = d
            self.backward = {v: k for k, v in d.items()}
        else:
            self.forward = {}
            self.backward = {}
    
    def __setitem__(self, key, value):
        self.forward[key] = value
        self.backward[value] = key
    
    def __getitem__(self, key):
        if key in self.forward:
            return self.forward[key]
        return self.backward[key]
    
    def get(self, key, default=None):
        if key in self.forward:
            return self.forward[key]
        return self.backward.get(key, default)
    
    def __contains__(self, key):
        return key in self.forward or key in self.backward
    
    def __delitem__(self, key):
        if key in self.forward:
            del self.backward[self.forward[key]]
            del self.forward[key]
        else:
            del self.forward[self.backward[key]]
            del self.backward[key]
    
    def __len__(self):
        return len(self.forward)
    
    def __iter__(self):
        return iter(self.forward)
    
    @staticmethod
    def __format__(k,v, align='left'):
        if align not in ('left', 'right'):
            raise ValueError(f"align must be 'left' or 'right', not {align}")
        
        str_left = getattr(str(k), 'ljust' if align == 'left' else 'rjust')
        str_right = getattr(str(v), 'rjust' if align == 'left' else 'ljust')
        
        return lambda l,r: f"{str_left(l)} <-> {str_right(r)}"
    
    def __repr__(self):
        output = 'bijection('
        offset = len(output)

        strings = [None for _ in self.forward]
        max_len_k = 0
        max_len_v = 0
        i = 0
        
        for k, v in self.forward.items():
            max_len_k = max(max_len_k, len(str(k)))
            max_len_v = max(max_len_v, len(str(v)))

            strings[i] = bijection.__format__(k,v, align='left')
            i += 1
        
        it = iter(map(lambda f: f(max_len_k, max_len_v), strings))
        output += next(it) + '\n'
        for s in it:
            output += (' '*offset) + s + '\n'
        output += (' '*(offset-1)) + ')'
        
        return output
    

# -------------------------------------------------------------------------

greek_lower = {
    "alpha": "α",
    "beta": "β",
    "gamma": "γ",
    "delta": "δ",
    "epsilon": "ε",
    "zeta": "ζ",
    "eta": "η",
    "theta": "θ",
    "iota": "ι",
    "kappa": "κ",
    "lambda": "λ",
    "mu": "μ",
    "nu": "ν",
    "xi": "ξ",
    "omicron": "ο",
    "pi": "π",
    "rho": "ρ",
    "sigma": "σ",
    "tau": "τ",
    "upsilon": "υ",
    "phi": "φ",
    "chi": "χ",
    "psi": "ψ",
    "omega": "ω"
}

greek_upper = {k.capitalize(): v.capitalize() for k, v in greek_lower.items()}

greek = {**greek_lower, **greek_upper}
greek = bijection(greek)