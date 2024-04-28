import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
nr_aufgabe = 0

# Aufgaben zur Differenzialrechnung
def aenderungsrate(nr, teilaufg=['a', 'b', 'c', 'd'], ableitung=None):
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
    fkt_str = (vorz_v_aussen(faktor, 'x^2') + vorz_v_innen(-2 * faktor * s_xwert,'x')
               + vorz_str((faktor * (s_xwert ** 2)) + s_ywert))
    fkt_abl = diff(fkt, x)
    fkt_abl_x0 = fkt_abl.subs(x, x_wert_2)

    # print("f(x)=" + str(fkt))
    # print("f'(x)=" + str(fkt_abl))
    # print("f'(x_0)=" + str(fkt_abl_x0))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Funktion:',
               r'f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    xwerte_geraden = [-6, 6]
    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        aufgabe.extend((str(liste_teilaufg[i]) + f') Bestimme zeichnerisch die mittlere Änderungsrate im '
                                          f'Interval [ {x_wert_1} | {x_wert_2} ] vom Graphen f.', 'Figure'))
        dy = y_wert_2 - y_wert_1
        dx = x_wert_2 - x_wert_1
        fkt_sekante = dy / dx * (x - x_wert_2) + y_wert_2
        xwerte = [-6 + n / 5 for n in range(60)]
        ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
        graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'',
                         'f', f'Aufgabe_{nr}{liste_teilaufg[i]}')

        xwerte_dy = [x_wert_2, x_wert_2]
        ywerte_dy = [y_wert_1, y_wert_2]
        xwerte_dx = [x_wert_1, x_wert_2]
        ywerte_dx = [y_wert_1, y_wert_1]

        steigung_dreieck = N((y_wert_2 - y_wert_1) / (x_wert_2 - x_wert_1), 2)

        ywerte_sekante = [fkt_sekante.subs(x, -6), fkt_sekante.subs(x, 6)]

        loesung.append(str(liste_teilaufg[i])
                       + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~~Steigungsdreieck~(1P),~Steigung~}'
                         r'\bm{m=' + gzahl(steigung_dreieck) + r'}~\mathrm{bestimmt~(1P)}')

        if 'c' not in teilaufg:
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, '',
                             'f',f'Loesung_{nr}{liste_teilaufg[i]}', xwerte_dy, ywerte_dy,
                             xwerte_dx, ywerte_dx, xwerte_geraden, ywerte_sekante)
            loesung.append('Figure')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')


        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die mittlere Änderungsrate im Interval '
                                          f'[ {x_wert_1} | {x_wert_2} ] durch Rechnung. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \frac{ \Delta y}{ \Delta x} ~=~ \frac{f(' + gzahl(x_wert_2)
            + ') - f(' + gzahl(x_wert_1) + ')}{' + gzahl(x_wert_2) + vorz_str(-1 * x_wert_1) + r'} ~=~ \frac{'
            + gzahl(N(y_wert_2, 3)) + vorz_str(-1 * N(y_wert_1, 3)) + '}{' + gzahl(x_wert_2)
            + vorz_str(-1 * x_wert_1) + r'} ~=~\bm{'
            + gzahl(N(Rational(y_wert_2 - y_wert_1, x_wert_2 - x_wert_1), 3))
            + r'}\quad \to \quad \mathrm{'r'Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (4P)')
        liste_punkte.append(4)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'',
                             'f',f'Aufgabe_{nr}{liste_teilaufg[i]}')
            graph_xyfix_plus(xwerte, ywerte, fkt, r'', 'f', 'loesung_Aufgabe_1',
                             f'Loesung_{nr}{liste_teilaufg[i]}',xwerte_dy_c, ywerte_dy_c,
                             xwerte_dx_c, ywerte_dx_c, xwerte_geraden, ywerte_tangente)
            aufgabe.append(str(liste_teilaufg[i])
                           + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}.')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            aufgabe.append('Figure')

        else:
            xwerte = [-6 + n / 5 for n in range(60)]
            ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt,
                             r'',
                             'f', f'Loesung_{nr}{liste_teilaufg[i]}',
                             xwerte_dy, ywerte_dy, xwerte_dx, ywerte_dx,
                            xwerte_geraden, ywerte_sekante, xwerte_dy_c, ywerte_dy_c, xwerte_dx_c, ywerte_dx_c,
                            xwerte_geraden, ywerte_tangente)
            aufgabe.append(str(liste_teilaufg[i])
                           + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')

        loesung.extend((str(liste_teilaufg[i])
                       + r') \quad \mathrm{Tangente~an~Punkt~(1P),~~Steigungsdreieck~(1P),~Steigung~}\bm{m='
                       + str(steigung_dreieck) + r'}\mathrm{~bestimmt~(1P)}', 'Figure'))
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        liste_punkte.append(3)
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i])
                       + f') Überprüfe die lokale Änderungsrate an der Stelle x = {x_wert_2} '
                         f'mit einer Rechnung. \n\n')
        a_3_re = faktor
        b_1_re = -2 * faktor * s_xwert
        b_2_re = faktor * x_wert_2
        b_3_re = b_1_re + b_2_re
        c_1_re = faktor * (s_xwert ** 2) + s_ywert - (faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert)
        c_2_re = b_3_re * x_wert_2

        a_1 = gzahl(N(faktor, 3))
        a_3 = gzahl(N(a_3_re, 3))
        b_1 = gzahl(N(b_1_re, 3))
        b_2 = gzahl(N(b_2_re, 3))
        b_3 = gzahl(N(b_3_re, 3))
        c_1 = gzahl(N(c_1_re, 3))
        c_2 = gzahl(N(c_2_re, 3))

        table = Tabular('c c|c|c', row_height=1.2)
        table.add_row('', a_1, b_1, c_1)
        table.add_hline( 2, 4)
        table.add_row('alternative Berechnung des Partialbruches mit Hornerschema: ','', b_2, c_2)
        table.add_hline(2, 4)
        table.add_row('', a_3, b_3, 0)

        division_fkt_linear = (fkt - fkt.subs(x, x_wert_2)) / (x - x_wert_2)
        partialbruch = gzahl(faktor) + 'x' + vorz_str(b_3_re)

        # print(division_fkt_linear)
        # print(partialbruch)

        if ableitung == None:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \lim \limits_{x \to ' + gzahl(x_wert_2)
                           + r'} ~ \frac{f(x)-f(' + gzahl(x_wert_2) + r')}{x' + vorz_str(-1 * x_wert_2)
                           + r'} ~=~ \lim \limits_{x \to ' + gzahl(x_wert_2) + r'} ~ \frac{' + fkt_str + '-('
                           + gzahl(N(fkt.subs(x, x_wert_2), 3)) + ')}{x' + vorz_str(-1 * x_wert_2)
                           + '} ~=~' + r' \lim \limits_{x \to ' + gzahl(x_wert_2) + '}~' + partialbruch + r'~=~ \bm{'
                           + gzahl(N(fkt_abl_x0, 3)) + r'} \quad (3P) \\'
                           + r' \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (1P)')
            loesung.append(table)
            loesung.append(' \n\n')
            liste_punkte.append(4)
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime} (x)~=~' + latex(fkt_abl)
                           + r' \to f^{ \prime} (' + gzahl(x_wert_2) + r')~=~\bm{'
                           + gzahl(fkt_abl.subs(x, x_wert_2))
                           + r'} \quad (2P) \quad \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein}'
                           r'\quad (1P) \\')
            liste_punkte.append(3)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def differentialqoutient(nr, teilaufg=['a', 'b']):
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        a1, a2 = faktorliste(2, 10, 2)  # funktioniert auch so :)
        b1, b2, b3 = faktorliste(2, 12, 3)
        fkt_str_a = str(a1) + 'x' + vorz_str(a2)
        fkt_str_b = str(b1) + 'x^2' + vorz_str(b2) + 'x' + vorz_str(b3)

        aufgabe.append(str(liste_teilaufg[i])
                       + r') Berechne die Ableitung der folgenden Funktionen mithilfe des Differentialquotienten.')
        aufgabe.append(r'i) \quad f_1 (x)~=~' + fkt_str_a + r' \hspace{10em} ' + r'ii) \quad f_2 (x)~=~'
                       + fkt_str_b + r' \hspace{5em} \\')
        loesung.append(str(liste_teilaufg[i])
                       + r') \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe~des~'
                         r'Differentialquotienten}.')
        loesung.append(r' i) \quad f_1 ^{ \prime} (x) ~=~ \lim \limits_{ h \to 0} \frac{f(x+h) ~-~ f(x)}{h}'
                       + r'= ~ \lim \limits_{ h \to 0}\frac{' + str(a1) + r'(x + h)~' + vorz_str(a2) + r'~-('
                       + str(a1) + r'x' + vorz_str(a2) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{'
                       + str(a1) + 'x~' + vorz_str(a1) + 'h~' + vorz_str(a2) + '~' + vorz_str(-1 * a1) + r'x~'
                       + vorz_str(-1 * a2) + r'}{h} =~ \lim \limits_{ h \to 0} \frac{~' + str(a1)
                       + r'h~}{h} ~=~\bm{' + str(a1) + r'} \quad (3P) \\\\')  # \\\\ für Übersichtlichkeit
        loesung.append(r' ii) \quad f_2 ^{ \prime} (x) ~=~ \lim \limits_{ h \to 0}'
                       + r' \frac{f(x+h) - f(x)}{h} ~=~ \lim \limits_{ h \to 0} \frac{' + str(b1) + r'(x + h)^2 ~'
                       + vorz_str(b2) + r'(x+h) ~' + vorz_str(b3) + r' ~-~ (' + str(b1) + r'x^2' + vorz_str(b2)
                       + r'x~' + vorz_str(b3) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{~' + str(b1)
                       + r'x^2 ~' + vorz_str(2 * b1) + 'xh ~' + vorz_str(b1) + 'h^2 ~' + vorz_str(b2) + 'x~'
                       + vorz_str(b2) + 'h~' + vorz_str(b3) + '~' + vorz_str(-1 * b1) + 'x^2~'
                       + vorz_str(-1 * b2) + 'x ~' + vorz_str(-1 * b3) + r'}{h} ~=~ \lim \limits_{ h \to 0} \frac{~'
                       + str(2 * b1) + r'xh ~' + vorz_str(b1) + r'h^2~' + vorz_str(b2) + r' h~}{h} \\'
                       + r' ~=~ \lim \limits_{ h \to 0} \frac{~ h(~' + str(2 * b1) + r'x~' + vorz_str(b1)
                       + 'h ~' + vorz_str(b2) + r'~)}{h} =~ \lim \limits_{ h \to 0} ' + str(2 * b1) + r'x~'
                       + vorz_str(b1) + 'h ~' + vorz_str(b2) + r'~=~ \bm{' + str(2 * b1) + 'x~' + vorz_str(b2)
                       + r'} \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        liste_punkte.append(punkte)
        i += 1
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def grafisches_ableiten(nr, teilaufg=['a', 'b']):
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        punkte = 3
        nst_1 = zzahl(1, 3)
        nst_2 = nst_1 + nzahl(1, 3) + 0.5
        nst_3 = nst_1 - nzahl(2, 3) - 0.5
        faktor = zzahl(3, 8) / 2
        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_abl = collect(expand(diff(fkt, x, 1)), x)

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))

        aufgabe.extend((str(liste_teilaufg[i])
                        + r') Skizzieren Sie im Koordinatensystem den Graphen der Ableitungsfunktion.', 'Figure'))
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{~Graph~der~Ableitungsfunktion~(2P)} ', 'Figure'))
        Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        Graph(xmin, xmax, fkt, fkt_abl, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')

        liste_punkte.append(punkte)
        i += 1

        if 'b' in teilaufg:
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 3
            fkt_1 = collect(expand(diff(fkt, x, 1)), x)
            fkt_2 = collect(expand(diff(fkt, x, 2)), x)
            fkt_3 = collect(expand(diff(fkt, x, 3)), x)
            extrema = solve(fkt_1, x)
            wendepkt = solve(fkt_2, x)
            wendepkt_art = fkt_3.subs(x, wendepkt[0])
            if wendepkt_art < 0:
                art = (r'  \mathrm{Es~ist~ein~\mathbf{links-rechts-Wendepunkt},~deswegen~ist~das~Extrema~ein~Hochpunkt'
                       + r' \quad (1P)} \\')
            else:
                art = (r'  \mathrm{Es~ist~ein~\mathbf{rechts-links-Wendepunkt},~deswegen~ist~das~Extrema~ein~Tiefpunkt'
                       + r' \quad (1P)} \\')
            aufgabe.append(str(liste_teilaufg[i]) + f') Begründen Sie Ihre Skizze. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Extrema~an~Stelle~}\bm{x_1~=~'
                           + gzahl(N(extrema[0],3)) + r'}\mathrm{~und~}\bm{x_2 ~=~' + gzahl(N(extrema[1], 3))
                           + r'}\mathrm{~sind~Nullstellen~der~Ableitung \quad (1P)} \\'
                           + r' \mathrm{Wendepunkte~an~Stelle~}\bm{x_w~=~' + gzahl(N(wendepkt[0], 3))
                           + r'}\mathrm{~ist~Extrema~der~Ableitung \quad (1P)} \\' + art
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')

            liste_punkte.append(punkte)
            i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ableitungen(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
    liste_bez = [f'{str(nr)}']
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Berechne die Ableitung der folgenden Funktionen mithilfe der elementaren Ableitungsregeln.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def funktion(p):  # erzeugt eine Funktion und deren Ableitungen mit p Summanden und maximal p-Grades
        fkt = nzahl(1,9)
        koeffizienten = faktorliste(1, 15, p)
        potenzen = exponenten(p)
        pkt = p
        for koeffizient in koeffizienten:
            fkt = koeffizient * (x ** potenzen.pop()) + fkt
            fkt = collect(fkt, x)
        fkt_uf = ''
        fkt_abl = collect(expand(diff(fkt, x)), x)
        fkt_2 = collect(expand(diff(fkt, x, 2)), x)
        return latex(fkt), fkt_uf, latex(fkt_abl), pkt

    def polynom():
        a1 = zzahl(3, 15)
        e1 = nzahl(2, 6)
        fkt = r' \frac{' + gzahl(a1) + '}{x^{' + gzahl(e1) + '}}'
        fkt_uf = '~=~' + gzahl(a1) + r'\cdot x^{' + gzahl(-1 * e1) + '}'
        fkt_abl = gzahl(-1 * a1 * e1) + r' \cdot x^{' + gzahl(-1 * e1 - 1) + '}'
        pkt = 1
        return fkt, fkt_uf, fkt_abl, pkt

    def wurzel():
        a1 = zzahl(2, 15)
        e1, e2 = exponenten(2)
        fkt = gzahl(a1) + r' \sqrt[' + gzahl(e1) + ']{x^{' + gzahl(e2) + '}}'
        fkt_uf = '~=~' + gzahl(a1) + r' \cdot x^{ \frac{' + gzahl(e2) + '}{' + gzahl(e1) + '}}'
        fkt_abl = (gzahl(Rational(a1 * e2, e1)) + r' \cdot x^{'
                       + gzahl(Rational(e2, e1) - 1) + '}')
        pkt = 1
        return fkt, fkt_uf, fkt_abl, pkt

    def poly_wurzel():
        a1, a2, a3 = faktorliste(2, 12, 3)
        e1, e2, e3 = exponenten(3)
        fkt = (vorz_aussen(a1 / a2) + r' \frac{' + gzahl(abs(a1)) + '}{' + gzahl(abs(a2)) + r'x^{'
                   + gzahl(e1) + '}}' + vorz(a3) + r' \frac{' + gzahl(abs(a3)) + r'}{ \sqrt[' + gzahl(e2) + r']{'
                   + gzahl(e3) + '}}')
        fkt_uf = ('~=~' + vorz_v_aussen(Rational(a1, a2), 'x^{' + gzahl(-1 * e1) + '}')
                      + vorz_v_innen(a3, 'x^{' + gzahl(Rational(-1 * e3, e2)) + '}'))
        fkt_abl = (vorz_v_aussen(Rational(-1 * a1 * e1, a2), 'x^{' + gzahl(-1 * e1 - 1) + '}')
                       + vorz_v_innen(Rational(-1 * a3 * e3, e2), 'x^{' + gzahl(Rational(-1 * (e3 - e2), e2)) + '}'))
        pkt = 2
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_exp():
        punkte = 2
        faktor_exp = zzahl(2, 8)
        pkt = 2
        fkt = 'x^{' + gzahl(faktor_exp) + r'} \cdot e^{x}'
        fkt_uf = ''
        fkt_abl = (gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                   + r'} \cdot e^{x} ~+~x^{' + gzahl(faktor_exp) + r'} \cdot e^{x} ~=~ e^{x} \cdot \big( '
                   + gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1) + '} + x^{' + gzahl(faktor_exp)
                   + r'} \big)')
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_ln():
        pkt = 3
        faktor_exp = zzahl(2, 8)
        fkt = 'x^{' + gzahl(faktor_exp) + r'} \cdot \ln(x)'
        fkt_uf = ''
        fkt_abl = (gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                   + r'} \cdot \ln(x) ~+~ x^{' + gzahl(faktor_exp) + r'} \cdot x^{-1} ~=~'
                   + 'x^{' + gzahl(faktor_exp - 1) + r'} \cdot (' + gzahl(faktor_exp)
                   + r' \cdot \ln(x) ~+~ 1)')
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_wurzel_exp():
        pkt = 3
        faktor_exp = zzahl(2, 8)
        faktor_sqrt = nzahl(2, 8)
        while abs(faktor_exp) == faktor_sqrt:
            faktor_sqrt = nzahl(2, 8)
        fkt = r' \sqrt[' + gzahl(faktor_sqrt) + ']{x^{' + gzahl(faktor_exp) + r'}} \cdot e^{x}'
        fkt_uf = (r'x^{' + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} \cdot e^{x}')
        fkt_abl = (gzahl(Rational(faktor_exp, faktor_sqrt)) + r' \cdot x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt) - 1) + r'} \cdot e^{x} ~+~' + 'x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} \cdot e^{x} ~=~ e^{x} \cdot ('
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + r' \cdot x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt) - 1) + r'} ~+~ x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + '}')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_exp():
        pkt = 3
        exponent = zzahl(2, 8)
        faktor_1 = zzahl(2, 8)
        faktor_2 = zzahl(1, 8)
        fkt = ('e^{' + vorz_v_aussen(faktor_1, 'x') + '^{' + gzahl(exponent) + r'}'
               + vorz_v_innen(faktor_2, 'x') + '}')
        fkt_uf = ''
        fkt_abl = ('e^{' + vorz_v_aussen(faktor_1, 'x') + '^{' + gzahl(exponent) + r'}'
                    + vorz_v_innen(faktor_2, 'x') + r'} \cdot (' + vorz_v_aussen(faktor_1 * exponent, 'x')
                       + '^{' + gzahl(exponent - 1) + r'}' + vorz_str(faktor_2) + r')')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_ln():
        pkt = 3
        exponent = zzahl(2, 8)
        faktor_1 = zzahl(2, 8)
        faktor_2 = zzahl(1, 8)
        fkt = (r' \ln(' + vorz_v_aussen(faktor_1, 'x^{' + gzahl(exponent) + r'}')
               + vorz_v_innen(faktor_2, 'x') + ')')
        fkt_uf = ''
        fkt_abl = (r' \frac{1}{' + vorz_v_aussen(faktor_1, 'x') + '^{'
                   + gzahl(exponent) + r'}' + vorz_v_innen(faktor_2, 'x') + r'} \cdot ('
                   + vorz_v_aussen(faktor_1 * exponent, 'x') + '^{' + gzahl(exponent - 1) + r'}'
                   + vorz_str(faktor_2) + r')')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_wurzel():
        pkt = 3
        exponent = zzahl(2, 8)
        wurzel = nzahl(2, 8)
        faktor = zzahl(1, 10)
        while abs(exponent) == wurzel:
            wurzel = nzahl(2, 8)
        summand = zzahl(1, 8)
        fkt = (r' \sqrt[' + gzahl(wurzel) + ']{' + vorz_v_aussen(faktor, 'x^{' + gzahl(exponent) + '}')
               + vorz_str(summand) + '}')
        fkt_uf = ('~=~(' + vorz_v_aussen(faktor, 'x') + '^{' + gzahl(exponent) + r'} '
                  + vorz_str(summand) + r')^{' + gzahl(Rational(1, wurzel)) + '}')
        fkt_abl = (r' \Big(' + vorz_v_aussen(Rational(faktor * exponent, wurzel), 'x')
                   + '^{' + gzahl(exponent - 1) + r'} \Big) \cdot (' + vorz_v_aussen(faktor, 'x')
                   + '^{' + gzahl(exponent) + r'} ' + vorz_str(summand) + r')^{'
                   + gzahl(Rational(1 - wurzel, wurzel)) + r'}')
        return fkt, fkt_uf, fkt_abl, pkt

    aufgaben = {'a': funktion(2), 'b': polynom(), 'c': wurzel(), 'd': poly_wurzel(), 'e': fkt_exp(), 'f': fkt_ln(),
                'g': fkt_wurzel_exp(), 'h': verkettet_exp(), 'i': verkettet_ln(), 'j': verkettet_wurzel()}

    aufg = ''
    lsg = (r' \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe'
           r'~der~elementaren~Ableitungsregeln.} \\')
    punkte = 0
    for element in teilaufg:
        fkt, fkt_uf, fkt_abl, pkt = aufgaben[element]
        if (i+1)%3 != 0:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad f(x)~=~' + fkt
            if i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        else:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad f(x)~=~' + fkt + r' \\\\'
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad f(x) ~=~' + fkt + fkt_uf
               + r' \quad \to \quad f^{ \prime }(x)~=~ \bm{' + fkt_abl + r'} \quad (' + str(pkt) + r'P) \\')
        punkte += pkt
        i += 1

    lsg = lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def kurvendiskussion_exponentialfkt_01(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], ableitung=False):
    liste_punkte = []
    liste_bez = []
    i = 0
    extrema_xwert = zzahl(1,3)
    extrema_ywert = zzahl(1,3)
    if extrema_xwert > 0:
        y_vers = -1*nzahl(0,2)
    else:
        y_vers = nzahl(0,2)
    # print(extrema_xwert), # print(extrema_ywert), # print(y_vers)

    # rekonstruktion der exponentialfunktion
    fkt_v = exp(b*x+2)*a*x**2
    fkt_a1 = diff(fkt_v,x)
    gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
    gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
    lsg = solve((gleichung1,gleichung2),(a,b))
    lsg_a = lsg[0][0]
    lsg_b = lsg[0][1]
    # print(lsg)
    fkt = exp(lsg_b*x+2)*lsg_a*x**2 + y_vers
    fkt_str = (vorz_v_aussen(lsg_a,'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b,'x+2') + '}'
               + vorz_str(y_vers))


    # Werte für Angaben zum Zeichnen des Graphen
    ywerte = [(element,fkt.subs(x,element)) for element in range(-5,6)]
    wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
    xmin = wertebereich[0]
    xmax = wertebereich[-1]
    # print(fkt), # print(ywerte), # print(wertebereich), # print(xmin), # print(xmax)
    graph_xyfix(fkt, name='Funktionsgraph')

    # Ableitung der Funktionen
    fkt_a1 = diff(fkt,x)
    fkt_a2 = diff(fkt, x,2)
    fkt_a3 = diff(fkt, x,3)

    fkt_a1_str_zw = (r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot' + gzahl_klammer(lsg_b) + r' \cdot'
                     + vorz_v_innen(lsg_a,'x^2') + r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot'
                     + vorz_v_innen(2*lsg_a,'x'))
    fkt_a2_str_zw = (gzahl(lsg_b) + r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \Big('
                     + vorz_v_aussen(lsg_a*lsg_b,'x^2') + vorz_v_innen(2*lsg_a,'x' + r' \Big)') + r'e^{'
                     + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \Big(' + vorz_v_aussen(2*lsg_a * lsg_b, 'x')
                     + vorz_str(2*lsg_a) + r' \Big)')
    fkt_a3_str_zw = (gzahl(lsg_b) + 'e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                     + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                     + vorz_str(2*lsg_a) + r' \Big)' + 'e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                     + vorz_v_aussen(2*lsg_a * lsg_b**2, 'x') + vorz_v_innen(4 * lsg_a*lsg_b, r' \Big)'))


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
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)
        # print(grenzwert_min), # print(grenzwert_pos)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + latex(grenzwert_min) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if y_vers == 0:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Schnittpunkte der'
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
        if ableitung == False:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_a1_str
                           + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1
        else:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            aufgabe.extend((str(liste_teilaufg[i]) + f') Geben Sie den Zwischenschritt bei der Berechnung'
                           + f'der folgenden Ableitungen an- \n\n', r') \quad f^{ \prime }(x) ~=~' + fkt_a1_str
                           + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str))
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_a1_str_zw + '~=~' + fkt_a1_str
                           + r' \\ \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str_zw + '~=~' + fkt_a2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str_zw  + '~=~' + fkt_a3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1


    if 'd' in teilaufg:
        punkte_aufg = 10
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
                       + vorz_str(2*lsg_a) + r' \Big)'
                       + r' \quad \to \quad x_1~=~0 \quad \mathrm{und} \quad 0~=~ '
                       + vorz_v_aussen(lsg_a*lsg_b,'x') + vorz_str(2*lsg_a) + r' \quad \vert \div '
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

        xwert_wp1 = N(-2/lsg_b - sqrt(2)/abs(lsg_b), 3)
        ywert_wp1 = N(fkt.subs(x,-2/lsg_b - sqrt(2)/abs(lsg_b)), 3)
        ywert_wp1 = N(fkt.subs(x, xwert_wp1),3)
        ywert_wp1_fkt_a1 = N(fkt_a1.subs(x, xwert_wp1),3)

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Tangente und Normale am Wendepunkt '
                                                f'WP({xwert_wp1}|{ywert_wp1}). \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                       + r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(ywert_wp1_fkt_a1,'(x')
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
        loesung.append('neueSeite')
        i += 1


    if 'g' in teilaufg:
        punkte_aufg = 5
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen im Intervall I [{xmin}|{xmax}]. \n\n')
        loesung.extend((str(liste_teilaufg[i])
                        + r') \quad \mathrm{Punkte~für~Koordinatensystem~2P,~Werte~2P,~Graph~1P} \\', 'Figure'))
        i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rekonstruktion_und_extremalproblem(nr, teilaufg=['a','b','c']):
    liste_punkte = []
    liste_bez = []
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
    fkt_str = vorz_v_aussen(x_1,'x') + '^2' + vorz_v_innen(x_2,'x') + vorz_str(x_3)
    fkt_a = fkt*x
    fkt_a_str = vorz_v_aussen(x_1,'x') + '^3' + vorz_v_innen(x_2,'x') + '^2' + vorz_v_innen(x_3,'x')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
               'Rechtecks auf dem Graphen von f. \n', 'Figure']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'Aufgabe_{nr}']
    grafiken_loesung = []
    # grafische Darstellung des Sachverhaltes
    xmax = solve(fkt, x)[1]
    def Darstellung(fkt, xmax, xwert_p, ywert_p, name):
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
        return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

    Darstellung(fkt, xmax, xwert_2, ywert_2, f'Aufgabe_{nr}')

    if 'a' in teilaufg:
        punkte = 19
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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

        z4 = NoEscape(gzahl(a1) + r'$ \cdot II' + vorz_str(-1 * a2) + r' \cdot I $')
        a4 = 0
        b4 = a1 * b2 - a2 * b1
        c4 = a1 - a2
        d4 = a1 * d2 - a2 * d1

        z5 = NoEscape(gzahl(a1) + r'$ \cdot III' + vorz_str(-1 * a3) + r' \cdot I $')
        a5 = 0
        b5 = a1 * b3 - a3 * b1
        c5 = a1 - a3
        d5 = a1 * d3 - a3 * d1

        # Zeile 6 vom LGS:

        z6 = NoEscape(gzahl(b4) + r'$ \cdot III' + vorz_str(-1 * b5) + r' \cdot II $')
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
        aufgabe.append('Von einer Funktion 2. Grades sind die folgenden Punkte gegeben:  S( ' + gzahl(xwert_1) + ' | '
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
                       + gzahl_klammer(c6) + r' \quad \to \quad c~=~' + latex(lsg_c) + r' \quad (2P) } \\'
                       + r' \mathrm{aus~II~folgt:~' + gzahl(b4) + r'b~' + vorz_str(c4)
                       + r' \cdot ~' + gzahl_klammer(lsg_c) + '~=~' + gzahl(d4) + r' \quad \vert ~-~'
                       + gzahl_klammer(c4 * lsg_c) + r' \quad \vert \div ' + gzahl_klammer(b4)
                       + r' \quad \to \quad b~=~' + latex(lsg_b) + r' \quad (2P) } \\'
                       + r' \mathrm{aus~I~folgt:~' + gzahl(a1) + r'~a~' + vorz_str(b1) + r' \cdot '
                       + gzahl_klammer(lsg_b) + vorz_str(c1) + r' \cdot ' + gzahl_klammer(lsg_c) + '~=~'
                       + gzahl(d1) + r' \quad \vert ~-~' + gzahl_klammer(b1 * lsg_b + c1 * lsg_c)
                       + r' \quad \vert \div ' + gzahl_klammer(a1) + r' \quad \to \quad a~=~' + latex(lsg_a)
                       + r' \quad (2P) }  \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        i += 1

    if 'b' in teilaufg:
        punkte = 15
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # zwischenrechnungen
        fkt_1_a = 3 * x_1 * (x ** 2) + 2 * x_2 * x + x_3
        fkt_1_a_str = vorz_v_aussen(3 * x_1,'x^2') + vorz_v_innen(2 * x_2,'x') + vorz_str(x_3)
        fkt_1_a_p = Rational(2*x_2/x_1,3)
        fkt_1_a_p2 = Rational(x_2/x_1,3)
        fkt_1_a_q = Rational(x_3/x_1,3)
        fkt_1_a_pq = 'x^2' + vorz_v_innen(fkt_1_a_p,'x') + vorz_str(fkt_1_a_q)
        fkt_1_a_sqrt_disk = N(sqrt(fkt_1_a_p2 ** 2 - fkt_1_a_q), 3)
        fkt_1_a_lsg = solve(fkt_1_a, x)
        fkt_2_a = 6 * x_1 * x + 2 * x_2
        fkt_2_a_xo = N(fkt_2_a.subs(x,re(fkt_1_a_lsg[1])),3)
        fkt_2_a_str = vorz_v_aussen(6 * x_1, 'x') + vorz_str(2*x_2)
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
                       + r' \quad und \quad A^{ \prime \prime } (x) ~=~' + fkt_2_a_str + r' \quad (2P) } \\'
                       + r' \mathrm{A^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + fkt_1_a_str + r' \quad \vert \div '
                       + gzahl_klammer(3*x_1) + r' \quad \to \quad 0~=~' + fkt_1_a_pq + r' \quad (2P) }\\'
                       + r' \mathrm{ x_{1/2} ~=~ - \frac{' + gzahl(fkt_1_a_p) + r'}{2} \pm \sqrt{ \Big( \frac{'
                       + gzahl(fkt_1_a_p) + r'}{2} \Big) ^2 -' + gzahl_klammer(fkt_1_a_q) + '} ~=~'
                       + gzahl(-1*fkt_1_a_p2) + r' \pm ' + gzahl(fkt_1_a_sqrt_disk) + r' \quad (2P) } \\'
                       + r' \mathrm{x_1 ~=~' + gzahl(N(re(fkt_1_a_lsg[0]),3)) + r' \quad und \quad x_2 ~=~'
                       + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r' \quad (2P) } \\ \mathrm{A^{ \prime \prime }('
                       + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~' + gzahl(6*x_1) + r' \cdot '
                       + gzahl_klammer(N(re(fkt_1_a_lsg[1]),3)) + vorz_str(2*x_2) + r'~=~'
                       + gzahl(fkt_2_a_xo) + r'~<0 \quad \to HP \quad (3P) } \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        i += 1

    if 'b' and 'c' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # Aufgaben und Lösungen
        aufgabe.append(str(teilaufg[i]) + ') Berechne den maximalen Flächeninhalt. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad A(' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~'
                       + gzahl(x_1) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^3'
                       + vorz_str(x_2) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^2'
                       + vorz_str(x_3) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3))
                       + ') ~=~' + gzahl(flaeche) + r' \quad (2P)')
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Aufgaben zur Integralrechnung

def rechenregeln_integrale(nr, teilaufg=['a','b']):
    liste_punkte = [len(teilaufg)]
    liste_bez = [f'{nr}']
    i = 0
    regeln_aufgabe = {r' \int x^n \,dx ~=~ \hspace{10em}': r' \int x^n \,dx ~=~ \frac{1}{n+1} \cdot x^{n+1} + C ',
                      r' \int a \cdot f(x) \,dx ~=~ \hspace{10em}':
                          r' \int a \cdot f(x) \,dx ~=~ a \cdot \int f(x) \,dx ~=~ a \cdot F(x) + C ',
                      r' \int \left( f(x) + g(x) \right) \,dx ~=~ \hspace{10em}':
                      r' \int \left( f(x) + g(x) \right) \,dx ~=~ \int f(x) \,dx + \int g(x) \,dx ~=~ F(x) + G(x) + C',
                      r' \int e^x \,dx ~=~ \hspace{10em}': r' \int e^x \,dx ~=~ e^x + C ',
                      r' \int_{a}^{a} f(x) \,dx ~=~ \hspace{10em}':
                          r' \int_{a}^{a} f(x) \,dx ~=~ \int_{a}^{a} f(x) \,dx ~=~ 0',
                      r' \int_{a}^{b} f(x) \,dx ~=~ \hspace{10em}':
                          r' - \int_{a}^{b} f(x) \,dx ~=~ \int_{b}^{a} f(x) \,dx',
                      r' \int_{a}^{b} f(x) \,dx + \int_{b}^{c} f(x) \,dx ~=~ \hspace{10em}':
                          r' \int_{a}^{b} f(x) \,dx + \int_{b}^{c} f(x) \,dx ~=~ \int_{a}^{c} f(x) \,dx'}
    auswahl = np.random.choice(list(regeln_aufgabe.keys()),2, False)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vervollständige die folgenden Rechenregeln für die Integralrechnung.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    aufg = lsg = ''
    if 'a' in teilaufg:
        aufg = aufg + str(liste_teilaufg[i]) + r') ~' + auswahl[i]
        lsg = lsg + str(liste_teilaufg[i]) + r') ~' + regeln_aufgabe[auswahl[i]] + r' \quad (1P) \\'
        i += 1

    if 'b' in teilaufg:
        aufg = aufg + str(liste_teilaufg[i]) + r') ~' + auswahl[i]
        lsg = (lsg + str(liste_teilaufg[i]) + r') ~' + regeln_aufgabe[auswahl[i]] + r' \quad (1P) \\'
               + r' \mathrm{insgesamt~' + str(len(teilaufg)) + r'~Punkte} \\')
        i += 1
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def unbestimmtes_integral(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g']):
    liste_bez = [nr]
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Bestimme die Stammfunktionen der folgenden Funktionen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []


    def polynom_01():
        konst_i = zzahl(2,20)
        e1_i = nzahl(2,5)
        e2_i = e1_i + nzahl(1,3)
        fkt = 'x^{' + gzahl(e2_i) + '} + x^{' + gzahl(e1_i) + '}' + vorz_str(konst_i)
        fkt_uf = ''
        Fkt = (r' \frac{1}{' + gzahl(e2_i+1) + r'} \cdot x^{' + gzahl(e2_i + 1) + r'} + \frac{1}{' + gzahl(e1_i+1)
               + r'} \cdot x^{' + gzahl(e1_i + 1) + '}' + vorz_str(konst_i) + 'x + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def polynom_02():
        konst_ii = zzahl(2, 20)
        e1_ii = nzahl(2, 5)
        e2_ii = e1_ii + nzahl(2, 4)
        a1 = (e1_ii + 1) * zzahl(1, 10) / 2
        a2 = (e2_ii + 1) * zzahl(1, 10) / 2
        fkt = (vorz_v_aussen(a2, 'x^{' + gzahl(e2_ii) + '}') + vorz_v_innen(a1, 'x^{' + gzahl(e1_ii) + '}')
                      + vorz_str(konst_ii))
        fkt_uf = ''
        Fkt = (vorz_v_aussen(Rational(a2, e2_ii + 1), 'x^{' + gzahl(e2_ii + 1) + '}')
                      + vorz_v_innen(Rational(a1, e1_ii + 1), 'x^{' + gzahl(e1_ii + 1) + '}')
                      + vorz_v_innen(konst_ii, 'x + C'))
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def e_funktion():
        a1 = zzahl(2, 9)
        k1 = zzahl(1, 19) / 2
        fkt = gzahl(a1) + r' \cdot e^x' + vorz_str(k1)
        fkt_uf = ''
        Fkt = gzahl(a1) + r' \cdot e^x' + vorz_v_innen(k1, 'x + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def trig_funktion():
        a1 = zzahl(2, 9)
        auswahl = random.choice([[latex(a1) + r' \cdot \sin(x)', latex(-1 * a1) + r' \cdot \cos(x) + C'],
                                 [latex(a1) + r' \cdot \cos(x)', latex(a1) + r' \cdot \sin(x) + C']])
        fkt = auswahl[0]
        fkt_uf = ''
        Fkt = auswahl[1]
        pkt = 1
        return fkt, fkt_uf, Fkt, pkt

    def ln_funktion():
        a1 = zzahl(2, 9)
        e1 = nzahl(2, 9)
        a2 = zzahl(2, 9)
        fkt = (vorz_aussen(a1) + r' \frac{' + gzahl(abs(a1)) + '}{x^{' + gzahl(e1) + '}}'
               + vorz(a2) + r'\frac{' + str(abs(a2)) + '}{x}')
        fkt_uf = r'~=~ \int ' + gzahl(a1) + r' x^{' + gzahl(-1 * e1) + '}' + vorz_str(a2) + r'x^{-1} \,dx'
        Fkt = (gzahl(Rational(a1, -1 * e1 + 1)) + 'x^{' + gzahl(-1 * e1 + 1) + '}' + vorz_str(a2)
               + r' \cdot \ln(x) + C')
        pkt = 3
        return fkt, fkt_uf, Fkt, pkt

    def kettenregel():
        a1 = zzahl(3, 20) / 2
        i1 = zzahl(3, 20) / 2
        k1 = zzahl(2, 9)
        e1 = nzahl(2, 9)
        innere = vorz_v_aussen(i1, 'x') + vorz_str(k1)
        auswahl = random.choice([[gzahl(a1) + r' \cdot (' + innere + ')^{' + latex(e1) + '}',
                                  gzahl(Rational(a1, i1 * (e1 + 1))) + r' \cdot (' + innere + ')^{' + latex(e1 + 1)
                                  + '} + C'],
                                 [gzahl(a1) + r' \cdot e^{' + innere + '}',
                                  gzahl(Rational(a1, i1)) + r' \cdot e^{' + innere + '} + C'],
                                 [gzahl(a1) + r' \cdot \sin(' + innere + ')' + vorz_str(k1),
                                  gzahl(Rational(-1 * a1, i1)) + r' \cdot \cos(' + innere + ')'
                                  + vorz_v_innen(k1,'x + C')],
                                 [gzahl(a1) + r' \cdot \cos(' + innere + ')' + vorz_str(k1),
                                  gzahl(Rational(a1, i1)) + r' \cdot \sin(' + innere + ')'
                                  + vorz_v_innen(k1,'x + C')]])
        fkt = auswahl[0]
        fkt_uf = ''
        Fkt = auswahl[1]
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def wurzelfunktion():
        a1 = nzahl(2, 6)
        e1 = a1 + nzahl(2, 4)
        fkt = r' \sqrt[' + gzahl(a1) + ']{x^{' + gzahl(e1) + '}}'
        fkt_uf = r' ~=~ \int x^{' + gzahl(Rational(e1, a1)) + r'} \,dx '
        Fkt = (gzahl(Rational(a1, a1 + e1)) + 'x^{' + gzahl(Rational(a1 + e1, a1)) + '} + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt


    aufgaben = {'a': polynom_01(), 'b': polynom_02(), 'c': e_funktion(), 'd': trig_funktion(), 'e': ln_funktion(),
                'f': kettenregel(), 'g': wurzelfunktion()}

    aufg = ''
    lsg = (r' \mathrm{~Bestimme~die~Stammfunktionen~der~gegebenen~Funktionen.} \\')
    punkte = 0
    for element in teilaufg:
        fkt, fkt_uf, Fkt, pkt = aufgaben[element]
        if (i + 1) % 3 != 0:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad \int ~' + fkt + r'~ \,dx '
            if i + 1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        else:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad \int ~' + fkt + r'~ \,dx \\\\'
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \int ~' + fkt + r'~ \,dx ' + fkt_uf
               + r' \quad \to \quad F(x)~=~' + Fkt + r' \quad (' + str(pkt) + r'P) \\')
        punkte += pkt
        i += 1

    lsg = lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)


    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def bestimmtes_integral(nr, teilaufg=['a', 'b']):
    liste_punkte = []
    liste_bez = []
    i = 0

    nst_1 = zzahl(1, 2)
    nst_2 = nst_1 + nzahl(1, 2) + 0.5
    nst_3 = nst_1 - nzahl(1, 2) - 0.5
    faktor = zzahl(3,7)/2

    fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
    fkt_a1 = faktor
    fkt_a2 = -1 * faktor * (nst_1 + nst_2 + nst_3)
    fkt_a3 = faktor * ((nst_1 * nst_2) + (nst_1 * nst_3) + (nst_2 * nst_3))
    fkt_a4 = -1 * faktor * nst_1 * nst_2 * nst_3
    fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
               + vorz_str(fkt_a4))
    fkt_h_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3 - 1, 'x')
                 + vorz_str(fkt_a4))
    fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
    fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
    fkt_partial_p = -1 * (nst_2 + nst_3)
    fkt_partial_q = (nst_2 * nst_3)

    fkt_1 = collect(expand(diff(fkt, x, 1)), x)
    fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * (nst_1 + nst_2 + nst_3), 3), 'x')
                + vorz_str(Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)))
    p_fkt_1_pq = Rational(-2 * (nst_1 + nst_2 + nst_3), 3)
    q_fkt_1_pq = Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)
    s_fkt = -1 * faktor * nst_1 * nst_2 * nst_3
    Fkt = collect(integrate(fkt,x),x)
    Fkt_str = (vorz_v_aussen(Rational(fkt_a1,4), 'x^4') + vorz_v_innen(Rational(fkt_a2,3), 'x^3')
               + vorz_v_innen(Rational(fkt_a3,2), 'x^2') + vorz_v_innen(fkt_a4,'x'))

    fkt_b2 = nst_1 * fkt_a1
    fkt_c2 = fkt_a2 + fkt_b2
    fkt_b3 = nst_1 * fkt_c2
    fkt_c3 = fkt_a3 + fkt_b3
    fkt_b4 = nst_1 * fkt_c3
    fkt_c4 = fkt_a4 + fkt_b4

    table2 = Tabular('c c|c|c|c', row_height=1.2)
    table2.add_row('', fkt_a1, fkt_a2, fkt_a3, fkt_a4)
    table2.add_hline(2, 5)
    table2.add_row('Berechnung der Partialfunktion  mit Hornerschema: ', '', fkt_b2, fkt_b3, fkt_b4)
    table2.add_hline(2, 5)
    table2.add_row('', fkt_a1, fkt_c2, fkt_c3, fkt_c4)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n', 'Gegeben ist die Funktion:',
               'f(x)~=~' + fkt_str + r' \hspace{20em}']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 12
        liste_punkte.append(punkte)

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Nullstellen der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + fkt_str
                       + r' \quad \mathrm{durch~probieren:~x_1~=~}' + gzahl(nst_1)
                       + r' \quad (2P) \\' + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1) + ')~=~'
                       + latex(fkt_partial) + r' \quad (4P)')
        loesung.append(table2)
        loesung.append(latex(fkt_partial) + r'~=~0 \quad \vert ~ \div '
                       + gzahl_klammer(faktor) + r' \quad \to \quad 0~=~' + latex(fkt_partial_pq)
                       + r' \quad (2P) \\' + r' x_{2/3}~=~ - \frac{' + gzahl_klammer(fkt_partial_p)
                       + r'}{2} \pm \sqrt{ \Big(' + r' \frac{' + latex(fkt_partial_p) + r'}{2} \Big)^2-'
                       + gzahl_klammer(fkt_partial_q) + r'} \quad (2P) \\' + r' x_2~=~' + gzahl(round(nst_2, 3))
                       + r' \quad \mathrm{und} \quad x_3~=~' + gzahl(round(nst_3, 3)) + r' \quad (2P) \\'
                       + r'S_{x_1}(' + gzahl(nst_1) + r'\vert 0) \quad S_{x_2}(' + gzahl(round(nst_2, 3))
                       + r' \vert 0) \quad S_{x_3}(' + gzahl(round(nst_3, 3)) + r' \vert 0)' + lsg
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)

        lsg_A1 = N(Fkt.subs(x, nst_1) - Fkt.subs(x, nst_3),3)
        lsg_A2 = N(Fkt.subs(x, nst_2) - Fkt.subs(x, nst_1),3)
        lsg_A = abs(lsg_A1) + abs(lsg_A2)

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Fläche, '
                       + f'die der Graph mit der x-Achse einschließt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad A~=~ \left| \int_{' + gzahl(N(nst_3,2)) + '}^{'
                       + gzahl(nst_1) + '}' + fkt_str + r' ~ \,dx \right| + \left| \int_{' + gzahl(nst_1) + '}^{'
                       + gzahl(nst_2) + '}' + fkt_str + r' ~ \,dx \right| \quad (2P) \\ =~ \left| \left[ '
                       + Fkt_str + r' \right]_{' + gzahl(N(nst_3,2)) + '}^{' + gzahl(nst_1)
                       + r'} \right| + \left| \left[ ' + Fkt_str + r' \right]_{'
                       + gzahl(N(nst_1,2)) + '}^{' + gzahl(nst_2) + r'} \right| \quad (2P) \\'
                       + r'=~ \left| ' + gzahl(lsg_A1) + r' \right| + \left| ' + gzahl(lsg_A2)
                       + r' \right| ~=~' + gzahl(lsg_A) + r' \quad (2P) \\'
                       + r'\mathrm{insgesamt~' + str(punkte) + '~Punkte}')

        i += 1


    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Komplexe Aufgaben (d.h. zur Differenzial- und Integralrechnung)

def kurvendiskussion_polynome(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']):
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
        fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
                   + vorz_str(fkt_a4))
        fkt_h_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3 - 1, 'x')
                     + vorz_str(fkt_a4))
        fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
        fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
        fkt_partial_p = -1 * (nst_2 + nst_3)
        fkt_partial_q = (nst_2 * nst_3)

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * (nst_1 + nst_2 + nst_3), 3), 'x')
                    + vorz_str(Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)))
        p_fkt_1_pq = Rational(-2 * (nst_1 + nst_2 + nst_3), 3)
        q_fkt_1_pq = Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)
        s_fkt = -1 * faktor * nst_1 * nst_2 * nst_3

    else:
        nst_1 = zzahl(1, 3)
        quadr_nst_23 = nzahl(2, 25)
        nst_2 = math.sqrt(quadr_nst_23)
        nst_3 = -1 * nst_2
        faktor = zzahl(3, 8) / 2

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * nst_1
        fkt_a3 = faktor * (-1 * quadr_nst_23)
        fkt_a4 = faktor * nst_1 * quadr_nst_23
        fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
                   + vorz_str(fkt_a4))
        fkt_h_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3 - 1, 'x')
                     + vorz_str(fkt_a4))
        fkt_partial = faktor * (x ** 2 - quadr_nst_23)
        fkt_partial_pq = x ** 2 - quadr_nst_23
        fkt_partial_p = 0
        fkt_partial_q = -1 * quadr_nst_23

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * nst_1, 3), 'x') +
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

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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

        x_12_fkt_1 = solve(fkt_1, x)
        x_1_fkt_1 = round(x_12_fkt_1[0], 3)
        x_2_fkt_1 = round(x_12_fkt_1[1], 3)

        fkt_2 = expand(diff(fkt, x, 2))
        fkt_2_str = vorz_v_aussen(6 * faktor, 'x') + vorz_str(-2 * faktor * (nst_1 + nst_2 + nst_3))
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

        xwert_Wendepunkt = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor), 3)
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

        xwert_wp1 = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor), 3)
        ywert_wp1 = N(fkt.subs(x, xwert_wp1), 3)
        ywert_wp1_fkt_1 = N(fkt_1.subs(x, xwert_wp1), 3)
        fkt_t = ywert_wp1_fkt_1 * (x - xwert_wp1) + ywert_wp1
        fkt_n = (-1 / ywert_wp1_fkt_1) * (x - xwert_wp1) + ywert_wp1
        # print('Wendepunkt: ' + str(xwert_wp1))
        # print('f(x)=' + latex(fkt))
        # print('f`(x)=' + latex(fkt_1))
        # print('t(x)=' + latex(fkt_t))
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Wendetangente und die Wendenormale '
                                                f'der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                       + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                       + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                       + vorz_v_aussen(ywert_wp1_fkt_1, '(x') + vorz_v_innen(-1 * N(xwert_wp1, 3), ')')
                       + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1, 'x')
                       + vorz_str(N(-1 * ywert_wp1_fkt_1 * xwert_wp1 + ywert_wp1, 3))
                       + r' \quad (3P) \\ \mathrm{Die~Steigung~der~Normale~am~Wendepunkt~wird~berechnet~mit \quad'
                       + r' m_n ~=~ \frac{-1}{f^{ \prime }(x_{w})} \quad und~daraus~folgt:} \\'
                       + r'n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                       + r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1 / ywert_wp1_fkt_1, '(x')
                       + vorz_v_innen(-1 * N(xwert_wp1, 3), ')') + vorz_str(ywert_wp1) + '~=~'
                       + vorz_v_aussen(-1 / ywert_wp1_fkt_1, 'x')
                       + vorz_str(N(xwert_wp1 / ywert_wp1_fkt_1 + ywert_wp1, 3))
                       + r' \quad (3P) \\' + r' \mathrm{insgesamt~' + str(6) + r'~Punkte}')
        loesung.append('neueSeite')
        # xmin = int(round(nst_3 - 0.4, 0))
        # xmax = int(round(nst_2 + 0.4, 0))
        # Graph(xmin,xmax, fkt, name='latex(fkt_t)')
        liste_punkte.append(punkte)
        i += 1

    if 'g' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))
        # plot(fkt, (x,xmin_f,xmax_f) ,show=False)

        aufgabe.append(str(liste_teilaufg[i])
                       + f') Zeichne den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ] \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Koordinatensystem~(2P) \quad Werte~(2P)'
                                                r' \quad Graph~(1P) \to \quad insgesamt~(5P)}')
        Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
        loesung.append('Figure')

        liste_punkte.append(5)
        i += 1

    if 'h' in teilaufg and (nst_1 > 0 or nst_2 > 0 or nst_3 > 0) and nst_1 * nst_2 * nst_3 != 0:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        Fkt = integrate(fkt, x)
        Fkt_str = (vorz_v_aussen(Rational(fkt_a1, 4), 'x^4') + vorz_v_innen(Rational(fkt_a2, 3), 'x^3')
                   + vorz_v_innen(Rational(fkt_a3, 2), 'x^2') + vorz_v_innen(fkt_a4, 'x'))

        def erste_positive_nst(vec):
            # print(vec)
            vec.sort()
            # print(vec)
            for element in vec:
                if element > 0:
                    # print(element)
                    return element
            exit('keine positive Nullstelle')

        obere_grenze = N(erste_positive_nst([nst_1, nst_2, nst_3]), 3)
        loesung_integral = Fkt.subs(x, obere_grenze)

        aufgabe.extend((f'Der Graph von f schließt, mit der x-Achse und der y-Achse '
                        + ' rechts vom Ursprung eine Fläche ein. \n\n',
                        str(liste_teilaufg[i]) + f') Berechne die eingeschlossen Fläche. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \left| \int \limits_0^{' + gzahl(obere_grenze) + '}' + fkt_str
                       + r'~ \mathrm{d}x \right| ~=~ \left| \left[' + Fkt_str + r' \right]_{0}^{' + gzahl(obere_grenze)
                       + r'} \right| ~=~' + latex(abs(N(loesung_integral, 3))) + r' \quad (4P) \\')

        liste_punkte.append(4)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# nochg einzupflegen

def kurvendiskussion_polynom_parameter_1(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f']):
    liste_punkte = []
    liste_bez = []
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
    fkt_a1_str = (vorz(nst_1+nst_3) + '(' + gzahl(abs(faktor * (nst_1 + nst_3))) + r'a'
                  + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
    fkt_a2_str = (vorz(-1 * faktor) + '(' + gzahl(abs(faktor)) + r'a '
                  + vorz_str(-1 * faktor * (nst_1 + nst_3)) + ')')
    fkt_a3_str = gzahl(faktor)

    fkt_a0_str = vorz_str(-1*faktor*nst_1*nst_3) + r' a'

    fkt_str = fkt_a3_str + r'x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str + r' \cdot x ~' + fkt_a0_str

    print(fkt), print(fkt_str)

    if nst_1 < 0:
        db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}'
    else:
        db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > ' + gzahl(nst_1) + r'}'

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))),
               r' \mathrm{Gegeben~ist~die~Funktion \quad  f(x)~=~' + fkt_str + r' \quad ' + db_bereich + r'}']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        grenzwert_neg = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + gzahl(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + gzahl(grenzwert_neg) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        fkt_a1_str_neg = (vorz(-1*(nst_1 + nst_3)) + '(' + gzahl(abs(faktor * (nst_1 + nst_3))) + r' a'
                          + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
        fkt_a3_str_neg = gzahl(-1*faktor)
        fkt_sym = (fkt_a3_str_neg + 'x^3' + fkt_a2_str + 'x^2' + fkt_a1_str_neg
                   + 'x' + fkt_a0_str)
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad f(-x)~=~' + fkt_sym
                                                 + r' \neq  f(x)  \neq -f(x) \\'
                                                 + r'\mathrm{nicht~symmetrisch} \quad (3P) \\'))
        i += 1
    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 15
        liste_punkte.append(punkte)
        # hier werden die Koeffizenten für das Hornerschema berechnet
        fkt_b2 = nst_1 * faktor
        fkt_c2 = -1 * faktor * a - faktor * nst_3
        fkt_b1 = -1 * faktor * nst_1 * a - faktor * nst_1 * nst_3
        fkt_c1 = faktor * nst_3 * a
        fkt_b0 = faktor * nst_1 * nst_3 * a
        fkt_partial = faktor * x**2 + fkt_c2 *x + fkt_c1

        # hier werden die Koeffizenten als String für das Hornerschema berechnet
        fkt_c2_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-1 * faktor, r' a')
                      + vorz_v_innen(-1 * faktor * nst_3,r') \cdot x'))
        fkt_c1_str = vorz_str(faktor*nst_3) + r' a'
        fkt_p = -1*a - nst_3    # -(a+x_3)
        fkt_q = nst_3 * a
        fkt_disk = ((fkt_p/2)**2)-fkt_q
        fkt_p_str = '-(a' + vorz_str(nst_3) + ')'
        fkt_q_str = vorz_str(nst_3) + r' a'
        fkt_partial_str = gzahl(faktor) + r' \cdot x^2' + fkt_c2_str + fkt_c1_str
        fkt_pq_str = 'x^2' + fkt_p_str + r' \cdot x' + fkt_q_str
        fkt_disk_str = r' \frac{a^2' + vorz_str(-1*2*nst_3) + r' a' + vorz_str(nst_3**2) + '}{4}'

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('',fkt_a3,latex(collect(fkt_a2,a)), latex(collect(fkt_a1,a)), latex(collect(fkt_a0,a)))
        table2.add_hline(2, 5)
        table2.add_row('Partialpolynom mit Horner Schema berechnen: ',' ',
                       latex(collect(fkt_b2,a)), latex(collect(fkt_b1,a)), latex(collect(fkt_b0,a)))
        table2.add_hline(2, 5)
        table2.add_row('',fkt_a3, latex(collect(fkt_c2,a)), latex(collect(fkt_c1,a)), '0')

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Schnittpunkte mit den Achsen der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                                                 + fkt_str + r' \quad (1P) \\ \mathrm{durch~probieren:~x_1~=~}'
                                                 + vorz_str(nst_1) + r' \quad (1P) \\'
                                                 + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1)
                                                 + r')~= \\ =~' + fkt_partial_str + r' \quad (4P)'))
        loesung.append(table2)
        loesung.append('0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + gzahl_klammer(faktor) +
                       r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2P) \\'
                       r' x_{2/3}~=~ - \frac{' + fkt_p_str + r'}{2} \pm \sqrt{ \Big(' +
                       r' \frac{' + fkt_p_str + r'}{2} \Big)^2-(' + latex(fkt_q) +
                       r')} ~=~ ' + gzahl(-1*fkt_p/2) + r' \pm \sqrt{'
                       + fkt_disk_str + r' } \quad (4P) \\ x_{2/3}~=~' + gzahl(-1*fkt_p/2) + r' \pm ('
                       + gzahl((a-nst_3)/2) + r') \quad \to \quad x_2~=~' + gzahl(nst_3)
                       + r' \quad \mathrm{und} \quad x_3~=~a \quad (3P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 19
        liste_punkte.append(punkte)
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

        fkt_1_a2_str = gzahl(3*faktor)
        fkt_1_a1_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor,r' a')
                        + vorz_v_innen(-2 * faktor * (nst_1 + nst_3),')'))
        fkt_1_a0_str = (vorz(faktor * (nst_1 + nst_3)) + '('
                         + vorz_v_aussen(abs(faktor * (nst_1 + nst_3)), r' a')
                         + vorz_v_innen(-1 * faktor * nst_1 * nst_3, ')'))

        # p und q in der pq-Formel
        fkt_1_p_str = r'-( \frac{2}{3} a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')'
        fkt_1_q_str = (vorz(nst_1+nst_3) + '(' + vorz_v_aussen(Rational(-1 * (nst_1 + nst_3), 3), r' a')
                       + vorz_v_innen(Rational(-1 * (nst_1 * nst_3), 3),')'))
        fkt_1_q2_str = (vorz_v_aussen(Rational((nst_1 + nst_3), 3), r' a')
                        + vorz_str(Rational((nst_1 * nst_3), 3)))

        # p und q in umgeformter pq-Formel
        fkt_1_p2_str = r'( \frac{2}{3} a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')^2'
        fkt_1_p3_str = r' \frac{1}{3} a' + vorz_str(Rational((nst_1 + nst_3), 3))
        fkt_1_q3_str = (vorz(-1*(nst_1 + nst_3)) + r' \frac{4 \cdot ('
                        + vorz_v_aussen(Rational(abs(nst_1 + nst_3), 3), r' a')
                        + vorz_v_innen(Rational(-1 * (nst_1 * nst_3), 3), ') }{4}'))

        # Diskriminante der Wurzel
        fkt_1_disk_str = (r' \frac{1}{9} \cdot ((a' + vorz_str(-1*(nst_1+nst_3)) + r')^2'
                          + vorz_str(-4*nst_1*nst_3) + ')')

        fkt_1_str = fkt_1_a2_str + 'x^2' + fkt_1_a1_str + 'x' + fkt_1_a0_str
        fkt_1_pq_str = 'x^2' + fkt_1_p_str + r' \cdot x' + fkt_1_q_str
        fkt_2_str = gzahl(6*faktor) + 'x' + fkt_1_a1_str
        fkt_3_str = gzahl(6*faktor)
        fkt_1_x1 = fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str + r'}'
        fkt_1_x2 = fkt_1_p3_str + r' - \sqrt{' + fkt_1_disk_str + r'}'

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie die Extremstellen der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_1_str
                       + r' \quad (1P) \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                       + r' \quad \mathrm{und} \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str
                       + r' \quad (2P) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_1_str + r' \vert ~ \div ' + gzahl_klammer(3 * faktor) + r' \quad (1P) \\'
                       r'0~=~ ' + fkt_1_pq_str + r' \quad (1P) \\' + r' x_{1/2}~=~ - \frac{'
                       + fkt_1_p_str + r'}{2} \pm \sqrt{ \Big(' + r' \frac{'
                       + fkt_1_p_str + r'}{2} \Big)^2-(' + fkt_1_q2_str + r')} \quad (2P) \\ =~ '
                       + fkt_1_p3_str + r' \pm \sqrt{' + r' \frac{' + fkt_1_p2_str
                       + r'}{4}' + fkt_1_q3_str + r'} ~=~' + fkt_1_p3_str + r' \pm \sqrt{' + fkt_1_disk_str
                       + r'} \quad (4P) \\ x_1~=~' + fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{und} \quad x_2~=~' + fkt_1_p3_str + r' - \sqrt{'
                       + fkt_1_disk_str + r'}  \quad (2P) \\'
                       + r'f^{ \prime \prime } (x_2) ~=~' + gzahl(6*faktor)
                       + r' \cdot \Big( ' + fkt_1_x1 + r' \Big) ' + fkt_1_a1_str
                       + r' \quad (1P) \\ ~=~ + \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{>~0} \quad \to TP \quad (2P) \\ f^{ \prime \prime } (x_2) ~=~'
                       + gzahl(6 * faktor) + r' \cdot \Big( ' + fkt_1_x2
                       + r' \Big) ' + fkt_1_a1_str + r' \quad (1P) \\ ~=~ - \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{<~0} \quad \to HP \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'e' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        liste_punkte.append(punkte)
        fkt_1_a1_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor, r' a')
                        + vorz_v_innen(-2 * faktor * (nst_1 + nst_3),')'))
        fkt_1_a1_str_neg = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor, r' a')
                            + vorz_v_innen(-2 * faktor * (nst_1 + nst_3), ')'))

        xwert_wendepunkt = r' \frac{1}{3} a' + vorz_str(Rational((nst_1+nst_3),3))
        fkt_2_str = gzahl(6*faktor) + 'x' + fkt_1_a1_str
        fkt_3_str = gzahl(6*faktor)

        aufgabe.append(str(liste_teilaufg[i]) + ') Überprüfen Sie rechnerisch auf mögliche Wendepunkte der Funktion f '
                                                'mithilfe des hinr. Kriteriums. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ~' + fkt_1_a1_str_neg + r' \quad \vert \div '
                       + gzahl_klammer(6 * faktor) + r' \quad (1P) \\ x_1~=~ \frac{1}{3} a'
                       + vorz_str(Rational((nst_1+nst_3),3))
                       + r' \quad (1P) \quad \to \quad f^{ \prime \prime \prime }(' + xwert_wendepunkt
                       + r') ~=~ ' + gzahl(6*faktor) + r' \quad \neq 0 \quad \to \quad Wendepunkt \quad (3P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'f' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        liste_punkte.append(punkte)
        wert_a_wp = nzahl(1,5)
        xwert_wp = Rational((wert_a_wp + nst_1 + nst_3),3)
        xwert_wendepunkt = r' \frac{1}{3} a' + vorz_str(Rational((nst_1 + nst_3), 3))
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Wert von a,'
                                                f' bei dem der Wendepunkt an der Stelle x = {xwert_wp} ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad ' + gzahl(xwert_wp) + '~=~' + xwert_wendepunkt
                                                 + r' \quad \vert ~' + gzahl(Rational(-1 * (nst_1 + nst_3), 3))
                                                 + r' \quad \vert \cdot 3 \quad \to \quad a~=~'
                                                 + str(wert_a_wp) + r' \quad (3P) \\'
                                                 + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\'))
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def kurvendiskussion_polynom_parameter_2(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
    liste_punkte = []
    liste_bez = []
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

    nst_1_str = gzahl(faktor_1) + 'a'
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
    nst_3_str = gzahl(faktor_3) + 'a'

    # Aufstellen der Funktionsgleichung
    fkt = collect(expand(faktor * (x - faktor_1 * a) * (x - faktor_2 * a) * (x - faktor_3 * a)),x)

    # Koeffizienten der Funktion
    fkt_a3 = faktor
    fkt_a2 = -1*faktor * (faktor_1 + faktor_2 + faktor_3)
    fkt_a1 = faktor*(faktor_1*faktor_2 + faktor_2*faktor_3 + faktor_1*faktor_3)
    fkt_a0 = -1*faktor*faktor_1*faktor_2*faktor_3

    fkt_str = (vorz_v_aussen(fkt_a3, r'x^3') + vorz_v_innen(fkt_a2, r'a \cdot x^2')
               + vorz_v_innen(fkt_a1, r'a^2 \cdot x') + vorz_v_innen(fkt_a0, r'a^3'))

    print(fkt), print(fkt_str)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion']
    aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    # Auswahl des Wertes von a für Teilaufgabe g und h
    a1 = nzahl(1, 4)
    a2 = nzahl(1,6)/2
    while a1 == a2:
        a2 = nzahl(1, 6) / 2


    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        grenzwert_neg = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~' + \
                       gzahl(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} ' + \
                       fkt_str + '~=~' + gzahl(grenzwert_neg) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        liste_punkte.append(punkte)
        fkt_sym = fkt.subs(x, -x)
        fkt_sym_str = (gzahl(-1 * fkt_a3)+ r'x^3 ~' + vorz_str(fkt_a2) + r'a \cdot x^2 ~'
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
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 14
        liste_punkte.append(punkte)
        # hier werden die Koeffizenten für das Hornerschema berechnet
        fkt_b2 = faktor * faktor_2
        fkt_c2 = -1 * faktor * (faktor_1 + faktor_3)
        fkt_b1 = -1 * faktor * faktor_2 * (faktor_1 + faktor_3)
        fkt_c1 = faktor * faktor_1 * faktor_3
        fkt_b0 = faktor*faktor_1*faktor_2*faktor_3
        # hier werden das Partialpolynom (Ergebnis Hornerschema) und die Gleichung für die pq-Formel berechnet
        fkt_partial = faktor * x**2 + fkt_c2 * a * x + fkt_c1 * a**2
        fkt_partial_str = (gzahl(faktor) + r' \cdot x^2' + vorz_str(fkt_c2) + r' a \cdot x'
                           + vorz_str(fkt_c1) + r' a^2')
        fkt_p = -1 * (faktor_1 + faktor_3)
        fkt_q = faktor_1 * faktor_3
        fkt_pq_str = 'x^2' + vorz_str(fkt_p) + r' a \cdot x' + vorz_str(fkt_q) + r' a^2'
        fkt_disk = Rational((faktor_1 - faktor_3)**2,4)

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('', latex(fkt_a3), NoEscape('$' + latex(fkt_a2*a) + '$'),
                       NoEscape('$' + latex(fkt_a1*a**2) + '$'), NoEscape('$' + latex(fkt_a0*a**3) + '$'))
        table2.add_hline(2, 5)
        table2.add_row('Partialpolynom mit Horner Schema berechnen: ' , '', NoEscape('$' + latex(fkt_b2*a) + '$'),
                       NoEscape('$' + latex(fkt_b1*a**2) + '$'), NoEscape('$' + latex(fkt_b0*a**3) +'$'))
        table2.add_hline(2, 5)
        table2.add_row('', NoEscape('$' + latex(fkt_a3) + '$'),
                       NoEscape('$' + latex(fkt_c2*a) + '$'), NoEscape('$' + latex(fkt_c1*a**2) + '$'), '0')

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Schnittpunkte mit den Achsen der Funktion f, '
                                                f'wenn eine Nullstelle bei {nst_2_str} ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                                                 + fkt_str + r' \quad (1P) \\ \mathrm{mit~x_1='
                                                 + nst_2_str + r'~folgt:} \quad (' + fkt_str
                                                 + r')~ \div ~(x' + nst_2_str_neg + r')~=~ \\' + fkt_partial_str
                                                 + r' \quad (4P)'))
        loesung.append(table2)
        loesung.append('0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + gzahl_klammer(faktor) +
                       r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2P) \\'
                       r' x_{2/3}~=~ - \frac{' + latex(fkt_p) + r'a}{2} \pm \sqrt{ \Big(' +
                       r' \frac{' + latex(fkt_p) + r'a}{2} \Big)^2-(' + latex(fkt_q) +  # p war grundlos ins Minus gestzt
                       r'a^2)} ~=~ ' + gzahl(Rational((faktor_1 + faktor_3),2)) + r'a \pm \sqrt{'
                       + latex(fkt_disk) + r' a^2} \quad (2P) \\ x_{2/3}~=~'
                       + gzahl(Rational(faktor_1 + faktor_3,2)) + r' a \pm \Big('
                       + gzahl(Rational(abs(faktor_1 - faktor_3),2)) + r' \Big) a \quad \to \quad x_2~=~'
                       + gzahl(faktor_1) + r'a \quad \mathrm{und} \quad x_3~=~'
                       + gzahl(faktor_3) + r'a \quad (3P) \\ S_{x_2}(' + nst_1_str + r'\vert 0) \quad S_{x_1}('
                       + nst_2_str + r' \vert 0) \quad S_{x_3}(' + nst_3_str + r' \vert 0) \quad \mathrm{sowie}'
                       r' \quad S_y(0 \vert' + gzahl(fkt_a0) + r'a^3) \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 14
        liste_punkte.append(punkte)
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
            lsg_extrema_1 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad HP(' + gzahl(N(x_1_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_1_fkt,3)) + r') \quad (2P) \\')
        else:
            lsg_extrema_1 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad TP(' + gzahl(N(x_1_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_1_fkt,3)) + r') \quad (2P) \\')

        if x_2_fkt_2.subs(a,1) < 0:
            lsg_extrema_2 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad HP(' + gzahl(N(x_2_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_2_fkt,3)) + r') \quad (2P) \\')
        else:
            lsg_extrema_2 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad TP(' + gzahl(N(x_2_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_2_fkt,3)) + r') \quad (2P) \\')

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
        fkt_2_str = gzahl(6*faktor) + 'x' + vorz_str(fkt_1_a1) + r'a'

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrempunkte der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_1_str
                       + r' \quad \mathrm{und} \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                       + r' \quad (2P) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_1_str + r' \vert ~ \div ' + gzahl_klammer(3 * faktor) + r' \quad (1P) \\'
                       r'0~=~ ' + fkt_1_pq_str + r' \quad (1P) \\' + r' x_{1/2}~=~ - \frac{'
                       + gzahl(fkt_1_p) + r' a}{2} \pm \sqrt{ \Big( \frac{'
                       + gzahl(fkt_1_p) + r' a}{2} \Big)^2 - \Big(' + gzahl(fkt_1_q)
                       + r' a^2 \Big) } \quad (1P) \\ =~ ' + gzahl(N(-1*fkt_1_p/2,3)) + r' a \pm \sqrt{'
                       + gzahl(N(fkt_1_disk,3)) + r' a^2} \quad ~=~ ' + gzahl(N(-1*fkt_1_p/2,3)) + r' a \pm '
                       + gzahl(N(fkt_1_sqrt,3)) + r' a \quad (1P) \\'
                       + r'x_1~=~' + gzahl(-1*fkt_1_p/2) + r' a ~-~' + gzahl(N(fkt_1_sqrt,3))
                       + r' a~=~' + gzahl(N(x_1_fkt_1,3)) + r' \quad \mathrm{und} \quad '
                       + r'x_2~=~' + gzahl(-1*fkt_1_p/2) + r' a~+~' + gzahl(N(fkt_1_sqrt,3))
                       + r' a~=~' + gzahl(N(x_2_fkt_1,3)) + r' \quad (2P) \\'
                       + r'f^{ \prime \prime } (' + gzahl(N(x_1_fkt_1,3)) +') ~=~' + gzahl(6*faktor) + r' \cdot ('
                       + gzahl(N(x_1_fkt_1,3)) + ')' + vorz_str(fkt_1_a1) + r' a ~=~'
                       + gzahl(N(x_1_fkt_2,3)) + r' \quad (1P)' + lsg_extrema_1
                       + r' f^{ \prime \prime } (' + gzahl(N(x_1_fkt_2,3)) + ') ~=~' + gzahl(6 * faktor)
                       + r' \cdot (' + gzahl(N(x_2_fkt_1,3)) + ')' + gzahl(fkt_1_a1) + 'a  ~=~'
                       + gzahl(N(x_2_fkt_2,3)) + r' \quad (2P)' + lsg_extrema_2
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'e' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        liste_punkte.append(punkte)
        fkt_2_a0 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
        fkt_2_str = gzahl(6*faktor) + 'x' + vorz_str(fkt_2_a0) + 'a'
        xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3),3)
        xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3)/3,3)
        ywert_wp_dezimal = N(fkt.subs(x,xwert_wp_bruch*a),3)
        fkt_3_str = gzahl(6*faktor)

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die möglichen Wendepunkte der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                       + r' \quad \to \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ~' + vorz_str(-1*fkt_2_a0) + r'a \quad \vert \div '
                       + gzahl_klammer(6 * faktor) + r' \quad (1P) \\ x_1~=~' + gzahl(xwert_wp_bruch) + 'a ~=~'
                       + gzahl(xwert_wp_dezimal) + r'a \quad (1P) \quad \to \quad f^{ \prime \prime \prime }('
                       + gzahl(xwert_wp_bruch) + ') ~=~ ' + fkt_3_str
                       + r' \quad \neq 0 \quad \to \quad \mathrm{Wendepunkt} (' + gzahl(xwert_wp_bruch)
                       + r'a \vert ' + gzahl(ywert_wp_dezimal) + r') \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'f' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        liste_punkte.append(punkte)
        xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3), 3)
        xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3) / 3)
        ywert_wp_dezimal = N(fkt.subs(x, xwert_wp_bruch*a), 3)
        if Rational(3,(faktor_1 + faktor_2 + faktor_3)) > 0:
            abhängigkeit = r'\mathrm{mit~x \in \mathbb{R} ~und~ x > 0}'
        else:
            abhängigkeit = r'\mathrm{mit~x \in \mathbb{R} ~und~ x < 0}'

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Ortskurve der Wendepunkte der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad x ~=~' + (gzahl(xwert_wp_bruch)) + r'a \quad \vert \div'
                       + gzahl_klammer(Rational((faktor_1 + faktor_2 + faktor_3),3)) + r' \quad \to \quad a~=~'
                       + gzahl(Rational(3,(faktor_1 + faktor_2 + faktor_3))) + r'x \quad' + abhängigkeit
                       + r'\quad (2P) \\ \mathrm{einsetzen~in~y} ~=~' + gzahl(ywert_wp_dezimal) + '~=~'
                       + gzahl(ywert_wp_dezimal/a**3) + r' \Big(' + gzahl(Rational(3,(faktor_1 + faktor_2 + faktor_3)))
                       + r'x \Big)^3 ~=~' + gzahl(N((ywert_wp_dezimal/a**3)*(3/(faktor_1 + faktor_2 + faktor_3))**3,4))
                       + r'x^3 \quad (3P) \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'g' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        punkte = 4
        liste_punkte.append(punkte)
        nst_1_a1 = faktor_1 * a1
        nst_3_a1 = faktor_3 * a1
        fkt_a1 = expand(faktor * (x - faktor_1 * a1) * (x - faktor_2 * a1) * (x - faktor_3 * a1))
        xmin_f = int(nst_1_a1 - 1)
        xmax_f = int(nst_3_a1 + 1)
        Graph(xmin_f,xmax_f,fkt_a1,name=f'Aufgabe_{nr}{liste_teilaufg[i]}')
        aufgabe.extend(('In der folgenden Abbildung ist ein Graph der Parameterfunktion dargestellt. '
                        'Dabei wurde für a ein Wert aus den natürlichen Zahlen gewählt.', 'Figure',
                        str(liste_teilaufg[i]) + f') Bestimme aus dem Graphen den zugehörigen Wert von a. '
                        + f'Begründe deine Aussage. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~zweite~Nullstelle~des'
                       + r'~Graphen~liegt~bei~ca.~x_2=' + str(faktor_2*a1)
                       + r'.~} \mathrm{Die~berechnete~Nullstelle~liegt~bei~x_2=' + nst_2_str
                       + r'.~} \\ \mathrm{Damit~gilt:~}' + str(faktor_2*a1) + '~=~' + nst_2_str
                       + r' \quad \to \quad a~=~' + str(a1) + r'. \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'h' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        punkte = 5
        liste_punkte.append(punkte)
        nst_1_a2 = faktor_1 * a2
        nst_3_a2 = faktor_3 * a2
        fkt_a2 = expand(faktor * (x - faktor_1 * a2) * (x - faktor_2 * a2) * (x - faktor_3 * a2))
        xmin_f = int(round(nst_1_a2 - 0.5,0))
        xmax_f = int(round(nst_3_a2 + 0.5,0))
        Graph(xmin_f,xmax_f,fkt_a2,name=f'Loesung_{nr}{liste_teilaufg[i]}')
        aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen von f für a = {gzahl(a2)} im '
                       + f'Intervall [ {xmin_f} | {xmax_f} ].')
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Die~folgende~Abbildung~zeigt~die~Lösung.~(5P)}',
                        'Figure'))
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
