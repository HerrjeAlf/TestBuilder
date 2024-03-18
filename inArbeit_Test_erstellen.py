import datetime, string, time,  random, math
import numpy as np
from funktionen import *
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from plotten import *
from sympy.plotting import plot as symplot


def seite(aufgaben):
    geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
    Aufgabe = Document(geometry_options=geometry_options)
    Loesung = Document(geometry_options=geometry_options)

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

    for loesung in aufgaben:
        k = 0
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Abbildung' in elements:
                with Loesung.create(Figure(position='h!')) as graph:
                    graph.add_image(loesung[3][k], width='300px')
            else:
                Loesung.append(elements)
            k += 1

    return Aufgabe, Loesung

def erzeugen(Teil, liste_seiten, angaben):
    Kurs, Fach, Klasse, Lehrer, Art, Titel = angaben[0], angaben[1], angaben[2], angaben[3], angaben[4], angaben[5]
    in_tagen = angaben[6]
    liste_bez = angaben[7]
    liste_punkte = angaben[8]
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d.%m.%Y')



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

    # der Teil in dem die PDF-Datei erzeugt wird
    @timer
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
        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 0
        for element in liste_seiten:
            Aufgabe.extend(element[0])
            Aufgabe.append(NewPage())

        if len(liste_seiten) % 2 == 0:
            Aufgabe.append('für Notizen und Rechnungen:')
            Aufgabe.append(NewPage())

        Aufgabe.append('\n\n')
        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.append('\n\n')
        Aufgabe.append('\n\n')
        Aufgabe.append(table2)

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)

    # Erwartungshorizont
    @timer
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 0
        for element in liste_seiten:
            Loesung.extend(element[0])
            Loesung.append(NewPage())

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()

def pdf_erzeugen(liste_seiten, angaben):
    anzahl_Arbeiten = 1
    probe = True
    alphabet = string.ascii_uppercase
    for teil_id in range(anzahl_Arbeiten):
        if probe:
            erzeugen('Probe {:02d}'.format(teil_id + 1), liste_seiten, angaben)
        else:
            erzeugen(f'Gr. {alphabet[teil_id]}', liste_seiten, angaben)
        print()  # Abstand zwischen den Arbeiten (im Terminal)



