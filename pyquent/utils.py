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

def inverse(d):
    return {v: k for k, v in d.items()}

def latex_greek(x):
    lookup_dict = greek_upper if not x.islower() else greek_lower

    if not x.isascii():
        lookup_dict = inverse(lookup_dict)

    result = lookup_dict.get(x, None)

    if result is None:
        return x
    
    if len(result) == 1:
        return f'\\{x}'
    
    return f'\\{result}'

# ------------------------------------------------------------------------------

LATEX_FONT_SIZE = [
    '\\tiny',
    '\\scriptsize',
    '\\footnotesize',
    '\\small',
    '\\normalsize',
    '\\large',
    '\\Large',
    '\\LARGE',
    '\\huge',
    '\\Huge'
]