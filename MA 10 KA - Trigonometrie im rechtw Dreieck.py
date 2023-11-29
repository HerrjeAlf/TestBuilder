import pylatex, math, random, sympy, numpy, matplotlib
from random import randrange, randint, choice
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from flaechen_konstruieren import dreieck_zeichnen

# Definition der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
fig = plt.Figure()


def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k


def nzahl(p, q):
    k = random.randint(p, q)
    return k


def vorz_str(k):
    if k < 0:
        k = latex(k)
    else:
        k = '+' + latex(k)
    return k


def vorz_str_minus(k):
    if k < 0:
        k = '(' + latex(k) + ')'
    else:
        k = latex(k)
    return k


# Berechnung für die Aufgaben
def kongruente_Dreiecke(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    l_a = (m ** 2 - n ** 2) / 10
    l_b = 2 * m * n / 10
    l_c = (m ** 2 + n ** 2) / 10
    gamma = 90
    beta = int(math.degrees(math.asin(l_b / l_c)))
    alpha = gamma - beta

    pkt_bez = ['A', 'B', 'C']
    st = ['a', 'b', 'c']
    st_werte = [l_a,l_b,l_c]
    wk = [r'\alpha', r'\beta', r'90^{ \circ}' ]
    wk_werte = [alpha,beta,gamma]
    pkt = [[0, 0], [l_c, 0], [(l_b ** 2) / l_c, l_a * l_b / l_c]]

    name = 'Aufgabe_' + str(nr)
    grafik = 'Aufgabe_' + str(nr) + '.png'

    auswahl = random.choice([['sss', 'a~=~' + str(l_a) + 'cm', 'b~=~' + str(l_b) + 'cm', 'c~=~' + str(l_c) + 'cm'],
                             ['sws', 'a~=~' + str(l_a) + 'cm', 'b~=~' + str(l_b) + 'cm',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['sws', 'b~=~' + str(l_b) + 'cm', 'c~=~' + str(l_c) + 'cm',
                              r' \alpha ~=~' + str(alpha) + r' ^{  \circ}'],
                             ['sws', 'c~=~' + str(l_c) + 'cm', 'a~=~' + str(l_a) + 'cm',
                              r' \beta ~=~' + str(beta) + r' ^{  \circ}'],
                             ['wsw', 'a~=~' + str(l_a) + 'cm', r' \beta ~=~' + str(beta) + r' ^{  \circ}',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['wsw', 'b~=~' + str(l_b) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}',
                              r' \gamma ~=~ ' + str(gamma) + r' ^{  \circ}'],
                             ['wsw', 'c~=~' + str(l_c) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}',
                              r' \beta ~=~ ' + str(beta) + r' ^{  \circ}'],
                             ['sww', 'b~=~' + str(l_b) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}',
                              r' \beta ~=~' + str(beta) + r' ^{  \circ}'],
                             ['sww', 'c~=~' + str(l_c) + 'cm', r' \beta ~=~' + str(beta) + r' ^{  \circ}',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['sww', 'a~=~' + str(l_a) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['Ssw', 'b~=~' + str(l_b) + 'cm', ' c ~=~' + str(l_c) + 'cm',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['Ssw', 'a~=~' + str(l_a) + 'cm', ' c ~=~' + str(l_c) + 'cm',
                              r' \gamma ~=~' + str(gamma) + r' ^{  \circ}']])

    # print('a = ' + str(a))
    # print('a = ' + str(a))
    # print('b = ' + str(b))
    # print('c = ' + str(c))
    # print('gamma = ' + str(gamma))
    # print('beta = ' + str(beta))
    # print('alpha = ' + str(alpha))
    print(auswahl)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Von einem kongruenten Dreieck sind folgende Daten gegeben:']
    aufgabe.append(str(auswahl[1]) + ',~' + str(auswahl[2]) + r'~ \mathrm{und} ~' + str(auswahl[3]) + r'.')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Nenne den Kongruenzsatz, nachdem das Dreieck kongruent ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + str(auswahl[0]) + r' \quad (1P) ~')
        Punkte += 1
        i += 1
    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Konstruiere das Dreieck mithilfe der gegebenen Daten. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Planskizze} ~ (2P), \quad ' + str(auswahl[1])
                       + '~(1P),~' + str(auswahl[2]) + '~(1P),~' + str(auswahl[3])
                       + r'~(1P), \\ \mathrm{restl.~Seite(n)~und~Beschrift.} ~(2P)')
        loesung.append('Abbildung')
        dreieck_zeichnen(pkt, pkt_bez, st, wk, name)
        plt.figure().clear()
        Punkte += 7
        i += 1
    return aufgabe, loesung, Punkte, grafik


def rechtwinkliges_dreieck(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    s_1 = (m ** 2 - n ** 2) / 10
    s_2 = 2 * m * n / 10
    s_3 = (m ** 2 + n ** 2) / 10
    print(s_1)
    print(s_2)
    print(s_3)
    w_3 = 90
    w_2 = int(math.degrees(math.asin(s_2 / s_3)))
    w_1 = w_3 - w_2

    auswahl = random.choice([['a', 'b', 'c', r' \alpha ', r' \beta ', r' \gamma '],
                             ['a', 'c', 'b', r' \alpha ', r' \gamma ', r' \beta '],
                             ['b', 'a', 'c', r' \beta ', r' \alpha ', r' \gamma '],
                             ['b', 'c', 'a', r' \beta ', r' \gamma ', r' \alpha '],
                             ['c', 'a', 'b', r' \gamma ', r' \alpha ', r' \beta '],
                             ['c', 'b', 'a', r' \gamma ', r' \beta ', r' \alpha ']])
    print(auswahl)
    if random.random() < 0.33:
        aufgabe_1 = (str(auswahl[0]) + '~=~' + str(s_1) + r'cm,~' + str(auswahl[1])
                     + '~=~' + str(s_2) + r'cm, ~ \mathrm{und} ~' + str(auswahl[5])
                     + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + str(auswahl[2])
                     + r'~=~ \sqrt{ (' + str(s_1) + r'cm)^2 ~+~ (' + str(s_2) + r'cm)^2 } ~=~'
                     + str(s_3) + r'cm \quad (3P) \\' + r' \mathrm{Planskizze} \quad (2P)')
    elif random.random() < 0.66:
        aufgabe_1 = (str(auswahl[1]) + '~=~' + str(s_2) + r'cm,~' + str(auswahl[2])
                     + '~=~' + str(s_3) + r'cm, ~ \mathrm{und} ~' + str(auswahl[5])
                     + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert -' + str(auswahl[1]) + r'^2 \quad \vert \sqrt{...} \quad \to \quad '
                     + str(auswahl[0]) + r'~=~ \sqrt{ (' + str(s_3) + r'cm)^2 ~-~ ('
                     + str(s_2) + r'cm)^2 } ~=~' + str(s_1) + r'cm \quad (3P) \\'
                     + r' \mathrm{Planskizze} \quad (2P)')
    else:
        aufgabe_1 = (str(auswahl[0]) + '~=~' + str(s_1) + r'cm,~' + str(auswahl[2])
                     + '~=~' + str(s_3) + r'cm, ~ \mathrm{und} ~' + str(auswahl[5])
                     + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert -' + str(auswahl[0]) + r'^2 \quad \vert \sqrt{...} \quad \to \quad '
                     + str(auswahl[1]) + r'~=~ \sqrt{ (' + str(s_3) + r'cm)^2 ~-~ ('
                     + str(s_1) + r'cm)^2 } ~=~' + str(s_2)
                     + r'cm \quad (3P) \\' + r' \mathrm{Planskizze} \quad (2P)')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Von einem rechtwinkligen Dreieck sind folgende Daten gegeben:']
    aufgabe.append(aufgabe_1)
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die fehlende Seitenlänge im Dreieck ABC. '
                                                'Fertige dazu eine Planskizze an. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + loesung_1)
        Punkte += 5
        i += 1

    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die fehlenden Winkel des Dreiecks. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{geg:~}' + str(auswahl[0]) + '~=~' + str(s_1)
                                                + 'cm,~' + str(auswahl[1]) + '~=~' + str(s_2) + 'cm,~'
                                                + str(auswahl[2]) + '~=~' + str(s_3) + r'cm ~ \mathrm{und} ~'
                                                + str(auswahl[5]) + '~=~' + str(w_3)
                                                + r' ^{  \circ} \quad \mathrm{ges:} ~' + str(auswahl[3])
                                                + ',~' + str(auswahl[4]) + r' ~ (1P) \\'
                       + r' sin(' + str(auswahl[3]) + r')~=~ \frac{' + str(auswahl[0]) + '}{' + str(auswahl[2])
                       + r'} ~=~ \frac{' + str(s_1) + '}{' + str(s_3)
                       + r'} \quad \vert ~ sin^{-1}() \quad \to \quad' + str(auswahl[3])
                       + r'~=~ sin^{-1} \Big( \frac{' + str(s_1) + '}{' + str(s_3) + r'} \Big) ~=~' + str(w_1)
                       + r' ^{ \circ} \quad (3P) \\' + str(auswahl[4]) + '~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ '
                       + str(w_1) + r'^{ \circ} ~=~ ' + str(w_2) + r'^{ \circ} \quad (2P)')
        Punkte += 5
        i += 1

    return aufgabe, loesung, Punkte


def verhaeltnisgleichgungen(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
    l_a = (m ** 2 - n ** 2) / 10
    l_b = 2 * m * n / 10
    l_c = (m ** 2 + n ** 2) / 10
    # hier werden die Winkel berechnet
    w_c = 90
    w_a = int(math.degrees(math.asin(l_a / l_c)))
    w_b = w_c - w_a
    # mithilfe der Seitenlänge werden die Punkte A, B und C im Koordinatensystem berechnet
    pkt = [[0, 0], [l_c, 0], [(l_b ** 2) / l_c, l_a * l_b / l_c]]
    print('Aufgabe 3 - Länge Seite a: ' + str(l_a))
    print('Aufgabe 3 - Länge Seite b: ' + str(l_b))
    print('Aufgabe 3 - Länge Seite c: ' + str(l_c))
    auswahl_beschriftung = random.randint(0, 6)
    bezeichnungen = [
        {'Punkte' : ['A', 'B', 'C'] ,'Seiten' : ['a', 'b', 'c'], 'Winkel' : [r'\alpha',r'\beta',r'90^{ \circ}']},
        {'Punkte' : ['D', 'E', 'F'] ,'Seiten' : ['d', 'e', 'f'], 'Winkel' : [r'\delta',r'\epsilon',r'90^{ \circ}']},
        {'Punkte' : ['G', 'K', 'L'] ,'Seiten' : ['g', 'k', 'l'], 'Winkel' : [r'\zeta',r'\eta',r'90^{ \circ}']},
        {'Punkte' : ['M', 'N', 'P'] ,'Seiten' : ['m', 'n', 'p'], 'Winkel' : [r'\mu',r'\nu',r'90^{ \circ}']},
        {'Punkte' : ['R', 'S', 'T'] ,'Seiten' : ['r', 's', 't'], 'Winkel' : [r'\rho',r'\sigma',r'90^{ \circ}']},
        {'Punkte' : ['U', 'V', 'W'] ,'Seiten' : ['u', 'v', 'w'], 'Winkel' : [r'\upsilon',r'\phi',r'90^{ \circ}']},
        {'Punkte' : ['X', 'Y', 'Z'] ,'Seiten' : ['x', 'y', 'z'], 'Winkel' : [r'\chi',r'\psi',r'90^{ \circ}']}]


    pkt_bez = bezeichnungen[auswahl_beschriftung]['Punkte']
    st = bezeichnungen[auswahl_beschriftung]['Seiten']
    st_werte = [l_a,l_b,l_c]
    wk = [r'\alpha', r'\beta', r'90^{ \circ}']
    wk_werte = [w_a, w_b, w_c]

    name = 'Aufgabe_' + str(nr)
    grafik = 'Aufgabe_' + str(nr) + '.png'
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               'Die folgende Abbildung stellt ein rechtwinkliges Dreieck dar.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    p = random.choice([0, 1])

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Vervollständige die folgenden Verhältnisgleichungen von Sinus, Kosiuns und Tangens. \n')
        dreieck_zeichnen(pkt, pkt_bez, st, wk, name)
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

        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + loesungen + r' \quad (3P)')

        Punkte += 3
        i += 1

    if b in teilaufg:
        auswahl_seite = random.randint(0,2)
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die fehlenden Größen, wenn außer dem rechten Winkel noch folgendes gegeben ist:')
        aufgabe.append(wk[p] + '~=~' + latex(wk_werte[p]) + r' ^{ \circ } ~, \quad ' + st[auswahl_seite] + '~=~'
                       + latex(st_werte[auswahl_seite]) + r' cm \\')
        if p == 0:
            if auswahl_seite == 0:
                loesung_1 = (' sin(' + wk[p] + r')~=~ \frac{' + st[auswahl_seite] + '}{' + st[2] + '}'
                             + r' \quad \vert ~ \cdot ' + st[2] + r' ~ \vert ~ \div sin(' + wk[p] + ')'
                             + r' \quad \to \quad ' + st[2]   + r'=~ \frac{' + st[auswahl_seite] + '}{ ~ sin('
                             + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite]) + ' cm ~}{~ sin('
                             + str(wk_werte[p]) + r') ~} ~=~' + str(st_werte[2]) + r' cm \quad (2P) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[auswahl_seite] + r'}{' + st[1] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[1] + r' ~ \vert ~ \div tan(' + wk[p]
                             + r') \quad \to \quad ' + st[1] +  r'=~ \frac{' + st[auswahl_seite] + r'}{ ~ tan('
                             + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite]) + ' cm ~}{~ tan('
                             + str(wk_werte[p]) + r') ~} ~=~' + str(st_werte[1]) + r' cm \quad (2P) \\')

            elif auswahl_seite == 1:
                loesung_1 = (' cos(' + wk[p] + r')~=~ \frac{' + st[auswahl_seite] + '}{' + st[2] + '}'
                             + r' \quad \vert ~ \cdot ' + st[2] + r' ~ \vert ~ \div cos(' + wk[p] + ')'
                             + r' \quad \to \quad ' + st[2] + r'=~ \frac{' + st[auswahl_seite] + '}{ ~ cos('
                             + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite]) + 'cm~ }{~ cos('
                             + str(wk_werte[p]) + r') ~} ~=~' + str(st_werte[2]) + r'cm \quad (2P) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[0] + r'}{' + st[auswahl_seite] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[0]
                             + '=~' + st[auswahl_seite] + r' \cdot tan(' + wk[p] + r')~ ~=~'
                             + str(st_werte[auswahl_seite]) + r' cm \cdot ~ tan(' + str(wk_werte[p]) + r') ~=~'
                             + str(st_werte[0]) + r' cm \quad (2P) \\')
            else:
                loesung_1 = (' sin(' + wk[p] + r')~=~ \frac{' + st[0] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[0]
                             + r'=~ sin(' + wk[p] + r') ~ \cdot ~' + st[auswahl_seite] + '~=~'
                             + r'=~ sin(' + str(wk_werte[p]) + r') ~ \cdot ~' + str(st_werte[auswahl_seite])
                             + 'cm~=~' + str(st_werte[0]) + r'cm \quad (2P) \\'

                             + ' cos(' + wk[p] + r')~=~ \frac{' + st[1] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad '
                             + st[1] + '=~' + st[auswahl_seite] + r' ~ \cdot ~ cos('
                             + wk[p] + r')~=~ ' + str(st_werte[auswahl_seite]) + r'cm~ \cdot ~ cos('
                             + str(wk_werte[p]) + r') ~=~' + str(st_werte[1]) + r'cm \quad (2P) \\')

            loesung.append(str(liste_teilaufg[i]) + (r') \quad' + loesung_1)
                + wk[1] + '~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ ' + str(wk_werte[p]) + r'^{ \circ} ~=~ '
                + str(wk_werte[1]) + r'^{ \circ} \quad (2P)')
        else:
            if auswahl_seite == 0:
                loesung_1 = (' cos(' + wk[p] + r')~=~ \frac{' + st[auswahl_seite] + '}{' + st[2] + '}'
                             + r' \quad \vert ~ \cdot ' + st[2] + r' ~ \vert ~ \div cos(' + wk[p] + ')'
                             + r' \quad \to \quad ' + st[2] + r'=~ \frac{' + st[auswahl_seite] + '}{ ~ cos('
                             + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite]) + 'cm~ }{~ cos('
                             + str(wk_werte[p]) + r') ~} ~=~' + str(st_werte[2]) + r'cm \quad (2P) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[1] + r'}{' + st[auswahl_seite] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[1]
                             + '=~' + st[auswahl_seite] + r' \cdot tan(' + wk[p] + r')~ ~=~'
                             + str(st_werte[auswahl_seite]) + r' cm \cdot ~ tan(' + str(wk_werte[p]) + r') ~=~'
                             + str(st_werte[1]) + r' cm \quad (2P) \\')

            elif auswahl_seite == 1:
                loesung_1 = (' sin(' + wk[p] + r')~=~ \frac{' + st[auswahl_seite] + '}{' + st[2] + '}'
                             + r' \quad \vert ~ \cdot ' + st[2] + r' \vert \div sin(' + wk[p] + r')'
                             + r' \quad \to \quad ' + st[2] + r'~=~ \frac{' + st[auswahl_seite] + '}{ ~ sin('
                             + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite]) + 'cm~ }{~ sin('
                             + str(wk_werte[p]) + r') ~} ~=~' + str(st_werte[2]) + r'cm \quad (2P) \\'

                             + ' tan(' + wk[p] + r') ~=~ \frac{' + st[auswahl_seite] + r'}{' + st[0] + r'}'
                             + r' \quad \vert ~ \cdot ' + st[0] + r' \vert \div tan(' + wk[p] + r')'
                             + r' \quad \to \quad ' + st[0] + r'=~ \frac{' + st[auswahl_seite]
                             + '}{ ~ tan(' + wk[p] + r')~ } ~=~ \frac{' + str(st_werte[auswahl_seite])
                             + 'cm~ }{~ tan(' + str(wk_werte[p]) + r') ~} ~=~'
                             + str(st_werte[0]) + r'cm \quad (2P) \\')
            else:
                loesung_1 = (' sin(' + wk[p] + r')~=~ \frac{' + st[1] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad ' + st[1]
                             + r'=~ sin(' + wk[p] + r') ~ \cdot ~' + st[auswahl_seite]
                             + r'~=~ sin(' + str(wk_werte[p]) + r') ~ \cdot ~' + str(st_werte[auswahl_seite])
                             + 'cm~=~' + str(st_werte[1]) + r'cm \quad (2P) \\'

                             + ' cos(' + wk[p] + r')~=~ \frac{' + st[0] + '}{' + st[auswahl_seite] + '}'
                             + r' \quad \vert ~ \cdot ' + st[auswahl_seite] + r' \quad \to \quad '
                             + st[0] + '=~' + st[auswahl_seite] + r' ~ \cdot ~ cos('
                             + wk[p] + r')~=~ ' + str(st_werte[auswahl_seite]) + r'cm~ \cdot ~ cos('
                             + str(wk_werte[p]) + r') ~=~' + str(st_werte[0]) + r'cm \quad (2P) \\')

            loesung.append(str(liste_teilaufg[i]) + (r') \quad' + loesung_1)
                           + wk[0] + '~=~180^{ \circ} ~-~ 90^{ \circ} ~-~ ' + str(wk_werte[p]) + r'^{ \circ} ~=~ '
                           + str(wk_werte[0]) + r'^{ \circ} \quad (2P)')

        Punkte += 6
        i += 1

    return aufgabe, loesung, Punkte, grafik

def sachaufgabe_01(nr, teilaufg):
    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
    abstand_beob_warte = (m ** 2 - n ** 2) / 10
    hoehe = 2 * m * n / 10
    abstand_beob_ballon = (m ** 2 + n ** 2) / 10
    # hier werden die Winkel berechnet
    w_warte = 90
    w_beob = int(math.degrees(math.atan(hoehe / abstand_beob_warte)))
    w_b = w_warte - w_beob
    i = 0
    Punkte = 0
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               f'In einer Wetterwarte steigt ein Wetterballon senkrecht auf.'
               f' Ein Beobachter befindet sich {abstand_beob_warte}km von der Wetterwarte entfernt und der Ballon hat eine Höhe von {hoehe}km erreicht. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Winkel, unter dem der Beobachter'
                                                f' den Ballon sieht. Fertige eine Planskizze an. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Lösung~Planskizze~(2P)} \quad \mathrm{geg:~a~=~'
                                                 + str(hoehe) + 'km,~c~=~' + str(abstand_beob_warte)
                                                 + r'km, \quad ges: \alpha \quad (1P)} \\'
                                                 + r' tan( \alpha ) ~=~ \frac{a}{c} \quad \vert tan^{-1}()'
                                                   r'\quad \to \quad \alpha ~=~ tan^{-1} \Big( \frac{a}{c} \Big) ~=~'
                                                   r' tan^{-1} \Big( \frac{' + str(hoehe) + 'km }{'
                                                 + str(abstand_beob_warte) + r'km } \Big) ~=~' + str(w_beob)
                                                 + r' ^{ \circ} \quad (3P)'))
        Punkte += 6
        i += 1
    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Abstand des Ballons vom Beobachter.')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{geg:~ \alpha ~=~' + str(w_beob) + r' ^{ \circ},~a~=~'
                                                 + str(hoehe) + r'km, \quad ges: b \quad (1P)} \\'
                                                 + r' sin( \alpha ) ~=~ \frac{a}{b}'
                                                   r' \quad \vert \cdot b \quad \vert \div tan( \alpha ) '
                                                   r' \quad \to \quad b ~=~ \frac{a}{ tan( \alpha )} ~=~'
                                                   r' \frac{' + str(hoehe) + r'km }{ tan( ' + str(w_beob)
                                                 + ' ^{ \circ}  )} ~=~' + str(abstand_beob_ballon) + r'  \quad (3P)'))
        Punkte += 4
        i += 1



    return aufgabe, loesung, Punkte

def sachaufgabe_02(nr, teilaufg):
    # hier wird die Länge der Leiter und die Deckenhöhe berechnet
    laenge_leiter = nzahl(23,50)/10
    deckenhoehe = N(laenge_leiter * (1-nzahl(5,15)/100),2)
    # hier werden die Winkel berechnet
    anstellwinkel = int(math.degrees(math.asin(deckenhoehe / laenge_leiter)))
    i = 0
    Punkte = 0
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
               f'Ein Dachboden ist über eine {laenge_leiter}m lange Klappleiter erreichbar.'
               f'Die Höhe vom Boden zum Dachboden beträgt {deckenhoehe}m.'
               f'Die Leiter ist gut zu begehen, wenn die Leiter mit dem Fußboden höchstens einen Winkel von 61° bildet. \n',
               'Fertige dazu eine Planskizze an. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Anstellwinkel der Leiter mit dem Dachboden. \n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Lösung~Planskizze~(2P)} \quad \mathrm{geg:~a~=~'
                                                 + str(deckenhoehe) + 'm,~b~=~' + str(laenge_leiter)
                                                 + r'm, \quad ges: \alpha \quad (1P)} \\'
                                                 + r' sin( \alpha ) ~=~ \frac{a}{b} \quad \vert sin^{-1}()'
                                                   r'\quad \to \quad \alpha ~=~ sin^{-1} \Big( \frac{a}{b} \Big) ~=~'
                                                   r' sin^{-1} \Big( \frac{' + str(deckenhoehe) + 'm }{'
                                                 + str(laenge_leiter) + r'm } \Big) ~=~' + str(N(anstellwinkel,2))
                                                 + r' ^{ \circ} \quad (3P)'))
        Punkte += 6
        i += 1
    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + f') Beurteile, ob der Dachboden mit der Dachleiter gut zu begehen ist.')
        if anstellwinkel <= 61:
            loesung.append(str(liste_teilaufg[i])
                           + (r') Der Anstellwinkel ist kleiner als 61° und somit der Dachboden gut zu begehen. (1P)'))
        else:
            loesung.append(str(liste_teilaufg[i])
                           + (r') Der Anstellwinkel ist größer als 61° und somit der Dachboden nicht gut zu begehen. (1P)'))
        Punkte += 1
        i += 1



    return aufgabe, loesung, Punkte

aufgaben = [kongruente_Dreiecke(1, [a, b]),
            rechtwinkliges_dreieck(2, [a,b]),
            verhaeltnisgleichgungen(3, [a,b]),
            sachaufgabe_02(4, [a,b])]
# print(kongruente_Dreiecke(1, [a, b]))
# print(rechtwinkliges_dreieck(2, [a,b]))
# print(verhaeltnisgleichgungen(3, [a,b]))
# print(sachaufgabe(4, [a]))
# print(aufgaben)
Punkte = str(sum(element[2] for element in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '10'
Lehrer = 'Herr Herrys'
Art = 'Klassenarbeit über rechtwinklige Dreiecke'
Teil = 'Nachschreiber'


# der Teil in dem die PDF-Datei erzeugt wird
def Hausaufgabenkontrolle():
    geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
    Aufgabe = Document(geometry_options=geometry_options)
    # erste Seite
    table1 = Tabular('c|c|c|c|c|c|', row_height=1.2)
    table1.add_hline(2, 6)
    table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:')
    table1.add_row(SmallText('mit gymnasialer Oberstufe'), Klasse, Fach, Kurs, Lehrer, Datum)
    table1.add_hline(2, 6)
    Aufgabe.append(table1)
    Aufgabe.append(' \n\n')

    Aufgabe.append(LargeText(bold(f'\n {Art} \n\n')))
    for aufgabe in aufgaben:
        for elements in aufgabe[0]:
            if '~' in elements:
                with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Abbildung' in elements:
                Aufgabe.append(elements)
                with Aufgabe.create(Figure(position='h!')) as graph:
                    graph.add_image(aufgabe[3], width='200px')
            else:
                Aufgabe.append(elements)

    Aufgabe.append('\n\n')
    Aufgabe.append(MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

    Aufgabe.append(NewPage())
    Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
    Aufgabe.generate_pdf(f'{Art} {Teil}', clean_tex=true)


# Erwartungshorizont
def Erwartungshorizont():
    geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
    Loesung = Document(geometry_options=geometry_options)
    Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

    for loesung in aufgaben:
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Abbildung' in elements:
                with Loesung.create(Figure(position='h!')) as graph:
                    graph.add_image(loesung[3], width='200px')
            else:
                Loesung.append(elements)

    Loesung.append('\n\n')
    Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

    Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
# Druck der Seiten
Hausaufgabenkontrolle()
Erwartungshorizont()
