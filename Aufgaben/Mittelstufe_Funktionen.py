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

def lineare_funktionen(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anz_einf=1, anz_pkt=1, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS Funktionsgleichungen einer linearen Funktion ablesen, einzeichnen und Wertetabellen erstellen.
    # Mit dem Parameter "anz_einf=" kann festgelegt werden, wie viele einfache Graphen (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_einf=1" und es wird ein Graph erzeugt.
    # Mit dem Parameter "anz_pkt=" kann festgelegt werden, wie viele Graphen von schwierigeren Funktionen (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_einf=1" und es wird ein Graph erzeugt.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    anz_einf = 6 if anz_einf not in list(range(0,7)) else anz_einf
    anz_pkt = 6 if anz_pkt not in list(range(0,7)) else anz_pkt
    fkt_bez = ['f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

    # Erstellen der vorgegebenen Graphen
    aufg_e = 1 if 'e' in teilaufg else 0
    fkt_m = random_selection([-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5], anz_einf + aufg_e)
    fkt_n = random_selection(list(range(-3,4)), anz_einf + aufg_e)
    # Punkte der schwierigeren Funktionen
    aufg_d = 1 if 'd' in teilaufg else 0
    xwerte_1, ywerte_1 = (random_selection(list(range(-5,6)), anz_pkt + aufg_d),
                          random_selection(list(range(-5,6)), anz_pkt + aufg_d))
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

    fkt_m_pkt = [Rational((ywerte_Q[step]-ywerte_P[step]),(xwerte_Q[step]-xwerte_P[step])) for step in range(anz_pkt + aufg_d)]
    fkt_n_pkt = [ywerte_P[step] - fkt_m_pkt[step]*xwerte_P[step] for step in range(anz_pkt + aufg_d)]
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
        punkte = (anz_einf)*3 + anz_pkt*6
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
        # zu einer vorgegebenen Funktionsgleichung die Nullstellen berechnen anlegen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = (anz_einf + anz_pkt)*2
        lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{die~Nullstellen~werden~berechnet~mit~'
               + r'x_0~=~ - \frac{n}{m}} \\')
        for step in range(anz_einf):
            lsg = (lsg + r' \mathrm{für~' + fkt_bez[step] + r'(x) ~ gilt:} x_0 ~=~ -\frac{' + gzahl(fkt_n[step]) + '}{'
                   + gzahl(fkt_m[step]) + r'}~=~' + gzahl(Rational(-1*fkt_n[step], fkt_m[step])) + r' \quad (2BE) ')
            lsg = lsg + r' \\ ' if step + 1 < anz_einf + anz_pkt else lsg
        for step in range(anz_pkt):
            lsg = (lsg + r' \mathrm{für~' + fkt_bez[anz_einf + step] + r'(x) ~ gilt:} x_0 ~=~ -\frac{'
                   + gzahl(fkt_n_pkt[step]) + '}{' + gzahl(fkt_m_pkt[step]) + r'}~=~'
                   + gzahl(Rational(-1*fkt_n_pkt[step], fkt_m_pkt[step])) + r' \quad (2BE) ')
            lsg = lsg + r' \\ ' if step + 1 < anz_einf + anz_pkt else lsg
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Nullstellen der Graphen mithilfe der '
                       + f'Funktionsgleichungen. \n\n')
        loesung.append(lsg)
        liste_punkte.append(punkte)
        i += 1


    if 'c' in teilaufg:
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

    if 'd' in teilaufg:
        # zu gegebenen Punkten einer Funktion den Graphen zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        k = anz_einf + anz_pkt
        punkte = 2
        aufgabe.extend((f'Die Funktion {fkt_bez[k]} geht durch die Punkte P({xwerte_P[anz_pkt]}|{ywerte_P[anz_pkt]}) '
                        f'und Q({xwerte_Q[anz_pkt]}|{ywerte_Q[anz_pkt]}). \n\n',
                        str(liste_teilaufg[i]) + r') Zeichne den Graphen der Funktion ' + fkt_bez[k]
                        + ' im oberen Koordinatensystem ein. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(2BE) \quad Graph~(1BE)}')
        if 'f' not in teilaufg:
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            graph_xyfix(*[fkt_m_pkt[anz_pkt]*x + fkt_n_pkt[anz_pkt]],
                        bezn=fkt_bez[k], name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
            loesung.append('Figure')
        else:
            loesung.append(r' \mathrm{Der~Graph~ist~im~Koordinatensystem~von~Teilaufgabe~f~enthalten.} ')

        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # zu gegebener Funktionsgleichung den Graphen zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        k = anz_einf + anz_pkt
        if 'd' in teilaufg:
            graph_xyfix(fkt_m_pkt[anz_pkt]*x + fkt_n_pkt[anz_pkt], fkt_m[anz_einf]*x + fkt_n[anz_einf],
                        bezn=[fkt_bez[k], fkt_bez[k+1]], name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        else:
            graph_xyfix(*[fkt_m[anz_einf]*x + fkt_n[anz_einf]],
                        bezn=fkt_bez[k+1], name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        punkte = 2
        aufgabe.extend((NoEscape(str(liste_teilaufg[i]) + r') Zeichne den Graphen der Funktion $' + fkt_bez[k+1] + '(x) = '
                       + vorz_v_aussen(fkt_m[anz_einf],'x') + vorz_str(fkt_n[anz_einf])
                       + '$ im oberen Koordinatensystem ein.'), ' \n\n'))
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(2BE) \quad Graph~(1BE)}',
                        'Figure'))
        liste_punkte.append(punkte)
        i += 1

        if 'f' in teilaufg:
            # überprüfen, ob ein Punkt T auf dem Graphen der gegebenen Funktion liegt
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 2
            wertetabelle = [[xwert, fkt_m[anz_einf] * xwert + fkt_n[anz_einf]] for xwert in range(-5,5) if abs(fkt_m[anz_einf] * xwert + fkt_n[anz_einf]) < 5]
            xwert_t = wertetabelle[0][0]
            ywert_t = wertetabelle[0][1]
            if random.choice([0,1]) == 0:
                lsg_vergl = (r' \quad \mathrm{w.A. \quad Der~Punkt~T~liegt~auf~der~Geraden~'
                             + fkt_bez[k+1] + r'.} \quad (1BE) \\'
                             + r' \mathrm{grafische~Lösung:~Einzeichnen~des~Punktes~T~im~Koordinatensystem~und~'
                             + r'die~Lage~überprüfen} \quad (2BE) \hspace{10em}')
            else:
                ywert_t = ywert_t + zzahl(1,2)
                lsg_vergl = (r' \quad \mathrm{f.A. \quad Der~Punkt~T~liegt~nicht~auf~der~Geraden~'
                             + fkt_bez[k+1] + r'.} \quad (1BE) \\'
                             + r' \mathrm{grafische~Lösung:~Einzeichnen~des~Punktes~T~im~Koordinatensystem~und~'
                             + r'die~Lage~überprüfen} \quad (2BE) \hspace{10em}')

            lsg = (r' \mathrm{einsetzen~des~Punktes~T~in~Funktionsgleichung} \hspace{15em} \\'
                   + gzahl(fkt_m[anz_einf]) + gzahl_klammer(xwert_t) + vorz_str(fkt_n[anz_einf]) + '~=~'
                   + gzahl(ywert_t) + r' \quad \to \quad ' + gzahl(fkt_m[anz_einf] * xwert_t + fkt_n[anz_einf])
                   + '~=~' + gzahl(ywert_t))

            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe, ob der Punkt T({gzahl(xwert_t)} | '
                           + f'{gzahl(N(ywert_t,3))}), auf dem Graphen von {fkt_bez[k+1]} liegt. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + lsg + lsg_vergl)
            liste_punkte.append(punkte)
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(
                f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def stirb_langsam_2(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], i=0, BE=[]):
    # In dieser Aufgabe können die SuS ihre Kenntnisse der linearen Funktionen auf verschiedene Situationen, angelehnt auf Szenen im Film "Stirb Langsam" anwenden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
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

def einf_parabeln(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anz_np=1, anz_ap=1, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS Funktionsgleichungen einer Parabel ablesen und umformen, Graphen einzeichnen und Wertetabellen erstellen.
    # Mit dem Parameter "anz_np=" kann festgelegt werden, wie viele Graphen einer Normalparabel (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_np=1" und es wird ein Graph in Teilaufgabe a erzeugt.
    # Mit dem Parameter "anz_ap=" kann festgelegt werden, wie viele Graphen einer allegemeinen Parabel (max. 6) zum Ablesen bei Teilaufgabe a erzeugt werden. Standardmäßig ist "anz_ap=1" und es wird ein Graph in Teilaufgabe a erzeugt.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    anz_np = 6 if anz_np not in list(range(0,7)) else anz_np
    anz_ap = 6 if anz_ap not in list(range(0,7)) else anz_ap
    fkt_bez = ['f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
    anz_d = 1 if 'c' in teilaufg else 0
    anz_e = 1 if 'e' in teilaufg else 0
    # Erstellen der vorgegebenen Graphen
    xwert_s = random_selection([-1*zahl for zahl in range(1,5)] + list(range(1,5)), anz_np + anz_ap + anz_d + anz_e)
    ywert_s = random_selection(list(range(-3,3)), anz_np + anz_ap + anz_d + anz_e)
    fakt_ap = random_selection([-2.5,-2,-1.5,-1,-0.5,0.5,1.5,2,2.5], anz_ap + anz_e)
    liste_fkt = ([(x - xwert_s[k])**2+ywert_s[k] for k in range(anz_np)]
                 + [fakt_ap[k]*(x - xwert_s[k+anz_np])**2+ywert_s[k+anz_np] for k in range(anz_ap)])
    grafiken_aufgaben.append(f'Aufgabe_{nr}')
    graph_xyfix(*liste_fkt, name=f'Aufgabe_{nr}.png')


    if 'a' in teilaufg:
        # SuS sollen aus dem Graphen den Scheitelpunkt ablesen und die Funktionsgleichung in Scheitelpunktsform aufstellen, dabei können mit den Parametern anz_np die Anzahl der Normalparabeln und mit anz_ap die Anzahl der allgemeinen Parabeln festgelegt werden bzw.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = anz_np * 2 + anz_ap * 3

        # Lösungen für Gleichungen
        lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{abgelesener~Scheitelpunkt,~ggf.~der~Faktor~und~die~'
               + r'Funktionsgleichung:} \\')
        for step in range(anz_np):
            lsg =  (lsg + r' S \left( ' + gzahl(xwert_s[step]) + r' \vert '
                    + gzahl(ywert_s[step]) + r' \right) \quad \to \quad ' + fkt_bez[step] + r'(x) ~=~ \left( x'
                    + vorz_str(-1*xwert_s[step]) + r' \right) ^2 ' + vorz_str(ywert_s[step]) + r' \quad (2BE)')
            lsg = lsg + r' \\ ' if step + 1 < anz_np + anz_ap else lsg
        for step in range(anz_ap):
            lsg = (lsg +r' S \left( ' + gzahl(xwert_s[anz_np+step]) + r' \vert ' + gzahl(ywert_s[anz_np+step])
                   + r' \right) \quad \mathrm{und} \quad a ~=~ ' + gzahl(fakt_ap[step]) + r' \quad \to \quad '
                   + fkt_bez[anz_np+step] + r'(x) ~=~ ' + vorz_v_aussen(fakt_ap[step],'') + r' \left( x'
                   + vorz_str(-1 * xwert_s[anz_np+step]) + r' \right) ^2 ' + vorz_str(ywert_s[anz_np+step])
                   + r' \quad (3BE)')
            lsg = lsg + r' \\ ' if (anz_np + step + 1) < anz_np + anz_ap else lsg

        if anz_np + anz_ap == 1:
            aufgabe.extend(('Im unteren Koordinatensystem ist der Graph einer quadratischen Funktion (Parabel) '
                            'dargestellt. \n\n', str(liste_teilaufg[i]) + f') Lies den Scheitelpunkt und ggf. den '
                            + f'Faktor a ab und nenne die zugeh. Funktionsgleichung. ', 'Grafik'))
        else:
            aufgabe.extend(('Im unteren Koordinatensystem sind die Graphen verschiedener quadratischen Funktionen '
                            '(Parabeln) dargestellt. \n\n', str(liste_teilaufg[i]) + f') Lies die Scheitelpunkte und '
                            + f'ggf. den Faktor a ab und nenne die zugeh. Funktionsgleichungen. ', 'Grafik'))

        loesung.append(lsg)
        liste_punkte.append(punkte)
        i += 1

        if 'b' in teilaufg:
            # die abgelesenen Gleichungen in die Normalform umformen
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = anz_np*2 + anz_ap*3

            # Lösungen für Gleichungen
            lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{umgeformte~Funktionsgleichung~lauten:} \hspace{15em}  \\')
            for step in range(anz_np):
                lsg = (lsg + fkt_bez[step] + r'(x) ~=~ x^2' + vorz_v_innen(-2 * xwert_s[step],'x +')
                       + gzahl(abs(xwert_s[step])) + '^2' + vorz_str(ywert_s[step]) + '~=~ x^2'
                       + vorz_v_innen(-2 * xwert_s[step],'x')
                       + vorz_str(xwert_s[step]**2 + ywert_s[step]) + r' \quad (2BE) ')
                lsg = lsg + r' \\ ' if step + 1 < anz_np + anz_ap else lsg
            for step in range(anz_ap):
                lsg = (lsg + fkt_bez[anz_np + step] + r'(x) ~=~ ' + vorz_v_aussen(fakt_ap[step],'')
                       + r' \left( x^2' + vorz_v_innen(-2 * xwert_s[anz_np + step],'x + ')
                       + gzahl_klammer(abs(xwert_s[anz_np + step]))
                       + r'^2 \right) ' + vorz_str(ywert_s[anz_np + step]) + '~=~'
                       + vorz_v_aussen(fakt_ap[step],'x^2')
                       + vorz_v_innen(-2 * fakt_ap[step] * xwert_s[anz_np + step], 'x')
                       + vorz_str(fakt_ap[step]*xwert_s[anz_np + step]**2) + vorz_str(ywert_s[anz_np + step]) + '~=~'
                       + vorz_v_aussen(fakt_ap[step],'x^2')
                       + vorz_v_innen(-2 * fakt_ap[step] * xwert_s[anz_np + step], 'x')
                       + vorz_str(fakt_ap[step]*xwert_s[anz_np + step]**2 + ywert_s[anz_np + step]) + r' \quad (3BE)')
                lsg = lsg + r' \\ ' if (step + 1) < anz_ap else lsg

            if anz_np + anz_ap == 1:
                aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + f') Gib die Funktionsgleichung '
                                        + f'aus Teilaufgabe a) auch in der Normalform an.'), '\n\n'))

            else:
                aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + f') Gib alle Funktionsgleichungen '
                                        + f'aus Teilaufgabe a) auch in der Normalform an.'), '\n\n'))
            loesung.append(lsg)
            liste_punkte.append(punkte)
            i += 1

            if 'c' in teilaufg:
                # die Nullstellen der eingezeichneten Funktionsgleichungen berechnen
                liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
                punkte = 0
                # Lösungen für Gleichungen
                lsg = (str(liste_teilaufg[i]) + r') \quad \mathrm{Nullstellen~mit~p~q~Formel~berechnen:} \hspace{15em} \\')
                for step in range(anz_np):
                    lsg = (lsg + '0 ~=~ x^2' + vorz_v_innen(-2 * xwert_s[step], 'x')
                           + vorz_str(xwert_s[step] ** 2 + ywert_s[step])
                           + r' \quad \to \quad x_{1/2} ~=~ - \frac{ ' + gzahl(-2 * xwert_s[step])
                           + r'}{2} \pm \sqrt{ \left( \frac{' + gzahl(-2 * xwert_s[step]) + r' }{2} \right) ^2 - '
                           + gzahl_klammer(xwert_s[step] ** 2 + ywert_s[step]) + r'} ~=~ ' + gzahl(xwert_s[step])
                           + r' \pm \sqrt{' + gzahl(-1 * ywert_s[step]) + r'} \quad (2BE) \\')
                    punkte += 2
                    if ywert_s[step] > 0:
                        lsg = (lsg + r' \mathrm{negative~Wurzel~nicht~lösbar \quad \to \quad keine~Nullstellen '
                               + r' \quad (1BE) }')
                        punkte += 1
                    elif ywert_s[step] == 0:
                        lsg = (lsg + r' \mathrm{nur~eine~Nullstelle~bei} \quad x_1 ~=~ '
                               + gzahl(xwert_s[step]) + r' \quad (1BE) ')
                        punkte += 1
                    else:
                        lsg = (lsg +r' x_1 ~=~ ' + gzahl(N(xwert_s[step] - sqrt(-1*ywert_s[step]),3))
                               + r' \quad \mathrm{und} \quad x_2 ~=~' + gzahl(N(xwert_s[step]  + sqrt(-1*ywert_s[step]),3)) + r' \quad (2BE)')
                        punkte += 2
                    lsg = lsg + r' \\ ' if step + 1 < anz_np + anz_ap else lsg

                for step in range(anz_ap):
                    lsg = (lsg + '0 ~=~' + vorz_v_aussen(fakt_ap[step], 'x^2')
                           + vorz_v_innen(-2 * fakt_ap[step] * xwert_s[anz_np + step], 'x')
                           + vorz_str(fakt_ap[step] * xwert_s[anz_np + step] ** 2 + ywert_s[anz_np + step])
                           + r'~ \vert \div ' + gzahl_klammer(fakt_ap[step]) + r' \quad \to \quad 0 ~=~ x^2 '
                           + vorz_v_innen(-2 * xwert_s[anz_np + step], 'x')
                           + vorz_str(xwert_s[anz_np + step] ** 2 + Rational(ywert_s[anz_np + step],fakt_ap[step]))
                           + r' \quad (2BE) \\ x_{1/2} ~=~ - \frac{ ' + gzahl(-2*xwert_s[anz_np + step])
                           + r'}{2} \pm \sqrt{ \left( \frac{' + gzahl(-2* xwert_s[anz_np + step])
                           + r' }{2} \right) ^2 - '
                           + gzahl_klammer(xwert_s[anz_np + step] ** 2 + Rational(ywert_s[anz_np + step],fakt_ap[step]))
                           + r' } ~=~ ' + gzahl(xwert_s[anz_np + step]) + r' \pm \sqrt{'
                           + gzahl(-1*Rational(ywert_s[anz_np + step]), fakt_ap[step]) + r'} \quad (1BE) \\ ')
                    punkte += 3
                    if fakt_ap[step] * ywert_s[anz_np + step] > 0:
                        lsg = (lsg + r' \mathrm{negative~Wurzel~nicht~lösbar \quad \to \quad keine~Nullstellen '
                               + r' \quad (1BE) }')
                        punkte += 1
                    elif fakt_ap[step] * ywert_s[anz_np + step] == 0:
                        lsg = (lsg + r' \mathrm{nur~eine~Nullstelle~bei} \quad x_1 ~=~ '
                               + gzahl(xwert_s[anz_np + step]) + r' \quad (1BE) ')
                        punkte += 1
                    else:
                        lsg = (lsg + ' x_1 ~=~ '
                               + gzahl(N(xwert_s[anz_np + step] - sqrt(-1*Rational(ywert_s[anz_np + step], fakt_ap[step])),3))
                               + r' \quad \mathrm{und} \quad x_2 ~=~'
                               + gzahl(N(xwert_s[anz_np + step] + sqrt(-1*Rational(ywert_s[anz_np + step], fakt_ap[step])),3))
                               + r' \quad (2BE)')
                        punkte += 2
                    lsg = lsg + r' \\ ' if (anz_np + step + 1) < anz_np + anz_ap else lsg
                    punkte += 5
                if anz_np + anz_ap == 1:
                    aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                            + f') Berechne die Nullstellen des Graphen mithilfe '
                                            + f'der Normalform aus Teilaufgabe b.'), '\n\n'))

                else:
                    aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                             + f') Berechne die Nullstellen der Graphen mithilfe '
                                             + f'der Normalform aus Teilaufgabe b.'), '\n\n'))
                loesung.append(lsg)
                liste_punkte.append(punkte)
                i += 1
    if 'd' in teilaufg:
        # zu einer gegebenen Funktionsgleichung in Scheitelpunktsform den Graphen zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        k = anz_np + anz_ap
        bez_fkt_d = fkt_bez[k]
        fkt_d = (x - xwert_s[k])**2+ywert_s[k]
        fkt_d_spf_str = (r' \left( x' + vorz_str(-1 * xwert_s[k]) + r' \right) ^2 '
                         + vorz_str(ywert_s[k]))
        punkte = 3
        aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + r') Zeichne den Graphen von $'
                                 + bez_fkt_d + '$(x) = $' + fkt_d_spf_str + '$ im Koordinatensystem ein.'), ' \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Scheitelpunkt~(1BE) \quad Graph~(1BE) \quad '
                        + r'Scheitelpunkt~und~a~stimmen~überein \quad (1BE) }')
        if 'f' not in teilaufg:
            loesung.append('Figure')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            graph_xyfix(*[fkt_d], bezn=bez_fkt_d, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        else:
            loesung.append(r' \\ \mathrm{Graph~siehe~Lösung~Teilaufgabe~f.} ')
        anz_np += 1
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # eine in Normalform gegebene Funktionsgleichung in Scheitelpunktsform umwandeln und den Scheitelpunkt, sowie den Faktor a daraus bestimmen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        k = anz_np + anz_ap
        bez_fkt_e = fkt_bez[k]
        fkt_e = fakt_ap[anz_ap]*(x - xwert_s[anz_np+anz_ap])**2+ywert_s[anz_ap + anz_np]
        fkt_e_nf_str = (vorz_v_aussen(fakt_ap[anz_ap],'x^2')
                        + vorz_v_innen(-2 * fakt_ap[anz_ap] * xwert_s[k], 'x')
                        + vorz_str(fakt_ap[anz_ap]*xwert_s[k]**2 + ywert_s[k]))
        fkt_e_spf_str = (vorz_v_aussen(fakt_ap[anz_ap],'') + r' \left( x'
                         + vorz_str(-1 * xwert_s[k]) + r' \right) ^2 '
                         + vorz_str(ywert_s[k]))
        aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + f') Forme die Funktion $' + bez_fkt_e
                        + '$(x) = $' + fkt_e_nf_str + '$ in die Scheitelpunktform um, nenne Scheitelpunkt und a.'),
                        ' \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + bez_fkt_e + '(x) ~=~' + fkt_e_nf_str + '~=~'
                       + vorz_v_aussen(fakt_ap[anz_ap],'') + r' \left( x^2'
                       + vorz_v_innen(-2 * xwert_s[k], 'x') + r' \right)'
                       + vorz_str(fakt_ap[anz_ap]*xwert_s[k]**2 + ywert_s[k]) + '~=~'
                       + vorz_v_aussen(fakt_ap[anz_ap],'') + r' \left( x^2'
                       + vorz(-1*xwert_s[anz_ap + anz_np]) + r' 2 \cdot '
                       + gzahl(abs(xwert_s[anz_ap + anz_np])) + 'x+'
                       + gzahl(abs(xwert_s[k])) + '^2'
                       + '-' + gzahl(abs(xwert_s[k])) + r'^2 \right) '
                       + vorz_str(fakt_ap[anz_ap]*xwert_s[k]**2 + ywert_s[k])
                       + r' \quad (2BE) \\' + vorz_v_aussen(fakt_ap[anz_ap],'') + r' \left( \left( x'
                       + vorz_str(-1*xwert_s[k]) + r' \right)^2'
                       + '-' + gzahl(abs(xwert_s[k])) + r'^2 \right) '
                       + vorz_str(fakt_ap[anz_ap]*xwert_s[k]**2 + ywert_s[k])
                       + '~=~' + vorz_v_aussen(fakt_ap[anz_ap],'') + r' \left(x'
                       + vorz_str(-1*xwert_s[k]) + r' \right)^2'
                       + vorz_str(-1*fakt_ap[anz_ap]*xwert_s[k]**2)
                       + vorz_str(fakt_ap[anz_ap]*xwert_s[k]**2 + ywert_s[k]) + '~=~'
                       + fkt_e_spf_str + r' \quad (2BE) \\ S \left( ' + gzahl(xwert_s[anz_np+anz_ap]) + r' \vert '
                       + gzahl(ywert_s[anz_np+anz_ap]) + r' \right) \quad \mathrm{und} \quad a ~=~ '
                       + gzahl(fakt_ap[anz_ap]) + r' \quad (1BE)')
        liste_punkte.append(punkte)
        i += 1

        if 'f' in teilaufg:
            # zur gegebenen Funktion den Graphen zeichnen
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            if 'd' in teilaufg:
                graph_xyfix(fkt_e, (x - xwert_s[k-1])**2+ywert_s[k-1],
                            bezn=[bez_fkt_e, fkt_bez[k-1]], name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
            else:
                graph_xyfix(*[fkt_e], bezn=bez_fkt_e, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
            punkte = 3
            aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + r') Zeichne den Graphen von '
                                    + bez_fkt_e + ' im Koordinatensystem ein und überprüfe deine Ergebnisse aus '
                                    + 'Teilaufgabe e).'))
            loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Scheitelpunkt~(1BE) \quad Graph~(1BE) \quad '
                            + r'Scheitelpunkt~und~a~stimmen~überein \quad (1BE) }', 'Figure'))
            liste_punkte.append(punkte)
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(
                f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def parabel_und_gerade(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], pruef_kl10=False, neue_seite=None, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS Funktionsgleichungen einer Parabel ablesen und umformen, Graphen einzeichnen und Wertetabellen erstellen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Ist der Parameter "pruef_kl10=True" dann wird unter der Teilaufgabe ein Notizfeld für die Berechnungen angezeigt. Standardmäßig ist "pruef_kl10=False" und es wird kein Notizfeld unter der Teilaufgabe angezeigt.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt kein erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    # Erstellen der Parabelgleichung
    nst1 = random.choice([-4, -3, -2, -1, 0, 1])
    abstand_nst = random.choice([2, 4])
    nst2 = nst1 + abstand_nst
    while nst1+nst2 == 0:
        nst1 = -1 * nzahl(1, 3)
        abstand_nst = random.choice([2, 4])
        nst2 = nst1 + abstand_nst
    fkt_p_lf = (x - nst1) * (x - nst2)
    fkt_p_nf = x**2-(nst1+nst2)*x + nst1*nst2
    fkt_p_sf = (x - (nst1 + nst2) / 2) ** 2 + nst1 * nst2 - ((nst1 + nst2) ** 2) / 4
    # print(fkt_p_nf)

    # Erstellen der linearen Funktion
    if abstand_nst == 2:
        xwert_p = nst1 - 1
        ywert_p = fkt_p_nf.subs(x, xwert_p)
        g_m = -1 * nzahl(1,5)/2
        g_n = ywert_p - xwert_p * g_m
        while abs(g_n) > 5:
            g_m = nzahl(1, 5) / 2
            g_n = ywert_p - xwert_p * g_m
        text = gzahl(abs(g_m)) + ' LE nach unten'
        fkt_g = x * g_m + g_n
    else:
        xwert_p = nst1 + 1
        ywert_p = fkt_p_nf.subs(x, xwert_p)
        g_m = nzahl(1,5)/2
        g_n = ywert_p - xwert_p * g_m
        while abs(g_n) > 5:
            g_m = nzahl(1, 5) / 2
            g_n = ywert_p - xwert_p * g_m

        text = gzahl(abs(g_m)) + 'LE nach oben'
        fkt_g = x * g_m + g_n
    wertetabelle = [[xwert, fkt_g.subs(x,xwert)] for xwert in range(-5,6) if abs(fkt_g.subs(x,xwert)) <= 5 and abs(fkt_g.subs(x,xwert)) % 1 == 0]
    punkt_p = wertetabelle[0]
    punkt_q = wertetabelle[-1]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'Aufgabe_{nr}']
    grafiken_loesung = []
    graph_xyfix(fkt_p_nf, bezn='p',  name=f'Aufgabe_{nr}.png')

    if 'a' in teilaufg:
        # Scheitelpunkt einer Parabel ablesen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 1
        aufgabe.extend((NoEscape('Im unteren Koordinatensystem ist der Graph der Parabel p(x) = $ x^2 '
                        + vorz_v_innen(-1*(nst1+nst2),'x') + vorz_str(nst1 * nst2) + '$ dargestellt. \n\n'),
                        ['Grafik','200px'], NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                                     + r') Lesen Sie den Scheitelpunkt S'
                                                     + r'$ \left( \qquad \vert \qquad \right) $ der Parabel ab. '),
                        ' \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{der~Scheitelpunkt~lautet:} \quad S \left( '
                       + gzahl((nst1 + nst2) / 2) + r' \vert ' + gzahl(nst1 * nst2 - ((nst1 + nst2) ** 2) / 4)
                       + r' \right) \quad (1BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # Parabelgleichung in Scheitelpunktform aufstellen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + r') Stellen Sie die Parabelgleichung in '
                                + r'Scheitelpunktform auf.'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_klein')
        else:
            aufgabe.append(' \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad p(x) ~=~ \left( x' + vorz_str(-1*(nst1 + nst2) / 2)
                       + r' \right) ^2 ' + vorz_str(nst1 * nst2 - ((nst1 + nst2) ** 2) / 4) + r' \quad (2BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # Nullstellen der Parabel berechnen
        stern = r'$ ^{ \star } $' if pruef_kl10 else ''
        liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))
        punkte = 5
        aufgabe.append(NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i]) + ') Berechnen Sie die Nullstellen '
                                + 'und vergleichen Sie ihre Ergebnisse mit dem Graphen.'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        loesung.append(str(liste_teilaufg[i]) + r') \quad p(x) ~=~ 0 \quad \to \quad 0 ~=~ x^2 '
                       + vorz_v_innen(-1*(nst1+nst2),'x') + vorz_str(nst1 * nst2) + r' \quad (1BE) \hspace{10em} \\'
                       + r' x_{ 1,2 } ~=~ - \frac{p}{2} \pm \sqrt{ \left( \frac{p}{2} \right) ^2 - q } '
                       + r' ~=~ - \frac{ ' + gzahl(-1*(nst1+nst2)) + r' }{2} \pm \sqrt{ \left( \frac{ '
                       + gzahl( -1 * (nst1+nst2)) + r'}{2} \right) ^2 ' + vorz_str(-1*nst1*nst2) + '} '
                       + '~=~ ' + gzahl(Rational(nst1+nst2,2)) + r' \pm \sqrt{ '
                       + gzahl(Rational((nst1+nst2)**2 - 4*(nst1*nst2),4)) + r' } \quad (1BE) \\ '
                       + 'x_1 ~=~ ' + gzahl(nst1) + r' \quad \mathrm{und} \quad x_2 ~=~ ' + gzahl(nst2)
                       + r' \quad \to \quad \mathrm{Sie~stimmen~mit~Graphen~überein} \quad (3BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # mithilfe zweier gegebener Punkte den Graphen einer linearen Funktion einzeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{str(nr)}_{str(liste_teilaufg[i])})')
        punkte = 3

        graph_xyfix(*[fkt_p_nf, fkt_g], bezn=['p', 'g'], name=f'Loesung_{str(nr)}_{str(liste_teilaufg[i])})')
        aufgabe.extend((NoEscape(r' \noindent Gegeben sind zwei Punkte der linearen Funktion g mit P$ \left( '
                                 + gzahl(punkt_p[0]) + r' \vert ' +  gzahl(punkt_p[1]) + r' \right) $ und Q$ \left( '
                                 + gzahl(punkt_q[0]) + r' \vert ' +  gzahl(punkt_q[1]) + r' \right). $'),' \n\n ',
                        NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                 + r') Zeichnen Sie den Graphen der linearen Funktion g in das obere '
                                 + r'Koordinatensystem ein.'),' \n\n'))
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(2BE) \quad Graph~(1BE)} ',['Grafik','150px']))
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Funktionsgleichung der gezeichneten linearen Funktionen erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + r') Erläutern Sie anhand des Graphen die '
                                + r'Funktionsgleichung von $ g(x) =  ' + vorz_v_aussen(g_m, 'x')
                                + vorz_str(g_n) + r'$. '))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_gross')
        else:
            aufgabe.append(' \n\n')

        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l',
                        data='Erläuterung der Funktionsgleichung'), 'Punkte')
        table1.add_row('', '-', 'die Zahl hinter dem x ist der y-Achsenabschnitt n und entspricht '
                       + 'dem Schnittpunkt des Graphen mit dem y-Achse', '2BE')
        table1.add_row('', '-', 'die Zahl vorm x entspricht der Steigung m und kann mithilfe des '
                                'Steigungsdreiecks bestimmt werden.', '1BE')
        table1.add_row('', '-', f'dafür geht man vom Punkt ( 0 | {gzahl(g_n)} ) eins nach recht und dann '
                       + text + ', was der Steigung entspricht', '1BE')
        table1.add_row('', '', '', 'insg.: ' + str(punkte) + 'BE')
        loesung.append(table1)
        loesung.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        # Schnittpunkte der linearen Funktion mit der Parabel berechnen
        stern = r'$ ^{ \star } $' if pruef_kl10 else ''
        liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))
        p = -1* (g_m + nst1 + nst2)
        q = nst1 * nst2 - g_n
        xwert_s1 = N(-p/2 + sqrt((p/2)**2-q),3)
        xwert_s2 = N(-p/2 - sqrt((p/2)**2-q),3)
        ywert_s1 = N(fkt_g.subs(x, xwert_s1),3)
        ywert_s2= N(fkt_g.subs(x, xwert_s2),3)
        punkte = 7
        aufgabe.append(NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i]) + ') Berechnen Sie die Schnittpunkte '
                                + 'der linearen Funktion mit dem Graphen der Parabel.'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_gross')
        else:
            aufgabe.append(' \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad g(x) ~=~ p(x) \quad \to \quad  '
                       + vorz_v_aussen(g_m, 'x') + vorz_str(g_n) + '~=~ x^2 '
                       + vorz_v_innen(-1*(nst1+nst2),'x') + vorz_str(nst1 * nst2) + r' \quad \vert '
                       + vorz_str(-1*g_n) + r' \quad \vert ' + vorz_v_innen(-1*g_m,'x')
                       + r' \quad \to \quad 0 ~=~ x^2 ' + vorz_v_innen(p,'x') + vorz_str(q)
                       + r' \quad (2BE) \\ x_{ 1,2 } ~=~ - \frac{p}{2} \pm \sqrt{ \left( \frac{p}{2} \right) ^2 - q} '
                       + r' ~=~ - \frac{ ' + gzahl(p) + r' }{2} \pm \sqrt{ \left( \frac{ '
                       + gzahl(p) + r'}{2} \right) ^2 ' + vorz_str(-1*q) + ' } ~=~'
                       + '~=~ ' + gzahl(Rational(-1*p,2)) + r' \pm \sqrt{ '
                       + gzahl(Rational((p)**2 - 4*(q),4)) + r' } \quad (1BE) \\ '
                       + 'x_1 ~=~ ' + gzahl(xwert_s1) + r' \quad \mathrm{und} \quad x_2 ~=~ ' + gzahl(xwert_s2)
                       + r' \quad (2BE) \\ S_1 \left( ' + gzahl(xwert_s1) + r' \vert ' + gzahl(ywert_s1)
                       + r' \right) \quad \mathrm{und} \quad S_2 \left( ' + gzahl(xwert_s2) + r' \vert '
                       + gzahl(ywert_s2) + r' \right) \quad (2BE) ')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    liste_punkte = BE if len(BE) == len(teilaufg) else liste_punkte
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]