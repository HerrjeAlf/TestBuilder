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
    i = 0
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
            print('Hochpunkt bei H_{' + str(i) +  '}( ' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
            i += 1
        elif wert_in_fkt_2 > 0:
            ywert = fkt.subs(x,xwert)
            print('Tiefpunkt bei  T_{' + str(i) +  '}( ' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
            i += 1
        else:
            ywert = fkt.subs(x, xwert)
            print('Eventuell ein Sattelpunkt bei S_{' + str(i) +  '} (' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
            i += 1

# def Wendepunkte(fkt):


def Graph(x_min, x_max, *funktionen):
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
    xwerte = np.arange(x_min, x_max, 0.01)
    for fkt in funktionen:
        ywerte = [fkt.subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte)
    plt.grid(True)
    return plt.show()

def integral(a,b,fkt):
    Fkt = integrate(fkt,x)
    flaeche = Fkt.subs(x,b)-Fkt.subs(x,a)
    print('F(x)=' + str(Fkt))
    print('Fläche unter dem Graphen von ' + str(a) + ' bis ' + str(b) + ' ist A= ' + str(flaeche) + ' FE.')


def schnittpunkte(fkt_1,fkt_2):
    i = 0
    xwerte = solve(Eq(fkt_1,fkt_2),x)
    for xwert in xwerte:
        ywert = fkt_1.subs(x, xwert)
        print('S_'+ str(i) + '(' + latex(N(xwert,3)) + ' | ' + latex(N(ywert,3)) + ' )')
        i += 1
print(expand(-2*(x+1)*(x+2)*(x-a)))
# schnittpunkte(4*x**3-16*x**2-5*x+42,3/79*x+16.28)
# Graph(0, 5,60*x**3-60*x**2 + 720, 720*x)
# integral(0,4/3,4*x**3-16*x**2-398/79*x+25.68)

# print(4*(4/3)**3-16*(4/3)**2-5*(4/3)+42)
# print(4*(4/3)**3-16*(4/3)**2-5*(4/3)+42-4/79)