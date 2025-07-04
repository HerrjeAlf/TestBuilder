import string
import numpy as np
import random, math
from fractions import Fraction
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Math)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *
import matplotlib.pyplot as plt

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

# Trigonometrie
def kongruente_Dreiecke(nr, teilaufg=['a', 'b'], kongr=['zufällig', 'sss', 'sws', 'wsw','sww', 'nicht kongruent'][0], i=0, BE=[]):
    # Bei dieser Aufgaben sollen die SuS aus den gegebenen Daten eines Dreiecks den Kongruenzsatz erkennen und das Dreieck konstruieren.
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Mit dem Parameter "kongr=" kann festgelegt werden, welcher Kongruenzsatz erzeugt werden soll (0: sss, 1: sws, 2: wsw, 3:sww, 4: Ssw).
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    alpha = 30 + nzahl(1, 6)*5
    beta = 70 + nzahl(1, 8)*5 - alpha
    gamma = 180 - alpha - beta
    seite_c = nzahl(4, 10)
    seite_a = round(seite_c * math.sin(math.radians(alpha)) / math.sin(math.radians(gamma)), 1)
    seite_b = round(seite_c * math.sin(math.radians(beta)) / math.sin(math.radians(gamma)), 1)
    xwert_punkt_c = round(math.cos(math.radians(alpha)) * seite_b, 3)
    ywert_punkt_c = round(math.sin(math.radians(alpha)) * seite_b, 3)
    # Listen für die Zeichung des Dreiecks
    pkt_list = [[0, 0], [seite_c, 0], [xwert_punkt_c, ywert_punkt_c]]
    pkt_bez = ['A', 'B', 'C']
    st = ['a', 'b', 'c']
    st_werte = [seite_a, seite_b, seite_c]
    wk = [r' \alpha ', r' \beta ', r' \gamma']
    wk_werte = [alpha, beta, gamma]


    kongr = random.choice(['sss', 'sws', 'wsw','sww', 'nicht kongruent']) if kongr == 'zufällig' else kongr # hier wird ausgewürfelt, welcher Kongruenzsatz erzeugt werden soll
    if kongr == 'sss':
        auswahl = ['sss', st[0] + '~=~' + gzahl(st_werte[0]) + 'cm',
                   st[1] + '~=~' + gzahl(st_werte[1]) + 'cm',
                   st[2] + '~=~' + gzahl(st_werte[2]) + 'cm']
    elif kongr == 'sws':
        rf = random.choice([[0,2,1], [0,1,2], [1,2,0]]) # mit rf wird die Reihenfolge der gegebenen Werte für sws festgelegt
        auswahl = ['sws', st[rf[0]] + '~=~' + gzahl(st_werte[rf[0]]) + 'cm',
                   st[rf[1]] + '~=~' + gzahl(st_werte[rf[1]]) + 'cm',
                   wk[rf[2]] + '~=~' + gzahl(wk_werte[rf[2]]) + r' ^{  \circ}']
    elif kongr == 'wsw':
        rf = random.choice([[0,2,1], [1,0,2], [0,1,2]]) # mit rf wird die Reihenfolge der gegebenen Werte für wsw festgelegt
        auswahl = ['wsw', st[rf[0]] + '~=~' + gzahl(st_werte[rf[0]]) + 'cm',
                   wk[rf[1]] + '~=~' + gzahl(wk_werte[rf[1]]) + r' ^{  \circ}',
                   wk[rf[2]] + '~=~' + gzahl(wk_werte[rf[2]]) + r' ^{  \circ}']
    elif kongr == 'sww':
        rf = random.choice([[0,0,2], [1,0,1], [2,1,2]]) # mit rf wird die Reihenfolge der gegebenen Werte für sww festgelegt
        auswahl = ['sww',  st[rf[0]] + '~=~' + gzahl(st_werte[rf[0]]) + 'cm',
                   wk[rf[1]] + '~=~' + gzahl(wk_werte[rf[1]]) + r' ^{  \circ}',
                   wk[rf[2]] + '~=~' + gzahl(wk_werte[rf[2]]) + r' ^{  \circ}']
    else:
        rf_elem = elemente_sort(st_werte)
        rf = random.choice([[rf_elem[0],rf_elem[1]], [rf_elem[0],rf_elem[2]], [rf_elem[1], rf_elem[2]]]) # mit rf wird die Reihenfolge der gegebenen Werte festgelegt
        if rf[1] < rf[0]:
            aufg2 = st[rf[0]] + '~=~' + gzahl(st_werte[rf[0]]) + 'cm'
            aufg1 = st[rf[1]] + '~=~' + gzahl(st_werte[rf[1]]) + 'cm'
        else:
            aufg1 = st[rf[0]] + '~=~' + gzahl(st_werte[rf[0]]) + 'cm'
            aufg2 = st[rf[1]] + '~=~' + gzahl(st_werte[rf[1]]) + 'cm'
        auswahl = ['Ssw', aufg1, aufg2, wk[rf[0]] + '~=~' + gzahl(wk_werte[rf[0]]) + r' ^{  \circ}']

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Von einem kongruenten Dreieck sind folgende Daten gegeben:']
    aufgabe.append(str(auswahl[1]) + ',~' + str(auswahl[2]) + r'~ \mathrm{und} ~'
                   + str(auswahl[3]) + r'.')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS eine Planskizze zeichnen, die gegebenen Größen markieren und den daraus folgenden Kongruenzsatz nennen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 3
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Fertige eine Planskizze an, markiere die gegebenen Größen und '
                                                'nenne den Kongruenzsatz. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + r' \mathrm{Planskizze} ~ (2BE), \quad \to \quad '
                       + str(auswahl[0]) + r' \quad (1BE)')
        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Hier sollen die SuS mithilfe der gegebenen Daten das Dreieck konstruieren.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        pkt = 5
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Konstruiere das Dreieck. \n\n')
        if 'a' not in teilaufg:
            loesung.extend((beschriftung(len(teilaufg), i, True) + r' \mathrm{Planskizze} ~ (2BE), \quad '
                            + str(auswahl[1]) + '~(1BE),~' + str(auswahl[2]) + '~(1BE),~'
                            + str(auswahl[3]) + r'~(1BE), \\ \mathrm{restl.~Seite(n)~und~Beschrift.} ~(2BE)',
                            'Figure'))
            pkt += 2
        else:
            loesung.extend((beschriftung(len(teilaufg), i, True) + str(auswahl[1])
                           + '~(1BE),~' + str(auswahl[2]) + '~(1BE),~' + str(auswahl[3])
                            + r'~(1BE), \\ \mathrm{restl.~Seite(n)~und~Beschrift.} ~(2BE)', 'Figure'))
        dreieck_zeichnen(pkt_list, pkt_bez, st, wk, f'Loesung_{nr}{liste_teilaufg[i]}')
        liste_punkte.append(pkt)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rechtwinkliges_dreieck(nr, teilaufg=['a', 'b'], gegeben=['zufällig','zwei Katheten', 'Kathete und Hypothenuse'][0], i=0, BE=[]):
    # Bei dieser Aufgaben sollen die SuS aus den gegebenen Daten eines Dreiecks die fehlende Seiten und Winkel mithilfe des Satz des Pythagoras und Sinus, Konsinus und Tnagens berechnen.
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Mit dem Parameter "gegeben=" kann festgelegt werden, welcher Seiten vom Dreieck gegeben sind. (0: zwei Katheten, 1: eine Kathete und eine Hypothenuse).
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    l_a = (m ** 2 - n ** 2) / 10
    l_b = 2 * m * n / 10
    l_c = (m ** 2 + n ** 2) / 10
    gamma = 90
    beta = round(math.degrees(math.asin(l_b / l_c)))
    alpha = gamma - beta
    auswahl = random.choice([[0, 1, 2], [0,2,1], []])
    st = [['a', 'b', 'c'][x] for x in auswahl]
    wk = [[r'\alpha', r'\beta', r'\gamma'][x] for x in auswahl]
    # die verschiedenen Aufgaben  ['a', 'b', 'c', r' \alpha ', r' \beta ', r' \gamma ']
    def kat_kat():
        auswahl = random.choice([[0, 1, 2], [0,2,1], [1,2,0]])
        st = [['a', 'b', 'c'][x] for x in auswahl]
        wk = [[r'\alpha', r'\beta', r'\gamma'][x] for x in auswahl]
        aufgabe_1 = (st[0] + '~=~' + gzahl(l_a) + r'cm,~' + st[1] + '~=~' + gzahl(l_b)
                     + r'cm, ~ \mathrm{und} ~' + wk[2] + r'~=~ 90^{  \circ} .')
        loesung_1 = (r'geg \colon  ~' + aufgabe_1 + 'ges: ~' + st[2] + r' \quad (1BE) \\'
                     + st[2] + '^2 ~=~' + st[0] + '^2 ~+~' + st[1] + r'^2 \quad \vert \sqrt{...} \quad \to \quad '
                     + st[2] + r'~=~ \sqrt{' + st[0] + r'^2 ~+~ ' + st[1] + r'^2 } ~=~ \sqrt{ ('
                     + gzahl(l_a) + r'cm)^2 ~+~ (' + gzahl(l_b) + r'cm)^2 } ~=~' + gzahl(l_c)
                     + r'cm \quad (3BE) \\ \mathrm{Planskizze} \quad (1BE)')
        return aufgabe_1, loesung_1, st, wk
    def kat_hyp():
        auswahl = random.choice([[0, 1, 2], [1,0,2], [2,0,1]])
        st = [['a', 'b', 'c'][x] for x in auswahl]
        wk = [[r'\alpha', r'\beta', r'\gamma'][x] for x in auswahl]
        aufgabe_2 = (st[1] + '~=~' + gzahl(l_b) + r'cm,~' + st[2] + '~=~' + gzahl(l_c) + r'cm, ~ \mathrm{und} ~'
                     + wk[2] + r'~=~ 90^{  \circ} .')
        loesung_2 = (r'geg \colon  ~' + aufgabe_2 + 'ges: ~' + st[0] + r' \quad (1BE) \\'
                     + st[2] + '^2 ~=~' + st[0] + '^2 ~+~' + st[1] + r'^2 \quad \vert -' + st[1]
                     + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + st[0] + r'~=~ \sqrt{' + st[2] + r'^2 ~-~ '
                     + st[1] + r'^2 } ~=~ \sqrt{ (' + gzahl(l_c) + r'cm)^2 ~-~ (' + gzahl(l_b) + r'cm)^2 } ~=~'
                     + gzahl(l_a) + r'cm \quad (3BE) \\' + r' \mathrm{Planskizze} \quad (1BE)')
        return aufgabe_2, loesung_2, st, wk
    def hyp_kat():
        auswahl = random.choice([[0, 1, 2], [1,0,2], [0,2,1]])
        st = [['a', 'b', 'c'][x] for x in auswahl]
        wk = [[r'\alpha', r'\beta', r'\gamma'][x] for x in auswahl]
        aufgabe_3 = (st[0] + '~=~' + gzahl(l_a) + r'cm,~' + st[2] + '~=~' + gzahl(l_c)
                     + r'cm, ~ \mathrm{und} ~' + wk[2] + r'~=~ 90^{  \circ} .')
        loesung_3 = (r'geg \colon  ~' + aufgabe_3 + r' ges \colon  ~' + st[1] + r' \quad (1BE) \\'
                     + st[2] + '^2 ~=~' + st[0] + '^2 ~+~' + st[1] + r'^2 \quad \vert -' + st[0]
                     + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + st[1] + r'~=~ \sqrt{' + st[2] + r'^2 ~-~ ' + st[0]
                     + r'^2 } ~=~ \sqrt{ (' + gzahl(l_c) + r'cm)^2 ~-~ (' + gzahl(l_a) + r'cm)^2 } ~=~'
                     + gzahl(l_b) + r'cm \quad (3BE) \\' + r' \mathrm{Planskizze} \quad (1BE)')
        return aufgabe_3, loesung_3, st, wk

    if gegeben == 'zufällig':
        auswahl = random.choice([kat_kat, kat_hyp, hyp_kat])()
    elif gegeben == 'zwei Katheten':
        auswahl = kat_kat()
    elif gegeben == 'Kathete und Hypothenuse':
        auswahl = random.choice([kat_hyp, hyp_kat])()

    st, wk = auswahl[2], auswahl[3]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Von einem rechtwinkligen Dreieck sind folgende Daten gegeben:', auswahl[0]]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS aus den gegebenen Daten die fehlende Seitenlänge im rechtw. Dreieck mit dem Satz von Pythagoras berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne die fehlende Seitenlänge im Dreieck ABC. '
                                                'Fertige dazu eine Planskizze an. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + auswahl[1])
        liste_punkte.append(5)
        i += 1

    if 'b' in teilaufg:
        # Mithilfe der Daten können die SuS die fehlenden Winkel im rechtwinkligen Dreieck mit Sinus, Kosinus und Tangens berechnen.
        if 'a' not in teilaufg:
            geg = (r' \mathrm{geg:~}' + st[0] + '~=~' + gzahl(l_a) + 'cm,~' + st[1] + '~=~' + gzahl(l_b) + 'cm,~'
                   + st[2] + '~=~' + gzahl(l_c) + r'cm ~ \mathrm{und} ~' + wk[2]
                   + r'~=~ 90^{  \circ} \quad \mathrm{ges:} ~' + wk[0] + ',~' + wk[1] + r' ~ (1BE) \\')
            punkte = 6
        else:
            geg = ''
            punkte = 5
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne die fehlenden Winkel des Dreiecks. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + geg + ' sin(' + wk[0] + r')~=~ \frac{' + st[0] + '}{'
                       + st[2] + r'} ~=~ \frac{' + gzahl(l_a) + 'cm}{' + gzahl(l_c)
                       + r'cm} \quad \vert ~ sin^{-1}() \quad \to \quad ' + wk[0]
                       + r'~=~ sin^{-1} \Big( \frac{' + gzahl(l_a) + '}{' + gzahl(l_c) + r'} \Big) ~=~' + gzahl(alpha)
                       + r' ^{ \circ} \quad (3BE) \\' + wk[1] + r'~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ '
                       + gzahl(alpha) + r'^{ \circ} ~=~ ' + gzahl(beta) + r'^{ \circ} \quad (2BE)')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def verhaeltnisgleichgungen(nr, teilaufg=['a', 'b'], auswahl_seite=[None, 0, 1][0], i=0, BE=[]):
    # Hier sollen die Schüler*innen mithilfe der gegebenen Daten eines rechtw. Dreieckes die Verhältnisgleichungen für den Sinus, Kosinus und Tangens aufstellen und die restlichen Größen berechnen.
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
    l_a = (m ** 2 - n ** 2) / 10
    l_b = 2 * m * n / 10
    l_c = (m ** 2 + n ** 2) / 10
    # hier werden die Winkel berechnet
    w_c = 90
    w_a = round(math.degrees(math.asin(l_a / l_c)))
    w_b = w_c - w_a
    # mithilfe der Seitenlänge werden die Punkte A, B und C im Koordinatensystem berechnet
    pkt = [[0, 0], [l_c, 0], [(l_b ** 2) / l_c, l_a * l_b / l_c]]
    auswahl_beschriftung = random.randint(0, 6)
    bezeichnungen = [
        {'Punkte': ['A', 'B', 'C'], 'Seiten': ['a', 'b', 'c'], 'Winkel': [r' \alpha ',r' \beta ',r'90^{ \circ }']},
        {'Punkte': ['D', 'E', 'F'], 'Seiten': ['d', 'e', 'f'], 'Winkel': [r' \delta ',r' \epsilon ',r'90^{ \circ }']},
        {'Punkte': ['G', 'K', 'L'], 'Seiten': ['g', 'k', 'l'], 'Winkel': [r' \zeta ',r' \eta ',r'90^{ \circ }']},
        {'Punkte': ['M', 'N', 'P'], 'Seiten': ['m', 'n', 'p'], 'Winkel': [r' \mu ',r' \nu ',r'90^{ \circ }']},
        {'Punkte': ['R', 'S', 'T'], 'Seiten': ['r', 's', 't'], 'Winkel': [r' \rho ',r' \sigma ',r'90^{ \circ }']},
        {'Punkte': ['U', 'V', 'W'], 'Seiten': ['u', 'v', 'w'], 'Winkel': [r' \upsilon ',r' \phi ',r'90^{ \circ }']},
        {'Punkte': ['X', 'Y', 'Z'], 'Seiten': ['x', 'y', 'z'], 'Winkel': [r' \chi ',r' \psi ',r'90^{ \circ }']}]


    pkt_bez = bezeichnungen[auswahl_beschriftung]['Punkte']
    st = bezeichnungen[auswahl_beschriftung]['Seiten']
    st_werte = [l_a,l_b,l_c]
    wk = bezeichnungen[auswahl_beschriftung]['Winkel']
    wk_werte = [w_a, w_b, w_c]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Die folgende Abbildung stellt ein rechtwinkliges Dreieck dar.', 'Figure']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'Loesung_{nr}']
    dreieck_zeichnen(pkt, pkt_bez, st, wk, f'Loesung_{nr}')
    grafiken_loesung = []

    p = random.choice([0, 1])
    p = 0 if auswahl_seite != None else p

    if 'a' in teilaufg:
        # Hier sollen die SuS die gegebenen Verhältnisgleichungen für sin, cos und tan vervollständigen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Vervollständige die folgenden Verhältnisgleichungen von Sinus, '
                       + 'Kosiuns und Tangens. \n')
        if p == 0:
            aufgabe.append(r' sin(' + wk[p] + r')~= \hspace{10em} cos(' + wk[p]
                           + r')~= \hspace{10em} tan(' + wk[p] + r')~= \hspace{10em} \\')
            loesungen = (r' \mathrm{sin(' + wk[0] + r')~=~ \frac{' + st[0] + '}{' + st[2]
                         + r'}, \quad cos(' + wk[0] + r')~=~ \frac{' + st[1] + '}{' + st[2]
                         + r'}, \quad tan(' + wk[0] + r')~=~ \frac{' + st[0] + '}{' + st[1] + '}}')
        else:
            aufgabe.append(r' sin(' + wk[p] + r')~= \hspace{10em} cos(' + wk[p]
                           + r')~= \hspace{10em} tan(' + wk[p] + r')~= \hspace{10em} \\')
            loesungen = (r' \mathrm{sin(' + wk[1] + r')~=~ \frac{' + st[1] + '}{' + st[2]
                         + r'}, \quad cos(' + wk[1] + r')~=~ \frac{' + st[0] + '}{' + st[2]
                         + r'}, \quad tan(' + wk[1] + r')~=~ \frac{' + st[1] + '}{' + st[0] + r'}}')

        loesung.append(beschriftung(len(teilaufg), i, True) + loesungen + r' \quad (3BE)')
        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # Hier sollen die Schüler*innen mithilfe der gegebenen Daten die restlichen Größen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        p = 0 if auswahl_seite != None else p
        auswahl_seite = random.randint(0,2) if auswahl_seite == None else auswahl_seite
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne die fehlenden Größen, '
                       + 'wenn außer dem rechten Winkel, noch folgende Werte gegeben sind.')
        aufgabe.append(wk[p] + '~=~' + gzahl(wk_werte[p]) + r'^{ \circ } \quad \mathrm{und} \quad ' + st[auswahl_seite]
                       + '~=~' + gzahl(st_werte[auswahl_seite]) + 'cm')
        if p == 0:
            if auswahl_seite == 0:
                lsg_1 = N(st_werte[auswahl_seite]/math.sin(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]/math.tan(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon ~'
                             + st[1] + ', ~' + st[2] + ', ~' + wk[1] + r' \quad (1BE) \\ sin(' + wk[p] + r')~=~ \frac{'
                             + st[auswahl_seite] + '}{' + st[2] + r'} \quad \vert ~ \cdot ' + st[2]
                             + r' ~ \vert ~ \div sin(' + wk[p] + r') \quad \to \quad ' + st[2]
                             + r'=~ \frac{' + st[auswahl_seite] + '}{ ~ sin(' + wk[p] + r')~ } ~=~ \frac{'
                             + gzahl(st_werte[auswahl_seite]) + ' cm ~}{~ sin(' + gzahl(wk_werte[p]) + r') ~} ~=~'
                             + gzahl(lsg_1) + r' cm \quad (3BE) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[auswahl_seite] + r'}{' + st[1] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[1] + r' ~ \vert ~ \div tan(' + wk[p]
                             + r') \quad \to \quad ' + st[1] +  r'=~ \frac{' + st[auswahl_seite] + r'}{ ~ tan('
                             + wk[p] + r')~ } ~=~ \frac{' + gzahl(st_werte[auswahl_seite]) + ' cm ~}{~ tan('
                             + gzahl(wk_werte[p]) + r') ~} ~=~' + gzahl(lsg_2) + r' cm \quad (3BE) \\')

            elif auswahl_seite == 1:
                lsg_1 = N(st_werte[auswahl_seite]/math.cos(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]*math.tan(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon  ~'
                             + st[0] + ', ~' + st[2] + ', ~' + wk[1] + r' \quad (1BE) \\ cos(' + wk[p] + r')~=~ \frac{'
                             + st[auswahl_seite] + '}{' + st[2] + r'} \quad \vert ~ \cdot ' + st[2]
                             + r' ~ \vert ~ \div cos(' + wk[p] + ')' + r' \quad \to \quad ' + st[2] + r'=~ \frac{'
                             + st[auswahl_seite] + '}{ ~ cos(' + wk[p] + r')~ } ~=~ \frac{'
                             + gzahl(st_werte[auswahl_seite]) + 'cm~ }{~ cos(' + gzahl(wk_werte[p]) + r') ~} ~=~'
                             + gzahl(lsg_1) + r'cm \quad (3BE) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[0] + r'}{' + st[auswahl_seite] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[0]
                             + '=~' + st[auswahl_seite] + r' \cdot tan(' + wk[p] + r')~ ~=~'
                             + gzahl(st_werte[auswahl_seite]) + r' cm \cdot ~ tan(' + gzahl(wk_werte[p]) + r') ~=~'
                             + gzahl(lsg_2) + r' cm \quad (3BE) \\')
            else:
                lsg_1 = N(st_werte[auswahl_seite]*math.sin(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]*math.cos(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon  ~'
                             + st[0] + ', ~' + st[1] + ', ~' + wk[1] + r' \quad (1BE) \\ sin(' + wk[p] + r')~=~ \frac{' + st[0]
                             + '}{' + st[auswahl_seite] + r'} \quad \vert ~ \cdot ' + st[auswahl_seite]
                             + r' \quad \to \quad ' + st[0] + r'=~ sin(' + wk[p] + r') ~ \cdot ~' + st[auswahl_seite]
                             + r'~=~ sin(' + gzahl(wk_werte[p]) + r') ~ \cdot ~' + gzahl(st_werte[auswahl_seite])
                             + 'cm~=~' + gzahl(lsg_1) + r'cm \quad (3BE) \\'

                             + ' cos(' + wk[p] + r')~=~ \frac{' + st[1] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad '
                             + st[1] + '=~' + st[auswahl_seite] + r' ~ \cdot ~ cos('
                             + wk[p] + r')~=~ ' + gzahl(st_werte[auswahl_seite]) + r'cm~ \cdot ~ cos('
                             + gzahl(wk_werte[p]) + r') ~=~' + gzahl(lsg_2) + r'cm \quad (2BE) \\')

            loesung.append(str(liste_teilaufg[i]) + (r') \quad ' + loesung_1)
                           + wk[1] + r'~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ ' + gzahl(wk_werte[p]) + r'^{ \circ} ~=~ '
                           + gzahl(wk_werte[1]) + r'^{ \circ} \quad (3BE)')
        else:
            if auswahl_seite == 0:
                lsg_1 = N(st_werte[auswahl_seite]/math.cos(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]*math.tan(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon  ~'
                             + st[1] + ', ~' + st[2] + ', ~' + wk[0] + r' \quad (1BE) \\ cos(' + wk[p] + r')~=~ \frac{'
                             + st[auswahl_seite] + '}{' + st[2] + r'} \quad \vert ~ \cdot ' + st[2]
                             + r' ~ \vert ~ \div cos(' + wk[p] + r') \quad \to \quad ' + st[2] + r'=~ \frac{'
                             + st[auswahl_seite] + '}{ ~ cos(' + wk[p] + r')~ } ~=~ \frac{'
                             + gzahl(st_werte[auswahl_seite]) + 'cm~ }{~ cos(' + gzahl(wk_werte[p]) + r') ~} ~=~'
                             + gzahl(lsg_1) + r'cm \quad (3BE) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[1] + r'}{' + st[auswahl_seite] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[1]
                             + '=~' + st[auswahl_seite] + r' \cdot tan(' + wk[p] + r')~ ~=~'
                             + gzahl(st_werte[auswahl_seite]) + r' cm \cdot ~ tan(' + gzahl(wk_werte[p]) + r') ~=~'
                             + gzahl(lsg_2) + r' cm \quad (3BE) \\')

            elif auswahl_seite == 1:
                lsg_1 = N(st_werte[auswahl_seite]/math.sin(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]/math.tan(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon  ~'
                             + st[0] + ', ~' + st[2] + ', ~' + wk[0] + r' \quad (1BE) \\ sin(' + wk[p] + r')~=~ \frac{'
                             + st[auswahl_seite] + '}{' + st[2] + r'} \quad \vert ~ \cdot ' + st[2]
                             + r' \vert \div sin(' + wk[p] + r') \quad \to \quad ' + st[2] + r'~=~ \frac{'
                             + st[auswahl_seite] + '}{ ~ sin(' + wk[p] + r')~ } ~=~ \frac{'
                             + gzahl(st_werte[auswahl_seite]) + 'cm~ }{~ sin(' + gzahl(wk_werte[p]) + r') ~} ~=~'
                             + gzahl(lsg_1) + r'cm \quad (3BE) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[auswahl_seite] + r'}{' + st[0] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[0] + r' \vert \div tan(' + wk[p] + r')'
                             + r' \quad \to \quad ' + st[0] + r'=~ \frac{' + st[auswahl_seite]
                             + '}{ ~ tan(' + wk[p] + r')~ } ~=~ \frac{' + gzahl(st_werte[auswahl_seite])
                             + 'cm~ }{~ tan(' + gzahl(wk_werte[p]) + r') ~} ~=~'
                             + gzahl(lsg_2) + r'cm \quad (3BE) \\')
            else:
                lsg_1 = N(st_werte[auswahl_seite]*math.sin(wk_werte[p]*pi/180),2)
                lsg_2 = N(st_werte[auswahl_seite]*math.cos(wk_werte[p]*pi/180),2)
                loesung_1 = (r'geg \colon ' + wk[p] + '~=~' + gzahl(wk_werte[p]) + r' ^{ \circ } \quad \mathrm{und} \quad '
                             + st[auswahl_seite] + '~=~' + gzahl(st_werte[auswahl_seite]) + r' cm \quad ges \colon  ~'
                             + st[0] + ', ~' + st[1] + ', ~' + wk[0] + r' \quad (1BE) \\ sin(' + wk[p] + r')~=~ \frac{' + st[1]
                             + '}{' + st[auswahl_seite] + r'} \quad \vert ~ \cdot ' + st[auswahl_seite]
                             + r' \quad \to \quad ' + st[1] + r'=~ sin(' + wk[p] + r') ~ \cdot ~' + st[auswahl_seite]
                             + r'~=~ sin(' + gzahl(wk_werte[p]) + r') ~ \cdot ~' + gzahl(st_werte[auswahl_seite])
                             + 'cm~=~' + gzahl(lsg_1) + r'cm \quad (3BE) \\'

                             + ' cos(' + wk[p] + r')~=~ \frac{' + st[0] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad '
                             + st[0] + '=~' + st[auswahl_seite] + r' ~ \cdot ~ cos('
                             + wk[p] + r')~=~ ' + gzahl(st_werte[auswahl_seite]) + r'cm~ \cdot ~ cos('
                             + gzahl(wk_werte[p]) + r') ~=~' + gzahl(lsg_2) + r'cm \quad (3BE) \\')

            loesung.append(beschriftung(len(teilaufg), i, True) + loesung_1
                           + wk[0] + r'~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ ' + gzahl(wk_werte[p]) + r'^{ \circ} ~=~ '
                           + gzahl(wk_werte[0]) + r'^{ \circ} \quad (2BE)')
        liste_punkte.append(9)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der '
                  f'Anzahl der Teilaufgaben ({len(teilaufg)}) überein. '
                  f'Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_wetterballon(nr, teilaufg=['a', 'b'], BE=[]):
    # Hier sollen die Schüler*innen den Sichtwinkel und den Abstand eines Beobachters von einem Wetterballon berechnen (Trigonometrie im rechtw. Dreieck).
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []
    i = 0

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
    abstand_beob_warte = (m ** 2 - n ** 2) / 10
    hoehe = 2 * m * n / 10
    abstand_beob_ballon = (m ** 2 + n ** 2) / 10
    # hier werden die Winkel berechnet
    w_warte = 90
    w_beob = round(math.degrees(math.atan(hoehe / abstand_beob_warte)))
    w_b = w_warte - w_beob

    if 'a' not in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
                   f'Bei einer Wetterwarte steigt ein Wetterballon senkrecht auf.'
                   f' Wenn der Ballon eine Höhe von {hoehe}km erreicht hat, '
                   f'sieht ein Beobachter den Ballon unter einem Winkel von {w_beob}°. \n\n']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
                   f'Bei einer Wetterwarte steigt ein Wetterballon senkrecht auf.'
                   f' Ein Beobachter befindet sich {abstand_beob_warte}km von der Wetterwarte entfernt '
                   f'und der Ballon hat eine Höhe von {hoehe}km erreicht. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen den Sichtwinkel berechnen, unter dem der Wetterballon gesehen werden kann.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne den Winkel, unter dem der Beobachter'
                                                f' den Ballon sieht. Fertige eine Planskizze an. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \mathrm{Lösung~Planskizze~(1BE)} \quad \mathrm{geg:~a~=~'
                       + str(hoehe) + 'km,~c~=~' + str(abstand_beob_warte)
                       + r'km, \quad ges \colon  \alpha \quad (1BE)} \\'
                       + r' tan( \alpha ) ~=~ \frac{a}{c} \quad \vert tan^{-1}()'
                       + r'\quad \to \quad \alpha ~=~ tan^{-1} \Big( \frac{a}{c} \Big) ~=~'
                       + r' tan^{-1} \Big( \frac{' + str(hoehe) + 'km }{'
                       + str(abstand_beob_warte) + r'km } \Big) ~=~' + str(w_beob)
                       + r' ^{ \circ} \quad (3BE)')
        liste_punkte.append(5)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen den Abstand des Beobachters vom Wetterballon berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne den Abstand des Ballons vom Beobachter. \n\n')
        if 'a' in teilaufg:
            loesung.append(beschriftung(len(teilaufg), i, True) + r' sin( \alpha ) ~=~ \frac{a}{b} \quad \vert \cdot '
                           + r'b \quad \vert \div sin( \alpha ) \quad \to \quad b ~=~ '
                           + r'\frac{a}{ sin( \alpha )} ~=~ \frac{' + str(hoehe) + r'km }{ sin( ' + str(w_beob)
                           + r' ^{ \circ}  )} ~=~' + str(abstand_beob_ballon) + r'km  \quad (3BE)')
            pkt = 3
        else:
            loesung.append(beschriftung(len(teilaufg), i, True) + r' \mathrm{geg:~ \alpha ~=~' + str(w_beob)
                           + r' ^{ \circ},~a~=~' + str(hoehe) + r'km, \quad ges \colon b \quad (1BE)} \\'
                           + r' sin( \alpha ) ~=~ \frac{a}{b} \quad \vert \cdot b \quad \vert \div sin( \alpha ) '
                           + r' \quad \to \quad b ~=~ \frac{a}{ sin( \alpha )} \frac{' + str(hoehe) + r'km }{ sin( '
                           + str(w_beob) + r' ^{ \circ}  )} ~=~' + str(abstand_beob_ballon) + r'km  \quad (3BE)')
            pkt = 4
        liste_punkte.append(pkt)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der '
                  f'Anzahl der Teilaufgaben ({len(teilaufg)}) überein. '
                  f'Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_klappleiter(nr, teilaufg=['a', 'b'], BE=[]):
    # Hier sollen die Schüler*innen den Anstellwinkel einer Klappleiter berechnen und beurteilen, ob dieser sicher aufgestellt werden kann (Trigonometrie im rechtw. Dreieck).
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []
    i = 0

    laenge_leiter = nzahl(23,50)/10
    deckenhoehe = round(laenge_leiter * (1-nzahl(5,15)/100),2)
    # hier werden die Winkel berechnet
    anstellwinkel = round(math.degrees(math.asin(deckenhoehe / laenge_leiter)),3)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               f'Ein Dachboden ist über eine {laenge_leiter}m lange Klappleiter erreichbar. '
               + f'Die Höhe vom Boden zum Dachboden beträgt {deckenhoehe}m. '
               + 'Die Leiter ist gut zu begehen, wenn der Anstellwinkel der Leiter mit dem Fußboden '
               + 'mindestens einen Winkel von 61° beträgt. \n',
               'Fertige dazu eine Planskizze an. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen den Anstellwinkel einer Klappleiter berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne den Anstellwinkel der Leiter mit dem Dachboden. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \mathrm{Lösung~Planskizze~(2BE)} \quad \mathrm{geg:~a~=~'
                       + latex(deckenhoehe) + 'm,~b~=~' + latex(laenge_leiter)
                       + r'm, \quad ges \colon  \alpha \quad (1BE)} '
                       + r' sin( \alpha ) ~=~ \frac{a}{b} \quad \vert sin^{-1}()'
                       + r'\quad \to \quad \alpha ~=~ sin^{-1} \Big( \frac{a}{b} \Big) ~=~'
                       + r' sin^{-1} \Big( \frac{' + latex(deckenhoehe) + 'm }{'
                       + latex(laenge_leiter) + r'm } \Big) ~=~' + latex(anstellwinkel) + r' ^{ \circ} \quad (3BE) \\')
        liste_punkte.append(6)
        i += 1

    if 'a' and 'b' in teilaufg:
        # Die SuS sollen beurteilen, ob die Dachleiter sicher aufgestellt werden kann.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i]) + f') Beurteile, ob der Dachboden mit der Dachleiter gut zu begehen ist.')
        if anstellwinkel <= 61:
            loesung.append(beschriftung(len(teilaufg), i, True)
                           + r' \mathrm{Der~Anstellwinkel~ist~kleiner~als~61°~und~somit~der~'
                           + r'Dachboden~nicht~gut~zu~begehen. \quad (1BE)}')
        else:
            loesung.append(beschriftung(len(teilaufg), i, True)
                           + r' \mathrm{Der~Anstellwinkel~ist~größer~als~61°~und~somit~der~'
                           + r' Dachboden~gut~zu~begehen. \quad (1BE)}')
        liste_punkte.append(1)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der '
                  f'Anzahl der Teilaufgaben ({len(teilaufg)}) überein. '
                  f'Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_turm(nr, koerpergroesse=[True, False][0], BE=[]):
    # Hier sollen die Schüler*innen die Höhe eines Turms berechnen (Trigonometrie im rechtw. Dreieck).
    # Mit dem Paramter "koerpergroesse=True" wird festgelegt, ob die Körpergröße des Beobachters in der Aufgabe berücksichtigt werden soll bzw. diese in der Aufgabenstellung genannt wird.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    i = 0

    n = random.randint(2, 5)
    m = n + random.randint(2, 5)

    # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
    abstand_beob_turm = (m ** 2 - n ** 2)
    hoehe = 2 * m * n
    abstand_beob_spitze = (m ** 2 + n ** 2)

    # hier werden die Winkel berechnet
    w_warte = 90
    w_beob = round(math.degrees(math.atan(hoehe / abstand_beob_turm)))
    w_b = w_warte - w_beob

    if koerpergroesse == True:
        hoehe_beob = random.choice(range(16,21))/10
        hoehe_beob_str = latex(N(hoehe_beob,1)) + 'm großer'
        lsg_0 = (r' \quad \to \quad h ~=~' + gzahl(hoehe) + 'm' + vorz_str(hoehe_beob) + 'm ~=~'
                 + gzahl(N(hoehe+hoehe_beob),1))
        punkte = 4
    else:
        lsg_0 = hoehe_beob_str = ''
        punkte = 3


    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               f'Ein {hoehe_beob_str} Betrachter steht {abstand_beob_turm}m entfernt von einem Turm '
               f'und sieht unter einem Winkel von {w_beob}° die Spitze des Turms. \n',
               'Berechne aus den gegebenen Werte die Höhe des Turms.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    loesung.append(r' \mathrm{geg:~ \alpha ~=~' + gzahl(w_beob) + r' ^{ \circ},~c~=~' + gzahl(abstand_beob_turm)
                   + r'm, \quad ges \colon  a \quad (1BE)} \\ tan( \alpha ) ~=~ \frac{a}{b}'
                   + r' \quad \vert \cdot b \quad \to \quad a ~=~ b \cdot tan( \alpha )'
                   + ' ~=~' + gzahl(abstand_beob_turm) + r'm \cdot tan(' + gzahl(w_beob) + r' ^{ \circ}  ) ~=~'
                   + gzahl(hoehe) + lsg_0 + r'm  \quad (4BE)')
    grafiken_aufgaben = []
    grafiken_loesung = []

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_rampe(nr, BE=[]):
    # Hier sollen die Schüler*innen die Länge einer Rampe berechnen, damit diese gut befahrbar ist (Trigonometrie im rechtw. Dreieck).
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    i = 0
    hoehe = nzahl(30,60)
    tiefe_rampe = hoehe + nzahl(30, 120)
    # hier werden die Winkel berechnet
    w_haus = 90
    w_rampe = round(math.degrees(math.atan(hoehe / tiefe_rampe)))
    w_haus = w_haus - w_rampe
    laenge_rampe = N(hoehe/math.sin(math.radians(w_rampe)),4)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               f'Eine Rollstuhlrampe in einem öffentlichen Gebäude soll eine Höhe von {hoehe}cm überwinden. '
               f'Der Steigungswinkel darf höchstens {w_rampe}° betragen. '
               f'Wie lang muss die Strecke sein, auf der der Rollstuhl nach unten fährt? \n'
               'Fertige dazu eine Planskizze an.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    loesung.append(r' \mathrm{Planskizze \quad (1BE) \quad \to \quad geg:~ \alpha ~=~' + str(w_rampe)
                   + r'^{ \circ},~a ~=~' + str(hoehe) + r'cm, \quad ges \colon  b \quad (1BE)} \\ sin( \alpha ) ~=~'
                   + r'\frac{a}{b} \quad \vert \cdot b \quad \vert \div sin( \alpha ) \quad \to \quad b '
                   + r'~=~ \frac{a}{ sin( \alpha )} ~=~ \frac{' + str(hoehe) + r'cm }{ sin( ' + str(w_rampe)
                   + r' ^{ \circ}  )} ~=~' + str(laenge_rampe) + r'cm  \quad (3BE)')
    grafiken_aufgaben = []
    grafiken_loesung = []

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [5]
        liste_punkte = BE
    else:
        liste_punkte = [5]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def berechnungen_allg_dreieck(nr, teilaufg=['a', 'b', 'c'], i=0, BE=[]):
    # Berechnungen im allgemeinen Dreieck
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    def werte_bel_dreieck():
        alpha = random.choice([nzahl(60, 85), nzahl(95,120)])
        seite_a = nzahl(6, 12)
        seite_b = seite_a * nzahl(4, 8) / 10
        beta = round(math.degrees(math.asin(math.sin(math.radians(alpha)) * seite_b / seite_a)))
        gamma = 180 - alpha - beta
        seite_c = round(seite_a * math.sin(math.radians(gamma)) / math.sin(math.radians(alpha)), 1)

        auswahl = random.sample([0, 1, 2], 3)
        auswahl_liste = {'Seite_bez' : [['a', 'b', 'c'][x] for x in auswahl],
                         'Seite_wert' : [seite_a, seite_b, seite_c],
                         'Winkel_bez' : [[r' \alpha ', r' \beta ', r' \gamma '][x] for x in auswahl],
                         'Winkel_wert' : [alpha, beta, gamma]}

        return auswahl_liste

    auswahl_liste = werte_bel_dreieck()
    seite_1, seite_wert_1, winkel_1, winkel_wert_1 = [element[0] for element in auswahl_liste.values()]
    seite_2, seite_wert_2, winkel_2, winkel_wert_2 = [element[1] for element in auswahl_liste.values()]
    seite_3, seite_wert_3, winkel_3, winkel_wert_3 = [element[2] for element in auswahl_liste.values()]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Von einem allgemeinen Dreieck, sind folgende Daten gegeben: ',
               seite_1 + '~ = ~' + gzahl(seite_wert_1) + r'cm, \quad '
               + seite_2 + '~ = ~' + gzahl(seite_wert_2) + r'cm, \quad '
               + winkel_1 + '~ = ~' + gzahl(winkel_wert_1) + r' ^{ \circ } \quad ']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    grafiken_aufgaben = []
    grafiken_loesung = []
    if len([element for element in ['a', 'b', 'c'] if element in teilaufg]) > 0:
        ges_a =  winkel_2 + ',~' + winkel_3
    if len([element for element in ['b', 'c'] if element in teilaufg]) > 0:
        ges_b =  ',~' + seite_3
    if 'c' in teilaufg:
        ges_c = ',~ A'
    gegeben_und_gesucht = (r' \mathrm{geg:~} ' + seite_1 + '~=~' + gzahl(seite_wert_1)
                           + r'cm, \quad ' + seite_2 + '~=~' + gzahl(seite_wert_2) + r'cm, \quad ' + winkel_1
                           + '~=~' + latex(winkel_wert_1) + r'^{ \circ } \quad \mathrm{ges \colon ~}'
                           + ges_a + ges_b + ges_c + r' \quad (1BE) \quad \mathrm{aus~der~Planskizze~(1BE)~folgt:~} \\')

    if len([element for element in ['a', 'b', 'c'] if element in teilaufg]) > 0:
        # Berechnung der Winkel im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 8
        aufgabe.append(beschriftung(len(teilaufg), i)+ 'Berechne die restlichen Winkel im Dreieck. '
                       + 'Fertige dazu eine Planskizze an. \n\n')
        loesung.append(gegeben_und_gesucht + beschriftung(len(teilaufg), i, True) + r' \frac{' + seite_2
                       + '}{~sin(' + winkel_2 + ')} ~=~' + r' \frac{' + seite_1 + '}{~sin(' + winkel_1
                       + r')} \quad \to \quad \frac{~sin(' + winkel_2 + ')}{ ' + seite_2 + r'} ~=~ \frac{ sin('
                       + winkel_1 + r') }{' + seite_1 + r'} \quad \vert \cdot ' + seite_2 + r' \quad (1BE) \\'
                       + 'sin(' + winkel_2 + r') ~=~ \frac{ sin(' + winkel_1 + r')}{' + seite_1
                       + r'} \cdot ' + seite_2 + r' \quad \vert ~ sin^{ -1}() \quad \to \quad '
                       + winkel_2 + r' ~=~ sin^{ -1} \left( \frac{ sin(' + winkel_1 + r')}{'
                       + seite_1 + r'} \cdot ' + seite_2 + r'\right) \quad (1BE) \\'
                       + winkel_2 + r' ~=~ sin^{ -1} \left( \frac{sin(' + gzahl(winkel_wert_1) + r'^{ \circ } )}{'
                       + gzahl(seite_wert_1) + r'cm} \cdot ' + gzahl(seite_wert_2) + r'cm \right) ~=~'
                       + gzahl(winkel_wert_2) + r'^{ \circ } \quad (2BE) \\' + winkel_3 + r'~=~ 180^{ \circ} ~-~'
                       + gzahl(winkel_wert_1) + r'^{ \circ} ~-~ ' + gzahl(winkel_wert_2) + r'^{ \circ} ~=~ '
                       + gzahl(winkel_wert_3) + r'^{ \circ} \quad (2BE) \\')
        liste_punkte.append(pkt)
        i += 1

    if len([element for element in ['b', 'c'] if element in teilaufg]) > 0:
        # Berechnung der fehlenden Seitenlänge im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 4
        aufgabe.append(beschriftung(len(teilaufg), i)
                       + 'Berechne die Länge der Seite {seite_3} mit dem Sinussatz. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \mathrm{aus~der~Planskizze~folgt:~} \hspace{15em} \\'
                       + r' \frac{' + seite_1 + '}{~sin(' + winkel_1 + ')} ~=~' + r' \frac{' + seite_3 + '}{~sin('
                       + winkel_3 + r')} \quad \vert \cdot sin(' + winkel_3 + r') \quad \to \quad ' + seite_3
                       + r'~=~ \frac{' + seite_1 + r' \cdot sin(' + winkel_3 + ') }{ sin(' + winkel_1
                       + r') } \quad (2BE) \\' + seite_3 + r'~=~ \frac{' + gzahl(seite_wert_1) + r'cm \cdot sin('
                       + gzahl(winkel_wert_3) + r' ^{ \circ } )}{ sin(' + gzahl(winkel_wert_1) + r' ^{ \circ } )} ~=~'
                       + gzahl(seite_wert_3) + r'cm \quad (2BE) \\')
        liste_punkte.append(pkt)
        i += 1

    if 'c' in teilaufg:
        # Berechnung der Fläche im allg. Dreieck

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 3
        flaeche = 0.5*seite_wert_1*seite_wert_2*math.sin(math.radians(winkel_wert_3))
        # print(N(flaeche,3))
        aufgabe.append(beschriftung(len(teilaufg), i) + 'Berechne die Fläche des Dreiecks. \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + r' A ~ = ~ \frac{1}{2} \cdot ' + seite_1
                       + r' \cdot ' + seite_2
                       + r' \cdot sin(' + winkel_3 + r') ~=~ \frac{1}{2} \cdot ' + gzahl(seite_wert_1) + r'cm \cdot '
                       + gzahl(seite_wert_2) + r'cm \cdot sin(' + latex(winkel_wert_3) + r'^{ \circ } ) ~=~ '
                       + gzahl(N(flaeche,3)) + r'cm^2 \quad (3BE) \\'
                       + r' \mathrm{insgesamt~' + str(pkt) + r'~Punkte} \\')
        liste_punkte.append(pkt)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def pruefung_kl10_allg_dr_01(nr, teilaufg=['a', 'b', 'c', 'd'], pruef_kl10=[False,True][0], neue_seite=[None, 0, 1, 2, 3][0], i=0, BE=[]):
    # das ist eine orginale Aufgabe der Abschlussprüfung Klasse 10 in Brandenburg zur Trigonometrie
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Ist der Parameter "pruef_kl10=True" dann wird unter der Teilaufgabe ein Notizfeld für die Berechnungen angezeigt. Standardmäßig ist "pruef_kl10=False" und es wird kein Notizfeld unter der Teilaufgabe angezeigt.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt kein erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    seite_a = nzahl(6, 12)
    seite_h = seite_a*nzahl(4,8)/10
    seite_FB = N(sqrt(seite_a**2-seite_h**2),3)
    beta = N(math.degrees(math.asin(seite_h / seite_a)),3)
    gamma_1 = nzahl(20,40)
    alpha = 90 - gamma_1
    seite_b = N(seite_a * math.sin(math.radians(beta)) / math.sin(math.radians(alpha)), 3)
    gamma = 180 - alpha - beta
    flaeche = N(0.5*seite_a*seite_b*math.sin(math.radians(gamma)),3)
    seite_c = N(seite_a * math.sin(math.radians(gamma)) / math.sin(math.radians(alpha)), 3)
    xwert_punkt_c = seite_c - seite_FB
    ywert_punkt_c = seite_h

    # Listen für die Zeichung des Dreiecks
    pkt_list = [[0, 0], [seite_c, 0], [xwert_punkt_c, ywert_punkt_c],[xwert_punkt_c,0]]
    pkt_bez = ['A', 'B', 'C', 'F']
    st = ['a', 'b', '', 'h']
    st_werte = [seite_a, seite_b, seite_c, seite_h]
    wk = [r' \alpha ', r' \beta ', r' \gamma_1 ',  r' ^{ \circ}']
    wk_werte = [alpha, beta, gamma_1, 90]
    dreieck_zeichnen_mit_hoehe(pkt_list, pkt_bez, st, wk, f'{str(nr)}')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
                NoEscape('Im abgebildeten allgemeinen Dreieck ist $ h = '
                         + gzahl(seite_h) + '$cm, $a = ' + gzahl(seite_a) + r'$cm und $ \gamma_1 = '
                         + gzahl(gamma_1) + r'^{ \circ}$.'), ['Grafik', '250px']]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'{str(nr)}']
    grafiken_loesung = []

    if len([element for element in ['a', 'b', 'c', 'd'] if element in teilaufg]) > 0:
        ges_a =  r' \overline{FB} '
    if len([element for element in ['b', 'c', 'd'] if element in teilaufg]) > 0:
        ges_b =  r',~ \alpha ,~ \beta '
    if len([element for element in [ 'c', 'd'] if element in teilaufg]) > 0:
        ges_c = ',~ b'
    if 'd' in teilaufg:
        ges_d = ',~ A'
    gegeben_und_gesucht = (r' \mathrm{geg: \quad a~=~' + gzahl(seite_a) + r'cm,~ h~=~'
                           + gzahl(seite_h) + r'cm \quad und  \gamma_1 = ' + gzahl(gamma_1)
                           + r'^{ \circ} \quad ges \colon  \quad ' + ges_a + ges_b + ges_c + ges_d
                           + r' \quad (1BE) \quad aus~der~Skizze~folgt:} \\')


    if len([element for element in ['a', 'b', 'c', 'd'] if element in teilaufg]) > 0:
        # Berechnung des Hypotenusenabschnittes mit Pythagoras
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                + ') Berechnen Sie die Länge der Strecke ' + r'$ \overline{FB} $.'))
        loesung.append(gegeben_und_gesucht + str(liste_teilaufg[i])
                       + r') \quad h^2~+~ \overline{FB}^2~=~a^2 \quad \vert ~- h^2'
                       + r' \quad \to \quad \overline{FB}^2~=~a^2~-~h^2 \quad \vert \sqrt{}'
                       + r' \quad \to \quad \overline{FB}~=~ \sqrt{a^2~-~h^2} \quad (2BE) \\'
                       + r' \overline{FB} ~=~ \sqrt{(' + gzahl(seite_a) + 'cm)^2 - ('
                       + gzahl(seite_h) + 'cm)^2 } ~=~' + gzahl(seite_FB) + r'cm \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(5) + r'~Punkte} \\')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(5)
        i += 1

    if len([element for element in ['b', 'c', 'd'] if element in teilaufg]) > 0:
        # Berechnung eines Winkels mit dem Sinus
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + 'Berechnen Sie die Größe der Winkel '
                                + r'$ \alpha $' + ' und ' + r'$ \beta $.'))
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \quad \alpha ~=~180^{ \circ } - 90^{ \circ } - \gamma_1 '
                       + r' ~=~180^{ \circ } - 90^{ \circ } -' + gzahl(gamma_1) + r'^{ \circ} ~=~' + gzahl(alpha)
                       + r'^{ \circ} \quad (2BE) \\ sin( \beta ) ~=~ \frac{h}{a} \quad \vert sin^{-1}() \quad '
                       + r' \to \quad \beta ~=~ sin^{-1} \Big( \frac{h}{a} \Big) ~=~ sin^{-1} \Big( \frac{'
                       + gzahl(seite_h) + '}{' + gzahl(seite_a) + r'} \Big) ~=~ ' + gzahl(beta)
                       + r'^{ \circ} \quad (4BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(6)
        i += 1

    if len([element for element in ['c', 'd'] if element in teilaufg]) > 0:
        # Berechnung einer Seite mit dem Sinussatz
        stern = r'$ ^{ \star } $' if pruef_kl10 else ''
        liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))
        aufgabe.append(NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i])
                                + ') Berechnen Sie die Länge der Seite b.'))
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \frac{a}{sin( \alpha)} ~=~ \frac{b}{sin( \beta)}'
                       + r' \quad \vert \cdot sin( \beta) \quad \to \quad b~=~'
                       + r' \frac{a \cdot sin( \beta )}{sin( \alpha )} ~=~ \frac{' + gzahl(seite_a) + r'cm \cdot sin('
                       + gzahl(beta) + r'^{ \circ})}' + r'{sin(' + gzahl(alpha) + r'^{ \circ})} ~=~' + gzahl(seite_b)
                       + r'cm \quad (4BE) \\')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(4)
        i += 1

    if 'd' in teilaufg:
        # Berechnung der Fläche des Dreiecks
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                + 'Berechnen Sie die Fläche des Dreiecks ABC.'))
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' \gamma ~=~180^{ \circ } - \alpha - \beta ~=~ 180^{ \circ } - ' + gzahl(alpha)
                       + r'^{ \circ } - ' + gzahl(beta) + r'^{ \circ } ~=~' + str(gamma) + r'^{ \circ} \quad (2BE) \\'
                       + r' A ~=~ \frac{1}{2} \cdot a \cdot b \cdot sin( \gamma ) ~=~ \frac{1}{2} \cdot '
                       + gzahl(seite_a) + r'cm \cdot ' + gzahl(seite_b) + r'cm \cdot sin(' + gzahl(gamma)
                       + r'^{ \circ }) ~=~' + gzahl(flaeche) + r'cm^2 \quad (3BE) \\')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(5)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_vermessung_see(nr, BE=[]):
    # Berechnungen der Länge eines Sees mit dem Kosinussatz
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    i = 0
    beta = nzahl(30,60)
    seite_c = nzahl(6, 12)
    seite_a = seite_c * nzahl(6, 9) / 10
    seite_b = N(sqrt(seite_c**2 + seite_a**2 - 2*seite_c*seite_a*math.cos(math.radians(beta))),3)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Um die Länge eines Sees zu vermessen, wurden mit einem Theodoliten die Entfernung zu den äußeren '
               f'Ufern mit a = {gzahl(seite_a)}km und c = {gzahl(seite_c)}km und der eingeschlossen Winkel von '
               f'{gzahl(beta)}° bestimmt. Berechnen Sie die Länge des Sees.', 'Bild',
               'Die Skizze der Vermessung des Sees ist nicht maßstabsgerecht \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\',
               r' \mathrm{Planskizze \quad (1BE) \quad \to \quad geg  \colon ~ a ~=~' + gzahl(seite_a)
               + r' km, ~ c ~=~' + gzahl(seite_c) + r'km \quad \mathrm{und} \quad \beta ~=~' + gzahl(beta)
               + r' ^{ \circ} \quad ges \colon  b \quad (1BE)} \\ b ~=~ \sqrt{a^2 + c^2 - 2ac \cdot cos( \beta ) }'
               + r' ~=~ \sqrt{ (' + gzahl(seite_a) + 'km) ^2 + (' + gzahl(seite_c) + r'km)^2 - 2 ~ \cdot'
               + gzahl(seite_a) + r'km \cdot ' + gzahl(seite_c) + r'km \cdot cos(' + gzahl(beta) + r'^{ \circ} )} ~=~'
               + gzahl(seite_b) + r'km  \quad (3BE)']
    grafiken_aufgaben = ['vermessung_see']
    grafiken_loesung = []

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [5]
        liste_punkte = BE
    else:
        liste_punkte = [5]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sachaufgabe_strassenbau(nr, BE=[]):
    # Berechnungen der Länge einer neu gebauten Straße mit dem Sinussatz
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    i = 0
    gamma = nzahl(95,120)
    beta = nzahl(15,45)
    seite_c = nzahl(6, 12)
    seite_b = N(seite_c * math.sin(math.radians(beta)) / math.sin(math.radians(gamma)), 2)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),NoEscape(
               f'Um ein Wohngebiet zu erschließen, wird der Bau einer neuen Straße geplant. Die neue Straße soll in '
               r'einem Winkel $ \gamma = $ '+ f' {gzahl(gamma)}° an die Eichenallee anschließen und der '
               f'Straßenabschnitt der Hauptstraße, zwischen der geplanten Straße und der Eichenallee, soll '
               f'{gzahl(seite_c)}km lang sein. \n Berechnen Sie die Länge der geplanten neuen Straße, '
               r'wenn der Winkel $ \beta $ ' + f'zwischen der Eichenallee und der Hauptstraße {gzahl(beta)}° beträgt.'),
               'Bild', 'Skizze des geplanten Bauprojekt ist nicht maßstabsgerecht \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\',
               r' \mathrm{Planskizze \quad (1BE) \quad \to \quad geg  \colon ~ c~=~' + gzahl(seite_c)
               + r' km, ~ \beta ~=~' + gzahl(beta) + r' ^{ \circ} \quad \mathrm{und} \quad \gamma ~=~' + gzahl(gamma)
               + r' ^{ \circ} \quad ges \colon  b \quad (1BE)} \\ \quad \mathrm{aus~der~Planskizze~folgt:~} '
               + r' \hspace{15em} \\ \frac{b}{ sin( \beta )} ~=~ \frac{c}{ sin( \gamma )} '
               + r' \quad \vert \cdot sin( \beta ) \quad \to \quad b~=~ \frac{ c \cdot sin( \beta ) }{ sin( \gamma )} '
               + r'\quad (2BE) \\ b ~=~ \frac{' + gzahl(seite_c) + r'km \cdot sin(' + gzahl(beta)
               + r' ^{ \circ } )}{ sin(' + gzahl(gamma) + r' ^{ \circ } )} ~=~' + gzahl(seite_b) + r'km \quad (2BE) \\']
    grafiken_aufgaben = ['strassenbau']
    grafiken_loesung = []
    pkt = 6

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [pkt]
        liste_punkte = BE
    else:
        liste_punkte = [pkt]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Flächen und Körperberechnung
def pool(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], pruef_kl10=[False,True][0], neue_seite=[None, 0, 1, 2, 3, 4][0], i=0, BE=[]):
    # das ist eine Aufgabe der Abschlussprüfung Klasse 10 in Brandenburg zur Flächen und Volumenberechung
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Ist der Parameter "pruef_kl10=True" dann wird unter der Teilaufgabe ein Notizfeld für die Berechnungen angezeigt. Standardmäßig ist "pruef_kl10=False" und es wird kein Notizfeld unter der Teilaufgabe angezeigt.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt kein erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    laenge = nzahl(2,5) * 5
    radius = laenge * nzahl(3,4)/10
    anz_bahnen = 1

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Familie Geiss plant auf ihrem Anwesen an der '
               + f'Côte d’Azur den Bau eines Swimmingpools. \n Dieser soll eine Länge von {gzahl(laenge+2*radius)}m und eine '
               + f'Breite von {gzahl(2*radius)}m haben.',
               ['Grafik','300px']]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    def pool_zeichnen(anz_bahnen, laenge, radius, bez_laenge='', bez_radius=''):
        fig, ax = plt.subplots()
        fig.canvas.draw()
        fig.tight_layout()
        ax.set_aspect(1)
        bahnen = []
        for step in range(0, anz_bahnen + 1):
            theta_1 = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
            theta_2 = np.linspace(np.pi / 2, - np.pi / 2, 100)
            kurve_l = (radius * (1 + step * 0.2) * np.cos(theta_1), radius * (1 + step * 0.2) * np.sin(theta_1))
            bahn_u = ([0, laenge], [-radius * (1 + step * 0.2), -radius * (1 + step * 0.2)])
            bahn_o = ([0, laenge], [radius * (1 + step * 0.2), radius * (1 + step * 0.2)])
            kurve_r = (
                radius * (1 + step * 0.2) * np.cos(theta_2) + laenge, radius * (1 + step * 0.2) * np.sin(theta_2))
            bahnen.extend((kurve_l, bahn_u, bahn_o, kurve_r))

        for element in bahnen:
            plt.plot(element[0], element[1], 'k')


        # Doppelseitige Pfeile für Länge und Breite
        plt.annotate('', xy=(-radius, 0), xytext=(laenge + radius, 0),
                     arrowprops=dict(arrowstyle='<->', lw=1.5))
        plt.annotate('Länge: ' + bez_laenge + 'm', xy=(radius,0.2), xytext=(radius, 0.2),
                     ha='center', va='bottom')
        plt.annotate('', xy=(laenge, -radius), xytext=(laenge, radius),
                     arrowprops=dict(arrowstyle='<->', lw=1.5))
        plt.annotate('Breite: ' + bez_radius + 'm', xy=(laenge*0.95, radius / 2), xytext=(laenge*0.95, radius / 2),
                     ha='left', va='center', rotation=90)
        plt.text(radius,radius+0.2,'Abflussrinne', )

        # Achsen ausschalten
        ax.axis('off')

        plt.savefig('img/temp/pool', dpi=200, bbox_inches='tight', pad_inches=0)
        plt.close('all')
        plt.clf()

    pool_zeichnen(anz_bahnen, laenge, radius, gzahl(laenge+2*radius), gzahl(2*radius) )

    grafiken_aufgaben = ['pool']
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS die geoemtrischen Formen erkennen, aus denen sich der Pool zusammensetzt.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 2
        aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + 'Geben Sie an, aus welchen Teilflächen '
                                + 'sich die Grundfläche des Pools zusammensetzt.'))
        loesung.append(beschriftung(len(teilaufg), i, True) + r' \mathrm{Aus~zwei~Halbkreisen~links~und~rechts~und~einem~'
                       + r'Rechteck~in~der~Mitte.} \quad (2BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_klein')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Hier sollen die SuS den Umfang des Pools berechnen
        liste_bez.append(NoEscape(f'{str(nr)}.{str(liste_teilaufg[i])})'))
        pkt = 5
        aufgabe.extend((NoEscape(r' \noindent Am Rand des Pools soll das beim Baden übergelaufene Wasser in eine '
                                + r'Abflussrinne laufen. Die Gitter für die Abdeckung der Rinne sind 50cm lang.'),
                                ' \n\n', beschriftung(len(teilaufg), i) + 'Berechnen Sie, wie viele Gitter für den Pool '
                                + 'benötigt werden.'))
        loesung.append(beschriftung(len(teilaufg), i, True)
                       + r' U_{ges} ~=~ U_{Kreis} + 2 \cdot (Länge - Breite) ~=~ '
                       + r' \pi \cdot Breite + 2 \left( ' + vorz_v_aussen(laenge + 2 * radius, 'm ')
                       + vorz_v_innen(2*radius, 'm') + r' \right) ~=~ \pi \cdot ' + gzahl(2*radius)
                       + r' m + 2 \cdot ' + gzahl(laenge) + r'm ~=~' + gzahl(N(2*pi*radius + 2*laenge,3))
                       + r'm \quad (4BE) \\ \mathrm{Es~sind~' + gzahl(int(4*(pi*radius + laenge)) + 1)
                       + r'~Gitter~für~die~Abdeckung~notwendig.} \quad (1BE) ')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_gross')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(pkt)
        i += 1

    if 'c' in teilaufg:
        # Hier sollen die SuS die Grundfläche des Pools berechnen
        liste_bez.append(NoEscape(f'{str(nr)}.{str(liste_teilaufg[i])})'))
        pkt = 3
        flaeche = N(laenge*2*radius + pi*radius**2,2)
        aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + 'Berechnen Sie die Größe der Grundfläche '
                                 + 'des Pools.'))
        loesung.append(beschriftung(len(teilaufg), i, True) + r' A_{ges} ~=~ A_{Rechteck} + A_{Kreis} ~=~ '
                       + r' ( Länge - Breite ) \cdot Breite + \pi \cdot r^2 \quad (1BE) \\ \hspace{15em} \left( '
                       + vorz_v_aussen(laenge + 2*radius, 'm') + vorz_v_innen(-2*radius, 'm')
                       + r' \right) \cdot ' + gzahl(2*radius) + r' + \pi \cdot \left( ' + gzahl(radius)
                       + r'm \right) ^2  ~=~ ' + gzahl(flaeche) + r'm^2 \quad (2BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(pkt)
        i += 1


        if 'd' in teilaufg:
            # Hier sollen die SuS das Wasservolumen des Pools berechnen
            stern = r'$ ^{ \star } $' if pruef_kl10 else ''
            hoehe_pool = nzahl(22, 30) / 10
            volumen = N((laenge * 2 * radius + pi * radius ** 2) * hoehe_pool, 2)
            pkt = 3
            liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))
            aufgabe.extend((NoEscape(r' \noindent Damit Herr Geiss einen Kopfsprung in den Pool machen kann, '
                                     f'soll dieser {gzahl(hoehe_pool)}m tief sein.'),' \n\n',
                            NoEscape(r' \noindent ' + stern + beschriftung(len(teilaufg), i)
                                     + 'Berechnen Sie die Wassermenge des Pools in $ m^3 $.')))
            loesung.append(beschriftung(len(teilaufg), i, True) + r' V ~=~ A \cdot h ~=~ ' + gzahl(flaeche)
                           + r'm^2 \cdot ' + gzahl(hoehe_pool) + 'm ~=~' + gzahl(volumen) +  r'm^3 \\')
            if pruef_kl10:
                aufgabe.append(['Bild', '430px'])
                grafiken_aufgaben.append('notizen_klein')
            else:
                aufgabe.append(' \n\n')
            aufgabe.append('NewPage') if neue_seite == i else ''
            liste_punkte.append(pkt)
            i += 1


            if 'e' in teilaufg:
                # Berechnung die Zeit zum Befüllen des Pools mit einem Gartenschlauch
                menge_schlauch = nzahl(6,13) * 100
                zeit = N(volumen/(menge_schlauch/1000),3)
                stern = r'$ ^{ \star } $' if pruef_kl10 else ''
                pkt = 3
                liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))
                aufgabe.extend((NoEscape(r' \noindent Herr Geiss ist ungeduldig und möchte für die Befüllung des Pool '
                                         + f'einen Gartenschlauch nutzen. Mit diesem kann er den Pool mit '
                                         + f'{gzahl(menge_schlauch)}l Wasser pro Stunde befüllen.'),' \n\n',
                                NoEscape(r' \noindent ' + stern + beschriftung(len(teilaufg), i)
                                         + 'Berechne Sie, wie lange es dauert den Pool so zu befüllen .')))
                loesung.append(beschriftung(len(teilaufg), i, True) + r' t ~=~ \frac{' + gzahl(volumen) + 'm^3 }{'
                               + gzahl(menge_schlauch/1000) + r' \frac{m^3}{h} } ~=~ ' + gzahl(zeit)
                               + r'h \quad (3BE) ')
                if pruef_kl10:
                    aufgabe.append(['Bild', '430px'])
                    grafiken_aufgaben.append('notizen_klein')
                else:
                    aufgabe.append(' \n\n')
                aufgabe.append('NewPage') if neue_seite == i else ''
                liste_punkte.append(pkt)
                i += 1

    liste_punkte = BE if len(BE) == len(teilaufg) else liste_punkte
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def prisma(nr, teilaufg=['a', 'b'], pruef_kl10=[False,True][0], neue_seite=[None, 0, 1][0], i=0, BE=[]):
    # hier sollen die Schüler*innen
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Ist der Parameter "pruef_kl10=True" dann wird unter der Teilaufgabe ein Notizfeld für die Berechnungen angezeigt. Standardmäßig ist "pruef_kl10=False" und es wird kein Notizfeld unter der Teilaufgabe angezeigt.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt kein erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    a = nzahl(5,10)
    h = a * nzahl(10,20)/5
    hg = round(sqrt(3)/2*a,1)

    dreiseitiges_prisma = (([0,a,a/2,0],[0,0,sqrt(3)/2*a,0], 'k'),
                           ([a+h*np.cos(30/180*np.pi),a/2 + h*np.cos(30/180*np.pi)],
                            [h*np.sin(30/180*np.pi), sqrt(3)/2*a+h*np.sin(30/180*np.pi)], 'k'),
                           ([a / 2 + h * np.cos(30 / 180 * np.pi), h * np.cos(30 / 180 * np.pi),
                             a + h * np.cos(30 / 180 * np.pi)],
                            [sqrt(3) / 2 * a + h * np.sin(30 / 180 * np.pi), h * np.sin(30 / 180 * np.pi),
                             h * np.sin(30 / 180 * np.pi)], '--'),
                           ([0,h*np.cos(30/180*np.pi)],[0,h*np.sin(30/180*np.pi)], '--'),
                           ([a,a+h*np.cos(30/180*np.pi)],[0,h*np.sin(30/180*np.pi)], 'k'),
                           ([a/2,a/2 + h*np.cos(30/180*np.pi)],[sqrt(3)/2*a,sqrt(3)/2*a + h*np.sin(30/180*np.pi)], 'k'),
                           ([a/2,a/2], [0,sqrt(3)/2*a], 'gray'))
    beschriftung_dr = ([a*0.3, - 0.5, f'{a}cm'],
                    [a + h*np.cos(30/180*np.pi)/2, h*np.sin(30/180*np.pi)/2 - 0.5, f'{h} cm'], [a/2+0.2,0.4*a, f'$ h_g $'])
    auswahl = random.choice([0])
    ausw_bez = ['regelmäßiges dreiseitiges'][auswahl]
    ausw_krp = [dreiseitiges_prisma]
    flaeche_zeichnen(*ausw_krp[auswahl], text=beschriftung_dr, name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               NoEscape(f'Gegeben ist ein {ausw_bez} Prisma mit den Kantenlängen a = {a} cm, der Höhe des Prismas '
                        + r' \\' + f'h = {h} cm und der Höhe in der Grundfläche mit ' + r'$ h_g $' + f' = {hg}cm.'),
               ['Grafik','150px']]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    grafiken_aufgaben = [f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})']
    grafiken_loesung = []

    if len([element for element in ['a', 'b'] if element in teilaufg]) > 0:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + 'Berechne die Oberfläche des Prismas.'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_klein')
        else:
            aufgabe.append(' \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + r' A_G ~=~ \frac{1}{2} \cdot a \cdot h_a ~=~ \frac{1}{2} \cdot '
                       + gzahl(a) + r'cm \cdot ' + gzahl(hg) + ' cm ~=~ ' + gzahl(round(0.5*a*hg,1))
                       + r'cm^2 \quad \mathrm{und} \quad A_M ~=~ 3 \cdot a \cdot b ~=~ 3 \cdot ' + gzahl(a) + r' cm\cdot '
                       + gzahl(h) + 'cm ~=~' + gzahl(3*a*h) + r'cm^2 \\ \mathrm{Die~Oberfläche~A_O~beträgt~dann:} '
                       + r' \quad A_O ~=~ 2 \cdot A_G + A_M ~=~ 2 \cdot' + gzahl(round(0.5*a*hg,1)) + 'cm^2'
                       + vorz_str(3*a*h) + 'cm^2 ~=~' + gzahl(round(a*hg + 3*a*h,1)) + r'cm^2')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(6)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + r') Berechne das Volumen des Prismas.'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_klein')
        else:
            aufgabe.append(' \n\n')
        loesung.append(beschriftung(len(teilaufg), i, True) + r' V ~=~ A_g \cdot h ~=~ ' + gzahl(round(0.5*a*hg,1))
                       + r'cm^2 \cdot ' + gzahl(h) + r'cm ~=~ ' + gzahl(round(0.5*a*hg*h,1)) + r' cm^3 ')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(2)
        i += 1
    liste_punkte = BE if len(BE) == len(teilaufg) else liste_punkte
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]