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


def stirb_langsam_2(nr, teilaufg=['a', 'b', 'c'], BE=[]):
    # In dieser Aufgabe können die SuS ihre Kenntnisse der linearen Funktionen auf verschiedene Situationen, angelehnt auf Szenen im Film "Stirb Langsam" anwenden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    steigung = Rational(nzahl(1, 8), 20)
    x_0 = random.choice([3, 2.5, 2])
    y_vers = Rational(nzahl(2, 8) * 50,100)
    wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
    ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0]
    while len(ganze_werte) == 0:
        steigung = Rational(nzahl(1, 8), 20)
        x_0 = random.choice([3, 2.5, 2])
        y_vers = Rational(nzahl(2, 8) * 50, 100)
        wertetabelle = [[element, steigung * element - x_0 * steigung] for element in range(0, 200)]
        ganze_werte = [[element[0], int(element[1])] for element in wertetabelle if element[1] % 1 == 0]

    n = -1 * x_0 * steigung
    fkt = steigung * x + n
    fkt_str = vorz_v_aussen(steigung, 'x') + vorz_str(n)
    fkt_vers = fkt - y_vers
    fkt_vers_str = vorz_v_aussen(steigung, 'x') + vorz_str(n - y_vers)
    v_flugzeug = 600 + nzahl(1,10)*40
    p1, p2 = ganze_werte[1], ganze_werte[2]
    abstand = sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    zeit = int(abstand / v_flugzeug)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Im zweiten Teil der legendären „Stirb langsam“ – Reihe versuchen Terroristen durch eine Manipulation '
               'des Instrumentenlandesystem (ILS) eines Flughafen, General Ramon Esperanza freizupressen. '
               'Die Terroristen lassen zur Abschreckung eine Boeing 747 landen, welches beim Landeanflug auf der '
               'Startbahn zerbricht und ausbrennt. Dafür manipulieren Sie die die Landeautomatik des Flugzeuges, '
               f'so dass in der Landeautomatik die Landebahn um {gzahl(y_vers*100)}m nach unten verschoben wird', 'Bild']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['stirb_langsam_2']
    grafiken_loesung = []

    if 'a' in teilaufg:
        # aus zwei gegebenen Punkten die Geradengleichung
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        wertetabelle = [[element, fkt.subs(x,element)] for element in range(0,200)]

        aufgabe.extend((f'alle Angaben sind in Kilometer \n\n'
                        f'Das Radar des Flughafens ortet die Boing zuerst bei Punkt A( {gzahl(p2[0])} | '
                        f'{gzahl(p2[1])} ) und danach bei Punkt B( {gzahl(p1[0])} | {gzahl(p1[1])} ). \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie die Funktionsgleichung der Flugbahn. \n\n'))
        loesung.append((str(liste_teilaufg[i]) + r') \quad f(x) ~=~ \frac{' + gzahl(p2[1]) + vorz_str(-1*p1[1]) + r'}{'
                        + gzahl(p2[0]) + gzahl(-1*p1[0]) + r'} \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                        + vorz_str(p2[1]) + '~=~' + gzahl(steigung) + r' \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                        + vorz_str(p2[1]) + '~=~' + vorz_v_aussen(steigung,'x') + vorz_str(-1 * steigung * p2[0])
                        + vorz_str(p2[1]) + '~=~' + fkt_str + r' \quad (3BE) \\'))

        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # aus zwei gegebenen Punkten die Geradengleichung
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        wertetabelle = [[element, fkt.subs(x,element)] for element in range(0,200)]

        aufgabe.extend((f'alle Angaben sind in Kilometer \n\n'
                        f'Das Radar des Flughafens ortet die Boing zuerst bei Punkt A( {gzahl(p2[0])} | '
                        f'{gzahl(p2[1])} ) und danach bei Punkt B( {gzahl(p1[0])} | {gzahl(p1[1])} ). \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie die Funktionsgleichung der Flugbahn. \n\n'))
        loesung.append((str(liste_teilaufg[i]) + r') \quad f(x) ~=~ \frac{' + gzahl(p2[1]) + vorz_str(-1*p1[1]) + r'}{'
                        + gzahl(p2[0]) + gzahl(-1*p1[0]) + r'} \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                        + vorz_str(p2[1]) + '~=~' + gzahl(steigung) + r' \left(x' + vorz_str(-1*p2[0]) + r' \right) '
                        + vorz_str(p2[1]) + '~=~' + vorz_v_aussen(steigung,'x') + vorz_str(-1 * steigung * p2[0])
                        + vorz_str(p2[1]) + '~=~' + fkt_str + r' \quad (3BE) \\'))

        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
