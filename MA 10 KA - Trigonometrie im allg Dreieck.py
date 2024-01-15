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
from flaechen_konstruieren import dreieck_zeichnen_mit_hoehe, dreieck_zeichnen

# Definition der Funktionen

a, b, c, d, e, f, g, r, s, x, y, z = symbols('a b c d e f g r s x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]

def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k


def nzahl(p, q):
    k = random.randint(p, q)
    return k

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)


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
                                                     + r') \quad \vert ~ sin^{ -1}() \quad \to \quad ' + winkel_2
                                                     + r' ~=~ sin^{ -1} \Big( \frac{' + str(seite_2)  + r'}{' + str(seite_1)
                                                     + r'} \cdot sin(' + winkel_1 + r') \Big) \quad (1P) \\'
                                                     + winkel_2 + r' ~=~ sin^{ -1} \Big( \frac{'
                                                     + latex(seite_2_wert) + 'cm}{' + latex(seite_1_wert)
                                                     + r'cm} \cdot sin(' + latex(winkel_1_wert) + r'^{ \circ } ) \Big) ~=~'
                                                     + latex(winkel_2_wert) + r'^{ \circ } \quad (2P) \\'
                                                     + winkel_3 + r'~=~ 180^{ \circ} ~-~' + str(winkel_1_wert)
                                                     + r'^{ \circ} ~-~ ' + str(winkel_2_wert) + r'^{ \circ} ~=~ '
                                                     + str(winkel_3_wert) + r'^{ \circ} \quad (2P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
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
                                                     + r' ^{ \circ } )} ~=~' + latex(seite_3_wert) + r'cm \quad (2P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
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
                                                     + latex(N(flaeche,3)) + r'cm^2 \quad (3P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        return aufgabe, loesung

    def pruefungsaufgaben_01(nr, teilaufg):
        i = 0
        alpha = nzahl(30,60)
        beta = nzahl(70,110)- alpha
        gamma = 180 - alpha - beta
        print('alpha ' + str(alpha)), print('beta ' + str(beta)), print('gamma ' + str(gamma))
        seite_c = nzahl(6,12)
        seite_a = round(seite_c * math.sin(math.radians(alpha))/math.sin(math.radians(gamma)),3)
        seite_b = round(seite_c * math.sin(math.radians(beta))/math.sin(math.radians(gamma)),3)
        seite_h = round(seite_a * math.sin(math.radians(beta)),1)
        print('seite a ' + str(seite_a)), print('seite b ' + str(seite_b)), print('seite c ' + str(seite_c)), print('seite h ' + str(seite_h))
        gamma_1 = 90 - alpha
        xwert_punkt_c = round(math.cos(math.radians(alpha))*seite_b,3)
        ywert_punkt_c = round(math.sin(math.radians(alpha))*seite_b,3)
        flaeche = round(0.5*seite_a*seite_b*math.sin(math.radians(gamma)),2)
        # Listen für die Zeichung des Dreiecks
        pkt = [[0, 0], [seite_c, 0], [xwert_punkt_c, ywert_punkt_c],[xwert_punkt_c,0]]
        print(pkt)
        pkt_bez = ['A', 'B', 'C', 'F']
        st = ['a', 'b', 'c', 'h']
        st_werte = [seite_a, seite_b, seite_c, seite_h]
        wk = [r' \alpha ', r' \beta ', r' \gamma_1 ',  r' ^{ \circ}']
        wk_werte = [alpha, beta, gamma_1, 90]

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n',
                   'Die folgende Abbildung stellt ein beliebiges Dreieck dar.']
        aufgabe.append(r' \mathrm{es~gilt: \quad h~=~' + str(seite_h) + r'cm, \quad a~=~' + str(seite_a)
                       + r'cm, \quad \mathrm{und} \quad \gamma_1~=~' + str(gamma_1) + r'^{ \circ}}')
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken = [f'Grafik_{nr}{liste_teilaufg[i]}']
            dreieck_zeichnen_mit_hoehe(pkt, pkt_bez, st, wk, grafiken[0])
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Länge der Strecke FB. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{geg: \quad a~=~' + str(seite_a) + r'cm,~ h~=~'
                                                     + str(seite_h) + r' \quad ges: \quad \overline{FB} \quad (1P)} \\'
                                                     + r'h^2~+~ \overline{FB}^2~=~a^2 \quad \vert ~- h^2'
                                                     r' \quad \to \quad \overline{FB}^2~=~a^2~-~h^2 \quad \vert \sqrt{}'
                                                     r' \quad \to \quad \overline{FB}~=~ \sqrt{a^2~-~h^2} \quad (2P) \\'
                                                     r' \overline{FB} ~=~ \sqrt{(' + str(seite_a) + 'cm)^2 - ('
                                                     + str(seite_h) + 'cm)^2 } ~=~'
                                                     + gzahl(N(seite_c - xwert_punkt_c,1)) + r'cm \quad (2P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        if b in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Größe der Winkel Alpha und Beta. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \alpha ~=~180^{ \circ } - 90^{ \circ } -' + str(gamma_1)
                                                     + r'^{ \circ} ~=~' + str(alpha)  + r'^{ \circ} \quad (2P) \\'
                                                     r' sin( \beta ) ~=~ \frac{h}{a} \quad \vert sin^{-1}() \quad'
                                                     r' \to \quad \beta ~=~ sin^{-1} \Big( \frac{h}{a} \Big) ~=~ '
                                                     r'sin^{-1} \Big( \frac{' + str(seite_h) + '}{' + str(seite_a)
                                                     + r'} \Big) ~=~ ' + str(beta) + r'^{ \circ} \quad (4P) \\ '
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        if c in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Länge der Seite b. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \frac{a}{sin( \alpha)} ~=~ \frac{b}{sin( \beta)}'
                                                     r' \quad \vert \cdot sin( \beta) \quad \to \quad b~=~'
                                                     r' \frac{a \cdot sin( \beta )}{sin( \alpha )} ~=~ \frac{'
                                                     + str(seite_a) + r'cm \cdot sin(' + str(beta) + r'^{ \circ})}'
                                                     r'{sin(' + str(alpha) + r'^{ \circ})} ~=~' + str(seite_b)
                                                     + r'cm \quad (4P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        if d in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Fläche vom Dreieck ABC. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \gamma ~=~180^{ \circ } - \alpha - \beta ~=~'
                                                     r'180^{ \circ } - ' + str(alpha) + r'^{ \circ } - ' + str(beta)
                                                     + r'^{ \circ } ~=~' + str(gamma) + r'^{ \circ} \quad (2P) \\'
                                                     r' A ~=~ \frac{1}{2} \cdot a \cdot b \cdot sin( \gamma ) ~=~'
                                                     r' \frac{1}{2} \cdot ' + str(seite_a) + r'cm \cdot '
                                                     + str(seite_b) + r'cm \cdot sin(' + str(gamma)
                                                     + r'^{ \circ }) ~=~' + str(flaeche) + r'cm^2 \quad (3P) \\'
                                                     + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1
        return aufgabe, loesung, grafiken

    aufgaben = (beliebiges_dreieck(1,[a,b,c]),
                pruefungsaufgaben_01(2, [a,b,c,d,e,f]))

    print(aufgaben[1][2])

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

    # Angaben für den Test im pdf-Dokument
    Datum = datetime.date.today().strftime('%d.%m.%Y')
    Kurs = 'Grundkurs'
    Fach = 'Mathematik'
    Klasse = '10'
    Lehrer = 'Herr Herrys'
    Art = 'Klassenarbeit'
    Titel = 'Trigonometrie in allgemeinen Dreiecken'


    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "1cm", "lmargin": "2cm", "bmargin": "1cm", "rmargin": "1cm"}
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
                        graph.add_image(aufgabe[2][0], width='250px')
                    del aufgabe[2][0]
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
        geometry_options = {"tmargin": "1cm", "lmargin": "2cm", "bmargin": "1cm", "rmargin": "1cm"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[2][0], width='200px')
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

