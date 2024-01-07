import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from sympy import *

# Definition der Funktionen

a, b, c, d, e, f, g, r, s, x, y, z = symbols('a b c d e f g r s x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]

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

def erstellen(Teil):
    print(f'\n\033[1;35m{Teil}\033[0m')

    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

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

        auswahl_liste = werte_bel_dreieck()
        seite_1 = auswahl_liste['Seite_bez'][0]
        seite_1_wert = auswahl_liste['Seite_wert'][0]
        seite_2 = auswahl_liste['Seite_bez'][1]
        seite_2_wert = auswahl_liste['Seite_wert'][1]
        seite_3 = auswahl_liste['Seite_bez'][2]
        seite_3_wert = auswahl_liste['Seite_wert'][2]
        winkel_1 = auswahl_liste['Winkel_bez'][0]
        winkel_1_wert = auswahl_liste['Winkel_wert'][0]
        winkel_2 = auswahl_liste['Winkel_bez'][1]
        winkel_2_wert = auswahl_liste['Winkel_wert'][1]
        winkel_3 = auswahl_liste['Winkel_bez'][2]
        winkel_3_wert = auswahl_liste['Winkel_wert'][2]


        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Von einem allgemeinen Dreieck, sind folgende Daten gegeben: ',
                   str(seite_1) + '~ = ~' + latex(seite_1_wert) + r'cm, \quad '
                   + str(seite_2) + '~ = ~' + latex(seite_2_wert) + r'cm, \quad '
                   + winkel_1 + '~ = ~' + latex(winkel_1_wert) + r' ^{ \circ } \quad']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        if a in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die restlichen Winkel im Dreieck. '
                                                    'Fertige dazu eine Planskizze an. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{geg:~} ' + str(seite_1) + '~=~' + latex(seite_1_wert)
                                                     + r'cm, \quad ' + str(seite_2) + '~=~' + latex(seite_2_wert)
                                                     + r'cm, \quad ' + winkel_1 + '~=~' + latex(winkel_1_wert)
                                                     + r'^{ \circ } \quad \mathrm{ges:~}' + winkel_2
                                                     + r' \quad (1P) \quad \mathrm{aus~der~Planskizze~(2P)~folgt:~} \\'
                                                     + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                     + r' \frac{' + str(seite_2) + '}{~sin(' + winkel_2
                                                     + r')} \quad \to \quad \frac{~sin(' + winkel_2 + ')}{sin('
                                                     + winkel_1 + r')} ~=~ \frac{' + str(seite_2) + '}{'
                                                     + str(seite_1) + r'} \quad \vert \cdot sin(' + winkel_1
                                                     + r') \quad (2P) \\' + 'sin(' + winkel_2 + r') ~=~ \frac{'
                                                     + str(seite_2) + r'}{' + str(seite_1) + r'} \cdot sin(' + winkel_1
                                                     + r') \quad \vert ~ arcsin() \quad \to \quad ' + winkel_2
                                                     + r' ~=~ arcsin \Big( \frac{' + str(seite_2)  + r'}{' + str(seite_1)
                                                     + r'} \cdot sin(' + winkel_1 + r') \Big) \quad (1P) \\'
                                                     + winkel_2 + r' ~=~ arcsin \Big( \frac{'
                                                     + latex(seite_2_wert) + 'cm}{' + latex(seite_1_wert)
                                                     + r'cm} \cdot sin(' + latex(winkel_1_wert) + r'^{ \circ } ) \Big) ~=~'
                                                     + latex(winkel_2_wert) + r'^{ \circ } \quad (2P) \\'
                                                     + winkel_3 + r'~=~ 180^{ \circ} ~-~' + str(winkel_1_wert)
                                                     + r'^{ \circ} ~-~ ' + str(winkel_2_wert) + r'^{ \circ} ~=~ '
                                                     + str(winkel_3_wert) + r'^{ \circ} \quad (2P)'))
            i += 1

        if b in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Länge der Seite {seite_3} mit dem Sinussatz. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{aus~der~Planskizze~folgt:~} \hspace{15em} \\'
                                                     + r' \frac{' + str(seite_1) + '}{~sin(' + winkel_1 + ')} ~=~'
                                                     + r' \frac{' + str(seite_3) + '}{~sin(' + winkel_3
                                                     + r')} \quad \vert \cdot sin(' + winkel_3 + r') \quad \to \quad '
                                                     + str(seite_3) + r'~=~ \frac{' + str(seite_1) + r' \cdot sin('
                                                     + winkel_3 + ') }{ sin(' + winkel_1 + r') } \quad (2P) \\'
                                                     + str(seite_3) + r'~=~ \frac{' + str(seite_1_wert) + r'cm \cdot sin('
                                                     + latex(winkel_3_wert) + r' ^{ \circ } )}{ sin(' + latex(winkel_1_wert)
                                                     + r' ^{ \circ } )} ~=~' + latex(seite_3_wert) + r'cm \quad (2P) \\'))
            i += 1

        if c in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            flaeche = 0.5*seite_1_wert*seite_2_wert*math.sin(math.radians(winkel_3_wert))
            print(N(flaeche,3))
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Fläche des Dreiecks. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad A ~ = ~ \frac{1}{2} \cdot ' + seite_1 + r' \cdot ' + seite_2
                                                     + r' \cdot sin(' + winkel_3 + r') ~=~ \frac{1}{2} \cdot '
                                                     + latex(seite_1_wert) + r'cm \cdot ' + latex(seite_2_wert)
                                                     + r'cm \cdot sin(' + latex(winkel_3_wert) + '^{ \circ } ) ~=~ '
                                                     + latex(N(flaeche,3)) + r'cm^2 \quad (3P) \\'))
            i += 1

        return aufgabe, loesung

    aufgaben = [beliebiges_dreieck(1,[a,b,c])]

    # erstellen der Tabelle zur Punkteübersicht
    Punkte = (sum(liste_punkte[1:]))
    liste_bez.append('Summe')
    liste_punkte.append(str(Punkte))
    anzahl_spalten = len(liste_punkte)
    liste_ergebnis_z1 = ['erhaltene']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z1.append('')
    liste_ergebnis_z2 = ['Punkte']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z2.append('')

    spalten = '|'
    for p in liste_punkte:
        spalten += 'c|'

    table2 = Tabular(spalten, row_height=1.2)
    table2.add_hline()
    table2.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben'),))
    table2.add_hline()
    table2.add_row(liste_bez)
    table2.add_hline()
    table2.add_row(liste_punkte)
    table2.add_hline()
    table2.add_row(liste_ergebnis_z1)
    table2.add_row(liste_ergebnis_z2)
    table2.add_hline()

    print(table2)
    # Angaben für den Test im pdf-Dokument
    Datum = datetime.date.today().strftime('%d.%m.%Y')
    Kurs = 'Grundkurs'
    Fach = 'Mathematik'
    Klasse = '10'
    Lehrer = 'Herr Herrys'
    Art = 'Hausaufgabenkontrolle 07'
    Titel = 'Flächen berechnen'


    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        # erste Seite
        table1 = Tabular('|c|c|c|c|c|c|', row_height=1.2)
        table1.add_row((MultiColumn(6, align='c', data=MediumText(bold('Torhorst - Gesamtschule'))),))
        table1.add_row((MultiColumn(6, align='c', data=SmallText(bold('mit gymnasialer Oberstufe'))),))
        table1.add_hline()
        table1.add_row('Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:', 'Art:')
        table1.add_hline()
        table1.add_row(Klasse, Fach, Kurs, Lehrer, Datum, Art)
        table1.add_hline()
        Aufgabe.append(table1)
        Aufgabe.append(' \n\n\n\n')
        Aufgabe.append(LargeText(bold(f' {Titel} \n\n')))
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
        Aufgabe.append(table2)

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mKontrolle erstellt\033[0m')

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

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

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 2
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print() # Abstand zwischen den Arbeiten (im Terminal)

