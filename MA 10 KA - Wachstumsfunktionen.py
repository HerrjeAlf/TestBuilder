import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from funktionen import *
from sympy import *
from plotten import graph_xyfix

# Definition der Funktionen

a, b, c, d, e, f, g, r, s, x, y, z = symbols('a b c d e f g r s x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
nr_aufgabe = 0

def erstellen(Teil):
    print(f'\n\033[1;35m{Teil}\033[0m')

    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    # Berechnung für die Aufgaben
    def lineare_funktionen_einstieg(nr, teilaufg):
        i = 0
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Im folgenden Abbildung ist der Graph der Funktion f dargestellt.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['', f'Aufgabe_{nr}{liste_teilaufg[i]}']
        grafiken_loesung = ['']

        # Werte für den Funktionsgraphen
        steigung = zzahl(2, 8) / 2
        schnittpunkt_y = zzahl(1, 8) / 2
        fkt = steigung * x + schnittpunkt_y
        fkt_str = gzahl(steigung) + 'x' + vorz_str(schnittpunkt_y)
        print(fkt), print(fkt_str)


        if 'a' in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend(('', '', ''))
            grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', '', ''))

            # Tabelle zum Eintragen der Werte
            table1aA = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
            table1aA.add_hline(start=2)
            table1aA.add_row(
                (MultiRow(3, data='Wertetabelle der Funktion f:'), 'x Werte', 'x = -2', 'x = -1', 'x = 0', 'x = 1', 'x = 2'))
            table1aA.add_hline(start=2)
            table1aA.add_row(('', MultiRow(2, data='y Werte'), '', '', '', '', ''))
            table1aA.add_empty_row()
            table1aA.add_hline(start=2)

            # Tabelle mit den Lösungen
            table1aB = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
            table1aB.add_hline(start=2)
            table1aB.add_row(
                (MultiRow(3, data='Wertetabelle der Funktion f:'), 'x Werte', 'x = -2', 'x = -1', 'x = 0', 'x = 1', 'x = 2'))
            table1aB.add_hline(start=2)
            table1aB.add_row(('', 'y Werte', gzahl(N(fkt.subs(x,-2),3)),
                              gzahl(N(fkt.subs(x,-1),3)), gzahl(N(fkt.subs(x,0),3)),gzahl(N(fkt.subs(x,1),3)),
                              gzahl(N(fkt.subs(x,2),3))))
            table1aB.add_hline(start=2)

            graph_xyfix(fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}')
            aufgabe.extend((str(liste_teilaufg[i]) + f') Lies die Funktionsgleichung f(x) aus der Darstellung '
                                                    f' ab und vervollständige die Wertetabelle. \n\n', table1aA,' \n\n\n\n'))
            loesung.extend((str(liste_teilaufg[i]) + r') \quad f(x)~=~ ' + fkt_str + r' \quad (2P) \hspace{5em} ', table1aB,
                           r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}'))
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', '', ''))
            grafiken_loesung.extend(('', f'Loesung_{nr}{liste_teilaufg[i]}'))

            # Werte für den Funktionsgraphen
            if steigung > 0:
                steigung_b = -1*nzahl(2, 8) / 2
                schnittpunkt_y_b = nzahl(1, 8) / 2
            else:
                steigung_b = nzahl(2, 8) / 2
                schnittpunkt_y_b = -1 * nzahl(1, 8) / 2


            fkt = steigung_b *x + schnittpunkt_y_b
            fkt_a = steigung*x+schnittpunkt_y
            fkt_str = gzahl(steigung_b) + 'x' + vorz_str(schnittpunkt_y_b)
            print(fkt), print(fkt_str)

            table1bA = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
            table1bA.add_hline(start=2)
            table1bA.add_row((MultiRow(3, data='Wertetabelle der Funktion h:'), 'x Werte', 'x = -2', 'x = -1',
                              'x = 0', 'x = 1', 'x = 2'))
            table1bA.add_hline(start=2)
            table1bA.add_row(('', 'y Werte', gzahl(N(fkt.subs(x,-2),3)),
                              gzahl(N(fkt.subs(x,-1),3)), gzahl(N(fkt.subs(x,0),3)),gzahl(N(fkt.subs(x,1),3)),
                              gzahl(N(fkt.subs(x,2),3))))
            table1bA.add_hline(start=2)

            aufgabe.extend((str(liste_teilaufg[i]) + f') Zeichne zur folgenden Wertetabelle den Graphen'
                                                     f' der Funktion h und lies die Gleichung h(x) ab. \n\n',
                                                     table1bA,' \n\n\n\n'))
            loesung.extend((str(liste_teilaufg[i]) + (r') \quad \mathrm{Graph~siehe~Koordinatensystem'
                           r'\quad (2P) \quad und \quad f(x)~=~ ' + fkt_str + r' \quad (2P)} \\'
                           r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
                           , 'Abbildung'))
            graph_xyfix(fkt,fkt_a, bezn='h', name=f'Loesung_{nr}{liste_teilaufg[i]}')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', '', ''))
            grafiken_loesung.extend(('', f'Loesung_{nr}{liste_teilaufg[i]}'))

            nst = gzahl(N(-1 * schnittpunkt_y / steigung, 2))

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Nullstelle der Funktion f und gib die Schnittpunkte'
                                                    f' mit den Achsen an. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{ x_{0} ~=~ - \frac{n}{m} ~=~ - \frac{'
                           + gzahl(schnittpunkt_y) + r'}{' + gzahl(steigung) + r'} ~=~ '
                           + nst + r' \quad (2P) \quad \to \quad S_x(' + nst + r' \vert 0) \quad und \quad S_y(0 \vert '
                           + gzahl(schnittpunkt_y) +  r') \quad (2P) } \\'
                           + r'\mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
            i += 1
        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def wiederholung_funktionen(nr, teilaufg):
        i = 0
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr)))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        grafiken_aufgaben = ['']
        grafiken_loesung = ['']

        # Werte für den Funktionsgraphen
        # lineare Funktion
        steigung = zzahl(2, 8) / 2
        schnittpunkt_y = zzahl(1, 8) / 2
        fkt_f = steigung * x + schnittpunkt_y
        fkt_f_str = gzahl(steigung) + 'x' + vorz_str(schnittpunkt_y)
        # Parabel
        xwert_sp = zzahl(1,4)
        ywert_sp = zzahl(1,4)
        fkt_p = collect(expand((x-xwert_sp)**2 + ywert_sp),x)
        fkt_sp_str = '(x' + vorz_str(-1*xwert_sp) + ')^2' + vorz_str(ywert_sp)
        fkt_p_str = 'x^2' + vorz_str(-1*2*xwert_sp) + 'x' + vorz_str(ywert_sp + xwert_sp**2)

        # Tabelle mit den Lösungen
        table1aB = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
        table1aB.add_hline(start=2)
        table1aB.add_row((MultiRow(3, data='Wertetabelle der Funktion f:'), 'x Werte', 'x = -2', 'x = -1',
                          'x = 0', 'x = 1', 'x = 2'))
        table1aB.add_hline(start=2)
        table1aB.add_row(('', 'y Werte', gzahl(N(fkt_f.subs(x, -2), 3)),
                          gzahl(N(fkt_f.subs(x, -1), 3)), gzahl(N(fkt_f.subs(x, 0), 3)),
                          gzahl(N(fkt_f.subs(x, 1), 3)), gzahl(N(fkt_f.subs(x, 2), 3))))
        table1aB.add_hline(start=2)

        if 'a' in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend(('', f'Aufgabe_{nr}{liste_teilaufg[i]}'))
            grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', '', ''))
            graph_xyfix(fkt_f, fkt_p, bezn='f', name=f'Aufgabe_{nr}{liste_teilaufg[i]}')
            aufgabe.extend(('In der oberen Abbildung sind die Graphen der linearen Funktion f(x)'
                            ' und der Parabel p(x) dargestellt. \n\n',
                            str(liste_teilaufg[i]) + ') Bestimme aus dem Graphen die Funktionsgleichung f'
                                                     ' und erstelle eine Wertetabelle von -2 bis 2. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + r') \quad f(x)~=~ ' + fkt_f_str + r' \quad (2P) \hspace{5em} ',
                            table1aB, r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}'))
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 8
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
            aufgabe.append(str(liste_teilaufg[i]) + ') Lies den Scheitelpunkt von p ab und bestimme aus dem Graphen'
                                                    ' die Scheitelpunkt- und Normalform. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad S(' + gzahl(xwert_sp) + r' \vert ' + gzahl(ywert_sp)
                           + r') \quad \to \quad f(x)~=~ ' + fkt_sp_str + ' ~=~ ' + fkt_sp_str
                           + r' \quad (4P) \hspace{5em} \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', ''))
            grafiken_loesung.extend(('','',f'Loesung_{nr}{liste_teilaufg[i]}'))

            # Gleichung für die zweite Funktion, in Abhängkeit von der ersten
            if steigung > 0:
                steigung_b = -1 * nzahl(2, 8) / 2
                schnittpunkt_y_b = nzahl(1, 4)
            else:
                steigung_b = nzahl(2, 8) / 2
                schnittpunkt_y_b = -1 * nzahl(1, 4)

            fkt = steigung_b * x + schnittpunkt_y_b
            fkt_a = steigung * x + schnittpunkt_y
            fkt_str = gzahl(steigung_b) + 'x' + vorz_str(schnittpunkt_y_b)
            # Berechnung eines Punktes mit ganzzahligen Werten
            werteliste = [[element,fkt.subs(x, element)] for element in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]]
            werteliste_gesiebt = []
            for element in werteliste:
                if element[1] % 1 == 0 and abs(element[1]) < 6:
                    werteliste_gesiebt.append(element)
                    print(element)

            aufgabe.extend(('Gegeben sind die Punkte Q(' + gzahl(werteliste_gesiebt[0][0]) + ' | '
                            + gzahl(werteliste_gesiebt[0][1]) + ') und P(' + gzahl(0) + ' | '
                            + gzahl(schnittpunkt_y_b) + ') der linearen Funktion h(x). \n\n',
                            str(liste_teilaufg[i]) + f') Zeichne den Graphen den Graphen durch die Punkte P und Q'
                                                     f' der Funktion h und lies die Gleichung h(x) ab. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + r') \quad \mathrm{Graph~siehe~Koordinatensystem'
                            r' \quad (2P) \quad und \quad f(x) ~=~ ' + fkt_str + r' \quad (2P) } \\'
                            + r'\mathrm{insgesamt~' + str(punkte_aufg) + '~Punkte}', 'Abbildung'))
            graph_xyfix(fkt, fkt_a, bezn='f', name=f'Loesung_{nr}{liste_teilaufg[i]}')
            i += 1

        if 'd' in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
            nst = gzahl(N(-1 * schnittpunkt_y / steigung, 2))
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Nullstelle der Funktion f und gib die Schnittpunkte'
                                                    f' mit den Achsen an. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{ x_{0} ~=~ - \frac{n}{m} ~=~ - \frac{'
                           + gzahl(schnittpunkt_y) + r'}{' + gzahl(steigung) + r'} ~=~ '
                           + nst + r' \quad (2P) \quad \to \quad S_x(' + nst + r' \vert 0) \quad und \quad S_y(0 \vert '
                           + gzahl(schnittpunkt_y) + r') \quad (2P) } \\'
                           + r'\mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]


    aufgaben = [wiederholung_funktionen(1,['a', 'b', 'c', 'd'])]

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
    Art = '9. Hausaufgabenkontrolle'
    Titel = 'Nullstellen von linearen Funktionen'


    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))  # fügt das Package 'amsfonts' hinzu, für das \mathbb{R} für reelle Zahlen
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
            k = 0
            for elements in aufgabe[0]:
                k += 1
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][k], width='300px')
                    Aufgabe.append(elements)
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
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            k = 0
            for elements in loesung[1]:
                k += 1
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='250px')
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
    print()  # Abstand zwischen den Arbeiten (im Terminal)


