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
    print(f'\n\033[1;35m{Teil}\033[0m')

    def kurvendiskussion(nr, teilaufg):
        i = 0
        Punkte = 0
        grafik = False

        auswahl = random.choice(['rationale_Nst', 'irrationale_Nst'])
        if auswahl == 'rationale_Nst':
            nst_f_1 = zzahl(0,2)
            nst_f_2 = nst_f_1 + nzahl(1, 2) + 0.5
            nst_f_3 = nst_f_1 - nzahl(2, 3) - 0.5
            faktor_f = zzahl(2,8) / 2

            fkt_f = expand(faktor_f * (x - nst_f_1) * (x - nst_f_2) * (x - nst_f_3))
            fkt_f_a1 = faktor_f
            fkt_f_a2 = -1 * faktor_f * (nst_f_1 + nst_f_2 + nst_f_3)
            fkt_f_a3 = faktor_f * ((nst_f_1 * nst_f_2) + (nst_f_1 * nst_f_3) + (nst_f_2 * nst_f_3))
            fkt_f_a4 = -1 * faktor_f * nst_f_1 * nst_f_2 * nst_f_3

            fkt_f_partial = expand(faktor_f * (x - nst_f_2) * (x - nst_f_3))
            fkt_f_partial_pq = expand((x - nst_f_2) * (x - nst_f_3))
            fkt_f_partial_p = -1 * (nst_f_2 + nst_f_3)
            fkt_f_partial_q = (nst_f_2 * nst_f_3)

            fkt_f_1 = expand(diff(fkt_f, x, 1))
            fkt_f_1_pq = 'x^2' + vorz_str(Rational(-2 * (nst_f_1 + nst_f_2 + nst_f_3), 3)) + \
                         'x~' + vorz_str(Rational((nst_f_1 * (nst_f_2 + nst_f_3)) + (nst_f_2 * nst_f_3), 3))
            p_fkt_f_1_pq = Rational(-2 * (nst_f_1 + nst_f_2 + nst_f_3), 3)
            q_fkt_f_1_pq = Rational((nst_f_1 * (nst_f_2 + nst_f_3)) + (nst_f_2 * nst_f_3), 3)
            s_fkt_f = -1 * faktor_f * nst_f_1 * nst_f_2 * nst_f_3

        else:
            nst_f_1 = zzahl(0,2)
            quadr_nst_23 = nzahl(2, 25)
            nst_f_2 = math.sqrt(quadr_nst_23)
            nst_f_3 = -1 * nst_f_2
            faktor_f = zzahl(2,8) / 2

            fkt_f = expand(faktor_f * (x - nst_f_1) * (x - nst_f_2) * (x - nst_f_3))
            fkt_f_a1 = faktor_f
            fkt_f_a2 = -1 * faktor_f * nst_f_1
            fkt_f_a3 = faktor_f * (-1 * quadr_nst_23)
            fkt_f_a4 = faktor_f * nst_f_1 * quadr_nst_23

            fkt_f_partial = faktor_f * (x ** 2 - quadr_nst_23)
            fkt_f_partial_pq = x ** 2 - quadr_nst_23
            fkt_f_partial_p = 0
            fkt_f_partial_q = -1 * quadr_nst_23

            fkt_f_1 = expand(diff(fkt_f, x, 1))
            fkt_f_1_pq = 'x^2' + vorz_str(Rational(-2 * nst_f_1, 3)) + \
                         'x~' + vorz_str(Rational(quadr_nst_23, -3))
            p_fkt_f_1_pq = Rational((-2 * nst_f_1), 3)
            q_fkt_f_1_pq = Rational(-1 * quadr_nst_23, 3)
            s_fkt_f = faktor_f * nst_f_1 * quadr_nst_23

        fkt_f_b2 = nst_f_1 * fkt_f_a1
        fkt_f_c2 = fkt_f_a2 + fkt_f_b2
        fkt_f_b3 = nst_f_1 * fkt_f_c2
        fkt_f_c3 = fkt_f_a3 + fkt_f_b3
        fkt_f_b4 = nst_f_1 * fkt_f_c3
        fkt_f_c4 = fkt_f_a4 + fkt_f_b4

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:',
                   r' f(x)~=~' + latex(fkt_f)]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        if a in teilaufg:
            grenzwert_f_min = limit(fkt_f, x, -oo)
            grenzwert_f_pos = limit(fkt_f, x, oo)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + latex(fkt_f) + '~=~'
                           + latex(grenzwert_f_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                           + latex(fkt_f) + '~=~' + latex(grenzwert_f_min) + r' \quad (2P) \\\\')
            Punkte += 2
            i += 1

        if b in teilaufg:
            fkt_f_sym = fkt_f.subs(x, -x)
            if fkt_f_sym == fkt_f:
                lsg = (r') \quad f(-x)~=~' + latex(fkt_f_sym) + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3P) \\\\')
            elif fkt_f_sym == -1 * fkt_f:
                lsg = (r') \quad f(-x)~=~' + latex(fkt_f_sym) + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3P) \\\\')
            else:
                lsg = (r') \quad f(-x)~=~' + latex(fkt_f_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad'
                                                         r'\mathrm{nicht~symmetrisch} \quad (3P) \\\\')
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + lsg)

            Punkte += 3
            i += 1

        if c in teilaufg:
            table2 = Tabular('c|c|c|c', row_height=1.2)
            table2.add_row(' ', fkt_f_a2, fkt_f_a3, fkt_f_a4)
            table2.add_hline(1, 4)
            table2.add_row(' ', fkt_f_b2, fkt_f_b3, fkt_f_b4)
            table2.add_hline(1, 4)
            table2.add_row(fkt_f_a1, fkt_f_c2, fkt_f_c3, fkt_f_c4)

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i])+ r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + latex(fkt_f)
                                             + r' \quad \mathrm{durch~probieren:~x_1~=~}' + latex(nst_f_1)
                                             + r' \quad (2P) \\')
            loesung.append('(' + latex(fkt_f) + r')~ \div ~(x' + vorz_str(-1 * nst_f_1) + ')~=~'
                           + latex(fkt_f_partial) + r' \quad (4P) \\')
            loesung.append(latex(fkt_f_partial) + r'~=~0 \quad \vert ~ \div ' + vorz_str_minus(faktor_f) +
                          r' \quad \to \quad 0~=~' + latex(fkt_f_partial_pq) + r' \quad (2P) \\')
            loesung.append(r' x_{2/3}~=~ - \frac{' + vorz_str_minus(fkt_f_partial_p) + r'}{2} \pm \sqrt{ \Big(' +
                          r' \frac{' + latex(fkt_f_partial_p) + r'}{2} \Big)^2-' + vorz_str_minus(fkt_f_partial_q) +
                          r'} \quad (2P) \\')
            loesung.append(r' x_2~=~' + latex(round(nst_f_2, 3)) + r' \quad \mathrm{und} \quad x_3~=~' +
                          latex(round(nst_f_3, 3)) + r' \quad (2P) \\')
            loesung.append(r'S_{x_1}(' + latex(nst_f_1) + r'\vert 0) \quad S_{x_2}(' + latex(round(nst_f_2, 3))
                           + r' \vert 0) \quad S_{x_3}(' + latex(round(nst_f_3, 3)) + r' \vert 0) \quad  S_y(0 \vert ' +
                           latex(s_fkt_f) + r') \quad (4P) \\\\')

            Punkte += 16
            i += 1

        if d in teilaufg:
            x_12_fkt_f_1 = solve(fkt_f_1, x)
            x_1_fkt_f_1 = round(x_12_fkt_f_1[0], 3)
            x_2_fkt_f_1 = round(x_12_fkt_f_1[1], 3)

            fkt_f_2 = expand(diff(fkt_f, x, 2))
            fkt_f_2_str = latex(6 * faktor_f) + 'x~' + vorz_str(-2 * faktor_f * (nst_f_1 + nst_f_2 + nst_f_3))
            fkt_f_3 = expand(diff(fkt_f, x, 3))

            print('x_1: ' + str(nst_f_1))
            print('x_2: ' + str(nst_f_2))
            print('x_3: ' + str(nst_f_3))
            print('Funktion: f(x)=' + str(fkt_f))
            print('1. Ableitung: f_1(x)=' + str(fkt_f_1))
            print('pq - Form: 0=' + str(fkt_f_1_pq))
            print('p-Wert 1. Ableitung: ' + str(p_fkt_f_1_pq))
            print('q-Wert 1. Ableitung: ' + str(q_fkt_f_1_pq))
            print('Loesung der pq-Formel -> x_1=' + str(x_1_fkt_f_1))
            print('Loesung der pq-Formel -> x_2=' + str(x_2_fkt_f_1))
            print('2. Ableitung: ' + str(fkt_f_2))
            print('3. Ableitung: f_1(x)=' + str(fkt_f_3))

            if fkt_f_2.subs(x, x_1_fkt_f_1) < 0:
                loesung_f_monotonie_1 = (r'~<~0~ \to HP(~' + latex(x_1_fkt_f_1) + r'~ \vert ~'
                                        + latex(round(fkt_f.subs(x, x_1_fkt_f_1), 3)) + r') \quad (3P) \\')
            else:
                loesung_f_monotonie_1 = (r'~>~0~ \to TP(~' + latex(x_1_fkt_f_1) + r'~ \vert ~'
                                        + latex(round(fkt_f.subs(x, x_1_fkt_f_1), 3)) + r') \quad (3P) \\')

            if fkt_f_2.subs(x, x_2_fkt_f_1) < 0:
                loesung_f_monotonie_2 = (r'~<~0~ \to HP(~' + latex(x_2_fkt_f_1) + r'~ \vert ~'
                                        + latex(round(fkt_f.subs(x, x_2_fkt_f_1), 3)) + r') \quad (3P) \\\\')
            else:
                loesung_f_monotonie_2 = (r'~>~0~ \to TP(~' + latex(x_2_fkt_f_1) + r'~ \vert ~'
                                        + latex(round(fkt_f.subs(x, x_2_fkt_f_1), 3)) + r') \quad (3P) \\\\')

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrema der Funktion f und deren Art'
                                              ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') f^{ \prime }(x) ~=~' + latex(fkt_f_1)
                           + r' \quad f^{ \prime \prime }(x) ~=~' + latex(fkt_f_2)
                           + r' \quad f^{ \prime \prime \prime } (x) ~=~' + latex(fkt_f_3) + r' \quad (3P) \\')
            loesung.append(r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + latex(fkt_f_1) + r' \vert ~ \div '
                           + vorz_str_minus(3 * faktor_f) + r' \quad (1P) \\')
            loesung.append(r' 0~=~ ' + fkt_f_1_pq + r' \quad \to \quad ' + r' x_{1/2}~=~ - \frac{'
                           + vorz_str_minus(p_fkt_f_1_pq) + r'}{2} \pm \sqrt{ \Big(' + r' \frac{'
                           + latex(p_fkt_f_1_pq) + r'}{2} \Big)^2-' + vorz_str_minus(q_fkt_f_1_pq) + r'} \quad (3P) \\')
            loesung.append(r'x_1~=~' + latex(x_1_fkt_f_1) + r' \quad \mathrm{und} \quad x_2~=~'
                           + latex(x_2_fkt_f_1) + r' \quad (2P) \\')
            loesung.append(r' f^{ \prime \prime }(' + latex(x_1_fkt_f_1) + ')~=~'
                           + latex(round(fkt_f_2.subs(x, x_1_fkt_f_1), 3)) + loesung_f_monotonie_1)
            loesung.append(r' f^{ \prime \prime }(' + latex(x_2_fkt_f_1) + ')~=~'
                           + latex(round(fkt_f_2.subs(x, x_2_fkt_f_1), 3)) + loesung_f_monotonie_2)
            Punkte += 15
            i += 1

        if e in teilaufg:
            xwert_Wendepunkt = Rational(2 * faktor_f * (nst_f_1 + nst_f_2 + nst_f_3), 6 * faktor_f)
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die möglichen Wendepunkte der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_f_2_str + r' \quad \vert ~-~' + vorz_str_minus(-2 * faktor_f * (nst_f_1 + nst_f_2 + nst_f_3))
                           + r' \quad \vert \div ' + vorz_str_minus(6 * faktor_f) + r' \quad \to \quad x_1~=~'
                           + latex(xwert_Wendepunkt) + r' \quad (2P) \\')
            loesung.append(r' f^{ \prime \prime \prime }(' + latex(xwert_Wendepunkt) + r') \quad \neq 0 \quad \to \quad WP('
                           + latex(xwert_Wendepunkt) + r' \vert ' + latex(round(fkt_f.subs(x, xwert_Wendepunkt), 3))
                           + r') \quad (3P) \\\\')
            Punkte += 5
            i += 1
        if f in teilaufg:
            xmin_f = round(nst_f_3 - 0.4, 0)
            xmax_f = round(nst_f_2 + 0.4, 0)
            xwerte = np.arange(xmin_f,xmax_f,0.01)
            ywerte = [fkt_f.subs(x, elements) for elements in xwerte]
            # plot(fkt_f, (x,xmin_f,xmax_f) ,show=False)
            fig, ax = plt.subplots()
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
            plt.plot(xwerte,ywerte)
            plt.grid(True)
            plt.savefig(f'Aufgabe_{nr}', dpi=200)
            grafik = f'Aufgabe_{nr}'
            plt.figure().clear()
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen von f im Intervall [{xmin_f};{xmax_f}].')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~folgende~Abbildung~zeigt~die~Lösung.~(5P)}')

            Punkte += 5
            i += 1

        return [aufgabe, loesung, Punkte, grafik]

    aufgaben = [kurvendiskussion(1, [a,b,c,d,e,f])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'HAK 06 - Kurvendiskussion von Polynomen'

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

        if loesung[3] == False:
            pass
        else:
            with Loesung.create(Figure(position='h!')) as graph:
                graph.add_image(loesung[3], width='250px')

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))


        Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()

anzahl_HAKs = 2
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')