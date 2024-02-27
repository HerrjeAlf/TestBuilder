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
from sympy.plotting import plot as symplot

from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def timer(func):
    """
    Timer-Dekorator zur Messung der Ausführungszeit einer Funktion.
    """
    def wrapper(*args, **kwargs):  # Erklärung eines Dekorators -> https://t1p.de/lqn4d
        start_time = time.perf_counter()  # Zeit vorm ausführen nehmen
        result = func(*args, **kwargs)  # Aufruf der eigentlichen Funktion mit ihren Argumenten
        end_time = time.perf_counter()  # Zeit nachm ausführen
        execution_time = end_time - start_time  # Vergangene Zeit berechnen

        if func.__name__ == 'Hausaufgabenkontrolle':
            print(f'\033[38;2;0;220;120m\033[1mKontrolle in {round(execution_time, 2)} Sekunden erstellt\033[0m')
        elif func.__name__ == 'Erwartungshorizont':
            print(f'\033[38;2;0;220;120m\033[1mErwartungshorizont in {round(execution_time, 2)} Sekunden erstellt\033[0m')
        else:
            print(f'\033[38;2;0;220;120m\033[1m{func.__name__} in {round(execution_time, 2)} Sekunden ausgeführt\033[0m')
        return result
    return wrapper

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def logarithmusgesetze(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        regeln_aufgabe = {r'\log_a(u \cdot v) ~=~ \hspace{10em}': r'\log_a(u \cdot v) ~=~ \log_a u + \log_a v',
                          r'\log_a \frac{u}{v} ~=~ \hspace{10em}': r'\log_a \frac{u}{v} ~=~ \log_a u - \log_a v',
                          r'\log_a u^r ~=~ \hspace{10em}': r'\log_a u^r ~=~ r \cdot \log_a u',
                          r'\log_a \sqrt[n]{u} ~=~ \hspace{10em}': r'\log_a \sqrt[n]{u} ~=~ \frac{1}{n} \cdot \log_a u',
                          r'\log_c b ~=~ \hspace{10em}': r'\log_c b ~=~ \frac{\log_a b}{\log_a c} ~=~ \frac{ln b}{ln c}',
                          r'a^{\log_a b} ~=~ \hspace{10em}': r'a^{\log_a b} ~=~ b',
                          r'\log_a 1 ~=~ \hspace{10em}': r'\log_a 1 ~=~ 0',
                          r'\log_a a ~=~ \hspace{10em}': r'\log_a a ~=~ 1',
                          r'\log_e ~=~ \hspace{10em}': r'\log_e ~=~ \ln',
                          r'\log_{10} ~=~ \hspace{10em}': r'\log_{10} ~=~ \lg'}
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
                           + str(liste_teilaufg[i+1]) + r') ~' + regeln_aufgabe[auswahl[i+1]] + r' \quad (1P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 2

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def exponentialgleichungen(nr, teilaufg):
        i = 0
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Lösen Sie die Exponentialgleichungen.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['', '']
        grafiken_loesung = ['']
        liste_bez.append(str(nr))
        punkte_aufg = 0

        if 'a' in teilaufg:
            # Berechnungen für Aufgabe
            basis_1 = nzahl(2,8)
            exponent_1 = nzahl(3,5)
            ergebnis_1 = basis_1 ** exponent_1
            basis_2 = nzahl(2,8)
            exponent_2 = nzahl(2,5)
            exponent_2_summe = zzahl(1,3)
            faktor = zzahl(2,30)*20
            ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_summe)
            punkte_aufg += 5
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')
            aufgabe.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1)
                           + r' \hspace{5em} ' + str(liste_teilaufg[i+1]) + r') \quad ' + gzahl(faktor) + r' \cdot '
                           + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(faktor*ergebnis_2)
                           + r' \hspace{5em}')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1)
                           + r' \quad \vert \log_{' + gzahl(basis_1) + r'} \quad \to \quad x ~=~ ' + gzahl(exponent_1)
                           + r' \quad (2P) \\' + str(liste_teilaufg[i+1]) + r') \quad ' + gzahl(faktor) + r' \cdot '
                           + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(faktor*ergebnis_2)
                           + r' \quad \vert \div ' + gzahl_klammer(faktor) + r' \quad \to \quad ' + gzahl(basis_2)
                           + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(ergebnis_2) + r' \quad \vert \log_{'
                           + gzahl(basis_2) + r'} \quad (1P) \\ x' + vorz_str(exponent_2_summe) + r' ~=~ '
                           + gzahl(exponent_2 + exponent_2_summe) + r' \quad \vert ' + vorz_str(-1 * exponent_2_summe)
                           + r' \quad \to \quad x ~=~ ' + gzahl(exponent_2) + r' \quad (2P)')
            i += 2

        if 'b' in teilaufg:
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')
            def Aufgabe_1():
                punkte = 2
                faktor_exp = zzahl(1, 8) / 2
                erg_gl = nzahl(2, 40) / 10
                aufgabe = 'e^{' + vorz_v_aussen(faktor_exp, 'x') + r'} ~=~ ' + gzahl(erg_gl)
                aufgabe_lsg = ('e^{' + vorz_v_aussen(faktor_exp,'x') + '} ~=~ ' + gzahl(erg_gl)
                               + r' \quad \vert ln() \quad \to \quad ' + vorz_gzahl(faktor_exp) + 'x ~=~ ln('
                               + gzahl(erg_gl) + r') \quad \vert \div ' + gzahl_klammer(faktor_exp)
                               + r' \quad \to \quad x~=~' + vorz_gzahl(N(log(erg_gl) / faktor_exp, 3))
                               + r' \quad (2P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_2():
                punkte = 3
                faktor_exp = zzahl(1, 8) / 2
                summand = zzahl(1,8)
                erg_gl = nzahl(2, 40) / 10
                aufgabe = 'e^{' + vorz_v_aussen(faktor_exp, 'x') + vorz_str(summand) + r'} ~=~ ' + gzahl(erg_gl)
                aufgabe_lsg = ('e^{' + vorz_v_aussen(faktor_exp, 'x') + vorz_str(summand) + '} ~=~ ' + gzahl(erg_gl)
                               + r' \quad \vert ln() \quad \to \quad ' + vorz_v_aussen(faktor_exp, 'x')
                               + vorz_str(summand) + ' ~=~ ln(' + gzahl(erg_gl) + r') \quad \vert '
                               + vorz_str(-1*summand) + r' \quad (1P) \\' + vorz_v_aussen(faktor_exp,'x')
                               + r' ~=~ ln(' + gzahl(erg_gl) + r')' + vorz_str(-1*summand) + r' \quad \vert \div '
                               + gzahl_klammer(faktor_exp) + r' \quad \to \quad x~=~'
                               + vorz_gzahl(N((log(erg_gl) - summand)/ faktor_exp, 3))
                               + r' \quad (2P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_3():
                punkte = 4
                faktor_exp_1 = zzahl(1,5)
                faktor_exp_2 = zzahl(1,5)
                while faktor_exp_1 == faktor_exp_2:
                    faktor_exp_2 = zzahl(1, 5)
                vorzeichen = random.choice([-1, 1])
                faktor_1 = vorzeichen * nzahl(1,40)
                faktor_2 = vorzeichen * nzahl(1,40)
                aufgabe = (vorz_gzahl(faktor_1/10) + 'e^{' + vorz_gzahl(faktor_exp_1) + r'x} ~=~'
                           + vorz_gzahl(faktor_2/10) + 'e^{' + vorz_gzahl(faktor_exp_2) + r'x}')
                aufgabe_lsg = (vorz_gzahl(faktor_1/10) + 'e^{' + vorz_gzahl(faktor_exp_1) + r'x} ~=~'
                               + vorz_gzahl(faktor_2/10) + 'e^{' + vorz_gzahl(faktor_exp_2) + r'x}'
                               + r' \quad \vert \div ' + gzahl_klammer(faktor_1/10) + r' \quad \to \quad '
                               + 'e^{' + vorz_gzahl(faktor_exp_1) + r'x} ~=~' + vorz_gzahl(Rational(faktor_2,faktor_1))
                               + r' \cdot e^{' + vorz_gzahl(faktor_exp_2) + r'x} \quad \vert \div e^{'
                               + vorz_gzahl(faktor_exp_2) + r'x} \quad (1P) \\'
                               + 'e^{' + vorz_gzahl(faktor_exp_1 - faktor_exp_2) + 'x} ~=~ '
                               + vorz_gzahl(Rational(faktor_2,faktor_1)) + r' \quad \vert ln() \quad \to \quad '
                               + vorz_gzahl(faktor_exp_1 - faktor_exp_2) + r'x ~=~ ln \Big('
                               + vorz_gzahl(Rational(faktor_2,faktor_1)) + r' \Big) \quad \vert \div '
                               + gzahl_klammer(faktor_exp_1 - faktor_exp_2) + r' \quad \to \quad x ~=~'
                               + gzahl(N(log(faktor_2/faktor_1)/(faktor_exp_1 - faktor_exp_2),3))
                               + r' \quad (3P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_4():
                punkte = 3
                faktor_exp_1 = zzahl(2, 8)
                faktor_exp_2 = zzahl(2, 8)
                summand = zzahl(1,7)
                while faktor_exp_1 == faktor_exp_2:
                    faktor_exp_2 = zzahl(1, 5)
                aufgabe = (r' ln(x^{' + gzahl(faktor_exp_1) + r'}) ~=~ ln(x^{' + gzahl(faktor_exp_2) + '})'
                           + vorz_str(summand))
                aufgabe_lsg = (r' ln(x^{' + gzahl(faktor_exp_1) + r'}) ~=~ ln(x^{' + gzahl(faktor_exp_2) + '})'
                               + vorz_str(summand) + r' \quad \vert ~-~ ln(x^{' + gzahl(faktor_exp_2) + '})'
                               + r' \quad \to \quad ln(x^{' + gzahl(faktor_exp_1-faktor_exp_2) + '}) ~=~'
                               + gzahl(summand) + r' \quad \vert e^{()} \quad (1P) \\ x^{'
                               + gzahl(faktor_exp_1-faktor_exp_2) + '} ~=~ e^{' + gzahl(summand)
                               + r'} \quad \vert \sqrt[' + gzahl(faktor_exp_1-faktor_exp_2)
                               + r'] \quad \to \quad x ~=~'
                               + gzahl(N(exp(summand)**(1/(faktor_exp_1-faktor_exp_2)),3)) + r' \quad (2P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            auswahl = np.random.choice([Aufgabe_1,Aufgabe_2, Aufgabe_3, Aufgabe_4], 2, False)

            aufgabe_1, aufgabe_lsg_1, punkte_1 = auswahl[0]()
            aufgabe_2, aufgabe_lsg_2, punkte_2 = auswahl[1]()
            punkte_aufg += punkte_1 + punkte_2

            aufgabe.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_1 + r' \hspace{5em}'
                           + str(liste_teilaufg[i+1]) + r') \quad ' + aufgabe_2 + r' \hspace{5em}')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_lsg_1 + r' \quad \\'
                           + str(liste_teilaufg[i+1]) + r') \quad ' + aufgabe_lsg_2 + r' \quad \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 2
        liste_punkte.append(punkte_aufg)
        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def wachstumsfunktion(nr, teilaufg):
        i = 0
        # hier wird die Funktion erstellt.
        def Aufgabe_Variante_1():

            Text = ('Ein Patient nimmt ein Medikament ein. Anschließend wird die Konzentration des Medikaments im Blut'
                    ' jede Stunde in mg/l gemessen. Die Messwerte ergeben folgende Tabelle: \n\n')

            Grundwert = nzahl(10, 20) * 10
            Prozentwert = nzahl(5, 15)
            Wachstumsfaktor = N(1 - Prozentwert / 100,4)
            Liste = []
            for j in range(20):
                wert = N(Grundwert * Wachstumsfaktor ** j, 4)
                if str(wert)[-1] == '.' or str(wert)[-2:] == '.0':
                    Liste.append(int(wert))
                else:
                    Liste.append(wert)

            Einheit_y = 'mg/l'
            Einheit_x = 'Stunden'
            Tabelle_beschriftung = 'Konzentrationsentwicklung:'
            return Text, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x, Tabelle_beschriftung

        def Aufgabe_Variante_2():

            Text = ('Die Anzahl der Einwohner in Millionen eines Landes wurde jedes Jahr bestimmt. Die Ergebnisse'
                    ' wurden in der folgenden Tabelle festgehalten: \n\n')

            Grundwert = nzahl(80, 200)
            Prozentwert = zzahl(10,50) / 10
            Wachstumsfaktor = N(1 + Prozentwert / 100,4)
            Liste = []
            for j in range(20):
                wert = N(Grundwert * Wachstumsfaktor ** j, 4)
                if str(wert)[-1] == '.' or str(wert)[-2:] == '.0':
                    Liste.append(int(wert))
                else:
                    Liste.append(wert)
            Einheit_y = 'Millionen'
            Einheit_x = 'Jahren'
            Tabelle_beschriftung = 'Bevölkerungsentwicklung:'
            return Text, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x, Tabelle_beschriftung

        if random.random() < 0.5:
            Aufg_Text, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x, Tab_beschr = Aufgabe_Variante_1()
        else:
            Aufg_Text, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x, Tab_beschr = Aufgabe_Variante_2()

        Aufg_t = nzahl(7, 10)
        Aufg_wert_y = int(N(Aufg_Liste[Aufg_t], 2))
        Aufg_wert_t = nzahl(10, 17)

        table2 = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
        table2.add_hline(2, 7)
        table2.add_row(Tab_beschr, f'Zeit in {Aufg_Einheit_x}', '0', '1', '2', '3', '4')
        table2.add_hline(2, 7)
        table2.add_row('', f'Wert in {Aufg_Einheit_y}', Aufg_Liste[0], Aufg_Liste[1], Aufg_Liste[2],
                       Aufg_Liste[3], Aufg_Liste[4])
        table2.add_hline(2, 7)

        table3 = Tabular('c|c|c|c|c|c|c|', row_height=1.5)
        table3.add_hline(2, 7)
        table3.add_row('Ergebnisse: ', 'Quotient der Werte', NoEscape(r'$\frac{a1}{a0}$'),
                       NoEscape(r'$\frac{a2}{a1}$'), NoEscape(r'$\frac{a3}{a2}$'), NoEscape(r'$\frac{a4}{a3}$'),
                       NoEscape(r'$\frac{a5}{a4}$'))
        table3.add_hline(2, 7)
        table3.add_row('', 'Quotienten', str(N(Aufg_Liste[1] / Aufg_Liste[0], 4)).rstrip('0'),
                       str(N(Aufg_Liste[2] / Aufg_Liste[1], 4)).rstrip('0'),
                       str(N(Aufg_Liste[3] / Aufg_Liste[2], 4)).rstrip('0'),
                       str(N(Aufg_Liste[4] / Aufg_Liste[3], 4)).rstrip('0'),
                       str(N(Aufg_Liste[5] / Aufg_Liste[4], 4)).rstrip('0'))
        table3.add_hline(2, 7)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), Aufg_Text]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
        grafiken_aufgaben = ['','']
        grafiken_loesung = ['', '', '']

        if 'a' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append((f'Loesung_{nr}{liste_teilaufg[i]}',''))

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.extend((table2, '\n\n\n', str(teilaufg[i]) + ') Weisen Sie nach, dass es sich um exponentielles '
                                                'Wachstum handelt.\n\n'))
            loesung.extend((str(teilaufg[i]) + r') \quad \mathrm{Alle~Quotienten~sind~gleich~gross.~Damit~handelt~es~sich~'
                                               r'um~exponentielles~Wachstum. \quad (3P)}', table3,
                                                r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
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
            loesung.append(str(teilaufg[i]) + (r') \quad f(x)~=~' + str(Aufg_c0) + r' \cdot '
                                               + str(Aufg_a) + r'^x \quad (2P) \\'
                                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1


        if 'c' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + f') Berechnen Sie die Zeit bis {Aufg_wert_y} {Aufg_Einheit_y}'
                                              ' erreicht werden. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad \quad ' + str(Aufg_wert_y) + r'~=~'+ str(Aufg_c0)
                                               + r' \cdot '+ str(Aufg_a) + r'^x \quad \vert \div ' + str(Aufg_c0)
                                               + r' \quad \to \quad ' + latex(Rational(Aufg_wert_y,Aufg_c0))
                                               + r'~=~'+ str(Aufg_a) + r'^x \quad \vert \log_{' + str(Aufg_a)
                                               + r'} \quad \to \quad x~=~'
                                               + str(N(math.log(Rational(Aufg_wert_y,Aufg_c0),Aufg_a),5))
                                               + r' \quad (3P) \\'
                                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1


        if 'd' in teilaufg:
            punkte_aufg = 2
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            # grafische Darstellung des Sachverhaltes

            # Aufgaben und Lösungen
            aufgabe.append(str(teilaufg[i]) + f') Berechnen Sie den Wert der nach {Aufg_wert_t} {Aufg_Einheit_x}'
                                              f' erreicht wird. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad f(' + str(Aufg_wert_t) + r')~=~' + str(Aufg_c0)
                                               + r' \cdot '+ str(Aufg_a) + r'^{'+ str(Aufg_wert_t)+ r'} ~=~ '
                                               + latex(N(Aufg_c0*Aufg_a**Aufg_wert_t,4)) + r' \quad (2P) \\'
                                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))
            i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def exp_ableitungen(nr, teilaufg):
        i = 0
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Berechnen Sie die Ableitung der folgenden Funktionen.']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['', '']
        grafiken_loesung = ['']
        liste_bez.append(str(nr))
        punkte_aufg = 0

        if 'a' in teilaufg:
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')

            def Aufgabe_1():
                punkte = 2
                faktor_exp = zzahl(2, 8)
                aufgabe = 'f(x) ~=~ x^{' + gzahl(faktor_exp) + r'} \cdot e^{x}'
                aufgabe_lsg = ('f(x) ~=~ x^{' + gzahl(faktor_exp) + r'} \cdot e^{x} \quad \to \quad '
                               + r' f^{ \prime } (x) ~=~' + gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                               + r'} \cdot e^{x} ~+~x^{' + gzahl(faktor_exp) + r'} \cdot e^{x} ~=~ e^{x} \cdot \big( '
                               + gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1) + '} + x^{' + gzahl(faktor_exp)
                               + r'} \big) \quad (2P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_2():
                punkte = 3
                faktor_exp = zzahl(2, 8)
                aufgabe = 'f(x) ~=~ x^{' + gzahl(faktor_exp) + r'} \cdot ln(x)'
                aufgabe_lsg = ('f(x) ~=~ x^{' + gzahl(faktor_exp) + r'} \cdot ln(x) \quad \to \quad '
                               + r' f^{ \prime } (x) ~=~' + gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                               + r'} \cdot ln(x) ~+~ x^{' + gzahl(faktor_exp) + r'} \cdot x^{-1} ~=~'
                               + 'x^{' + gzahl(faktor_exp - 1) + r'} \cdot (' + gzahl(faktor_exp)
                               + r' \cdot ln(x) ~+~ 1) \quad (3P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_3():
                punkte = 4
                faktor_exp = zzahl(2, 8)
                faktor_sqrt = nzahl(2, 8)
                while abs(faktor_exp) == faktor_sqrt:
                    faktor_sqrt = nzahl(2, 8)
                aufgabe = 'f(x) ~=~ \sqrt[' + gzahl(faktor_sqrt) + ']{x^{' + gzahl(faktor_exp) + r'}} \cdot e^{x}'
                aufgabe_lsg = (r'f(x) ~=~ \sqrt[' + gzahl(faktor_sqrt) + ']{x^{' + gzahl(faktor_exp) + r'}} \cdot e^{x} ~=~'
                               + r' x^{' + gzahl(Rational(faktor_exp,faktor_sqrt)) + r'} \cdot e^{x} \quad \to \quad '
                               + r' f^{ \prime } (x) ~=~' + gzahl(Rational(faktor_exp,faktor_sqrt)) + r' \cdot x^{'
                               + gzahl(Rational(faktor_exp, faktor_sqrt)-1) + r'} \cdot e^{x} ~+~' + 'x^{'
                               + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} \cdot e^{x} ~=~ e^{x} \cdot ('
                               + gzahl(Rational(faktor_exp, faktor_sqrt)) + r' \cdot x^{'
                               + gzahl(Rational(faktor_exp, faktor_sqrt)-1) + r'} ~+~ x^{'
                               + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} ) \quad (4P) \\')
                return [aufgabe, aufgabe_lsg, punkte]

            auswahl = np.random.choice([Aufgabe_1, Aufgabe_2, Aufgabe_3], 2, False)
            aufgabe_1, aufgabe_lsg_1, punkte_1 = auswahl[0]()
            aufgabe_2, aufgabe_lsg_2, punkte_2 = auswahl[1]()
            punkte_aufg += punkte_1 + punkte_2

            aufgabe.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_1 + r' \hspace{5em} '
                           + str(liste_teilaufg[i + 1]) + r') \quad ' + aufgabe_2)
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_lsg_1
                           + str(liste_teilaufg[i + 1]) + r') \quad ' + aufgabe_lsg_2)
            i += 2

        if 'b' in teilaufg:
            grafiken_aufgaben.append(f'Aufgabe_{nr}')
            grafiken_loesung.append(f'Loesung_{nr}')

            def Aufgabe_1():
                punkte = 3
                exponent = zzahl(2, 8)
                faktor_1 = zzahl(2, 8)
                faktor_2 = zzahl(1,8)
                aufgabe = ('f(x) ~=~ e^{' + vorz_v_aussen(faktor_1,'x') + '^{' + gzahl(exponent) + r'}'
                           + vorz_v_innen(faktor_2,'x') +  '}')
                aufgabe_lsg = (r' \mathrm{Noch~zu~programmieren! \quad (3P)} \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_2():
                punkte = 3
                exponent = zzahl(2, 8)
                faktor_1 = zzahl(2, 8)
                faktor_2 = zzahl(1, 8)
                aufgabe = ('f(x) ~=~ ln(' + vorz_v_aussen(faktor_1, 'x') + '^{' + gzahl(exponent) + r'}'
                           + vorz_v_innen(faktor_2, 'x') + ')')
                aufgabe_lsg = (r' \mathrm{Noch~zu~programmieren! \quad (3P)} \\')
                return [aufgabe, aufgabe_lsg, punkte]

            def Aufgabe_3():
                punkte = 3
                exponent = zzahl(2, 8)
                wurzel = nzahl(2, 8)
                faktor = zzahl(1,10)
                while abs(exponent) == wurzel:
                    wurzel = nzahl(2, 8)
                summand = zzahl(1,8)
                aufgabe = ('f(x) ~=~ \sqrt[' + gzahl(wurzel) + ']{(' + vorz_v_aussen(faktor,'x')
                           + '^{' + gzahl(exponent) + r'} ' + vorz_str(summand) + r')} ')
                aufgabe_lsg = (r' \mathrm{Noch~zu~programmieren! \quad (3P)} \\')
                return [aufgabe, aufgabe_lsg, punkte]

            auswahl = np.random.choice([Aufgabe_1, Aufgabe_2, Aufgabe_3], 2, False)
            aufgabe_1, aufgabe_lsg_1, punkte_1 = auswahl[0]()
            aufgabe_2, aufgabe_lsg_2, punkte_2 = auswahl[1]()
            punkte_aufg += punkte_1 + punkte_2

            aufgabe.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_1 + r' \hspace{5em}'
                           + str(liste_teilaufg[i + 1]) + r') \quad ' + aufgabe_2)
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + aufgabe_lsg_1
                           + str(liste_teilaufg[i + 1]) + r') \quad ' + aufgabe_lsg_2)
            i += 2

        liste_punkte.append(punkte_aufg)
        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    aufgaben = [logarithmusgesetze(1, ['a', 'b']),
                exponentialgleichungen(2, ['a', 'b']),
                wachstumsfunktion(3,['a','b','c','d']),
                exp_ableitungen(4,['a', 'b'])]

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
    Art = '2. Test (2. Semester)'
    Titel = 'Exponentialfunktionen und höhere Ableitungsregeln'

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
        # print('\033[38;2;0;220;120m\033[1mKontrolle erstellt\033[0m')

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
                    Loesung.append(elements)
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='200px')
                else:
                    Loesung.append(elements)
                k += 1

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        # print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

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