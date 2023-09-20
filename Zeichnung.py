import matplotlib.pyplot as plt
from sympy import *
import numpy

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()


def Graph(a_1, b_1, xwert, f, titel, n, name, *lswerte):
    # lswerte sind für die Werte für die Lösungen
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
    for i, werte in enumerate(lswerte):
        if i % 2 != 0:  # überspringt ungerade Zahlen für das elif weiter unten
            continue
        elif werte is not None and lswerte[i + 1] is not None:  # Überprüft, ob es den Wert oder den nächsten Wert gibt
            plt.plot(werte, lswerte[i + 1], linewidth=2)
    plt.suptitle(titel, usetex=True)
    return plt.savefig(name, dpi=200)


def loeschen():
    plt.figure().clear()
