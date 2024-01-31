import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
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

def vektor_rational(vec,p):
    vec_p = [element*p for element in vec]
    print(vec_p)
    k = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
    if k == 3:
        pruefung = True
    else:
        pruefung = False
    print(pruefung)
    return pruefung

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
        loesung_vektor = [1/3,1/5,1/7]
        while vektor_rational(loesung_vektor,10) != True:
            xwert_1 = -1 * nzahl(1,3)
            ywert_1 = nzahl(3,8)
            xwert_2 = nzahl(1,3)
            ywert_2 = ywert_1 + nzahl(2,6)
            xwert_3 = xwert_2 + nzahl(1,3)
            ywert_3 = nzahl (2,8)

            A = np.array([[xwert_1 ** 2, xwert_1, 1],
                             [xwert_2 ** 2, xwert_2, 1],
                             [xwert_3 ** 2, xwert_3, 1]])

            b = np.array([ywert_1, ywert_2, ywert_3])
            loesung_vektor = slv(A, b)
        [x_1, x_2, x_3] = loesung_vektor
        fkt = x_1 * x**2 + x_2 * x + x_3
        fkt_str = gzahl(x_1) + 'x^2' + vorz_str(x_2) + 'x' + vorz_str(x_3)
        fkt_a = fkt*x
        fkt_a_str = gzahl(x_1) + 'x^3' + vorz_str(x_2) + 'x^2' + vorz_str(x_3) + 'x'

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
                   'Rechtecks auf dem Graphen von f.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['', f'Aufgabe_{nr}']
        grafiken_loesung = ['']
        # grafische Darstellung des Sachverhaltes
        xmax = solve(fkt, x)[1]
        Graph(fkt,xmax, xwert_2, ywert_2,f'Aufgabe_{nr}')

        if 'a' in teilaufg:
            punkte_aufg = 19
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}',''))
            grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}','',''))

            # Rekonstruktion der Funktion
            # Zeilen 1 bis 3 vom LGS:

            a1 = xwert_1 ** 2
            b1 = xwert_1
            c1 = 1
            d1 = ywert_1


            a2 = xwert_2 ** 2
            b2 = xwert_2
            c2 = 1
            d2 = ywert_2

            a3 = xwert_3 ** 2
            b3 = xwert_3
            c3 = 1
            d3 = ywert_3

            # Zeile 4 und 5 vom LGS:

            z4 = gzahl(a1) + '*II' + vorz_str(-1*a2) + '*I'
            a4 = 0
            b4 = a1 * b2 - a2 * b1
            c4 = a1 - a2
            d4 = a1 * d2 - a2 * d1

            z5 = gzahl(a1) + '*III' + vorz_str(-1*a3) + '*I'
            a5 = 0
            b5 = a1 * b3 - a3 * b1
            c5 = a1 - a3
            d5 = a1 * d3 - a3 * d1

            # Zeile 6 vom LGS:

            z6 = gzahl(b4) + '*III' + vorz_str(-1*b5) + '*II'
            b6 = 0
            c6 = b4 * c5 - b5 * c4
            d6 = b4 * d5 - b5 * d4

            # Lösungen des LGS:

            lsg_c = d6 / c6
            lsg_b = (d4 - (c4 * lsg_c)) / b4
            lsg_a = (d1 - (c1 * lsg_c) - (b1 * lsg_b)) / a1

            table2 = Tabular('c|c|c|c|c|c|c|c', row_height=1.2)
            table2.add_hline(2, 7)
            table2.add_row('Berechnung mit Gauß-Algorithmus','Nr.', 'Berechnung', 'a', 'b', 'c', 'lsg', '')
            table2.add_hline(2, 7)
            table2.add_row('','I', ' ', gzahl(a1), gzahl(b1), gzahl(c1), gzahl(d1), '(1P)')
            table2.add_row('', 'II', ' ', gzahl(a2), gzahl(b2), gzahl(c2), gzahl(d2), '(1P)')
            table2.add_row('', 'III', ' ', gzahl(a3), gzahl(b3), gzahl(c3), gzahl(d3), '(1P)')
            table2.add_hline(2, 7)
            table2.add_row('', 'I', ' ', gzahl(a1), gzahl(b1), gzahl(c1), gzahl(d1), '')
            table2.add_row('', 'II', z4, gzahl(a4), gzahl(b4), gzahl(c4), gzahl(d4), '(1P)')
            table2.add_row('', 'III', z5, gzahl(a5), gzahl(b5), gzahl(c5), gzahl(d5), '(1P)')
            table2.add_hline(2, 7)
            table2.add_row('', 'I', ' ', gzahl(a1), gzahl(b1), gzahl(c1), gzahl(d1), '')
            table2.add_row('', 'II', ' ', gzahl(a4), gzahl(b4), gzahl(c4), gzahl(d4), '')
            table2.add_row('', 'III', z6, ' ', gzahl(b6), gzahl(c6), gzahl(d6), '(1P)')
            table2.add_hline(2, 7)

            # Aufgaben und Lösungen
            aufgabe.append('Von einer Funktion 3. Grades sind die folgenden Punkte gegeben:  S( ' + gzahl(xwert_1) + ' | '
                           + gzahl(ywert_1) + ' ),  P( ' + gzahl(xwert_2) +  r' | '
                           + gzahl(ywert_2) + ' ) und Q( ' + gzahl(xwert_3)
                           + ' | ' + gzahl(ywert_3) + ' ) \n\n')
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Funktionsgleichung von f. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Die~allgemeine~Funktionsgleichung~lautet:'
                           + r'~f(x)~=~ax^2~+~bx~+~c \quad (1P) } \\'
                           + r' \mathrm{aus~den~gegebenen~Punkten~folgt:} \quad '
                           + r' \mathrm{I:~f(' + gzahl(xwert_1) + ')~=~' + gzahl(ywert_1) + r' \quad \to \quad '
                           + gzahl(xwert_1**2) + 'a' + vorz_str(xwert_1) + 'b + c ~=~' + gzahl(ywert_1)
                           + r' \quad (2P)} \\ \mathrm{II:~f(' + gzahl(xwert_2) + ')~=~' + gzahl(ywert_2)
                           + r' \quad \to \quad ' + gzahl(xwert_2**2) + 'a' + vorz_str(xwert_2) + 'b + c ~=~'
                           + gzahl(ywert_2) + r' \quad (2P)} \\ \mathrm{III:~f(' + gzahl(xwert_3) + ')~=~'
                           + gzahl(ywert_3) + r' \quad \to \quad ' + gzahl(xwert_3**2) + 'a' + vorz_str(xwert_3)
                           + 'b + c ~=~' + gzahl(ywert_3) + r' \quad (2P) }')
            loesung.append(table2)
            loesung.append(r' \mathrm{aus~III~folgt:~' + gzahl(c6) + '~c~=~' + gzahl(d6) + r' \quad \vert \div '
                           + vorz_str_minus(c6) + r' \quad \to \quad c~=~' + latex(lsg_c) + r' \quad (2P) } \\'
                           + r' \mathrm{aus~II~folgt:~' + gzahl(b4) + r'b~' + vorz_str(c4)
                           + r' \cdot ~' + vorz_str_minus(lsg_c) + '~=~' + gzahl(d4) + r' \quad \vert ~-~'
                           + vorz_str_minus(c4 * lsg_c) + r' \quad \vert \div ' + vorz_str_minus(b4)
                           + r' \quad \to \quad b~=~' + latex(lsg_b) + r' \quad (2P) } \\'
                           + r' \mathrm{aus~I~folgt:~' + gzahl(a1) + r'~a~' + vorz_str(b1) + r' \cdot '
                           + vorz_str_minus(lsg_b) + vorz_str(c1) + r' \cdot ' + vorz_str_minus(lsg_c) + '~=~'
                           + gzahl(d1) + r' \quad \vert ~-~' + vorz_str_minus(b1 * lsg_b + c1 * lsg_c)
                           + r' \quad \vert \div ' + vorz_str_minus(a1) + r' \quad \to \quad a~=~' + latex(lsg_a)
                           + r' \quad (2P) } \\')
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 15
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # zwischenrechnungen
            fkt_1_a = 3 * x_1 * (x ** 2) + 2 * x_2 * x + x_3
            fkt_1_a_str = gzahl(3 * x_1) + 'x^2' + vorz_str(2 * x_2) + 'x' + vorz_str(x_3)
            fkt_1_a_p = Rational(2 * x_2, 3 * x_1)
            fkt_1_a_p2 = Rational(x_2, 3 * x_1)
            fkt_1_a_q = Rational(x_3, 3 * x_1)
            fkt_1_a_pq = 'x^2' + vorz_str(fkt_1_a_p) + 'x' + vorz_str(fkt_1_a_q)
            fkt_1_a_sqrt_disk = N(sqrt(fkt_1_a_p2 ** 2 - fkt_1_a_q), 3)
            fkt_1_a_lsg = solve(fkt_1_a, x)
            fkt_2_a = 6 * x_1 * x + 2 * x_2
            fkt_2_a_xo = N(fkt_2_a.subs(x,re(fkt_1_a_lsg[1])),3)
            fkt_2_a_str = gzahl(6 * x_1) + 'x' + vorz_str(2*x_2)
            flaeche = N(fkt_a.subs(x,re(fkt_1_a_lsg[1])),3)

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + r') Wie muss x gewählt werden, damit die Rechtecksfläche maximal wird,'
                                              r' wenn')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{ist.}')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrm{geg: \quad f(x)~=~' + fkt_str
                           + r' \quad ges: x~für~A_{max} \quad (1P) } \\'
                           + r' \mathrm{es~gilt: \quad HB.: \quad A~=~x \cdot y \quad und \quad NB.: \quad f(x)~=~'
                           + fkt_str + r' \quad (2P)}  \\'
                           + r' \to \quad \mathrm{HB.: \quad A(x)~=~x \cdot (' + fkt_str + r')~=~ ' + fkt_a_str
                           + r' \quad (1P) } \\ \mathrm{A^{ \prime }(x)~=~' + fkt_1_a_str
                           + r' \quad und \quad A^{ \prime \prime } ~=~' + fkt_2_a_str + r' \quad (2P) } \\'
                           + r' \mathrm{A^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + fkt_1_a_str + r' \quad \vert \div '
                           + vorz_str_minus(3*x_1) + r' \quad \to \quad 0~=~' + fkt_1_a_pq + r' \quad (2P) }\\'
                           + r' \mathrm{ x_{1/2} ~=~ - \frac{' + gzahl(fkt_1_a_p) + r'}{2} \pm \sqrt{ \Big( \frac{'
                           + gzahl(fkt_1_a_p) + r'}{2} \Big) ^2 -' + vorz_str_minus(fkt_1_a_q) + '} ~=~'
                           + gzahl(-1*fkt_1_a_p2) + r' \pm ' + gzahl(fkt_1_a_sqrt_disk) + r' \quad (2P) } \\'
                           + r' \mathrm{x_1 ~=~' + gzahl(N(re(fkt_1_a_lsg[0]),3)) + r' \quad und \quad x_2 ~=~'
                           + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r' \quad (2P) } \\ \mathrm{A^{ \prime \prime }('
                           + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~' + gzahl(6*x_1) + r' \cdot '
                           + vorz_str_minus(N(re(fkt_1_a_lsg[1]),3)) + vorz_str(2*x_2) + r'~=~'
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
            aufgabe.append(str(teilaufg[i]) + ') Berechne den maximalen Flächeninhalt. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad A(' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~'
                           + gzahl(x_1) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^3'
                           + vorz_str(x_2) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^2'
                           + vorz_str(x_3) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3))
                           + ') ~=~' + gzahl(flaeche) + r' \quad (2P) \\')
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
    Art = 'Test I (2. Semester)'
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


anzahl_Arbeiten = 2
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)
