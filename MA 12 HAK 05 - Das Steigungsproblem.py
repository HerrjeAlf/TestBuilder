import string
import numpy
import random
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
        ax.set_xlabel('West', size=10, labelpad=-24, x=1.03)
        ax.set_ylabel('Höhe', size=10, labelpad=-21, y=1.02, rotation=0)
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(numpy.linspace(0, 8, 9, endpoint=True))
        plt.yticks(numpy.linspace(1, 5, 5, endpoint=True))
        plt.axis([-1, 9, 0, 6])
        plt.plot(a, b, linewidth=2)
        plt.suptitle(titel, usetex=True)
        return plt.savefig(name, dpi=200)
    def anwendungen(nr, teilaufg):
        i = 0
        Punkte = 0
        x_wert_s = nzahl(8, 16) / 2
        y_wert_s = x_wert_s - 3
        faktor = -1 * nzahl(2, 20) / 20
        fkt = expand(faktor * (x - x_wert_s) ** 2 + y_wert_s)
        fkt_abl = diff(fkt, x, 1)
        x_wert_x0 = solve(Eq(fkt, 0), x)
        m_tangente = Rational(y_wert_s , (x_wert_s - 1))
        m_tangente_prozent = Rational(y_wert_s *100, (x_wert_s - 1))
        fkt_tangente = m_tangente * x - m_tangente
        print(fkt_tangente)
        x_wert_schnittpunkt = solve(Eq(fkt, fkt_tangente), x)
        y_wert_schnittpunkt = fkt_tangente.subs(x, x_wert_schnittpunkt[0])
        xwerte = [-1 + n / 5 for n in range(60)]
        ywerte_huegel = [fkt.subs(x, xwerte[i]) for i in range(60)]
        xwerte_gerade = [1, x_wert_schnittpunkt[0]]
        ywerte_gerade = [0, y_wert_schnittpunkt]
        plt.plot(xwerte_gerade, ywerte_gerade)
        Graph(xwerte, ywerte_huegel, x_wert_s, fkt, '$f(x) =' + latex(fkt) + '$', 'Hügel', 'Aufgabe_3')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Im Koordinatensystem auf der Rückseite ist die Profilkurve eines Hügels aufgetragen.',
                   r' f(x)~=~' + latex(fkt)]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        if a in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Fußpunkte des Hügels. \n\n')
            loesung.append(str(teilaufg[i]) + r')')

            Punkte += 3
            i += 1

        if b in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Steigung  und den Steigungswinkel am westlichen Fußpunkt. \n\n')
            loesung.append(str(teilaufg[i]) + r')')

            Punkte += 3
            i += 1

        if c in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Die Seilbahn startet bei B(1|0). Berechne den Treffpunkt mit dem Hügel, wenn die Steigung')
            aufgabe.append(r' \mathrm{m~=~}' + latex(m_tangente) + r' \mathrm{~beträgt}. \hspace{38em}')
            loesung.append(str(teilaufg[i]) + r')')

            Punkte += 3
            i += 1


        return [aufgabe, loesung, Punkte]

    aufgaben = [anwendungen(1, [a,b,c])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'HAK 05 - Anwendungen der Ableitung'

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
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
