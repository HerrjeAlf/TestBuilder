import numpy
import random

import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat
from pylatex.utils import bold
from sympy import *

# Defintion der Funktionen

Expand All
	@@ -14,56 +14,64 @@

liste_variable = [a, b, c, d, x, y, z]


def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k


def nzahl(p, q):
    k = random.randint(p, q)
    return k


def vorz_str(k):
    if k < 0:
        k = latex(k)
    else:
        k = '+' + latex(k)
    return k


def vorz_str_minus(k):
    if k < 0:
        k = '(' + latex(k) + ')'
    else:
        k = latex(k)
    return k


def Bild_1(a, b, f, n):
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
    plt.annotate(n, xy=(-4, f.subs(x, -4)), xycoords='data', xytext=(+5, +5), textcoords='offset points', fontsize=12)
    plt.grid(True)
    plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    return plt.plot(a, b, linewidth=2)


# Berechnung für die Aufgaben

def folgen(nr, teilaufg):
    liste_teilaufg = [a, b, c, d]
    i = 0

    start_arithm_folge = zzahl(1, 10)
    start_geom_folge = nzahl(1, 10)
    arithm_folge_d = nzahl(2, 10)
    basis = zzahl(2, 10)

    if nzahl(1, 2) == 1:
        p = random.choice([2, 4, 5, 8, 10])
        geom_folge_q = Rational(1, p)
Expand All
	@@ -72,13 +80,14 @@ def folgen(nr, teilaufg):

    bel_vorschrift = [start_arithm_folge + basis ** x,
                      start_arithm_folge - 1 / x,
                      start_arithm_folge / (x + arithm_folge_d),
                      x ** arithm_folge_d]
    bel_vorschrift_str = [str(start_arithm_folge) + vorz_str(basis) + r'^{n}',
                          str(start_arithm_folge) + r'~-~ \frac{1}{n}',
                          r' \frac{' + str(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                          r'n^{' + str(arithm_folge_d) + '}']
    ausw_folge = random.randint(1, len(bel_vorschrift)) - 1

    a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                start_geom_folge * geom_folge_q ** (x - 1),
                bel_vorschrift[ausw_folge]]
Expand All
	@@ -92,36 +101,33 @@ def folgen(nr, teilaufg):
    data = [a_n.subs(x, i) for i in range(1, 5)]
    data_lsg = [a_n.subs(x, i) for i in range(1, 8)]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Zahlenfolge: \n\n',
               latex(data[0]) + r', \quad ' + latex(data[1]) + r', \quad ' + latex(data[2]) + r', \quad ' +
               latex(data[3]) + r', ~ ...  \\']

    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Setze die Zahlenfolge um drei weitere Glieder fort. \n\n')
        loesung.append(
            str(liste_teilaufg[i]) + r') \quad ' + latex(data_lsg[0]) + ',~' + latex(data_lsg[1]) + ',~' + latex(
                data_lsg[2]) + ',~' +
            latex(data_lsg[3]) + r',~' + latex(data_lsg[4]) + ',~' + latex(data_lsg[5]) + ',~' + latex(data_lsg[6]))
        i += 1

    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Überprüfe ob es sich um eine arithmetische oder geometrische '
                                                'Zahlenfolge handelt. \n\n')
        if auswahl_folgenart == 0:
            table_b = Tabular('|c|c|c|c|', row_height=1.2)
            table_b.add_hline(1, 4)
            table_b.add_row('Differenz der Werte', 'a1-a0', 'a2-a1', 'a3-a2')
            table_b.add_hline(1, 4)
            table_b.add_row('Ergebnis', data[1] - data[0], data[2] - data[1], data[3] - data[2])
            table_b.add_hline(1, 4)
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                    r'~ist~es~eine~arithmetische~Folge~mit~d~=~'
                           + str(arithm_folge_d) + r'.} \quad (3P)')
            loesung.append(table_b)
        if auswahl_folgenart == 1:
            table_b = Tabular('|c|c|c|c|', row_height=1.2)
Expand All
	@@ -131,9 +137,9 @@ def folgen(nr, teilaufg):
            table_b.add_row('Ergebnis', Rational(data[1], data[0]), Rational(data[2] / data[1]),
                            Rational(data[3] / data[2]))
            table_b.add_hline(1, 4)
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                    r'~ist~es~eine~geometrische~Folge~mit~q~=~'
                           + str(geom_folge_q) + '.} \quad (3P)')
            loesung.append(table_b)
        if auswahl_folgenart == 2:
            table_b = Tabular('|c|c|c|c|c|', row_height=1.2)
Expand All
	@@ -143,28 +149,32 @@ def folgen(nr, teilaufg):
            table_b.add_row('Ergebnis', data[1] - data[0], data[2] - data[1], N(data[1] / data[0], 3),
                            N(data[2] / data[1], 4))
            table_b.add_hline(1, 5)
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                    r'~ist~weder~eine~arithmetische,~noch~eine~geometrische~Folge.} '
                                                    r'\quad (3P)')
            loesung.append(table_b)
        i += 1

    if c in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Nenne das Bildungsgesetz der Zahlenfolge. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad a_n~=~' + a_n_str + r' \quad (2P)')
        i += 1

    print(data)
    print(a_n)
    print(auswahl_folgenart)
    return aufgabe, loesung


def grenzwerte(nr, teilaufg):
    liste_teilaufg = [a, b, c, d]
    i = 0

    start_arithm_folge = zzahl(1, 10)
    start_geom_folge = nzahl(1, 10)
    arithm_folge_d = nzahl(2, 10)
    basis = zzahl(2, 10)

    if nzahl(1, 2) == 1:
        p = random.choice([2, 4, 5, 8, 10])
        geom_folge_q = Rational(1, p)
Expand All
	@@ -173,13 +183,14 @@ def grenzwerte(nr, teilaufg):

    bel_vorschrift = [start_arithm_folge + basis ** x,
                      start_arithm_folge - 1 / x,
                      start_arithm_folge / (x + arithm_folge_d),
                      x ** arithm_folge_d]
    bel_vorschrift_str = [str(start_arithm_folge) + vorz_str(basis) + r'^{n}',
                          str(start_arithm_folge) + r'~-~ \frac{1}{n}',
                          r' \frac{' + str(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                          r'n^{' + str(arithm_folge_d) + '}']
    ausw_folge = random.randint(1, len(bel_vorschrift)) - 1

    a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                start_geom_folge * geom_folge_q ** (x - 1),
                bel_vorschrift[ausw_folge]]
Expand All
	@@ -192,23 +203,20 @@ def grenzwerte(nr, teilaufg):
    a_n_str = a_n_str_alle[auswahl_folgenart]
    grenzwert = limit(a_n, x, oo)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Bildungsvorschrift:',
               r'a_{n}~=~' + a_n_str]

    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne den Grenzwert der gegebenen Folge. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \lim \limits_{n \to \infty } ' + a_n_str + '~=~'
                       + latex(grenzwert) + r' \quad (2P) \\')
        i += 1
    return aufgabe, loesung


Aufgabe_1, Loesung_1 = folgen(1, [a, b, c])
Aufgabe_2, Loesung_2 = grenzwerte(2, [a])

# Angaben für den Test im pdf-Dokument
Expand All
	@@ -222,6 +230,7 @@ def grenzwerte(nr, teilaufg):
Art = 'HAK 20 - Folgen und Bildungsvorschrift'
Teil = 'Gruppe A'


# der Teil in dem die PDF-Datei erzeugt wird

def Hausaufgabenkontrolle():
