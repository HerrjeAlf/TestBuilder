import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from sympy.plotting import plot as symplot

from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def vorz(k):
    if k == -1:
        return '-'
    elif k == 1:
        return '+'
    else:
        pass

def vorz_str(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

def vorz_str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def vektor_rational(vec,p):
    vec_p = [element*p for element in vec]
    print(vec_p)
    k = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
    if k == 3:
        pruefung = True
    else:
        pruefung = False
    print(pruefung)
    return pruefung

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def logarithmusgesetze(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        regeln_aufgabe = {r'log_a(u \cdot v) ~=~ \hspace{10em}': r'log_a(u \cdot v) ~=~ log_a u + log_a v',
                          r'log_a \frac{u}{v} ~=~ \hspace{10em}': r'log_a \frac{u}{v} ~=~ log_a u - log_a v',
                          r'log_a u^r ~=~ \hspace{10em}': r' r \cdot log_a u',
                          r'log_a \sqrt[n]{u} ~=~ \hspace{10em}': r'log_a \sqrt[n]{u} ~=~ \frac{1}{n} \cdot log_a u',
                          r'log_c b ~=~ \hspace{10em}': r'log_c b ~=~ \frac{log_a b}{log_a c} ~=~ \frac{ln b}{ln c}',
                          r'a^{log_a b} ~=~ \hspace{10em}': r'a^{log_a b} ~=~ b',
                          r'log_a 1 ~=~ \hspace{10em}': r'log_a 1 ~=~ 0',
                          r'log_a a ~=~ \hspace{10em}': r'log_a 1 ~=~ 1',
                          r'log_e ~=~ \hspace{10em}': r'log_e ~=~ ln',
                          r'log_{10} ~=~ \hspace{10em}': r'log_{10} ~=~ lg'}
        auswahl = np.random.choice(list(regeln_aufgabe.keys()),2, False)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Vervollständige die folgenden Logarithmusgesetze']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['','']
        grafiken_loesung = ['']


        if 'a' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr))
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')
            aufgabe.append(str(liste_teilaufg[i]) + r') ~' + auswahl[i] + str(liste_teilaufg[i+1])
                           + r') ~' + auswahl[i+1])
            loesung.append(str(liste_teilaufg[i]) + r') ~' + regeln_aufgabe[auswahl[i]] + r' \quad (1P) \hspace{5em}'
                           + str(liste_teilaufg[i+1]) + r') ~' + regeln_aufgabe[auswahl[i+1]] + r' \quad (1P)')
            i += 2

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def exponentialgleichungen(nr, teilaufg):
        i = 0
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Lösen Sie die Exponentialgleichungen.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['', '']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            basis_1 = nzahl(2,8)
            exponent_1 = nzahl(3,5)
            ergebnis_1 = basis_1 ** exponent_1
            basis_2 = nzahl(2,8)
            exponent_2 = nzahl(2,5)
            exponent_2_summe = zzahl(1,3)
            faktor = zzahl(2,30)*20
            ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_summe)

            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr))
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')
            aufgabe.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1)
                           + r' \quad ' + str(liste_teilaufg[i+1]) + r') \quad ' + gzahl(faktor) + r' \cdot '
                           + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(faktor*ergebnis_2)
                           + r' \hspace{5em}')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1)
                           + r' \quad \vert log_{' + gzahl(basis_1) + r'} \quad \to \quad x ~=~ ' + gzahl(exponent_1)
                           + r' \quad (2P) \\' + str(liste_teilaufg[i+1]) + r') \quad ' + gzahl(faktor) + r' \cdot '
                           + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(faktor*ergebnis_2)
                           + r' \quad \vert \div ' + vorz_str_minus(faktor) + r' \quad \to \quad ' + gzahl(basis_2)
                           + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(ergebnis_2) + r' \quad \vert log_{'
                           + gzahl(basis_2) + r'} \quad (2P) \\ x' + vorz_str(exponent_2_summe) + r' ~=~ '
                           + gzahl(exponent_2 + exponent_2_summe) + r' \quad \vert ' + vorz_str(-1 * exponent_2_summe)
                           + r' \quad \to \quad x ~=~ ' + gzahl(exponent_2) + r' \quad (2P) \\')
            i += 2

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def wachstumsfunktion(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        def Aufgabe_Variante_1():

            Text = ('Ein Patient nimmt ein Medikament ein. Anschließend wird die Konzentration des Medikaments  im Blut'
                    ' jede Stunde in mg/l gemessen. Die Messwerte ergeben folgende Tabelle: \n\n')

            Grundwert = nzahl(10, 20) * 10
            Prozentwert = nzahl(5, 15)
            Wachstumsfaktor = 1 - Prozentwert / 100
            Liste = [N(Grundwert * Wachstumsfaktor ** i, 3) for i in range(20)]
            Einheit_y = 'mg/l'
            Einheit_x = 'Stunden'
            return Text, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x

        def Aufgabe_Variante_2():

            Text = ('Die Anzahl der Einwohner in Millionen eines Landes wurde jedes Jahr bestimmt. Die Ergebnisse'
                   ' wurden in der folgenden Tabelle festgehalten: \n\n')

            Grundwert = nzahl(80, 200)
            Prozentwert = zzahl(2,20) / 10
            Wachstumsfaktor = 1 + Prozentwert / 100
            Liste = [N(Grundwert * Wachstumsfaktor ** i, 4) for i in range(20)]
            Einheit_y = 'Millionen'
            Einheit_x = 'Jahren'
            return Text, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x

        if random.random() < 0.5:
            Aufg_Text, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x = Aufgabe_Variante_1()
        else:
            Aufg_Text, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x = Aufgabe_Variante_2()

        Aufg_t = nzahl(7, 10)
        Aufg_wert_y = int(N(Aufg_Liste[Aufg_t], 2))
        Aufg_wert_t = nzahl(10, 17)

        table2 = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
        table2.add_hline(2, 7)
        table2.add_row('Tabelle mit Werten ',f'Zeit in {Aufg_Einheit_x}', '0', '1', '2', '3', '4')
        table2.add_hline(2, 7)
        table2.add_row('',f'Wert in {Aufg_Einheit_y}', Aufg_Liste[0], Aufg_Liste[1], Aufg_Liste[2],
                       Aufg_Liste[3], Aufg_Liste[4])
        table2.add_hline(2, 7)

        table3 = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
        table3.add_hline(2, 7)
        table3.add_row('Ergebnisse: ','Quotient der Werte', 'a1/a0', 'a2/a1', 'a3/a2', 'a4/a3', 'a5/a4')
        table3.add_hline(2, 7)
        table3.add_row('','Quotienten', N(Aufg_Liste[1] / Aufg_Liste[0], 4), N(Aufg_Liste[2] / Aufg_Liste[1], 4),
                       N(Aufg_Liste[3] / Aufg_Liste[2], 4), N(Aufg_Liste[4] / Aufg_Liste[3], 4),
                       N(Aufg_Liste[5] / Aufg_Liste[4], 4))
        table3.add_hline(2, 7)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), Aufg_Text]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['','']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append((f'Loesung_{nr}{liste_teilaufg[i]}',''))

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.extend((str(teilaufg[i]) + ') Weisen Sie nach, das es sich um exponentielles '
                                                'Wachstum handelt. \n\n', table2, ' \n\n\n'))
            loesung.extend((str(teilaufg[i]) + r') \quad \mathrm{Alle~Quotienten~sind~gleich~gross.~Damit~handelt~es~sich~'
                                               r'um~exponentielles~Wachstum. \quad (3P)}', table3))
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + ') Stellen Sie die Wachstumsfunktion f(x) auf. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad (x)~=~' + str(Aufg_c0) + r' \cdot '
                                               + str(Aufg_a) + r'^x \quad (2P)'))
            i += 1


        if 'c' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + f') Berechnen Sie die Zeit bis  {Aufg_wert_y} {Aufg_Einheit_y}'
                                              ' erreicht werden. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad \quad ' + str(Aufg_wert_y) + r'~=~'+ str(Aufg_c0)
                                               + r' \cdot '+ str(Aufg_a) + r'^x \quad \vert \div ' + str(Aufg_c0)
                                               + r' \quad \to \quad ' + latex(Rational(Aufg_wert_y,Aufg_c0))
                                               + r'~=~'+ str(Aufg_a) + r'^x \quad \vert log_{' + str(Aufg_a)
                                               + r'} \quad \to \quad x~=~'
                                               + str(N(math.log(Rational(Aufg_wert_y,Aufg_c0),Aufg_a),5))
                                               + r' \quad (3P)'))
            i += 1


        if 'd' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + f') Berechne den Wert der nach {Aufg_wert_t} {Aufg_Einheit_x}'
                                              f' erreicht wird. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad f(' + str(Aufg_wert_t) + r')~=~' + str(Aufg_c0)
                                               + r' \cdot '+ str(Aufg_a) + r'^{'+ str(Aufg_wert_t)+ r'} ~=~ '
                                               + latex(N(Aufg_c0*Aufg_a**Aufg_wert_t,4)) + r' \quad (2P)'))
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]


    aufgaben = [logarithmusgesetze(1, ['a', 'b']),
                exponentialgleichungen(2, ['a']),
                wachstumsfunktion(3,['a','b','c','d'])]

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
    Titel = 'Wachstumsfunktionen und Logarithmus'

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