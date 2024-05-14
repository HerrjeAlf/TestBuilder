import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *
from random import shuffle

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')

# Klausur Gr. A

fkt = -2*x**3-11*a*x**2-17*a**2*x-6*a**3
fkt_1 = diff(fkt,x)
fkt_2 = diff(fkt,x,2)
fkt_3 = diff(fkt,x,3)
Fkt = integrate(fkt,x)

# print(fkt.subs(x,-1.83))
# print(Fkt.subs())

# Klausur Gr. B

fkt = -5*x**3-2.5*a*x**2+30*a**2*x-22.5*a**3
fkt_1 = diff(fkt,x)
fkt_2 = diff(fkt,x,2)
fkt_3 = diff(fkt,x,3)
Fkt = integrate(fkt ,x)

print(Fkt.subs(x,-a))