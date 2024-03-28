from pylatex import (MediumText)
from pylatex.utils import bold
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *
from sympy.plotting import plot

from funktionen import *
from plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def kurvendiskussion_polynome(nr, teilaufg):
    liste_punkte = []
    liste_bez = []
    i = 0

    if random.random() < 0.5:
        nst_1 = zzahl(1, 3)
        nst_2 = nst_1 + nzahl(1, 3) + 0.5
        nst_3 = nst_1 - nzahl(2, 3) - 0.5
        faktor = zzahl(3, 8) / 2

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * (nst_1 + nst_2 + nst_3)
        fkt_a3 = faktor * ((nst_1 * nst_2) + (nst_1 * nst_3) + (nst_2 * nst_3))
        fkt_a4 = -1 * faktor * nst_1 * nst_2 * nst_3
        fkt_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3,'x')
                   + vorz_str(fkt_a4))

        fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
        fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
        fkt_partial_p = -1 * (nst_2 + nst_3)
        fkt_partial_q = (nst_2 * nst_3)

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * (nst_1 + nst_2 + nst_3), 3),'x')
                    + vorz_str(Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)))
        p_fkt_1_pq = Rational(-2 * (nst_1 + nst_2 + nst_3), 3)
        q_fkt_1_pq = Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)
        s_fkt = -1 * faktor * nst_1 * nst_2 * nst_3


    else:
        nst_1 = zzahl(0,2)
        quadr_nst_23 = nzahl(2, 25)
        nst_2 = math.sqrt(quadr_nst_23)
        nst_3 = -1 * nst_2
        faktor = zzahl(3,8) / 2

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * nst_1
        fkt_a3 = faktor * (-1 * quadr_nst_23)
        fkt_a4 = faktor * nst_1 * quadr_nst_23
        fkt_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3,'x')
                   + vorz_str(fkt_a4))

        fkt_partial = faktor * (x ** 2 - quadr_nst_23)
        fkt_partial_pq = x ** 2 - quadr_nst_23
        fkt_partial_p = 0
        fkt_partial_q = -1 * quadr_nst_23

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * nst_1, 3),'x') +
                    vorz_str(Rational(quadr_nst_23, -3)))
        p_fkt_1_pq = Rational((-2 * nst_1), 3)
        q_fkt_1_pq = Rational(-1 * quadr_nst_23, 3)
        s_fkt = faktor * nst_1 * quadr_nst_23

    fkt_b2 = nst_1 * fkt_a1
    fkt_c2 = fkt_a2 + fkt_b2
    fkt_b3 = nst_1 * fkt_c2
    fkt_c3 = fkt_a3 + fkt_b3
    fkt_b4 = nst_1 * fkt_c3
    fkt_c4 = fkt_a4 + fkt_b4

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    grafiken_aufgaben = ['', '', '']
    grafiken_loesung = ['']


    
    if 'a' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + gzahl(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + gzahl(grenzwert_min) + r' \quad (2P)')
        liste_punkte.append(2)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        fkt_sym = fkt.subs(x, -x)
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3P)')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3P)')
        else:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad'
                                                          r'\mathrm{nicht~symmetrisch} \quad (3P)')
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + lsg)
        liste_punkte.append(3)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', '', ''))

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('', fkt_a1, fkt_a2, fkt_a3, fkt_a4)
        table2.add_hline(2, 5)
        table2.add_row('Berechnung der Partialfunktion  mit Hornerschema: ', '', fkt_b2, fkt_b3, fkt_b4)
        table2.add_hline(2, 5)
        table2.add_row('', fkt_a1, fkt_c2, fkt_c3, fkt_c4)

        if nst_1 == 0 or nst_2 == 0 or nst_3 == 0:
            lsg = r' \quad (3P) \\'
            punkte = 15
        else:
            lsg = r' \quad S_y(0 \vert' + latex(s_fkt) + r') \quad (4P) \\'
            punkte = 16

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + fkt_str
                       + r' \quad \mathrm{durch~probieren:~x_1~=~}' + gzahl(nst_1)
                       + r' \quad (2P) \\' + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1) + ')~=~'
                       + latex(fkt_partial) + r' \quad (4P)')
        loesung.append(table2)
        loesung.append(r'\hspace{10em} \\' + latex(fkt_partial) + r'~=~0 \quad \vert ~ \div '
                       + gzahl_klammer(faktor) + r' \quad \to \quad 0~=~' + latex(fkt_partial_pq)
                       + r' \quad (2P) \\' + r' x_{2/3}~=~ - \frac{' + gzahl_klammer(fkt_partial_p)
                       + r'}{2} \pm \sqrt{ \Big(' + r' \frac{' + latex(fkt_partial_p) + r'}{2} \Big)^2-'
                       + gzahl_klammer(fkt_partial_q) + r'} \quad (2P) \\' + r' x_2~=~' + gzahl(round(nst_2, 3))
                       + r' \quad \mathrm{und} \quad x_3~=~' + gzahl(round(nst_3, 3)) + r' \quad (2P) \\'
                       + r'S_{x_1}(' + gzahl(nst_1) + r'\vert 0) \quad S_{x_2}(' + gzahl(round(nst_2, 3))
                       + r' \vert 0) \quad S_{x_3}(' + gzahl(round(nst_3, 3)) + r' \vert 0)' + lsg
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        punkte = 16
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        x_12_fkt_1 = solve(fkt_1, x)
        x_1_fkt_1 = round(x_12_fkt_1[0], 3)
        x_2_fkt_1 = round(x_12_fkt_1[1], 3)

        fkt_2 = expand(diff(fkt, x, 2))
        fkt_2_str = vorz_v_aussen(6 * faktor,'x') + vorz_str(-2 * faktor * (nst_1 + nst_2 + nst_3))
        fkt_3 = expand(diff(fkt, x, 3))
        fkt_3 = vorz_str(6 * faktor)

        if fkt_2.subs(x, x_1_fkt_1) < 0:
            loesung_f_monotonie_1 = (r'~<~0~ \to HP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3P) \\')
        else:
            loesung_f_monotonie_1 = (r'~>~0~ \to TP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                    + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3P) \\')

        if fkt_2.subs(x, x_2_fkt_1) < 0:
            loesung_f_monotonie_2 = (r'~<~0~ \to HP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3P) \\')
        else:
            loesung_f_monotonie_2 = (r'~>~0~ \to TP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3P) \\')

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrema der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + latex(fkt_1)
                       + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                       + r' \quad f^{ \prime \prime \prime } (x) ~=~' + latex(fkt_3) + r' \quad (3P) \\'
                       + r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + latex(fkt_1) + r' \vert ~ \div '
                       + gzahl_klammer(3 * faktor) + r' \quad (1P) \\  0 ~=~' + fkt_1_pq + r' \quad \to \quad '
                       + r' x_{1/2} ~=~ - \frac{' + gzahl_klammer(p_fkt_1_pq) + r'}{2} \pm \sqrt{ \Big(' + r' \frac{'
                       + latex(p_fkt_1_pq) + r'}{2} \Big)^2-' + gzahl_klammer(q_fkt_1_pq) + r'} \quad (3P) \\'
                       + r'x_1~=~' + gzahl(x_1_fkt_1) + r' \quad \mathrm{und} \quad x_2~=~' + gzahl(x_2_fkt_1)
                       + r' \quad (2P) \\' + r' f^{ \prime \prime }(' + gzahl(x_1_fkt_1) + ')~=~'
                       + gzahl(round(fkt_2.subs(x, x_1_fkt_1), 3)) + loesung_f_monotonie_1 + r' f^{ \prime \prime }('
                       + gzahl(x_2_fkt_1) + ')~=~' + gzahl(round(fkt_2.subs(x, x_2_fkt_1), 3))
                       + loesung_f_monotonie_2 + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        punkte = 5
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        xwert_Wendepunkt = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor),3)
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die möglichen Wendepunkte der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ' + vorz_str(2 * faktor * (nst_1 + nst_2 + nst_3))
                       + r' \quad \vert \div ' + gzahl_klammer(6 * faktor) + r' \quad \to \quad x_1~=~'
                       + gzahl(xwert_Wendepunkt) + r' \quad (2P) \\ f^{ \prime \prime \prime }('
                       + gzahl(xwert_Wendepunkt) + r') \quad \neq 0 \quad \to \quad WP('
                       + gzahl(xwert_Wendepunkt) + r' \vert ' + gzahl(round(fkt.subs(x, xwert_Wendepunkt), 3))
                       + r') \quad (3P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        xwert_wp1 = Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor)
        ywert_wp1 = fkt.subs(x, xwert_wp1)
        ywert_wp1_fkt_1 = fkt_1.subs(x, xwert_wp1)
        fkt_t = ywert_wp1_fkt_1*(x-xwert_wp1) + ywert_wp1
        fkt_n = (-1/ywert_wp1_fkt_1)*(x-xwert_wp1) + ywert_wp1
        print('Wendepunkt: ' + str(xwert_wp1))
        print('f(x)=' + latex(fkt))
        print('f`(x)=' + latex(fkt_1))
        print('t(x)=' + latex(fkt_t))
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Wendetangente und die Wendenormale '
                                                f'der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                           + r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(ywert_wp1_fkt_1,'(x')
                           + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(ywert_wp1_fkt_1,'x')
                           + vorz_str(N(-1*ywert_wp1_fkt_1*xwert_wp1 + ywert_wp1,3))
                           + r' \quad (3P) \\ n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                           r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1/ywert_wp1_fkt_1,'(x')
                           + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(-1/ywert_wp1_fkt_1,'x')
                           + vorz_str(N(xwert_wp1/ywert_wp1_fkt_1 + ywert_wp1,3))
                           + r' \quad (3P) \\'
                           + r' \mathrm{insgesamt~' + str(6) + r'~Punkte}')
        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))
        Graph(xmin,xmax, fkt, fkt_t, fkt_n , name='latex(fkt_t)')
        liste_punkte.append(5)
        i += 1

    if 'g' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.extend(('',f'Loesung_{nr}{liste_teilaufg[i]}'))

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))
        # plot(fkt, (x,xmin_f,xmax_f) ,show=False)
        Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
        aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen von f im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ].')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Koordinatensystem~(2P) \quad Werte~(2P)'
                                                r' \quad Graph~(1P) \to \quad insgesamt~(5P)}')
        loesung.append(f'Die Abbildung zeigt den Graphen von f(x) im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ]. \n\n')

        liste_punkte.append(5)
        i += 1
        
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# kurvendiskussion_polynome(1,['f'])