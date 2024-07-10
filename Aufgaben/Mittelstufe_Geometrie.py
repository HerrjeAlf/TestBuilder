import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Math)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
nr_aufgabe = 0

# Trigonometrie
def berechnungen_bel_dreieck(nr, teilaufg=['a', 'b', 'c']):
    # Berechnungen im allgemeinen Dreieck

    liste_punkte = []
    liste_bez = []
    i = 0
    def werte_bel_dreieck():
        beta = nzahl(30, 60)
        gamma = nzahl(30,60)
        alpha = 180 - gamma - beta
        print('alpha ' + str(alpha)), print('beta ' + str(beta)), print('gamma ' + str(gamma))
        seite_a = nzahl(6, 12)
        seite_b = round(seite_a * math.sin(math.radians(beta)) / math.sin(math.radians(alpha)), 1)
        seite_c = round(seite_a * math.sin(math.radians(gamma)) / math.sin(math.radians(alpha)), 1)
        auswahl = random.sample([0, 1, 2], 3)
        auswahl_liste = {'Seite_bez' : [['a', 'b', 'c'][x] for x in auswahl],
                         'Seite_wert' : [seite_a, seite_b, seite_c],
                         'Winkel_bez' : [[r' \alpha', r' \beta', r' \gamma'][x] for x in auswahl],
                         'Winkel_wert' : [alpha, beta, gamma]}

        return auswahl_liste

    auswahl_liste = werte_bel_dreieck()
    seite_1, seite_wert_1, winkel_1, winkel_wert_1 = [element[0] for element in auswahl_liste.values()]
    seite_2, seite_wert_2, winkel_2, winkel_wert_2 = [element[1] for element in auswahl_liste.values()]
    seite_3, seite_wert_3, winkel_3, winkel_wert_3 = [element[2] for element in auswahl_liste.values()]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Von einem allgemeinen Dreieck, sind folgende Daten gegeben: ',
               seite_1 + '~ = ~' + latex(seite_wert_1) + r'cm, \quad '
               + seite_2 + '~ = ~' + latex(seite_wert_2) + r'cm, \quad '
               + winkel_1 + '~ = ~' + latex(winkel_wert_1) + r' ^{ \circ } \quad']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    grafiken_aufgaben = []
    grafiken_loesung = []


    if 'a' or 'b' or 'c' in teilaufg:
        # Berechnung der Winkel im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 10
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die restlichen Winkel im Dreieck. '
                                                'Fertige dazu eine Planskizze an. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{geg:~} ' + str(seite_1) + '~=~' + latex(seite_wert_1)
                                                 + r'cm, \quad ' + str(seite_2) + '~=~' + latex(seite_wert_2)
                                                 + r'cm, \quad ' + winkel_1 + '~=~' + latex(winkel_wert_1)
                                                 + r'^{ \circ } \quad \mathrm{ges:~}' + winkel_2
                                                 + r' \quad (1P) \quad \mathrm{aus~der~Planskizze~(2P)~folgt:~} \\'
                                                 + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                 + r' \frac{' + str(seite_2) + '}{~sin(' + winkel_2
                                                 + r')} \quad \to \quad \frac{~sin(' + winkel_2 + ')}{sin('
                                                 + winkel_1 + r')} ~=~ \frac{' + str(seite_2) + '}{'
                                                 + str(seite_1) + r'} \quad \vert \cdot sin(' + winkel_1
                                                 + r') \quad (2P) \\' + 'sin(' + winkel_2 + r') ~=~ \frac{'
                                                 + str(seite_2) + r'}{' + str(seite_1) + r'} \cdot sin(' + winkel_1
                                                 + r') \quad \vert ~ sin^{ -1}() \quad \to \quad ' + winkel_2
                                                 + r' ~=~ sin^{ -1} \Big( \frac{' + str(seite_2)  + r'}{' + str(seite_1)
                                                 + r'} \cdot sin(' + winkel_1 + r') \Big) \quad (1P) \\'
                                                 + winkel_2 + r' ~=~ sin^{ -1} \Big( \frac{'
                                                 + latex(seite_wert_2) + 'cm}{' + latex(seite_wert_1)
                                                 + r'cm} \cdot sin(' + latex(winkel_wert_1) + r'^{ \circ } ) \Big) ~=~'
                                                 + latex(winkel_wert_2) + r'^{ \circ } \quad (2P) \\'
                                                 + winkel_3 + r'~=~ 180^{ \circ} ~-~' + str(winkel_wert_1)
                                                 + r'^{ \circ} ~-~ ' + str(winkel_wert_2) + r'^{ \circ} ~=~ '
                                                 + str(winkel_wert_3) + r'^{ \circ} \quad (2P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Berechnung der fehlenden Seitenlänge im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 4
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Länge der Seite {seite_3} mit dem Sinussatz. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{aus~der~Planskizze~folgt:~} \hspace{15em} \\'
                                                 + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                 + r' \frac{' + str(seite_3) + '}{~sin(' + winkel_3
                                                 + r')} \quad \vert \cdot sin(' + winkel_3 + r') \quad \to \quad '
                                                 + str(seite_3) + r'~=~ \frac{' + str(seite_1) + r' \cdot sin('
                                                 + winkel_3 + ') }{ sin(' + winkel_1 + r') } \quad (2P) \\'
                                                 + str(seite_3) + r'~=~ \frac{' + str(seite_wert_1) + r'cm \cdot sin('
                                                 + latex(winkel_wert_3) + r' ^{ \circ } )}{ sin(' + latex(winkel_wert_1)
                                                 + r' ^{ \circ } )} ~=~' + latex(seite_wert_3) + r'cm \quad (2P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    if 'c' in teilaufg:
        # Berechnung der Fläche im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 3
        flaeche = 0.5*seite_wert_1*seite_wert_2*math.sin(math.radians(winkel_wert_3))
        print(N(flaeche,3))
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Fläche des Dreiecks. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad A ~ = ~ \frac{1}{2} \cdot ' + seite_1 + r' \cdot ' + seite_2
                                                 + r' \cdot sin(' + winkel_3 + r') ~=~ \frac{1}{2} \cdot '
                                                 + latex(seite_wert_1) + r'cm \cdot ' + latex(seite_wert_2)
                                                 + r'cm \cdot sin(' + latex(winkel_wert_3) + r'^{ \circ } ) ~=~ '
                                                 + latex(N(flaeche,3)) + r'cm^2 \quad (3P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def pruefung_Kl10_allg_dr_01(nr, teilaufg=['a', 'b', 'c', 'd']):
    liste_punkte = []
    liste_bez = []
    i = 0
    alpha = nzahl(30,60)
    beta = nzahl(70,110)- alpha
    gamma = 180 - alpha - beta
    print('alpha ' + str(alpha)), print('beta ' + str(beta)), print('gamma ' + str(gamma))
    seite_c = nzahl(6,12)
    seite_a = round(seite_c * math.sin(math.radians(alpha))/math.sin(math.radians(gamma)),1)
    seite_b = round(seite_c * math.sin(math.radians(beta))/math.sin(math.radians(gamma)),1)
    seite_h = round(seite_a * math.sin(math.radians(beta)),1)
    print('seite a ' + str(seite_a)), print('seite b ' + str(seite_b)), print('seite c ' + str(seite_c)), print('seite h ' + str(seite_h))
    gamma_1 = 90 - alpha
    xwert_punkt_c = round(math.cos(math.radians(alpha))*seite_b,3)
    ywert_punkt_c = round(math.sin(math.radians(alpha))*seite_b,3)
    flaeche = round(0.5*seite_a*seite_b*math.sin(math.radians(gamma)),2)
    # Listen für die Zeichung des Dreiecks
    pkt_list = [[0, 0], [seite_c, 0], [xwert_punkt_c, ywert_punkt_c],[xwert_punkt_c,0]]
    pkt_bez = ['A', 'B', 'C', 'F']
    st = ['a', 'b', 'c', 'h']
    st_werte = [seite_a, seite_b, seite_c, seite_h]
    wk = [r' \alpha ', r' \beta ', r' \gamma_1 ',  r' ^{ \circ}']
    wk_werte = [alpha, beta, gamma_1, 90]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
                NoEscape('Abbildung 1 stellt ein beliebiges Dreieck mit $ h = '
                         + latex(seite_h) + '$cm, $a = ' + latex(seite_a) + r'$cm und $ \gamma_1 = '
                         + latex(gamma_1) + r'^{ \circ}$ dar.'), 'Figure']
    loesung = [r' \mathbf{Lösung~AufgSabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'{str(nr)}']
    grafiken_loesung = []

    if 'a' or 'b' or 'c' or 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 5
        dreieck_zeichnen_mit_hoehe(pkt_list, pkt_bez, st, wk, f'{str(nr)}')
        aufgabe.append(NoEscape(str(liste_teilaufg[i]) + ') Berechne die Länge der Strecke ' + r'$ \overline{FB} $'
                       + r' \\\\'))
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{geg: \quad a~=~' + str(seite_a) + r'cm,~ h~=~'
                                                 + str(seite_h) + r' \quad ges: \quad \overline{FB} \quad (1P)} \\'
                                                 + r'h^2~+~ \overline{FB}^2~=~a^2 \quad \vert ~- h^2'
                                                 r' \quad \to \quad \overline{FB}^2~=~a^2~-~h^2 \quad \vert \sqrt{}'
                                                 r' \quad \to \quad \overline{FB}~=~ \sqrt{a^2~-~h^2} \quad (2P) \\'
                                                 r' \overline{FB} ~=~ \sqrt{(' + str(seite_a) + 'cm)^2 - ('
                                                 + str(seite_h) + 'cm)^2 } ~=~'
                                                 + gzahl(N(seite_c - xwert_punkt_c,3)) + r'cm \quad (2P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    if 'b' or 'c' or 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 6
        aufgabe.append(NoEscape(str(liste_teilaufg[i]) + ') Berechne die Größe der Winkel ' + r'$ \alpha $'
                                + ' und ' + r'$ \beta $' + r'. \\\\'))
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \alpha ~=~180^{ \circ } - 90^{ \circ } - \gamma_1 '
                                                 r' ~=~180^{ \circ } - 90^{ \circ } -' + str(gamma_1)
                                                 + r'^{ \circ} ~=~' + str(alpha) + r'^{ \circ} \quad (2P) \\'
                                                 r' sin( \beta ) ~=~ \frac{h}{a} \quad \vert sin^{-1}() \quad'
                                                 r' \to \quad \beta ~=~ sin^{-1} \Big( \frac{h}{a} \Big) ~=~ '
                                                 r'sin^{-1} \Big( \frac{' + str(seite_h) + '}{' + str(seite_a)
                                                 + r'} \Big) ~=~ ' + str(beta) + r'^{ \circ} \quad (4P) \\ '
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    if 'c' or 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 4
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Länge der Seite b. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \frac{a}{sin( \alpha)} ~=~ \frac{b}{sin( \beta)}'
                                                 r' \quad \vert \cdot sin( \beta) \quad \to \quad b~=~'
                                                 r' \frac{a \cdot sin( \beta )}{sin( \alpha )} ~=~ \frac{'
                                                 + str(seite_a) + r'cm \cdot sin(' + str(beta) + r'^{ \circ})}'
                                                 r'{sin(' + str(alpha) + r'^{ \circ})} ~=~' + str(seite_b)
                                                 + r'cm \quad (4P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 5
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Fläche vom Dreieck ABC. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \gamma ~=~180^{ \circ } - \alpha - \beta ~=~'
                                                 r'180^{ \circ } - ' + str(alpha) + r'^{ \circ } - ' + str(beta)
                                                 + r'^{ \circ } ~=~' + str(gamma) + r'^{ \circ} \quad (2P) \\'
                                                 r' A ~=~ \frac{1}{2} \cdot a \cdot b \cdot sin( \gamma ) ~=~'
                                                 r' \frac{1}{2} \cdot ' + str(seite_a) + r'cm \cdot '
                                                 + str(seite_b) + r'cm \cdot sin(' + str(gamma)
                                                 + r'^{ \circ }) ~=~' + str(flaeche) + r'cm^2 \quad (3P) \\'
                                                 + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\'))
        liste_punkte.append(pkt)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]