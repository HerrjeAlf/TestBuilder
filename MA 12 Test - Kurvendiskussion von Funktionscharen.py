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
        nst_2 = nst_1 + nzahl(2, 8) / 2
        nst_3 = nst_1 - nzahl(2, 8) / 2
        while nst_3 == 0:
            nst_3 = nst_1 - nzahl(2, 8) / 2
        faktor = zzahl(3, 8) / 2
        # Aufstellen der Funktionsgleichung
        fkt = collect(expand(faktor * (x - nst_1) * (x - a) * (x - nst_3)),x)
        # Koeffizienten der Funktion
        fkt_a3 = faktor
        fkt_a2 = -1* (faktor*a + faktor*(nst_1 + nst_3))
        fkt_a1 = (faktor*(nst_1 + nst_3)*a + faktor*nst_1*nst_3)
        fkt_a0 = -1*faktor*nst_1*nst_3*a

        # Koeffizienten der Funktion als String und der richtigen Darstellung
        fkt_a3_str = latex(faktor)
        if faktor < 0:
            fkt_a2_str = '+(' + latex(abs(faktor)) + r' \cdot a ' + vorz_str(-1*faktor*(nst_1 + nst_3)) + ')'
        else:
            fkt_a2_str = '-(' + latex(abs(faktor)) + r' \cdot a ' + vorz_str(faktor*(nst_1 + nst_3)) + ')'

        if faktor*(nst_1 + nst_3) < 0:
            fkt_a1_str = '-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(-1*faktor * nst_1 * nst_3) + ')'
        else:
            fkt_a1_str = '+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(faktor * nst_1 * nst_3) + ')'
        fkt_a0_str = vorz_str(-1*faktor*nst_1*nst_3) + r' \cdot a'

        fkt_str = fkt_a3_str + r' \cdot x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str + r' \cdot x ~' + fkt_a0_str

        print(fkt), print(fkt_str)

        if nst_1 < 0:
            db_bereich = r'\mathrm{mit~a \in \Re ~und~ a > 0}'
        else:
            db_bereich = r'\mathrm{mit~a \in \Re ~und~ a > ' + latex(nst_1) + '}'

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:',
                   r' f(x)~=~' + latex(fkt_str) + r' \quad ' + db_bereich]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']



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

        if b in teilaufg:
            fkt_a3_str_neg = latex(-1*faktor)
            if faktor * (nst_1 + nst_3) > 0:
                fkt_a1_str_neg = '+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(
                    -1 * faktor * nst_1 * nst_3) + ')'
            else:
                fkt_a1_str_neg = '+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a' + vorz_str(
                    faktor * nst_1 * nst_3) + ')'
            fkt_sym = (fkt_a3_str_neg + r' \cdot x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str_neg
                       + r' \cdot x ~' + fkt_a0_str)
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad f(-x)~=~' + latex(fkt_sym)
                                                     + r' \neq  f(x)  \neq -f(x) \quad \to \quad '
                                                       r'\mathrm{nicht~symmetrisch} \quad (3P) \\\\'))

        if c in teilaufg:

            table2 = Tabular('c|c|c|c', row_height=1.2)
            table2.add_row(' ', fkt_a2, fkt_a1, fkt_a0)
            table2.add_hline(1, 4)
            table2.add_row(' ', fkt_f_b2, fkt_f_b3, fkt_f_b4)
            table2.add_hline(1, 4)
            table2.add_row(fkt_a3, fkt_f_c2, fkt_f_c3, fkt_f_c4)

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f. \n\n')
            loesung.append(
                str(liste_teilaufg[i]) + r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + latex(fkt_f)
                + r' \quad \mathrm{durch~probieren:~x_1~=~}' + latex(nst_f_1)
                + r' \quad (2P) \\')
            loesung.append('(' + latex(fkt_f) + r')~ \div ~(x' + vorz_str(-1 * nst_f_1) + ')~=~'
                           + latex(fkt_f_partial) + r' \quad (4P) \\')
            loesung.append(table2)
            loesung.append(r'\hspace{10em} \\')
            loesung.append(latex(fkt_f_partial) + r'~=~0 \quad \vert ~ \div ' + vorz_str_minus(faktor_f) +
                           r' \quad \to \quad 0~=~' + latex(fkt_f_partial_pq) + r' \quad (2P) \\')
            loesung.append(r' x_{2/3}~=~ - \frac{' + vorz_str_minus(fkt_f_partial_p) + r'}{2} \pm \sqrt{ \Big(' +
                           r' \frac{' + latex(fkt_f_partial_p) + r'}{2} \Big)^2-' + vorz_str_minus(fkt_f_partial_q) +
                           r'} \quad (2P) \\')
            loesung.append(r' x_2~=~' + latex(round(nst_f_2, 3)) + r' \quad \mathrm{und} \quad x_3~=~' +
                           latex(round(nst_f_3, 3)) + r' \quad (2P) \\')
            loesung.append(r'S_{x_1}(' + latex(nst_f_1) + r'\vert 0) \quad S_{x_2}(' + latex(round(nst_f_2, 3))
                           + r' \vert 0) \quad S_{x_3}(' + latex(round(nst_f_3, 3)) + r' \vert 0)')
            if nst_f_1 == 0 or nst_f_2 == 0 or nst_f_3 == 0:
                loesung.append(r' \quad (3P) \\\\')
                Punkte += 15
            else:
                loesung.append(r' \quad S_y(0 \vert' + latex(s_fkt_f) + r') \quad (4P) \\\\')
                Punkte += 16
            i += 1

            print(fkt)
            print(fkt_sym)

            Punkte += 3
            i += 1

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