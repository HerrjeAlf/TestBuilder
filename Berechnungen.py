import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def Ableitungen(fkt):
    fkt_1 = diff(fkt,x,1)
    fkt_2 = diff(fkt,x,2)
    fkt_3 = diff(fkt,x,3)
    print(r'f_1 (x) = ' + str(fkt_1))
    print(r'f_2 (x) = ' + str(fkt_2))
    print(r'f_3 (x) = ' + str(fkt_3))
    return fkt_1, fkt_2, fkt_3

def Extrema(fkt):
    fkt_1 = diff(fkt, x, 1)
    fkt_2 = diff(fkt, x, 2)
    xwerte_extrema_alle = solve(fkt_1,x)
    xwerte_extrema_reell = [x for x in xwerte_extrema_alle if not isinstance(x, complex)]
    # print(xwerte_extrema_alle)
    # print(xwerte_extrema_reell)
    for xwert in xwerte_extrema_reell:
        wert_in_fkt_2 = fkt_2.subs(x,xwert)
        if wert_in_fkt_2 < 0:
            ywert = fkt.subs(x,xwert)
            print('Hochpunkt bei ( ' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
        elif wert_in_fkt_2 > 0:
            ywert = fkt.subs(x,xwert)
            print('Tiefpunkt bei ( ' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
        else:
            ywert = fkt.subs(x, xwert)
            print('Eventuell ein Sattelpunkt bei S( ' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')

# def Wendepunkte(fkt):


def Graph(x_min, x_max, fkt):
    xwerte = np.arange(x_min,x_max,0.01)
    ywerte = [fkt.subs(x, elements) for elements in xwerte]
    fig, ax = plt.subplots()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.plot(xwerte, ywerte)
    plt.grid(True)
    return plt.show(), plt.savefig('Graph der Funktion', dpi=300)

Extrema(-2.5*x**3-7.5*x**2+8.125*x+13.125)
Graph(-5,5,-2.5*x**3-7.5*x**2+8.125*x+13.125)
