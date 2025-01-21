import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *


a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

def lineare_funktionen(nr, teilaufg=['a', 'b', 'c'], anz_einf=1, anz_pkt=1, BE=[]):
    # In dieser Aufgabe sollen die SuS Funktionsgleichungen einer linearen Funktion ablesen, einzeichnen und Wertetabellen erstellen.
    # Mit dem Parameter "anz_einf=" kann festgelegt werden, wie viele einfache Graphen (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_einf=1" und es wird ein Graph erzeugt.
    # Mit dem Parameter "anz_pkt=" kann festgelegt werden, wie viele Graphen von schwierigeren Funktionen (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_einf=1" und es wird ein Graph erzeugt.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    anz_einf = 6 if anz_einf not in [1, 2, 3, 4, 5, 6] else anz_einf
    anz_pkt = 6 if anz_pkt not in [1, 2, 3, 4, 5, 6] else anz_pkt
    fkt_bez = ['f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

    # Erstellen der vorgegebenen Graphen
    fkt_m = random_selection([-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5], anz_einf)
    fkt_n = random_selection(list(range(-3,4)), anz_einf)
    # Punkte der schwierigeren Funktionen
    aufg_c = 1 if 'c' in teilaufg else 0
    xwerte_1, ywerte_1 = (random_selection(list(range(-5,6)), anz_pkt + aufg_c),
                          random_selection(list(range(-5,6)), anz_pkt + aufg_c))
    xwerte_2_unbegr, ywerte_2_unbegr = ([wert+random.choice([1,2,4,6]) for wert in xwerte_1],
                                        [wert + random.choice([3,5,7]) for wert in ywerte_1])
    xwerte_2, ywerte_2 = ([wert if wert < 6 else wert - 10 for wert in xwerte_2_unbegr],
                          [wert if wert < 6 else wert - 10 for wert in ywerte_2_unbegr])
    if xwerte_1 < xwerte_2:
        xwerte_P, ywerte_P = xwerte_1, ywerte_1
        xwerte_Q, ywerte_Q = xwerte_2, ywerte_2
    else:
        xwerte_P, ywerte_P = xwerte_2, ywerte_2
        xwerte_Q, ywerte_Q = xwerte_1, ywerte_1

    fkt_m_pkt = [Rational((ywerte_Q[step]-ywerte_P[step]),(xwerte_Q[step]-xwerte_P[step])) for step in range(anz_pkt + aufg_c)]
    fkt_n_pkt = [ywerte_P[step] - fkt_m_pkt[step]*xwerte_P[step] for step in range(anz_pkt + aufg_c)]
    # Liste der Funktionsgleichungen und Erzeugen der Darstellung
    liste_fkt = ([fkt_m[k] * x + fkt_n[k] for k in range(anz_einf)]
                 + [fkt_m_pkt[k] * x + fkt_n_pkt[k] for k in range(anz_pkt)])
    liste_fkt_str = ([vorz_v_aussen(fkt_m[k], 'x') + vorz_str(fkt_n[k]) for k in range(anz_einf)]
                     + [vorz_v_aussen(fkt_m_pkt[k], 'x') + vorz_str(fkt_n_pkt[k]) for k in range(anz_pkt)])
    grafiken_aufgaben.append(f'Aufgabe_{nr}')
    graph_xyfix(*liste_fkt, name=f'Aufgabe_{nr}.png')

    if 'a' in teilaufg:
        # SuS sollen die Funktionsgleichungen aus den Graphen ablesen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = anz_einf*3 + anz_pkt*6
        # Lösungen für Gleichungen
        lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{die~Funktionsgleichung(en):} \hspace{10em} \\')
        for step in range(anz_einf):
            lsg = (lsg + 'n=' + gzahl(fkt_n[step]) + r' \quad \mathrm{und} \quad m=' + gzahl(fkt_m[step])
                   + r' \quad \to \quad ' + fkt_bez[step] + r'(x) ~=~' + vorz_v_aussen(fkt_m[step], 'x')
                   + vorz_str(fkt_n[step]) + r' \quad (3BE) ')
            lsg = lsg + r' \\ ' if step + 1 < anz_einf + anz_pkt else lsg
        for step in range(anz_pkt):
            lsg = (lsg + 'P(' + gzahl(xwerte_P[step]) + r' \vert ' + gzahl(ywerte_P[step]) + r') ~ \mathrm{und} ~ Q('
                   + gzahl(xwerte_Q[step]) + r' \vert ' + gzahl(ywerte_Q[step]) + r') \quad \to \quad m ~=~ \frac{'
                   + gzahl(ywerte_Q[step]) + vorz_str(-1*ywerte_P[step]) + '}{' + gzahl(xwerte_Q[step])
                   + vorz_str(-1*xwerte_P[step]) + '} ~=~ ' + gzahl(fkt_m_pkt[step]) + r' \quad \to \quad '
                   + fkt_bez[anz_einf + step] + r'(x) ~=~ ' + gzahl(fkt_m_pkt[step]) + r' \left( x'
                   + vorz_str(-1*xwerte_P[step]) + r' \right) ' + vorz_str(ywerte_P[step]) + '~=~'
                   + vorz_v_aussen(fkt_m_pkt[step],'x') + vorz_str(fkt_n_pkt[step]) + r' \quad (6BE) ')
            lsg = lsg + r' \\ ' if (anz_einf + step + 1) < anz_einf + anz_pkt else lsg
        if anz_einf + anz_pkt == 1:
            aufgabe.append(str(liste_teilaufg[i]) + f') Lies aus dem Graphen die Funktionsgleichung ab. \n\n')
        else:
            aufgabe.append(str(liste_teilaufg[i]) + f') Lies aus den Graphen die jeweilige Funktionsgleichung ab.\n\n')
        loesung.append(lsg)
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # zu einer vorgegebenen Funktionsgleichung die Wertetabelle anlegen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = (anz_einf + anz_pkt)*2
        aufgabe.extend((str(liste_teilaufg[i]) + f') Erstelle zu den abgelesenen Funktionen eine Wertetabelle für '
                       + f'-2 < x < 2.', 'Grafik \n\n'))

        # Tabelle mit den Lösungen
        def tabelle(fkt, fkt_str, bez):
            table1 = Tabular('c|c|c|c|c|c|c|c', row_height=1.2)
            table1.add_hline(2,7)
            table1.add_row((MultiRow(2, data=NoEscape(f'Wertetabelle für $' + bez + '(x) =' + fkt_str + '$')),
                            'x Werte', '-2', '-1', '0', '1', '2',
                            MultiRow(2, data=' (2BE)')))
            table1.add_hline(2,7)
            table1.add_row(('', 'y Werte', gzahl(N(fkt.subs(x, -2), 3)),
                              gzahl(N(fkt.subs(x, -1), 2)), gzahl(N(fkt.subs(x, 0), 2)),
                              gzahl(N(fkt.subs(x, 1), 2)), gzahl(N(fkt.subs(x, 2), 2)),''))
            table1.add_hline(2,7)
            return table1
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wertetabelle~für~die~aufgestellte(n)~'
                       + r'Funktionsgleichungen.} \hspace{10em}')
        for step in range(anz_einf + anz_pkt):
            loesung.extend((tabelle(liste_fkt[step], liste_fkt_str[step], fkt_bez[step]),' \n\n\n'))
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # zu gegebenen Punkten einer Funktion den Graphen zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        k = anz_einf + anz_pkt
        graph_xyfix(*[fkt_m_pkt[anz_pkt]*x + fkt_n_pkt[anz_pkt]], name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        punkte = 2
        aufgabe.extend((f'Die Funktion {fkt_bez[k]} geht durch die Punkte P({xwerte_P[anz_pkt]}|{ywerte_P[anz_pkt]}) '
                        f'und Q({xwerte_Q[anz_pkt]}|{ywerte_Q[anz_pkt]}). \n\n',
                        str(liste_teilaufg[i]) + r') Zeichne den Graphen der Funktion ' + fkt_bez[k]
                        + ' im oberen Koordinatensystem ein.'))
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(2BE) \quad Graph~(1BE)}',
                        'Figure'))
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # überprüfen ob ein Punkt auf dem Graphen der gegebenen Funktion liegt
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        aufgabe.append(str(liste_teilaufg[i]) + r') Zeichne den Graphen der Funktion ' + fkt_bez[k]
                        + ' im oberen Koordinatensystem ein.')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(2BE) \quad Graph~(1BE)}')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(
                f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def stirb_langsam_2(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], BE=[]):
    # In dieser Aufgabe können die SuS ihre Kenntnisse der linearen Funktionen auf verschiedene Situationen, angelehnt auf Szenen im Film "Stirb Langsam" anwenden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    wert_steigung = nzahl(1, 8)
    steigung = wert_steigung/20
    x_0 = random.choice([3, 2.5, 2])
    y_vers = nzahl(2, 8)/20
    wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
    ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0 and element[1] > 0]
    while len(ganze_werte) == 0:
        wert_steigung = nzahl(1, 8)
        steigung = wert_steigung / 20
        x_0 = random.choice([3, 2.5, 2])
        y_vers = Rational(nzahl(2, 8), 20)
        wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
        ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0 and element[1] > 0]

    # Werte für die Boing
    n = -1 * x_0 * steigung
    fkt = steigung * x + n
    fkt_str = vorz_v_aussen(steigung, 'x') + vorz_str(n)
    n_vers = n - y_vers
    fkt_vers = steigung * x + n_vers
    fkt_vers_str = vorz_v_aussen(steigung, '~x~') + vorz_str(n_vers)
    v_flugzeug = 200 + nzahl(1,10)*5
    p1, p2 = ganze_werte[1], ganze_werte[2]
    abstand = N(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2), 3)
    zeit = int(abstand*1000 / v_flugzeug)
    swinkel = N(np.arctan(wert_steigung/20) * 180 / pi, 3)

    # Werte für den Airbus
    steigung_airbus = -1 * nzahl(1, 15) / 5
    n_airbus = int(ganze_werte[0][1]) - steigung_airbus * int(ganze_werte[0][0])
    xwert_s = Rational(n_airbus - n + y_vers, steigung - steigung_airbus)
    ywert_s = N(steigung_airbus * xwert_s + n_airbus, 3)
    swinkel_airbus = N(np.arctan(steigung_airbus) * 180 / pi, 3)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Im zweiten Teil der legendären „Stirb langsam“ – Reihe manipulieren Terroristen '
               'das Instrumentenlandesystem (ILS) eines Flughafen, um General Ramon Esperanza freizupressen. '
               'Dabei lassen die Terroristen zur Abschreckung eine Boeing 747 landen, welche durch die Manipulation '
               'beim Landeanflug auf der Startbahn zerbricht und ausbrennt. ', 'Bild']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['stirb_langsam_2']
    grafiken_loesung = []

    if 'a' in teilaufg:
        # aus zwei gegebenen Punkten die Geradengleichung
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.extend((f'Das Radar des Flughafens ortet die Boing zuerst bei Punkt P({gzahl(p2[0])}|'
                        f'{gzahl(p2[1])}) und nach {gzahl(zeit)}s bei Punkt Q({gzahl(p1[0])}|{gzahl(p1[1])}). \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie die Funktionsgleichung der Flugbahn. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad f(x) ~=~ \frac{y_2 - y_1}{x_2 - x_1} \cdot (x - x_1) + y_1 '
                       + r' ~=~ \frac{' + gzahl(p2[1]) + vorz_str(-1*p1[1]) + r'}{' + gzahl(p2[0]) + gzahl(-1*p1[0])
                       + r'} \left(x' + vorz_str(-1*p2[0]) + r' \right) ' + vorz_str(p2[1])
                       + r' \quad (2BE) \\ f(x) ~=~' + gzahl(steigung) + r' \left(x' + vorz_str(-1*p2[0])
                       + r' \right) ' + vorz_str(p2[1]) + '~=~' + vorz_v_aussen(steigung,'x')
                       + vorz_str(-1 * steigung * p2[0]) + vorz_str(p2[1]) + '~=~' + fkt_str + r' \quad (1BE) \\')
        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # die SuS sollen den Abstand zwischen zwei Punkten bestimmen und damit die Geschwindigkeit berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie Geschwindigkeit der Boing (in km/h) im '
                       + f'Landeanflug. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad d(PQ) ~=~ \sqrt{ \left( ' + gzahl(p2[0])
                       + vorz_str(-1*p1[0]) + r' \right) ^2 + \left( ' + gzahl(p2[1]) + vorz_str(-1*p1[1])
                       + r' \right) ^2 } ~=~' + gzahl(abstand) + r'km \quad (2BE) \quad \to \quad v ~=~ \frac{s}{t} '
                       + r'~=~ \frac{' + gzahl(abstand*1000) + 'm}{' + gzahl(zeit) + 's} ~=~'
                       + gzahl(int(abstand*1000/zeit)) + r' \frac{m}{s} ~=~' + gzahl(int(abstand*1000/zeit*3.6))
                       + r' \frac{km}{h} \quad (3BE)')
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in ['c', 'd', 'e', 'f', 'g', 'h'] if element in teilaufg]) > 0:
        # die SuS sollen die Veränderung des y-Achsenabschnittes durch die Manipulation der Flugbahn erklären
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        aufgabe.extend(('Durch die Manipulation rechnet die Flugzeugelektronik der Boeing mit der Funktion '
                        f' f(x) = {gzahl(steigung)}x - {gzahl(abs(n_vers))}. \n\n',
                        str(liste_teilaufg[i]) + f') Erläutern Sie den Unterschied zur ursprünglichen Funktion '
                        + f'bzw. Flugbahn. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Der~Unterschied~ist~der~Schnittpunkt~mit~'
                       + r'der~y-Achse.~Die~manipulierte} \\ \mathrm{Flugbahn~ist~um~' + gzahl(round(y_vers,3)*1000)
                       + r'm~nach~unten~verschoben. \quad (2BE) }')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # die SuS sollen den Schnittwinkel des Flugzeuges mit der Landebahn berechnen (Steigungswinkel)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        lsg = r' ~ \leq 3.5^{ \circ } \to \mathrm{Die~Boing~ist~nicht~gefährdet.}'
        lsg = r' ~ > 3.5^{ \circ } \to \mathrm{Die~Boing~ist~gefährdet.}' if swinkel > 3.5 else lsg
        aufgabe.extend(('Ein Flugzeug landet unbeschadet, wenn der Anflugwinkel 3,5° nicht überschreiten wird. \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie den Anflugwinkel (Schnittwinkel) der Boing. '
                        + f'Ist die Boing gefährdet? \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad tan( \alpha ) ~=~ m \quad \vert tan^{-1}() \to '
                       + r' \alpha ~=~ tan^{-1} \left( ' + gzahl(steigung) + r' \right) ~=~' + gzahl(swinkel) + lsg
                       + r' \quad (4BE)')
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # die SuS sollen den Landepunkt des Flugzeuges berechnen (Nullstelle) und beurteilen, ob es noch auf der Landebahn landet
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        lsg = r' > 3 \quad \to \quad \mathrm{Die~Boing~landet~vor~der~Landebahn.}'
        lsg = r' \leq 3 \to \mathrm{Die~Boing~landet~auf~der~Landebahn.}' if N(-1*(n-y_vers)/steigung,3) <= 3 else lsg
        aufgabe.extend(('Im Film landet die Boeing, bevor sie zerbricht, trotz der manipulierten Flugbahn '
                        'auf der Landebahn (Nullstelle). Die Landebahn beginnt im Punkt A(3|0) und endet im '
                        'Koordinatenursprung E(0|0). \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie die Landestelle nach der Manipulation '
                        + f'des ILS. Landet die Boing auf der Landebahn? \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad x_0 ~=~ - \frac{n}{m} ~=~ - \frac{ ' + gzahl(N(n-y_vers,3))
                       + r'}{' + gzahl(N(steigung,3)) + '} ~=~' + gzahl(N(-1*(n-y_vers)/steigung,3)) + lsg
                       + r' \quad (4BE)')
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in ['f', 'g'] if element in teilaufg]) > 0:
        # Die SuS sollen erläutern, woran man erkennen kann das sich zwei Geraden schneiden
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.extend((f'Über dem Flughafen kreisen mehrere Flugzeuge und warten auf Landerlaubnis. Ein Airbus bewegt '
                        f'sich auf der Flugbahn h(x) = {gzahl(steigung_airbus)} x {vorz_str(n_airbus)}, während sich '
                        f'die Boing im Landeanflug befindet. \n\n',
                        str(liste_teilaufg[i]) + f') Erläutern Sie, woran man erkennen kann, dass sich die Flugbahnen '
                        + f'schneiden. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{~Da~die~Steigungen~der~beiden~Geraden~verschieden~'
                       + r'sind.} \quad (1BE)')
        liste_punkte.append(1)
        i += 1

    if 'g' in teilaufg:
        # Die SuS sollen den Schnittpunkt zweier linearen Funktionen (Flugbahnen) berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Schnittpunkt der Flugbahnen des Airbus und '
                       + f'der Boing. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Ansatz: \quad f(x)=g(x)} '
                        + r' \quad \to \quad ' + fkt_vers_str + '~=~' + vorz_v_aussen(steigung_airbus,'x')
                        + vorz_str(n_airbus) + r' \quad \vert ' + vorz_v_innen(-1 * steigung_airbus, 'x')
                        + r' \quad \vert ' + vorz_str(-1*float(n_vers)) + r' \quad (3BE) \\'
                        + vorz_v_aussen(steigung - steigung_airbus, 'x')
                        + '~=~' + gzahl(n_airbus - n_vers) + r' \quad \vert \div' + gzahl(steigung - steigung_airbus)
                        + r' \quad \to \quad x~=~'
                        + gzahl(N((n_airbus - n + y_vers)/(steigung - steigung_airbus), 3))
                        + r' \quad (3BE) \\ \mathrm{Schnittpunkt \quad S(' + gzahl(N(xwert_s,3)) + r'~ \vert ~'
                        + gzahl(ywert_s) + r') \quad (2BE)}')
        liste_punkte.append(8)
        i += 1

    if 'h' in teilaufg:
        # Die SuS sollen den Schnittwinkel zweier linearen Funktionen (Flugbahnen) berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if 'd' in teilaufg:
            lsg = (r' \mathrm{nach~Teilaufgabe~d~gilt: \quad \alpha ~=~ ' + gzahl(swinkel)
                   +  r' ^{ \circ } \quad und \quad \beta ~=~ tan^{-1}(' + gzahl(steigung_airbus) + ')~=~'
                   + gzahl(swinkel_airbus) + r' \quad (2BE) } \\')
            pkt = 4
        else:
            lsg = (r' \mathrm{ \alpha  ~=~ tan^{-1}(' + gzahl(steigung) + ')~=~' + gzahl(swinkel)
                   +  r' ^{ \circ } und \quad \beta ~=~ tan^{-1}(' + gzahl(steigung_airbus) + '~=~'
                   + gzahl(swinkel_airbus) + r' \quad (4BE) } \\')
            pkt = 6

        if abs(swinkel_airbus - swinkel) > 90:
            lsg_1 = (r' ^{ \circ } > 90 ^{ \circ } \quad \to \quad \gamma ~=~ 180 - '
                     + gzahl(abs(swinkel_airbus - swinkel)) + '~=~'
                     + gzahl(180 - abs(swinkel_airbus - swinkel)) + r' \quad (3BE)')
            pkt += 1
        else:
            lsg_1 = r' ^{ \circ } \quad (2BE)'

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Schnittwinkel der Flugbahnen des Airbus und '
                       + f'der Boing. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + lsg
                       + r' \gamma ~=~ \vert \beta - \alpha \vert ~=~ \vert ' + gzahl(swinkel_airbus) + '~-~'
                       + gzahl_klammer(swinkel) + r' \vert ~=~' + gzahl(N(abs(swinkel_airbus - swinkel),3)) + lsg_1)
        liste_punkte.append(pkt)
        i += 1

    if 'i' in teilaufg and (swinkel >= 3.5 or -1*(n-y_vers)/steigung >= 3):
        # Die SuS die orthogonale Flugbahn zur manipulierten Flugbahn berechnen. Die Aufgabe wird nur angezeigt, wenn der Anflugwinkel zu groß ist, oder das Flugzeug vor der Landebahn landen würde.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        xwert, ywert = ganze_werte[0][0], ganze_werte[0][1] - float(y_vers)
        steigung_g = N(-20/wert_steigung,3)
        aufgabe.extend((f'Da die Gefahr für einen Absturz der Boing zu groß ist, muss Sie im Punkt ({gzahl(xwert)}|'
                        f'{gzahl(ywert)}) orthogonal zur bisherigen (manipulierten) Flugbahn durchstarten und nach '
                        f'einer Schleife eine erneute Landung versuchen. \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie die neue Flugbahn g(x), '
                        + f'nachdem die Boing durchgestartet ist. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Steigung~der~orthogonalen~Flugbahn:} \quad m_g ~=~ '
                       + r' - \frac{1}{m_f} ~=~ - \frac{1}{' + gzahl(steigung) + '} ~=~' + gzahl(steigung_g)
                       + r' \quad (2BE) \\ g(x) ~=~' + gzahl(steigung_g) + binom_klammer(1, -1 * xwert, 'x')
                       + vorz_str(ywert) + '~=~' + vorz_v_aussen(steigung_g,'x')
                       + vorz_str(N(20/wert_steigung*xwert+ywert,3)) + r' \quad (2BE)')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def einf_parabeln(nr, teilaufg=['a', 'b', 'c'], anz_np=1, anz_ap=1, BE=[]):
    # In dieser Aufgabe sollen die SuS Funktionsgleichungen einer Parabel ablesen und umformen, Graphen einzeichnen und Wertetabellen erstellen.
    # Mit dem Parameter "anz_np=" kann festgelegt werden, wie viele Graphen einer Normalparabel (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_np=1" und es wird ein Graph in Teilaufgabe a erzeugt.
    # Mit dem Parameter "anz_ap=" kann festgelegt werden, wie viele Graphen einer allegemeinen Parabel (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_ap=1" und es wird ein Graph in Teilaufgabe a erzeugt.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    anz_np = 6 if anz_np not in list(range(1,7)) else anz_np
    anz_ap = 6 if anz_ap not in list(range(1,7)) else anz_ap
    fkt_bez = ['f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

    # Erstellen der vorgegebenen Graphen
    xwert_s = random_selection(list(range(-4,5)), anz_np+anz_ap)
    ywert_s = random_selection(list(range(-3,3)), anz_np+anz_ap)
    fakt_ap = random_selection([-2.5,-2,-1.5,-1,-0.5,0.5,1.5,2,2.5], anz_ap)
    liste_fkt = ([(x - xwert_s[k])**2+ywert_s[k] for k in range(anz_np)]
                 + [fakt_ap[k]*(x - xwert_s[k+anz_np])**2+ywert_s[k+anz_np] for k in range(anz_np)])
    grafiken_aufgaben.append(f'Aufgabe_{nr}')
    graph_xyfix(*liste_fkt, name=f'Aufgabe_{nr}.png')


    if 'a' in teilaufg:
        # SuS sollen aus dem Graphen den Scheitelpunkt ablesen und die Funktionsgleichung in Scheitelpunktsform aufstellen, dabei können mit den Parametern anz_np die Anzahl der Normalparabeln und mit anz_ap die Anzahl der allgemeinen Parabeln festgelegt werden bzw.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = anz_np * 3 + anz_ap * 4

        # Lösungen für Gleichungen
        lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{abgelesener~Scheitelpunkt,~ggf.~der~Faktor~und~die~'
               + r'Funktionsgleichung:} \\')
        for step in range(anz_np):
            lsg =  (lsg + r' S \left( ' + gzahl(xwert_s[step]) + r' \vert '
                    + gzahl(ywert_s[step]) + r' \right) \quad \to \quad ' + fkt_bez[step] + r'(x) ~=~ \left( x'
                    + vorz_str(-1*xwert_s[step]) + r' \right) ^2 ' + vorz_str(ywert_s[step]) + r' \quad (3BE)')
            lsg = lsg + r' \\ ' if step + 1 < anz_np + anz_ap else lsg
        for step in range(anz_ap):
            lsg = (lsg +r' S \left( ' + gzahl(xwert_s[anz_np+step]) + r' \vert ' + gzahl(ywert_s[anz_np+step])
                   + r' \right) \quad \mathrm{und} \quad a ~=~ ' + gzahl(fakt_ap[step]) + r' \quad \to \quad '
                   + fkt_bez[anz_np+step] + r'(x) ~=~ ' + gzahl(fakt_ap[step]) + r' \cdot \left( x'
                   + vorz_str(-1 * xwert_s[anz_np+step]) + r' \right) ^2 ' + vorz_str(ywert_s[anz_np+step])
                   + r' \quad (4BE)')
            lsg = lsg + r' \\ ' if (anz_np + step + 1) < anz_np + anz_ap else lsg

        if anz_np + anz_ap == 1:
            aufgabe.extend((str(liste_teilaufg[i]) + f') Lies aus dem Graphen den Scheitelpunkt ab '
                            + f'und stelle die Funktionsgleichung auf.', 'Grafik \n\n'))
        else:
            aufgabe.extend((str(liste_teilaufg[i]) + f') Lies aus den Graphen die Scheitelpunkte ab '
                            + f'und stelle die Funktionsgleichungen auf.', 'Grafik \n\n'))

        loesung.append(lsg)
        liste_punkte.append(punkte)
        i += 1

        if 'b' in teilaufg:
            # zu einer vorgegebenen Funktionsgleichung den Graphen zeichnen
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = anz_np*2 + anz_ap*3

            # Lösungen für Gleichungen
            lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{umgeformte~Funktionsgleichung~lauten:} \\')
            for step in range(anz_np):
                lsg = (lsg + fkt_bez[step] + r'(x) ~=~ x^2' + vorz_v_innen(2 * xwert_s[step],'x')
                       + vorz_str(xwert_s[step]**2 + ywert_s[step]) + r' \quad (2BE) ')
                lsg = lsg + r' \\ ' if step + 1 < anz_np + anz_ap else lsg
            for step in range(anz_ap):
                lsg = (lsg + r' S \left( ' + gzahl(xwert_s[anz_np + step]) + r' \vert ' + gzahl(ywert_s[anz_np + step])
                       + r' \right) \quad \mathrm{und} \quad a ~=~ ' + gzahl(fakt_ap[step]) + r' \quad \to \quad '
                       + fkt_bez[anz_np + step] + r'(x) ~=~ ' + gzahl(fakt_ap[step]) + r' \cdot \left( x'
                       + vorz_str(-1 * xwert_s[anz_np + step]) + r' \right) ^2 ' + vorz_str(ywert_s[anz_np + step])
                       + r' \quad (4BE)')
                lsg = lsg + r' \\ ' if (anz_np + step + 1) < anz_np + anz_ap else lsg

            aufgabe.append(str(liste_teilaufg[i]) + f') Gib alle Funktionsgleichungen aus Teilaufgabe a) '
                           + f'auch in der Normalform an. \n\n' )
            loesung.append(lsg)
            liste_punkte.append(punkte)
            i += 1

    if 'c' in teilaufg:
        # zu einer vorgegebenen Funktionsgleichung den Graphen zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        punkte = 2
        aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen der Funktion' )
        loesung.append(str(liste_teilaufg[i]) + r') \quad f(x) ~=~' + r' \quad (2BE) \\')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(
                f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
