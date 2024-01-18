import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *

# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

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

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def vorz_str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def vorz_Str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return r' \Big( ' + latex(k) + r' \Big)'
    else:
        return latex(k)

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def kurvendiskussion_01(nr, teilaufg):
        i = 0
        # Berechnung der Nullstellen und des Faktors
        nst_1 = zzahl(1, 5)
        nst_2 = nst_1 + nzahl(2, 8) / 2
        nst_3 = nst_1 - nzahl(2, 8) / 2
        while nst_3 == 0:
            nst_3 = nst_1 - nzahl(2, 8) / 2
        faktor = zzahl(3, 8) / 2
        # Aufstellen der Funktionsgleichung
        fkt = collect(expand(faktor * (x - nst_1) * (x - a) * (x - nst_3)),x)
        # Koeffizienten der Funktion
        fkt_a3 = faktor
        fkt_a2 = -1* (faktor*a + faktor*(nst_1 + nst_3))
        fkt_a1 = (faktor*(nst_1 + nst_3)*a + faktor*nst_1*nst_3)
        fkt_a0 = -1*faktor*nst_1*nst_3*a

        # Koeffizienten der Funktion als String und der richtigen Darstellung
        fkt_a3_str = latex(faktor)
        if faktor < 0:
            fkt_a2_str = '+(' + latex(abs(faktor)) + r' \cdot a ' + vorz_str(-1*faktor*(nst_1 + nst_3)) + ')'
        else:
            fkt_a2_str = '-(' + latex(abs(faktor)) + r' \cdot a ' + vorz_str(faktor*(nst_1 + nst_3)) + ')'

        if faktor*(nst_1 + nst_3) < 0:
            fkt_a1_str = '-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(-1*faktor * nst_1 * nst_3) + ')'
        else:
            fkt_a1_str = '+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(faktor * nst_1 * nst_3) + ')'

        fkt_a0_str = vorz_str(-1*faktor*nst_1*nst_3) + r' \cdot a'

        fkt_str = fkt_a3_str + r' \cdot x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str + r' \cdot x ~' + fkt_a0_str

        print(fkt), print(fkt_str)

        if nst_1 < 0:
            db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}'
        else:
            db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > ' + latex(nst_1) + r'}'

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:']
        aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad ' + db_bereich)
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']



        if 'a' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grenzwert_neg = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                           + latex(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} '
                           + fkt_str + '~=~' + latex(grenzwert_neg) + r' \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            fkt_a3_str_neg = latex(-1*faktor)
            if faktor * (nst_1 + nst_3) > 0:
                fkt_a1_str_neg = ('-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                  + vorz_str(-1*faktor * nst_1 * nst_3) + ')')
            else:
                fkt_a1_str_neg = ('+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                  + vorz_str(faktor * nst_1 * nst_3) + ')')
            fkt_sym = (fkt_a3_str_neg + r' \cdot x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str_neg
                       + r' \cdot x ~' + fkt_a0_str)
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad f(-x)~=~' + fkt_sym
                                                     + r' \neq  f(x)  \neq -f(x) \\'
                                                     + r'\mathrm{nicht~symmetrisch} \quad (3P) \\'))
            i += 1
        if 'c' in teilaufg:
            punkte_aufg = 15
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            # hier werden die Koeffizenten für das Hornerschema berechnet
            fkt_b2 = nst_1 * faktor
            fkt_c2 = -1 * faktor * a - faktor * nst_3
            fkt_b1 = -1 * faktor * nst_1 * a - faktor * nst_1 * nst_3
            fkt_c1 = faktor * nst_3 * a
            fkt_b0 = faktor * nst_1 * nst_3 * a
            fkt_partial = faktor * x**2 + fkt_c2 *x + fkt_c1

            # hier werden die Koeffizenten als String für das Hornerschema berechnet
            if faktor < 0:
                fkt_c2_str = '+(' + latex(-1*faktor) + r' \cdot a' + vorz_str(-1*faktor*nst_3) + r') \cdot x'
            else:
                fkt_c2_str = '-(' + latex(faktor) + r' \cdot a' + vorz_str(faktor*nst_3) + r') \cdot x'
            fkt_c1_str = vorz_str(faktor*nst_3) + r' \cdot a'
            fkt_p = -1*a - nst_3    # -(a+x_3)
            fkt_q = nst_3 * a
            fkt_disk = ((fkt_p/2)**2)-fkt_q
            fkt_p_str = '-(a' + vorz_str(nst_3) + ')'
            fkt_q_str = vorz_str(nst_3) + r' \cdot a'
            fkt_partial_str = latex(faktor) + r' \cdot x^2' + fkt_c2_str + fkt_c1_str
            fkt_pq_str = 'x^2' + fkt_p_str + r' \cdot x' + fkt_q_str
            fkt_disk_str = r' \frac{a^2' + vorz_str(-1*2*nst_3) + r' \cdot a' + vorz_str(nst_3**2) + '}{4}'

            table2 = Tabular('c c|c|c|c', row_height=1.2)
            table2.add_row('',fkt_a3,latex(collect(fkt_a2,a)), latex(collect(fkt_a1,a)), latex(collect(fkt_a0,a)))
            table2.add_hline(2, 5)
            table2.add_row('Partialpolynom mit Horner Schema berechnen: ',' ', latex(collect(fkt_b2,a)), latex(collect(fkt_b1,a)), latex(collect(fkt_b0,a)))
            table2.add_hline(2, 5)
            table2.add_row('',fkt_a3, latex(collect(fkt_c2,a)), latex(collect(fkt_c1,a)), '0')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                                                     + fkt_str + r' \quad (1P) \\ \mathrm{durch~probieren:~x_1~=~}'
                                                     + vorz_str(nst_1) + r' \quad (1P) \\'
                                                     + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1)
                                                     + r')~= \\ =~' + fkt_partial_str + r' \quad (4P)'))
            loesung.append(table2)
            loesung.append('0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + vorz_str_minus(faktor) +
                           r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2P) \\'
                           r' x_{2/3}~=~ - \frac{' + fkt_p_str + r'}{2} \pm \sqrt{ \Big(' +
                           r' \frac{' + fkt_p_str + r'}{2} \Big)^2-(' + latex(fkt_q) +
                           r')} ~=~ ' + latex(-1*fkt_p/2) + r' \pm \sqrt{'
                           + fkt_disk_str + r' } \quad (4P) \\ x_{2/3}~=~' + latex(-1*fkt_p/2) + r' \pm ('
                           + latex((a-nst_3)/2) + r') \quad \to \quad x_2~=~' + latex(nst_3)
                           + r' \quad \mathrm{und} \quad x_3~=~a \quad (3P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1
        if 'd' in teilaufg:
            punkte_aufg = 19
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            fkt_1 = collect(diff(fkt,x,1),x)
            fkt_2 = collect(diff(fkt,x,2),x)
            fkt_3 = collect(diff(fkt,x,3),x)
            x_12_fkt_1 = solve(fkt_1, x)
            x_1_fkt_1 = x_12_fkt_1[0]
            x_2_fkt_1 = x_12_fkt_1[1]

            # Koeffizienten der ersten Ableitung
            fkt_1_a2 = 3*faktor
            fkt_1_a1 = (-2*faktor*a -2*faktor*(nst_1 + nst_3))
            fkt_1_a0 = (faktor*(nst_1+nst_3)*a+faktor*nst_1*nst_3)
            fkt_1_p = (-2/3*a -2/3*(nst_1*nst_3))
            fkt_1_q = (1/3*(nst_1+nst_3)*a + 1/3*nst_1*nst_3)

            fkt_1 = fkt_1_a2 * x**2 + fkt_1_a1 * x + fkt_1_a0

            # Koeffizienten der ersten Ableitung als string

            fkt_1_a2_str = latex(3*faktor)
            if faktor < 0:
                fkt_1_a1_str = '+(' + latex(-2*faktor) + r' \cdot a' + vorz_str(-2*faktor*(nst_1+nst_3)) + ')'
            else:
                fkt_1_a1_str = '-(' + latex(2*faktor) + r' \cdot a' + vorz_str(2*faktor*(nst_1+nst_3)) + ')'

            if faktor * (nst_1 + nst_3) < 0:
                fkt_1_a0_str = ('-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
            else:
                fkt_1_a0_str = ('+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                + vorz_str(faktor * nst_1 * nst_3) + ')')
            # p und q in der pq-Formel
            fkt_1_p_str = r'-( \frac{2}{3} \cdot a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')'
            if (nst_1 + nst_3) < 0:
                fkt_1_q_str = ('-(' + latex(Rational(-1*(nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational(-1*(nst_1 * nst_3),3)) + ')')
                fkt_1_q2_str = (latex(Rational((nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)))
            else:
                fkt_1_q_str = ('+(' + latex(Rational(nst_1 + nst_3,3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)) + ')')
                fkt_1_q2_str = (latex(Rational(nst_1 + nst_3, 3)) + r' \cdot a'
                               + vorz_str(Rational((nst_1 * nst_3), 3)))

            # p und q in umgeformter pq-Formel
            fkt_1_p2_str = r'( \frac{2}{3} \cdot a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')^2'
            fkt_1_p3_str = r' \frac{1}{3} \cdot a' + vorz_str(Rational((nst_1 + nst_3), 3))
            if (nst_1 + nst_3) < 0:
                fkt_1_q3_str = (r'+ \frac{4 \cdot (' + latex(Rational(abs(nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational(-1*(nst_1 * nst_3),3)) + ') }{4}')
            else:
                fkt_1_q3_str = (r'- \frac{4 \cdot ('+ latex(Rational(nst_1 + nst_3,3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)) + ')}{4}')
            # Diskriminante der Wurzel
            fkt_1_disk_str = (r' \frac{1}{9} \cdot ((a' + vorz_str(-1*(nst_1+nst_3)) + r')^2'
                              + vorz_str(-4*nst_1*nst_3) + ')')

            fkt_1_str = fkt_1_a2_str + 'x^2' + fkt_1_a1_str + 'x' + fkt_1_a0_str
            fkt_1_pq_str = 'x^2' + fkt_1_p_str + r' \cdot x' + fkt_1_q_str
            fkt_2_str = latex(6*faktor) + 'x' + fkt_1_a1_str
            fkt_3_str = latex(6*faktor)
            fkt_1_x1 = fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str + r'}'
            fkt_1_x2 = fkt_1_p3_str + r' - \sqrt{' + fkt_1_disk_str + r'}'

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extremstellen der Funktion f und deren Art'
                                                    ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \quad (1P) \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad \mathrm{und} \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str
                           + r' \quad (2P) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_1_str + r' \vert ~ \div ' + vorz_str_minus(3 * faktor) + r' \quad (1P) \\'
                           r'0~=~ ' + fkt_1_pq_str + r' \quad (1P) \\' + r' x_{1/2}~=~ - \frac{'
                           + fkt_1_p_str + r'}{2} \pm \sqrt{ \Big(' + r' \frac{'
                           + fkt_1_p_str + r'}{2} \Big)^2-(' + fkt_1_q2_str + r')} \quad (2P) \\ =~ '
                           + fkt_1_p3_str + r' \pm \sqrt{' + r' \frac{' + fkt_1_p2_str
                           + r'}{4}' + fkt_1_q3_str + r'} ~=~' + fkt_1_p3_str + r' \pm \sqrt{' + fkt_1_disk_str
                           + r'} \quad (4P) \\ x_1~=~' + fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{und} \quad x_2~=~' + fkt_1_p3_str + r' - \sqrt{'
                           + fkt_1_disk_str + r'}  \quad (2P) \\'
                           + r'f^{ \prime \prime } (x_2) ~=~' + latex(6*faktor)
                           + r' \cdot \Big( ' + fkt_1_x1 + r' \Big) ' + fkt_1_a1_str
                           + r' \quad (1P) \\ ~=~ + \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{>~0} \quad \to TP \quad (2P) \\ f^{ \prime \prime } (x_2) ~=~'
                           + latex(6 * faktor) + r' \cdot \Big( ' + fkt_1_x2
                           + r' \Big) ' + fkt_1_a1_str + r' \quad (1P) \\ ~=~ - \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{<~0} \quad \to HP \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'e' in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            if faktor < 0:
                fkt_1_a1_str = '+(' + latex(-2*faktor) + r' \cdot a' + vorz_str(-2*faktor*(nst_1+nst_3)) + ')'
            else:
                fkt_1_a1_str = '-(' + latex(2*faktor) + r' \cdot a' + vorz_str(2*faktor*(nst_1+nst_3)) + ')'

            if faktor < 0:
                fkt_1_a1_str_neg = '-(' + latex(-2 * faktor) + r' \cdot a' + vorz_str(-2 * faktor * (nst_1 + nst_3)) + ')'
            else:
                fkt_1_a1_str_neg = '+(' + latex(2 * faktor) + r' \cdot a' + vorz_str(2 * faktor * (nst_1 + nst_3)) + ')'
            xwert_wendepunkt = r' \frac{1}{3} \cdot a' + vorz_str(Rational((nst_1+nst_3),3))
            fkt_2_str = latex(6*faktor) + 'x' + fkt_1_a1_str
            fkt_3_str = latex(6*faktor)

            aufgabe.append(str(liste_teilaufg[i]) + ') Überprüfe rechnerisch auf Wendepunkte der Funktion f '
                                                    'mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_2_str + r' \quad \vert ~' + fkt_1_a1_str_neg + r' \quad \vert \div '
                           + vorz_str_minus(6 * faktor) + r' \quad (1P) \\ x_1~=~ \frac{1}{3} a'
                           + vorz_str(Rational((nst_1+nst_3),3))
                           + r' \quad (1P) \quad \to \quad f^{ \prime \prime \prime }(' + xwert_wendepunkt
                           + r') ~=~ ' + latex(6*faktor) + r' \quad \neq 0 \quad \to \quad Wendepunkt \quad (3P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'f' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            wert_a_wp = random.randint(1,5)
            xwert_wp = Rational((wert_a_wp + nst_1 + nst_3),3)
            xwert_wendepunkt = r' \frac{1}{3} \cdot a' + vorz_str(Rational((nst_1 + nst_3), 3))
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen den Wert von a,'
                                                    f' bei dem der Wendepunkt an der Stelle x = {xwert_wp} ist. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad ' + latex(xwert_wp) + '~=~' + xwert_wendepunkt
                                                     + r' \quad \vert ~' + vorz_str(Rational(-1 * (nst_1 + nst_3), 3))
                                                     + r' \quad \vert \cdot 3 \quad \to \quad a~=~'
                                                     + str(wert_a_wp) + r' \quad (3P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        return [aufgabe, loesung]

    def kurvendiskussion_02(nr, teilaufg):
        i = 0
        # Berechnung der Nullstellen und des Faktors
        faktor = zzahl(1, 5)
        faktor_1 = -1*nzahl(5,10)/2
        faktor_2 = zzahl(1,2)
        if faktor_1%1 == 0:
            faktor_3 = nzahl(2,5)+0.5
        else:
            faktor_3 = nzahl(3,5)
        while faktor_1 + faktor_2 + faktor_3 == 0:
            faktor_1 = -1 * nzahl(5, 10) / 2
            faktor_2 = zzahl(1,2)
            if faktor_1 % 1 == 0:
                faktor_3 = nzahl(2, 5) + 0.5
            else:
                faktor_3 = nzahl(3, 5)

        nst_1_str = latex(faktor_1) + 'a'
        if faktor_2 == 1:
            nst_2_str = 'a'
            nst_2_str_neg = '-a'
        elif faktor_2 == -1:
            nst_2_str = '-a'
            nst_2_str_neg = '+a'
        else:
            nst_2_str = gzahl(faktor_2) + 'a'
            if int(gzahl(-1 * faktor_2)) > 0:
                nst_2_str_neg = f'+{gzahl(-1 * faktor_2)}a'
            else:
                nst_2_str_neg = f'{gzahl(-1 * faktor_2)}a'
        nst_3_str = latex(faktor_3) + 'a'

        # Aufstellen der Funktionsgleichung
        fkt = collect(expand(faktor * (x - faktor_1 * a) * (x - faktor_2 * a) * (x - faktor_3 * a)),x)

        # Koeffizienten der Funktion
        fkt_a3 = faktor
        fkt_a2 = -1*faktor * (faktor_1 + faktor_2 + faktor_3)
        fkt_a1 = faktor*(faktor_1*faktor_2 + faktor_2*faktor_3 + faktor_1*faktor_3)
        fkt_a0 = -1*faktor*faktor_1*faktor_2*faktor_3

        fkt_str = (latex(fkt_a3) + r' \cdot x^3 ~' + vorz_str(fkt_a2) + r'a \cdot x^2 ~' + vorz_str(fkt_a1)
                   + r'a^2 \cdot x ~' + vorz_str(fkt_a0) + r'a^3')

        print(fkt), print(fkt_str)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:']
        aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}')
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        # Auswahl des Wertes von a für Teilaufgabe g und h
        a1 = nzahl(1, 4)
        a2 = nzahl(1,6)/2
        while a1 == a2:
            a2 = nzahl(1, 6) / 2

        grafiken = []

        if 'a' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grenzwert_neg = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~' + \
                           latex(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} ' + \
                           fkt_str + '~=~' + latex(grenzwert_neg) + r' \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            fkt_sym = fkt.subs(x, -x)
            fkt_sym_str = (latex(-1 * fkt_a3)+ r' \cdot x^3 ~' + vorz_str(fkt_a2) + r'a \cdot x^2 ~'
                           + vorz_str(-1 * fkt_a1) + r'a^2 \cdot x ~' + vorz_str(fkt_a0) + r'a^3')
            if fkt_sym == fkt:
                lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                       + r'~=~f(x) \\ \to \quad \mathrm{Achsensymmetrie} \quad (3P) \\')
            elif fkt_sym == -1 * fkt:
                lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                       + r'~=~-f(x) \\ \to \quad \mathrm{Punktsymmetrie} \quad (3P) \\')
            else:
                lsg = (r') \quad f(-x)~=~' + fkt_sym_str + r' \neq  f(x)  \neq -f(x) \\ \to \quad'
                                                           r'\mathrm{nicht~symmetrisch} \quad (3P) \\')
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + lsg + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 18
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            # hier werden die Koeffizenten für das Hornerschema berechnet
            fkt_b2 = faktor * faktor_2
            fkt_c2 = -1 * faktor * (faktor_1 + faktor_3)
            fkt_b1 = -1 * faktor * faktor_2 * (faktor_1 + faktor_3)
            fkt_c1 = faktor * faktor_1 * faktor_3
            fkt_b0 = faktor*faktor_1*faktor_2*faktor_3
            # hier werden das Partialpolynom (Ergebnis Hornerschema) und die Gleichung für die pq-Formel berechnet
            fkt_partial = faktor * x**2 + fkt_c2 * a * x + fkt_c1 * a**2
            fkt_partial_str = (latex(faktor) + r' \cdot x^2' + vorz_str(fkt_c2) + r' \cdot a \cdot x'
                               + vorz_str(fkt_c1) + r' \cdot a^2')
            fkt_p = -1 * (faktor_1 + faktor_3)
            fkt_q = faktor_1 * faktor_3
            fkt_pq_str = 'x^2' + vorz_str(fkt_p) + r' \cdot a \cdot x' + vorz_str(fkt_q) + r' \cdot a^2'
            fkt_disk = Rational((faktor_1 - faktor_3)**2,4)

            table2 = Tabular('c c|c|c|c', row_height=1.2)
            table2.add_row('',latex(fkt_a3),latex(fkt_a2*a),latex(fkt_a1*a**2),latex(fkt_a0*a**3))
            table2.add_hline(2, 5)
            table2.add_row('Partialpolynom mit Horner Schema berechnen: ',' ',latex(fkt_b2*a),
                           latex(fkt_b1*a**2),latex(fkt_b0*a**3))
            table2.add_hline(2, 5)
            table2.add_row('', latex(fkt_a3), latex(fkt_c2*a), latex(fkt_c1*a**2), '0')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f, '
                                                    f'wenn eine Nullstelle bei {nst_2_str} ist. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                                                     + fkt_str + r' \quad (1P) \\ \mathrm{mit~x_1='
                                                     + nst_2_str + r'~folgt:} \quad (' + fkt_str
                                                     + r')~ \div ~(x' + nst_2_str_neg + r')~=~ \\' + fkt_partial_str
                                                     + r' \quad (4P)'))
            loesung.append(table2)
            loesung.append('0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + vorz_str_minus(faktor) +
                           r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2P) \\'
                           r' x_{2/3}~=~ - \frac{' + latex(fkt_p) + r'a}{2} \pm \sqrt{ \Big(' +
                           r' \frac{' + latex(fkt_p) + r'a}{2} \Big)^2-(' + latex(fkt_q) +  # p war grundlos ins Minus gestzt
                           r'a^2)} ~=~ ' + latex(Rational((faktor_1 + faktor_3),2)) + r'a \pm \sqrt{'
                           + latex(fkt_disk) + r' \cdot a^2} \quad (4P) \\ x_{2/3}~=~'
                           + latex(Rational(faktor_1 + faktor_3,2)) + r' \cdot a \pm \Big('
                           + latex(Rational(abs(faktor_1 - faktor_3),2)) + r' \Big) \cdot a \quad \to \quad x_2~=~'
                           + latex(faktor_1) + r'a \quad \mathrm{und} \quad x_3~=~'
                           + latex(faktor_3) + r'a \quad (3P) \\ S_{x_2}(' + nst_1_str + r'\vert 0) \quad S_{x_1}('
                           + nst_2_str + r' \vert 0) \quad S_{x_3}(' + nst_3_str + r' \vert 0) \quad \mathrm{sowie}'
                           r' \quad S_y(0 \vert' + latex(fkt_a0) + r'a^3) \quad (4P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'd' in teilaufg:
            punkte_aufg = 14
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            fkt_1 = collect(diff(fkt,x,1),x)
            fkt_2 = collect(diff(fkt,x,2),x)
            x_12_fkt_1 = solve(fkt_1, x)
            x_1_fkt_1 = x_12_fkt_1[0]
            x_2_fkt_1 = x_12_fkt_1[1]
            y_1_fkt = fkt.subs(x, x_1_fkt_1)
            y_2_fkt = fkt.subs(x, x_2_fkt_1)
            x_1_fkt_2 = fkt_2.subs(x,x_1_fkt_1)
            x_2_fkt_2 = fkt_2.subs(x,x_2_fkt_1)
            # print(x_1_fkt_2), print(x_2_fkt_2)
            if x_1_fkt_2.subs(a,1) < 0:
                lsg_extrema_1 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad HP(' + latex(N(x_1_fkt_1,3)) + r' \vert '
                                 + latex(N(y_1_fkt,3)) + r') \quad (2P) \\')
            else:
                lsg_extrema_1 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad TP(' + latex(N(x_1_fkt_1,3)) + r' \vert '
                                 + latex(N(y_1_fkt,3)) + r') \quad (2P) \\')

            if x_2_fkt_2.subs(a,1) < 0:
                lsg_extrema_2 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad HP(' + latex(N(x_2_fkt_1,3)) + r' \vert '
                                 + latex(N(y_2_fkt,3)) + r') \quad (2P) \\')
            else:
                lsg_extrema_2 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad TP(' + latex(N(x_2_fkt_1,3)) + r' \vert '
                                 + latex(N(y_2_fkt,3)) + r') \quad (2P) \\')

            # Koeffizienten der ersten Ableitung
            # fkt_a3 = faktor
            # fkt_a2 = -1 * faktor * (faktor_1 + faktor_2 + faktor_3)
            # fkt_a1 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
            # fkt_a0 = -1 * faktor * faktor_1 * faktor_2 * faktor_3
            fkt_1_a2 = 3*faktor
            fkt_1_a1 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
            fkt_1_a0 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
            fkt_1_p = Rational(-2 * (faktor_1 + faktor_2 + faktor_3),3)
            fkt_1_q = Rational((faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3),3)
            fkt_1_disk = (faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9
            fkt_1_sqrt = sqrt((faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9)

            # Funktionsgleichung und Partialpolynomne
            fkt_1_str = (latex(fkt_1_a2) + 'x^2' + vorz_str(fkt_1_a1) + r'a \cdot x'
                         + vorz_str(fkt_1_a0) + r'a^2')
            fkt_1_pq_str = 'x^2' + vorz_str(fkt_1_p) + r'a \cdot x' + vorz_str(fkt_1_q) + r'a^2'
            fkt_2_str = latex(6*faktor) + 'x' + vorz_str(fkt_1_a1) + r'a'

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrempunkte der Funktion f und deren Art'
                                                    ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \quad \mathrm{und} \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad (2P) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_1_str + r' \vert ~ \div ' + vorz_str_minus(3 * faktor) + r' \quad (1P) \\'
                           r'0~=~ ' + fkt_1_pq_str + r' \quad (1P) \\' + r' x_{1/2}~=~ - \frac{'
                           + latex(fkt_1_p) + r' \cdot a}{2} \pm \sqrt{ \Big( \frac{'
                           + latex(fkt_1_p) + r' \cdot a}{2} \Big)^2 - \Big(' + latex(fkt_1_q)
                           + r' \cdot a^2 \Big) } \quad (1P) \\ =~ ' + latex(N(-1*fkt_1_p/2,3)) + r' \cdot a \pm \sqrt{'
                           + latex(N(fkt_1_disk,3)) + r' \cdot a^2} \quad ~=~ ' + latex(N(-1*fkt_1_p/2,3)) + r' \cdot a \pm '
                           + latex(N(fkt_1_sqrt,3)) + r' \cdot a \quad (1P) \\'
                           + r'x_1~=~' + latex(-1*fkt_1_p/2) + r' \cdot a ~-~' + latex(N(fkt_1_sqrt,3))
                           + r' \cdot a~=~' + latex(N(x_1_fkt_1,3)) + r' \quad \mathrm{und} \quad '
                           + r'x_2~=~' + latex(-1*fkt_1_p/2) + r' \cdot a~+~' + latex(N(fkt_1_sqrt,3))
                           + r' \cdot a~=~' + latex(N(x_2_fkt_1,3)) + r' \quad (1P) \\'
                           + r'f^{ \prime \prime } (x_1) ~=~' + latex(6*faktor) + r' \cdot (' + latex(N(x_1_fkt_1,3))
                           + ')' + vorz_str(fkt_1_a1) + r' \cdot a ~=~' + latex(N(x_1_fkt_2,3)) + r' \quad (1P)'
                           + lsg_extrema_1 + r' f^{ \prime \prime } (x_2) ~=~' + latex(6 * faktor) + r' \cdot ('
                           + latex(N(x_2_fkt_1,3)) + ')' + latex(fkt_1_a1) + 'a  ~=~' + latex(N(x_2_fkt_2,3))
                           + r' \quad (1P)' + lsg_extrema_2 + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'e' in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            fkt_2_a0 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
            fkt_2_str = latex(6*faktor) + 'x' + vorz_str(fkt_2_a0) + 'a'
            xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3),3)
            xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3)/3,3)
            ywert_wp_dezimal = N(fkt.subs(x,xwert_wp_bruch*a),3)
            fkt_3_str = latex(6*faktor)

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die möglichen Wendepunkte der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad (1P) \quad \to \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_2_str + r' \quad \vert ~' + vorz_str(-1*fkt_2_a0) + r'a \quad \vert \div '
                           + vorz_str_minus(6 * faktor) + r' \quad (1P) \\ x_1~=~' + latex(xwert_wp_bruch) + 'a ~=~'
                           + latex(xwert_wp_dezimal) + r'a \quad (1P) \quad \to \quad f^{ \prime \prime \prime }('
                           + latex(xwert_wp_bruch) + ') ~=~ ' + fkt_3_str
                           + r' \quad \neq 0 \quad \to \quad \mathrm{Wendepunkt} (' + latex(xwert_wp_bruch)
                           + r'a \vert ' + latex(ywert_wp_dezimal) + r') \quad (4P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'f' in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3), 3)
            xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3) / 3)
            ywert_wp_dezimal = N(fkt.subs(x, xwert_wp_bruch*a), 3)
            if Rational(3,(faktor_1 + faktor_2 + faktor_3)) > 0:
                abhängigkeit = r'\mathrm{mit~x \in \mathbb{R} ~und~ x > 0}'
            else:
                abhängigkeit = r'\mathrm{mit~x \in \mathbb{R} ~und~ x < 0}'

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Ortskurve der Wendepunkte der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad x ~=~' + (latex(xwert_wp_bruch)) + r'a \quad \vert \div'
                           + vorz_Str_minus(Rational((faktor_1 + faktor_2 + faktor_3),3)) + r' \quad \to \quad a~=~'
                           + latex(Rational(3,(faktor_1 + faktor_2 + faktor_3))) + r'x \quad' + abhängigkeit
                           + r'\quad (3P) \\ \mathrm{einsetzen~in~y} ~=~' + latex(ywert_wp_dezimal) + '~=~'
                           + latex(ywert_wp_dezimal/a**3) + r' \Big(' + latex(Rational(3,(faktor_1 + faktor_2 + faktor_3)))
                           + r'x \Big)^3 ~=~' + latex(N((ywert_wp_dezimal/a**3)*(3/(faktor_1 + faktor_2 + faktor_3))**3,4))
                           + r'x^3 \quad (2P) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'g' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            nst_1_a1 = faktor_1 * a1
            nst_3_a1 = faktor_3 * a1
            fkt_a1 = expand(faktor * (x - faktor_1 * a1) * (x - faktor_2 * a1) * (x - faktor_3 * a1))
            xmin_f = int(nst_1_a1 - 1)
            xmax_f = int(nst_3_a1 + 1)
            xwerte = np.arange(xmin_f, xmax_f, 0.01)
            ywerte = [fkt_a1.subs(x, elements) for elements in xwerte]
            # plot(fkt_f, (x,xmin_f,xmax_f) ,show=False)
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
            fig.tight_layout()
            plt.savefig(f'Grafik_{nr}{liste_teilaufg[i]}', dpi=250)
            grafiken = [f'Grafik_{nr}{liste_teilaufg[i]}']
            plt.figure().clear()
            aufgabe.append('In der folgenden Abbildung ist ein Graph der Parameterfunktion dargestellt.')
            aufgabe.append('Dabei wurde für a ein Wert aus den natürlichen Zahlen gewählt. \n\n')
            aufgabe.append(str(liste_teilaufg[i]) + f') Bestimme aus dem Graphen den zugehörigen Wert von a. '
                                                    f'Begründe deine Aussage. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~zweite~Nullstelle~des'
                                                     r'~Graphen~liegt~bei~ca.~x_2=' + str(faktor_2*a1)
                           + r'.~} \mathrm{Die~berechnete~Nullstelle~liegt~bei~x_2=' + nst_2_str
                           + r'.~} \\ \mathrm{Damit~gilt:~}' + str(faktor_2*a1) + '~=~' + nst_2_str
                           + r' \quad \to \quad a~=~' + str(a1) + r'. \\'
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'h' in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            nst_1_a2 = faktor_1 * a2
            nst_3_a2 = faktor_3 * a2
            fkt_a2 = expand(faktor * (x - faktor_1 * a2) * (x - faktor_2 * a2) * (x - faktor_3 * a2))
            xmin_f = int(round(nst_1_a2 - 0.5,0))
            xmax_f = int(round(nst_3_a2 + 0.5,0))
            xwerte = np.arange(xmin_f, xmax_f, 0.01)
            ywerte = [fkt_a2.subs(x, elements) for elements in xwerte]
            # plot(fkt_f, (x,xmin_f,xmax_f) ,show=False)
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
            fig.tight_layout()
            plt.savefig(f'Grafik_{nr}{liste_teilaufg[i]}', dpi=200)
            grafiken.append(f'Grafik_{nr}{liste_teilaufg[i]}')
            plt.figure().clear()
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen von f für a={gzahl(a2)} im Intervall [{xmin_f};{xmax_f}].')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Die~folgende~Abbildung~zeigt~die~Lösung.~(5P)}'))
            loesung.append('Abbildung')
            i += 1
        return [aufgabe, loesung, grafiken]

    aufgaben = [kurvendiskussion_02(1, ['a','b','c','d','e','f','g','h'])]

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
    Art = 'Test 4'
    Titel = 'Kurvendiskussion von Parameterfunktionen'

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
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][0], width='250px')
                    del aufgabe[2][0]
                else:
                    Aufgabe.append(elements)

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
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[2][0], width='400px')
                    del loesung[2][0]
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
