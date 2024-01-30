import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.gridspec as grid

from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from sympy.plotting import plot as symplot

from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def vorz(k):
    if k == -1:
        return '-'
    elif k == 1:
        return '+'
    else:
        pass

def vorz_str(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

def vorz_str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def Graph(fkt, xmax, xwert_p, ywert_p, name):
        fig, ax = plt.subplots()
        fig.canvas.draw()
        fig.tight_layout()
        plt.grid()
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
        plt.annotate(r'$ P( x \vert y ) $', xy=(xwert_p, ywert_p),
                     xycoords='data', xytext=(+10, +10), textcoords='offset points', fontsize=16)
        xwerte = np.arange(0, xmax, 0.01)
        ywerte = [fkt.subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte)
        plt.plot([0, xwert_p], [ywert_p, ywert_p])
        plt.plot([xwert_p, xwert_p], [ywert_p, 0])
        plt.scatter([xwert_p, ], [ywert_p, ], 50, color='blue')
        return plt.savefig(name, dpi=200)


    def extremalproblem_01(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        sp_yachse = nzahl(3,8)
        steigung = -1 * nzahl(1,10)/4
        fkt = steigung * x + sp_yachse
        fkt_str = gzahl(steigung) + 'x' + vorz_str(sp_yachse)
        xmax = -1*sp_yachse/steigung

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
                   'Rechtecks auf dem Graphen von f.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['','']
        grafiken_loesung = []

        if 'a' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes
            xwert_p = int(xmax/3 + 0.5)
            ywert_p = fkt.subs(x,xwert_p)
            Graph(fkt, xmax, xwert_p,ywert_p,f'Aufgabe_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Wie muss x gewählt werden, damit die Rechtecksfläche maximal wird,'
                                              r' wenn')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{ist.}')
            loesung.append(str(teilaufg[i]) + r') \quad geg: f(x)~=~' + fkt_str
                           + r' \quad ges: \mathrm{x,y~für~A_{max}} \quad (1P) \hspace{20em} \\'
                           + r' \mathrm{es~gilt: \quad HB.: A~=~x \cdot y \quad und \quad NB.:f(x)~=~'
                           + fkt_str + r' \quad (2P) } \\'
                           + r' \\')
            i += 1

        if 'a' and 'b' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Berechne den maximalen Flächeninhalt. ')
            loesung.append(str(teilaufg[i]) + r') \quad \\')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def extremalproblem_02(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        xwert_s = nzahl(5,10)
        ywert_s = nzahl(5, 10)
        ywert = ywert_s - nzahl(1,ywert_s-1)
        faktor = (ywert-ywert_s)/xwert_s**2
        fkt = faktor*(x**2) - 2*faktor*xwert_s*x + ywert
        fkt_str = gzahl(faktor) + 'x^2' + vorz_str(-2*faktor*xwert_s) + 'x' + vorz_str(ywert)
        if abs(faktor) == 1:
            fkt_str = vorz(faktor) + 'x^2' + vorz_str(-2 * faktor * xwert_s) + 'x' + vorz_str(ywert)
        fkt_a = faktor*(x**3) - 2*faktor*xwert_s*(x**2) + ywert * x
        fkt_a_str = gzahl(faktor) + 'x^3' + vorz_str(-2*faktor*xwert_s) + 'x^2' + vorz_str(ywert) + 'x'

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
                   'Rechtecks auf dem Graphen von f.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['', f'Aufgabe_{nr}']
        grafiken_loesung = ['']
        # grafische Darstellung des Sachverhaltes
        xwert_p0 = nzahl(1, 3)
        ywert_p0 = N(fkt.subs(x, xwert_p0),4)
        xwert_p1 = -1 * nzahl(1, 3)
        ywert_p1 = N(fkt.subs(x, xwert_p1),4)
        xwert_p2 = xwert_p0 + nzahl(1, 3)
        ywert_p2 = N(fkt.subs(x, xwert_p2),4)
        xmax = solve(fkt, x)[1]
        Graph(fkt,xmax, xwert_p0, ywert_p0,f'Aufgabe_{nr}')

        if 'a' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}',''))
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append('Vom Graphen sind folgende Punkte gegeben:  S( ' + gzahl(xwert_p1) + ' | '
                           + gzahl(ywert_p1) + ' ),  P( ' + gzahl(xwert_p0) +  r' | '
                           + gzahl(ywert_p0) + ' ) und Q( ' + gzahl(xwert_p2)
                           + ' | ' + gzahl(ywert_p2) + ' ) \n\n')
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Funktionsgleichung von f. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad (2P) \\')
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 15
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # zwischenrechnungen
            fkt_1_a = 3 * faktor * (x ** 2) - 4 * faktor * xwert_s * (x) + ywert
            fkt_1_a_str = gzahl(3 * faktor) + 'x^2' + vorz_str(-4 * faktor * xwert_s) + 'x' + vorz_str(ywert)
            fkt_1_a_p = Rational(-4 * xwert_s, 3)
            fkt_1_a_p2 = Rational(-2 * xwert_s, 3)
            fkt_1_a_q = Rational(ywert, 3 * faktor)
            fkt_1_a_pq = 'x^2' + vorz_str(fkt_1_a_p) + 'x' + vorz_str(fkt_1_a_q)
            fkt_1_a_sqrt_disk = N(sqrt(fkt_1_a_p2 ** 2 - fkt_1_a_q), 3)
            fkt_1_a_lsg = solve(fkt_1_a, x)
            fkt_2_a = 6 * faktor * (x) - 4 * faktor * xwert_s
            fkt_2_a_xo = N(fkt_2_a.subs(x,re(fkt_1_a_lsg[1])),3)
            fkt_2_a_str = gzahl(6 * faktor) + 'x' + vorz_str(-4 * faktor * xwert_s)
            flaeche = N(fkt_a.subs(x,re(fkt_1_a_lsg[1])),3)

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Wie muss x gewählt werden, damit die Rechtecksfläche maximal wird,'
                                              r' wenn')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{ist.}')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrm{geg: \quad f(x)~=~' + fkt_str
                           + r' \quad ges: x,y~für~A_{max} \quad (1P) } \\'
                           + r' \mathrm{es~gilt: \quad HB.: \quad A~=~x \cdot y \quad und \quad NB.: \quad f(x)~=~'
                           + fkt_str + r' \quad (2P)}  \\'
                           + r' \to \quad \mathrm{HB.: \quad A(x)~=~x \cdot (' + fkt_str + r')~=~ ' + fkt_a_str
                           + r' \quad (1P) } \\ \mathrm{A^{ \prime }(x)~=~' + fkt_1_a_str
                           + r' \quad und \quad A^{ \prime \prime } ~=~' + fkt_2_a_str + r' \quad (2P) } \\'
                           + r' \mathrm{A^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + fkt_1_a_str + r' \quad \vert \div '
                           + vorz_str_minus(3*faktor) + r' \quad \to \quad 0~=~' + fkt_1_a_pq + r' \quad (2P) }\\'
                           + r' \mathrm{ x_{1/2} ~=~ - \frac{' + gzahl(fkt_1_a_p) + r'}{2} \pm \sqrt{ \Big( \frac{'
                           + gzahl(fkt_1_a_p) + r'}{2} \Big) ^2 -' + vorz_str_minus(fkt_1_a_q) + '} ~=~'
                           + gzahl(-1*fkt_1_a_p2) + r' \pm ' + gzahl(fkt_1_a_sqrt_disk) + r' \quad (2P) } \\'
                           + r' \mathrm{x_1 ~=~' + gzahl(N(re(fkt_1_a_lsg[0]),3)) + r' \quad und \quad x_2 ~=~'
                           + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r' \quad (2P) } \\ \mathrm{A^{ \prime \prime }('
                           + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~' + gzahl(6*faktor) + r' \cdot '
                           + vorz_str_minus(N(re(fkt_1_a_lsg[1]),3)) + vorz_str(-4*faktor*xwert_s) + r'~=~'
                           + gzahl(fkt_2_a_xo) + r'~<0 \quad \to HP \quad (3P) } \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' and 'c' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Berechne den maximalen Flächeninhalt. ')
            loesung.append(str(teilaufg[i]) + r') \quad A(' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~'
                           + gzahl(faktor) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^3'
                           + vorz_str(-2*faktor*xwert_s) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^2'
                           + vorz_str(faktor*(xwert_s**2)+ywert_s) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3))
                           + ') ~=~' + gzahl(flaeche) + r' \quad (2P) \\\\')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def rekonstruktion(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        faktor = -1 * nzahl(2,10)/5
        while faktor == -1:
            faktor = -1 * nzahl(1, 10)/5
        nst = nzahl(5,8)
        xvers = nzahl(1,3)
        yvers = nzahl(2,6)  * (-1*faktor)

        # Funktionen und Ableitungen

        fkt = collect(expand(faktor*((x + xvers)*(x + xvers - nst) * (x + xvers + nst)) + yvers),x)
        fkt_str = (gzahl(faktor) + 'x^(3)' + vorz_str(3*faktor*xvers) + 'x^(2)'
                   + vorz_str(3*faktor*(xvers**2)-faktor*(nst**2)) + 'x'
                   + vorz_str(-1*faktor*(nst**2)*xvers + faktor*(xvers**3)+yvers))
        fkt_a = collect(expand((faktor*((x + xvers)*(x + xvers - nst) * (x + xvers + nst)) + yvers)*x),x)
        fkt_a_str = (gzahl(faktor) + 'x^(4)' + vorz_str(3*faktor*xvers) + 'x^(3)'
                     + vorz_str(3*faktor*(xvers**2)-faktor*(nst**2)) + 'x^2'
                     + vorz_str(-1*faktor*(nst**2)*xvers + faktor*(xvers**3)+yvers) + 'x')
        fkt_1_a = diff(fkt_a,x)
        fkt_1_a_str = (gzahl(4*faktor) + 'x^(3)' + vorz_str(9*faktor*xvers) + 'x^(2)'
                   + vorz_str(6*faktor*(xvers**2)-2*faktor*(nst**2)) + 'x'
                   + vorz_str(-1*faktor*(nst**2)*xvers + faktor*(xvers**3)+yvers))
        fkt_2_a = diff(fkt_a,x,2)
        fkt_2_a_str = (gzahl(12*faktor) + 'x^(2)' + vorz_str(18*faktor*xvers) + 'x'
                       + vorz_str(6*faktor*(xvers**2)-2*faktor*(nst**2)))
        fkt_1_a_x0 =  solve(fkt_1_a, x)
        print(fkt_1_a_x0)
        # Werte für Horner-Schema
        fkt_1_a_a1 = gzahl(4*faktor)
        fkt_1_a_a2 = gzahl(9*faktor*xvers)
        fkt_1_a_a3 = gzahl(6*faktor*(xvers**2)-2*faktor*(nst**2))
        fkt_1_a_a4 = gzahl(6*faktor*(xvers**2)-2*faktor*(nst**2))

        # print(fkt), print(fkt_str), print(xmax), print(fkt_a), print(fkt_a_str), print(fkt_1_a), print(fkt_1_a_str), print(fkt_2_a), print(fkt_2_a_str), symplot(fkt)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
                   'Rechtecks auf dem Graphen von f.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['', f'Aufgabe_{nr}']
        grafiken_loesung = ['']

        # grafische Darstellung des Sachverhaltes
        xmax = nst - xvers
        xwert_p = int(xmax / 3 + 0.5)
        ywert_p = fkt.subs(x, xwert_p)
        Graph(fkt, xmax, xwert_p, ywert_p, f'Aufgabe_{nr}')

        if 'a' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') ')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrmn{} \\')
            i += 1

        if 'b' in teilaufg:

            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

             # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Wie muss x gewählt werden, '
                                              r'damit die Rechtecksfläche maximal wird, wenn')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{ist.}')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrmn{geg: \quad f(x)~=~' + fkt_str
                           + r' \quad ges: x,y~für~A_{max} \quad (1P) \hspace{10em} \\'
                           + r'es~gilt: \quad HB.: \quad A~=~x \cdot y \quad und \quad NB.: \quad f(x)~=~'
                           + fkt_str + r' \quad (2P) \\'
                           + r' \to \quad HB.: \quad A(x)~=~x \cdot (' + fkt_str + r')~=~ ' + fkt_a_str
                           + r' \quad (1P) \\ A^{ \prime }(x)~=~' + fkt_1_a_str
                           + r' \quad und \quad A^{ \prime \prime } ~=~' + fkt_2_a_str + r' \quad (2P) \\'
                           + r'A^{ \prime}(x) ~=~0 \quad \to \quad 0~=~' + fkt_1_a_str + r''
                           + r'} \\')
            i += 1
        if 'b' and 'c' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + ') Berechne den maximalen Flächeninhalt des Rechtecks. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad \\')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [extremalproblem_02(1, ['a', 'b', 'c'])]

    # erstellen der Tabelle zur Punkteübersicht
    Punkte = (sum(liste_punkte[1:]))
    liste_bez.append('Summe')
    liste_punkte.append(str(Punkte))
    anzahl_spalten = len(liste_punkte)
    liste_ergebnis_z1 = ['erhaltene']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z1.append('')
    liste_ergebnis_z2 = ['Punkte']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z2.append('')

    spalten = '|'
    for p in liste_punkte:
        spalten += 'c|'

    table2 = Tabular(spalten, row_height=1.2)
    table2.add_hline()
    table2.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben'),))
    table2.add_hline()
    table2.add_row(liste_bez)
    table2.add_hline()
    table2.add_row(liste_punkte)
    table2.add_hline()
    table2.add_row(liste_ergebnis_z1)
    table2.add_row(liste_ergebnis_z2)
    table2.add_hline()

    # Angaben für den Test im pdf-Dokument
    Datum = datetime.date.today().strftime('%d.%m.%Y')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = '8. Hausaufgabenkontrolle'
    Titel = 'Extremalprobleme und Rekonstruktion von Funktionen'

    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))  # fügt das Package 'amsfonts' hinzu, für das \mathbb{R} für reelle Zahlen
        # erste Seite
        table1 = Tabular('|c|c|c|c|c|c|', row_height=1.2)
        table1.add_row((MultiColumn(6, align='c', data=MediumText(bold('Torhorst - Gesamtschule'))),))
        table1.add_row((MultiColumn(6, align='c', data=SmallText(bold('mit gymnasialer Oberstufe'))),))
        table1.add_hline()
        table1.add_row('Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:', 'Art:')
        table1.add_hline()
        table1.add_row(Klasse, Fach, Kurs, Lehrer, Datum, Art)
        table1.add_hline()
        Aufgabe.append(table1)
        Aufgabe.append(' \n\n\n\n')
        Aufgabe.append(LargeText(bold(f' {Titel} \n\n')))
        for aufgabe in aufgaben:
            k = 0
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][k], width='200px')
                else:
                    Aufgabe.append(elements)
                k +=1

        Aufgabe.append('\n\n')
        Aufgabe.append(table2)

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mKontrolle erstellt\033[0m')

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            k = 0
            for elements in loesung[1]:
                k += 1
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Loesung.append(elements)
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='200px')
                else:
                    Loesung.append(elements)

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 1
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)
