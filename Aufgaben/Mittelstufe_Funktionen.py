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


def stirb_langsam_2(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], BE=[]):
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

    n = -1 * x_0 * steigung
    fkt = steigung * x + n
    fkt_str = vorz_v_aussen(steigung, 'x') + vorz_str(n)
    fkt_vers = fkt - y_vers
    fkt_vers_str = vorz_v_aussen(steigung, 'x') + vorz_str(n - y_vers)
    v_flugzeug = 200 + nzahl(1,10)*5
    p1, p2 = ganze_werte[1], ganze_werte[2]
    abstand = round(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2),2)
    zeit = int(abstand*1000 / v_flugzeug)

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
        steigung = round(wert_steigung/20,3)
        swinkel = round(np.arctan(steigung)*180/pi, 1)
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
                        + f'des ILS? Landet die Boing auf der Landebahn? \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad x_0 ~=~ - \frac{n}{m} ~=~ - \frac{ ' + gzahl(round(n-y_vers,3))
                       + r'}{' + gzahl(round(steigung,3)) + '} ~=~' + gzahl(round(-1*(n-y_vers)/steigung,3)) + lsg
                       + r' \quad (4BE)')
        liste_punkte.append(punkte)
        i += 2

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
