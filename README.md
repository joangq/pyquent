<div align="center">
<p>
$$
\LARGE \dashv\mkern-2mu\text{\Huge p$\gamma$quent}\;\;
$$
</p>

<p>
$$
\begin{array}{l}
\large
\text{Python parser for \textit{sequent calculus}} \\
\large
\text{\& \textit{natural deduction} inferences.}
\end{array}
$$
</p>

</div>

![](./assets/terminal.png)

Real time webapp:

https://github.com/joangq/pyquent/assets/86327859/a9d755d8-cd2c-405d-996e-f529fe1fda8f


---

# ✨ Extra: Natural Deduction System helper

https://github.com/joangq/pyquent/assets/86327859/fa301231-bfc2-4d4c-a313-cbf283526bf5



Usage:
```python
from lark import Lark
from pyquent import Pyquent
from pyquent.transformer import *
from typing import Optional
from IPython.display import display, Math
from pyquent.natural_deduction import dict_to_latex
from pyquent.utils import LATEX_FONT_SIZE

pyquent = Pyquent()

parse_to_latex = lambda s: '' if not s else pyquent.transform(s).to_latex()

def display_math(s, size=7):
    # Size between 1 and 10
    display(Math(LATEX_FONT_SIZE[size-1]+'{'+s+'}'))

# ...

d = {'Γ ⊢ τ': 'Γ |- τ and sigma', 'rule': r'\land_{\text{e}_1}'}
display_math(dict_to_latex(d, parser=parse_to_latex))
```

Output:

$$
\displaystyle \Huge\frac{\Gamma \vdash \tau \land \sigma}{\Gamma \vdash \sigma}\land_{\text{e}_2}
$$
