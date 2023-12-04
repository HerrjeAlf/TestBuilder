import pylatex, math, random, sympy, numpy, matplotlib
from random import randrange, randint, choice, shuffle
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
def beliebiges_dreieck(nr, teilaufg):
    i = 0
    Punkte = 0

    def werte_bel_dreieck():
        seite_b = nzahl(3,12)
        seite_a = seite_b + nzahl(2,8)
        gamma = nzahl(30,59)
        seite_c = round(math.sqrt(seite_a**2+seite_b**2-2*seite_a*seite_b*cos(math.radians(gamma))),1)
        alpha = int(math.degrees(math.acos(((seite_a)**2 - (seite_b)**2 - (seite_c)**2)/(-2*seite_b*seite_c))))
        beta = int(180-gamma-alpha)
        auswahl = random.sample([0, 1, 2], 3)
        auswahl_liste = {'Seite_bez' : [['a', 'b', 'c'][x] for x in auswahl],
                    'Seite_wert' : [seite_a, seite_b, seite_c],
                    'Winkel_bez' : [[r' \alpha', r' \beta', r' \gamma'][x] for x in auswahl],
                    'Winkel_wert' : [alpha, beta, gamma]}

        return auswahl_liste

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist jeweils ein beliebiges Dreieck. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    if a in teilaufg:
        auswahl_liste = werte_bel_dreieck()
        seite_1 = auswahl_liste['Seite_bez'][1]
        seite_1_wert = auswahl_liste['Seite_wert'][1]
        seite_2 = auswahl_liste['Seite_bez'][2]
        seite_2_wert = auswahl_liste['Seite_wert'][2]
        winkel_1 = auswahl_liste['Winkel_bez'][1]
        winkel_1_wert = auswahl_liste['Winkel_wert'][1]
        winkel_2 = auswahl_liste['Winkel_bez'][2]
        winkel_2_wert = auswahl_liste['Winkel_wert'][2]

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die gesuchte Seitenlänge mit dem Sinussatz. '
                                                'Fertige dazu eine Planskizze an.')
        aufgabe.append(str(seite_1) + '~ = ~' + latex(seite_1_wert) + r'cm, \quad'
                       + winkel_1 + '~ = ~' + latex(winkel_1_wert) + r' ^{ \circ }, \quad'
                       + winkel_2 + '~ = ~' + latex(winkel_2_wert) + r' ^{ \circ }, \quad'
                       + r' \mathrm{und~gesucht~ist:~} ' + str(seite_2))
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{aus~der~Planskizze~(2P)~folgt:~} \quad '
                                                 + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                 + r' \frac{' + str(seite_2) + '}{~sin(' + winkel_2
                                                 + r')} \quad \vert \cdot sin(' + winkel_2 + r') \quad \to \quad '
                                                 + str(seite_2) + r'~=~ \frac{' + str(seite_1) + r' \cdot sin('
                                                 + winkel_2 + ') }{ sin(' + winkel_1 + r')} \quad (2P) \\' + str(seite_2)
                                                 + r'~=~ \frac{' + str(seite_1_wert) + r'cm \cdot sin('
                                                 + latex(winkel_2_wert) + r' ^{ \circ } )}{ sin(' + latex(winkel_1_wert)
                                                 + r' ^{ \circ } )} ~=~' + latex(seite_2_wert) + r'cm \quad (2P) \\'))
        i += 1
        Punkte += 6
    if b in teilaufg:
        auswahl_liste = werte_bel_dreieck()
        seite_1 = auswahl_liste['Seite_bez'][1]
        seite_1_wert = auswahl_liste['Seite_wert'][1]
        seite_2 = auswahl_liste['Seite_bez'][2]
        seite_2_wert = auswahl_liste['Seite_wert'][2]
        winkel_1 = auswahl_liste['Winkel_bez'][1]
        winkel_1_wert = auswahl_liste['Winkel_wert'][1]
        winkel_2 = auswahl_liste['Winkel_bez'][2]
        winkel_2_wert = auswahl_liste['Winkel_wert'][2]

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechne den gesuchten Winkel. '
                                                'Fertige dazu eine Planskizze an. ')
        aufgabe.append(str(seite_1) + '~ = ~' + latex(seite_1_wert) + r'cm, \quad '
                       + str(seite_2) + '~ = ~' + latex(seite_2_wert) + r'cm, \quad '
                       + winkel_1 + '~ = ~' + latex(winkel_1_wert) + r' ^{ \circ } \quad '
                       + r' \mathrm{und~gesucht~ist:~} ' + str(winkel_2))
        loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{aus~der~Planskizze~(2P)~folgt:~} \quad '
                                                 + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                 + r' \frac{' + str(seite_2) + '}{~sin(' + winkel_2
                                                 + r')} \quad \to \quad \frac{~sin(' + winkel_2 + ')}{sin('
                                                 + winkel_1 + r')} ~=~ \frac{' + str(seite_2) + '}{'
                                                 + str(seite_1) + r'} \quad \vert \cdot sin(' + winkel_1
                                                 + r') \quad (2P) \\ sin(' + winkel_2 + r')~=~ \frac{' + str(seite_2)
                                                 + r'}{' + str(seite_1) + r'} \cdot sin(' + winkel_1
                                                 + r') \quad \vert ~ arcsin() \quad \to \quad ' + winkel_2
                                                 + r' ~=~ arcsin \Big( \frac{' + str(seite_2)  + r'}{' + str(seite_1)
                                                 + r'} \cdot sin(' + winkel_1 + r') \Big) \quad (1P) \\'
                                                 + winkel_2 + r' ~=~ arcsin \Big( \frac{'
                                                 + latex(seite_2_wert) + 'cm}{' + latex(seite_1_wert) + r'cm} \cdot sin('
                                                 + latex(winkel_1_wert) + r' ^{ \circ } ) \Big) ~=~' + latex(winkel_2_wert)
                                                 + r' ^{ \circ } \quad (2P) \\'))
        i += 1
        Punkte += 7


    return aufgabe, loesung, Punkte


aufgaben = [beliebiges_dreieck(1,[a,b])]

Punkte = str(sum(element[2] for element in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '10'
Lehrer = 'Herr Herrys'
Art = 'HAK 06 - Sinussatz II'
Teil = 'Gr. A'


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
