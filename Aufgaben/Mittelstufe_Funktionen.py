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


def stirb_langsam_2(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e'], BE=[]):
    # In dieser Aufgabe können die SuS ihre Kenntnisse der linearen Funktionen auf verschiedene Situationen, angelehnt auf Szenen im Film "Stirb Langsam" anwenden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    wert_steigung = nzahl(1, 8)
    steigung = Rational(wert_steigung,20)
    x_0 = random.choice([3, 2.5, 2])
    y_vers = Rational(nzahl(2, 8),20)
    wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
    ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0]
    while len(ganze_werte) == 0:
        wert_steigung = nzahl(1, 8)
        steigung = Rational(wert_steigung, 20)
        x_0 = random.choice([3, 2.5, 2])
        y_vers = Rational(nzahl(2, 8), 20)
        wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
        ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0]

    # Werte für die Boing
    n = -1 * x_0 * steigung
    fkt = steigung * x + n
    fkt_str = vorz_v_aussen(steigung, 'x') + vorz_str(n)
    fkt_vers = fkt - y_vers
    fkt_vers_str = vorz_v_aussen(steigung, 'x') + vorz_str(n - y_vers)
    v_flugzeug = 200 + nzahl(1,10)*5
    p1, p2 = ganze_werte[1], ganze_werte[2]
    abstand = round(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2),2)
    zeit = int(abstand*1000 / v_flugzeug)
    swinkel = round(np.arctan(wert_steigung/20) * 180 / pi, 1)

    # Werte für den Airbus
    steigung_airbus = -1 * nzahl(1, 15) / 5
    n_airbus = int(ganze_werte[0][1]) - steigung_airbus * int(ganze_werte[0][0])
    xwert_s = Rational(n_airbus - n, steigung - steigung_airbus)
    ywert_s = N(steigung_airbus * xwert_s + n_airbus, 2)
    swinkel_airbus = round(np.arctan(steigung_airbus) * 180 / pi, 1)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Im zweiten Teil der legendären „Stirb langsam“ – Reihe manipulieren Terroristen '
               'des Instrumentenlandesystem (ILS) eines Flughafen, um General Ramon Esperanza freizupressen. '
               'Dabei lassen die Terroristen zur Abschreckung eine Boeing 747 landen, welche durch die Manipulation '
               'beim Landeanflug auf der Startbahn zerbricht und ausbrennt. ', 'Bild']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['stirb_langsam_2']
    grafiken_loesung = []

    if 'a' in teilaufg:
        # aus zwei gegebenen Punkten die Geradengleichung
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.extend((f'alle Angaben sind in Kilometer \n\n'
                        f'Das Radar des Flughafens ortet die Boing zuerst bei Punkt P({gzahl(p2[0])}|'
                        f'{gzahl(p2[1])}) und nach {gzahl(zeit)}s bei Punkt Q({gzahl(p1[0])}|{gzahl(p1[1])}). \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie die Funktionsgleichung der Flugbahn. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad f(x) ~=~ \frac{' + gzahl(p2[1]) + vorz_str(-1*p1[1]) + r'}{'
                       + gzahl(p2[0]) + gzahl(-1*p1[0]) + r'} \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                       + vorz_str(p2[1]) + '~=~' + gzahl(steigung) + r' \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                       + vorz_str(p2[1]) + '~=~' + vorz_v_aussen(steigung,'x') + vorz_str(-1 * steigung * p2[0])
                       + vorz_str(p2[1]) + '~=~' + fkt_str + '~=~' + vorz_v_aussen(round(steigung,3),'x')
                       + vorz_str(round(n,3)) + r' \quad (3BE) \\')
        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # die SuS sollen den Abstand zwischen zwei Punkten bestimmen und damit die Geschwindigkeit berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie Geschwindigkeit der Boing (in km/h) im '
                       + f'Landeanflug.  \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad d(PQ) ~=~ \sqrt{ \left( ' + gzahl(p2[0])
                       + vorz_str(-1*p1[0]) + r' \right) ^2 + \left( ' + gzahl(p2[1]) + vorz_str(-1*p1[1])
                       + r' \right) ^2 } ~=~' + gzahl(abstand) + r'km \quad \to \quad v ~=~ \frac{s}{t} '
                       + r'~=~ \frac{' + gzahl(abstand*1000) + 'm}{' + gzahl(zeit) + 's} ~=~'
                       + gzahl(int(abstand*1000/zeit)) + r' \frac{m}{s} ~=~' + gzahl(int(abstand*1000/zeit*3.6))
                       + r' \frac{km}{h} \quad (4BE) \\')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # die SuS sollen die Veränderung des y-Achsenabschnittes durch die Manipulation der Flugbahn erklären
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        aufgabe.extend(('Durch die Manipulation rechnet die Flugzeugelektronik der Boeing mit der Funktion '
                        f' f(x) = {gzahl(round(steigung,3))}x - {gzahl(abs(round(n-y_vers,3)))}. \n\n',
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
        aufgabe.extend(('Ein Flugzeug landet unbeschadet, wenn der Anflugwinkel 3,5° nicht überschreiten. '
                        + 'Aufgrund der Manipulation hat die Boeing vor der Landung keine Zeit die Landeklappen '
                        + 'auszufahren um die Geschwindigkeit und seinen Anflugwinkel zu verringern. \n\n',
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
        lsg = r' \leq 3 \to \mathrm{Die~Boing~landet~auf~der~Landebahn.}' if round(-1*(n-y_vers)/steigung,3) <= 3 else lsg
        aufgabe.extend(('Im Film landet die Boeing, bevor sie zerbricht, trotz der manipulierten Flugbahn '
                        'auf der Landebahn (Nullstelle). Die Landebahn beginnt im Punkt A(3|0) und endet im '
                        'Koordinatenursprung E(0|0). \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie die Landestelle nach der Manipulation '
                        + f'des ILS. Landet die Boing auf der Landebahn? \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad x_0 ~=~ - \frac{n}{m} ~=~ - \frac{ ' + gzahl(round(n-y_vers,3))
                       + r'}{' + gzahl(round(steigung,3)) + '} ~=~' + gzahl(round(-1*(n-y_vers)/steigung,3)) + lsg
                       + r' \quad (4BE)')
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in ['f', 'g'] if element in teilaufg]) > 0:
        # Die SuS sollen den Schnittpunkt zweier linearen Funktionen (Flugbahnen) berechnen


        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.extend((f'Über dem Flughafen kreisen mehrere Flugzeuge und warten auf Landerlaubnis. Ein Airbus bewegt '
                        f'sich auf der Flugbahn h(x) = {gzahl(steigung_airbus)} x {vorz_str(n_airbus)}. \n\n',
                        str(liste_teilaufg[i]) + f') Erläutern Sie, woran man erkennen kann, dass sich die Flugbahnen '
                        + f'schneiden. \n\n',
                        str(liste_teilaufg[i+1]) + f') Berechnen Sie den Schnittpunkt der Flugbahnen. \n\n'))
        loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{~Da~die~Steigungen~der~beiden~Geraden~verschieden~'
                        + r'sind.} \quad (1BE)', str(liste_teilaufg[i]) + r') \quad \mathrm{Ansatz: \quad f(x)=g(x)} '
                        + r' \quad \to \quad ' + fkt_str + '~=~' + vorz_v_aussen(steigung_airbus,'x')
                        + vorz_str(n_airbus) + r' \quad \vert ' + vorz_str(-1 * steigung_airbus)
                        + r' \quad \to ' + vorz_str(-1*n) + r' \quad (3BE) \\'
                        + vorz_v_aussen(steigung - steigung_airbus, 'x')
                        + '~=~' + gzahl(n_airbus - n) +  r' \quad \vert \div' + gzahl(steigung - steigung_airbus)
                        + r' \quad \to \quad x~=~' + gzahl(Rational(n_airbus - n,steigung - steigung_airbus))
                        + r' \quad (3BE) \\ \mathrm{Schnittpunkt \quad S(' + gzahl(xwert_s) + r'~ \vert ~'
                        + gzahl(ywert_s) + r') \quad (2BE) \\'))
        liste_punkte.append(punkte)
        i += 2

    if 'g' in teilaufg:
        # Die SuS sollen den Schnittwinkel zweier linearen Funktionen (Flugbahnen) berechnen

        if 'd' in teilaufg:
            lsg = (r' \mathrm{nach~Teilaufgabe~d~gilt: \quad \alpha ~=~ ' + gzahl(swinkel)
                   +  r' ^{ \circ } und \quad \beta ~=~ tan^{-1}(' + gzahl(steigung_airbus) + '~=~'
                   + gzahl(swinkel_airbus) + r' \quad (2BE) } \\')
            pkt = 2
        else:
            lsg = (r' \mathrm{nach~Teilaufgabe~d~gilt: \quad \alpha ~=~ tan^{-1}(' + gzahl(steigung) + '~=~'
                   + gzahl(swinkel) +  r' ^{ \circ } und \quad \beta ~=~ tan^{-1}(' + gzahl(steigung_airbus) + '~=~'
                   + gzahl(swinkel_airbus) + r' \quad (4BE) } \\')
            pkt = 4

        if abs(swinkel_airbus - swinkel) > 90:
            lsg_1 = (r' > 90 ^{ \circ } \quad \to \quad \gamma ~=~ 180 - ' + gzahl(abs(swinkel_airbus - swinkel))
                     + '~=~' + gzahl(180 - abs(swinkel_airbus - swinkel)) + r' \quad (3BE)')
            pkt += 3
        else:
            lsg_1 = r' \quad (2BE)'
            pkt += 2

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.append(str(liste_teilaufg[i+1]) + f') Berechnen Sie den Schnittwinkel der Flugbahnen des Airbus und '
                       + f'der Boing. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + lsg
                       + r' \gamma ~=~ \vert \beta - \alpha \vert ~=~ \vert ' + gzahl(swinkel_airbus) + '~-~'
                       + gzahl_klammer(swinkel) + r' \vert ~=~' + gzahl(abs(swinkel_airbus - swinkel)) + lsg_1)
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Die SuS sollen den Schnittwinkel zweier linearen Funktionen (Flugbahnen) berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        m_e = nzahl(1, 2)
        x_0_e = random.choice([0.25, 0.5, 0.75, 1])
        n_e = -1 * x_0_e * m_e
        xwert = (1 - n_e)/m_e
        fkt_e = m_e * x + n_e
        fkt_e_str = vorz_v_aussen(m_e, 'x') + vorz_str(n_e)

        aufgabe.extend((f'Ein Flugzeug schafft es nicht mehr rechtzeitig zu landen. Es muss im Punkt ( {xwert} | 1 ) '
                        f'orthogonal zur bisherigen Flugbahn h(x) = {gzahl(m_e)}x {vorz_str(n_e)} durchstarten, '
                        f'damit es nicht abstürzt. \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie die neue Flugbahn, '
                            + f'nachdem es durchgestartet ist. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad ')
        liste_punkte.append(punkte)
        i += 2

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
