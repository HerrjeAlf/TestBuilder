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
from plotten import graph_xyfix, loeschen

# Definition der Funktionen

a, b, c, d, e, f, g, r, s, x, y, z = symbols('a b c d e f g r s x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]


def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def vorz(k):
    if k == -1:
        return '-'
    elif k == 1:
        return '+'
    else:
        return k

def vorz_str(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def vorz_str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)


def erstellen(Teil):
    print(f'\n\033[1;35m{Teil}\033[0m')

    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    # Berechnung für die Aufgaben
    def lineare_funktionen(nr, teilaufg):
        i = 0

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        if 'a' in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken = ['Graph_Aufgabe']
            # Werte für den Funktionsgraphen
            steigung = zzahl(2,8)/2
            schnittpunkt_y = zzahl(1,8)/2
            fkt = steigung *x + schnittpunkt_y
            fkt_str = gzahl(steigung) + 'x' + vorz_str(schnittpunkt_y)
            print(fkt), print(fkt_str)

            table1aA = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
            table1aA.add_hline(start=2)
            table1aA.add_row(
                (MultiRow(3, data='Wertetabelle der Funktion f:'), 'x Werte', 'x = -2', 'x = -1', 'x = 0', 'x = 1', 'x = 2'))
            table1aA.add_hline(start=2)
            table1aA.add_row(('', MultiRow(2, data='y Werte'), '', '', '', '', ''))
            table1aA.add_empty_row()
            table1aA.add_hline(start=2)

            table1aB = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
            table1aB.add_hline(start=2)
            table1aB.add_row(
                (MultiRow(3, data='Wertetabelle der Funktion f:'), 'x Werte', 'x = -2', 'x = -1', 'x = 0', 'x = 1', 'x = 2'))
            table1aB.add_hline(start=2)
            table1aB.add_row(('', 'y Werte', gzahl(N(fkt.subs(x,-2),3)),
                              gzahl(N(fkt.subs(x,-1),3)), gzahl(N(fkt.subs(x,0),3)),gzahl(N(fkt.subs(x,1),3)),
                              gzahl(N(fkt.subs(x,2),3))))
            table1aB.add_hline(start=2)

            graph_xyfix(fkt, name='Graph_Aufgabe')
            aufgabe.append(str(liste_teilaufg[i]) + f') Lies die Funktionsgleichung f(x) aus der folgenden Abbildung'
                                                    f' ab und vervollständige die Wertetabelle.')
            aufgabe.append(table1aA)
            loesung.append(str(liste_teilaufg[i]) + r') \quad f(x)~=~ ' + fkt_str +  r' \quad (2P)')
            loesung.append(table1aB)
            loesung.append(r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1
        return [aufgabe, loesung, grafiken]

    aufgaben = [lineare_funktionen(1,['a'])]


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
    Art = 'Hausaufgabenkontrolle 08'
    Titel = 'Wiederholung der lineare Funktionen'


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


anzahl_Arbeiten = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print() # Abstand zwischen den Arbeiten (im Terminal)

