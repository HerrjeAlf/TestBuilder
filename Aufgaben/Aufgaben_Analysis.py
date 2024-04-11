from pylatex import (MediumText)
from pylatex.utils import bold
import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def aenderungsrate(nr, teilaufg):
    liste_punkte = []
    liste_bez = []
    i = 0

    faktor = zzahl(1, 20) / 10
    s_xwert = zzahl(1, 3)
    s_ywert = zzahl(1, 3)
    abstand = random.choice([[-1, 2], [-2, 1]])

    x_wert_1 = s_xwert + abstand[0]
    x_wert_2 = s_xwert + abstand[1]
    y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
    y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
    werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

    while not all(abs(wert) < 6 for wert in werte):
        s_xwert = zzahl(1, 3)
        s_ywert = zzahl(1, 3)
        abstand = random.choice([[-1, 2], [-2, 1]])

        x_wert_1 = s_xwert + abstand[0]
        x_wert_2 = s_xwert + abstand[1]
        y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
        y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
        werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

    fkt = expand(faktor * (x - s_xwert) ** 2 + s_ywert)
    fkt_abl = diff(fkt, x)
    fkt_str = (latex(faktor) + 'x^2' + vorz_str(-2 * faktor * s_xwert)
               + 'x' + vorz_str((faktor * (s_xwert ** 2)) + s_ywert))
    fkt_abl = diff(fkt, x)
    fkt_abl_x0 = fkt_abl.subs(x, x_wert_2)

    print("f(x)=" + str(fkt))
    print("f'(x)=" + str(fkt_abl))
    print("f'(x_0)=" + str(fkt_abl_x0))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Funktion:',
               r'f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    grafiken_aufgaben = ['', '', '']
    grafiken_loesung = ['']

    xwerte_geraden = [-6, 6]
    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        aufgabe.append(str(teilaufg[i]) + f') Bestimme zeichnerisch die mittlere Änderungsrate im '
                                          f'Interval [ {x_wert_1} | {x_wert_2} ] vom Graphen f. \n\n')
        dy = y_wert_2 - y_wert_1
        dx = x_wert_2 - x_wert_1
        fkt_sekante = dy / dx * (x - x_wert_2) + y_wert_2
        xwerte = [-6 + n / 5 for n in range(60)]
        ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
        graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'Dargestellt ist der Graph von: $f(x) =' + fkt_str + '$',
                         'f', f'Aufgabe_{nr}{liste_teilaufg[i]}')

        xwerte_dy = [x_wert_2, x_wert_2]
        ywerte_dy = [y_wert_1, y_wert_2]
        xwerte_dx = [x_wert_1, x_wert_2]
        ywerte_dx = [y_wert_1, y_wert_1]

        steigung_dreieck = N((y_wert_2 - y_wert_1) / (x_wert_2 - x_wert_1), 2)

        ywerte_sekante = [fkt_sekante.subs(x, -6), fkt_sekante.subs(x, 6)]

        loesung.append(str(teilaufg[i])
                       + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~~Steigungsdreieck~(1P),~Steigung~'
                         r'\mathbf{m=' + str(steigung_dreieck) + r'}~bestimmt~(1P)} \\\\')

        if c not in teilaufg:
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'Dargestellt ist der Graph von: $f(x) =' + fkt_str + '$',
                             'f',f'Loesung_{nr}{liste_teilaufg[i]}', xwerte_dy, ywerte_dy,
                             xwerte_dx, ywerte_dx, xwerte_geraden, ywerte_sekante)

        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        aufgabe.append(str(teilaufg[i]) + f') Überprüfe die mittlere Änderungsrate im Interval'
                                          f'[ {x_wert_1} | {x_wert_2} ] durch Rechnung. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \frac{ \Delta y}{ \Delta x} ~=~ \frac{f(' + str(x_wert_2)
            + ') - f(' + str(x_wert_1) + ')}{' + str(x_wert_2) + str(vorz_str(-1 * x_wert_1)) + r'} ~=~ \frac{'
            + latex(N(y_wert_2, 3)) + vorz_str(-1 * N(y_wert_1, 3)) + '}{' + str(x_wert_2)
            + vorz_str(-1 * x_wert_1) + r'} ~=~\mathbf{'
            + latex(N(Rational(y_wert_2 - y_wert_1, x_wert_2 - x_wert_1), 3))
            + r'}\quad \to \quad \mathrm{'r'Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (4P) \\\\')
        liste_punkte.append(4)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        aufgabe.append(str(teilaufg[i])
                       + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')

        steigung_tangente = fkt_abl.subs(x, x_wert_2)
        fkt_tangente = steigung_tangente * (x - x_wert_2) + y_wert_2

        x_wert_3 = x_wert_2 - 1
        y_wert_3 = fkt_tangente.subs(x, x_wert_3)
        steigung_dreieck = N((y_wert_2 - y_wert_3) / (x_wert_2 - x_wert_3), 2)
        xwerte_dy_c = [x_wert_2, x_wert_2]
        ywerte_dy_c = [y_wert_2, y_wert_3]
        xwerte_dx_c = [x_wert_2, x_wert_3]
        ywerte_dx_c = [y_wert_3, y_wert_3]
        ywerte_tangente = [fkt_tangente.subs(x, -6), fkt_tangente.subs(x, 6)]

        if 'a' not in teilaufg:
            xwerte = [-6 + n / 5 for n in range(60)]
            ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'Dargestellt ist der Graph von: \ $f(x) =' + fkt_str + '$',
                             'f',f'Aufgabe_{nr}{liste_teilaufg[i]}')
            graph_xyfix_plus(xwerte, ywerte, fkt, r'Dargestellt ist der Graph von: \ $f(x) ='
                            + fkt_str + '$', 'f', 'loesung_Aufgabe_1', f'Loesung_{nr}{liste_teilaufg[i]}',
                             xwerte_dy_c, ywerte_dy_c, xwerte_dx_c, ywerte_dx_c, xwerte_geraden, ywerte_tangente)
        else:
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'Lösung für Aufgabe 1a/c - Geraden '
                                                          r'und ihre Steigungsdreiecke',
                            'f', f'Loesung_{nr}{liste_teilaufg[i]}', xwerte_dy, ywerte_dy, xwerte_dx, ywerte_dx,
                            xwerte_geraden, ywerte_sekante, xwerte_dy_c, ywerte_dy_c, xwerte_dx_c, ywerte_dx_c,
                            xwerte_geraden, ywerte_tangente)

        loesung.append(str(teilaufg[i])
                       + r') \quad \mathrm{Tangente~an~Punkt~(1P),~~Steigungsdreieck~(1P),~Steigung~\mathbf{m='
                       + str(steigung_dreieck) + r'}~bestimmt~(1P)} \\\\')
        liste_punkte.append(3)
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        aufgabe.append(str(teilaufg[i])
                       + f') Überprüfe die lokale Änderungsrate an der Stelle x = {x_wert_2} '
                         f'mit einer Rechnung. \n\n')
        a_3_re = faktor
        b_1_re = -2 * faktor * s_xwert
        b_2_re = faktor * x_wert_2
        b_3_re = b_1_re + b_2_re
        c_1_re = faktor * (s_xwert ** 2) + s_ywert - (faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert)
        c_2_re = b_3_re * x_wert_2

        a_1 = latex(N(faktor, 3))
        a_3 = latex(N(a_3_re, 3))
        b_1 = latex(N(b_1_re, 3))
        b_2 = latex(N(b_2_re, 3))
        b_3 = latex(N(b_3_re, 3))
        c_1 = latex(N(c_1_re, 3))
        c_2 = latex(N(c_2_re, 3))

        table = Tabular('c|c|c', row_height=1.2)
        table.add_row(a_1, b_1, c_1)
        table.add_hline(1, 3)
        table.add_row('', b_2, c_2)
        table.add_hline(1, 3)
        table.add_row(a_3, b_3, 0)

        division_fkt_linear = (fkt - fkt.subs(x, x_wert_2)) / (x - x_wert_2)
        partialbruch = latex(faktor) + 'x' + vorz_str(b_3_re)

        print(division_fkt_linear)
        print(partialbruch)

        # loesung.append(str(teilaufg[i]) + r') \quad \lim \limits_{x \to ' + str(x_wert_2)
        #               + r'} ~ \frac{f(x)-f(' + str(x_wert_2) + r')}{x' + vorz_str(-1 * x_wert_2)
        #               + r'} ~=~ \lim \limits_{x \to ' + str(x_wert_2) + r'} ~ \frac{' + fkt_str + '-('
        #               + latex(N(fkt.subs(x, x_wert_2), 3)) + ')}{x' + vorz_str(-1 * x_wert_2)
        #               + '} ~=~' + r' \lim \limits_{x \to ' + str(x_wert_2) + '}~' + partialbruch + '~=~'
        #               + latex(N(fkt_abl_x0, 3)) + r' \quad (3P) \\'
        #               + r'\to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (1P) \\\\')
        # loesung.append(r' \mathrm{Lösung~mit~Hornerschema~(2P):}  \hspace{3em} ')
        # loesung.append(table)
        # loesung.append(r' \hspace{5em}')

        loesung.append(str(teilaufg[i]) + r') \quad f^{ \prime} (x)~=~' + latex(fkt_abl) + r' \to f^{ \prime} ('
                       + str(x_wert_2) + r')~=~\mathbf{' + latex(fkt_abl.subs(x, x_wert_2)) +
                       r'} \quad (2P) \quad \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} '
                       r'\quad (1P) \\\\')
        liste_punkte.append(3)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

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
        fkt_h_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3-1,'x')
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
        nst_1 = zzahl(1,3)
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
        fkt_h_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3-1,'x')
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
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
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
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
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
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
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
            lsg = r' \quad S_y(0 \vert' + gzahl(s_fkt) + r') \quad (4P) \\'
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
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
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
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
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
        punkte = 6
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        xwert_wp1 = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor),3)
        ywert_wp1 = N(fkt.subs(x, xwert_wp1),3)
        ywert_wp1_fkt_1 = N(fkt_1.subs(x, xwert_wp1),3)
        fkt_t = ywert_wp1_fkt_1*(x-xwert_wp1) + ywert_wp1
        fkt_n = (-1/ywert_wp1_fkt_1)*(x-xwert_wp1) + ywert_wp1
        # print('Wendepunkt: ' + str(xwert_wp1))
        # print('f(x)=' + latex(fkt))
        # print('f`(x)=' + latex(fkt_1))
        # print('t(x)=' + latex(fkt_t))
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Wendetangente und die Wendenormale '
                                                f'der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                       + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                       + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                       + vorz_v_aussen(ywert_wp1_fkt_1,'(x') + vorz_v_innen(-1 * N(xwert_wp1,3),')')
                       + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1,'x')
                       + vorz_str(N(-1*ywert_wp1_fkt_1*xwert_wp1 + ywert_wp1,3))
                       + r' \quad (3P) \\ \mathrm{Die~Steigung~der~Normale~am~Wendepunkt~wird~berechnet~mit \quad'
                       + r' m_n ~=~ \frac{-1}{f^{ \prime }(x_{w})} \quad und~daraus~folgt:} \\'
                       + r'n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                       + r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1/ywert_wp1_fkt_1,'(x')
                       + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                       + vorz_v_aussen(-1/ywert_wp1_fkt_1,'x')
                       + vorz_str(N(xwert_wp1/ywert_wp1_fkt_1 + ywert_wp1,3))
                       + r' \quad (3P) \\' + r' \mathrm{insgesamt~' + str(6) + r'~Punkte} \\\\ \\\\')
        # xmin = int(round(nst_3 - 0.4, 0))
        # xmax = int(round(nst_2 + 0.4, 0))
        # Graph(xmin,xmax, fkt, name='latex(fkt_t)')
        liste_punkte.append(punkte)
        i += 1

    if 'g' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.extend(('', f'Loesung_{nr}{liste_teilaufg[i]}'))

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))
        # plot(fkt, (x,xmin_f,xmax_f) ,show=False)

        aufgabe.append(str(liste_teilaufg[i])
                       + f') Zeichne den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ] \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Koordinatensystem~(2P) \quad Werte~(2P)'
                                                r' \quad Graph~(1P) \to \quad insgesamt~(5P)}')
        Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
        loesung.append('Abbildung')

        liste_punkte.append(5)
        i += 1

    if 'h' in teilaufg and (nst_1 > 0 or nst_2 > 0 or nst_3 > 0) and nst_1*nst_2*nst_3 != 0 :
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.extend(('', f'Aufgabe_{nr}{liste_teilaufg[i]}'))
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        Fkt = integrate(fkt,x)
        Fkt_str = (vorz_v_aussen(Rational(fkt_a1,4),'x^4') + vorz_v_innen(Rational(fkt_a2,3),'x^3')
               + vorz_v_innen(Rational(fkt_a3,2),'x^2') + vorz_v_innen(fkt_a4,'x'))

        def erste_positive_nst(vec):
            print(vec)
            vec.sort()
            print(vec)
            for element in vec:
                if element > 0:
                    print(element)
                    return element
            exit('keine positive Nullstelle')

        obere_grenze = N(erste_positive_nst([nst_1, nst_2, nst_3]),3)
        loesung_integral = Fkt.subs(x, obere_grenze)


        aufgabe.extend((f'Der Graph von f schließt, mit der x-Achse und der y-Achse '
                        + ' rechts vom Ursprung eine Fläche ein. \n\n',
                        str(liste_teilaufg[i]) + f') Berechne die eingeschlossen Fläche. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \left| \int \limits_0^{' + gzahl(obere_grenze) + '}' + fkt_str
                       + r'~ \mathrm{d}x \right| ~=~ \left| \left(' + Fkt_str + r' \right)_{0}^{' + gzahl(obere_grenze)
                       + r'} \right| ~=~' + latex(abs(N(loesung_integral,3))) + r' \quad (4P) \\')

        liste_punkte.append(4)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
def exponentialfunktionen_01(nr, teilaufg):
    liste_punkte = []
    liste_bez = []
    i = 0
    extrema_xwert = zzahl(1,3)
    extrema_ywert = zzahl(1,3)
    if extrema_xwert > 0:
        y_vers = -1*nzahl(0,2)
    else:
        y_vers = nzahl(0,2)
    print(extrema_xwert), print(extrema_ywert), print(y_vers)

    # rekonstruktion der exponentialfunktion
    fkt_v = exp(b*x+2)*a*x**2
    fkt_a1 = diff(fkt_v,x)
    gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
    gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
    lsg = solve((gleichung1,gleichung2),(a,b))
    lsg_a = lsg[0][0]
    lsg_b = lsg[0][1]
    print(lsg)
    fkt = exp(lsg_b*x+2)*lsg_a*x**2 + y_vers
    fkt_str = (vorz_v_aussen(lsg_a,'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b,'x+2') + '}'
               + vorz_str(y_vers))


    # Werte für Angaben zum Zeichnen des Graphen
    ywerte = [(element,fkt.subs(x,element)) for element in range(-5,6)]
    wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
    xmin = wertebereich[0]
    xmax = wertebereich[-1]
    print(fkt), print(ywerte), print(wertebereich), print(xmin), print(xmax)
    graph_xyfix(fkt)

    # Ableitung der Funktionen
    fkt_a1 = diff(fkt,x)
    fkt_a2 = diff(fkt, x,2)
    fkt_a3 = diff(fkt, x,3)

    fkt_a1_str = (r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \Big(' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                  + vorz_v_innen(2*lsg_a,'x' + r' \Big)'))
    fkt_a2_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                  + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                  + vorz_str(2*lsg_a) + r' \Big)')
    fkt_a3_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                  + vorz_v_aussen(lsg_a * lsg_b**3, 'x^2') + vorz_v_innen(6 * lsg_a * lsg_b**2, 'x')
                  + vorz_str(6*lsg_a*lsg_b) + r' \Big)')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['','','']
    grafiken_loesung = ['']

    if 'a' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)
        print(grenzwert_min), print(grenzwert_pos)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + latex(grenzwert_min) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        if y_vers == 0:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte der'
                                                    f' Funktion f mit den Achsen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                           + r' \hspace{10em} \\ \mathrm{Ansatz:~f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                           + r' \quad da~e^{' + vorz_v_innen(lsg[0][1],'x+2') + r'} ~immer~ \neq 0'
                           + r' \quad \to \quad ' + (vorz_v_innen(lsg[0][0],'x^2'))
                           + r'~=~ 0} \quad \vert \div ' + gzahl_klammer(lsg[0][0]) + r' \quad \vert \sqrt{~} \\'
                           + r' x~=~0 \quad \to \quad S_y ~=~ S_x (0 \vert 0) \quad (4P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        else:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Schnittpunkt der'
                                                    f' Funktion f mit der y-Achse. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~y-Achse:}'
                           + r' \mathrm{Ansatz:~f(0)~=~ ' + gzahl(y_vers)
                           + r' \quad \to \quad S_y (0 \vert ' + gzahl(y_vers) + r')} \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1

    if 'c' in teilaufg:
        punkte_aufg = 6
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die ersten drei Ableitungen der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_a1_str
                       + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                       + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str  # passt sonst manchmal nicht aufs blatt
                       + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1

    if 'd' in teilaufg:
        punkte_aufg = 10
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        if fkt_a2.subs(x,0) < 0:
            lsg_extrema1 = r'~<~0~ \to HP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2P)'
        elif fkt_a2.subs(x,0) > 0:
            lsg_extrema1 = r'~>~0~ \to TP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2P)'
        else:
            lsg_extrema1 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'

        if fkt_a2.subs(x,-2/lsg_b) < 0:
            lsg_extrema2 = (r'~<~0~ \to HP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                            + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2P)')
        elif fkt_a2.subs(x,-2/lsg_b) > 0:
            lsg_extrema2 = (r'~>~0~ \to TP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                            + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2P)')
        else:
            lsg_extrema2 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'


        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrema der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad 0 ~=~ f^{ \prime }(x) ~=~'
                       + fkt_a1_str + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                       + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                       + vorz_v_innen(2*lsg_a,'x') + r'\quad (3P) \\'
                       + r'0~=~x \cdot \Big(' + vorz_v_aussen(lsg_a*lsg_b,'x')
                       + vorz_v_innen(2*lsg_a,r' \Big)')
                       + r' \quad \to \quad x_1~=~0 \quad \mathrm{und} \quad 0~=~ '
                       + vorz_v_aussen(lsg_a*lsg_b,'x') + vorz_v_innen(2*lsg_a,'') + r' \quad \vert \div '
                       + gzahl_klammer(lsg_a*lsg_b) + r' \quad \to \quad 0~=~x' + vorz_str(2/lsg_b)
                       + r' \quad \to \quad x_2~=~' + gzahl(-2/lsg_b) + r' \quad (3P) \\'
                       + r' f^{ \prime \prime }(0) ~=~ ' + gzahl(N(fkt_a2.subs(x,0),2)) + lsg_extrema1
                       + r' \quad \mathrm{und} \quad f^{ \prime \prime }(' + gzahl(-2/lsg_b) + ') ~=~ '
                       + gzahl(N(fkt_a2.subs(x,-2/lsg_b),2)) + lsg_extrema2 + r' \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1

    if 'e' in teilaufg:
        punkte_aufg = 10
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        xwert_wp1 = -2 / lsg_b - sqrt(2) / abs(lsg_b)
        xwert_wp2 = -2/lsg_b + sqrt(2)/abs(lsg_b)

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Wendepunkte der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad 0 ~=~ f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                       + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                       + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2')
                       + vorz_v_innen(4 * lsg_a*lsg_b, 'x') + vorz_str(2*lsg_a) + r' \quad \vert \div '
                       + gzahl_klammer(lsg_a*lsg_b**2) + r' \quad (3P) \\'
                       + r' 0 ~=~ x^2 ' + vorz_v_innen(4/lsg_b, 'x') + vorz_str(2/lsg_b**2)
                       + r' \quad \to \quad x_{1/2} ~=~  - \frac{' + gzahl_klammer(4/lsg_b)
                       + r'}{2} \pm \sqrt{ \Big( \frac{' + gzahl_klammer(4/lsg_b) + r'}{2} \Big)^2'
                       + vorz_str(-2/lsg_b**2) + r'} ~=~ ' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(abs(sqrt(2)/lsg_b))
                       + '~=~' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(N(abs(sqrt(2)/lsg_b),3)) + r' \quad (2P) \\'
                       + r' x_1 ~=~ ' + gzahl(N(xwert_wp1,3)) + r' \quad \mathrm{und} \quad x_2 ~=~'
                       + gzahl(N(xwert_wp2,3)) + r' \quad (1P) \\'
                       + r' f^{ \prime \prime \prime }(' + gzahl(N(xwert_wp1,3)) + ') ~=~ '
                       + gzahl(N(fkt_a3.subs(x,xwert_wp1),3)) + r' \neq 0 \quad \to \quad WP(~'
                       + gzahl(N(xwert_wp1,3)) + r'~ \vert ~ '
                       + gzahl(N(fkt.subs(x,xwert_wp1),3))
                       + r') \quad (2P) \\ f^{ \prime \prime \prime }('
                       + gzahl(N(xwert_wp2,3)) + ') ~=~ '
                       + gzahl(N(fkt_a3.subs(x,xwert_wp2),3)) + r' \neq 0 \quad \to \quad WP(~'
                       + gzahl(N(xwert_wp2,2)) + r'~ \vert ~ '
                       + gzahl(N(fkt.subs(x, xwert_wp2),2)) + r') \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
        i += 1

    if 'f' in teilaufg:
        punkte_aufg = 6
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        xwert_wp1 = N(-2/lsg_b - sqrt(2)/abs(lsg_b), 3)
        ywert_wp1 = N(fkt.subs(x,-2/lsg_b - sqrt(2)/abs(lsg_b)), 3)
        ywert_wp1 = N(fkt.subs(x, xwert_wp1),3)
        ywert_wp1_fkt_a1 = N(fkt_a1.subs(x, xwert_wp1),3)

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Tangente und Normale am Wendepunkt '
                                                f'WP({xwert_wp1}|{ywert_wp1}). \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                       r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(ywert_wp1_fkt_a1,'(x')
                       + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                       + vorz_v_aussen(ywert_wp1_fkt_a1,'x')
                       + vorz_str(N(-1*ywert_wp1_fkt_a1*xwert_wp1 + ywert_wp1,3))
                       + r' \quad (3P) \\ n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                       r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1/ywert_wp1_fkt_a1,'(x')
                       + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                       + vorz_v_aussen(-1/ywert_wp1_fkt_a1,'x')
                       + vorz_str(N(xwert_wp1/ywert_wp1_fkt_a1 + ywert_wp1,3))
                       + r' \quad (3P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
        i += 1


    if 'g' in teilaufg:
        punkte_aufg = 5
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}',''))
        Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen im Intervall I({xmin}|{xmax}). \n\n')
        loesung.extend(('Abbildung', str(liste_teilaufg[i])
                         + r') \quad \mathrm{Punkte~für~Koordinatensystem~2P,~Werte~2P,~Graph~1P} \\'))
        i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

kurvendiskussion_polynome(1,['f'])