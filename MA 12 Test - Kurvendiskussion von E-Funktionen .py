import datetime
import string
import time
import numpy as np
import random, math
from funktionen import *
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from plotten import *
from sympy.plotting import plot as symplot

from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def timer(func):
    """
    Timer-Dekorator zur Messung der Ausführungszeit einer Funktion.
    """
    def wrapper(*args, **kwargs):  # Erklärung eines Dekorators -> https://t1p.de/lqn4d
        start_time = time.perf_counter()  # Zeit vorm ausführen nehmen
        result = func(*args, **kwargs)  # Aufruf der eigentlichen Funktion mit ihren Argumenten
        end_time = time.perf_counter()  # Zeit nachm ausführen
        execution_time = end_time - start_time  # Vergangene Zeit berechnen

        if func.__name__ == 'Hausaufgabenkontrolle':
            print(f'\033[38;2;0;220;120m\033[1mKontrolle in {round(execution_time, 2)} Sekunden erstellt\033[0m')
        elif func.__name__ == 'Erwartungshorizont':
            print(f'\033[38;2;0;220;120m\033[1mErwartungshorizont in {round(execution_time, 2)} Sekunden erstellt\033[0m')
        else:
            print(f'\033[38;2;0;220;120m\033[1m{func.__name__} in {round(execution_time, 2)} Sekunden ausgeführt\033[0m')
        return result
    return wrapper

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def exponentialfunktionen_01(nr, teilaufg):
        i = 0
        extrema_xwert = zzahl(1,3)
        extrema_ywert = zzahl(1,3)
        print(extrema_xwert)
        print(extrema_ywert)
        # rekonstruktion der exponentialfunktion
        fkt_v = exp(b*x+2)*a*x**2
        fkt_a1 = diff(fkt_v,x)
        gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
        gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
        lsg = solve((gleichung1,gleichung2),(a,b))
        print(lsg)
        fkt = exp(lsg[0][1]*x+2)*lsg[0][0]*x**2
        ywerte = [(element,fkt.subs(x,element)) for element in range(-5,6)]
        wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
        xmin = wertebereich[0]
        xmax = wertebereich[-1]
        print(fkt)
        print(ywerte)
        print(wertebereich)
        print(xmin)
        print(xmax)
        graph_xyfix(fkt)
        # return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [exponentialfunktionen_01(1, ['a', 'b'])]

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
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = '2. Test (2. Semester)'
    Titel = 'Exponentialfunktionen und höhere Ableitungsregeln'

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
                k +=1

        Aufgabe.append('\n\n')
        Aufgabe.append(table2)

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)
        # print('\033[38;2;0;220;120m\033[1mKontrolle erstellt\033[0m')

    # Erwartungshorizont
    @timer
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
        # print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

    # Druck der Seiten
    # Hausaufgabenkontrolle()
    # Erwartungshorizont()


anzahl_Arbeiten = 1
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)