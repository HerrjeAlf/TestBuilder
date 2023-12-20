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
            db_bereich = r' \mathrm{mit~a \in \Re ~und~ a > 0}'
        else:
            db_bereich = r' \mathrm{mit~a \in \Re ~und~ a > ' + latex(nst_1) + r'}'

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:']
        aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad ' + db_bereich)
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']



        if a in teilaufg:
            grenzwert_neg = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~' + \
                           latex(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} ' + \
                           fkt_str + '~=~' + latex(grenzwert_neg) + r' \quad (2P) \\\\')
            Punkte += 2
            i += 1

        if b in teilaufg:
            fkt_a3_str_neg = latex(-1*faktor)
            if faktor * (nst_1 + nst_3) > 0:
                fkt_a1_str_neg = ('-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                  + vorz_str(-1*faktor * nst_1 * nst_3) + ')')
            else:
                fkt_a1_str_neg = ('+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                  + vorz_str(faktor * nst_1 * nst_3) + ')')
            fkt_sym = (fkt_a3_str_neg + r' \cdot x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str_neg
                       + r' \cdot x ~' + fkt_a0_str)
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad f(-x)~=~' + fkt_sym
                                                     + r' \neq  f(x)  \neq -f(x) \\'
                                                       r'\mathrm{nicht~symmetrisch} \quad (3P) \\'))
            Punkte += 3
            i += 1

        if c in teilaufg:
            # hier werden die Koeffizenten für das Hornerschema berechnet
            fkt_b2 = nst_1 * faktor
            fkt_c2 = -1 * faktor * a - faktor * nst_3
            fkt_b1 = -1 * faktor * nst_1 * a - faktor * nst_1 * nst_3
            fkt_c1 = faktor * nst_3 * a
            fkt_b0 = faktor * nst_1 * nst_3 * a

            fkt_partial = faktor * x**2 + fkt_c2 *x + fkt_c1

            # hier werden die Koeffizenten als String für das Hornerschema berechnet
            if faktor < 0:
                fkt_c2_str = '+(' + latex(-1*faktor) + r' \cdot a' + vorz_str(-1*faktor*nst_3) + r') \cdot x'
            else:
                fkt_c2_str = '-(' + latex(faktor) + r' \cdot a' + vorz_str(faktor*nst_3) + r') \cdot x'
            fkt_c1_str = vorz_str(faktor*nst_3) + r' \cdot a'

            fkt_p = -1*a - nst_3    # -(a+x_3)
            fkt_q = nst_3 * a
            fkt_disk = ((fkt_p/2)**2)-fkt_q
            fkt_p_str = '-(a' + vorz_str(nst_3) + ')'

            fkt_q_str = vorz_str(nst_3) + r' \cdot a'

            fkt_partial_str = latex(faktor) + r' \cdot x^2' + fkt_c2_str + fkt_c1_str
            fkt_pq_str = 'x^2' + fkt_p_str + r' \cdot x' + fkt_q_str
            fkt_disk_str = r' \frac{a^2' + vorz_str(-1*2*nst_3) + r' \cdot a' + vorz_str(nst_3**2) + '}{4}'



            table2 = Tabular('c c|c|c|c', row_height=1.2)
            table2.add_row('',fkt_a3,latex(collect(fkt_a2,a)), latex(collect(fkt_a1,a)), latex(collect(fkt_a0,a)))
            table2.add_hline(2, 5)
            table2.add_row('Partialpolynom mit Horner Schema berechnen: ',' ', latex(collect(fkt_b2,a)), latex(collect(fkt_b1,a)), latex(collect(fkt_b0,a)))
            table2.add_hline(2, 5)
            table2.add_row('',fkt_a3, latex(collect(fkt_c2,a)), latex(collect(fkt_c1,a)), '0')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte mit den Achsen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                                                     + fkt_str + r' \quad (1P) \\ \mathrm{durch~probieren:~x_1~=~}'
                                                     + latex(nst_1) + r' \quad (1P) \\'
                                                     + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1)
                                                     + r')~= \\ =~' + fkt_partial_str + r' \quad (4P)'))
            loesung.append(table2)
            loesung.append('0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + vorz_str_minus(faktor) +
                           r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2P) \\'
                           r' x_{2/3}~=~ - \frac{' + fkt_p_str + r'}{2} \pm \sqrt{ \Big(' +
                           r' \frac{' + fkt_p_str + r'}{2} \Big)^2-(' + latex(fkt_q) +
                           r')} ~=~ ' + latex(-1*fkt_p/2) + r' \pm \sqrt{'
                           + fkt_disk_str + r' } \quad (4P) \\ x_{2/3}~=~' + latex(-1*fkt_p/2) + r' \pm ('
                           + latex((a-nst_3)/2) + r') \quad \to \quad x_2~=~' + latex(nst_3)
                           + r' \quad \mathrm{und} \quad x_3~=~a \quad (3P) \\')

            Punkte += 15
            i += 1
        if d in teilaufg:
            fkt_1 = collect(diff(fkt,x,1),x)
            fkt_2 = collect(diff(fkt,x,2),x)
            fkt_3 = collect(diff(fkt,x,3),x)
            x_12_fkt_1 = solve(fkt_1, x)
            x_1_fkt_1 = x_12_fkt_1[0]
            x_2_fkt_1 = x_12_fkt_1[1]

            # Koeffizienten der ersten Ableitung
            fkt_1_a2 = 3*faktor
            fkt_1_a1 = (-2*faktor*a -2*faktor*(nst_1 + nst_3))
            fkt_1_a0 = (faktor*(nst_1+nst_3)*a+faktor*nst_1*nst_3)
            fkt_1_p = (-2/3*a -2/3*(nst_1*nst_3))
            fkt_1_q = (1/3*(nst_1+nst_3)*a + 1/3*nst_1*nst_3)

            fkt_1 = fkt_1_a2 * x**2 + fkt_1_a1 * x + fkt_1_a0

            # Koeffizienten der ersten Ableitung als string

            fkt_1_a2_str = latex(3*faktor)
            if faktor < 0:
                fkt_1_a1_str = '+(' + latex(-2*faktor) + r' \cdot a' + vorz_str(-2*faktor*(nst_1+nst_3)) + ')'
            else:
                fkt_1_a1_str = '-(' + latex(2*faktor) + r' \cdot a' + vorz_str(2*faktor*(nst_1+nst_3)) + ')'

            if faktor * (nst_1 + nst_3) < 0:
                fkt_1_a0_str = ('-(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
            else:
                fkt_1_a0_str = ('+(' + latex(abs(faktor * (nst_1 + nst_3))) + r' \cdot a'
                                + vorz_str(faktor * nst_1 * nst_3) + ')')
            # p und q in der pq-Formel
            fkt_1_p_str = r'-( \frac{2}{3} \cdot a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')'
            if (nst_1 + nst_3) < 0:
                fkt_1_q_str = ('-(' + latex(Rational(-1*(nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational(-1*(nst_1 * nst_3),3)) + ')')
                fkt_1_q2_str = (latex(Rational((nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)))
            else:
                fkt_1_q_str = ('+(' + latex(Rational(nst_1 + nst_3,3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)) + ')')
                fkt_1_q2_str = (latex(Rational(nst_1 + nst_3, 3)) + r' \cdot a'
                               + vorz_str(Rational((nst_1 * nst_3), 3)))

            # p und q in umgeformter pq-Formel
            fkt_1_p2_str = r'( \frac{2}{3} \cdot a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')^2'
            fkt_1_p3_str = r' \frac{1}{3} \cdot a' + vorz_str(Rational((nst_1 + nst_3), 3))
            if (nst_1 + nst_3) < 0:
                fkt_1_q3_str = (r'+ \frac{4 \cdot (' + latex(Rational(abs(nst_1 + nst_3),3)) + r' \cdot a'
                                + vorz_str(Rational(-1*(nst_1 * nst_3),3)) + ') }{4}')
            else:
                fkt_1_q3_str = (r'- \frac{4 \cdot ('+ latex(Rational(nst_1 + nst_3,3)) + r' \cdot a'
                                + vorz_str(Rational((nst_1 * nst_3),3)) + ')}{4}')
            # Diskriminante der Wurzel
            fkt_1_disk_str = (r' \frac{1}{9} \cdot ((a' + vorz_str(-1*(nst_1+nst_3)) + r')^2'
                              + vorz_str(-4*nst_1*nst_3) + ')')

            fkt_1_str = fkt_1_a2_str + 'x^2' + fkt_1_a1_str + 'x' + fkt_1_a0_str
            fkt_1_pq_str = 'x^2' + fkt_1_p_str + r' \cdot x' + fkt_1_q_str
            fkt_2_str = latex(6*faktor) + 'x' + fkt_1_a1_str
            fkt_3_str = latex(6*faktor)
            fkt_1_x1 = fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str + r'}'
            fkt_1_x2 = fkt_1_p3_str + r' - \sqrt{' + fkt_1_disk_str + r'}'





            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extremstellen der Funktion f und deren Art'
                                                    ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \quad (1P) \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad \mathrm{und} \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str
                           + r' \quad (2P) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_1_str + r' \vert ~ \div ' + vorz_str_minus(3 * faktor) + r' \quad (1P) \\'
                           r'0~=~ ' + fkt_1_pq_str + r' \quad (1P) \\' + r' x_{1/2}~=~ - \frac{'
                           + fkt_1_p_str + r'}{2} \pm \sqrt{ \Big(' + r' \frac{'
                           + fkt_1_p_str + r'}{2} \Big)^2-(' + fkt_1_q2_str + r')} \quad (2P) \\ =~ '
                           + fkt_1_p3_str + r' \pm \sqrt{' + r' \frac{' + fkt_1_p2_str
                           + r'}{4}' + fkt_1_q3_str + r'} ~=~' + fkt_1_p3_str + r' \pm \sqrt{' + fkt_1_disk_str
                           + r'} \quad (4P) \\ x_1~=~' + fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{und} \quad x_2~=~' + fkt_1_p3_str + r' - \sqrt{'
                           + fkt_1_disk_str + r'}  \quad (2P) \\'
                           + r'f^{ \prime \prime } (x_2) ~=~' + latex(6*faktor)
                           + r' \cdot \Big( ' + fkt_1_x1 + r' \Big) ' + fkt_1_a1_str
                           + r' \quad (1P) \\ ~=~ + \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{>~0} \quad \to TP \quad (2P) \\ f^{ \prime \prime } (x_2) ~=~'
                           + latex(6 * faktor) + r' \cdot \Big( ' + fkt_1_x2
                           + r' \Big) ' + fkt_1_a1_str + r' \quad (1P) \\ ~=~ - \sqrt{' + fkt_1_disk_str
                           + r'} \quad \mathrm{<~0} \quad \to HP \quad (2P)')
            Punkte += 19
            i += 1

        if e in teilaufg:
            if faktor < 0:
                fkt_1_a1_str = '+(' + latex(-2*faktor) + r' \cdot a' + vorz_str(-2*faktor*(nst_1+nst_3)) + ')'
            else:
                fkt_1_a1_str = '-(' + latex(2*faktor) + r' \cdot a' + vorz_str(2*faktor*(nst_1+nst_3)) + ')'

            if faktor < 0:
                fkt_1_a1_str_neg = '-(' + latex(-2 * faktor) + r' \cdot a' + vorz_str(-2 * faktor * (nst_1 + nst_3)) + ')'
            else:
                fkt_1_a1_str_neg = '+(' + latex(2 * faktor) + r' \cdot a' + vorz_str(2 * faktor * (nst_1 + nst_3)) + ')'
            xwert_wendepunkt = r' \frac{1}{3} \cdot a' + vorz_str(Rational((nst_1+nst_3),3))
            fkt_2_str = latex(6*faktor) + 'x' + fkt_1_a1_str
            fkt_3_str = latex(6*faktor)

            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die möglichen Wendepunkte der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_2_str + r' \quad \vert ~' + fkt_1_a1_str_neg + r' \quad \vert \div '
                           + vorz_str_minus(6 * faktor) + r' \quad (1P) \\ x_1~=~ \frac{1}{3} a'
                           + vorz_str(Rational((nst_1+nst_3),3))
                           + r' \quad (1P) \quad \to \quad f^{ \prime \prime \prime }(' + xwert_wendepunkt
                           + r') ~=~ ' + latex(6*faktor) + r' \quad \neq 0 \quad \to \quad Wendepunkt \quad (3P) \\\\')
            Punkte += 5
            i += 1

        return [aufgabe, loesung, Punkte]

    aufgaben = [kurvendiskussion(1, [a,b,c,d,e])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'HAK 08'
    Titel = 'Kurvendiskussion von Parameterfunktionen'

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
        Aufgabe.append(LargeText(bold(f'\n {Art} {Titel} \n\n')))
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

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Titel} {Teil}', clean_tex=true)

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

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


        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Titel} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()

anzahl_HAKs = 2
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')