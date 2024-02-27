import datetime
import string
import numpy as np
import random, math
from funktionen import *
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']


    def ereignisse_ergebnisse(nr, teilaufg):
        i = 0
        auswahl_farbe = np.random.choice(['Weiß', 'Schwarz', 'Blau', 'Rot', 'Gelb', 'Grün'], 2, False)
        farbe_1 = auswahl_farbe[0]
        anzahl_1 = nzahl(5,15)
        farbe_2 = auswahl_farbe[1]
        anzahl_2 = 20 - anzahl_1
        anzahl_ziehen = random.choice([[2,'zweimal'],[3,'dreimal']])
        ergebnisraum = ergebnisraum_zmZ(anzahl_ziehen[0], farbe1=farbe_1, farbe2=farbe_2)
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   f'In einer Urne befinden sich {anzahl_1} Kugeln der Farbe {farbe_1} und {anzahl_2}'
                   f' Kugeln der Farbe {farbe_2}. Aus dieser Urne wird nun {anzahl_ziehen[1]} eine Kugel gezogen und '
                   f'anschließend wieder zurückgelegt. \n\n']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['','']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            def ereig_1():
                anzahl_kugel = nzahl(1,2)
                if anzahl_kugel == 1:
                    text = r' \mathrm{Die~Kugel~der~Farbe~' + latex(farbe_1) + '~wird~einmal~gezogen}'
                else:
                    text = r' \mathrm{Die~Kugel~der~Farbe~' + latex(farbe_1) + '~wird~zweimal~gezogen}'
                lsg_menge = []
                for element in ergebnisraum:
                    i = 0
                    for ergebnis in element:
                        if ergebnis == farbe_1:
                            i += 1
                    if i == anzahl_kugel:
                        lsg_menge.append(element)
                print(lsg_menge)
                return text, lsg_menge

            def ereig_2():
                auswahl = random.choice([farbe_1, farbe_2])
                auswahl_kugel = random.choice(['erste','zweite'])
                text = r' \mathrm{Die~' + auswahl_kugel + '~Kugel~ist~' + latex(auswahl) + '}'
                lsg_menge = []
                if auswahl_kugel == 'erste':
                    for element in ergebnisraum:
                        if element[0] == auswahl:
                            lsg_menge.append(element)
                else:
                    for element in ergebnisraum:
                        if element[1] == auswahl:
                            lsg_menge.append(element)
                return text, lsg_menge

            ereignis_1, lsg_menge_1 = ereig_1()
            ereignis_2, lsg_menge_2 = ereig_2()

            def vereinigung():
                text = r' \mathrm{E_1 \cup E_2}'
                lsg_menge = lsg_menge_1.copy()
                for element2 in lsg_menge_2:
                    if element2 not in lsg_menge:
                        lsg_menge.append(element2)
                return text, lsg_menge

            def geschnitten():
                text = r' \mathrm{E_1 \cap E_2}'
                lsg_menge = []
                for element1 in lsg_menge_1:
                    for element2 in lsg_menge_2:
                        if element2 == element1:
                            lsg_menge.append(element2)
                return text, lsg_menge

            vereinigung, lsg_vereinigung = vereinigung()
            schnittmenge, lsg_schnittmenge = geschnitten()

            aufgabe.extend((str(liste_teilaufg[i]) + f')  Geben Sie die Ergebnismenge der folgenden Ereignisse an.',
                            r' E_1: ' + ereignis_1 + r' \\'
                            + r'E_2: ' + ereignis_2 + r' \hspace{7em} \\'
                            + vereinigung + r' \quad \mathrm{und} \quad ' + schnittmenge + r' \hspace{10em} \\'))
            loesung.append(str(liste_teilaufg[i]) +') Lösung E1: ' + str(lsg_menge_1) + ' (2P) \n'
                           + ' Lösung E2: ' + str(lsg_menge_2) + '(2P) \n'
                           + ' Lösung E1 und E2 vereinigt: ' + str(lsg_vereinigung) + ' (1P) \n'
                           + ' Lösung E1 und E2 geschnitten: ' + str(lsg_schnittmenge) + ' (1P) \n'
                           + ' insgesamt ' + str(punkte_aufg) + ' Punkte \n\n')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]


    aufgaben = [ereignisse_ergebnisse(1, ['a'])]

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
    Klasse = '13'
    Lehrer = 'Herr Herrys'
    Art = '11. Hausaufgabenkontrolle'
    Titel = 'Ergebnisse und Ereignisse im Urnenmodell'

    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))  # fügt das Package 'amsfonts' hinzu, für das \mathbb{R} für reelle Zahlen
        # erste Seite
        table1 = Tabular('|p{1.2cm}|p{2cm}|p{2cm}|p{2cm}|p{1.5cm}|p{5cm}|', row_height=1.2)
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
            k = 0
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][k], width='200px')
                else:
                    Aufgabe.append(elements)
                k += 1

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
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            k = 0
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Loesung.append(elements)
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='200px')
                else:
                    Loesung.append(elements)
                k += 1
        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)
