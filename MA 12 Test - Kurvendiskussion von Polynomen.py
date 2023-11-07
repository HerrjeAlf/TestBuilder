import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *

# Definition der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def vorz_str(k):
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

def vorz_str_minus(k):
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def erstellen(Teil):
    print(f'\n\033[1;35mHAK {Teil}\033[0m')

    def Graph(a, b, xwert, f, titel, n, name):
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_xlabel('Ost', size=10, labelpad=-24, x=1.03)
        ax.set_ylabel('Höhe', size=10, labelpad=-21, y=1.02, rotation=0)
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(np.linspace(0, 8, 9, endpoint=True))
        plt.yticks(np.linspace(1, 5, 5, endpoint=True))
        plt.axis([-1, 9, 0, 6])
        plt.plot(a, b, linewidth=2)
        plt.suptitle(titel, usetex=True)
        return plt.savefig(name, dpi=200)

    def kurvendiskussion(nr, teilaufg):
        i = 0
        Punkte = 0
        xwert_Extrema = zzahl(1,4)
        ywert_Extrema = zzahl(1,4)
        if xwert_Extrema < 0:
            xwert_Wendepunkt = xwert_Extrema + nzahl(1,3)
        else:
            xwert_Wendepunkt = xwert_Extrema - nzahl(1,3)

        if a in teilaufg:
            A = numpy.array([[xwert_Extrema ** 3, xwert_Extrema ** 2, xwert_Extrema, 1],
                             [xwert_Wendepunkt ** 3, xwert_Wendepunkt ** 2, xwert_Wendepunkt, 1],
                             [3 * (xwert_Extrema ** 2), 2 * xwert_Extrema, 1, 0],
                             [6* xwert_Wendepunkt, 2, 0, 0]])
            lv = numpy.array([ywert_Extrema, 0, 0, 0])

            Punkte += 6
            i += 1

        return [aufgabe, loesung, Punkte]

    aufgaben = [kurvendiskussion(1, [a])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'Test - Anwendungen der Ableitung'

    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        # erste Seite
        table1 = Tabular('c|c|c|c|c|c|', row_height=1.2)
        table1.add_hline(2, 6)
        table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:',
                       'Datum:')
        table1.add_row(SmallText('mit gymnasialer Oberstufe'), Klasse, Fach, Kurs, Lehrer, Datum)
        table1.add_hline(2, 6)
        Aufgabe.append(table1)
        Aufgabe.append(' \n\n')
        Aufgabe.append(LargeText(bold(f'\n {Art} \n\n')))

        for aufgabe in aufgaben:
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                else:
                    Aufgabe.append(elements)

        Aufgabe.append('\n\n')
        Aufgabe.append(
            MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
        Aufgabe.append(' \n\n')
        with Aufgabe.create(Figure(position='h!')) as graph:
            graph.add_image(r'Aufgabe_3.png', width='400px')
            # falls es nicht funktioniert wieder zu 'C:\Users\aherr\Documents\GitHub\Aufgabe_1.png' wechseln

        Aufgabe.generate_pdf(f'{Art} {Teil}', clean_tex=true)

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

        for loesung in aufgaben:
            with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                for elements in loesung[1]:
                    agn.append(elements)

        Loesung.append('\n\n')
        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))


        Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
        plt.cla()

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_HAKs = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')