import pylatex, math, random, sympy, numpy
from random import randrange, randint, choice
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold

# Defintion der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')

pi = numpy.pi

liste_variable = [a, b, c, d, x, y, z]


def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k


def nzahl(p, q):
    k = random.randint(p, q)
    return k


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


def folge(zsmstlg):
    a_n = ''
    a_n_str = f'{zsmstlg[0]} '
    for i in zsmstlg:
        a_n += f'{i} '
        if i == '**':
            a_n_str += r'^ '
        elif i == 'x':
            a_n_str += r'n '
        if i == '*':
            a_n_str += r'\cdot '
        if i == '-':
            a_n_str += r'~-~ '
        if i == '+':
            a_n_str += r'~+~ '
    a_n_str += f'{zsmstlg[-1]}'
    a_n = parse_expr(a_n.strip())

    return a_n, a_n_str


def erstellen(buchstabe):
    def Bild_1(a, b, f, n):
        ax = plt.gca()
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
        plt.annotate(n, xy=(-4, f.subs(x, -4)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.axis([-6, 6, -6, 6])
        return plt.plot(a, b, linewidth=2)

    # Berechnung für die Aufgaben

    def folgen(nr, teilaufg):
        liste_teilaufg = [a, b, c, d]
        i = 0
        start_arithm_folge = zzahl(1, 10)
        start_geom_folge = nzahl(1, 10)
        arithm_folge_d = nzahl(2, 10)
        if nzahl(1, 2) == 1:
            p = random.choice([2, 4, 5, 8, 10])
            geom_folge_q = Rational(1, p)
        else:
            geom_folge_q = random.choice([2, 3, 4, 5])

        zusammenstellung = [random.choice([start_arithm_folge, start_geom_folge])]
        auswahl_zusammenstellung = ['+', r'-', r'*', r'**']
        for _ in range(2):
            auswahl = random.choice(auswahl_zusammenstellung)
            zusammenstellung.append(auswahl)
            auswahl_zusammenstellung.remove(auswahl)
            if len(zusammenstellung) == 2:
                zusammenstellung.append('x')

        if zusammenstellung[0] == start_arithm_folge:
            zusammenstellung.append(arithm_folge_d)
            folgenart = r' \mathrm{Es~ist~eine~arithmetische~Folge.} '
            auswahl_folgenart = 0
        else:
            zusammenstellung.append(geom_folge_q)
            folgenart = r' \mathrm{Es~ist~eine~geometrische~Folge.} '
            auswahl_folgenart = 1

        a_n, a_n_str = folge(zusammenstellung)[0], folge(zusammenstellung)[1]

        data = [a_n.subs(x, i) for i in range(4)]
        data_lsg = [a_n.subs(x, i) for i in range(7)]

        print(f'Zusammenstellung: {zusammenstellung}')
        print(a_n)
        print(a_n_str)
        print(data)
        print(folgenart)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Zahlenfolge: \n\n',
                   latex(data[0]) + r', \quad ' + latex(data[1]) + r', \quad ' + latex(data[2]) + r', \quad ' + latex(
                       data[3]) + r', ~ ...  \\']

        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Setze die Zahlenfolge um drei weitere Glieder fort. \n\n')
            loesung.append(
                str(liste_teilaufg[i]) + r') \quad ' + latex(data_lsg[0]) + ',~' + latex(data_lsg[1]) + ',~' + latex(
                    data_lsg[2]) + ',~' +
                latex(data_lsg[3]) + r',~' + latex(data_lsg[4]) + ',~' + latex(data_lsg[5]) + ',~' + latex(data_lsg[6]))
            i += 1

        if b in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) +
                           ') Überprüfe ob es sich um eine arithmetische oder geometrische Zahlenfolge handelt. \n\n')
            if auswahl_folgenart == 0:
                loesung.append(str(
                    liste_teilaufg[i]) + r') \quad \mathrm{Hier~die~Lösung~für~arithm.~Folge} --> a_2 - a_1 = ... usw.')
            elif auswahl_folgenart == 1:
                loesung.append(str(liste_teilaufg[i]) +
                               r') \quad \mathrm{Hier~die~Lösung~für~geometr.~Folge} --> a_2 / a_1 = ... usw.')
            else:
                loesung.append(str(liste_teilaufg[i]) +
                               r') \quad \mathrm{Hier~die~Lösung~für~arithm.~Folge} '
                               r'--> a_2 - a_1 = ... und a_2 / a_1 = ...')
            i += 1

        if c in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Nenne das Bildungsgesetz der Zahlenfolge. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad a_n~=~' + a_n_str + r' \quad (2P)')
            i += 1

        return aufgabe, loesung

    Aufgabe_1, Loesung_1 = folgen(1, [a, b, c])

    # Angaben für den Test im pdf-Dokument

    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '11'
    Lehrer = 'Herr Herrys'

    Art = 'HAK 20 - Folgen und Bildungsvorschrift'
    Teil = f'Gruppe {buchstabe}'

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

        for elements in Aufgabe_1:
            if '~' in elements:
                with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            else:
                Aufgabe.append(elements)

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'HAK 20 - Folgen und Bildungsvorschrift {Teil}', clean_tex=true)

    # Erwartungshorizont

    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)

        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

        for elements in Loesung_1:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            else:
                Loesung.append(elements)

        Loesung.generate_pdf(f'HAK 20 - Folgen und Bildungsvorschrift {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


for buchstabe in ['A', 'B']:
    erstellen(buchstabe)
