import datetime
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.gridspec as grid

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

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def extremalproblem_01(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        auswahl = random.choice([0,1])
        auswahl = 1
        if auswahl == 0:
            sp_yachse = nzahl(3,8)
            steigung = -1 * nzahl(1,10)/4
            fkt = steigung * x + sp_yachse
            fkt_str = gzahl(steigung) + 'x' + vorz_str(sp_yachse)
            xmax = gzahl(-1*sp_yachse/steigung)
        elif auswahl == 1:
            faktor = -1*nzahl(10,40)
            sp_yachse = nzahl(3,8)
            print(faktor/50)
            fkt = faktor/50*x**2 + sp_yachse
            fkt_str = latex(Rational(faktor,50)) + 'x^2' + vorz_str(sp_yachse)
            print(solve(fkt,x))
            xmax = solve(fkt,x)[1]


        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen \n'
                   'Rechtecks auf dem Graphen von f.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['','']
        grafiken_loesung = []

        if 'a' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes
            xwert_p = int(xmax/3 + 0.5)
            ywert_p = fkt.subs(x,xwert_p)
            fig, ax = plt.subplots()
            fig.canvas.draw()
            fig.tight_layout()
            ax.spines['top'].set_color('none')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position(('data', 0))
            ax.spines['left'].set_position(('data', 0))
            ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
            ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
            ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
            arrow_fmt = dict(markersize=4, color='black', clip_on=False)
            ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
            ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
            plt.annotate(r'$ P(x \vert y ) $', xy=(xwert_p, ywert_p), xycoords='data',
                         xytext=(+10, +10), textcoords='offset points', fontsize=16)
            plt.grid()
            xwerte = np.arange(0, xmax, 0.01)
            ywerte = [fkt.subs(x, elements) for elements in xwerte]
            plt.plot(xwerte, ywerte)
            plt.plot([0,xwert_p], [ywert_p,ywert_p])
            plt.plot([xwert_p,xwert_p],[ywert_p,0])
            plt.scatter([xwert_p, ], [ywert_p, ], 50, color='blue')
            plt.savefig(f'Aufgabe_{nr}{liste_teilaufg[i]}', dpi=200)
            plt.show()

            # Aufgaben und Lösungen
            aufgabe.append('Wie muss x gewählt werden, damit die Rechtecksfläche maximal wird, wenn ')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{ist.}')
            loesung.append(str(teilaufg[i]) + r') \quad geg: f(x)~=~' + fkt_str
                           + r' \quad ges: \mathrm{x,y~für~A_{max}} \quad (1P) \hspace{20em} \\'
                           + r' \mathrm{es~gilt: \quad HB.: A~=~x \cdot y \quad und \quad NB.:f(x)~=~'
                           + fkt_str + r' \quad (2P) } \\'
                           + r' \\')
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [extremalproblem_01(1, ['a'])]

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
    Art = '8. Hausaufgabenkontrolle'
    Titel = 'Extremalprobleme und Rekonstruktion von Funktionen'

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
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][k], width='200px')
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
                    Loesung.append(elements)
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='200px')
                else:
                    Loesung.append(elements)

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

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
