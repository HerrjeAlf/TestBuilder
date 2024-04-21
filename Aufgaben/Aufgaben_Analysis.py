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
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
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
                       + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~~Steigungsdreieck~(1P),~Steigung~'
                         r'\mathbf{m=' + gzahl(steigung_dreieck) + r'}~bestimmt~(1P)}')

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
            + vorz_str(-1 * x_wert_1) + r'} ~=~\mathbf{'
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
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt,
                             r'',
                             'f', f'Loesung_{nr}{liste_teilaufg[i]}',
                             xwerte_dy, ywerte_dy, xwerte_dx, ywerte_dx,
                            xwerte_geraden, ywerte_sekante, xwerte_dy_c, ywerte_dy_c, xwerte_dx_c, ywerte_dx_c,
                            xwerte_geraden, ywerte_tangente)
            aufgabe.append(str(liste_teilaufg[i])
                           + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')

        loesung.extend((str(liste_teilaufg[i])
                       + r') \quad \mathrm{Tangente~an~Punkt~(1P),~~Steigungsdreieck~(1P),~Steigung~\mathbf{m='
                       + str(steigung_dreieck) + r'}~bestimmt~(1P)}', 'Figure'))
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
                           + '} ~=~' + r' \lim \limits_{x \to ' + gzahl(x_wert_2) + '}~' + partialbruch + '~=~'
                           + gzahl(N(fkt_abl_x0, 3)) + r' \quad (3P) \\'
                           + r' \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (1P)')
            loesung.append(table)
            loesung.append(' \n\n')
            liste_punkte.append(4)
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime} (x)~=~' + latex(fkt_abl)
                           + r' \to f^{ \prime} (' + gzahl(x_wert_2) + r')~=~\mathbf{'
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
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
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
                       + r'h~}{h} ~=~\mathbf{' + str(a1) + r'} \quad (3P) \\\\')  # \\\\ für Übersichtlichkeit
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
                       + vorz_str(b1) + 'h ~' + vorz_str(b2) + r'~=~ \mathbf{' + str(2 * b1) + 'x~' + vorz_str(b2)
                       + r'} \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        liste_punkte.append(punkte)
        i += 1

def grafisches_ableiten(nr, teilaufg=['a', 'b']):
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
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
            extrema = solve(fkt_1,x)
            wendepkt = solve(fkt_1,x)
            wendepkt_art = fkt_3.subs(x,wendepkt)
            if wendepkt > 0:
                art = (r'  \mathrm{Es~ist~ein links-rechts-Wendepunkt,~deswegen~ist~das~Extrema~ein~Hochpunkt}'
                       + r' \quad (1P) \\')
            else:
                art = (r'  \mathrm{Es~ist~ein rechts-links-Wendepunkt,~deswegen~ist~das~Extrema~ein~Tiefpunkt}'
                       + r' \quad (1P) \\')
            aufgabe.append(str(liste_teilaufg[i]) + f') Begründen Sie Ihre Skizze. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Extrema~an~Stelle~x_1~=~'
                           + gzahl(N(extrema[0],3)) + 'und~x_2 ~=~' + gzahl(N(extrema[1],3))
                           + r' sind Nullstellen der Ableitung \quad (1P)} \\'
                           + r' \mathrm{Wendepunkte~an~Stelle~x_w~=~' + gzahl(N(wendepunkt[0]))
                           + r'ist~Extrema~der~Ableitung \quad (1P) \\' + art
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
                   + r' \cdot \ln(x) ~+~ 1) \\')
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
                       + '^{' + gzahl(exponent - 1) + r'}' + vorz_str(faktor_2) + r') \\')
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
               + r' \quad \to \quad f^{ \prime }(x)~=~' + fkt_abl + r' \quad (' + str(pkt) + r'P) \\')
        punkte += pkt
        i += 1

    lsg = lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def exponentialfunktionen_01(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g']):
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

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
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
                      r' \int e^x \,dx ~=~ \hspace{10em}': r' \int e^x \,dx ~=~ e^x + C '}
    auswahl = np.random.choice(list(regeln_aufgabe.keys()),2, False)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vervollständige die folgenden Rechenregeln für unbestimmte Integrale']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []


    if 'a' in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + r') ~' + auswahl[i])
        loesung.append(str(liste_teilaufg[i]) + r') ~' + regeln_aufgabe[auswahl[i]] + r' \quad (1P) \\')
        i += 1

    if 'b' in teilaufg:
        aufgabe.append(r' \hspace{5em}' + str(liste_teilaufg[i]) + r') ~' + auswahl[i + 1])
        loesung.append(str(liste_teilaufg[i]) + r') ~' + regeln_aufgabe[auswahl[i+1]] + r' \quad (1P) \\'
                       + r' \mathrm{insgesamt~' + str(len(teilaufg)) + r'~Punkte} \\')
        i += 1
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
        Fkt = gzahl(a1) + r' \cdot e^x' + vorz_v_aussen(k1, 'x + C')
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
        pkt = 3
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

def bestimmtes_integral(nr, teilaufg=['a', 'b', 'c', 'd']):
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Bestimme die Stammfunktionen der folgenden Funktionen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 4
        liste_punkte.append(punkte_aufg)

        # Funktion und Stammfunktion 1
        konst_i = zzahl(2,20)
        e1_i = nzahl(2,5)
        e2_i = e1_i + nzahl(1,3)
        fkt_str_i = 'x^{' + gzahl(e2_i) + '} + x^{' + gzahl(e1_i) + '}' + vorz_str(konst_i)
        Fkt_str_i = (r' \frac{1}{' + gzahl(e2_i+1) + r'} \cdot x^{' + gzahl(e2_i + 1) + r'} + \frac{1}{' + gzahl(e1_i+1)
                     + r'} \cdot x^{' + gzahl(e1_i + 1) + '}' + vorz_str(konst_i) + 'x + C')

        # Funktion und Stammfunktion 2
        konst_ii = zzahl(2,20)
        e1_ii = nzahl(2,5)
        e2_ii = e1_ii + nzahl(2,4)
        a1 = (e1_ii+1) * zzahl(1,10)/2
        a2 = (e2_ii+1) * zzahl(1,10)/2
        fkt_str_ii = (vorz_v_aussen(a2,'x^{' + gzahl(e2_ii) + '}') + vorz_v_innen(a1,'x^{' + gzahl(e1_ii) + '}')
                      + vorz_str(konst_ii))
        Fkt_str_ii = (vorz_v_aussen(Rational(a2,e2_ii+1),'x^{' + gzahl(e2_ii +1) + '}')
                      + vorz_v_innen(Rational(a1,e1_ii + 1), 'x^{' + gzahl(e1_ii+1) + '}')
                      + vorz_v_innen(konst_ii,'x + C'))

        aufgabe.append(str(liste_teilaufg[i]) + r') \quad f(x) ~=~ ' + fkt_str_i + r' \hspace{10em} '
                       + str(liste_teilaufg[i+1]) + r') \quad h(x) ~=~' + fkt_str_ii + r' \hspace{10em} ')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f(x) ~=~ ' + fkt_str_i + r' \quad \to \quad F(x) ~=~'
                       + Fkt_str_i + r' \quad (2P) \\'
                       + str(liste_teilaufg[i+1]) + r') \quad h(x) ~=~' + fkt_str_ii + r' \quad \to \quad H(x) ~=~'
                       + Fkt_str_ii + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 2


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
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
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

