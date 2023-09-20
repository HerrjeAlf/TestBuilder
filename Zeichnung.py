import matplotlib.pyplot as plt
from sympy import *
import numpy

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()

def Graph(a_1, b_1, xwert, f, titel, n, name, a_2 = [], b_2 = [], a_3 = [], b_3 = [], a_4=[], b_4 = [],a_5= [], b_5 = [], a_6 = [], b_6 = [],  a_7 = [], b_7 = []):
    # die Schlüsselwortparameter (a_2, b_2 bis a_7, b_7 können stattdessen um beliebige Anzahl mit *xwerte, *ywerte ersetzt werden - keine Zeit grade
    ax = plt.gca()
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
    plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                 fontsize=12)
    plt.grid(True)
    plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    plt.plot(a_1, b_1, linewidth=2)
    if a_2 != [] and b_2 != []:
        plt.plot(a_2, b_2, linewidth=2)
    if a_3 != [] and b_3 != []:
        plt.plot(a_3, b_3, linewidth=2)
    if a_4 != [] and b_4 != []:
        plt.plot(a_4, b_4, linewidth=2)
    if a_5 != [] and b_5 != []:
        plt.plot(a_5, b_5, linewidth=2)
    if a_6 != [] and b_6 != []:
        plt.plot(a_6, b_6, linewidth=2)
    if a_7 != [] and b_7 != []:
        plt.plot(a_7, b_7, linewidth=2)
    plt.suptitle(titel, usetex=True)
    return plt.savefig(name, dpi=200)

def loeschen():
    plt.figure().clear()


