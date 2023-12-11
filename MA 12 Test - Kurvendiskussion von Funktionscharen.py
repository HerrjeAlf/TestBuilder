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
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

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
        pass

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
    print(f'\n\033[1;35m{Teil}\033[0m')

    def kurvendiskussion(nr, teilaufg):
        i = 0
        Punkte = 0
        # Berechnung der Nullstellen und des Faktors
        nst_1 = zzahl(1, 5)
        nst_2 = nst_1 + nzahl(2, 8)/2
        nst_3 = nst_1 - nzahl(1, 8)/2
        faktor = zzahl(3, 8) / 2
        # Aufstellen der Funktionsgleichung
        fkt = expand(faktor * (x - nst_1) * (x - nst_2) * (x - a))
        # Koeffizienten der Funktion
        fkt_a3 = faktor
        fkt_a2 = (faktor*(-1)*(nst_1 + nst_2) - a*faktor)
        fkt_a1 = (a*faktor*(nst_1 + nst_2) + faktor*nst_1*nst_2)
        fkt_a0 = -1*faktor*nst_1*nst_2

        fkt_str = (latex(fkt_a3) + 'x^3 ~' + vorz(-1 * faktor / abs(faktor)) + '(' + latex(nst_1+nst_2*abs(faktor))
                   + vorz_str(abs(faktor)) + 'a) \cdot x^2 ~' + vorz(faktor/abs(faktor)) + '('
                   + latex(abs(faktor)*(nst_1 + nst_2)) + r'a' + vorz_str(nst_1*nst_2*abs(faktor))
                   + r') \cdot x ~' + vorz_str(-1*faktor*nst_1*nst_2))

        print(fkt)
        print(fkt_str)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:',
                   r' f(x)~=~' + latex(fkt_str) + r' \quad \mathrm{mit~a \in \Re ^{ + } }']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafik = 'Aufgabe ' + str(nr)

        if a in teilaufg:
            grenzwert_neg = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + latex(fkt_str) + '~=~' + \
                           latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} ' + \
                           latex(fkt) + '~=~' + latex(grenzwert_neg) + r' \quad (2P) \\\\')
            Punkte += 2
            i += 1
        print(grenzwert_pos)
        print(grenzwert_neg)

        return [aufgabe, loesung, Punkte, grafik]

    aufgaben = [kurvendiskussion(1, [a,b])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'Test - Kurvendiskussion von Polynomen'

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

        Aufgabe.append(LargeText(bold(f'\n {Art} \n\n')))
        for aufgabe in aufgaben:
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[3], width='200px')
                else:
                    Aufgabe.append(elements)

        Aufgabe.append('\n\n')
        Aufgabe.append(
            MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'{Art} {Teil}', clean_tex=true)

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

        for loesung in aufgaben:
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3], width='200px')
                else:
                    Loesung.append(elements)

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))


        Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    # Hausaufgabenkontrolle()
    # Erwartungshorizont()

anzahl_HAKs = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')