import datetime
import string
import time
import numpy as np
import random, math
from funktionen import *
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from plotten import *
from sympy.plotting import plot as symplot

# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def erstellen(Teil, in_tagen: int = 0):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def exponentialfunktionen_01(nr, teilaufg):
        i = 0
        extrema_xwert = zzahl(1,3)
        extrema_ywert = zzahl(1,3)
        if extrema_xwert > 0:
            y_vers = -1*nzahl(0,2)
        else:
            y_vers = nzahl(0,2)
        print(extrema_xwert), print(extrema_ywert), print(y_vers)

        # rekonstruktion der exponentialfunktion
        fkt_v = exp(b*x+2)*a*x**2
        fkt_a1 = diff(fkt_v,x)
        gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
        gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
        lsg = solve((gleichung1,gleichung2),(a,b))
        lsg_a = lsg[0][0]
        lsg_b = lsg[0][1]
        print(lsg)
        fkt = exp(lsg_b*x+2)*lsg_a*x**2 + y_vers
        fkt_str = (vorz_v_aussen(lsg_a,'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b,'x+2') + '}'
                   + vorz_str(y_vers))


        # Werte für Angaben zum Zeichnen des Graphen
        ywerte = [(element,fkt.subs(x,element)) for element in range(-5,6)]
        wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
        xmin = wertebereich[0]
        xmax = wertebereich[-1]
        print(fkt), print(ywerte), print(wertebereich), print(xmin), print(xmax)
        graph_xyfix(fkt)

        # Ableitung der Funktionen
        fkt_a1 = diff(fkt,x)
        fkt_a2 = diff(fkt, x,2)
        fkt_a3 = diff(fkt, x,3)

        fkt_a1_str = (r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \Big(' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                      + vorz_v_innen(2*lsg_a,'x' + r' \Big)'))
        fkt_a2_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                      + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                      + vorz_str(2*lsg_a) + r' \Big)')
        fkt_a3_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \Big('
                      + vorz_v_aussen(lsg_a * lsg_b**3, 'x^2') + vorz_v_innen(6 * lsg_a * lsg_b**2, 'x')
                      + vorz_str(6*lsg_a*lsg_b) + r' \Big)')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
                   r' f(x)~=~' + fkt_str]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['','','']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

            grenzwert_min = limit(fkt, x, -oo)
            grenzwert_pos = limit(fkt, x, oo)
            print(grenzwert_min), print(grenzwert_pos)

            aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                           + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                           + fkt_str + '~=~' + latex(grenzwert_min) + r' \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' in teilaufg:
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            if y_vers == 0:
                punkte_aufg = 4
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Schnittpunkte der'
                                                        f' Funktion f mit den Achsen. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                               + r' \hspace{10em} \\ \mathrm{Ansatz:~f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                               + r' \quad da~e^{' + vorz_v_innen(lsg[0][1],'x+2') + r'} ~immer~ \neq 0'
                               + r' \quad \to \quad ' + (vorz_v_innen(lsg[0][0],'x^2'))
                               + r'~=~ 0} \quad \vert \div ' + gzahl_klammer(lsg[0][0]) + r' \quad \vert \sqrt{~} \\'
                               + r' x~=~0 \quad \to \quad S_y ~=~ S_x (0 \vert 0) \quad (4P) \\'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            else:
                punkte_aufg = 2
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechne den Schnittpunkt der'
                                                        f' Funktion f mit der y-Achse. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Schnittpunkt~mit~der~y-Achse:}'
                               + r' \mathrm{Ansatz:~f(0)~=~ ' + gzahl(y_vers)
                               + r' \quad \to \quad S_y (0 \vert ' + gzahl(y_vers) + r')} \quad (2P) \\'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad f^{ \prime }(x) ~=~' + fkt_a1_str
                           + r' \quad f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_a3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'd' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

            if fkt_a2.subs(x,0) < 0:
                lsg_extrema1 = r'~<~0~ \to HP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2P)'
            elif fkt_a2.subs(x,0) > 0:
                lsg_extrema1 = r'~>~0~ \to TP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2P)'
            else:
                lsg_extrema1 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'

            if fkt_a2.subs(x,-2/lsg_b) < 0:
                lsg_extrema2 = (r'~<~0~ \to HP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                                + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2P)')
            elif fkt_a2.subs(x,-2/lsg_b) > 0:
                lsg_extrema2 = (r'~>~0~ \to TP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                                + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2P)')
            else:
                lsg_extrema2 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'


            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne die Extrema der Funktion f und deren Art'
                                                    ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad 0 ~=~ f^{ \prime }(x) ~=~'
                           + fkt_a1_str + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                           + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                           + vorz_v_innen(2*lsg_a,'x') + r'\quad (3P) \\'
                           + r'0~=~x \cdot \Big(' + vorz_v_aussen(lsg_a*lsg_b,'x')
                           + vorz_v_innen(2*lsg_a,r' \Big)')
                           + r' \quad \to \quad x_1~=~0 \quad \mathrm{und} \quad 0~=~ '
                           + vorz_v_aussen(lsg_a*lsg_b,'x') + vorz_v_innen(2*lsg_a,'') + r' \quad \vert \div '
                           + gzahl_klammer(lsg_a*lsg_b) + r' \quad \to \quad 0~=~x' + vorz_str(2/lsg_b)
                           + r' \quad \to \quad x_2~=~' + gzahl(-2/lsg_b) + r' \quad (3P) \\'
                           + r' f^{ \prime \prime }(0) ~=~ ' + gzahl(N(fkt_a2.subs(x,0),2)) + lsg_extrema1
                           + r' \quad \mathrm{und} \quad f^{ \prime \prime }(' + gzahl(-2/lsg_b) + ') ~=~ '
                           + gzahl(N(fkt_a2.subs(x,-2/lsg_b),2)) + lsg_extrema2 + r' \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'e' in teilaufg:
            punkte_aufg = 10
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

            xwert_wp1 = -2 / lsg_b - sqrt(2) / abs(lsg_b)
            xwert_wp2 = -2/lsg_b + sqrt(2)/abs(lsg_b)

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Wendepunkte der Funktion f. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad 0 ~=~ f^{ \prime \prime }(x) ~=~' + fkt_a2_str
                           + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                           + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2')
                           + vorz_v_innen(4 * lsg_a*lsg_b, 'x') + vorz_str(2*lsg_a) + r' \quad \vert \div '
                           + gzahl_klammer(lsg_a*lsg_b**2) + r' \quad (3P) \\'
                           + r' 0 ~=~ x^2 ' + vorz_v_innen(4/lsg_b, 'x') + vorz_str(2/lsg_b**2)
                           + r' \quad \to \quad x_{1/2} ~=~  - \frac{' + gzahl_klammer(4/lsg_b)
                           + r'}{2} \pm \sqrt{ \Big( \frac{' + gzahl_klammer(4/lsg_b) + r'}{2} \Big)^2'
                           + vorz_str(-2/lsg_b**2) + r'} ~=~ ' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(abs(sqrt(2)/lsg_b))
                           + '~=~' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(N(abs(sqrt(2)/lsg_b),3)) + r' \quad (2P) \\'
                           + r' x_1 ~=~ ' + gzahl(N(xwert_wp1,3)) + r' \quad \mathrm{und} \quad x_2 ~=~'
                           + gzahl(N(xwert_wp2,3)) + r' \quad (1P) \\'
                           + r' f^{ \prime \prime \prime }(' + gzahl(N(xwert_wp1,3)) + ') ~=~ '
                           + gzahl(N(fkt_a3.subs(x,xwert_wp1),3)) + r' \neq 0 \quad \to \quad WP(~'
                           + gzahl(N(xwert_wp1,3)) + r'~ \vert ~ '
                           + gzahl(N(fkt.subs(x,xwert_wp1),3))
                           + r') \quad (2P) \\ f^{ \prime \prime \prime }('
                           + gzahl(N(xwert_wp2,3)) + ') ~=~ '
                           + gzahl(N(fkt_a3.subs(x,xwert_wp2),3)) + r' \neq 0 \quad \to \quad WP(~'
                           + gzahl(N(xwert_wp2,2)) + r'~ \vert ~ '
                           + gzahl(N(fkt.subs(x, xwert_wp2),2)) + r') \quzad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
            i += 1

        if 'f' in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

            xwert_wp1 = N(-2/lsg_b - sqrt(2)/abs(lsg_b), 3)
            ywert_wp1 = N(fkt.subs(x,-2/lsg_b - sqrt(2)/abs(lsg_b)), 3)
            ywert_wp1 = N(fkt.subs(x, xwert_wp1),3)
            ywert_wp1_fkt_a1 = N(fkt_a1.subs(x, xwert_wp1),3)

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechne die Tangente und Normale am Wendepunkt '
                                                    f'WP({xwert_wp1}|{ywert_wp1}). \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                           r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(ywert_wp1_fkt_a1,'(x')
                           + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(ywert_wp1_fkt_a1,'x')
                           + vorz_str(N(-1*ywert_wp1_fkt_a1*xwert_wp1 + ywert_wp1,3))
                           + r' \quad (3P) \\ n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                           r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1/ywert_wp1_fkt_a1,'(x')
                           + vorz_v_innen(-1 * N(xwert_wp1,3),')') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(-1/ywert_wp1_fkt_a1,'x')
                           + vorz_str(N(xwert_wp1/ywert_wp1_fkt_a1 + ywert_wp1,3))
                           + r' \quad (3P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte}')
            i += 1


        if 'g' in teilaufg:
            punkte_aufg = 5
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}. {str(liste_teilaufg[i])})')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}',''))
            Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichne den Graphen im Intervall I({xmin}|{xmax}). \n\n')
            loesung.extend(('Abbildung', str(liste_teilaufg[i])
                             + r') \quad \mathrm{Punkte~für~Koordinatensystem~2P,~Werte~2P,~Graph~1P} \\'))
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [exponentialfunktionen_01(1, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])]
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
    Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d.%m.%Y')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = '3. Test (2. Semester)'
    Titel = 'Kurvendiskussionen einer Exponentialfunktion'

    # der Teil in dem die PDF-Datei erzeugt wird
    @timer
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))  # fügt das Package 'amsfonts' hinzu, für das \mathbb{R} für reelle Zahlen
        # erste Seite
        table1 = Tabular('|p{1.2cm}|p{2cm}|p{2cm}|p{2cm}|p{1.5cm}|p{5cm}|', row_height=1.2)
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

    # Erwartungshorizont
    @timer
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
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='300px')
                else:
                    Loesung.append(elements)
                k += 1

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 1
probe = True
datum_delta = 1  # in zukünftigen Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1), datum_delta)
    else:
        erstellen(f'Gr. {alphabet[teil_id]}', datum_delta)
    print()  # Abstand zwischen den Arbeiten (im Terminal)
