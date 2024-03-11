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


def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def exponentialfunktionen_01(nr, teilaufg):
        i = 0
        extrema_xwert = zzahl(1,3)
        extrema_ywert = zzahl(1,3)
        if extrema_xwert > 0:
            y_vers = -1*nzahl(0,2)
        else:
            y_vers = nzahl(0,2)
        print(extrema_xwert), print(extrema_ywert), print(y_vers)

        # rekonstruktion der exponentialfunktion
        fkt_v = exp(b*x+2)*a*x**2
        fkt_a1 = diff(fkt_v,x)
        gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
        gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
        lsg = solve((gleichung1,gleichung2),(a,b))
        lsg_a = lsg[0][0]
        lsg_b = lsg[0][1]
        print(lsg)
        fkt = exp(lsg_b*x+2)*lsg_a*x**2 + y_vers
        fkt_str = (vorz_v_aussen(lsg_a,'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b,'x+2') + '}'
                   + vorz_str(y_vers))


        # Werte für Angaben zum Zeichnen des Graphen
        ywerte = [(element,fkt.subs(x,element)) for element in range(-5,6)]
        wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
        xmin = wertebereich[0]
        xmax = wertebereich[-1]
        print(fkt), print(ywerte), print(wertebereich), print(xmin), print(xmax)
        graph_xyfix(fkt)

        # Ableitung der Funktionen
        fkt_a1 = diff(fkt,x)
        fkt_a2 = diff(fkt, x,2)
        fkt_a3 = diff(fkt, x,3)

        fkt_a1_str = ('e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \Big(' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                      + vorz_v_innen(2*lsg_a,'x' + r' \Big)'))
        fkt_a2_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                      + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                      + vorz_str(2*lsg_a) + r' \Big)')
        fkt_a3_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                      + vorz_v_aussen(lsg_a * lsg_b**3, 'x^2') + vorz_v_innen(6 * lsg_a * lsg_b**2, 'x')
                      + vorz_str(6*lsg_a*lsg_b) + r' \Big)')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
                   r' f(x)~=~' + fkt_str]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['','','']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')

            grenzwert_min = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)

            print(grenzwert_min), print(grenzwert_pos)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                           + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                           + fkt_str + '~=~' + latex(grenzwert_min) + r' \quad (2P) \\\\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' in teilaufg:
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')
            if y_vers == 0:
                punkte_aufg = 4
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte der'
                                                        f' Funktion f mit den Achsen. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                               + r' \hspace{10em} \\ \mathrm{Ansatz:~f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                               + r' \quad da e^{' + vorz_v_innen(lsg[0][1],'x+2') + r'} ~immer~ \neq 0'
                               + r' \quad \to \quad ' + (vorz_v_innen(lsg[0][0],'x^2'))
                               + r'~=~ 0} \quad \vert \div ' + gzahl_klammer(lsg[0][0]) + r' \quad \vert sqrt{}() \\'
                               + r' x~=~0 \quad \to \quad S_y ~=~ S_x (0 \vert 0) \quad (4P) \\'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            else:
                punkte_aufg = 2
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Schnittpunkt der'
                                                        f' Funktion f mit der y-Achse. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~y-Achse:}'
                               + r' \hspace{5em} \\ \mathrm{Ansatz:~f(0)~=~ ' + gzahl(y_vers)
                               + r' \quad \to \quad S_y (0 \vert ' + gzahl(y_vers) + r')} \quad (2P) \\'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \mathrm{f^{ \prime }(x) ~=~' + fkt_a1_str
                           + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                           + r' \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str + r'} \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [exponentialfunktionen_01(1, ['a', 'b', 'c'])]

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
    Art = '10. Hausaufgabenkontrolle'
    Titel = 'Kurvendiskussionen einer Exponentialfunktionen'

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

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 1
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)
