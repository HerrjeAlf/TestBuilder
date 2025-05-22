import string
import numpy as np
import random, math
from fractions import Fraction
import sympy
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *
from math import log

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)
# Aufgaben zu den Regeln

def logarithmusgesetze(nr, anzahl=1, BE=[]):
    # Hier sollen die Schüler und Schülerinnen Logarithmusgesetze vervollständigen.
    # Mit dem Argument "anzahl=" kann die Anzahl der zufällig ausgewählten Logarithmusgesetze festgelegt werden.
    # Standardmäßig wird immer ein Gesetz erstellt.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    # hier wird die Funktion erstellt.
    regeln_aufgabe = {r' \log_a(u \cdot v) ~=~ \hspace{15em}': r' \log_a(u \cdot v) ~=~ \log_a u + \log_a v',
                      r' \log_a \frac{u}{v} ~=~ \hspace{15em}': r' \log_a \frac{u}{v} ~=~ \log_a u - \log_a v',
                      r' \log_a u^r ~=~ \hspace{15em}': r' \log_a u^r ~=~ r \cdot \log_a u',
                      r' \log_a \sqrt[n]{u} ~=~ \hspace{15em}': r' \log_a \sqrt[n]{u} ~=~ \frac{1}{n} \cdot \log_a u',
                      r' \log_c b ~=~ \hspace{15em}': r' \log_c b ~=~ \frac{\log_a b}{\log_a c} ~=~ \frac{\ln b}{\ln c}',
                      r'a^{\log_a b} ~=~ \hspace{15em}': r'a^{\log_a b} ~=~ b',
                      r' \log_a 1 ~=~ \hspace{15em}': r' \log_a 1 ~=~ 0',
                      r' \log_a a ~=~ \hspace{15em}': r' \log_a a ~=~ 1',
                      r' \log_e ~=~ \hspace{15em}': r' \log_e ~=~ \ln',
                      r' \log_{10} ~=~ \hspace{15em}': r' \log_{10} ~=~ \lg'}

    exit("Die Eingabe bei anzahl muss eine Zahl sein") if type(anzahl) != int else anzahl
    anzahl = len(regeln_aufgabe) if anzahl > len(regeln_aufgabe) else anzahl
    auswahl = np.random.choice(list(regeln_aufgabe.keys()), anzahl, False)
    if anzahl == 1:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Vervollständigen Sie das folgende Logarithmusgesetz.']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Vervollständigen Sie die folgenden Logarithmusgesetze.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    aufg = lsg = ''
    for element in range(anzahl):
        if (element + 1) % 2 != 0 and (element + 1) != anzahl:
            aufg = aufg + auswahl[element]
        elif (element + 1) % 2 == 0 and (element + 1) != anzahl:
            aufg = aufg + auswahl[element] + r' \\\\'
        else:
            aufg = aufg + auswahl[element]
        lsg = lsg + regeln_aufgabe[auswahl[element]] + r' \\'
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [anzahl]
        liste_punkte = BE
    else:
        liste_punkte = [anzahl]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rechenregeln_integrale(nr, anzahl=1, BE=[]):
    # Hier sollen die Schüler und Schülerinnen Rechenregeln der Integralrechnung vervollständigen.
    # Mit dem Argument "anzahl=" kann die Anzahl der zufällig ausgewählten Regeln festgelegt werden.
    # Standardmäßig wird immer eine Regel erstellt.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    i = 0
    regeln_aufgabe = {r' \int x^n \,dx ~=~ \hspace{15em}': r' \int x^n \,dx ~=~ \frac{1}{n+1} \cdot x^{n+1} + C ',
                      r' \int a \cdot f(x) \,dx ~=~ \hspace{15em}':
                          r' \int a \cdot f(x) \,dx ~=~ a \cdot \int f(x) \,dx ~=~ a \cdot F(x) + C ',
                      r' \int \left( f(x) + g(x) \right) \,dx ~=~ \hspace{15em}':
                      r' \int \left( f(x) + g(x) \right) \,dx ~=~ \int f(x) \,dx + \int g(x) \,dx ~=~ F(x) + G(x) + C',
                      r' \int e^x \,dx ~=~ \hspace{15em}': r' \int e^x \,dx ~=~ e^x + C ',
                      r' \int_{a}^{a} f(x) \,dx ~=~ \hspace{15em}':
                          r' \int_{a}^{a} f(x) \,dx ~=~ \int_{a}^{a} f(x) \,dx ~=~ 0',
                      r' - \int_{a}^{b} f(x) \,dx ~=~ \hspace{15em}':
                          r' - \int_{a}^{b} f(x) \,dx ~=~ \int_{b}^{a} f(x) \,dx',
                      r' \int_{a}^{b} f(x) \,dx + \int_{b}^{c} f(x) \,dx ~=~ \hspace{15em}':
                      r' \int_{a}^{b} f(x) \,dx + \int_{b}^{c} f(x) \,dx ~=~ \int_{a}^{c} f(x) \,dx'}

    anzahl = len(regeln_aufgabe) if anzahl > len(regeln_aufgabe) else anzahl
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [anzahl]
        liste_punkte = BE
    else:
        liste_punkte = [anzahl]
    auswahl = np.random.choice(list(regeln_aufgabe.keys()), anzahl, False)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vervollständigen Sie die folgenden Rechenregeln der Integrale.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    aufg = lsg = ''
    for element in range(anzahl):
        if (element + 1) % 2 != 0 and (element + 1) != anzahl:
            aufg = aufg + auswahl[element]
        elif (element + 1) % 2 == 0 and (element + 1) != anzahl:
            aufg = aufg + auswahl[element] + r' \\\\'
        else:
            aufg = aufg + auswahl[element]
        lsg = lsg + regeln_aufgabe[auswahl[element]] + r' \\'

    lsg = lsg + r' \\ \mathrm{insgesamt~' + str(anzahl) + r'~BE}'
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Aufgaben zur Differenzialrechnung
def folgen(nr, teilaufg=['a', 'b', 'c', 'd'], ausw_folgenart=None, i=0, BE=[]):
    # Hier sollen die SuS Zahlenfolge um weitere Folgenglieder ergänzen, die Art (arithmetisch oder geometrisch) erkennen, ein Bildungsgesetz benennen und ggf. ein bestimmtes Folgenglied berechnen.
    # Mit dem Parameter "teilaufg=[]" kann festgelegt werden, welche Teilaufgaben verwendet werden. Standardmäßig werden alle Teilaufgabe verwendet.
    # Mit "ausw_folgenart=" kann festgelegt werden, ob es sich um arithmetische oder geometrische Zahlenfolge handelt, oder keine spezielle Zahlenfolge vorliegt. Der Parameter "ausw_folgenart=" kann None, 'arithmetisch', 'geometrisch' oder 'keine Vorschrift' sein. Standardmäßig ist None eingestellt und die Auswahl damit zufällig.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    # Berechnungen der Zahlenfolgen
    start_arithm_folge = zzahl(1, 10)
    start_geom_folge = nzahl(1, 10)
    arithm_folge_d = nzahl(2, 10)
    basis = zzahl(2, 10)
    if nzahl(1, 2) == 1:
        p = random.choice([2, 4, 5, 8, 10])
        geom_folge_q = Rational(1, p)
    else:
        geom_folge_q = random.choice([2, 3, 4, 5])
    bel_vorschrift = [start_arithm_folge + basis ** x,
                      start_arithm_folge - 1 / x,
                      start_arithm_folge / (x + arithm_folge_d),
                      x ** arithm_folge_d]
    bel_vorschrift_str = [gzahl(start_arithm_folge) + r'+ \left( ' + gzahl(basis) + r' \right) ^{n}',
                          gzahl(start_arithm_folge) + r'~-~ \frac{1}{n}',
                          r' \frac{' + gzahl(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                          r'n^{' + str(arithm_folge_d) + '}']
    ausw_folge = random.randint(0,len(bel_vorschrift)-1)
    a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                start_geom_folge * geom_folge_q ** (x - 1),
                bel_vorschrift[ausw_folge]]
    a_n_str_alle = [latex(start_arithm_folge) + r'~+~ (n-1) \cdot ~' + latex(arithm_folge_d),
                    latex(start_geom_folge) + r' \cdot ' + latex(geom_folge_q) + r'^{n-1}',
                    bel_vorschrift_str[ausw_folge]]
    liste_folgen = [ 'arithmetisch', 'geometrisch', 'keine Vorschrift']
    ausw_folgenart = random.choice(liste_folgen) if ausw_folgenart == None else ausw_folgenart
    exit(f"ausw_folgenart muss None, oder 'arithmetisch', 'geometrisch', 'keine Vorschrift' sein")\
        if ausw_folgenart not in liste_folgen else ausw_folgenart
    auswahl_folgenart = liste_folgen.index(ausw_folgenart)
    a_n = a_n_alle[auswahl_folgenart]
    a_n_str = a_n_str_alle[auswahl_folgenart]
    data = [a_n.subs(x, element) for element in range(1, 5)]
    data_lsg = [a_n.subs(x, element) for element in range(1, 8)]

    # Aufgaben
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Zahlenfolge:',
               latex(data[0]) + r', \quad ' + latex(data[1]) + r', \quad ' + latex(data[2]) + r', \quad ' +
               latex(data[3]) + r', ~ ...  \\']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen eine gegebene Zahlenfolge um drei weitere Glieder ergänzen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Setze die Zahlenfolge um drei weitere Glieder fort. \n\n')
        loesung.append(beschriftung(teilaufg, i, True) + latex(data_lsg[0]) + ',~' + latex(data_lsg[1])
                       + ',~' + latex(data_lsg[2]) + ',~' + latex(data_lsg[3]) + r',~' + latex(data_lsg[4])
                       + ',~' + latex(data_lsg[5]) + ',~' + latex(data_lsg[6]) + r' \quad (3BE)')
        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen entscheiden, ob eine arithmetische oder geometrische Zahlenfolge vorliegt
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Überprüfe ob es sich um eine arithmetische oder geometrische '
                                                'Zahlenfolge handelt. \n\n')
        if auswahl_folgenart == 0:
            table_b = Tabular('c|c|c|c|c|', row_height=1.2)
            table_b.add_hline(2, 5)
            table_b.add_row('Liste der Differenz aus den Folgengliedern', 'Werte', 'a1-a0', 'a2-a1', 'a3-a2')
            table_b.add_hline(2, 5)
            table_b.add_row('', 'Ergebnis', data[1] - data[0], data[2] - data[1], data[3] - data[2])
            table_b.add_hline(2, 5)
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                    r'~ist~es~eine~arithmetische~Folge~mit~d~=~'
                           + gzahl(arithm_folge_d) + r'.} \quad (3BE)')
            loesung.append(table_b)

        if auswahl_folgenart == 1:
            table_b = Tabular('c|c|c|c|c|', row_height=1.2)
            table_b.add_hline(2, 5)
            table_b.add_row('Liste der Quotienten aus den Folgengliedern ', 'Werte', 'a1/a0', 'a2/a1', 'a3/a2')
            table_b.add_hline(2, 5)
            table_b.add_row('', 'Ergebnis', Rational(data[1], data[0]), Rational(data[2] / data[1]),
                            Rational(data[3] / data[2]))
            table_b.add_hline(2, 5)
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                           + r'~ist~es~eine~geometrische~Folge~mit~q~=~' + gzahl(geom_folge_q) + r'.} \quad (3BE)')
            loesung.append(table_b)
        if auswahl_folgenart == 2:
            table_b = Tabular('c|c|c|c|c|c|', row_height=1.2)
            table_b.add_hline(2, 6)
            table_b.add_row('Liste der Differenzen und Qoutienten aus den ', 'Werten',
                            'a1-a0', 'a2-a1', 'a1/a0', 'a2/a1')
            table_b.add_hline(2, 6)
            table_b.add_row('', 'Ergebnis', data[1] - data[0], data[2] - data[1], N(data[1] / data[0], 3),
                            N(data[2] / data[1], 4))
            table_b.add_hline(2, 6)
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                    r'~ist~weder~eine~arithmetische,~noch~eine~geometrische~Folge.} '
                                                    r' \quad (3BE)')
            loesung.append(table_b)
        liste_punkte.append(3)
        i += 1

    if 'c' in teilaufg:
        # Die SuS sollen das Bildungsgesetz der gegebenen Zahlenfolge finden bzw. nennen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Nenne das Bildungsgesetz der Zahlenfolge. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' a_n~=~' + a_n_str + r' \quad (2BE)')
        liste_punkte.append(3)
        i += 1

    if 'd' in teilaufg and auswahl_folgenart < 2:
        # Die Teilaufgabe wird nur angezeigt, wenn eine arithmetische oder geometrische Zahlenfolge vorliegt. Hier sollen die SuS ein bestimmtes Folgenglied berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if auswahl_folgenart == 0:
            a_unten = nzahl(1, 50)
            a_oben = nzahl(51, 100)
            n = a_oben - a_unten
            wert_a_unten = a_n.subs(x, a_unten)
            wert_a_oben = a_n.subs(x, a_oben)
            aufgabe.append(str(liste_teilaufg[i])
                           + f') Berechnen Sie die Summe der Folgenglieder von n={a_unten} bis n={a_oben}. \n\n')
            ergebnis = n * (wert_a_oben + wert_a_unten) / 2
            loesung.append(beschriftung(teilaufg,i, True) + r' \displaystyle\sum_{i=' + gzahl(a_unten)
                           + '}^{' + gzahl(a_oben) + r'} ~ a_n ~=~ ' + gzahl(n) + r' \cdot \frac{~'
                           + gzahl(wert_a_unten) + vorz_str(wert_a_oben) + '~}{~2~} ~=~' + gzahl(N(ergebnis, 5))
                           + r' \quad (3BE) \\')
        else:
            a_unten = nzahl(11, 20)
            a_oben = nzahl(21, 30)
            n = a_oben - a_unten
            aufgabe.append(beschriftung(teilaufg, i) + f'Berechnen Sie die Summe der Folgenglieder von n={a_unten} '
                                                    f'bis n={a_oben}. \n\n')
            ergebnis = (1 - geom_folge_q ** (n + 1)) / (1 - geom_folge_q)
            loesung.append(beschriftung(teilaufg,i, True) + r' \displaystyle\sum_{i=' + gzahl(a_unten) + '}^{' +
                           gzahl(a_oben) + r'} ~ q^n ~=~ \frac{~1~-~ \left(' + gzahl(geom_folge_q) + r' \right)^{'
                           + gzahl(n + 1) + '~}}{~1~-~' + gzahl(geom_folge_q) + '} ~=~' + gzahl(N(ergebnis, 5))
                           + r' \quad (3BE) \\')
        liste_punkte.append(3)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es werden die Standardpunkte übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def grenzwerte_folge(nr, ausw_folgenart=None, BE=[]):
    # In dieser Aufgabe sollen die SuS den Grenzwert einer bestimmten Zahlenfolgen berechnen. Die Aufgabe hat keine Teilaufgaben.
    # Mit "ausw_folgenart=" kann festgelegt werden, ob es sich um arithmetische oder geometrische Zahlenfolge handelt, oder keine spezielle Zahlenfolge vorliegt. Der Parameter "ausw_folgenart=" kann None, 'arithmetisch', 'geometrisch' oder 'keine Vorschrift' sein. Standardmäßig ist None eingestellt und die Auswahl damit zufällig.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    start_arithm_folge = zzahl(2, 10)
    start_geom_folge = nzahl(2, 10)
    arithm_folge_d = nzahl(2, 10)
    basis = zzahl(2, 10)
    if nzahl(1, 2) == 1:
        p = random.choice([2, 4, 5, 8, 10])
        geom_folge_q = Rational(1, p)
    else:
        geom_folge_q = random.choice([2, 3, 4, 5])
    bel_vorschrift = [start_arithm_folge + basis ** x,
                      start_arithm_folge - 1 / x,
                      start_arithm_folge / (x + arithm_folge_d),
                      x ** arithm_folge_d]
    bel_vorschrift_str = [str(start_arithm_folge) + vorz_str(basis) + r'^{n}',
                          gzahl(start_arithm_folge) + r'~-~ \frac{1}{n}',
                          r' \frac{' + gzahl(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                          r'n^{' + gzahl(arithm_folge_d) + '}']
    ausw_folge = random.randint(1, len(bel_vorschrift)) - 1
    a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                start_geom_folge * geom_folge_q ** (x - 1),
                bel_vorschrift[ausw_folge]]
    a_n_str_alle = [latex(start_arithm_folge) + r'~+~ (n-1) \cdot ~' + latex(arithm_folge_d),
                    latex(start_geom_folge) + r' \cdot \left(' + latex(geom_folge_q) + r' \right) ^{n-1}',
                    bel_vorschrift_str[ausw_folge]]
    liste_folgen = [ 'arithmetisch', 'geometrisch', 'keine Vorschrift']
    ausw_folgenart = random.choice(liste_folgen) if ausw_folgenart == None else ausw_folgenart
    exit(f"ausw_folgenart muss None, oder 'arithmetisch', 'geometrisch', 'keine Vorschrift' sein")\
        if ausw_folgenart not in liste_folgen else ausw_folgenart
    auswahl_folgenart = liste_folgen.index(ausw_folgenart)
    a_n = a_n_alle[auswahl_folgenart]
    a_n_str = a_n_str_alle[auswahl_folgenart]
    print(a_n)
    grenzwert = limit(a_n, x, oo)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Berechne den Grenzwert der folgende Bildungsvorschrift:',
               r'a_{n}~=~' + a_n_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    loesung.append(r' \lim \limits_{n \to \infty } ' + a_n_str + '~=~'
                   + latex(grenzwert) + r' \quad (2BE)')
    grafiken_aufgaben = []
    grafiken_loesung = []
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [2]
        liste_punkte = BE
    else:
        liste_punkte = [2]
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def grenzwerte_funktionen(nr, BE=[]):
    # In dieser Aufgabe sollen die SuS den Grenzwert einer rationalen Funktion berechnen. Die Aufgabe besitzt keine Teilaufgaben.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    faktor = zzahl(1, 10)
    polstelle = zzahl(1, 8)
    zaehler = collect(expand(faktor * (x ** 2 - polstelle ** 2)),x)
    nenner = x + (-1 * polstelle)
    Bruch = r' \frac{' + latex(zaehler) + '}{' + latex(nenner) + '}'
    Bruch_gekuerzt = (r'~=~ \lim \limits_{x \to ' + gzahl(polstelle) + '} ~ ' + vorz_v_aussen(faktor, r' \cdot (x')
                      + vorz_v_innen(polstelle,')'))
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    aufgabe.extend(('Bestimmen Sie den Grenzwert durch Termumformungen.',
                    r' \lim \limits_{x \to ' + gzahl(polstelle) + '} ~' + Bruch))
    loesung.append(r' \quad \lim \limits_{x \to ' + gzahl(polstelle) + '} ~' + Bruch +
                   r'~=~ \lim \limits_{x \to ' + gzahl(polstelle) + r'} ~ \frac{' + vorz_v_aussen(faktor,'(x') +
                   vorz_v_innen(polstelle, r') \cdot (x~') + vorz_v_innen(-1 * polstelle, ')}{') + latex(nenner) + '}' +
                   Bruch_gekuerzt + r'~=~' + gzahl(faktor * (polstelle * 2)) + r' \quad (4BE) \\')
    grafiken_aufgaben = []
    grafiken_loesung = []
    if BE != []:
        if len(BE) > 1:
            print(
                'Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [2]
        liste_punkte = BE
    else:
        liste_punkte = [2]
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def aenderungsrate(nr, teilaufg=['a', 'b', 'c', 'd'], ableitung=False, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS die mittlere Änderungsrate in einem gegebenen Intervall und lokale Änderungsrate an einer gegebenen Stelle einer Funktion rechnerisch und zeichnerisch bestimmen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Der Parameter "ableitung=" kann 'True' oder 'False' sein und gibt die mögliche Lösung für Teilaufgabe d) vor. Bei 'False' kennen die SuS die Ableitung einer Funktion noch nicht und müssen die lokale Änderungsrate mit einer Grenzwertberechnung bestimmen. Bei 'True' ist es die triviale Lösung mithilfe der Ableitung der Funktion.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    faktor = zzahl(1, 20) / 10
    s_xwert = zzahl(1, 3)
    s_ywert = zzahl(1, 3)
    abstand = random.choice([[-1, 2], [-2, 1]])

    x_wert_1 = s_xwert + abstand[0]
    x_wert_2 = s_xwert + abstand[1]
    y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
    y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
    werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

    while not all(abs(wert) < 6 for wert in werte):
        s_xwert = zzahl(1, 3)
        s_ywert = zzahl(1, 3)
        abstand = random.choice([[-1, 2], [-2, 1]])

        x_wert_1 = s_xwert + abstand[0]
        x_wert_2 = s_xwert + abstand[1]
        y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
        y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
        werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

    fkt = expand(faktor * (x - s_xwert) ** 2 + s_ywert)
    fkt_abl = diff(fkt, x)
    fkt_str = (vorz_v_aussen(faktor, 'x^2') + vorz_v_innen(-2 * faktor * s_xwert,'x')
               + vorz_str((faktor * (s_xwert ** 2)) + s_ywert))
    fkt_abl = diff(fkt, x)
    fkt_abl_x0 = fkt_abl.subs(x, x_wert_2)

    print(fkt)

    # print("f(x)=" + str(fkt))
    # print("f'(x)=" + str(fkt_abl))
    # print("f'(x_0)=" + str(fkt_abl_x0))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Funktion:',
               r'f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    xwerte_geraden = [-6, 6]
    if 'a' in teilaufg:
        # Die SuS sollen die mittlere Änderungsrate im gegebenen Intervall eines Graphen zeichnerisch bestimmen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')

        aufgabe.extend((beschriftung(teilaufg, i) + f'Bestimme zeichnerisch die mittlere Änderungsrate im '
                                          f'Interval [ {x_wert_1} | {x_wert_2} ] vom Graphen f.', 'Figure'))
        dy = y_wert_2 - y_wert_1
        dx = x_wert_2 - x_wert_1
        fkt_sekante = dy / dx * (x - x_wert_2) + y_wert_2
        xwerte = [-6 + n / 5 for n in range(60)]
        ywerte = [fkt.subs(x, xwerte[element]) for element in range(60)]
        print(ywerte)
        graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, r'',
                         'f', f'Aufgabe_{nr}{liste_teilaufg[i]}')

        xwerte_dy = [x_wert_2, x_wert_2]
        ywerte_dy = [y_wert_1, y_wert_2]
        xwerte_dx = [x_wert_1, x_wert_2]
        ywerte_dx = [y_wert_1, y_wert_1]

        steigung_dreieck = N((y_wert_2 - y_wert_1) / (x_wert_2 - x_wert_1), 2)

        ywerte_sekante = [fkt_sekante.subs(x, -6), fkt_sekante.subs(x, 6)]

        loesung.append(beschriftung(teilaufg, i, True)
                       + r' \mathrm{Gerade~durch~beide~Punkte~(1BE),~~Steigungsdreieck~(1BE),~Steigung~}'
                       + r' \bm{m=' + gzahl(steigung_dreieck) + r'}~\mathrm{bestimmt~(1BE)}')

        if 'c' not in teilaufg:
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, '',
                             'f',f'Loesung_{nr}{liste_teilaufg[i]}', xwerte_dy, ywerte_dy,
                             xwerte_dx, ywerte_dx, xwerte_geraden, ywerte_sekante)
            loesung.append('Figure')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')


        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die mittlere Änderungsrate in einem gegebenen Intervall berechnen und ihr Ergebnis der vorherigen Teilaufgabe überprüfen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg, i) + f'Überprüfe die mittlere Änderungsrate im Interval '
                                          f'[ {x_wert_1} | {x_wert_2} ] durch Rechnung. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \frac{ \Delta y}{ \Delta x} ~=~ \frac{f(' + gzahl(x_wert_2)
                       + ') - f(' + gzahl(x_wert_1) + ')}{' + gzahl(x_wert_2) + vorz_str(-1 * x_wert_1)
                       + r'} ~=~ \frac{' + gzahl(N(y_wert_2, 3)) + vorz_str(-1 * N(y_wert_1, 3))
                       + '}{' + gzahl(x_wert_2) + vorz_str(-1 * x_wert_1) + r'} ~=~\bm{'
                       + gzahl(N(Rational(y_wert_2 - y_wert_1, x_wert_2 - x_wert_1), 3))
                       + r'} \quad \to \quad \mathrm{'r'Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (4P)')
        liste_punkte.append(4)
        i += 1

    if 'c' in teilaufg:
        # Die SuS sollen die lokale Änderungsrate an einer Stelle eines Graphen zeichnerisch bestimmen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        steigung_tangente = fkt_abl.subs(x, x_wert_2)
        fkt_tangente = steigung_tangente * (x - x_wert_2) + y_wert_2

        x_wert_3 = x_wert_2 - 1
        y_wert_3 = fkt_tangente.subs(x, x_wert_3)
        steigung_dreieck = N((y_wert_2 - y_wert_3) / (x_wert_2 - x_wert_3), 2)
        xwerte_dy_c = [x_wert_2, x_wert_2]
        ywerte_dy_c = [y_wert_2, y_wert_3]
        xwerte_dx_c = [x_wert_2, x_wert_3]
        ywerte_dx_c = [y_wert_3, y_wert_3]
        ywerte_tangente = [fkt_tangente.subs(x, -6), fkt_tangente.subs(x, 6)]

        if 'a' not in teilaufg:
            xwerte = [-6 + n / 5 for n in range(60)]
            ywerte = [fkt.subs(x, xwerte[element]) for element in range(60)]
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, '',
                             'f',f'Aufgabe_{nr}{liste_teilaufg[i]}')
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt, '', 'f',
                             f'Loesung_{nr}{liste_teilaufg[i]}',xwerte_dy_c, ywerte_dy_c,
                             xwerte_dx_c, ywerte_dx_c, xwerte_geraden, ywerte_tangente)
            aufgabe.append(beschriftung(teilaufg, i)
                           + f'Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}.')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            aufgabe.append('Figure')

        else:
            xwerte = [-6 + n / 5 for n in range(60)]
            ywerte = [fkt.subs(x, xwerte[element]) for element in range(60)]
            graph_xyfix_plus(xwerte, ywerte, s_xwert, fkt,
                             r'',
                             'f', f'Loesung_{nr}{liste_teilaufg[i]}',
                             xwerte_dy, ywerte_dy, xwerte_dx, ywerte_dx,
                            xwerte_geraden, ywerte_sekante, xwerte_dy_c, ywerte_dy_c, xwerte_dx_c, ywerte_dx_c,
                            xwerte_geraden, ywerte_tangente)
            aufgabe.append(beschriftung(teilaufg, i)
                           + f'Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')

        loesung.extend((beschriftung(teilaufg,i, True)
                        + r' \mathrm{Tangente~an~Punkt~(1BE),~~Steigungsdreieck~(1BE),~Steigung~} \bm{m='
                       + gzahl(steigung_dreieck) + r'} \mathrm{~bestimmt~(1BE)}', 'Figure'))
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        liste_punkte.append(3)
        i += 1

    if 'd' in teilaufg:
        # Die SuS sollen die zeichnerisch bestimmte lokale Änderungsrate rechnerisch überprüfen. Die Lösung hängt vom gewählten Parameter 'ableitung=' ab.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg, i) + f'Überprüfe die lokale Änderungsrate an der Stelle x = {x_wert_2} '
                       + f'mit einer Rechnung. \n\n')
        a_3_re = faktor
        b_1_re = -2 * faktor * s_xwert
        b_2_re = faktor * x_wert_2
        b_3_re = b_1_re + b_2_re
        c_1_re = faktor * (s_xwert ** 2) + s_ywert - (faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert)
        c_2_re = b_3_re * x_wert_2

        a_1 = gzahl(N(faktor, 3))
        a_3 = gzahl(N(a_3_re, 3))
        b_1 = gzahl(N(b_1_re, 3))
        b_2 = gzahl(N(b_2_re, 3))
        b_3 = gzahl(N(b_3_re, 3))
        c_1 = gzahl(N(c_1_re, 3))
        c_2 = gzahl(N(c_2_re, 3))

        table = Tabular('c c|c|c', row_height=1.2)
        table.add_row('', a_1, b_1, c_1)
        table.add_hline( 2, 4)
        table.add_row('alternative Berechnung des Partialbruches mit Hornerschema: ','', b_2, c_2)
        table.add_hline(2, 4)
        table.add_row('', a_3, b_3, 0)

        division_fkt_linear = (fkt - fkt.subs(x, x_wert_2)) / (x - x_wert_2)
        partialbruch = gzahl(faktor) + 'x' + vorz_str(b_3_re)

        # print(division_fkt_linear)
        # print(partialbruch)

        if ableitung == False:
            loesung.append(beschriftung(teilaufg,i, True) + r' \lim \limits_{x \to ' + gzahl(x_wert_2)
                           + r'} ~ \frac{f(x)-f(' + gzahl(x_wert_2) + r')}{x' + vorz_str(-1 * x_wert_2)
                           + r'} ~=~ \lim \limits_{x \to ' + gzahl(x_wert_2) + r'} ~ \frac{' + fkt_str + '-('
                           + gzahl(N(fkt.subs(x, x_wert_2), 3)) + ')}{x' + vorz_str(-1 * x_wert_2)
                           + '} ~=~' + r' \lim \limits_{x \to ' + gzahl(x_wert_2) + '}~' + partialbruch + r'~=~ \bm{'
                           + gzahl(N(fkt_abl_x0, 3)) + r'} \quad (3BE) \\'
                           + r' \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (1BE)')
            loesung.append(table)
            loesung.append(' \n\n')
            liste_punkte.append(4)
        else:
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime} (x)~=~' + latex(fkt_abl)
                           + r' \to f^{ \prime} (' + gzahl(x_wert_2) + r')~=~ \bm{'
                           + gzahl(fkt_abl.subs(x, x_wert_2))
                           + r'} \quad (2BE) \quad \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein}'
                           r' \quad (1BE) \\')
            liste_punkte.append(3)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def differentialqoutient(nr, teilaufg=['a', 'b'], i=0, BE=[]):
    # Die SuS sollen die Ableitung einer linearen bzw. quadratischen Funktion mithilfe des Differentialqoutienten berechnen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    # Berechnung der Koeffizienten
    a1, a2 = faktorliste(2, 10, 2)
    b1, b2, b3 = faktorliste(2, 12, 3)
    fkt_str_a = vorz_v_aussen(a1,'x') + vorz_str(a2)
    fkt_str_b = vorz_v_aussen(b1,'x^2') + vorz_v_innen(b2, 'x') + vorz_str(b3)

    if len(teilaufg) == 1:
        if 'a' in teilaufg:
            aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                       NoEscape('Berechne die erste Ableitung der Funktion $ f(x) =' + vorz_v_aussen(a1,'x')
                                + vorz_str(a2) + '$ mithilfe des Differentialquotienten.')]
        else:
            aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                       NoEscape('Berechne die erste Ableitung der Funktion $ f(x) =' + vorz_v_aussen(b1,'x^2')
                                + vorz_v_innen(b2, 'x') + vorz_str(b3) + '$ mithilfe des Differentialquotienten.')]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
                   r' \mathrm{Berechne~die~erste~Ableitung~der~folgenden~Funktion~mithilfe~des~'
                   r'Differentialquotienten}.']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Berechne die erste Ableitung der folgenden Funktionen mithilfe des Differentialquotienten.',
                   beschriftung(teilaufg,i, True) + r' f(x)~=~' + fkt_str_a + r' \hspace{10em}'
                   + str(liste_teilaufg[i + 1]) + r') \quad f(x)~=~' + fkt_str_b + r' \hspace{5em} \\']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
                   r' \mathrm{Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe~des~'
                   r'Differentialquotienten}.']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Mit dem Differentialqoutienten eine lineare Funktion ableiten.
        punkte = 3
        a1, a2 = faktorliste(2, 10, 2)
        fkt_str_a = gzahl(a1) + 'x' + vorz_str(a2)
        if len(teilaufg) == 1:
            liste_bez.append(f'{str(nr)}')
            loesung.append(r'f ^{ \prime} (x) ~=~ \lim \limits_{ h \to 0} \frac{f(x+h) ~-~ f(x)}{h}'
                           + r'= ~ \lim \limits_{ h \to 0}\frac{' + str(a1) + r'(x + h)~' + vorz_str(a2) + r'~-('
                           + str(a1) + r'x' + vorz_str(a2) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{'
                           + str(a1) + 'x~' + vorz_str(a1) + 'h~' + vorz_str(a2) + '~' + vorz_str(-1 * a1) + r'x~'
                           + vorz_str(-1 * a2) + r'}{h} =~ \lim \limits_{ h \to 0} \frac{~' + str(a1)
                           + r'h~}{h} ~=~\bm{' + str(a1) + r'} \quad (3BE)')
        else:
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            loesung.append(beschriftung(teilaufg,i, True) + r' f ^{ \prime} (x) ~=~'
                           + r' \lim \limits_{ h \to 0} \frac{f(x+h) ~-~ f(x)}{h} = ~ \lim \limits_{ h \to 0}\frac{'
                           + str(a1) + r'(x + h)~' + vorz_str(a2) + r'~-(' + str(a1) + r'x' + vorz_str(a2)
                           + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{' + str(a1) + 'x~' + vorz_str(a1)
                           + 'h~' + vorz_str(a2) + '~' + vorz_str(-1 * a1) + r'x~'
                           + vorz_str(-1 * a2) + r'}{h} =~ \lim \limits_{ h \to 0} \frac{~' + str(a1)
                           + r'h~}{h} ~=~\bm{' + str(a1) + r'} \quad (3BE) \\')
        liste_punkte.append(punkte)
        i += 1
    if 'b' in teilaufg:
        # Mit dem Differentialqoutienten eine quadratische Funktion ableiten.
        punkte = 5
        fkt_str_b = gzahl(b1) + 'x^2' + vorz_str(b2) + 'x' + vorz_str(b3)
        if len(teilaufg) == 1:
            liste_bez.append(f'{str(nr)}')
            loesung.append(r' f^{ \prime} (x) ~=~ \lim \limits_{ h \to 0} \frac{f(x+h) - f(x)}{h} ~=~'
                           + r' \lim \limits_{ h \to 0} \frac{' + str(b1) + r'(x + h)^2 ~'
                           + vorz_str(b2) + r'(x+h) ~' + vorz_str(b3) + r' ~-~ (' + str(b1) + r'x^2' + vorz_str(b2)
                           + r'x~' + vorz_str(b3) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{~' + str(b1)
                           + r'x^2 ~' + vorz_str(2 * b1) + 'xh ~' + vorz_str(b1) + 'h^2 ~' + vorz_str(b2) + 'x~'
                           + vorz_str(b2) + 'h~' + vorz_str(b3) + '~' + vorz_str(-1 * b1) + 'x^2~'
                           + vorz_str(-1 * b2) + 'x ~' + vorz_str(-1 * b3) + r'}{h} ~=~ \lim \limits_{ h \to 0} \frac{~'
                           + str(2 * b1) + r'xh ~' + vorz_str(b1) + r'h^2~' + vorz_str(b2) + r' h~}{h} \\'
                           + r' ~=~ \lim \limits_{ h \to 0} \frac{~ h(~' + str(2 * b1) + r'x~' + vorz_str(b1)
                           + 'h ~' + vorz_str(b2) + r'~)}{h} =~ \lim \limits_{ h \to 0} ' + str(2 * b1) + r'x~'
                           + vorz_str(b1) + 'h ~' + vorz_str(b2) + r'~=~ \bm{' + str(2 * b1) + 'x~' + vorz_str(b2)
                           + r'} \quad (5P)')
            liste_punkte.append(punkte)
        else:
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime} (x) ~=~ \lim \limits_{ h \to 0}'
                           + r' \frac{f(x+h) - f(x)}{h} ~=~ \lim \limits_{ h \to 0} \frac{' + str(b1) + r'(x + h)^2 ~'
                           + vorz_str(b2) + r'(x+h) ~' + vorz_str(b3) + r' ~-~ (' + str(b1) + r'x^2' + vorz_str(b2)
                           + r'x~' + vorz_str(b3) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{~' + str(b1)
                           + r'x^2 ~' + vorz_str(2 * b1) + 'xh ~' + vorz_str(b1) + 'h^2 ~' + vorz_str(b2) + 'x~'
                           + vorz_str(b2) + 'h~' + vorz_str(b3) + '~' + vorz_str(-1 * b1) + 'x^2~'
                           + vorz_str(-1 * b2) + 'x ~' + vorz_str(-1 * b3) + r'}{h} ~=~ \lim \limits_{ h \to 0} \frac{~'
                           + str(2 * b1) + r'xh ~' + vorz_str(b1) + r'h^2~' + vorz_str(b2) + r' h~}{h} \\'
                           + r' ~=~ \lim \limits_{ h \to 0} \frac{~ h(~' + str(2 * b1) + r'x~' + vorz_str(b1)
                           + 'h ~' + vorz_str(b2) + r'~)}{h} =~ \lim \limits_{ h \to 0} ' + str(2 * b1) + r'x~'
                           + vorz_str(b1) + 'h ~' + vorz_str(b2) + r'~=~ \bm{' + str(2 * b1) + 'x~' + vorz_str(b2)
                           + r'} \quad (5P)')
            liste_punkte.append(punkte)
        i += 1
    loesung.append(r' \mathrm{insgesamt~' + str(sum(liste_punkte)) + r'~BE}')
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def grafisches_ableiten(nr, teilaufg=['a', 'b'], i=0, BE=[]):
    # Die SuS sollen in einem gegebenen Graphen einer Funktion den Graphen der Ableitungsfunktion skizzieren und den skizzierten Verlauf begründen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if len([element for element in ['a', 'b'] if element in teilaufg]) > 0:
        # Die SuS sollen den Ableitungsgraphen für einen vorgegebenen Graphen skizzieren.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        punkte = 3
        nst_1 = zzahl(1, 3)
        nst_2 = nst_1 + nzahl(1, 3) + 0.5
        nst_3 = nst_1 - nzahl(2, 3) - 0.5
        faktor = zzahl(3, 8) / 2
        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_abl = collect(expand(diff(fkt, x, 1)), x)

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))

        aufgabe.extend((beschriftung(teilaufg, i)
                           + f'Skizzieren Sie im Koordinatensystem den Graphen der Ableitungsfunktion.', 'Figure'))
        loesung.extend((beschriftung(teilaufg,i, True)
                        + r' \mathrm{~Graph~der~Ableitungsfunktion~(2BE)} ', 'Figure'))
        Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        Graph(xmin, xmax, fkt, fkt_abl, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')

        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen ihre Skizze begründen. Die Teilaufgabe wird nur angezeigt, wenn Teilaufgabe a) ausgewählt ist.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_2 = collect(expand(diff(fkt, x, 2)), x)
        fkt_3 = collect(expand(diff(fkt, x, 3)), x)
        extrema = solve(fkt_1, x)
        wendepkt = solve(fkt_2, x)
        wendepkt_art = fkt_3.subs(x, wendepkt[0])
        if wendepkt_art < 0:
            art = (r' \mathrm{Es~ist~ein~ \mathbf{links-rechts-Wendepunkt},~deswegen~ist~das~Extrema~ein~Hochpunkt}'
                   + r' \quad (1BE) \\')
        else:
            art = (r' \mathrm{Es~ist~ein~ \mathbf{rechts-links-Wendepunkt},~deswegen~ist~das~Extrema~ein~Tiefpunkt}'
                   + r' \quad (1BE) \\')
        aufgabe.append(beschriftung(teilaufg, i) + f'Begründen Sie Ihre Skizze. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Extrema~an~Stelle~} \bm{x_1~=~'
                       + gzahl(N(extrema[0],3)) + r'} \mathrm{~und~} \bm{x_2 ~=~' + gzahl(N(extrema[1], 3))
                       + r'} \mathrm{~sind~Nullstellen~der~Ableitung \quad (1BE)} \\'
                       + r' \mathrm{Wendepunkte~an~Stelle~} \bm{x_w~=~' + gzahl(N(wendepkt[0], 3))
                       + r'} \mathrm{~ist~Extrema~der~Ableitung \quad (1BE)} \\' + art
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')

        liste_punkte.append(punkte)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ableitungen(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Die SuS sollen mithilfe der Ableitungsregeln die Ableitungen verschiedener Funktionen bestimmen.
    # Mithilfe von "teilaufg=[]" können folgenden Funktionstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) ganzrationales Polynom
    # b) rationales Polynom
    # c) Wurzelfunktion
    # d) Polynom mit Wurzelfunktion
    # e) Exponentialfunktion
    # f) Logarithmusfunktion
    # g) Exponentialfunktion mit Wurzel
    # h) verkettete Expoenentialfunktion
    # i) verkettete Logarithmusfunktion
    # j) verkettete Wurzelfunktion
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{str(nr)}']

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Berechne die Ableitung der folgenden Funktionen mithilfe der elementaren Ableitungsregeln.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def polynom():  # erzeugt eine Funktion und deren Ableitungen mit p Summanden
        p = nzahl(1, 2)
        fkt = nzahl(1,9)
        koeffizienten = faktorliste(p, 1, 15)
        potenzen = exponenten(p)
        pkt = p
        for koeffizient in koeffizienten:
            fkt = koeffizient * (x ** potenzen.pop()) + fkt
        fkt = collect(fkt, x)
        fkt_uf = ''
        fkt_abl = collect(expand(diff(fkt, x)), x)
        fkt_2 = collect(expand(diff(fkt, x, 2)), x)
        return latex(fkt), fkt_uf, latex(fkt_abl), pkt

    def polynom_rational():
        a1 = zzahl(3, 15)
        e1 = nzahl(2, 6)
        fkt = r' \frac{' + gzahl(a1) + '}{x^{' + gzahl(e1) + '}}'
        fkt_uf = '~=~' + gzahl(a1) + r'\cdot x^{' + gzahl(-1 * e1) + '}'
        fkt_abl = gzahl(-1 * a1 * e1) + r' \cdot x^{' + gzahl(-1 * e1 - 1) + '}'
        pkt = 1
        return fkt, fkt_uf, fkt_abl, pkt

    def wurzel():
        a1 = zzahl(2, 15)
        e1, e2 = exponenten(2)
        fkt = gzahl(a1) + r' \sqrt[' + gzahl(e1) + ']{x^{' + gzahl(e2) + '}}'
        fkt_uf = '~=~' + gzahl(a1) + r' \cdot x^{ \frac{' + gzahl(e2) + '}{' + gzahl(e1) + '}}'
        fkt_abl = (gzahl(Rational(a1 * e2, e1)) + r' \cdot x^{'
                       + gzahl(Rational(e2, e1) - 1) + '}')
        pkt = 1
        return fkt, fkt_uf, fkt_abl, pkt

    def poly_wurzel():
        a1, a2, a3 = faktorliste(3, 3, 12)
        e1, e2, e3 = exponenten(3)
        fkt = (vorz_aussen(a1 / a2) + r' \frac{' + gzahl(abs(a1)) + '}{' + gzahl(abs(a2)) + r'x^{'
                   + gzahl(e1) + '}}' + vorz(a3) + r' \frac{' + gzahl(abs(a3)) + r'}{ \sqrt[' + gzahl(e2) + r']{'
                   + r'x^{' + gzahl(e3) + '}}}')
        fkt_uf = ('~=~' + vorz_v_aussen(Rational(a1, a2), 'x^{' + gzahl(-1 * e1) + '}')
                      + vorz_v_innen(a3, 'x^{' + gzahl(Rational(-1 * e3, e2)) + '}'))
        fkt_abl = (vorz_v_aussen(Rational(-1 * a1 * e1, a2), 'x^{' + gzahl(-1 * e1 - 1) + '}')
                       + vorz_v_innen(Rational(-1 * a3 * e3, e2), 'x^{' + gzahl(Rational(-1 * (e3 + e2), e2)) + '}'))
        pkt = 2
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_exp():
        punkte = 2
        faktor_exp = zzahl(2, 8)
        pkt = 2
        fkt = 'x^{' + gzahl(faktor_exp) + r'} \cdot e^{x}'
        fkt_uf = ''
        fkt_abl = (gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                   + r'} \cdot e^{x} ~+~x^{' + gzahl(faktor_exp) + r'} \cdot e^{x} ~=~ e^{x} \cdot \big( '
                   + gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1) + '} + x^{' + gzahl(faktor_exp)
                   + r'} \big)')
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_ln():
        pkt = 3
        faktor_exp = zzahl(2, 8)
        fkt = 'x^{' + gzahl(faktor_exp) + r'} \cdot \ln(x)'
        fkt_uf = ''
        fkt_abl = (gzahl(faktor_exp) + 'x^{' + gzahl(faktor_exp - 1)
                   + r'} \cdot \ln(x) ~+~ x^{' + gzahl(faktor_exp) + r'} \cdot x^{-1} ~=~'
                   + 'x^{' + gzahl(faktor_exp - 1) + r'} \cdot (' + gzahl(faktor_exp)
                   + r' \cdot \ln(x) ~+~ 1)')
        return fkt, fkt_uf, fkt_abl, pkt

    def fkt_wurzel_exp():
        pkt = 3
        faktor_exp = zzahl(2, 8)
        faktor_sqrt = nzahl(2, 8)
        while abs(faktor_exp) == faktor_sqrt:
            faktor_sqrt = nzahl(2, 8)
        fkt = r' \sqrt[' + gzahl(faktor_sqrt) + ']{x^{' + gzahl(faktor_exp) + r'}} \cdot e^{x}'
        fkt_uf = (r'~=~x^{' + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} \cdot e^{x}')
        fkt_abl = (gzahl(Rational(faktor_exp, faktor_sqrt)) + r' \cdot x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt) - 1) + r'} \cdot e^{x} ~+~' + 'x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + r'} \cdot e^{x} ~=~ e^{x} \cdot ('
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + r' \cdot x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt) - 1) + r'} ~+~ x^{'
                   + gzahl(Rational(faktor_exp, faktor_sqrt)) + '})')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_exp():
        pkt = 3
        exponent = zzahl(2, 8)
        faktor_1 = zzahl(2, 8)
        faktor_2 = zzahl(1, 8)
        fkt = ('e^{' + vorz_v_aussen(faktor_1, 'x') + '^{' + gzahl(exponent) + r'}'
               + vorz_v_innen(faktor_2, 'x') + '}')
        fkt_uf = ''
        fkt_abl = ('e^{' + vorz_v_aussen(faktor_1, 'x') + '^{' + gzahl(exponent) + r'}'
                    + vorz_v_innen(faktor_2, 'x') + r'} \cdot (' + vorz_v_aussen(faktor_1 * exponent, 'x')
                       + '^{' + gzahl(exponent - 1) + r'}' + vorz_str(faktor_2) + r')')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_ln():
        pkt = 3
        exponent = zzahl(2, 8)
        faktor_1 = zzahl(2, 8)
        faktor_2 = zzahl(1, 8)
        fkt = (r' \ln(' + vorz_v_aussen(faktor_1, 'x^{' + gzahl(exponent) + r'}')
               + vorz_v_innen(faktor_2, 'x') + ')')
        fkt_uf = ''
        fkt_abl = (r' \frac{1}{' + vorz_v_aussen(faktor_1, 'x') + '^{'
                   + gzahl(exponent) + r'}' + vorz_v_innen(faktor_2, 'x') + r'} \cdot ('
                   + vorz_v_aussen(faktor_1 * exponent, 'x') + '^{' + gzahl(exponent - 1) + r'}'
                   + vorz_str(faktor_2) + r')')
        return fkt, fkt_uf, fkt_abl, pkt

    def verkettet_wurzel():
        pkt = 3
        exponent = zzahl(2, 8)
        wurzel = nzahl(2, 8)
        faktor = zzahl(1, 10)
        while abs(exponent) == wurzel:
            wurzel = nzahl(2, 8)
        summand = zzahl(1, 8)
        fkt = (r' \sqrt[' + gzahl(wurzel) + ']{' + vorz_v_aussen(faktor, 'x^{' + gzahl(exponent) + '}')
               + vorz_str(summand) + '}')
        fkt_uf = ('~=~(' + vorz_v_aussen(faktor, 'x') + '^{' + gzahl(exponent) + r'} '
                  + vorz_str(summand) + r')^{' + gzahl(Rational(1, wurzel)) + '}')
        fkt_abl = (r' \left(' + vorz_v_aussen(Rational(faktor * exponent, wurzel), 'x')
                   + '^{' + gzahl(exponent - 1) + r'} \right) \cdot (' + vorz_v_aussen(faktor, 'x')
                   + '^{' + gzahl(exponent) + r'} ' + vorz_str(summand) + r')^{'
                   + gzahl(Rational(1 - wurzel, wurzel)) + r'}')
        return fkt, fkt_uf, fkt_abl, pkt

    if anzahl != False:
        if type(anzahl) != int:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        else:
            anzahl = 26 if anzahl > 26 else anzahl
            teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        if type(wdh) != int or len(teilaufg)*wdh > 26:
            exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
                 "26 Teilaufgaben ergeben.")
        else:
            print(teilaufg)
            anzahl = 26 if anzahl > 26 or anzahl == False else anzahl
            teilaufg = repeat(teilaufg, wdh, laenge=anzahl)
            print(teilaufg)

    aufgaben = {'a': polynom, 'b': polynom_rational, 'c': wurzel, 'd': poly_wurzel, 'e': fkt_exp,
                'f': fkt_ln, 'g': fkt_wurzel_exp, 'h': verkettet_exp, 'i': verkettet_ln,
                'j': verkettet_wurzel}

    aufg = ''
    lsg = (r' \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe'
           r'~der~elementaren~Ableitungsregeln.} \\')
    punkte = 0

    for element in teilaufg:
        fkt, fkt_uf, fkt_abl, pkt = aufgaben[element]()
        if (i+1) % 3 != 0:
            aufg = aufg + beschriftung(teilaufg,i, True) + r' f(x)~=~' + fkt
            if i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and i+1 != len(teilaufg):
            aufg = aufg + beschriftung(teilaufg,i, True) + r' f(x)~=~' + fkt + r' \\\\'
        else:
            aufg = aufg + beschriftung(teilaufg,i, True) + r' f(x)~=~' + fkt
        lsg = (lsg + beschriftung(teilaufg,i, True) + r' f(x) ~=~' + fkt + fkt_uf
               + r' \quad \to \quad \bm{f^{ \prime }(x)~=~ ' + fkt_abl + r'} \quad (' + str(pkt) + r'BE) \\')
        punkte += pkt
        i += 1

    lsg = lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}'
    aufgabe.append(aufg)
    loesung.append(lsg)
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def anwend_abl_seilbahn(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS verschiedene Anwendungen der Ableitung am Beispiel eines Hügels, dessen Gipfel mit einer Seilbahn erreicht werden kann, kennenlernen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    y_wert_s = 0
    while y_wert_s > 5 or y_wert_s < 1:
        x_wert_x1 = nzahl(4, 8) / 2
        x_wert_x2 = x_wert_x1 + nzahl(4, 8) / 2
        x_wert_s = 0.5 * (x_wert_x2 + x_wert_x1)
        faktor = -1 * nzahl(2, 8) / 2
        fkt = collect(expand(faktor * (x - x_wert_x1) * (x - x_wert_x2)),x)

        y_wert_s = fkt.subs(x, x_wert_s)

    fkt_str = (vorz_v_aussen(faktor, 'x^2') + vorz_v_innen(-1 * faktor * (x_wert_x1 + x_wert_x2), 'x')
               + vorz_str(faktor * x_wert_x1 * x_wert_x2))
    p_fkt = -1 * (x_wert_x1 + x_wert_x2)
    q_fkt = x_wert_x1 * x_wert_x2
    fkt_str_pq = 'x^2~' + vorz_str(p_fkt) + 'x~' + vorz_str(q_fkt)
    fkt_abl = diff(fkt, x, 1)
    fkt_abl_str = str(2 * faktor) + 'x~' + vorz_str(-1 * faktor * (x_wert_x1 + x_wert_x2))
    m_tangente_str = Rational(y_wert_s,(x_wert_s - 1))
    m_tangente = y_wert_s/(x_wert_s - 1)
    fkt_tangente = N(m_tangente,3) * x - N(m_tangente,3)
    #print(fkt_tangente)
    x_wert_schnittpunkt = solve(Eq(fkt, fkt_tangente), x)
    y_wert_schnittpunkt = fkt_tangente.subs(x, x_wert_schnittpunkt[0])
    # Werte für die Grafik
    xwerte = [x_wert_x1 + x/10 for x in range(int((x_wert_x2 - x_wert_x1)*10)+1)]
    ywerte_huegel = [fkt.subs(x, element) for element in xwerte]
    xwerte_gerade = [1, x_wert_schnittpunkt[0]]
    ywerte_gerade = [0, y_wert_schnittpunkt]
    # Erzeugen der Grafik
    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect(1/2)
    plt.plot(xwerte_gerade, ywerte_gerade)
    plt.plot(xwerte, ywerte_huegel)
    # plt.show()
    plt.savefig('img/temp/' + str(nr), dpi=200, bbox_inches="tight", pad_inches=0.02)

    # plt.plot(xwerte, ywerte_huegel, x_wert_s, fkt, '$f(x) =' + latex(fkt) + '$', 'Hügel', 'Aufgabe_3')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'In der folgenden Abbildung ist die Profilkurve eines Hügels aufgetragen, '
               'dessen Gipfel mit einer Seilbahn erreicht werden kann.', 'Grafik',
               r' \mathrm{ f(x)~=~' + fkt_str + '}']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [str(nr)]
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS die Nullstellen, bei gegebener Funktionsgleichung, des Hügels berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Fußpunkte des Hügels. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                       + r' \quad \vert ~ \div ~' + gzahl_klammer(faktor) + r' \\ 0~=~'
                       + fkt_str_pq + r' \quad (2BE) \\ x_{^1/_2} ~=~ - ~ \frac{' + gzahl_klammer(N(p_fkt, 4))
                       + r'}{2} \pm' + r' \sqrt{ \left( \frac{' + str(N(p_fkt, 4)) + r'}{2} \right) ^2'
                       + vorz_str(N(-1 * q_fkt, 4)) + r'} ~=~' + str(N(-0.5 * p_fkt, 4)) + r' \pm '
                       + gzahl_klammer(N(sqrt((p_fkt * 0.5) ** 2 - q_fkt), 4)) + r' \quad (2BE) \\'
                       + r' x_1 ~=~ \mathbf{' + str(x_wert_x1) + r'} \quad \mathrm{und} \quad x_2 ~=~\mathbf{'
                       + str(x_wert_x2) + r'} \quad (1BE) \quad \mathbf{P_1(' + str(x_wert_x1)
                       + r' \vert 0)} \quad \mathrm{und} \quad \mathbf{P_2(' + str(x_wert_x2)
                       + r' \vert 0)} \quad (1BE) \\\\')
        liste_punkte.append(5)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Steigung und den Steigungswinkel am westlichen Fußpunkt des Hügels berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        m_x1 = fkt_abl.subs(x, x_wert_x1)
        #print('m_x1 = ' + str(m_x1))
        winkel_x1 = math.degrees(N(atan(m_x1),2))
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Steigung und den Steigungswinkel '
                       + 'am westlichen Fußpunkt. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime } (x) ~=~ ' + fkt_abl_str
                       + r' \quad \to \quad f^{ \prime } (' + str(x_wert_x1) + r') ~=~ \mathbf{' + str(N(m_x1,3))
                       + r'} \quad (2BE) \\' + r' \alpha ~=~ arctan(' + str(N(m_x1,3)) + r') ~=~ \mathbf{'
                       + str(N(winkel_x1,3)) + r'^{ \circ }} \quad (2BE) \\\\')
        liste_punkte.append(4)
        i += 1

    if len([element for element in ['c', 'd', 'e'] if element in teilaufg]) > 0:
        # Hier sollen die SuS den Schnittpunkt zwischen Seilbahn (lineare Fkt.) und Hügel (quadratische Fkt.) berechnen. Diese Teilaufgabe wird immer angezeigt, wenn 'd' oder 'e' in 'teilaufg=['d', 'e']' enthalten sind.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        fkt_tp = fkt - fkt_tangente
        fkt_tp_str = (str(faktor) + 'x^2~' + vorz_str(N(-1 * faktor * (x_wert_x1 + x_wert_x2) - m_tangente,3)) + 'x~'
                      + vorz_str(N(faktor * x_wert_x1 * x_wert_x2 + m_tangente,3)))
        p_fkt_tp = -1 * (x_wert_x1 + x_wert_x2) - m_tangente/faktor
        q_fkt_tp = x_wert_x1 * x_wert_x2 + m_tangente/faktor
        fkt_tp_pq = ('x^2~' + vorz_str(N(-1 * (x_wert_x1 + x_wert_x2) - m_tangente/faktor,3)) + 'x~'
                      + vorz_str(N(x_wert_x1 * x_wert_x2 + m_tangente/faktor,3)))
        x_werte_tp = solve(fkt_tp,x)
        y_wert_tp = fkt.subs(x, x_werte_tp[0])
        #print(x_werte_tp[0], x_werte_tp[1])
        aufgabe.append(beschriftung(teilaufg,i) + 'Die Seilbahn startet bei B(1|0). '
                       +'Berechnen Sie den Treffpunkt mit dem Hügel, wenn die Steigung')
        aufgabe.append(r' \mathrm{m~=~}' + latex(m_tangente_str) + r' \mathrm{~beträgt}. \hspace{38em}')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{B~und~m~einsetzen~in~}  t(x)~=~m~x~+~n \to \quad '
                       + r' 0 ~=~' + latex(N(m_tangente,3)) + r' \cdot 1 ~+~n \quad \vert '
                       + vorz_str(N(-1 * m_tangente,3)) + r' \quad (1BE) \\ n ~=~' + vorz_str(N(-1 * m_tangente,3))
                       + r' \quad t(x)~=~' + str(N(m_tangente,3)) + r' \cdot x ' + vorz_str(N(-1 * m_tangente,3))
                       + r' \quad (2BE) \\' + fkt_str + '~=~' + latex(fkt_tangente) + r'~ \vert -('
                       + latex(fkt_tangente) + r') \quad (1BE) \\' + ' 0 ~=~ ' + fkt_tp_str + r'~ \vert \div '
                       + gzahl_klammer(faktor) + r' \quad \to \quad 0~=~'
                       + fkt_tp_pq + r' \quad (1BE) \\ x_{^1/_2} ~=~ - ~ \frac{' + gzahl_klammer(N(p_fkt_tp, 3))
                       + r'}{2} \pm' + r' \sqrt{ \left( \frac{' + str(N(p_fkt_tp, 3)) + r'}{2} \right) ^2'
                       + vorz_str(N(-1 * q_fkt_tp, 3)) + r'} ~=~' + str(N(-0.5 * p_fkt_tp, 3)) + r' \pm '
                       + gzahl_klammer(N(sqrt((p_fkt_tp * 0.5) ** 2 - q_fkt_tp), 3)) + r' \quad (2BE) \\'
                       + r' x_1 ~=~\mathbf{' + str(N(x_werte_tp[0],3)) + r'} \quad \mathrm{und} \quad x_2 ~=~\mathbf{'
                       + str(N(x_werte_tp[1],3)) + r'} \quad (1BE) \quad \mathbf{P_1(' + str(N(x_werte_tp[0],3))
                       + r' \vert' + str(N(y_wert_tp,3)) + r')} \quad (1BE) \\\\')
        liste_punkte.append(9)
        i += 1

    if len([element for element in ['d', 'e'] if element in teilaufg]) > 0:
        # Hier sollen die SuS den Schnittwinkel zwischen Seilbahn (lineare Fkt.) und Hügel (quadratische Fkt.) berechnen. Diese Teilaufgabe wird immer angezeigt, wenn 'e' in 'teilaufg=['e']' enthalten ist.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pkt = 0
        m_fkt_x_tp = fkt_abl.subs(x, x_werte_tp[0])
        winkel_alpha = N(math.degrees(atan(m_fkt_x_tp)),3)
        winkel_beta = N(math.degrees(atan(m_tangente)),3)
        loesung_1 = (r' \gamma ~=~ \vert ' + str(winkel_beta) + r'^{ \circ }~-~' + gzahl_klammer(winkel_alpha)
                   + r'^{ \circ } \vert ~=~\mathbf{' + str(abs(winkel_beta-winkel_alpha)) + r'^\circ} \quad (2BE) \\\\')
        if abs(winkel_beta-winkel_alpha) > 90:
            loesung_1 = (r' \gamma ~=~ \vert ' + str(winkel_beta) + r'^{ \circ }~-~' + gzahl_klammer(winkel_alpha)
                         + r'^{ \circ } \vert ~=~' + str(abs(winkel_beta - winkel_alpha))
                         + r'^{ \circ } \quad \to \quad \gamma ~=~ 180^{ \circ } ~-~'
                         + str(abs(winkel_beta - winkel_alpha)) + r'^{ \circ } ~=~ \mathbf{'
                         + str(180 - abs(winkel_beta - winkel_alpha)) + r'^{ \circ }} \quad (2BE) \\\\')
            pkt += 1
        # print(m_fkt_x_tp)
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Schnittwinkel der Seilbahn mit dem Hügel. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime } (x) ~=~ ' + fkt_abl_str + r' \quad \to \quad f^{ \prime } ('
                       + str(N(x_werte_tp[0],3)) + r') ~=~ ' + str(N(m_fkt_x_tp,3))
                       + r' \quad (1BE) \quad \to \quad ' + r' \alpha ~=~ arctan(' + str(N(m_fkt_x_tp,3))+ ') ~=~'
                       + latex(winkel_alpha) + r'^{ \circ } \quad (2BE) \\'
                       + r' t^{ \prime}(x) ~=~' + str(N(m_tangente,3)) + r' \quad \to \quad '
                       + r' \beta ~=~ arctan(' + str(N(m_tangente,3))+ ') ~=~' + latex(winkel_beta)
                       + r'^{ \circ } \quad (2BE) \\' + loesung_1)
        pkt += 6
        liste_punkte.append(pkt)
        i += 1

    if 'e' in teilaufg:
        # Hier sollen die SuS die Funktionsgleichung der Seilbahn (lineare Funktion) mithilfe der Steigung rekonstruieren.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den  Startpunkt der Seilbahn, damit sie am '
                       + 'Schnittpunkt die Steigung des Hügels besitzt. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{aus~} f^{ \prime } ('
                       + str(N(x_werte_tp[0],3)) + ') ~=~ ' + str(N(m_fkt_x_tp,3)) + r' \mathrm{~und~} P_1('
                       + str(N(x_werte_tp[0],3)) + r' \vert' + str(N(y_wert_tp,3))
                       + r') \mathrm{~folgt~} \quad \to \quad ' + str(N(y_wert_tp,3)) + '~=~'
                       + str(N(m_fkt_x_tp,3)) + r' \cdot ' + gzahl_klammer(N(x_werte_tp[0],3))
                       + r'+~n \quad \vert ' + vorz_str(N(-1*m_fkt_x_tp*x_werte_tp[0],3)) + r' \quad n~=~'
                       + latex(N(y_wert_tp-m_fkt_x_tp*x_werte_tp[0],3))
                       + r' \quad (3BE) \\ x_0 ~=~ - \frac{n}{m} ~=~ - \frac{'
                       + str(N(y_wert_tp-m_fkt_x_tp*x_werte_tp[0],3)) + '}{'+ str(N(m_fkt_x_tp,3))
                       + r'} ~=~ \mathbf{' + str(N(-1*((y_wert_tp-m_fkt_x_tp*x_werte_tp[0])/m_fkt_x_tp),3))
                       + r'} \quad (2BE) \\\\')

        liste_punkte.append(5)
        i += 1

    if 'f' in teilaufg:
        # Hier sollen de SuS den Scheitelpunkt einer Parabel mit quadratischer Ergänzung bestimmen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Höhe des Hügels. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f(x)~=~' + fkt_str + '~=~' + gzahl(faktor)
                       + r' \cdot (~x^2~' + vorz_str(p_fkt) + '~x)~' + vorz_str(faktor*q_fkt) + r' \quad (1BE) \\ ~=~'
                       + str(faktor) + r' \cdot (~x^2~' + vorz_str(p_fkt) + '~x~'
                       + vorz_str((p_fkt/2)**2) + vorz_str(-1*(p_fkt/2)**2) + ')'
                       + vorz_str(faktor*q_fkt) + r' \quad (1BE) \\ ~=~' + gzahl(faktor) + r' \cdot ((x'
                       + vorz_str(-1*x_wert_s) + ')^2' + vorz_str(-1 * (p_fkt / 2) ** 2) + ')'
                       + vorz_str(faktor * q_fkt) + '~=~' + gzahl(faktor)
                       + '(~x~' + vorz_str(-1*x_wert_s) + r'~)^2 \mathbf{' + vorz_str(y_wert_s)
                       + r'} \quad (1BE) \\ \mathrm{Die~Höhe~beträgt~' + gzahl(y_wert_s) +  r'.} \quad (1BE)')
        liste_punkte.append(4)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def anwendung_abl_steig(nr, teilaufg=['a', 'b'], i=0, BE=[]):
    # Die SuS sollen mithilfe der Ableitung den Wert von x bzw. der Variablen a bestimmen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen den x-Wert berechnen, an dem eine (rationale) Funktion die gegebene Steigung besitzt.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        steigung = 0
        while steigung == 0:
            try:
                a1, a2, a3 = faktorliste(3, 2, 8)
                e1 = (nzahl(2,4)*2)-1
                e2 = e1 + (nzahl(0,2)*2)+1
                funktionen_liste = ([[a1*x**2 + a2*x + a3, str(a1) + 'x^2' + vorz_str(a2) + 'x' + vorz_str(a3), str(2*a1) + r'x' + vorz_str(a2)],
                                     [a1/(x**e1),r' \frac{' + str(a1) + '}{x^{' + str(e1) + '}}',
                                      str(-1 * a1 * e1) + r' \cdot x^{' + str(-1 * e1 - 1) + '}'],
                                     [a1 * x ** (e1 / e2), str(a1) + r' \sqrt[' + str(e1) + ']{x^{' + str(e2) + '}}',
                                      latex(Rational(a1 * e2, e1)) + r' \cdot x^{' + latex(Rational(e2,e1) - 1) + '}']])

                Aufgabe = random.randint(0, 2)
                # Aufgabe = 1
                funktion_liste = funktionen_liste[Aufgabe]
                fkt, fkt_str, fkt_abl_str = funktion_liste[0], funktion_liste[1], funktion_liste[2]
                fkt_abl = diff(fkt, x)
                stelle = nzahl(3, 10)/2
                steigung = int(fkt_abl.subs(x, stelle))
            except TypeError as te:
                print(te)
                steigung = 0

        loesung_liste = [r' \quad f ^ { \prime} (x) ~ = ~' + str(fkt_abl_str) + '~ = ~' + str(steigung) + r'~ \vert ~-~'
                         + gzahl_klammer(a2) + r'~ \vert \div ' + gzahl_klammer(2 * a1) + r' \quad \to \quad x~=~\mathbf{'
                         + latex(N((steigung-a2)/(2*a1),3)) + r'} \quad (3BE)',
                         r' \quad f ^ { \prime} (x) ~ = ~' + str(fkt_abl_str) + '~ = ~' + str(steigung) + r'~ \vert \div'
                         + gzahl_klammer(-1*a1*e1) + r'~ \vert ~(~)^{' + str(Rational(1,-1*e1-1)) + r'} \quad \to \quad x~=~ \big('
                         + latex(Rational(steigung,-1*a1*e1)) + r' \big) ^{' + latex(Rational(1,-1*e1-1)) + r'} ~=~\mathbf{'
                         + latex(N(((steigung/(-1*a1*e1))**(1/(-1*e1-1))), 3)) + r'} \quad (3BE)',
                         r' \quad f ^ { \prime} (x) ~ = ~' + str(fkt_abl_str) + '~ = ~' + str(steigung) + r'~ \vert \div'
                         + gzahl_klammer(Rational(a1 * e2, e1)) + r'~ \vert ~(~)^{' + latex(N(1/((e2-e1)/e1), 3))
                         + r'} \quad \to \quad x~=~ \left(' + latex(Rational(steigung*e1, a1 * e2))
                         + r' \right) ^{ ' + latex(N(1/((e2-e1)/e1), 3)) + r'} ~=~ \mathbf{'
                         + latex(N(((steigung*e1)/(a1 * e2))**(1/((e2-e1)/e1)), 3)) + r'} \quad (3BE)']

        loesung_1 = loesung_liste[Aufgabe]
        aufgabe.append(beschriftung(teilaufg,i)
                       + f'Berechnen Sie den Wert x, an der die Funktion f die Steigung m hat. ')
        aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{und} \quad m~=~' + str(steigung) + r' \hspace{20em} \\')
        loesung.append(beschriftung(teilaufg,i, True) + loesung_1)
        liste_punkte.append(3)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen den Wert von a einer quadratischen Parameterfunktion berechnen, an dem diese eine lineare Funktion berührt.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        a1, a2, a3 = faktorliste(3, 3, 10)
        verschiebung = zzahl(2,10)/2
        fkt_parabel, fkt_str_parabel, fkt_abl_str_parabel = (a1 * x ** 2 + a, str(a1) + 'x^2 + a', str(2*a1) + 'x')
        fkt_gerade, fkt_str_gerade, fkt_abl_str_gerade = (a2*x+a3, str(a2) + 'x' + vorz_str(a3), str(a2))

        aufgabe.append(beschriftung(teilaufg,i)
                       + f'Berechnen Sie den Wert von a, für den sich beide Funktionen berühren.')
        aufgabe.append(r'f(x)~=~' + fkt_str_parabel + r' \quad \mathrm{und} \quad g(x)~=~' + fkt_str_gerade
                       + r' \hspace{15em}')
        loesung.append(beschriftung(teilaufg,i, True) + r' f ^{ \prime} (x) ~ = ~ g ^{ \prime } (x) \quad \to \quad '
                         + fkt_abl_str_parabel + '~ = ~' + fkt_abl_str_gerade + r' \quad \to \quad \vert \div '
                         + gzahl_klammer(2*a1) + r' \quad \to \quad x~=~' + latex(Rational(a2,(2*a1)))
                         + r' \quad (3BE) \\' + r' \quad f(' + latex(Rational(a2,(2*a1)))
                         + r') ~ = ~ g(' + latex(Rational(a2,(2*a1))) + r') \quad \to \quad '
                         + str(a1) + r' \cdot \left(' + latex(Rational(a2,(2*a1))) + r' \right) ^2 + a ~=~'
                         + str(a2) + r' \cdot \left( ' + latex(Rational(a2,(2*a1))) + r' \right)' + vorz_str(a3)
                         + r' \quad \vert ' + vorz_str(N(-1 * (a2**2)/(4*a1),3))
                         + r' \quad \to \quad a~=~ \mathbf{' + latex(N((a2**2/(2*a1)) + a3 - (a2**2)/(4*a1),3))
                         + r'} \quad (3BE)')
        liste_punkte.append(6)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rekonstruktion_und_extremalproblem(nr, teilaufg=['a', 'b', 'c'], gleichung=True, i=0, BE=[]):
    # Den SuS ist ein Grah einer quadratischen Funktion gegeben, dessen Funktionsgleichung Sie rekonstruieren müssen, um damit ein Extremalproblem zu lösen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'gleichung=' kann festgelegt, ob den SuS die Funktionsgleichung aus Teilaufgabe a) bei b) gegeben ist. Wurde Teilaufgabe a) nicht ausgewählt, ist die Funktionsgleichung automatisch gegeben.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    # hier wird die Funktion erstellt.
    loesung_vektor = [1/3,1/5,1/7]
    while vektor.rational(loesung_vektor,10) != True:
        xwert_1 = -1 * nzahl(1,3)
        ywert_1 = nzahl(3,8)
        xwert_2 = nzahl(1,3)
        ywert_2 = ywert_1 + nzahl(2,6)
        xwert_3 = xwert_2 + nzahl(1,3)
        ywert_3 = nzahl (2,8)

        A = np.array([[xwert_1 ** 2, xwert_1, 1],
                         [xwert_2 ** 2, xwert_2, 1],
                         [xwert_3 ** 2, xwert_3, 1]])

        b = np.array([ywert_1, ywert_2, ywert_3])
        loesung_vektor = slv(A, b)
    [x_1, x_2, x_3] = loesung_vektor
    fkt = x_1 * x**2 + x_2 * x + x_3
    fkt_str = vorz_v_aussen(x_1,'x') + '^2' + vorz_v_innen(x_2,'x') + vorz_str(x_3)
    fkt_a = fkt*x
    fkt_a_str = vorz_v_aussen(x_1,'x') + '^3' + vorz_v_innen(x_2,'x') + '^2' + vorz_v_innen(x_3,'x')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen '
               'Rechtecks auf dem Graphen von f.', 'Figure']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = [f'Aufgabe_{nr}']
    grafiken_loesung = []
    # grafische Darstellung des Sachverhaltes
    xmax = solve(fkt, x)[1]
    def Darstellung(fkt, xmax, xwert_p, ywert_p, name):
        fig, ax = plt.subplots()
        fig.canvas.draw()
        fig.tight_layout()
        plt.grid()
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
        plt.annotate(r'$ P( x \vert y ) $', xy=(xwert_p, ywert_p),
                     xycoords='data', xytext=(+10, +10), textcoords='offset points', fontsize=16)
        xwerte = np.arange(0, xmax, 0.01)
        ywerte = [fkt.subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte)
        plt.plot([0, xwert_p], [ywert_p, ywert_p])
        plt.plot([xwert_p, xwert_p], [ywert_p, 0])
        plt.scatter([xwert_p, ], [ywert_p, ], 50, color='blue')
        return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0.02)

    Darstellung(fkt, xmax, xwert_2, ywert_2, f'Aufgabe_{nr}')

    if 'a' in teilaufg:
        # Den SuS sollen mithilfe drei gegebener Punkte eine quadratischen Funktion rekonstruieren. Da nicht der Scheitelpunkt gegeben ist, müssen die SuS das Gaußverfahren nutzen.
        punkte = 16
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # Rekonstruktion der Funktion
        # Zeilen 1 bis 3 vom LGS:

        a1 = xwert_1 ** 2
        b1 = xwert_1
        c1 = 1
        d1 = ywert_1


        a2 = xwert_2 ** 2
        b2 = xwert_2
        c2 = 1
        d2 = ywert_2

        a3 = xwert_3 ** 2
        b3 = xwert_3
        c3 = 1
        d3 = ywert_3

        # Zeile 4 und 5 vom LGS:

        z4 = NoEscape(gzahl(a1) + r'$ \cdot II' + vorz_str(-1 * a2) + r' \cdot I $')
        a4 = 0
        b4 = a1 * b2 - a2 * b1
        c4 = a1 - a2
        d4 = a1 * d2 - a2 * d1

        z5 = NoEscape(gzahl(a1) + r'$ \cdot III' + vorz_str(-1 * a3) + r' \cdot I $')
        a5 = 0
        b5 = a1 * b3 - a3 * b1
        c5 = a1 - a3
        d5 = a1 * d3 - a3 * d1

        # Zeile 6 vom LGS:

        z6 = NoEscape(gzahl(b4) + r'$ \cdot III' + vorz_str(-1 * b5) + r' \cdot II $')
        b6 = 0
        c6 = b4 * c5 - b5 * c4
        d6 = b4 * d5 - b5 * d4

        # Lösungen des LGS:

        lsg_c = d6 / c6
        lsg_b = (d4 - (c4 * lsg_c)) / b4
        lsg_a = (d1 - (c1 * lsg_c) - (b1 * lsg_b)) / a1

        table2 = Tabular('c|c|c|c|c|c|c|c', row_height=1.2)
        table2.add_hline(2, 7)
        table2.add_row('Berechnung mit Gauß-Algorithmus','Nr.', 'Berechnung', 'a', 'b', 'c', 'lsg', '')
        table2.add_hline(2, 7)
        table2.add_row('','I', ' ', gzahl(a1), gzahl(b1), gzahl(c1), gzahl(d1), '')
        table2.add_row('', 'II', ' ', gzahl(a2), gzahl(b2), gzahl(c2), gzahl(d2), '')
        table2.add_row('', 'III', ' ', gzahl(a3), gzahl(b3), gzahl(c3), gzahl(d3), '')
        table2.add_hline(2, 7)
        table2.add_row('', 'II', z4, gzahl(a4), gzahl(b4), gzahl(c4), gzahl(d4), '(1BE)')
        table2.add_row('', 'III', z5, gzahl(a5), gzahl(b5), gzahl(c5), gzahl(d5), '(1BE)')
        table2.add_hline(2, 7)
        table2.add_row('', 'III', z6, ' ', gzahl(b6), gzahl(c6), gzahl(d6), '(1BE)')
        table2.add_hline(2, 7)

        # Aufgaben und Lösungen
        aufgabe.append('Von einer Funktion 2. Grades sind die folgenden Punkte gegeben:  S( ' + gzahl(xwert_1) + ' | '
                       + gzahl(ywert_1) + ' ),  P( ' + gzahl(xwert_2) +  r' | '
                       + gzahl(ywert_2) + ' ) und Q( ' + gzahl(xwert_3)
                       + ' | ' + gzahl(ywert_3) + ' ) \n\n')
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Funktionsgleichung von f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Die~allgemeine~Funktionsgleichung~lautet:'
                       + r'~f(x)~=~ax^2~+~bx~+~c \quad (1BE) } \\'
                       + r' \mathrm{aus~den~gegebenen~Punkten~folgt:} \quad '
                       + r' \mathrm{I:~f(' + gzahl(xwert_1) + ')~=~' + gzahl(ywert_1) + r' \quad \to \quad '
                       + gzahl(xwert_1**2) + 'a' + vorz_str(xwert_1) + 'b + c ~=~' + gzahl(ywert_1)
                       + r' \quad (2BE)} \\ \mathrm{II:~f(' + gzahl(xwert_2) + ')~=~' + gzahl(ywert_2)
                       + r' \quad \to \quad ' + gzahl(xwert_2**2) + 'a' + vorz_str(xwert_2) + 'b + c ~=~'
                       + gzahl(ywert_2) + r' \quad (2BE)} \\ \mathrm{III:~f(' + gzahl(xwert_3) + ')~=~'
                       + gzahl(ywert_3) + r' \quad \to \quad ' + gzahl(xwert_3**2) + 'a' + vorz_str(xwert_3)
                       + 'b + c ~=~' + gzahl(ywert_3) + r' \quad (2BE) }')
        loesung.append(table2)
        if gleichung != True:
            punkte += 1
            loesung.append(r' \mathrm{aus~III~folgt:~' + gzahl(c6) + '~c~=~' + gzahl(d6) + r' \quad \vert \div '
                           + gzahl_klammer(c6) + r' \quad \to \quad c~=~' + latex(lsg_c) + r' \quad (2BE) } \\'
                           + r' \mathrm{aus~II~folgt:~' + gzahl(b4) + r'b~' + vorz_str(c4)
                           + r' \cdot ~' + gzahl_klammer(lsg_c) + '~=~' + gzahl(d4) + r' \quad \vert ~-~'
                           + gzahl_klammer(c4 * lsg_c) + r' \quad \vert \div ' + gzahl_klammer(b4)
                           + r' \quad \to \quad b~=~' + latex(lsg_b) + r' \quad (2BE) } \\'
                           + r' \mathrm{aus~I~folgt:~' + gzahl(a1) + r'~a~' + vorz_str(b1) + r' \cdot '
                           + gzahl_klammer(lsg_b) + vorz_str(c1) + r' \cdot ' + gzahl_klammer(lsg_c) + '~=~'
                           + gzahl(d1) + r' \quad \vert ~-~' + gzahl_klammer(b1 * lsg_b + c1 * lsg_c)
                           + r' \quad \vert \div ' + gzahl_klammer(a1) + r' \quad \to \quad a~=~' + latex(lsg_a)
                           + r' \quad (2BE) } \\ \to \quad f(x)~=~' + fkt_str + r' \quad  (1BE) \\ \mathrm{insgesamt~'
                           + str(punkte) + '~BE}')
        else:
            loesung.append(r' \mathrm{aus~III~folgt:~' + gzahl(c6) + '~c~=~' + gzahl(d6) + r' \quad \vert \div '
                           + gzahl_klammer(c6) + r' \quad \to \quad c~=~' + latex(lsg_c) + r' \quad (2BE) } \\'
                           + r' \mathrm{aus~II~folgt:~' + gzahl(b4) + r'b~' + vorz_str(c4)
                           + r' \cdot ~' + gzahl_klammer(lsg_c) + '~=~' + gzahl(d4) + r' \quad \vert ~-~'
                           + gzahl_klammer(c4 * lsg_c) + r' \quad \vert \div ' + gzahl_klammer(b4)
                           + r' \quad \to \quad b~=~' + latex(lsg_b) + r' \quad (2BE) } \\'
                           + r' \mathrm{aus~I~folgt:~' + gzahl(a1) + r'~a~' + vorz_str(b1) + r' \cdot '
                           + gzahl_klammer(lsg_b) + vorz_str(c1) + r' \cdot ' + gzahl_klammer(lsg_c) + '~=~'
                           + gzahl(d1) + r' \quad \vert ~-~' + gzahl_klammer(b1 * lsg_b + c1 * lsg_c)
                           + r' \quad \vert \div ' + gzahl_klammer(a1) + r' \quad \to \quad a~=~' + latex(lsg_a)
                           + r' \quad (2BE) } \\ \mathrm{insgesamt~' + str(punkte) + '~BE}')
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in ['b', 'c'] if element in teilaufg]) > 0:
        # Hier sollen die SuS einen Punkt auf dem Graphen berechnen, der ein Eckpunkt eines Rechtecks mit maximalen Flächeninhalt ist.

        punkte = 15
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # zwischenrechnungen
        fkt_1_a = 3 * x_1 * (x ** 2) + 2 * x_2 * x + x_3
        fkt_1_a_str = vorz_v_aussen(3 * x_1,'x^2') + vorz_v_innen(2 * x_2,'x') + vorz_str(x_3)
        fkt_1_a_p = Rational(2*x_2,3*x_1)
        fkt_1_a_p2 = Rational(x_2,3*x_1)
        fkt_1_a_q = Rational(x_3,3*x_1)
        fkt_1_a_pq = 'x^2' + vorz_v_innen(fkt_1_a_p,'x') + vorz_str(fkt_1_a_q)
        fkt_1_a_sqrt_disk = N(sqrt(fkt_1_a_p2 ** 2 - fkt_1_a_q), 3)
        fkt_1_a_lsg = solve(fkt_1_a, x)
        fkt_2_a = 6 * x_1 * x + 2 * x_2
        fkt_2_a_xo = N(fkt_2_a.subs(x,re(fkt_1_a_lsg[1])),3)
        fkt_2_a_str = vorz_v_aussen(6 * x_1, 'x') + vorz_str(2*x_2)
        flaeche = N(fkt_a.subs(x,re(fkt_1_a_lsg[1])),3)

        # Aufgaben und Lösungen
        if ('a' not in teilaufg) or (gleichung == True):
            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie den x-Wert von Punkt P für den maximalen '
                           + r'Flächeninhalt, wenn')
            aufgabe.append(r' \mathrm{f(x)~=~' + fkt_str + r' \quad ist.} ')
        else:
            aufgabe.append(NoEscape(beschriftung(teilaufg,i) + 'Berechnen Sie den x-Wert von Punkt P, für den '
                                    + 'maximalen Flächeninhalt. \n\n'))
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{geg: \quad f(x)=~' + fkt_str
                       + r' \quad ges: x~für~A_{max} \quad (1BE) } \\'
                       + r' \mathrm{es~gilt: \quad HB.: \quad A~=~x \cdot y \quad und \quad NB.: \quad f(x)~=~'
                       + fkt_str + r' \quad (2BE)}  \\'
                       + r' \to \quad \mathrm{HB.: \quad A(x)~=~x \cdot (' + fkt_str + r')~=~ ' + fkt_a_str
                       + r' \quad (1BE) } \\ \mathrm{A^{ \prime }(x)~=~' + fkt_1_a_str
                       + r' \quad und \quad A^{ \prime \prime } (x) ~=~' + fkt_2_a_str + r' \quad (2BE) } \\'
                       + r' \mathrm{A^{ \prime }(x) ~=~0 \quad \to \quad 0~=~' + fkt_1_a_str + r' \quad \vert \div '
                       + gzahl_klammer(3*x_1) + r' \quad \to \quad 0~=~' + fkt_1_a_pq + r' \quad (2BE) }\\'
                       + r' \mathrm{ x_{1/2} ~=~ - \frac{' + gzahl(fkt_1_a_p) + r'}{2} \pm \sqrt{ \left( \frac{'
                       + gzahl(fkt_1_a_p) + r'}{2} \right) ^2 -' + gzahl_klammer(fkt_1_a_q) + '} ~=~'
                       + gzahl(-1*fkt_1_a_p2) + r' \pm ' + gzahl(fkt_1_a_sqrt_disk) + r' \quad (2BE) } \\'
                       + r' \mathrm{x_1 ~=~' + gzahl(N(re(fkt_1_a_lsg[0]),3)) + r' \quad und \quad x_2 ~=~'
                       + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r' \quad (2BE) } \\ \mathrm{A^{ \prime \prime }('
                       + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~' + gzahl(6*x_1) + r' \cdot '
                       + gzahl_klammer(N(re(fkt_1_a_lsg[1]),3)) + vorz_str(2*x_2) + r'~=~'
                       + gzahl(fkt_2_a_xo) + r'~<0 \quad \to HP \quad (3BE) } \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if 'c' in teilaufg:
        # Die SuS sollen mithilfe der Ergebnisse der vorherigen Teilaufgabe den maximalen Flächeninhalt berechnen. Wird diese Teilaufgabe ausgewählt, ist automatisch auch die vorherige Teilaufgabe in 'teilaufg' enthalten.
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # Aufgaben und Lösungen
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den maximalen Flächeninhalt des Rechteckes. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' A(' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + r')~=~'
                       + gzahl(x_1) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^3'
                       + vorz_str(x_2) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3)) + ')^2'
                       + vorz_str(x_3) + r' \cdot (' + gzahl(N(re(fkt_1_a_lsg[1]),3))
                       + ') ~=~' + gzahl(flaeche) + r' \quad (2BE)')
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def extremalproblem_einfach(nr, i=0, BE=[]):
    # Den SuS ist eine lineare Funktion gegeben, um damit ein Extremalproblem zu lösen.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{str(nr)}']

    # hier wird die Funktion erstellt.
    m = nzahl(-5,-1)/2
    xmax = nzahl(6,10)
    n = -1*xmax*m
    fkt = m * x + n
    fkt_str = vorz_v_aussen(m,'x') + vorz_str(n)
    fkt_a = fkt*x
    fkt_a_str = vorz_v_aussen(m,'x^2') + vorz_v_innen(n,'x')
    fkt_a_str_1 = gzahl(m) + r' \cdot ' + binom_klammer(1,Rational(n,m), 'x^2', 'x')
    fkt_a_str_2 = (gzahl(m) + r' \cdot \left( x^2 '+ vorz(Rational(n,m)) + r' 2 \cdot ' + gzahl(abs(Rational(n,2*m)))
                   + r' \cdot x + \left( ' + gzahl(abs(Rational(n,2*m))) + r' \right) ^2 - \left( '
                   + gzahl(abs(Rational(n,2*m))) + r' \right) ^2 \right) ')
    fkt_a_str_3 = (gzahl(m) + r' \cdot \left( \left( x ' + vorz_str(Rational(n,2*m)) + r' \right) ^2 - '
                   + gzahl(Rational(n**2, 4*m**2)) + r' \right) ')
    fkt_a_str_4 = (gzahl(m) + r' \left( x ' + vorz_str(Rational(n,2*m)) + r' \right) ^2 '
                   + vorz_str(Rational(n**2, 4*m)))
    xwert = -1 * Rational(n, 2*m)
    ywert = Rational(n,2)
    wert_A = Rational(n**2, -4*m)

    xwert_2 = int(xmax/2) + zzahl(1,2)
    ywert_2 = fkt.subs(x, xwert_2)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),NoEscape(
               f'Wie in der Abbildung zu sehen, liegt der Eckpunkt P des abgebildeten achsenparallelen '
               'Rechtecks auf dem Graphen von $ f(x) = ' + vorz_v_aussen(m,'x') + vorz_str(n) +  '$.'), 'Grafik',
               NoEscape(r' \noindent Berechnen Sie die Koordinaten von P, sodass die Rechtecksfläche maximal wird.'),
               ' \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
               r' \mathrm{es~gilt: \quad HB.: \quad A ~=~ x \cdot y \quad und \quad NB.: \quad f(x) ~=~ '
               + fkt_str + r'} \quad (2BE) \\ A(x)~=~x \cdot (' + fkt_str
               + r')~=~ ' + fkt_a_str + r' \quad (1BE) \\  A(x) ~=~ ' + fkt_a_str_1 + '~=~' + fkt_a_str_2 + '~=~'
               + r' \quad (2BE) \\ A(x) ~=~ ' + fkt_a_str_3 + '~=~' + fkt_a_str_4 + r' \quad (2BE) \\ S('
               + gzahl(xwert) + r' \vert ' + gzahl(wert_A) +') ' + r' \quad \to \quad f(' + gzahl(xwert) + ') ~=~ '
               + gzahl(m) + r' \cdot ' + gzahl_klammer(xwert) + vorz_str(n) + '~=~' + gzahl(ywert)
               + r' \quad (2BE) \\ \mathrm{Für~x~=~ ' + gzahl(xwert) + '~und~y~=~' + gzahl(ywert)
               + r'~besitzt~das~Rechteck~die~maximale~Fläche.}']
    grafiken_aufgaben = [f'Aufgabe_{nr}']
    grafiken_loesung = []
    def Darstellung(fkt, xmax, xwert_p, ywert_p, name):
        fig, ax = plt.subplots()
        fig.canvas.draw()
        fig.tight_layout()
        ax.set_aspect(-1/(2*m), adjustable='box')
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_xlabel('x', size=10, labelpad=-30, x=0.97)
        ax.set_ylabel('y', size=10, labelpad=-30, y=0.97, rotation=0)
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        plt.annotate(r'$ P( x \vert y ) $', xy=(xwert_p, ywert_p),
                     xycoords='data', xytext=(+10, +10), textcoords='offset points', fontsize=16)
        xwerte = np.arange(0, xmax, 0.01)
        ywerte = [fkt.subs(x, elements) for elements in xwerte]
        plt.plot(xwerte, ywerte)
        plt.plot([0, xwert_p], [ywert_p, ywert_p])
        plt.plot([xwert_p, xwert_p], [ywert_p, 0])
        plt.scatter([xwert_p, ], [ywert_p, ], 50, color='blue')
        return plt.savefig('img/temp/' + name, dpi=200, bbox_inches="tight", pad_inches=0)
    Darstellung(fkt, xmax, xwert_2, ywert_2, f'Aufgabe_{nr}')
    liste_punkte = [9] if BE == [] else BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rekonstruktion(nr, xwerte=[], faktor=None, BE=[]):
    # In dieser Aufgabe sollen die SuS eine einfache quadratische Funktion rekonstruieren. Die Aufgaben besitzt keine Teilaufgaben.
    # Mit dem Parameter 'xwerte=' können die x-Werte von drei Punkten der Funktion in der Form [x1, x2, x3] vorgegeben werden. Standardmäßig ist die Liste leer und die x-Werte werden zufällig zwischen -3 und 3 gebildet.
    # Mit dem Parameter 'faktor=' kann der Streckungs- bzw. Stazchungsfaktor der Funktion festgelegt werden. Standardmäßig ist der Wert None und der Faktor wird zufällig zwischen 0,5 und 4 gebildet.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    punkte = 11
    liste_bez = [f'{str(nr)}']
    # hier wird die Funktion erstellt.
    faktor = zzahl(1, 8)/2 if faktor == None or type(faktor) != int else faktor
    if len(xwerte) != 3 or not all(type(n) == int for n in xwerte):
        xwert_2 = zzahl(1, 2)
        xwert_3 = xwert_2 + 1
        xwert_1 = xwert_2 - 1

    while (-1*(xwert_1**2 - xwert_2**2)*(xwert_1**2*xwert_3 - xwert_1*xwert_3**2)
           + (xwert_1**2 - xwert_3**2)*(xwert_1**2*xwert_2 - xwert_1*xwert_2**2) == 0):
        if len(xwerte) != 3 or not all(type(n) == int for n in xwerte):
            xwert_2 = zzahl(1, 2)
            xwert_3 = xwert_2 + 1
            xwert_1 = xwert_2 - 1

    ywert_2 = zzahl(1, 3)
    ywert_3 = faktor * (xwert_3 - xwert_2) ** 2 + ywert_2
    ywert_1 = faktor * (xwert_1 - xwert_2) ** 2 + ywert_2
    fkt_str = (vorz_v_aussen(faktor, 'x^2') + vorz_v_innen(-2 * faktor * xwert_2, 'x')
               + vorz_str((faktor * (xwert_2 ** 2)) + ywert_2))
    fkt = faktor * (x - xwert_2) ** 2 + ywert_2

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Von einer Funktion 2. Grades sind die folgenden Punkte gegeben:  S(' + gzahl(xwert_1) + '|'
               + gzahl(ywert_1) + '), P(' + gzahl(xwert_2) + r'|' + gzahl(ywert_2) + ') und Q('
               + gzahl(xwert_3) + '|' + gzahl(ywert_3) + '). \n Berechnen Sie die Funktionsgleichung von f. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    # Rekonstruktion der Funktion
    # Zeilen 1 bis 3 vom LGS:

    a1 = xwert_1 ** 2
    b1 = xwert_1
    c1 = 1
    d1 = ywert_1


    a2 = xwert_2 ** 2
    b2 = xwert_2
    c2 = 1
    d2 = ywert_2

    a3 = xwert_3 ** 2
    b3 = xwert_3
    c3 = 1
    d3 = ywert_3

    # Zeile 4 und 5 vom LGS:

    z4 = NoEscape(gzahl(a1) + r'$ \cdot II' + vorz_str(-1 * a2) + r' \cdot I $')
    a4 = 0
    b4 = a1 * b2 - a2 * b1
    c4 = a1 - a2
    d4 = a1 * d2 - a2 * d1

    z5 = NoEscape(gzahl(a1) + r'$ \cdot III' + vorz_str(-1 * a3) + r' \cdot I $')
    a5 = 0
    b5 = a1 * b3 - a3 * b1
    c5 = a1 - a3
    d5 = a1 * d3 - a3 * d1

    # Zeile 6 vom LGS:

    z6 = NoEscape(gzahl(b4) + r'$ \cdot III' + vorz_str(-1 * b5) + r' \cdot II $')
    b6 = 0
    c6 = b4 * c5 - b5 * c4
    d6 = b4 * d5 - b5 * d4

    # Lösungen des LGS:

    lsg_c = d6 / c6
    lsg_b = (d4 - (c4 * lsg_c)) / b4
    lsg_a = (d1 - (c1 * lsg_c) - (b1 * lsg_b)) / a1


    table2 = Tabular('c|c|c|c|c|c|c|c', row_height=1.2)
    table2.add_hline(2, 7)
    table2.add_row('Berechnung mit Gauß-Algorithmus','Nr.', 'Berechnung', 'a', 'b', 'c', 'lsg', '')
    table2.add_hline(2, 7)
    table2.add_row('','I', ' ', gzahl(a1), gzahl(b1), gzahl(c1), gzahl(d1), '')
    table2.add_row('', 'II', ' ', gzahl(a2), gzahl(b2), gzahl(c2), gzahl(d2), '')
    table2.add_row('', 'III', ' ', gzahl(a3), gzahl(b3), gzahl(c3), gzahl(d3), '')
    table2.add_hline(2, 7)
    table2.add_row('', 'II', z4, gzahl(a4), gzahl(b4), gzahl(c4), gzahl(d4), '(1BE)')
    table2.add_row('', 'III', z5, gzahl(a5), gzahl(b5), gzahl(c5), gzahl(d5), '(1BE)')
    table2.add_hline(2, 7)
    table2.add_row('', 'III', z6, ' ', gzahl(b6), gzahl(c6), gzahl(d6), '(1BE)')
    table2.add_hline(2, 7)

    # Aufgaben und Lösungen
    loesung.append(r' \mathrm{Die~allgemeine~Funktionsgleichung~lautet \quad }'
                   + r' f(x)~= ~ a  x^2 ~ + ~ b x ~ + ~ c \quad (1BE) \\'
                   + r' \mathrm{aus~den~gegebenen~Punkten~folgt:} \quad '
                   + r' \mathrm{I:~f(' + gzahl(xwert_1) + ')~=~' + gzahl(ywert_1) + r' \quad \to \quad '
                   + vorz_v_aussen(xwert_1**2,'a') + vorz_v_innen(xwert_1, 'b') + ' + c ~=~' + gzahl(ywert_1)
                   + r' \quad (1BE)} \\ \mathrm{II:~f(' + gzahl(xwert_2) + ')~=~' + gzahl(ywert_2)
                   + r' \quad \to \quad ' + vorz_v_aussen(xwert_2**2, 'a') + vorz_v_innen(xwert_2, 'b')
                   + ' + c ~=~' + gzahl(ywert_2) + r' \quad (1BE)} \\ \mathrm{III:~f(' + gzahl(xwert_3) + ' ) ~=~ } '
                   + gzahl(ywert_3) + r' \quad \to \quad ' + vorz_v_aussen(xwert_3**2, 'a')
                   + vorz_v_innen(xwert_3,'b + c ~=~' + gzahl(ywert_3) + r' \quad (1BE)'))
    loesung.append(table2)
    loesung.append(r' \mathrm{aus~III~folgt:~' + vorz_v_aussen(c6,'c~=~') + vorz_str(d6) + r' \quad \vert \div '
                   + gzahl_klammer(c6) + r' \quad \to \quad c~=~' + latex(lsg_c) + r' \quad (1BE) } \\'
                   + r' \mathrm{aus~II~folgt:~' + vorz_v_aussen(b4,'b~') + vorz_str(c4)
                   + r' \cdot ~' + gzahl_klammer(lsg_c) + '~=~' + gzahl(d4) + r' \quad \vert ~-~'
                   + gzahl_klammer(c4 * lsg_c) + r' \quad \vert \div ' + gzahl_klammer(b4)
                   + r' \quad \to \quad b~=~' + latex(lsg_b) + r' \quad (1BE) } \\'
                   + r' \mathrm{aus~I~folgt:~ ' + vorz_v_aussen(a1,'a') + vorz_str(b1) + r' \cdot '
                   + gzahl_klammer(lsg_b) + vorz_str(c1) + r' \cdot ' + gzahl_klammer(lsg_c) + '~=~'
                   + gzahl(d1) + r' \quad \vert ~-~' + gzahl_klammer(b1 * lsg_b + c1 * lsg_c)
                   + r' \quad \vert \div ' + gzahl_klammer(a1) + r' \quad \to \quad a~=~' + latex(lsg_a)
                   + r' \quad (1BE) }  \\' + r' \bm{f(x)~=~' + vorz_v_aussen(lsg_a,'x^2')
                   + vorz_v_innen(lsg_b,'x') + vorz_str(lsg_c) + r'} \quad (1BE) \\'
                   + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

    if BE != []:
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def exponentialgleichungen(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], anzahl=False, wdh=False, i=0, BE=[]):
    # Die SuS sollen verschiedene Exponentialgleichungen lösen.
    # Mithilfe von "teilaufg=[]" können folgenden Gleichungstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) einfache Exponentfkt
    # b) Exponentfkt mit einem Faktor
    # c) Exponentfkt mit einem Faktor und einem Summanden
    # d) Exponentialfkt mit einf. lin. Fkt als Exponenten
    # e) Exponentialfkt mit lin. Fkt als Exponenten
    # f) Summe von Exponentialfkt
    # g) Logarithmusfkt
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{str(nr)}']

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Lösen Sie die Exponentialgleichungen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def exp_einfach():
        basis_1 = nzahl(2,8)
        exponent_1 = nzahl(3,5)
        ergebnis_1 = basis_1 ** exponent_1
        aufg = gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1)
        lsg = (gzahl(basis_1) + '^x ~=~ ' + gzahl(ergebnis_1) + r' \quad \vert \log_{'
               + gzahl(basis_1) + r'} \quad \to \quad x ~=~ ' + gzahl(exponent_1) + r' \quad (1BE)')
        pkt = 1
        return aufg, lsg, pkt

    def exp_faktor():
        pkt = 3
        basis_2 = nzahl(2,8)
        exponent_2 = nzahl(2,5)
        exponent_2_summe = zzahl(1,exponent_2)
        vorz_exp = -1 if exponent_2_summe < 0 else 1
        faktor = zzahl(2,30)*20
        ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_summe)
        while abs(ergebnis_2 * faktor) > 10 ** 5:
            basis_2 = basis_2 - 1 if basis_2 > 2 else basis_2
            exponent_2_summe = vorz_exp * (abs(exponent_2_summe) - 1) if exponent_2_summe > 1 else exponent_2_summe
            faktor = faktor / 10
            ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_summe)
        erg_2 = faktor*ergebnis_2
        erg_3 = ergebnis_2
        aufg = (gzahl(faktor) + r' \cdot ' + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe)
                + r'} ~=~ ' + gzahl(erg_2))
        lsg = (gzahl(faktor) + r' \cdot ' + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ '
               + gzahl(erg_2) + r' \quad \vert \div ' + gzahl_klammer(faktor) + r' \quad \to \quad '
               + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_summe) + r'} ~=~ ' + gzahl(erg_3)
               + r' \quad \vert \log_{' + gzahl(basis_2) + r'} \quad (1BE) \\ x' + vorz_str(exponent_2_summe) + r' ~=~ '
               + gzahl(exponent_2 + exponent_2_summe) + r' \quad \vert ' + vorz_str(-1 * exponent_2_summe)
               + r' \quad \to \quad x ~=~ ' + gzahl(exponent_2)) + r' \quad (2BE)'
        return aufg, lsg, pkt

    def exp_faktor_summe():
        pkt = 3
        basis_2 = nzahl(2,8)
        exponent_2 = nzahl(2,5)
        exponent_2_sum = zzahl(1,exponent_2)
        vorz_exp = -1 if exponent_2_sum < 0 else 1
        faktor = zzahl(2,30)*20
        ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_sum)
        while abs(ergebnis_2 * faktor) > 10 ** 5:
            basis_2 = basis_2 - 1 if basis_2 > 2 else basis_2
            exponent_2_sum = vorz_exp * (abs(exponent_2_sum) - 1) if exponent_2_sum > 1 else exponent_2_sum
            faktor = faktor / 10
            ergebnis_2 = basis_2 ** (exponent_2 + exponent_2_sum)
        summand = zzahl(1,100)*faktor
        umf_sum = '+' if summand < 0 else '-'
        erg_1 = faktor*ergebnis_2+summand
        erg_2 = faktor*ergebnis_2
        erg_3 = ergebnis_2
        aufg = (gzahl(faktor) + r' \cdot ' + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_sum)
                + r'} ' + vorz_str(summand) + ' ~=~ ' + gzahl(erg_1))
        lsg = (gzahl(faktor) + r' \cdot ' + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_sum)
               + r'} ' + vorz_str(summand) + '~=~ ' + gzahl(erg_1) + umformung(summand, umf_sum)
               + r' \quad \to \quad ' + gzahl(faktor) + r' \cdot ' + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_sum)
               + r'} ~=~ ' + gzahl(erg_2) + umformung(faktor, ':') + r' \quad (2BE) \\'
               + gzahl(basis_2) + '^{x' + vorz_str(exponent_2_sum) + r'} ~=~ ' + gzahl(erg_3)
               + r' \quad \vert \log_{' + gzahl(basis_2) + r'} \quad \to \quad x' + vorz_str(exponent_2_sum)
               + r' ~=~ ' + gzahl(exponent_2 + exponent_2_sum) + r' \quad \vert ' + vorz_str(-1 * exponent_2_sum)
               + r' \quad \to \quad x ~=~ ' + gzahl(exponent_2)) + r' \quad (3BE)'
        return aufg, lsg, pkt

    def exp_linear_einfach():
        pkt = 2
        faktor_exp = zzahl(1, 8) / 2
        erg_gl = nzahl(2, 40) / 10
        aufg = 'e^{' + vorz_v_aussen(faktor_exp, 'x') + '} ~=~ ' + gzahl(erg_gl)
        lsg = ('e^{' + vorz_v_aussen(faktor_exp,'x') + '} ~=~ ' + gzahl(erg_gl)
               + r' \quad \vert \ln() \quad \to \quad ' + vorz_str(faktor_exp) + r'x ~=~ \ln('
               + gzahl(erg_gl) + r') \quad \vert \div ' + gzahl_klammer(faktor_exp)
               + r' \quad \to \quad x~=~' + vorz_str(N(log(erg_gl) / faktor_exp, 3))
               + r' \quad (2BE)')
        return aufg, lsg, pkt

    def exp_linear_schwer():
        pkt = 3
        faktor_exp = zzahl(1, 8) / 2
        summand = zzahl(1,8)
        erg_gl = nzahl(2, 40) / 10
        aufg = 'e^{' + vorz_v_aussen(faktor_exp, 'x') + vorz_str(summand) + r'} ~=~ ' + gzahl(erg_gl)
        lsg = ('e^{' + vorz_v_aussen(faktor_exp, 'x') + vorz_str(summand) + '} ~=~ ' + gzahl(erg_gl)
               + r' \quad \vert \ln() \quad \to \quad ' + vorz_v_aussen(faktor_exp, 'x')
               + vorz_str(summand) + r' ~=~ \ln( ' + gzahl(erg_gl) + r') \quad \vert '
               + vorz_str(-1*summand) + r' \quad (1BE) \\' + vorz_v_aussen(faktor_exp,'x')
               + r' ~=~ \ln(' + gzahl(erg_gl) + r')' + vorz_str(-1*summand) + r' \quad \vert \div '
               + gzahl_klammer(faktor_exp) + r' \quad \to \quad x~=~'
               + vorz_str(N((log(erg_gl) - summand)/ faktor_exp, 3))
               + r' \quad (2BE)')
        return aufg, lsg, pkt

    def exp_summe():
        pkt = 4
        faktor_exp_1 = zzahl(1,5)
        faktor_exp_2 = zzahl(1,5)
        while faktor_exp_1 == faktor_exp_2:
            faktor_exp_2 = zzahl(1, 5)
        vorzeichen = random.choice([-1, 1])
        faktor_1 = vorzeichen * nzahl(1,40)
        faktor_2 = vorzeichen * nzahl(1,40)
        aufg = (gzahl(faktor_1/10) + 'e^{' + vorz_v_aussen(faktor_exp_1, 'x') + r'} ~=~'
                + gzahl(faktor_2/10) + 'e^{' + vorz_v_aussen(faktor_exp_2, 'x') + r'}')
        lsg = (gzahl(faktor_1/10) + 'e^{' + vorz_v_aussen(faktor_exp_1, 'x') + '} ~=~'
               + gzahl(faktor_2/10) + 'e^{' + vorz_v_aussen(faktor_exp_2, 'x') + '}'
               + r' \quad \vert \div ' + gzahl_klammer(faktor_1/10) + r' \quad \to \quad '
               + 'e^{' + vorz_v_aussen(faktor_exp_1,'x') + r'} ~=~' + gzahl(Rational(faktor_2,faktor_1))
               + r' \cdot e^{' + vorz_v_aussen(faktor_exp_2,'x') + r'} \quad \vert \div e^{'
               + gzahl(faktor_exp_2) + r'x} \quad (1BE) \\'
               + 'e^{' + gzahl(faktor_exp_1 - faktor_exp_2) + 'x} ~=~ '
               + gzahl(Rational(faktor_2,faktor_1)) + r' \quad \vert \ln () \quad \to \quad '
               + vorz_v_aussen(faktor_exp_1 - faktor_exp_2,'x') + r' ~=~ \ln \left('
               + gzahl(Rational(faktor_2,faktor_1)) + r' \right) \quad \vert \div '
               + gzahl_klammer(faktor_exp_1 - faktor_exp_2) + r' \quad \to \quad x ~=~'
               + gzahl(N(log(faktor_2/faktor_1)/(faktor_exp_1 - faktor_exp_2),3))
               + r' \quad (3BE)')
        return aufg, lsg, pkt

    def logarithmus():
        pkt = 3
        faktor_exp_1 = zzahl(2, 8)
        faktor_exp_2 = zzahl(2, 8)
        summand = zzahl(1,7)
        while faktor_exp_1 == faktor_exp_2:
            faktor_exp_2 = zzahl(1, 5)
        aufg = (r' \ln(x^{' + gzahl(faktor_exp_1) + r'}) ~=~ \ln(x^{' + gzahl(faktor_exp_2) + '})'
                   + vorz_str(summand))
        lsg = (r' \ln(x^{' + gzahl(faktor_exp_1) + r'}) ~=~ \ln (x^{' + gzahl(faktor_exp_2) + '})'
               + vorz_str(summand) + r' \quad \vert ~-~ \ln (x^{' + gzahl(faktor_exp_2) + '})'
               + r' \quad \to \quad \ln (x^{' + gzahl(faktor_exp_1-faktor_exp_2) + '}) ~=~'
               + gzahl(summand) + r' \quad \vert e^{ \Box } \quad (1BE) \\ x^{'
               + gzahl(faktor_exp_1-faktor_exp_2) + '} ~=~ e^{' + gzahl(summand)
               + r'} \quad \vert \sqrt[' + gzahl(faktor_exp_1-faktor_exp_2)
               + r'] \quad \to \quad x ~=~'
               + gzahl(N(exp(summand)**(1/(faktor_exp_1-faktor_exp_2)),3)) + r' \quad (2BE)')
        return aufg, lsg, pkt

    auswahl = {'a': exp_einfach, 'b': exp_faktor, 'c': exp_faktor_summe, 'd': exp_linear_einfach,
               'e': exp_linear_schwer, 'f': exp_summe,'g': logarithmus}

    if anzahl != False:
        if type(anzahl) != int:
            exit("Fehler in exponentialgleichungen(nr, ...): Der Parameter 'anzahl=' muss eine natürliche Zahl "
                 "kleiner 27 sein.")
        else:
            anzahl = 26 if anzahl > 26 else anzahl
            teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        if type(wdh) != int:
            exit("Fehler in exponentialgleichungen(nr, ...): Der Parameter 'wdh=' muss eine natürliche Zahl "
                 "kleiner 14 sein.")
        else:
            anzahl = 26 if anzahl > 26 or anzahl == False or len(teilaufg)*wdh > 26 else len(teilaufg)*wdh
            teilaufg = repeat(teilaufg, wdh, laenge=anzahl)

    aufg_text = ''
    lsg_aufg = (r' \mathrm{Lösen~Sie~die~Exponentialgleichungen.} \\')
    punkte = 0
    i = 0
    for element in teilaufg:
        aufg, lsg, pkt = auswahl[element]()
        if (i + 1) % 2 != 0:
            aufg_text = aufg_text + beschriftung(teilaufg,i) + r' \quad ' +  aufg
            if i + 1 < len(teilaufg):
                aufg_text = aufg_text + r' \hspace{10em} '
        elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
            aufg_text = aufg_text + beschriftung(teilaufg,i) + r' \quad ' + aufg + r' \\\\'
        else:
            aufg_text = aufg_text + beschriftung(teilaufg,i) + r' \quad ' + aufg
        lsg_aufg = (lsg_aufg + beschriftung(teilaufg,i, True) + r' \quad ' + lsg + r' \\')
        punkte += pkt
        i += 1

    lsg_aufg = lsg_aufg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}'
    if BE != []:
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg_text)
    loesung.append(lsg_aufg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def wachstumsfunktion(nr, teilaufg=['a', 'b', 'c', 'd'], i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS in einer Sachaufgaben zum Wachstum ihre Kenntnisse der Logarithmusgesetze nutzen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    # hier wird die Funktion erstellt.
    def Aufgabe_Variante_1():

        text = ('Ein Patient nimmt ein Medikament ein. Anschließend wird die Konzentration des Medikaments im Blut'
                ' jede Stunde in mg/l gemessen. ')
        text2 = 'Die Messwerte ergeben folgende Tabelle: '
        Grundwert = nzahl(10, 20) * 10
        Prozentwert = nzahl(5, 15)
        Wachstumsfaktor = 1 - Prozentwert/100
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
        text3 = (f'Dabei wurde festgestellt, dass diese am Anfang {gzahl(Grundwert)} mg/l betrug und '
                 f'{gzahl(Prozentwert)}% pro Stunde abnimmt')
        return text, text2, text3, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x, Tabelle_beschriftung

    def Aufgabe_Variante_2():

        text = 'Die Einwohnerzahl eines Landes wurde jedes Jahr gezählt (Angaben in Millionen). '
        text2 = 'Die Ergebnisse wurden in der folgenden Tabelle festgehalten:'
        Grundwert = nzahl(80, 200)
        Prozentwert = zzahl(10,50)/10
        Wachstumsfaktor = 1 + Prozentwert/100
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
        richtung = 'zu' if Prozentwert > 0 else 'ab'
        text3 = (f'Dabei wurde festgestellt, das die Einwohnerzahl jedes Jahr von ursprünglich {gzahl(Grundwert)} '
                 f'Millionen Menschen um {gzahl(abs(Prozentwert))}% {richtung}nimmt.')
        return text, text2, text3, Liste, Wachstumsfaktor, Grundwert, Einheit_y, Einheit_x, Tabelle_beschriftung

    if random.random() < 0.5:
        text, text2, text3, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x, Tab_beschr = Aufgabe_Variante_1()
    else:
        text, text2, text3, Aufg_Liste, Aufg_a, Aufg_c0, Aufg_Einheit_y, Aufg_Einheit_x, Tab_beschr = Aufgabe_Variante_2()

    Aufg_t = nzahl(7, 10)
    Aufg_wert_y = int(N(Aufg_Liste[Aufg_t], 2))
    Aufg_wert_t = nzahl(10, 17)
    # Aufg_Liste_str = [str(x).replace('.',',') for x in Aufg_Liste]
    # print(Aufg_Liste_str)
    table2 = Tabular('c|c|c|c|c|c|c|', row_height=1.2)
    table2.add_hline(2, 7)
    table2.add_row(Tab_beschr, f'Zeit in {Aufg_Einheit_x}', ' 0', '1', '2', '3', '4')
    table2.add_hline(2, 7)
    table2.add_row('', f'Wert in {Aufg_Einheit_y}', Aufg_Liste[0], Aufg_Liste[1], Aufg_Liste[2],
                   Aufg_Liste[3], Aufg_Liste[4])
    table2.add_hline(2, 7)

    table3 = Tabular('c|c|c|c|c|c|', row_height=1.5)
    table3.add_hline(2, 6)
    table3.add_row('Übersichtstabelle der Quotienten (2BE): ', 'Quotient der Werte', NoEscape(r'$ \frac{a1}{a0} $'),
                   NoEscape(r'$ \frac{a2}{a1} $'), NoEscape(r'$ \frac{a3}{a2} $'), NoEscape(r'$\frac{a4}{a3}$'))
    table3.add_hline(2, 6)
    table3.add_row('', 'Quotienten', str(N(Aufg_Liste[1] / Aufg_Liste[0], 4)).rstrip(' 0'),
                   str(N(Aufg_Liste[2] / Aufg_Liste[1], 4)).rstrip(' 0'),
                   str(N(Aufg_Liste[3] / Aufg_Liste[2], 4)).rstrip(' 0'),
                   str(N(Aufg_Liste[4] / Aufg_Liste[3], 4)).rstrip(' 0'))
    table3.add_hline(2, 6)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), text]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen mithilfe des Quotienten aufeinanderfolgender Werte das exponentielle Wachstum nachweisen,
        liste_punkte.append(3)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # grafische Darstellung des Sachverhaltes

        # Aufgaben und Lösungen
        aufgabe.extend((text2 + ' \n\n', table2, ' \n\n\n',
                        beschriftung(teilaufg,i)
                        + 'Weisen Sie nach, dass es sich um exponentielles Wachstum handelt.\n\n'))
        loesung.extend((beschriftung(teilaufg,i, True)
                        + r' \mathrm{Alle~Quotienten~sind~gleich~gross.~Damit~handelt~es~sich~'
                        + r'um~exponentielles~Wachstum. \quad (1BE)}', table3))
        i += 1
    else:
        aufgabe.append(text3 + '\n\n')

    if len([element for element in ['b', 'c', 'd'] if element in teilaufg]) > 0:
        # Die SuS sollen mithilfe der Werte und dem Quotienten aus der vorherigen Teilaufgabe, die Gleichung dieser Wachstumsfunktion aufstellen.
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # Aufgaben und Lösungen
        aufgabe.append(beschriftung(teilaufg,i) + 'Stellen Sie die Wachstumsfunktion f(x) auf. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f(x)~=~' + str(Aufg_c0) + r' \cdot '
                       + str(Aufg_a) + r'^x \quad (2BE) \\')
        i += 1
    if 'c' in teilaufg:
        # Mithilfe der Gleichung aus Teilaufgabe 'b' sollen die SuS einen x-Wert bei gegebenen y-Wert berechnen.

        punkte_aufg = 3
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # grafische Darstellung des Sachverhaltes

        # Aufgaben und Lösungen
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Zeit bis {Aufg_wert_y} {Aufg_Einheit_y}'
                       + ' erreicht werden. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + str(Aufg_wert_y) + r'~=~'+ str(Aufg_c0)
                       + r' \cdot '+ str(Aufg_a) + r'^x \quad \vert \div ' + str(Aufg_c0)
                       + r' \quad \to \quad ' + latex(Rational(Aufg_wert_y,Aufg_c0))
                       + r'~=~'+ str(Aufg_a) + r'^x \quad \vert \log_{' + str(Aufg_a)
                       + r'} \quad \to \quad x~=~' + str(N(log(Rational(Aufg_wert_y,Aufg_c0),Aufg_a),5))
                       + r' \quad (3BE) \\')
        i += 1

    if 'd' in teilaufg:
        # Mithilfe der Gleichung aus Teilaufgabe 'b' sollen die SuS einen y-Wert bei gegebenen x-Wert berechnen.

        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        # grafische Darstellung des Sachverhaltes

        # Aufgaben und Lösungen
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie den Wert der nach {Aufg_wert_t} {Aufg_Einheit_x}'
                       + f' erreicht wird. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + f' f(' + str(Aufg_wert_t) + r')~=~' + str(Aufg_c0)
                       + r' \cdot '+ str(Aufg_a) + r'^{'+ str(Aufg_wert_t)+ r'} ~=~ '
                       + latex(N(Aufg_c0*Aufg_a**Aufg_wert_t,4)) + r' \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Aufgaben zur Integralrechnung
def unbestimmtes_integral(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], anzahl=False, wdh=False, i=0, BE=[]):
    # Die SuS sollen verschiedene Funktionen ableiten.
    # Mithilfe von "teilaufg=[]" können folgenden Gleichungstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) einfaches Polynom
    # b) Polynom
    # c) Exponentialfkt
    # d) Trigonometrische Fkt
    # e) Logarithmusfkt
    # f) verschiedene verkettete Fkt
    # g) Wurzelfunktion
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [nr]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Bestimme die Stammfunktionen der folgenden Funktionen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []


    def polynom_01():
        konst_i = zzahl(2,20)
        e1_i = nzahl(2,5)
        e2_i = e1_i + nzahl(1,3)
        fkt = 'x^{' + gzahl(e2_i) + '} + x^{' + gzahl(e1_i) + '}' + vorz_str(konst_i)
        fkt_uf = ''
        Fkt = (r' \frac{1}{' + gzahl(e2_i+1) + r'} \cdot x^{' + gzahl(e2_i + 1) + r'} + \frac{1}{' + gzahl(e1_i+1)
               + r'} \cdot x^{' + gzahl(e1_i + 1) + '}' + vorz_str(konst_i) + 'x + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def polynom_02():
        konst_ii = zzahl(2, 20)
        e1_ii = nzahl(2, 5)
        e2_ii = e1_ii + nzahl(2, 4)
        a1 = (e1_ii + 1) * zzahl(1, 10) / 2
        a2 = (e2_ii + 1) * zzahl(1, 10) / 2
        fkt = (vorz_v_aussen(a2, 'x^{' + gzahl(e2_ii) + '}') + vorz_v_innen(a1, 'x^{' + gzahl(e1_ii) + '}')
                      + vorz_str(konst_ii))
        fkt_uf = ''
        Fkt = (vorz_v_aussen(Rational(a2, e2_ii + 1), 'x^{' + gzahl(e2_ii + 1) + '}')
                      + vorz_v_innen(Rational(a1, e1_ii + 1), 'x^{' + gzahl(e1_ii + 1) + '}')
                      + vorz_v_innen(konst_ii, 'x + C'))
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def e_funktion():
        a1 = zzahl(2, 9)
        k1 = zzahl(1, 19) / 2
        fkt = gzahl(a1) + r' \cdot e^x' + vorz_str(k1)
        fkt_uf = ''
        Fkt = gzahl(a1) + r' \cdot e^x' + vorz_v_innen(k1, 'x + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt

    def trig_funktion():
        a1 = zzahl(2, 9)
        auswahl = random.choice([[latex(a1) + r' \cdot \sin(x)', latex(-1 * a1) + r' \cdot \cos(x) + C'],
                                 [latex(a1) + r' \cdot \cos(x)', latex(a1) + r' \cdot \sin(x) + C']])
        fkt = auswahl[0]
        fkt_uf = ''
        Fkt = auswahl[1]
        pkt = 1
        return fkt, fkt_uf, Fkt, pkt

    def ln_funktion():
        a1 = zzahl(2, 9)
        e1 = nzahl(2, 9)
        a2 = zzahl(2, 9)
        fkt = (vorz_aussen(a1) + r' \frac{' + gzahl(abs(a1)) + '}{x^{' + gzahl(e1) + '}}'
               + vorz(a2) + r' \frac{' + str(abs(a2)) + '}{x}')
        fkt_uf = r'~=~ \int ' + gzahl(a1) + r' x^{' + gzahl(-1 * e1) + '}' + vorz_str(a2) + r'x^{-1} \,dx'
        Fkt = (gzahl(Rational(a1, -1 * e1 + 1)) + 'x^{' + gzahl(-1 * e1 + 1) + '}' + vorz_str(a2)
               + r' \cdot \ln (x) + C')
        pkt = 3
        return fkt, fkt_uf, Fkt, pkt

    def kettenregel():
        a1 = zzahl(3, 20) / 2
        i1 = zzahl(3, 20) / 2
        k1 = zzahl(2, 9)
        e1 = nzahl(2, 9)
        innere = vorz_v_aussen(i1, 'x') + vorz_str(k1)
        auswahl = random.choice([[gzahl(a1) + r' \cdot (' + innere + ')^{' + latex(e1) + '}',
                                  gzahl(Rational(a1, i1 * (e1 + 1))) + r' \cdot (' + innere + ')^{' + latex(e1 + 1)
                                  + '} + C'],
                                 [gzahl(a1) + r' \cdot e^{' + innere + '}',
                                  gzahl(Rational(a1, i1)) + r' \cdot e^{' + innere + '} + C'],
                                 [gzahl(a1) + r' \cdot \sin(' + innere + ')' + vorz_str(k1),
                                  gzahl(Rational(-1 * a1, i1)) + r' \cdot \cos(' + innere + ')'
                                  + vorz_v_innen(k1,'x + C')],
                                 [gzahl(a1) + r' \cdot \cos(' + innere + ')' + vorz_str(k1),
                                  gzahl(Rational(a1, i1)) + r' \cdot \sin(' + innere + ')'
                                  + vorz_v_innen(k1,'x + C')]])

        fkt, fkt_uf, Fkt, pkt = auswahl[0], '', auswahl[1], 2
        return fkt, fkt_uf, Fkt, pkt

    def wurzelfunktion():
        a1 = nzahl(2, 6)
        e1 = a1 + nzahl(2, 4)
        fkt = r' \sqrt[' + gzahl(a1) + ']{x^{' + gzahl(e1) + '}}'
        fkt_uf = r' ~=~ \int x^{' + gzahl(Rational(e1, a1)) + r'} \,dx '
        Fkt = (gzahl(Rational(a1, a1 + e1)) + 'x^{' + gzahl(Rational(a1 + e1, a1)) + '} + C')
        pkt = 2
        return fkt, fkt_uf, Fkt, pkt


    aufgaben = {'a': polynom_01, 'b': polynom_02, 'c': e_funktion, 'd': trig_funktion, 'e': ln_funktion,
                'f': kettenregel, 'g': wurzelfunktion}

    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
        teilaufg = random_selection(teilaufg, anzahl, True)

    aufg = ''
    lsg = (r' \mathrm{~Bestimme~die~Stammfunktionen~der~gegebenen~Funktionen.} \\')
    punkte = 0
    for element in teilaufg:
        fkt, fkt_uf, Fkt, pkt = aufgaben[element]()
        if (i + 1) % 3 != 0:
            aufg = aufg + beschriftung(teilaufg,i) + r' \int ~' + fkt + r'~ \,dx '
            if i + 1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        else:
            aufg = aufg + beschriftung(teilaufg,i) + r' \int ~' + fkt + r'~ \,dx \\\\'
        lsg = (lsg + beschriftung(teilaufg,i, True) + r' \int ~' + fkt + r'~ \,dx ' + fkt_uf
               + r' \quad \to \quad \bm{F(x)~=~' + Fkt + r'} \quad (' + str(pkt) + r'BE) \\')
        punkte += pkt
        i += 1

    lsg = lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}'
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)


    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def bestimmtes_integral(nr, teilaufg=['a', 'b'], grad=3, i=0, BE=[]):
    # Die SuS sollen die vom Graph einer Funktion (zweiten oder dritten Grades) mit der x-Achse eingeschlossene Fläche berechnen.
    # Mit dem Parameter 'grad=' kann der Grad der Funktion festgelegt werden. Es ist momentan nur die Wahl zwischen grad=2 oder grad=3 möglich. Werden andere Werte angegeben, wird der Grad der Funktion zufällig ausgewählt.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    # Hinweis: Die Funktion zweiten Grades ist für den hilfsmittelfreien Teil geeignet.
    liste_punkte = []
    liste_bez = []

    grad = random.choice([2, 3]) if grad not in (2, 3) else grad
    if grad == 3:
        nst_1 = zzahl(1, 2)
        nst_2 = nst_1 + nzahl(1, 2) + 0.5
        nst_3 = nst_1 - nzahl(1, 2) - 0.5
        faktor = zzahl(3,7)/2

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * (nst_1 + nst_2 + nst_3)
        fkt_a3 = faktor * ((nst_1 * nst_2) + (nst_1 * nst_3) + (nst_2 * nst_3))
        fkt_a4 = -1 * faktor * nst_1 * nst_2 * nst_3
        fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
                   + vorz_str(fkt_a4))
        fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
        fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
        fkt_partial_p = -1 * (nst_2 + nst_3)
        fkt_partial_q = (nst_2 * nst_3)

        Fkt = collect(integrate(fkt,x),x)
        Fkt_str = (vorz_v_aussen(Rational(fkt_a1,4), 'x^4') + vorz_v_innen(Rational(fkt_a2,3), 'x^3')
                   + vorz_v_innen(Rational(fkt_a3,2), 'x^2') + vorz_v_innen(fkt_a4,'x'))

        fkt_b2 = nst_1 * fkt_a1
        fkt_c2 = fkt_a2 + fkt_b2
        fkt_b3 = nst_1 * fkt_c2
        fkt_c3 = fkt_a3 + fkt_b3
        fkt_b4 = nst_1 * fkt_c3
        fkt_c4 = fkt_a4 + fkt_b4

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('', fkt_a1, fkt_a2, fkt_a3, fkt_a4)
        table2.add_hline(2, 5)
        table2.add_row('Berechnung der Partialfunktion  mit Hornerschema: ', '', fkt_b2, fkt_b3, fkt_b4)
        table2.add_hline(2, 5)
        table2.add_row('', fkt_a1, fkt_c2, fkt_c3, fkt_c4)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n', 'Gegeben ist die Funktion:',
                   'f(x)~=~' + fkt_str + r' \hspace{20em}']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = []
        grafiken_loesung = []

        if len([element for element in ['a', 'b'] if element in teilaufg]) > 0:
            # Die SuS sollen die Nullstellen der Funktion berechnen. Bei der Funktion dritten Grades mithilfe des Gaußalgorithmus und beim zweiten Grad reicht die p-q-Formel.

            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 12
            liste_punkte.append(punkte)

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechne die Nullstellen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + fkt_str
                           + r' \quad \mathrm{durch~probieren:~x_1~=~}' + gzahl(nst_1)
                           + r' \quad (2BE) \\' + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1) + ')~=~'
                           + latex(fkt_partial) + r' \quad (4P)')
            loesung.append(table2)
            loesung.append(latex(fkt_partial) + r'~=~0 \quad \vert ~ \div '
                           + gzahl_klammer(faktor) + r' \quad \to \quad 0~=~' + latex(fkt_partial_pq)
                           + r' \quad (2BE) \\' + r' x_{2/3}~=~ - \frac{' + gzahl_klammer(fkt_partial_p)
                           + r'}{2} \pm \sqrt{ \left(' + r' \frac{' + latex(fkt_partial_p) + r'}{2} \right)^2-'
                           + gzahl_klammer(fkt_partial_q) + r'} \quad (2BE) \\' + r' \mathrm{x_2~=~' + gzahl(round(nst_2, 3))
                           + r' \quad und \quad x_3~=~' + gzahl(round(nst_3, 3)) + r' \quad (2BE)} \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
            i += 1

        if 'b' in teilaufg:
            # Die SuS sollen mithilfe der vorher bestimmten Nullstellen die vom Graphen der Funktion und der x-Achse eingeschlossene Fläche berechnen.

            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 6
            liste_punkte.append(punkte)

            lsg_A1 = N(Fkt.subs(x, nst_1) - Fkt.subs(x, nst_3),3)
            lsg_A2 = N(Fkt.subs(x, nst_2) - Fkt.subs(x, nst_1),3)
            lsg_A = abs(lsg_A1) + abs(lsg_A2)

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechne die Fläche, '
                           + f'die der Graph mit der x-Achse einschließt. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' A~=~ \left| \int_{' + gzahl(N(nst_3,2)) + '}^{'
                           + gzahl(nst_1) + '}' + fkt_str + r' ~ \,dx \right| + \left| \int_{' + gzahl(nst_1) + '}^{'
                           + gzahl(nst_2) + '}' + fkt_str + r' ~ \,dx \right| \quad (2BE) \\ =~ \left| \left[ '
                           + Fkt_str + r' \right]_{' + gzahl(N(nst_3,2)) + '}^{' + gzahl(nst_1)
                           + r'} \right| + \left| \left[ ' + Fkt_str + r' \right]_{'
                           + gzahl(N(nst_1,2)) + '}^{' + gzahl(nst_2) + r'} \right| \quad (2BE) \\'
                           + r'=~ \left| ' + gzahl(lsg_A1) + r' \right| + \left| ' + gzahl(lsg_A2)
                           + r' \right| ~=~' + gzahl(lsg_A) + r' \quad (2BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + '~BE}')

            i += 1
    elif grad == 2:
        nst_1 = -1* nzahl(1,2)
        nst_2 = nst_1 + nzahl(3,4)
        while nst_1*nst_2 == 0 or abs(nst_1) == abs(nst_2):
            nst_1 = -1 * nzahl(1, 2)
            nst_2 = nst_1 + nzahl(3, 4)
        faktor = zzahl(1,5)/2

        fkt = collect(expand(faktor * (x - nst_1)*(x - nst_2)), x)
        fkt_str = (vorz_v_aussen(faktor,'x^2') + vorz_v_innen(-1*faktor*(nst_1+nst_2),'x')
                   + vorz_str(faktor*nst_1*nst_2))
        fkt_pq_str = ('x^2' + vorz_v_innen(-1*(nst_1+nst_2),'x') + vorz_str(nst_1*nst_2))
        fkt_p = -1*(nst_1+nst_2)
        fkt_q = nst_1*nst_2
        Fkt = integrate(fkt,x)
        Fkt_str = (vorz_v_aussen(Rational(faktor,3),'x^3')
                   + vorz_v_innen(Rational(-1*faktor*(nst_1+nst_2),2),'x^2')
                   + vorz_v_innen(faktor*nst_1*nst_2,'x'))
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n', 'Gegeben ist die Funktion:',
                   'f(x)~=~' + fkt_str + r' \hspace{20em}']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = []
        grafiken_loesung = []

        if len([element for element in ['a', 'b'] if element in teilaufg]) > 0:
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 6
            liste_punkte.append(punkte)

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechne die Nullstellen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + fkt_str
                           + r' \quad \vert \div ' + gzahl_klammer(faktor) + r' \quad \to \quad 0~=~' + fkt_pq_str
                           + r' \quad (2BE) \\ x_{1/2}~=~ - \frac{' + gzahl_klammer(fkt_p)
                           + r'}{2} \pm \sqrt{ \left(' + r' \frac{' + latex(fkt_p) + r'}{2} \right)^2-'
                           + gzahl_klammer(fkt_q) + r'} \quad (2BE) \\' + r' \bm{x_1~=~' + gzahl(nst_1)
                           + r'} \quad \mathrm{und} \quad \bm{x_2~=~' + gzahl(nst_2) + r'} \quad (2BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
            i += 1

        if 'b' in teilaufg:
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 3
            liste_punkte.append(punkte)

            lsg_A = N(Fkt.subs(x, nst_2) - Fkt.subs(x, nst_1), 3)

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechne die Fläche, '
                           + f'die der Graph mit der x-Achse einschließt. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' A~=~ \left| \int_{' + gzahl(nst_1) + '}^{'
                           + gzahl(nst_2) + '}' + fkt_str + r' ~ \,dx \right| =~ \left| \left[ '
                           + Fkt_str + r' \right]_{' + gzahl(nst_1) + '}^{' + gzahl(nst_2)
                           + r'} \right| ~=~ \left| ' + gzahl(lsg_A) + r' \right| ~=~ \bm{'
                           + gzahl(abs(lsg_A)) + r'} \quad (3BE) \\')

            i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def polynome_kennenlernen(nr, teilaufg=['a', 'b'], anz_terme=3, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS den Grad, die Koeffizienten und die Symmetrie von Polynomen untersuchen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'anz_terme=' wird die Anzahl der Summanden der Funktion festgelegt.
    # Mit dem Parameter 'wendenormale=' kann für Teilaufgabe h) festgelegt werden, ob die Wendenormale berechnet werden soll. Standardmäßig ist 'wendenormale=True' und die Wendenormale ist in Teilaufgabe h) enthalten.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []
    exp = random.choice([random_selection([2*k for k in range(5)], anzahl=anz_terme),
                         random_selection([k+1 for k in range(5)], anzahl=anz_terme),
                         random_selection([k for k in range(9)], anzahl=anz_terme)])
    exp.sort()
    exp.reverse()
    fakt = exponenten(anz_terme,1,12, ganzz=True)
    fkt = fakt[0]*x**exp[0]
    fkt_str = potenz(fakt[0], exp[0])
    koef = 'a_{' + gzahl(exp[0]) + '} ~=~ ' + gzahl(fakt[0]) + ', ~ '
    for k in range(anz_terme-1):
        fkt = fkt + fakt[k+1]*x**exp[k+1]
        fkt_str = fkt_str + potenz(fakt[k+1], exp[k+1], vrz=True)
        koef = koef + 'a_{' + gzahl(exp[k+1]) + '} ~=~ ' + gzahl(fakt[k+1]) + '~ ~'

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               NoEscape('Gegeben ist die Funktion f(x) = $' + fkt_str + '$'),' \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen den Grad und die Koeffizienten der Funktion nennen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(beschriftung(teilaufg,i) + f'Geben Sie den Grad und die Koeffizienten der Funktion f an. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Grad: ~ ' + gzahl(exp[0])
                       + r'} \quad \mathrm{und} \quad ' + koef + r' \quad (' + gzahl(1+anz_terme) + 'BE)')
        liste_punkte.append(anz_terme + 1)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Funktion auf Symmetrie untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        fkt_sym = fkt.subs(x, -x)
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3BE)')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3BE)')
        else:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad '
                                                          r' \mathrm{nicht~symmetrisch} \quad (3BE)')
        aufgabe.append(beschriftung(teilaufg,i) + f'Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + lsg)
        liste_punkte.append(3)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def polynome_untersuchen(nr, teilaufg=['a', 'b', 'c', 'd'], grad=2, neue_seite=None, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS den Graphen einer Funktion 2. oder 3. Grades untersuchen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'grad=' wird der Grad der Funktion festgelegt.
    # Mit dem Parameter 'wendenormale=' kann für Teilaufgabe h) festgelegt werden, ob die Wendenormale berechnet werden soll. Standardmäßig ist 'wendenormale=True' und die Wendenormale ist in Teilaufgabe h) enthalten.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    if grad == 2:
        xwert1 = -1 * nzahl(2, 5)
        abst = list(range(2, 6))
        abst.remove(abs(xwert1))
        wert_abst = random.choice(abst)
        xwert2 = xwert1 + wert_abst
        xwerts = 0.5 * (xwert2 + xwert1)
        a_max = int(abs(20 / wert_abst ** 2))
        while a_max <= 1:
            xwert1 = -1 * nzahl(2, 5)
            abst = list(range(2, 6))
            abst.remove(abs(xwert1))
            wert_abst = random.choice(abst)
            xwert2 = xwert1 + wert_abst
            xwerts = 0.5 * (xwert2 + xwert1)
            a_max = int(abs(20 / wert_abst ** 2))
        xwert_extrema = [xwerts]
        faktor = -1 * nzahl(1, abs(a_max) * 2) / 2 if xwert1 * xwert2 < 0 else nzahl(1, a_max) / 2
        fkt = collect(expand(faktor * (x - xwert1) * (x - xwert2)), x)
        fkt_str = (vorz_v_aussen(faktor, 'x^2') + vorz_v_innen(-1 * faktor * (xwert1 + xwert2), 'x')
                   + vorz_str(faktor * xwert1 * xwert2))
        koeff = [faktor, -1*faktor*(xwert1 + xwert2), faktor*xwert1*xwert2]
        p_fkt = -1 * (xwert1 + xwert2)
        q_fkt = xwert1 * xwert2
    elif grad == 3:
        xwert_extrema1 = -1 * nzahl(1, 4)
        ywert_extrema1 = zzahl(1, 10)
        xwert_extrema2 = nzahl(1,4)
        xwert_extrema = [xwert_extrema1, xwert_extrema2]
        nst = random.randint(xwert_extrema1 + 1, xwert_extrema2 - 1)
        glsystem = Matrix(((nst ** 3, nst ** 2, nst, 1, 0),
                           (xwert_extrema1 ** 3, xwert_extrema1 ** 2, xwert_extrema1, 1, ywert_extrema1),
                           (3 * xwert_extrema1 ** 2, 2 * xwert_extrema1, 1, 0, 0),
                           (3 * xwert_extrema2 ** 2, 2 * xwert_extrema2, 1, 0, 0)))
        lsg = solve_linear_system(glsystem, a, b, c, d)
        lsg_gzahl = vektor.kuerzen((lsg[a], lsg[b], lsg[c], lsg[d]))
        faktor = zzahl(3, 7) / 2
        koeff = k1, k2, k3, k4 = [faktor*element for element in lsg_gzahl]
        fkt = k1 * x ** 3 + k2 * x ** 2 + k3 * x + k4
        fkt_str = (vorz_v_aussen(k1,'x^3') + vorz_v_innen(k2,'x^2')
                   + vorz_v_innen(k3,'x') + vorz_str(k4))
        lsg_nst = solve(fkt, x)
        lsg_nst.sort()
        nst1, nst2, nst3 = lsg_nst
        xmin = int(round(nst1 - 0.4, 0))
        xmax = int(round(nst3 + 0.4, 0))
    elif grad == 4:
        nst_12 = nzahl(1, 9)
        nst_34 = nst_12 + nzahl(1, 9)
        xmin = int(round(-1*sqrt(nst_34) - 0.4, 0))
        xmax = int(round(sqrt(nst_34) + 0.4, 0))
        xwert_extrema1 = N(-0.5*(sqrt(nst_34) + sqrt(nst_12)),2)
        xwert_extrema3 = N(0.5*(sqrt(nst_34) + sqrt(nst_12)),2)
        xwert_extrema = [xwert_extrema1, 0, xwert_extrema3]
        faktor = zzahl(1, 7) / 2
        fkt = collect(expand(faktor * (x ** 2 - nst_12) * (x ** 2 - nst_34)), x) # f(x)= a*x**4 - x**2*(a*b + a*c) + a*b*c
        fkt_str = (vorz_v_aussen(faktor,'x^4') + vorz_v_innen(-1*faktor*(nst_12 + nst_34),'x^2')
                   + vorz_str(faktor*nst_12 * nst_34))
        fkt_z_str = (vorz_v_aussen(faktor,'z^2') + vorz_v_innen(-1*faktor*(nst_12 + nst_34),'z')
                     + vorz_str(faktor*nst_12 * nst_34))
        koeff = [faktor, -1*faktor*(nst_12 + nst_34), faktor*nst_12 * nst_34]

    else:
        exit('Fehler bei "polynome_untersuchen": der eingegebene Parameter für "grad=" muss 2, 3 oder 4 sein.')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               NoEscape('Gegeben ist die Funktion f(x) = $' + fkt_str + '$'),' \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen den Graphen der Funktion zeichnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        if grad == 2:
            # plot(fkt, fkt_n, (x,xmin,xmax))
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichnen Sie den Graphen der Funktion f.')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Koordinatensystem~(2BE) \quad Werte~(1BE)'
                                                    r' \quad Graph~(1BE) \to \quad insgesamt~(5P) }')
            graph_xyfix(fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
            loesung.append('Figure')
            punkte = 4
        elif grad == 3 or grad == 4:
            # plot(fkt, fkt_n, (x,xmin,xmax))
            aufgabe.append(beschriftung(teilaufg,i)
                           + f'Zeichnen Sie den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ].')
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' \mathrm{Koordinatensystem:~2BE \quad Werte:~2BE'
                           + r' \quad Graph:~1BE \to \quad insgesamt~5BE}')
            Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
            loesung.append('Figure')
            punkte = 5

        if 'b' not in teilaufg:
            aufgabe.append(' \n\n')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # wählt man Teilaufgabe f, wird unter der Aufgabe kariertes Papier eingefügt
        aufgabe.append(['Bild', '400px'])
        grafiken_aufgaben.append('notizen_gross')
        aufgabe.append('NewPage') if neue_seite == i else ''

    if 'c' in teilaufg:
        fkt_1 = diff(fkt,x,2)
        kruemmung_x1 = fkt_1.subs(x, xwert_extrema[0])
        # Die SuS sollen die Funktion auf Monotonie untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(teilaufg,i)
                                 + 'Untersuchen Sie die Funktion f auf Monotonie.'), ' \n\n'))
        if kruemmung_x1 > 1:
            liste_monotonie = ['fallend', 'steigend']
            for step in range(len(xwert_extrema) - 1):
                liste_monotonie.append(liste_monotonie[step])
        else:
            liste_monotonie = ['steigend', 'fallend']
            for step in range(len(xwert_extrema) - 1):
                liste_monotonie.append(liste_monotonie[step])

        text = (beschriftung(teilaufg,i,True) + r' \mathrm{Die~Funktion~ist~im~Intervall~I(- \infty \vert '
                + gzahl(xwert_extrema[0]) + ')~ monoton ~' + liste_monotonie[0] + r'} \\')
        for step in range(len(xwert_extrema)):
            if step < len(xwert_extrema) - 1:
                text = (text + r' \mathrm{im ~ Intervall ~ I(' + gzahl(xwert_extrema[step]) + r' \vert '
                        + gzahl(xwert_extrema[step+1]) + r' ) ~monoton~ ' + liste_monotonie[step+1]+ r'} \\')
            else:
                text = (text + r' \mathrm{und ~ im ~ Intervall ~ I(' + gzahl(xwert_extrema[step])
                        + r' \vert \infty ) ~ monoton ~' + liste_monotonie[step+1] + r'}')
        loesung.append(text + r'\\ \mathrm{insgesamt \quad ' + gzahl(len(liste_monotonie)) + 'BE}')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(len(liste_monotonie))
        i += 1

    if 'd' in teilaufg:
        # Die SuS sollen die Schnittpunkte mit den Achsen berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Schnittpunkte der Funktion f mit den '
                       + f'Achsen. \n\n')
        if grad == 2:
            text, lsg, punkte = quadr_gl(koeff, schnittpkt=True)
            loesung.append(beschriftung(teilaufg,i,True) + text[0])
        elif grad == 3:
            text, lsg, punkte = kubische_gl(koeff, lsg_nst, schnittpkt=True)
            loesung.append(beschriftung(teilaufg,i,True)
                           + r' \mathrm{Ansatz: \quad }' + text[0])
            for step in range(len(text)-1):
                loesung.append(text[step+1])
        elif grad == 4:
            text, lsg, punkte = quadr_gl(koeff, var='z')
            if sqrt(nst_12)%1==0:
                S2 = r'S_{x_1}(-' + gzahl(sqrt(nst_12)) + r' \vert 0) \quad '
                S3 = r'S_{x_2}(' + gzahl(sqrt(nst_12)) + r' \vert 0) \quad '
            else:
                S2 = r'S_{x_1}(- \sqrt{' + gzahl(nst_12) + r'} \vert 0) \quad '
                S3 = r' S_{x_2}( \sqrt{' + gzahl(nst_12) + r'} \vert 0) \quad '
            if sqrt(nst_34)%1==0:
                S1 = r'S_{x_3}(-' + gzahl(sqrt(nst_34)) + r' \vert 0) \quad '
                S4 = r'S_{x_4}(' + gzahl(sqrt(nst_34)) + r' \vert 0) \quad \mathrm{und} \quad '
            else:
                S1 = r' S_{x_3}( - \sqrt{' + gzahl(nst_34) + r'} \vert 0) \quad '
                S4 = r' S_{x_4}( \sqrt{' + gzahl(nst_34) + r'} \vert 0) \quad \mathrm{und} \quad '

            loesung.append(beschriftung(teilaufg,i,True) + r' \mathrm{Lösung~durch~Substitution~von}~z=x^2:'
                           + r' \quad f(x) ~ \to ~ f(z) ~=~ ' + fkt_z_str
                           + r' \quad (1BE) \\ \mathrm{Ansatz: \quad }' + text[0]
                           + r' \\ \mathrm{Rücksubstitution} ~ \sqrt{z} = \pm x \quad \to \quad x_{1,2} ~=~ '
                           + r' \pm \sqrt{' + gzahl(nst_12) + r'} \quad \mathrm{und} \quad x_{3,4} ~=~ \pm \sqrt{'
                           + gzahl(nst_34) + r'} \quad (2BE) \\' + S1 + S2 + S3 + S4 + r' S_{y}( 0 \vert '
                           + gzahl(koeff[2]) + r') \quad (2BE) \\')
            punkte += 5

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1



    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# Komplexe Aufgaben (d.h. zur Differenzial- und Integralrechnung)
def kurvendiskussion_polynome(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ableitungen=None, grad=3, wendenormale=True, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS eine vollständige Kurvendiskussion eines Polynoms (dritten oder vierten Grades) durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'ableitungen=' kann Teilaufgabe d) festgelegt werden. Standardmäßig ist 'ableitung=None' und die SuS müssen in Teilaufgabe d) die Ableitungen berechnen. Ist 'ableitungen=True' sind die Ableitungen gegeben und die SuS müssen mithilfe der Ableitungsregeln die Berechnung der Ableitung erläutern.
    # Mit dem Parameter 'grad=' wird die Art der Nullstellen der Funktion festgelegt. Bei Funktionen dritten Grades gibt es immer eine ganzzahlige Nullstelle. Bei 'grad=4' handelt es sich um eine biquadratische Funktion. Standardmäßig ist 'grad=3' eingestellt.
    # Mit dem Parameter 'wendenormale=' kann für Teilaufgabe h) festgelegt werden, ob die Wendenormale berechnet werden soll. Standardmäßig ist 'wendenormale=True' und die Wendenormale ist in Teilaufgabe h) enthalten.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    if grad == 3:
        xwert_extrema1 = -1 * nzahl(1, 4)
        ywert_extrema1 = zzahl(1, 10)
        abstand = nzahl(1, 3)
        xwert_extrema2 = nzahl(1,4)
        xwert_wendepkt = (xwert_extrema1 + xwert_extrema2)/2
        nst = random.randint(xwert_extrema1 + 1, xwert_extrema2 - 1)
        glsystem = Matrix(((nst ** 3, nst ** 2, nst, 1, 0),
                           (xwert_extrema1 ** 3, xwert_extrema1 ** 2, xwert_extrema1, 1, ywert_extrema1),
                           (3 * xwert_extrema1 ** 2, 2 * xwert_extrema1, 1, 0, 0),
                           (3 * xwert_extrema2 ** 2, 2 * xwert_extrema2, 1, 0, 0)))
        lsg = solve_linear_system(glsystem, a, b, c, d)
        lsg_gzahl = vektor.kuerzen((lsg[a], lsg[b], lsg[c], lsg[d]))
        faktor = zzahl(3, 7) / 2
        fkt_a1, fkt_a2, fkt_a3, fkt_a4 = [faktor*element for element in lsg_gzahl]
        print(fkt_a1)
        fkt = fkt_a1 * x ** 3 + fkt_a2 * x ** 2 + fkt_a3 * x + fkt_a4
        fkt_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2')
                   + vorz_v_innen(fkt_a3,'x') + vorz_str(fkt_a4))
        lsg_nst = solve(fkt, x)
        lsg_nst.sort()
        nst_1, nst_2, nst_3 = lsg_nst
        fkt_1 = 3*fkt_a1 * x**2 + 2*fkt_a2 * x + fkt_a3
        fkt_1_str = vorz_v_aussen(3*fkt_a1,'x^2') + vorz_v_innen(2*fkt_a2, 'x') + vorz_str(fkt_a3)
        fkt_2 = 6*fkt_a1 * x + 2*fkt_a2
        fkt_2_str = vorz_v_aussen(6*fkt_a1, 'x') + vorz_str(2*fkt_a2)
        fkt_3 = 6*fkt_a1
        fkt_3_str = gzahl(6*fkt_a1)
        # print('x_{E_1} =~= ' + str(xwert_extrema1)), print('x_{E_2} =~= ' + str(xwert_extrema2))
        # print('x_W =~= ' + str(xwert_wendepkt)), print('Nst:' + str(lsg_nst))
        # print(fkt_str)
    elif grad == 4:
        nst_12 = nzahl(1, 9)
        nst_34 = nst_12 + nzahl(1, 9)
        faktor = zzahl(1, 7) / 2
        fkt = collect(expand(faktor * (x ** 2 - nst_12) * (x ** 2 - nst_34)), x) # f(x)= a*x**4 + x**2*(-a*b - a*c) + a*b*c
        fkt_str = (vorz_v_aussen(faktor,'x^4') + vorz_v_innen(-1*faktor*(nst_12 + nst_34),'x^2')
                   + vorz_str(faktor*nst_12 * nst_34))

        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * (nst_12 + nst_34)
        fkt_a3 = faktor * nst_12 * nst_34
        fkt_1 = collect(diff(fkt,x,1), x)
        fkt_1_str = vorz_v_aussen(4 * faktor,'x^3') + vorz_v_innen(-2*faktor*(nst_12 + nst_34),'x')
        fkt_2 = collect(diff(fkt, x, 2), x)
        fkt_2_str = vorz_v_aussen(12 * faktor, 'x^2') + vorz_str(-2 * faktor * (nst_12 + nst_34))
        fkt_3 = collect(diff(fkt, x, 3), x)
        fkt_3_str = vorz_v_aussen(24 * faktor, 'x')


    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen das Verhalten der Funktion im Unendlichen untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(beschriftung(teilaufg,i) + f'Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \lim \limits_{x \to \infty } ' + fkt_str + '~=~'
                       + gzahl(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim \limits_{x \to - \infty} '
                       + fkt_str + '~=~' + gzahl(grenzwert_min) + r' \quad (2BE)')
        liste_punkte.append(2)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Funktion auf Symmetrie untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        fkt_sym = fkt.subs(x, -x)
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3BE)')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3BE)')
        else:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad '
                                                          r' \mathrm{nicht~symmetrisch} \quad (3BE)')
        aufgabe.append(beschriftung(teilaufg,i) + f'Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + lsg)
        liste_punkte.append(3)
        i += 1
    if 'c' in teilaufg:
        # Die SuS sollen die Schnittpunkte der Funktion mit den Achsen berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i)
                       + f'Berechnen Sie die Schnittpunkte mit den Achsen der Funktion f. \n\n')
        if grad == 3:
            if fkt_a2 == 0 and fkt_a4 == 0:
                punkte = 8
                fkt_x_ausgekl_str = vorz_v_aussen(fkt_a1, 'x^2') + vorz_str(fkt_a3)
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Ansatz: ~f(x)}~=~0 \quad \to \quad 0~=~'
                               + fkt_str + r' ~=~ x \cdot (' + fkt_x_ausgekl_str
                               + r') \quad \to \quad x_1 = 0 \quad (3BE) \\ 0~=~' + fkt_x_ausgekl_str
                               + r' \quad \vert ' + vorz_str(-1 * fkt_a3) + r' \quad \vert \div'
                               + gzahl_klammer(fkt_a1) + r' \quad \to \quad x_{2,3}~=~ \pm \sqrt{'
                               + latex(Rational(-1 * fkt_a3, fkt_a1)) + r'} ~=~ \pm ' + gzahl(N(nst_3,3))
                               + r' \quad (3BE) \\ \mathrm{ S_{x_2}(' + gzahl(N(nst_1, 3))
                               + r' \vert 0) \quad S_y ~=~ S_{x_1}(0 \vert 0) \quad S_{x_3}(' + gzahl(N(nst_3, 3))
                               + r' \vert 0) \quad (2BE)} \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
            elif fkt_a4 == 0:
                punkte = 11
                fkt_x_ausgekl_str = vorz_v_aussen(fkt_a1, 'x^2') + vorz_v_innen(fkt_a2,'x') + vorz_str(fkt_a3)
                fkt_pq_str = 'x^2' + vorz_v_innen(Rational(fkt_a2,fkt_a1),'x') + vorz_str(Rational(fkt_a3,fkt_a1))
                fkt_p = Rational(fkt_a2,fkt_a1)
                fkt_q = Rational(fkt_a3,fkt_a1)
                fkt_diskr = sqrt((fkt_p/2)**2 - fkt_q)
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Ansatz:~f(x)}~=~0 \quad \to \quad 0~=~'
                               + fkt_str + r' ~=~ x \cdot ' + fkt_x_ausgekl_str
                               + r' \quad \to \quad x_1 = 0 \quad (3BE)  \\ 0~=~' + fkt_x_ausgekl_str
                               + r' \quad \vert \div' + gzahl_klammer(fkt_a1) + r' \quad \to \quad 0~=~' + fkt_pq_str
                               + r' \quad (2BE)  \\ x_{2,3}~=~ - \frac{' + gzahl(fkt_p)
                               + r'}{2} \pm \sqrt{ \left( \frac{' + gzahl(fkt_p) + r'}{2} \right) ^2'
                               + vorz_str(-1 * fkt_q) + r'} ~=~ ' + gzahl(Rational(-1*fkt_a2,2*fkt_a1)) + r' \pm '
                               + gzahl(N(fkt_diskr,3)) + r' \quad \to \quad x_2 ~=~' + gzahl(N(nst_1,3))
                               + r' \quad und \quad x_3 ~=~' + gzahl(N(nst_3,3)) + r' \quad (4BE) \\ \mathrm{ S_{x_2}('
                               + gzahl(round(nst_1, 3)) + r' \vert 0) \quad S_y ~=~ S_{x_1}(0 \vert 0) \quad S_{x_3}('
                               + gzahl(round(nst_3, 3)) + r' \vert 0) \quad (2BE)} \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
            else:
                punkte = 14
                # Berechnung der Werte für Hornerschema
                fkt_b2 = nst_2 * fkt_a1
                fkt_c2 = fkt_a2 + fkt_b2
                fkt_b3 = nst_2 * fkt_c2
                fkt_c3 = fkt_a3 + fkt_b3
                fkt_b4 = nst_2 * fkt_c3
                fkt_c4 = fkt_a4 + fkt_b4

                # Tabelle Hornerschema
                table2 = Tabular('c c|c|c|c', row_height=1.2)
                table2.add_row('', gzahl(fkt_a1), gzahl(fkt_a2), gzahl(fkt_a3), gzahl(fkt_a4))
                table2.add_hline(2, 5)
                table2.add_row('Berechnung der Partialfunktion  mit Hornerschema: ', '',
                               gzahl(fkt_b2), gzahl(fkt_b3), gzahl(fkt_b4))
                table2.add_hline(2, 5)
                table2.add_row('', gzahl(fkt_a1), gzahl(fkt_c2), gzahl(fkt_c3), gzahl(fkt_c4))

                fkt_partial = collect(simplify(fkt / (x - nst_2)), x)
                fkt_partial_pq = collect(simplify((x ** 3 + lsg_gzahl[1]/lsg_gzahl[0] * x ** 2
                                                   + lsg_gzahl[2]/lsg_gzahl[0] * x
                                                   + lsg_gzahl[3]/lsg_gzahl[0])  / (x - nst_2)), x)
                nst_partial = solve(fkt_partial_pq, x)
                fkt_partial_p = -1 * (nst_partial[0] + nst_partial[1])
                fkt_partial_q = nst_partial[0] * nst_partial[1]

                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                               + fkt_str + r' \quad \mathrm{durch~probieren:~x_1~=~}' + gzahl(nst_2)
                               + r' \quad (2BE) \\' + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_2) + ')~=~'
                               + latex(fkt_partial) + r' \quad (4P)')
                loesung.append(table2)
                loesung.append(latex(fkt_partial) + r'~=~0 \quad \vert ~ \div ' + gzahl_klammer(fkt_a1)
                               + r' \quad \to \quad 0~=~' + latex(fkt_partial_pq) + r' \quad (2BE) \\'
                               + r' x_{2/3}~=~ - \frac{' + gzahl_klammer(fkt_partial_p) + r'}{2} \pm \sqrt{ \left('
                               + r' \frac{' + latex(fkt_partial_p) + r'}{2} \right) ^2-' + gzahl_klammer(fkt_partial_q)
                               + r'} \quad (2BE) \\' + r' x_2~=~' + gzahl(round(nst_1, 3))
                               + r' \quad \mathrm{und} \quad x_3~=~' + gzahl(round(nst_3, 3)) + r' \quad (2BE) \\'
                               + r'S_{x_1}(' + gzahl(nst_2) + r' \vert 0) \quad S_{x_2}(' + gzahl(round(nst_1, 3))
                               + r' \vert 0) \quad S_{x_3}(' + gzahl(round(nst_3, 3)) + r' \vert 0)'
                               + r' \quad S_y(0 \vert' + gzahl(fkt_a4) + r') \quad (2BE) \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        elif grad == 4:
            punkte = 14
            fkt_z_str = (vorz_v_aussen(faktor,'z^2') + vorz_v_innen(-1*faktor*(nst_12 + nst_34),'z')
                   + vorz_str(faktor*nst_12 * nst_34))
            fkt_z_pq = 'z^2' + vorz_v_innen(-1*(nst_12 + nst_34),'z') + vorz_str(nst_12 * nst_34)
            fkt_z_p = -1*(nst_12 + nst_34)
            fkt_z_q = nst_12 * nst_34
            if sqrt(nst_12)%1==0:
                S1 = r'S_{x_1}(-' + gzahl(sqrt(nst_12)) + r' \vert 0) \quad '
                S2 = r'S_{x_2}(' + gzahl(sqrt(nst_12)) + r' \vert 0) \quad '
            else:
                S1 = r'S_{x_1}(- \sqrt{' + gzahl(nst_12) + r'} \vert 0) \quad '
                S2 = r' S_{x_2}( \sqrt{' + gzahl(nst_12) + r'} \vert 0) \quad '
            if sqrt(nst_34)%1==0:
                S3 = r'S_{x_3}(-' + gzahl(sqrt(nst_34)) + r' \vert 0) \quad '
                S4 = r'S_{x_4}(' + gzahl(sqrt(nst_34)) + r' \vert 0) \quad \mathrm{und} \quad '
            else:
                S3 = r' S_{x_3}( - \sqrt{' + gzahl(nst_34) + r'} \vert 0) \quad '
                S4 = r' S_{x_4}( \sqrt{' + gzahl(nst_34) + r'} \vert 0) \quad \mathrm{und} \quad '

            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Lösung~durch~Substitution~von}~z=x^2:'
                           + r' \quad f(x) ~ \to ~ f(z) ~=~ ' + fkt_z_str + r'  \quad (1BE) \\ '
                           + r' \mathrm{Ansatz:}~f(z)~=~0 \quad \to \quad 0~=~' + fkt_z_str
                           + r' \quad \to \quad \vert \div ' + gzahl_klammer(faktor) + r' \quad \to \quad 0 ~=~'
                           + fkt_z_pq + r' \quad (3BE) \\ z_{1,2}~=~ - \frac{' + gzahl(fkt_z_p)
                           + r'}{2} \pm \sqrt{ \left( \frac{' + gzahl(fkt_z_p) + r'}{2} \right) ^2'
                           + vorz_str(-1 * fkt_z_q) + r'} ~=~ ' + gzahl((nst_12 + nst_34)/2) + r' \pm '
                           + gzahl(sqrt(((nst_12 + nst_34)**2)/4-(nst_12*nst_34))) + r' \quad \to \quad z_1 ~=~'
                           + gzahl(nst_12) + r' \quad und \quad z_2 ~=~' + gzahl(nst_34)
                           + r' \quad (4BE) \\ \mathrm{Rücksubstitution} ~ \sqrt{z} = \pm x \quad \to \quad x_{1,2} ~=~ '
                           + r' \pm \sqrt{' + gzahl(nst_12) + r'} \quad \mathrm{und} \quad x_{3,4} ~=~ \pm \sqrt{'
                           + gzahl(nst_34) + r'} \quad (3BE) \\' + S1 + S2 + S3 + S4
                           + r' S_{y}( 0 \vert ' + gzahl(fkt_a3) + r') \quad (3BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        liste_punkte.append(punkte)
        i += 1
    if len([element for element in ['d', 'e', 'f', 'g'] if element in teilaufg]) > 0:
        # Je nach gewählten Parameter 'ableitung=' müssen die SuS entweder die ersten drei Ableitungen berechnen bzw. die Berechnung der Ableitung begründen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if ableitungen:
            punkte = 4
            aufgabe.extend(('Gegeben sind die ersten drei Ableitungen der Funktion f.',
                            r'f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \hspace{5em} f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \hspace{5em} f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str,
                            beschriftung(teilaufg,i) + 'Erläutern Sie mithilfe der elementaren Ableitungsregeln, '
                                + 'wie diese Ableitungen bestimmt wurden. \n\n'))
            # Tabelle mit dem Text
            table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
            table1.add_row(beschriftung(teilaufg,i), MultiColumn(2, align='l',
                            data='Erklärung der Ableitungen'), 'Punkte')
            table1.add_row('', '-', 'bei der Ableitung fällt der hintere Term (die Konstante) '
                           + 'immer weg (Konstantenregel) ', '1P')
            table1.add_row('', '-', 'die einzelnen Summanden können nach der Summenregel '
                           + 'einzeln abgeleitet werden', '1P')
            table1.add_row('', '-', 'die Potenzen von x werden nach der Potenzregeln abgeleitet, '
                           + 'wobei der bisherige Exponent mit dem Faktor multipliziert wird (Faktorregel)'
                           + ' und der neue Exponent um eins kleiner wird', '2P')
            table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
            loesung.append(table1)
            if teilaufg[i+1] == 'f':
                loesung.append(' \n\n\n')
        else:
            punkte = 3
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \hspace{5em} f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \hspace{5em} f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str + r' \quad (3BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1
    if len([element for element in ['e', 'f'] if element in teilaufg]) > 0:
        # Hier sollen die SuS die Extrema und deren Art mithilfe des notwendigen und hinreichenden Kriteriums berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        if grad == 3:
            punkte = 12
            x_12_fkt_1 = solve(fkt_1, x)
            x_1_fkt_1 = round(x_12_fkt_1[0], 3)
            x_2_fkt_1 = round(x_12_fkt_1[1], 3)
            fkt_1_pq_str = ('x^2' + vorz_v_innen(Rational(2*fkt_a2,3*fkt_a1),'x')
                            + vorz_str(Rational(fkt_a3,3*fkt_a1)))
            p_fkt_1_pq = Rational(2*fkt_a2,3*fkt_a1)
            q_fkt_1_pq = Rational(fkt_a3,3*fkt_a1)

            if fkt_2.subs(x, x_1_fkt_1) < 0:
                loesung_f_monotonie_1 = (r'~<~0~ \to HP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3BE) \\')
            else:
                loesung_f_monotonie_1 = (r'~>~0~ \to TP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3BE) \\')

            if fkt_2.subs(x, x_2_fkt_1) < 0:
                loesung_f_monotonie_2 = (r'~<~0~ \to HP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3BE) \\')
            else:
                loesung_f_monotonie_2 = (r'~>~0~ \to TP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3BE) \\')

            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extrema der Funktion f und deren Art'
                           + ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_1_str + r' \vert ~ \div ' + gzahl_klammer(3 * fkt_a1) + r' \quad (1BE) \\  0 ~=~'
                           + fkt_1_pq_str + r' \quad \to \quad ' + r' x_{1/2} ~=~ - \frac{' + gzahl_klammer(p_fkt_1_pq)
                           + r'}{2} \pm \sqrt{ \left(' + r' \frac{' + latex(p_fkt_1_pq) + r'}{2} \right)^2-'
                           + gzahl_klammer(q_fkt_1_pq) + r'} \quad (3BE) \\'
                           + r'x_1~=~' + gzahl(x_1_fkt_1) + r' \quad \mathrm{und} \quad x_2~=~' + gzahl(x_2_fkt_1)
                           + r' \quad (2BE) \\' + r' f^{ \prime \prime }(' + gzahl(x_1_fkt_1) + ')~=~'
                           + gzahl(round(fkt_2.subs(x, x_1_fkt_1), 3)) + loesung_f_monotonie_1
                           + r' f^{ \prime \prime }(' + gzahl(x_2_fkt_1) + ')~=~'
                           + gzahl(round(fkt_2.subs(x, x_2_fkt_1), 3)) + loesung_f_monotonie_2
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        if grad == 4:
            punkte = 13
            x_12_fkt_1 = solve(fkt_1, x)
            x_1_fkt_1 = round(x_12_fkt_1[0], 3)
            x_3_fkt_1 = round(x_12_fkt_1[2], 3)
            fkt_1_str_ausg = vorz_v_aussen(4 * faktor, 'x^2') + vorz_str(-2 * faktor * (nst_12 + nst_34))

            if fkt_2.subs(x, x_1_fkt_1) < 0:
                loesung_f_monotonie_1 = (r'~<~0~ \to HP(~ - \sqrt{' + gzahl((nst_12+nst_34)/2) + r'}~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_12_fkt_1[0]), 3)) + r'~) \quad (2BE) \\')
            else:
                loesung_f_monotonie_1 = (r'~>~0~ \to TP(~ - \sqrt{' + gzahl((nst_12+nst_34)/2) + r'}~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_12_fkt_1[0]), 3)) + r'~) \quad (2BE) \\')

            if fkt_2.subs(x, 0) < 0:
                loesung_f_monotonie_2 = (r'~<~0~ \to HP(~0~ \vert ~' + gzahl(round(fkt.subs(x, 0), 3))
                                         + r'~) \quad (2BE) \\')
            else:
                loesung_f_monotonie_2 = (r'~>~0~ \to TP(~0~ \vert ~' + gzahl(round(fkt.subs(x, 0), 3))
                                         + r'~) \quad (2BE) \\')

            if fkt_3.subs(x, x_3_fkt_1) < 0:
                loesung_f_monotonie_3 = (r'~<~0~ \to HP(~ \sqrt{' + gzahl((nst_12+nst_34)/2) + r'}~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_12_fkt_1[2]), 3)) + r'~) \quad (2BE) \\')
            else:
                loesung_f_monotonie_3 = (r'~>~0~ \to TP(~ \sqrt{' + gzahl((nst_12+nst_34)/2) + r'}~ \vert ~'
                                         + gzahl(round(fkt.subs(x, x_12_fkt_1[2]), 3)) + r'~) \quad (2BE) \\')

            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extrema der Funktion f und deren Art'
                                                    ' mithilfe des hinreichenden Kriteriums. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_1_str + r' ~=~ x \cdot (' + fkt_1_str_ausg + r') \quad \to \quad x_1 ~=~0 \quad (3BE) \\'
                           + r' 0 ~=~ ' + fkt_1_str_ausg + r' \quad \vert ' + vorz_str(2*faktor * (nst_12 + nst_34))
                           + r' \quad \vert \div ' + gzahl_klammer(4 * faktor) + r' \quad (1BE) \\'
                           + r' x^2 ~=~ ' + gzahl((nst_12+nst_34)/2) + r' \quad \vert \sqrt{} \quad \to \quad x_{2,3}'
                           + r'~=~ \pm ~ \sqrt{' + gzahl((nst_12+nst_34)/2) + r'} \quad (3BE) \\'
                           + r' f^{ \prime \prime }( - \sqrt{' + gzahl((nst_12+nst_34)/2) + r'})~=~'
                           + gzahl(round(fkt_2.subs(x, x_12_fkt_1[0]), 3)) + loesung_f_monotonie_1
                           + r' f^{ \prime \prime }(0)~=~' + gzahl(round(fkt_2.subs(x, 0), 3)) + loesung_f_monotonie_2
                           + r' f^{ \prime \prime }( \sqrt{' + gzahl((nst_12+nst_34)/2) + r'})~=~'
                           + gzahl(round(fkt_2.subs(x, x_12_fkt_1[2]), 3)) + loesung_f_monotonie_3
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        liste_punkte.append(punkte)
        i += 1
    if 'f' in teilaufg:
        # Die SuS sollen mithilfe der Ergebnisse der vorherigen Teilaufgabe die Existenz der/des Wendepunkte(s) begründen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if grad == 3:
            aufgabe.append(beschriftung(teilaufg,i) + 'Begründen Sie mithilfe der vorherigen Ergebnisse, '
                                                    'dass diese Funktion einen Wendepunkt besitzt. \n\n')
            table1 = Tabular('p{0.2cm}p{13cm} p{2cm}')
            table1.add_row(str(liste_teilaufg[i]) + ')', 'mögliche Begründung', 'Punkte')
            if 'c' in teilaufg:
                table1.add_row('', 'Da die Funktion drei Nullstellen besitzt und ein Polynom mit ganzrationalen '
                                    'Exponenten ist, hat sie zwei Extrema und damit einen Wendepunkt.', '3P')
                punkte = 3
            if 'e' in teilaufg and 'c' not in teilaufg:
                table1.add_row('', f'Da die Funktion zwei Extrema hat, besitzt sie auch einen Wendepunkt.', '2P')
                punkte = 2
            loesung.append(table1)
            loesung.append(' \n')
        if grad == 4:
            aufgabe.append(beschriftung(teilaufg,i) + 'Nennen und begründen Sie ohne Rechnung, die Anzahl der möglichen'
                                                    ' Wendepunkte dieser Funktion. \n\n')
            table1 = Tabular('p{0.2cm}p{13cm} p{2cm}')
            table1.add_row(beschriftung(teilaufg,i), 'mögliche Begründung', 'Punkte')
            if 'c' in teilaufg:
                table1.add_row('', 'Da die Funktion vier Nullstellen besitzt und ein Polynom mit ganzrationalen '
                                   'Exponenten ist, hat sie drei Extrema und damit zwei Wendepunkte.', '3P')
                punkte = 3
            if 'e' in teilaufg and 'c' not in teilaufg:
                table1.add_row('', f'Da die Funktion drei Extrema hat, besitzt sie auch zwei Wendepunkte.', '2P')
                punkte = 2
            loesung.append(table1)
            loesung.append(' \n')

        liste_punkte.append(punkte)
        i += 1
    if len([element for element in ['g', 'h'] if element in teilaufg]) > 0:
        # Die SuS sollen den Wendepunkt der Funktion berechnen
        if grad == 3:
            punkte = 5
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            xwert_wp1 = N(Rational(-2*fkt_a2, 6 * fkt_a1), 3)
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Wendepunkt der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_2_str + r' \quad \vert ' + vorz_str(-1*2*fkt_a2)
                           + r' \quad \vert \div ' + gzahl_klammer(6 * fkt_a1) + r' \quad \to \quad x_1~=~'
                           + gzahl(xwert_wp1) + r' \quad (2BE) \\ f^{ \prime \prime \prime }('
                           + gzahl(xwert_wp1) + r') \quad \neq 0 \quad \to \quad WP('
                           + gzahl(xwert_wp1) + r' \vert ' + gzahl(round(fkt.subs(x, xwert_wp1), 3))
                           + r') \quad (3BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        if grad == 4:
            punkte = 8
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            xwert_wp1 = N(-1*sqrt(Rational((nst_12 + nst_34),6)),3)
            xwert_wp2 = N(sqrt(Rational((nst_12 + nst_34), 6)),3)
            # fkt_2_str = vorz_v_aussen(12 * faktor, 'x^2') + vorz_str(-2 * faktor * (nst_12 + nst_34))
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Wendepunkte der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                           + fkt_2_str + r' \quad \vert ' + vorz_str(2 * faktor * (nst_12 + nst_34))
                           + r' \quad \vert \div ' + gzahl_klammer(12 * faktor) + r' \quad (2BE) \\ x^2~=~ \pm'
                           + gzahl(Rational((nst_12 + nst_34), 6)) + r' \quad \vert \sqrt{} \quad \to \quad '
                           + r' x_{W_{1,2}} ~=~ \pm ' + gzahl(xwert_wp2) + r'(2BE) \\ f^{ \prime \prime \prime }('
                           + gzahl(xwert_wp1) + ')~=~' + gzahl(N(fkt_3.subs(x, xwert_wp1),3))
                           + r' \quad \neq 0 \quad \to \quad WP(' + gzahl(xwert_wp1) + r' \vert '
                           + gzahl(round(fkt.subs(x, xwert_wp1), 3)) + r') \quad (2BE) \\  f^{ \prime \prime \prime }('
                           + gzahl(xwert_wp2) + ')~=~' + gzahl(N(fkt_3.subs(x, xwert_wp2),3))
                           + r' \quad \neq 0 \quad \to \quad WP(' + gzahl(xwert_wp2)
                           + r' \vert ' + gzahl(round(fkt.subs(x, xwert_wp2), 3))
                           + r') \quad (2BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        liste_punkte.append(punkte)
        i += 1
    if 'h' in teilaufg:
        # Die SuS sollen die Wendetangente bzw. die Wendenormale, abhängig vom gewählten Parameter 'wendenormale', berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        if grad == 3:
            ywert_wp1 = N(fkt.subs(x, xwert_wp1), 3)
            ywert_wp1_fkt_1 = N(fkt_1.subs(x, xwert_wp1), 3)
            fkt_t = ywert_wp1_fkt_1 * (x - xwert_wp1) + ywert_wp1
            fkt_n = (-1 / ywert_wp1_fkt_1) * (x - xwert_wp1) + ywert_wp1

            if wendenormale not in ([True, False]):
                exit("wendenormale muss True oder False sein")
            if wendenormale == True:
                punkte = 6
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Wendetangente und die Wendenormale '
                                                        f'der Funktion f. \n\n')
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                               + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                               + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                               + gzahl(ywert_wp1_fkt_1) + '(x' + vorz_str(-1*xwert_wp1) + ')'
                               + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1, 'x')
                               + vorz_str(N(-1 * ywert_wp1_fkt_1 * xwert_wp1 + ywert_wp1, 3))
                               + r' \quad (3BE) \\ \mathrm{Die~Steigung~der~Normale~am~Wendepunkt~wird~berechnet~mit \quad '
                               + r' m_n ~=~ \frac{-1}{f^{ \prime }(x_{w})} \quad und~daraus~folgt:} \\'
                               + r'n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                               + r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(N(-1 / ywert_wp1_fkt_1,3)) + '(x'
                               + vorz_str(-1 * xwert_wp1) + ')' + vorz_str(ywert_wp1) + '~=~'
                               + vorz_v_aussen(N(-1 / ywert_wp1_fkt_1,3), 'x')
                               + vorz_str(N(xwert_wp1 / ywert_wp1_fkt_1 + ywert_wp1, 3))
                               + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')

            if wendenormale == False:
                punkte = 3
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Funktionsgleichung der Wendetangente'
                               + f' der Funktion f. \n\n')
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                               + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                               + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                               + gzahl(ywert_wp1_fkt_1) + '(x' + vorz_str(-1 * xwert_wp1) + ')'
                               + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1, 'x')
                               + vorz_str(N(-1 * ywert_wp1_fkt_1 * xwert_wp1 + ywert_wp1, 3))
                               + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        if grad == 4:
            ywert_wp2 = N(fkt.subs(x, Rational((nst_12 + nst_34), 6)), 3)
            ywert_wp2_fkt_1 = N(fkt_1.subs(x, Rational((nst_12 + nst_34), 6)), 3)
            fkt_t = ywert_wp2_fkt_1 * (x - xwert_wp2) + ywert_wp2
            fkt_n = (-1 / ywert_wp2_fkt_1) * (x - xwert_wp2) + ywert_wp2

            if wendenormale not in ([True, False]):
                exit("wendenormale muss True oder False sein")
            if wendenormale == True:
                punkte = 6
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Wendetangente und die Wendenormale der '
                               + f'Funktion f bei x = {xwert_wp2}. \n\n')
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                               + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                               + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                               + gzahl(ywert_wp2_fkt_1) + '(x' + vorz_str(-1*xwert_wp2) + ')'
                               + vorz_str(ywert_wp2) + '~=~' + vorz_v_aussen(ywert_wp2_fkt_1, 'x')
                               + vorz_str(N(-1 * ywert_wp2_fkt_1 * ((nst_12 + nst_34)/6) + ywert_wp2, 3))
                               + r' \quad (3BE) \\ \mathrm{Die~Steigung~der~Normale~am~Wendepunkt~wird~berechnet~mit \quad '
                               + r' m_n ~=~ \frac{-1}{f^{ \prime }(x_{w})} \quad und~daraus~folgt:} \\'
                               + r'n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                               + r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(N(-1 / ywert_wp2_fkt_1,3)) + '(x'
                               + vorz_str(-1 * xwert_wp2) + ')' + vorz_str(ywert_wp2) + '~=~'
                               + vorz_v_aussen(N(-1 / ywert_wp2_fkt_1,3), 'x')
                               + vorz_str(N(((nst_12 + nst_34)/6) / ywert_wp2_fkt_1 + ywert_wp2, 3))
                               + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')

            if wendenormale == False:
                punkte = 3
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Funktionsgleichung der Wendetangente'
                               + f' der Funktion f bei x = {xwert_wp2}. \n\n')
                loesung.append(beschriftung(teilaufg,i, True)
                               + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                               + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                               + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                               + gzahl(ywert_wp2_fkt_1) + '(x' + vorz_str(-1 * xwert_wp2) + ')'
                               + vorz_str(ywert_wp2) + '~=~' + vorz_v_aussen(ywert_wp2_fkt_1, 'x')
                               + vorz_str(N(-1 * ywert_wp2_fkt_1 * ((nst_12 + nst_34)/6) + ywert_wp2, 3))
                               + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        liste_punkte.append(punkte)
        i += 1
    if 'i' in teilaufg:
        # Die SuS sollen den Graphen der Funktion zeichnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        if grad == 3:
            xmin = int(round(nst_1 - 0.4, 0))
            xmax = int(round(nst_3 + 0.4, 0))
            # plot(fkt, fkt_n, (x,xmin,xmax))

            aufgabe.append(beschriftung(teilaufg,i)
                           + f'Zeichnen Sie den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ] \n\n')
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' \mathrm{Koordinatensystem~(2BE) \quad Werte~(2BE)'
                                                    r' \quad Graph~(1BE) \to \quad insgesamt~(5P)}')
            Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
            loesung.append('Figure')
        if grad == 4:
            xmin = int(round(-1*sqrt(nst_34) - 0.4,0))
            xmax = int(round(sqrt(nst_34) + 0.4,0))
            # plot(fkt, fkt_n, (x,xmin,xmax))

            aufgabe.append(beschriftung(teilaufg,i)
                           + f'Zeichnen Sie den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ] \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Koordinatensystem~(2BE) \quad Werte~(2BE)'
                           + r' \quad Graph~(1BE) \to \quad insgesamt~(5P)}')
            Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
            loesung.append('Figure')

        liste_punkte.append(5)
        i += 1
    if 'j' in teilaufg:
        # Die SuS sollen die vom Funktionsgraphen im ersten Quadranten eingeschlossene Fläche berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if grad == 3:
            Fkt = integrate(fkt, x)
            Fkt_str = (vorz_v_aussen(Rational(fkt_a1, 4), 'x^4') + vorz_v_innen(Rational(fkt_a2, 3), 'x^3')
                       + vorz_v_innen(Rational(fkt_a3, 2), 'x^2') + vorz_v_innen(fkt_a4, 'x'))
            def erste_positive_nst(vec):
                vec.sort()
                for element in vec:
                    if element > 0:
                        # print(element)
                        return element
                return exit(f'Aufgabe {str(nr)}.{str(liste_teilaufg[i])}): Es gibt keine positive Nullstelle!')

            obere_grenze = N(erste_positive_nst([nst_1, nst_2, nst_3]), 3)
            loesung_integral = Fkt.subs(x, obere_grenze)
            if 'c' in teilaufg:
                aufgabe.extend((f'Der Graph von f schließt, mit der x-Achse und der y-Achse '
                                + ' rechts vom Ursprung eine Fläche ein. \n\n', str(liste_teilaufg[i])
                                + f') Berechnen Sie die eingeschlossen Fläche. \n\n'))
            else:
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Fläche unter dem Graphen '
                                                        f'im Intervall I(0|{gzahl(obere_grenze)}). \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \left| \int \limits_0^{' + gzahl(obere_grenze) + '}' + fkt_str
                           + r'~ \mathrm{d}x \right| ~=~ \left| \left[' + Fkt_str + r' \right]_{0}^{' + gzahl(obere_grenze)
                           + r'} \right| ~=~' + latex(abs(N(loesung_integral, 3))) + r' \quad (4BE) \\')
        if grad == 4:
            Fkt = integrate(fkt, x)
            Fkt_str = (vorz_v_aussen(Rational(fkt_a1, 5), 'x^5') + vorz_v_innen(Rational(fkt_a2, 3), 'x^3')
                       + vorz_v_innen(fkt_a3, 'x'))
            untere_grenze = sqrt(nst_12)
            obere_grenze = sqrt(nst_34)
            loesung_integral = integrate(fkt, (x,untere_grenze,obere_grenze))
            if 'c' in teilaufg:
                aufgabe.extend((f'Der Graph von f schließt, mit der x-Achse'
                                + ' rechts vom Ursprung eine Fläche ein. \n\n', str(liste_teilaufg[i])
                                + f') Berechnen Sie die eingeschlossen Fläche. \n\n'))
            else:
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Fläche unter dem Graphen im Intervall '
                               + f'I({gzahl(N(untere_grenze,3))}| {gzahl(N(obere_grenze,3))}). \n\n')
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' \left| \int \limits_{' + gzahl(N(untere_grenze,3))
                           + '}^{'  + gzahl(N(obere_grenze,3)) + '}' + fkt_str
                           + r'~ \mathrm{d}x \right| ~=~ \left| \left[' + Fkt_str + r' \right]_{'
                           + gzahl(N(untere_grenze,3)) + '}^{' + gzahl(N(obere_grenze,3))
                           + r'} \right| ~=~' + latex(abs(N(loesung_integral, 3))) + r' \quad (4BE) \\')

        liste_punkte.append(4)
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def kurvendiskussion_polynom_parameter(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ableitungen=None, i=0, BE=[]):
    # In dieser Aufgaben sollen die SuS eine Kurvendiskussion einer Polynomfunktion (dritten Grades) mit einem Parameter durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'ableitungen=' kann Teilaufgabe d) festgelegt werden. Standardmäßig ist 'ableitung=None' und die SuS müssen in Teilaufgabe d) die Ableitungen berechnen. Ist 'ableitungen=True' sind die Ableitungen gegeben und die SuS müssen mithilfe der Ableitungsregeln die Berechnung der Ableitung erläutern.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    # Berechnung der Nullstellen und des Faktors
    faktor = zzahl(1, 5)
    faktor_1 = -1*nzahl(5,10)/2
    faktor_2 = zzahl(1,2)
    if faktor_1%1 == 0:
        faktor_3 = faktor_2 + nzahl(0,2)+0.5
    else:
        faktor_3 = faktor_2 + nzahl(1,3)
    while faktor_1 + faktor_2 + faktor_3 == 0:
        faktor_1 = -1 * nzahl(5, 10) / 2
        faktor_2 = zzahl(1,2)
        if faktor_1 % 1 == 0:
            faktor_3 = nzahl(2, 5) + 0.5
        else:
            faktor_3 = nzahl(3, 5)

    nst_1_str = vorz_v_aussen(faktor_1,'a', null=True)
    nst_2_str = vorz_v_aussen(faktor_2,'a', null=True)
    nst_2_str_neg = vorz_v_innen(-1*faktor_2,'a', null=True)
    nst_3_str = vorz_v_aussen(faktor_3,'a', null = True)

    # Aufstellen der Funktionsgleichung
    fkt = collect(expand(faktor * (x - faktor_1 * a) * (x - faktor_2 * a) * (x - faktor_3 * a)),x)

    # Koeffizienten der Funktion
    fkt_a3 = faktor
    fkt_a2 = -1*faktor * (faktor_1 + faktor_2 + faktor_3)
    fkt_a1 = faktor*(faktor_1*faktor_2 + faktor_2*faktor_3 + faktor_1*faktor_3)
    fkt_a0 = -1*faktor*faktor_1*faktor_2*faktor_3

    fkt_str = (vorz_v_aussen(fkt_a3, r'x^3') + vorz_v_innen(fkt_a2, r'a \cdot x^2')
               + vorz_v_innen(fkt_a1, r'a^2 \cdot x') + vorz_v_innen(fkt_a0, r'a^3'))

    print(fkt), print(fkt_str)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion']
    aufgabe.append(r' f_a(x)~=~' + fkt_str + r' \quad \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    # Auswahl des Wertes von a für Teilaufgabe g und h
    a1 = nzahl(1, 4)
    a2 = nzahl(1,6)/2
    while a1 == a2:
        a2 = nzahl(1, 6) / 2

    if 'a' in teilaufg:
        # Die SuS sollen das Verhalten der Funktion im Unendlichen untersuchen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        grenzwert_neg = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(beschriftung(teilaufg,i) + 'Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \lim\limits_{x \to \infty} ' + fkt_str + r'~=~\bm{'
                       + gzahl(grenzwert_pos) + r'} \\ \lim\limits_{x \to - \infty} '
                       + fkt_str + r'~=~\bm{' + gzahl(grenzwert_neg) + r'} \quad (2BE)')
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Funktion auf Symmetrie untersuchen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        liste_punkte.append(punkte)
        fkt_sym = fkt.subs(x, -x)
        fkt_sym_str = (gzahl(-1 * fkt_a3)+ r'x^3 ~' + vorz_str(fkt_a2) + r'a \cdot x^2 ~'
                       + vorz_str(-1 * fkt_a1) + r'a^2 \cdot x ~' + vorz_str(fkt_a0) + r'a^3')
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                   + r'~=~f(x) \\ \to \quad \mathbf{Achsensymmetrie} \quad (3BE) \\')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                   + r'~=~-f(x) \\ \to \quad \mathbf{Punktsymmetrie} \quad (3BE) \\')
        else:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str + r' \neq  f(x)  \neq -f(x) \\ \to \quad '
                                                       r' \mathbf{nicht~symmetrisch} \quad (3BE) \\')
        aufgabe.append(beschriftung(teilaufg,i) + f'Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg, i, True) + lsg)
        i += 1

    if 'c' in teilaufg:
        # Die SuS sollen hier die Schnittpunkte mit den Achsen berechnen. Da alle Nullstellen vom Parameter a abhängen, ist eine Nullstelle gegeben.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 14
        liste_punkte.append(punkte)
        # hier werden die Koeffizenten für das Hornerschema berechnet
        fkt_b2 = faktor * faktor_2
        fkt_c2 = -1 * faktor * (faktor_1 + faktor_3)
        fkt_b1 = -1 * faktor * faktor_2 * (faktor_1 + faktor_3)
        fkt_c1 = faktor * faktor_1 * faktor_3
        fkt_b0 = faktor*faktor_1*faktor_2*faktor_3
        # hier werden das Partialpolynom (Ergebnis Hornerschema) und die Gleichung für die pq-Formel berechnet
        fkt_partial = faktor * x**2 + fkt_c2 * a * x + fkt_c1 * a**2
        fkt_partial_str = (gzahl(faktor) + r' \cdot x^2' + vorz_str(fkt_c2) + r' a \cdot x'
                           + vorz_str(fkt_c1) + r' a^2')
        fkt_p = -1 * (faktor_1 + faktor_3)
        fkt_q = faktor_1 * faktor_3
        fkt_pq_str = 'x^2' + vorz_str(fkt_p) + r' a \cdot x' + vorz_str(fkt_q) + r' a^2'
        fkt_disk = Rational((faktor_1 - faktor_3)**2,4)

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('', gzahl(fkt_a3), NoEscape('$' + gzahl(fkt_a2*a) + '$'),
                       NoEscape('$' + gzahl(fkt_a1*a**2) + '$'), NoEscape('$' + gzahl(fkt_a0*a**3) + '$'))
        table2.add_hline(2, 5)
        table2.add_row('Partialpolynom mit Horner Schema berechnen: ' , '', NoEscape('$' + gzahl(fkt_b2*a) + '$'),
                       NoEscape('$' + gzahl(fkt_b1*a**2) + '$'), NoEscape('$' + gzahl(fkt_b0*a**3) +'$'))
        table2.add_hline(2, 5)
        table2.add_row('', NoEscape('$' + gzahl(fkt_a3) + '$'),
                       NoEscape('$' + gzahl(fkt_c2*a) + '$'), NoEscape('$' + gzahl(fkt_c1*a**2) + '$'), ' 0')

        aufgabe.append(beschriftung(teilaufg,i)
                       + f'Berechnen Sie die Schnittpunkte mit den Achsen der Funktion. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                       + fkt_str + r' \quad (1BE) \\ \mathrm{durch~probieren:} \quad x_2 ~=~ '
                       + nst_2_str + r' \quad \to \quad (' + fkt_str + r')~ \div ~(x' + nst_2_str_neg + r')~=~ \\'
                       + fkt_partial_str + r' \quad (4P)')
        loesung.append(table2)
        loesung.append(' 0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + gzahl_klammer(faktor) +
                       r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2BE) \\'
                       r' x_{1/3}~=~ - \frac{' + latex(fkt_p) + r'a}{2} \pm \sqrt{ \left(' +
                       r' \frac{' + latex(fkt_p) + r'a}{2} \right)^2-(' + latex(fkt_q) +  # p war grundlos ins Minus gestzt
                       r'a^2)} ~=~ ' + gzahl(Rational((faktor_1 + faktor_3),2)) + r'a \pm \sqrt{'
                       + latex(fkt_disk) + r' a^2} \quad (2BE) \\ x_{1/3}~=~'
                       + gzahl(Rational(faktor_1 + faktor_3,2)) + r' a \pm \left('
                       + gzahl(Rational(abs(faktor_1 - faktor_3),2)) + r' \right) a \quad \to \quad x_1~=~'
                       + vorz_v_aussen(faktor_1,'a', null=True) + r' \quad \mathrm{und} \quad x_3~=~'
                       + vorz_v_aussen(faktor_3, 'a', null=True) + r' \quad (3BE) \\ \bm{S_{x_1}(' + nst_1_str + r' \vert 0) \quad S_{x_2}('
                       + nst_2_str + r' \vert 0) \quad S_{x_3}(' + nst_3_str + r' \vert 0) \quad }\mathrm{sowie}'
                       + r' \bm{\quad S_y(0 \vert' + vorz_v_aussen(fkt_a0,'a^3', null=True) + r')} \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if len([element for element in ['d', 'e', 'f', 'g'] if element in teilaufg]) > 0:
        # Je nach gewählten Parameter 'ableitung=' müssen die SuS entweder die ersten drei Ableitungen berechnen bzw. die Berechnung der Ableitung begründen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        fkt_1_a2 = 3*faktor
        fkt_1_a1 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
        fkt_1_a0 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
        fkt_1_p = Rational(-2 * (faktor_1 + faktor_2 + faktor_3),3)
        fkt_1_q = Rational((faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3),3)
        fkt_1_disk = (faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9
        fkt_1_sqrt = sqrt((faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9)

        # Funktionsgleichung und Partialpolynomne
        fkt_1_str = (latex(fkt_1_a2) + 'x^2' + vorz_str(fkt_1_a1) + 'ax'
                     + vorz_str(fkt_1_a0) + r'a^2')
        fkt_1_pq_str = 'x^2' + vorz_str(fkt_1_p) + r'a \cdot x' + vorz_str(fkt_1_q) + r'a^2'
        fkt_2_str = gzahl(6*faktor) + 'x' + vorz_str(fkt_1_a1) + r'a'
        fkt_3_str = gzahl(6*faktor)


        if ableitungen:
            punkte = 4
            aufgabe.extend(('Gegeben sind die ersten drei Ableitungen der Funktion f.',
                            r'f^{ \prime }(x) ~=~' + fkt_1_str
                            + r' \hspace{5em} f^{ \prime \prime }(x) ~=~' + fkt_2_str
                            + r' \hspace{5em} f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str,
                            beschriftung(teilaufg,i) + 'Erläutern Sie mithilfe der elementaren Ableitungsregeln, '
                            + 'wie diese Ableitungen bestimmt wurden. \n\n'))
            # Tabelle mit dem Text
            table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
            table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l',
                                                                     data='Erklärung der Ableitungen'), 'Punkte')
            table1.add_row('', '-', 'bei der Ableitung fällt der hintere Term (die Konstante) '
                           + 'immer weg (Konstantenregel) ', '1P')
            table1.add_row('', '-', 'die einzelnen Summanden können nach der Summenregel '
                           + 'einzeln abgeleitet werden', '1P')
            table1.add_row('', '-', 'die Potenzen von x werden nach der Potenzregeln abgeleitet, '
                           + 'wobei der bisherige Exponent mit dem Faktor multipliziert wird (Faktorregel)'
                           + ' und der neue Exponent um eins kleiner wird', '2P')
            table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
            loesung.append(table1)

        else:
            punkte = 6
            aufgabe.append(beschriftung(teilaufg,i) + 'Bestimmen Sie die ersten drei Ableitungen der Funktion. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{ f^{ \prime }(x) ~=~' + fkt_1_str
                           + r'} \\ \mathrm{f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r'} \\ \mathrm{f^{ \prime \prime \prime }(x) ~=~ ' + fkt_3_str
                           + r'} \\ \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Die SuS sollen die Extrempunkte und deren Art mithilfe des hinreichenden Kriteriums berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 12
        liste_punkte.append(punkte)
        fkt_1 = collect(diff(fkt,x,1),x)
        fkt_2 = collect(diff(fkt,x,2),x)
        x_12_fkt_1 = solve(fkt_1, x)
        x_1_fkt_1 = x_12_fkt_1[0]
        x_2_fkt_1 = x_12_fkt_1[1]
        y_1_fkt = fkt.subs(x, x_1_fkt_1)
        y_2_fkt = fkt.subs(x, x_2_fkt_1)
        x_1_fkt_2 = fkt_2.subs(x,x_1_fkt_1)
        x_2_fkt_2 = fkt_2.subs(x,x_2_fkt_1)
        # print(x_1_fkt_2), print(x_2_fkt_2)
        if x_1_fkt_2.subs(a,1) < 0:
            lsg_extrema_1 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad \mathbf{HP}\bm{(' + gzahl(N(x_1_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_1_fkt,3)) + r')} \quad (2BE) \\')
        else:
            lsg_extrema_1 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad \mathbf{TP}\bm{(' + gzahl(N(x_1_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_1_fkt,3)) + r')} \quad (2BE) \\')

        if x_2_fkt_2.subs(a,1) < 0:
            lsg_extrema_2 = (r' \quad \mathrm{<~0~da~a>0} \quad \to \quad \mathbf{HP}\bm{(' + gzahl(N(x_2_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_2_fkt,3)) + r')} \quad (2BE) \\')
        else:
            lsg_extrema_2 = (r' \quad \mathrm{>~0~da~a>0} \quad \to \quad \mathbf{TP}\bm{(' + gzahl(N(x_2_fkt_1,3)) + r' \vert '
                             + gzahl(N(y_2_fkt,3)) + r')} \quad (2BE) \\')

        # Koeffizienten der ersten Ableitung
        # fkt_a3 = faktor
        # fkt_a2 = -1 * faktor * (faktor_1 + faktor_2 + faktor_3)
        # fkt_a1 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
        # fkt_a0 = -1 * faktor * faktor_1 * faktor_2 * faktor_3
        fkt_1_a2 = 3*faktor
        fkt_1_a1 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
        fkt_1_a0 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
        fkt_1_p = Rational(-2 * (faktor_1 + faktor_2 + faktor_3),3)
        fkt_1_q = Rational((faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3),3)
        fkt_1_disk = (faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9
        fkt_1_sqrt = sqrt((faktor_1**2 + faktor_2**2 + faktor_3**2 - (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3))/9)

        # Funktionsgleichung und Partialpolynomne
        fkt_1_str = (latex(fkt_1_a2) + 'x^2' + vorz_str(fkt_1_a1) + r'a \cdot x'
                     + vorz_str(fkt_1_a0) + r'a^2')
        fkt_1_pq_str = 'x^2' + vorz_str(fkt_1_p) + r'a \cdot x' + vorz_str(fkt_1_q) + r'a^2'
        fkt_2_str = gzahl(6*faktor) + 'x' + vorz_str(fkt_1_a1) + r'a'

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extrempunkte der Funktion und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_1_str + r' \vert ~ \div ' + gzahl_klammer(3 * faktor) + r' \quad (1BE) \\'
                       r' 0~=~ ' + fkt_1_pq_str + r' \quad (1BE) \\' + r' x_{1/2}~=~ - \frac{'
                       + gzahl(fkt_1_p) + r' a}{2} \pm \sqrt{ \left( \frac{'
                       + gzahl(fkt_1_p) + r' a}{2} \right)^2 - \left(' + gzahl(fkt_1_q)
                       + r' a^2 \right) } \quad (1BE) \\ =~ ' + gzahl(N(-1*fkt_1_p/2,3)) + r' a \pm \sqrt{'
                       + gzahl(N(fkt_1_disk,3)) + r' a^2} \quad ~=~ ' + gzahl(N(-1*fkt_1_p/2,3)) + r' a \pm '
                       + gzahl(N(fkt_1_sqrt,3)) + r' a \quad (1BE) \\'
                       + r'x_1~=~' + gzahl(-1*fkt_1_p/2) + r' a ~-~' + gzahl(N(fkt_1_sqrt,3))
                       + r' a~=~' + gzahl(N(x_1_fkt_1,3)) + r' \quad \mathrm{und} \quad '
                       + r'x_2~=~' + gzahl(-1*fkt_1_p/2) + r' a~+~' + gzahl(N(fkt_1_sqrt,3))
                       + r' a~=~' + gzahl(N(x_2_fkt_1,3)) + r' \quad (2BE) \\'
                       + r'f^{ \prime \prime } (' + gzahl(N(x_1_fkt_1,3)) +') ~=~' + gzahl(6*faktor) + r' \cdot ('
                       + gzahl(N(x_1_fkt_1,3)) + ')' + vorz_str(fkt_1_a1) + r' a ~=~'
                       + gzahl(N(x_1_fkt_2,3)) + r' \quad (1BE)' + lsg_extrema_1
                       + r' f^{ \prime \prime } (' + gzahl(N(x_2_fkt_1,3)) + ') ~=~' + gzahl(6 * faktor)
                       + r' \cdot (' + gzahl(N(x_2_fkt_1,3)) + ')' + vorz_str(fkt_1_a1) + 'a  ~=~'
                       + gzahl(N(x_2_fkt_2,3)) + r' \quad (1BE)' + lsg_extrema_2
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'f' in teilaufg:
        # Die SuS sollen dem Wendepunkt der Funktion berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        liste_punkte.append(punkte)
        fkt_2_a0 = -2*faktor*(faktor_1 + faktor_2 + faktor_3)
        fkt_2_str = gzahl(6*faktor) + 'x' + vorz_str(fkt_2_a0) + 'a'
        xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3),3)
        xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3)/3,3)
        ywert_wp_dezimal = N(fkt.subs(x,xwert_wp_bruch*a),3)
        fkt_3_str = gzahl(6*faktor)

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die möglichen Wendepunkte der Funktion. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ~' + vorz_str(-1*fkt_2_a0) + r'a \quad \vert \div '
                       + gzahl_klammer(6 * faktor) + r' \quad (1BE) \\ x_1~=~' + gzahl(xwert_wp_bruch) + 'a ~=~'
                       + gzahl(xwert_wp_dezimal) + r'a \quad \quad \to \quad f^{ \prime \prime \prime }\left('
                       + gzahl(xwert_wp_bruch) + r'a \right) ~=~ ' + fkt_3_str
                       + r' \quad \neq 0 \quad \to \quad \mathbf{Wendepunkt} \bm{\left(' + gzahl(xwert_wp_bruch)
                       + r'a \vert ' + gzahl(ywert_wp_dezimal) + r' \right)} \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'g' in teilaufg:
        # Die SuS sollen die Ortskurve der Wendepunkte berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        liste_punkte.append(punkte)
        xwert_wp_bruch = Rational((faktor_1 + faktor_2 + faktor_3), 3)
        xwert_wp_dezimal = N((faktor_1 + faktor_2 + faktor_3) / 3)
        ywert_wp_dezimal = N(fkt.subs(x, xwert_wp_bruch*a), 3)
        if Rational(3,(faktor_1 + faktor_2 + faktor_3)) > 0:
            abhängigkeit = r' \mathrm{mit~x \in \mathbb{R} ~und~ x > 0}'
        else:
            abhängigkeit = r' \mathrm{mit~x \in \mathbb{R} ~und~ x < 0}'

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Ortskurve der Wendepunkte. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' x ~=~' + (gzahl(xwert_wp_bruch))
                       + r'a \quad \vert \div' + gzahl_klammer(Rational((faktor_1 + faktor_2 + faktor_3),3))
                       + r' \quad \to \quad a~=~' + gzahl(Rational(3,(faktor_1 + faktor_2 + faktor_3)))
                       + r'x \quad ' + abhängigkeit + r' \quad (2BE) \\ \mathrm{einsetzen~in~y} ~=~'
                       + gzahl(ywert_wp_dezimal) + '~=~' + gzahl(ywert_wp_dezimal/a**3) + r' \left('
                       + gzahl(Rational(3,(faktor_1 + faktor_2 + faktor_3))) + r'x \right)^3 ~=~\bm{'
                       + gzahl(N((ywert_wp_dezimal/a**3)*(3/(faktor_1 + faktor_2 + faktor_3))**3,4))
                       + r'x^3} \quad (3BE)')
        i += 1

    if 'h' in teilaufg:
        # Die bekommen einen Graphen der Parameterfunktion vorgegeben und sollen daraus den Wert für a bestimmen und ihre Anwort begründen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        punkte = 4
        liste_punkte.append(punkte)
        nst_1_a1 = faktor_1 * a1
        nst_3_a1 = faktor_3 * a1
        fkt_a1 = expand(faktor * (x - faktor_1 * a1) * (x - faktor_2 * a1) * (x - faktor_3 * a1))
        xmin_f = int(nst_1_a1 - 1)
        xmax_f = int(nst_3_a1 + 1)
        Graph(xmin_f,xmax_f,fkt_a1,name=f'Aufgabe_{nr}{liste_teilaufg[i]}')
        aufgabe.extend(('In der folgenden Abbildung ist ein Graph der Parameterfunktion dargestellt. '
                        'Dabei wurde für a ein Wert aus den natürlichen Zahlen gewählt.', 'Figure',
                        beschriftung(teilaufg,i) + f'Bestimmen Sie aus dem Graphen den zugehörigen Wert von a. '
                        + f'Begründen Sie ihre Aussage. \n\n'))
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Die~zweite~Nullstelle~des'
                       + r'~Graphen~liegt~bei~ca.~x_2=' + str(faktor_2*a1)
                       + r'.~} \mathrm{Die~berechnete~Nullstelle~liegt~bei~x_2=' + nst_2_str
                       + r'.~} \\ \mathrm{Damit~gilt:~}' + str(faktor_2*a1) + '~=~' + nst_2_str
                       + r' \quad \to \quad \bm{a~=~' + str(a1) + r'} \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'i' in teilaufg:
        # Die SuS sollen den Graphen für einen vorgegebenen Wert für a in einem festgelegten Intervall zeichnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        punkte = 5
        liste_punkte.append(punkte)
        nst_1_a2 = faktor_1 * a2
        nst_3_a2 = faktor_3 * a2
        fkt_a2 = expand(faktor * (x - faktor_1 * a2) * (x - faktor_2 * a2) * (x - faktor_3 * a2))
        xmin_f = int(round(nst_1_a2 - 0.5,0))
        xmax_f = int(round(nst_3_a2 + 0.5,0))
        Graph(xmin_f,xmax_f,fkt_a2,name=f'Loesung_{nr}{liste_teilaufg[i]}')
        aufgabe.append(beschriftung(teilaufg,i) + f'Zeichnen Sie den Graphen für a = {gzahl(a2)} im '
                       + f'Intervall [ {xmin_f} | {xmax_f} ]. \n\n')
        loesung.extend((beschriftung(teilaufg,i, True) + r' \mathrm{Die~folgende~Abbildung~zeigt~die~Lösung.~(5P)}',
                        'Figure'))
        i += 1

    if 'j' in teilaufg:
        # Die SuS wird die Fläche eines Integrals gegeben, die der Graph mit der x-Achse einschließt und sollen daraus den Wert für a und damit die zugehörige Parameterfunktion bestimmen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        liste_punkte.append(punkte)

        # Aufstellen der Funktionsgleichung (a festlegen und dann A berechnen)
        fkt = collect(expand(faktor * (x - faktor_1 * a) * (x - faktor_2 * a) * (x - faktor_3 * a)), x)
        a_fest = zzahl(1,10)/2
        fkt_a = fkt.subs(a, a_fest)
        if faktor < 0:
            grenze_a = faktor_2
            grenze_b = faktor_3
        else:
            grenze_a = faktor_1
            grenze_b = faktor_2
        Fkt = integrate(fkt,x)
        flaeche = Fkt.subs(x, grenze_b*a) - Fkt.subs(x, grenze_a*a)
        flaeche_a = flaeche.subs(a, a_fest)
        flaeche_a_wert = N(flaeche_a,4)
        Fkt_grenze_b = Fkt.subs(x,grenze_b*a)
        Fkt_grenze_b_wert = N(Fkt_grenze_b.subs(a,1),4)
        Fkt_grenze_a = Fkt.subs(x,grenze_a*a)
        Fkt_grenze_a_wert = N(Fkt_grenze_a.subs(a,1),4)
        integral = Fkt_grenze_b - Fkt_grenze_a
        integral_wert = N(Fkt_grenze_b.subs(a,1)-Fkt_grenze_a.subs(a,1),3)
        wert_integr = integral.subs(a, a_fest)
        # Koeffizienten der Funktion
        fkt_a3 = faktor
        fkt_a2 = -1 * faktor * (faktor_1 + faktor_2 + faktor_3)
        fkt_a1 = faktor * (faktor_1 * faktor_2 + faktor_2 * faktor_3 + faktor_1 * faktor_3)
        fkt_a0 = -1 * faktor * faktor_1 * faktor_2 * faktor_3
        Fkt_a3_a = Rational(fkt_a3,4)
        Fkt_a2_a = Rational(fkt_a2*a_fest,3)
        Fkt_a1_a = Rational(fkt_a1*a_fest**2,2)
        Fkt_a0_a = fkt_a0 * a_fest**3

        fkt_str = (vorz_v_aussen(fkt_a3, r'x^3') + vorz_v_innen(fkt_a2, r'a \cdot x^2')
                   + vorz_v_innen(fkt_a1, r'a^2 \cdot x') + vorz_v_innen(fkt_a0, r'a^3'))
        Fkt_str = (vorz_v_aussen(Rational(fkt_a3,4), r'x^4')
                   + vorz_v_innen(Rational(fkt_a2,3), r'a \cdot x^3')
                   + vorz_v_innen(Rational(fkt_a1,2), r'a^2 \cdot x^2')
                   + vorz_v_innen(fkt_a0, r'a^3 \cdot x'))
        aufgabe.extend(('Der Graph schließt oberhalb der x-Achse eine Fläche mit der x-Achse ein. \n\n',
                        beschriftung(teilaufg,i) + f'Berechnen Sie den Wert für a, wenn '
                       + f'diese Fläche A = {gzahl(flaeche_a_wert)} FE beträgt. \n\n'))
        loesung.append(beschriftung(teilaufg,i, True) + r' A ~=~ \left| \int_{' + gzahl(grenze_a)
                       + 'a' + '}^{' + gzahl(grenze_b) + 'a' + '} ' + fkt_str + r' \,dx \right| ~=~ \left| \left[ '
                       + Fkt_str + r' \right]_{' + gzahl(grenze_a) + 'a' + '}^{' + gzahl(grenze_b)+ 'a'
                       + r'} \right| \quad (2BE) \\ ~=~  \left| (' + latex(Fkt_grenze_b_wert) + 'a^4)-('
                       + latex(Fkt_grenze_a_wert) + r'a^4) \right| \quad \to \quad '
                       + gzahl(flaeche_a_wert) + '~=~' + latex(integral_wert)
                       + r'a^4 \quad \vert \div ' + gzahl(integral_wert) + r' \quad \vert \sqrt[4]{~}'
                       + r' \\ \quad \to \quad \bm{a ~=~' + gzahl(N((flaeche_a/integral_wert)**(1/4),4))
                       + r'} \quad (3BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def kurvendiskussion_exponentialfkt(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ableitung=None, expfkt=2, verschiebung=True, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS eine Kurvendiskussion einer Exponentialfunktion durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'ableitungen=' kann Teilaufgabe c) festgelegt werden. Standardmäßig ist 'ableitung=None' und die SuS müssen in Teilaufgabe c) die Ableitungen berechnen. Ist 'ableitungen=True' sind die Ableitungen gegeben und die SuS müssen die Zwischenschritte angeben.
    # Mit dem Parameter 'expfkt=' kann die Art der Exponentialfunktion ausgewählt werden. Bei 'expfkt=1' hat die Funktion die Form ax^2*exp(bx+2)+c und bei 'expfkt=2' die Form (x+a)*exp(b*x). Standardmäßig ist 'expfkt=None' festgelegt und die Funktion wird zufällig ausgewählt.
    # Mit dem Parameter 'verschiebung=' kann die Verschiebung der ersten Exponentialfunktion (ax^2*exp(bx+2)+c) auf der y-Achse festgelegt werden. Standardmäßig ist die 'verschiebung=True' und die Funktion ist auf der y-Achse verschoben bzw. besitzt die Gleichung eine Konstante. Wird 'verschiebung=None' gesetzt, besitzt die e-Funktion keine Konstante.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden (z.B. liste_punkte=[1,2,3]). Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    expfkt = random.choice([1, 2]) if expfkt not in ([1,2]) else expfkt
    if expfkt == 1:
        extrema_xwert = zzahl(1,3)
        extrema_ywert = zzahl(1,3)
        if verschiebung == True:
            if extrema_xwert > 0:
                y_vers = -1*nzahl(1,3)
            else:
                y_vers = nzahl(1,3)
        else:
            y_vers = 0

        # print(extrema_xwert), # print(extrema_ywert), # print(y_vers)
        # rekonstruktion der exponentialfunktion
        fkt_v = exp(d*x+2)*a*x**2
        fkt_a1 = diff(fkt_v,x)
        gleichung1 = Eq(fkt_v.subs(x,extrema_xwert),extrema_ywert)
        gleichung2 = Eq(fkt_a1.subs(x,extrema_xwert),0)
        lsg = solve((gleichung1,gleichung2),(a,d))
        lsg_a = lsg[0][0]
        lsg_b = lsg[0][1]
        # print(lsg)
        fkt = exp(lsg_b*x+2)*lsg_a*x**2 + y_vers
        fkt_str = (vorz_v_aussen(lsg_a,'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b,'x+2') + '}'
                   + vorz_str(y_vers))

        # Ableitung der Funktionen
        fkt_1 = diff(fkt,x)
        fkt_2 = diff(fkt, x,2)
        fkt_3 = diff(fkt, x,3)

        fkt_1_str_zw = (r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot' + gzahl_klammer(lsg_b) + r' \cdot ('
                         + vorz_v_aussen(lsg_a,'x^2') + r') + e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot ('
                         + vorz_v_aussen(2*lsg_a,'x')) + ')'
        fkt_2_str_zw = (gzahl(lsg_b) + r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \left('
                         + vorz_v_aussen(lsg_a*lsg_b,'x^2') + vorz_v_innen(2*lsg_a,'x') + r' \right) + e^{'
                         + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \left(' + vorz_v_aussen(2*lsg_a * lsg_b, 'x')
                         + vorz_str(2*lsg_a) + r' \right)')
        fkt_3_str_zw = (gzahl(lsg_b) + 'e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \left('
                         + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                         + vorz_str(2*lsg_a) + r' \right)' + ' + e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \left('
                         + vorz_v_aussen(2*lsg_a * lsg_b**2, 'x') + vorz_v_innen(4 * lsg_a*lsg_b, r' \right)'))


        fkt_1_str = (r'e^{' + vorz_v_aussen(lsg_b,'x+2') + r'} \cdot \left(' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                      + vorz_v_innen(2*lsg_a,'x' + r' \right)'))
        fkt_2_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \left('
                      + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2') + vorz_v_innen(4 * lsg_a*lsg_b, 'x')
                      + vorz_str(2*lsg_a) + r' \right)')
        fkt_3_str = ('e^{' + vorz_v_aussen(lsg_b, 'x+2') + r'} \cdot \left('
                      + vorz_v_aussen(lsg_a * lsg_b**3, 'x^2') + vorz_v_innen(6 * lsg_a * lsg_b**2, 'x')
                      + vorz_str(6*lsg_a*lsg_b) + r' \right)')
    else:
        b = zzahl(2, 5)
        extrema_xwert = nzahl(1, 4)
        nst = extrema_xwert + nzahl(1, 3)
        c = -1 * nst * b
        fkt_v = (b * x + c) * exp(a * x)
        fkt_a1 = diff(fkt_v, x)
        gleichung2 = Eq(fkt_a1.subs(x, extrema_xwert), 0)
        lsg = solve(fkt_a1.subs(x, extrema_xwert), a)
        fkt = (b * x + c) * exp(lsg[0] * x)
        fkt_str = '(' + vorz_v_aussen(b,'x') + vorz_str(c) + r') \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'}'
        fkt_1 = diff(fkt, x)
        fkt_2 = diff(fkt, x, 2)
        fkt_3 = diff(fkt, x, 3)

        fkt_1_str_zw = (gzahl(b) + r' \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} + \left(' + vorz_v_aussen(b,'x')
                        + vorz_str(c) + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} \cdot '
                        + gzahl_klammer(lsg[0]))
        fkt_1_str = (r' \left(' + vorz_v_aussen(lsg[0]*b,'x') + vorz_str(lsg[0]*c+b)
                     + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'}')
        fkt_2_str_zw = (gzahl(lsg[0]*b) + r' \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} + '
                        + r' \left(' + vorz_v_aussen(lsg[0]*b,'x') + vorz_str(lsg[0]*c+b)
                        + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} \cdot '
                        + gzahl_klammer(lsg[0]))
        fkt_2_str = (r' \left(' + vorz_v_aussen(lsg[0]**2*b,'x') + vorz_str(lsg[0]**2*c+2*lsg[0]*b)
                     + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'}')
        fkt_3_str_zw = (gzahl(lsg[0]**2*b) + r' \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} + '
                        + r' \left(' + vorz_v_aussen(lsg[0]**2*b,'x') + vorz_str(lsg[0]**2*c+2*lsg[0]*b)
                        + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'} \cdot '
                        + gzahl_klammer(lsg[0]))
        fkt_3_str = (r' \left(' + vorz_v_aussen(lsg[0]**3*b,'x') + vorz_str(lsg[0]**3*c+3*lsg[0]**2*b)
                     + r' \right) \cdot e^{' + vorz_v_aussen(lsg[0],'x') + r'}')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if len([element for element in ['a', 'e'] if element in teilaufg]) > 0:
        # Hier sollen die SuS das Verhalten der Funktion im Unendlichen untersuchen.

        punkte_aufg = 2
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        grenzwert_neg = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)
        # print(grenzwert_min), # print(grenzwert_pos)

        aufgabe.append(beschriftung(teilaufg,i) + f'Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + latex(grenzwert_neg) + r' \quad (2BE) ')
        liste_punkte.append(punkte_aufg)
        i += 1
    if 'b' in teilaufg:
        # In dieser Aufgabe sollen die SuS die Schnittpunkte mit den Achsen (immer bei x=0) berechnen. Ist der Parameter 'verschiebung=True' sollen die SuS nur den Schnittpunkt mit der y-Achse berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if expfkt == 1:
            if y_vers == 0:
                punkte_aufg = 4
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Schnittpunkte der'
                               + f' Funktion f mit den Achsen. \n\n')
                loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                               + r' \hspace{20em} \\ \mathrm{Ansatz:~f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                               + r' \quad da~e^{' + vorz_v_aussen(lsg[0][1],'x+2') + r'} ~immer~ \neq 0'
                               + r' \quad \to \quad ' + (vorz_v_innen(lsg[0][0],'x^2'))
                               + r'~=~ 0} \quad \vert \div ' + gzahl_klammer(lsg[0][0]) + r' \quad \vert \sqrt{~} \\'
                               + r' x~=~0 \quad \to \quad S_y ~=~ S_x (0 \vert 0) \quad (4BE) ')
            else:
                punkte_aufg = 2
                aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie den Schnittpunkt der'
                                                        f' Funktion f mit der y-Achse. \n\n')
                loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Schnittpunkt~mit~der~y-Achse:}'
                               + r' \hspace{5em} \\ \mathrm{Ansatz:~f(0)~=~ ' + gzahl(y_vers)
                               + r' \quad \to \quad S_y (0 \vert ' + gzahl(y_vers) + r')} \quad (2BE) \\'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        if expfkt == 2:
            punkte_aufg = 6
            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Schnittpunkte der'
                                                    f' Funktion f mit den Achsen. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                           + r' \hspace{5em} f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                           + r' \quad (1BE) \\ \mathrm{ da~e^{' + vorz_v_aussen(lsg[0], 'x') + r'} ~immer~ \neq 0 }'
                           + r' \quad \to \quad 0 ~=~' + vorz_v_aussen(b, 'x') + vorz_str(c)
                           + r' \quad \vert ' + vorz_str(-1*c) + r' \quad \vert \div ' + gzahl_klammer(b)
                           + r' \quad \to \quad ' + r' x ~=~' + gzahl(Rational(-1*c,b)) + r' \quad \to \quad S_x ( '
                           + gzahl(Rational(-1*c,b)) + r' \vert 0) \quad (4BE) \\ '
                           + r' \mathrm{Schnittpunkt~mit~der~y-Achse:} \hspace{5em} '
                           + r' f(0) = e^0 \cdot (0' + vorz_str(c) + r') \quad \to \quad S_y( 0 \vert '
                           + gzahl(c) + r') \quad (1BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')

        liste_punkte.append(punkte_aufg)
        i += 1
    if len([element for element in ['c', 'd', 'f'] if element in teilaufg]) > 0:
        # Hier sollen die SuS, abhängig vom Parameter 'ableitung=', die drei Ableitungen bzw. die Zwischenschritte der drei gegebenen Ableitungen berechnen.

        if ableitung == None:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \\ \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \\ \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
            i += 1
        else:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            aufgabe.extend((beschriftung(teilaufg,i) + f'Geben Sie den Zwischenschritt bei der Berechnung '
                           + f'der folgenden Ableitungen an.', r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str + r' \\'))
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str_zw + '~=~' + fkt_1_str
                           + r' \\ \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str_zw + '~=~' + fkt_2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str_zw + '~=~' + fkt_3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
            i += 1
    if len([element for element in ['d', 'e'] if element in teilaufg]) > 0:
        # Hier sollen die SuS die Extrempunkte und deren Art mithilfe des hinreichenden Kriteriums berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extrema der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        if expfkt == 1:
            punkte_aufg = 10
            if fkt_2.subs(x,0) < 0:
                lsg_extrema1 = r'~<~0~ \to HP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2BE)'
            elif fkt_2.subs(x,0) > 0:
                lsg_extrema1 = r'~>~0~ \to TP(~0~ \vert ~' + gzahl(N(fkt.subs(x, 0), 3)) + r') \quad (2BE)'
            else:
                lsg_extrema1 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'

            if fkt_2.subs(x,-2/lsg_b) < 0:
                lsg_extrema2 = (r'~<~0~ \to HP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                                + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2BE)')
            elif fkt_2.subs(x,-2/lsg_b) > 0:
                lsg_extrema2 = (r'~>~0~ \to TP(~' + gzahl(-2/lsg_b) + r'~ \vert ~'
                                + gzahl(N(fkt.subs(x, -2/lsg_b), 3)) + r') \quad (2BE)')
            else:
                lsg_extrema2 = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium}'

            loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime }(x) ~=~'
                           + fkt_1_str + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                           + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a*lsg_b,'x^2')
                           + vorz_v_innen(2*lsg_a,'x') + r' \quad (3BE) \\'
                           + r' 0~=~x \cdot \left(' + vorz_v_aussen(lsg_a*lsg_b,'x')
                           + vorz_str(2*lsg_a) + r' \right)'
                           + r' \quad \to \quad x_1~=~0 \quad \mathrm{und} \quad 0~=~ '
                           + vorz_v_aussen(lsg_a*lsg_b,'x') + vorz_str(2*lsg_a) + r' \quad \vert \div '
                           + gzahl_klammer(lsg_a*lsg_b) + r' \quad \to \quad 0~=~x' + vorz_str(2/lsg_b)
                           + r' \quad \to \quad x_2~=~' + gzahl(-2/lsg_b) + r' \quad (3BE) \\'
                           + r' f^{ \prime \prime }(0) ~=~ ' + gzahl(N(fkt_2.subs(x,0),2)) + lsg_extrema1
                           + r' \quad \mathrm{und} \quad f^{ \prime \prime }(' + gzahl(-2/lsg_b) + ') ~=~ '
                           + gzahl(N(fkt_2.subs(x,-2/lsg_b),2)) + lsg_extrema2 + r' \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        elif expfkt == 2:
            punkte_aufg = 7
            xwert_extr = Rational(-1*(lsg[0]*c+b), lsg[0]*b)
            if fkt_2.subs(x, xwert_extr) < 0:
                lsg_extrema = (r'~<~0~ \to HP(~' + gzahl(N(xwert_extr, 3)) + r'~ \vert ~'
                               + gzahl(N(fkt.subs(x, xwert_extr), 3)))
            elif fkt_2.subs(x, xwert_extr) > 0:
                lsg_extrema = (r'~>~0~ \to TP(~ ' + gzahl(N(xwert_extr, 3)) + r' ~ \vert ~'
                               + gzahl(N(fkt.subs(x, xwert_extr), 3)))
            else:
                lsg_extrema = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium} \\'

            loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime }(x) ~=~'
                           + fkt_1_str + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg[0],'x')
                           + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg[0]*b,'x') + vorz_str(lsg[0]*c+b)
                           + r' \quad \vert ' + vorz_str(-1*(lsg[0]*c+b)) + r' \quad \vert \div '
                           + gzahl_klammer(lsg[0]*b) + r' \quad (3BE) \\ x~=~ ' + gzahl(N(xwert_extr, 3))
                           + r' \quad \to \quad f^{ \prime \prime }(' + gzahl(N(xwert_extr, 3)) + ') ~=~ '
                           + r' \left(' + gzahl(lsg[0] ** 2 * b) + r' \cdot ' + gzahl(N(xwert_extr, 3))
                           + vorz_str(lsg[0] ** 2 * c + 2 * lsg[0] * b) + r' \right) \cdot e^{' + gzahl(lsg[0])
                           + r' \cdot' + gzahl(N(xwert_extr, 3)) + r'} ~=~'
                           + gzahl(N(fkt_2.subs(x,xwert_extr),3)) + lsg_extrema + r') \quad (4BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        liste_punkte.append(punkte_aufg)
        i += 1
    if 'e' in teilaufg:
        # Hier sollen die SuS mithilfe der bisherigen Ergebnisse und ohne Rechnung begründen, dass die Funktion mind. einen Wendepunkte besitzt.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if expfkt == 1:
            punkte = 4

            xwert_wp1 = -2 / lsg_b - sqrt(2) / abs(lsg_b)
            xwert_wp2 = -2/lsg_b + sqrt(2)/abs(lsg_b)
            aufgabe.append(beschriftung(teilaufg,i) + 'Begründen Sie ohne Rechnung, '
                                                    'dass diese Funktion zwei Wendepunkte besitzt. \n\n')
            table1 = Tabular('p{0.2cm}p{13cm} p{2cm}')
            table1.add_row(beschriftung(teilaufg,i), 'mögliche Begründung', 'Punkte')
            table1.add_row('', f'Da die Funktion zwei Extrema hat, besitzt sie dazwischen einen Wendepunkt.', '2P')
            table1.add_row('', f'Einen weiteren Wendepunkt besitzt die Funktion, nach dem Extrema, wenn '
                               f'sich der Graph der Asymptote nähert.', '2P')
            loesung.append(table1)
            loesung.append(' \n')
        if expfkt == 2:
            punkte = 3
            aufgabe.append(beschriftung(teilaufg,i) + 'Begründen Sie ohne Rechnung,'
                                                    'dass diese Funktion einen Wendepunkte besitzt. \n\n')
            table1 = Tabular('p{0.2cm}p{13cm} p{2cm}')
            table1.add_row(beschriftung(teilaufg,i), 'mögliche Begründung', 'Punkte')
            if grenzwert_neg == 0:
                table1.add_row('',NoEscape('Da die Funktion ein Extrema hat und '
                                           r'$ \lim\limits_{x \to - \infty} = 0 $ ist, '
                                           r'muss dazwischen eine Wendestelle existieren.'),'(3BE)')
            if grenzwert_pos == 0:
                table1.add_row('',NoEscape('Da die Funktion ein Extrema hat und '
                                           r'$ \lim\limits_{x \to \infty} = 0 $ ist, '
                                           r'muss dazwischen eine Wendestelle existieren.'),'(3BE)')
            loesung.append(table1)
            loesung.append(' \n')
        liste_punkte.append(punkte)
        i += 1
    if len([element for element in ['f', 'g'] if element in teilaufg]) > 0:
        # Hier sollen die SuS die Wendepunkte berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if expfkt == 1:
            punkte_aufg = 10
            xwert_wp1 = -2 / lsg_b - sqrt(2) / abs(lsg_b)
            xwert_wp2 = -2/lsg_b + sqrt(2)/abs(lsg_b)
            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Wendepunkte der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg_b,'x+2')
                           + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(lsg_a * lsg_b**2, 'x^2')
                           + vorz_v_innen(4 * lsg_a*lsg_b, 'x') + vorz_str(2*lsg_a) + r' \quad \vert \div '
                           + gzahl_klammer(lsg_a*lsg_b**2) + r' \quad (3BE) \\'
                           + r' 0 ~=~ x^2 ' + vorz_v_innen(4/lsg_b, 'x') + vorz_str(2/lsg_b**2)
                           + r' \quad \to \quad x_{1/2} ~=~  - \frac{' + gzahl_klammer(4/lsg_b)
                           + r'}{2} \pm \sqrt{ \left( \frac{' + gzahl_klammer(4/lsg_b) + r'}{2} \right)^2'
                           + vorz_str(-2/lsg_b**2) + r'} ~=~ ' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(abs(sqrt(2)/lsg_b))
                           + '~=~' + gzahl(-2/lsg_b) + r' \pm ' + gzahl(N(abs(sqrt(2)/lsg_b),3)) + r' \quad (2BE) \\'
                           + r' x_1 ~=~ ' + gzahl(N(xwert_wp1,3)) + r' \quad \mathrm{und} \quad x_2 ~=~'
                           + gzahl(N(xwert_wp2,3)) + r' \quad (1BE) \\'
                           + r' f^{ \prime \prime \prime }(' + gzahl(N(xwert_wp1,3)) + ') ~=~ '
                           + gzahl(N(fkt_3.subs(x,xwert_wp1),3)) + r' \neq 0 \quad \to \quad WP(~'
                           + gzahl(N(xwert_wp1,3)) + r'~ \vert ~ '
                           + gzahl(N(fkt.subs(x,xwert_wp1),3))
                           + r') \quad (2BE) \\ f^{ \prime \prime \prime }('
                           + gzahl(N(xwert_wp2,3)) + ') ~=~ '
                           + gzahl(N(fkt_3.subs(x,xwert_wp2),3)) + r' \neq 0 \quad \to \quad WP(~'
                           + gzahl(N(xwert_wp2,2)) + r'~ \vert ~ '
                           + gzahl(N(fkt.subs(x, xwert_wp2),2)) + r') \quad (2BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        if expfkt == 2:
            punkte_aufg = 7
            xwert_w = Rational(-1*(lsg[0]*c+2*b),lsg[0]*b)
            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie den Wendepunkt der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(lsg[0],'x')
                           + r'} \neq 0 \quad \to \quad 0~=~ ' + vorz_v_aussen(lsg[0]**2*b,'x')
                           + vorz_str(lsg[0]**2*c+2*lsg[0]*b) + r' \quad \vert ' + vorz_str(-1*(lsg[0]**2*c+2*lsg[0]*b))
                           + r' \quad \vert \div ' + gzahl_klammer(lsg[0]**2*b) + r' \quad (4BE) \\ x~=~'
                           + gzahl_klammer(N(xwert_w,3)) + r' \quad \to \quad f^{ \prime \prime \prime }('
                           + gzahl(N(xwert_w, 3)) + r') ~=~ \left(' + gzahl(lsg[0]**3*b) + r' \cdot '
                           + gzahl(N(xwert_w, 3)) + vorz_str(lsg[0]**3*c+3*lsg[0]**2*b) + r' \right) \cdot e^{'
                           + gzahl(lsg[0]) + r' \cdot '+ gzahl(N(xwert_w, 3)) + r'} ~=~'
                           + gzahl(N(fkt_3.subs(x, xwert_w), 3)) + r' \neq 0 \quad \to \quad WP(~'
                           + gzahl(N(xwert_w, 3)) + r'~ \vert ~ ' + gzahl(N(fkt.subs(x, xwert_w), 3))
                           + r') \quad (3BE) \\' + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        liste_punkte.append(punkte_aufg)
        i += 1
    if 'g' in teilaufg:
        # In dieser Aufgabe sollen die SuS die Tangente und Normale am Wendepunkt berechnen. Zur Kontrolle ist der Wendepunkt gegeben.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if expfkt == 1:
            punkte_aufg = 6
            xwert_wp1 = N(-2/lsg_b - sqrt(2)/abs(lsg_b), 3)
            ywert_wp1 = N(fkt.subs(x,-2/lsg_b - sqrt(2)/abs(lsg_b)), 3)
            ywert_wp1 = N(fkt.subs(x, xwert_wp1),3)
            ywert_wp1_fkt_1 = N(fkt_1.subs(x, xwert_wp1),3)

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Tangente und Normale am Wendepunkt '
                           + f'WP({xwert_wp1}|{ywert_wp1}). \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                           + r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(ywert_wp1_fkt_1)
                           + binom_klammer(1,-1 * N(xwert_wp1,3),str1='x') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(ywert_wp1_fkt_1,'x')
                           + vorz_str(N(-1*ywert_wp1_fkt_1*xwert_wp1 + ywert_wp1,3))
                           + r' \quad (3BE) \\ n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                           r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(-1/ywert_wp1_fkt_1)
                           + binom_klammer(1,-1 * N(xwert_wp1,3),str1='x') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(-1/ywert_wp1_fkt_1,'x')
                           + vorz_str(N(xwert_wp1/ywert_wp1_fkt_1 + ywert_wp1,3))
                           + r' \quad (3BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        if expfkt == 2:
            punkte_aufg = 6
            xwert_w = Rational(-1*(lsg[0]*c+2*b),lsg[0]*b)
            ywert_w = N(fkt.subs(x, xwert_w), 3)
            ywert_w_fkt_1 = N(fkt_1.subs(x, xwert_w),3)
            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Tangente und Normale am Wendepunkt '
                           + f'WP({gzahl(N(xwert_w,3))}|{gzahl(ywert_w)}). \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' t(x)~=~ f^{ \prime }(x_{w}) \cdot '
                           + r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(ywert_w_fkt_1)
                           + binom_klammer(1, -1 * N(xwert_w,3),str1='x') + vorz_str(ywert_w) + '~=~'
                           + vorz_v_aussen(ywert_w_fkt_1,'x')
                           + vorz_str(N(-1*ywert_w_fkt_1*xwert_w + ywert_w,3))
                           + r' \quad (3BE) \\ n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                           r'(x - x_{w}) + y_{w} ~=~ ' + gzahl(-1/ywert_w_fkt_1)
                           + binom_klammer(1,-1 * N(xwert_w,3), 'x') + vorz_str(ywert_w) + '~=~'
                           + vorz_v_aussen(-1/ywert_w_fkt_1,'x')
                           + vorz_str(N(xwert_w/ywert_w_fkt_1 + ywert_w,3))
                           + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')

        liste_punkte.append(punkte_aufg)
        i += 1
    if 'h' in teilaufg:
        # Hier sollen die SuS den Graphen der Funktion zeichnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if expfkt == 1:
            # Werte für Angaben zum Zeichnen des Graphen
            ywerte = [(element, fkt.subs(x, element)) for element in range(-5, 6)]
            wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
            xmin = wertebereich[0]
            xmax = wertebereich[-1]
        if expfkt == 2:
            ywerte = [(element, fkt.subs(x, element)) for element in range(-20, 20)]
            k = 0
            wertebereich = []
            for zahl in range(len(ywerte) - 1):
                if abs(ywerte[k][1]) < 6 and abs(ywerte[k][1] - ywerte[k + 1][1]) > 0.5:
                    wertebereich.append(ywerte[k][0])
                k += 1
            xmin = wertebereich[0]
            xmax = wertebereich[-1]

        punkte_aufg = 5
        grafiken_loesung.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        Graph(xmin, xmax, fkt, name=f'Aufgabe_{nr}{liste_teilaufg[i]}.png')
        aufgabe.append(beschriftung(teilaufg,i) + f'Zeichnen Sie den Graphen im Intervall I [{xmin}|{xmax}]. \n\n')
        loesung.extend((beschriftung(teilaufg, i, True)
                        + r' \mathrm{Punkte~für~Koordinatensystem~2P,~Werte~2P,~Graph~1P} \\', 'Figure'))
        liste_punkte.append(punkte_aufg)

        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def kurvendiskussion_exponentialfkt_parameter(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ableitung=None, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS eine Kurvendiskussion einer Exponentialfunktion mit einem Parameter durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter 'ableitungen=' kann Teilaufgabe c) festgelegt werden. Standardmäßig ist 'ableitung=None' und die SuS müssen in Teilaufgabe c) die Ableitungen berechnen. Ist 'ableitungen=True' sind die Ableitungen gegeben und die SuS müssen die Zwischenschritte angeben.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden (z.B. liste_punkte=[1,2,3]). Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    c = random.choice([Rational(zzahl(1, 10), 5), Rational(zzahl(1, 8), 4)])
    n1 = Rational(random.choice([2, 4, 5, 6, 8, 10]), 2)
    a = n1 * c
    n2 = Rational(random.choice([2, 4, 5, 6, 8, 10]), 2)
    n3 = Rational(random.choice([2, 4, 5, 6, 8, 10]), 2)
    b_h = -1 * a * n2
    b_ij = -1 * a * n3
    xe = -1 / c - b / a
    ywert_xe_bij = -a/c*exp(-b_ij*c/a-1)

    while (100/a) % 1 != 0 and (100/c) % 1 != 0 and (10*xe)%1 != 0 and abs(ywert_xe_bij) < 1:
        c = random.choice([Rational(zzahl(1, 10), 5), Rational(zzahl(1,8),4)])
        n1 = Rational(random.choice([2, 4, 5, 6, 8, 10]),2)
        a = n1 * c
        n2 = Rational(random.choice([2, 4, 5, 6, 8, 10]), 2)
        n3 = Rational(random.choice([2, 4, 5, 6, 8, 10]), 2)
        b_h = -1 * a * n2
        b_ij = -1 * a * n3
        xe = -1 / c - b / a
        ywert_xe_bij = -a / c * exp(-b_ij * c / a - 1)

    fkt_b = (a * (x - n3)) * exp(c * x)
    fkt_str = '(' + vorz_v_aussen(a, r'x + b ) \cdot e^{' + vorz_v_aussen(c,'x') + r'}')
    fkt_1_str_zw = (gzahl(a) + r' \cdot e^{' + vorz_v_aussen(c,'x') + r'} + ('
                    + vorz_v_aussen(a, r'x + b) \cdot e^{' + vorz_v_aussen(c,'x') + r'}')
                    + r' \cdot ' + gzahl_klammer(c))
    fkt_1_str = (r' \left( ' + vorz_v_aussen( a * c ,r'x') + vorz_str(a) + vorz_v_innen(c, r'~ b \right) \cdot e^{'
                 + vorz_v_aussen(c,'x') + r'}'))
    fkt_2_str_zw = (gzahl(a * c) + r' \cdot e^{' + vorz_v_aussen(c,'x') + r'} + \left( '
                    + vorz_v_aussen(a * c,r'x') + vorz_str(a) + vorz_v_innen(c, r'~ b \right) \cdot e^{'
                    + vorz_v_aussen(c,'x') + r'}') + r' \cdot ' + gzahl_klammer(c))
    fkt_2_str = (r' \left( ' + vorz_v_aussen( a * c**2 ,r'x') + vorz_str(2*a*c)
                 + vorz_v_innen(c**2, r'~ b \right) \cdot e^{' + vorz_v_aussen(c,'x') + r'}'))
    fkt_3_str_zw = (gzahl(a * c**2) + r' \cdot e^{' + vorz_v_aussen(c,'x') + r'} + \left( '
                    + vorz_v_aussen(a * c**2,r'x') + vorz_str(2*a*c)
                    + vorz_v_innen(c**2, r'~ b \right) \cdot e^{' + vorz_v_aussen(c,'x') + r'}')
                    + r' \cdot ' + gzahl_klammer(c))
    fkt_3_str = (r' \left( ' + vorz_v_aussen( a * c**3 ,r'x') + vorz_str(3*a*c**2)
                 + vorz_v_innen(c**3, r'~ b \right) \cdot e^{' + vorz_v_aussen(c,'x') + r'}'))


    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS das Verhalten der Funktion im Unendlichen untersuchen.

        punkte_aufg = 2
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        grenzwert_neg = limit(fkt_b, x, -oo)
        grenzwert_pos = limit(fkt_b, x, oo)
        # print(grenzwert_min), # print(grenzwert_pos)

        aufgabe.append(beschriftung(teilaufg,i) + f'Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + latex(grenzwert_neg) + r' \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        liste_punkte.append(punkte_aufg)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Funktion auf Symmetrie untersuchen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        fkt_sym = fkt_b.subs(x, -x)
        fkt_sym_str = '(' + vorz_v_aussen(-1*a, r'x + b ) \cdot e^{' + vorz_v_aussen(-1*c,'x') + r'}')
        if fkt_sym == fkt_b:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                   + r'~=~f(x) \\ \to \quad \mathbf{Achsensymmetrie} \quad (3BE) \\')
        elif fkt_sym == -1 * fkt_b:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str
                   + r'~=~-f(x) \\ \to \quad \mathbf{Punktsymmetrie} \quad (3BE) \\')
        else:
            lsg = (r') \quad f(-x)~=~' + fkt_sym_str + r' \neq  f(x)  \neq -f(x) \\ \to \quad '
                                                       r' \mathbf{nicht~symmetrisch} \quad (3BE) \\')
        aufgabe.append(beschriftung(teilaufg,i) + f'Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # In dieser Aufgabe sollen die SuS die Schnittpunkte mit den Achsen (immer bei x=0) berechnen, wenn der Parameter 'verschiebung=False' ist. Ist der Parameter 'verschiebung=True' sollen die SuS nur den Schnittpunkt mit der y-Achse berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 6
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Schnittpunkte der'
                       + f' Parameterfunktion f mit den Achsen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Schnittpunkt~mit~der~x-Achse:}'
                       + r' \hspace{5em} f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                       + r' \quad (1BE) \\ \mathrm{ da~e^{' + vorz_v_aussen(c, 'x') + r'} ~immer~ \neq 0 }'
                       + r' \quad \to \quad 0 ~=~' + vorz_v_aussen(a, 'x + b') + r' \quad \vert ~ -b'
                       + r' \quad \vert \div ' + gzahl_klammer(a) + r' \quad \to \quad x ~=~ '
                       + vorz_v_innen(Rational(-1,a),'b') + r' \quad \to \quad S_x ( '
                       + vorz_v_innen(Rational(-1,a),'b') + r' \vert 0) \quad (4BE) \\ '
                       + r' \mathrm{Schnittpunkt~mit~der~y-Achse:} \hspace{5em} '
                       + r' f(0) = e^0 \cdot (0 + b) \quad \to \quad S_y( 0 \vert b) \quad (1BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')

        liste_punkte.append(punkte_aufg)
        i += 1

    if len([element for element in ['d', 'e', 'f', 'g', 'h'] if element in teilaufg]) > 0:
        # Hier sollen die SuS, abhängig vom Parameter 'ableitung=', die drei Ableitungen bzw. die Zwischenschritte der drei gegebenen Ableitungen berechnen.

        if ableitung == None:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \\ \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \\ \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
            i += 1
        else:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            aufgabe.extend((beschriftung(teilaufg,i) + f'Geben Sie den Zwischenschritt bei der Berechnung '
                           + f'der folgenden Ableitungen an.', r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str + r' \\'))
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str_zw + '~=~'
                           + fkt_1_str + r' \\ \quad f^{ \prime \prime }(x) ~=~' + fkt_2_str_zw + '~=~' + fkt_2_str
                           + r' \\ f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str_zw + '~=~' + fkt_3_str  # passt sonst manchmal nicht aufs blatt
                           + r' \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
            i += 1

    if len([element for element in ['e', 'f', 'g', 'h'] if element in teilaufg]) > 0:
        # Hier sollen die SuS die Extrempunkte und deren Art mithilfe des hinreichenden Kriteriums berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Extrema der Parameterfunktion f und deren Art'
                       + ' mithilfe des hinreichenden Kriteriums. \n\n')
        punkte_aufg = 8

        if a*c < 0:
            lsg_extrema = (r'~<~0 \quad \to \quad HP \left( ~' + gzahl(-1/c) + vorz_v_innen(-1/a,'b')
                           + r' ~ \vert ~' + gzahl(-1*a/c)+ 'e^{' + vorz_str(-1*c/a) + r'b -1} \right)')
        elif a*c > 0:
            lsg_extrema = (r'~>~0 \quad \to \quad TP \left( ~' + gzahl(-1/c) + vorz_v_innen(-1/a,'b')
                           + r' ~ \vert ~' + gzahl(-1*a/c) + 'e^{' + vorz_str(-1*c/a) + r'b -1} \right) ')
        else:
            lsg_extrema = r' ~=~0 \to \mathrm{Vorzeichenwechselkriterium} \\'

        loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime }(x) ~=~'
                       + fkt_1_str + r' \quad (1BE) \\ \mathrm{da} ~ e^{' + vorz_v_aussen(c,'x')
                       + r'} \neq 0 \quad \to \quad 0~=~' + vorz_v_aussen(a * c,'x') + vorz_str(a)
                       + vorz_v_innen(c, 'b') + r' \quad \vert ' + vorz_str(-1*a) + vorz_str(-1*c)
                       + r'b \quad \vert \div ' + gzahl_klammer(a*c) + r' \quad \to \quad x_E~=~ '
                       + gzahl(-1/c) + vorz_v_innen(-1/a,'b') + r' \quad (3BE) \\ f^{ \prime \prime } \left( '
                       + gzahl(-1/c) + vorz_v_innen(-1/a,r'b') + r' \right) ~=~ \left( ' + gzahl(a*c**2)
                       + r' \cdot \left( ' + gzahl(-1/c) + vorz_v_innen(-1/a,'b') + r' \right) '
                       + vorz_str(2*a*c) + vorz_v_innen(c**2,'b') + r' \right) \cdot e^{' + gzahl(c)
                       + r' \cdot \left( ' + gzahl(-1/c) + vorz_str(-1/a) + r' \cdot b \right)} ~=~ '
                       + gzahl(a*c) + r' \cdot e^{' + vorz_str(-1*c/a) + r'b -1} \quad (2BE) \\ \mathrm{da~e^{'
                       + vorz_str(-1*c/a) + r'b -1} ~immer~ \neq 0 }' + r' \quad \to \quad '
                       + r' f^{ \prime \prime } \left( ' + gzahl(-1/c) + vorz_v_innen(-1/a,r'b') + r' \right)~=~'
                       + gzahl(a*c) + lsg_extrema + r' \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        liste_punkte.append(punkte_aufg)
        i += 1

    if 'f' in teilaufg:
        # Hier sollen die SuS beurteilen, welchen Einfluss der Faktor b auf die Extremstelle und dessen Art hat.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.append(beschriftung(teilaufg,i) + f'Erläutern Sie die Abhängigkeit der Extremwerte und deren Art '
                                                '(HP oder TP) von der Variablen b. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Der~Extremwert~ist~x_E ~=~' + gzahl(-1/c)
                       + vorz_v_innen(-1/a,'b') + r'~und~somit~von~b~abhängig.} \quad (2BE) \\'
                       + r' \mathrm{Da} \quad f^{ \prime \prime } (' + gzahl(-1/c)
                       + vorz_v_innen(-1/a, r'b') + ') ~=~ ' + gzahl(a*c)
                       + r' \quad \mathrm{nicht~von~b~abhängt,~ist~die~Art~des~Extrema~unabhängig~von~b.} \quad (2BE)'
                       + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        liste_punkte.append(punkte)
        i += 1

    if 'g' in teilaufg:
        # Die SuS sollen die Ortskurve der Extrema berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        liste_punkte.append(punkte)

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Ortskurve der Extrema. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' x ~=~' + gzahl(-1/c) + vorz_v_innen(-1/a,'b')
                       + r' \quad \vert ' + vorz_str(1/c) + r' \quad \vert \cdot ' + gzahl_klammer(-a)
                       + r' \quad \to \quad b~=~ ' + gzahl(-a) + r'x' + vorz_str(-a/c) + r' \quad (2BE) \\ '
                       + r' \mathrm{einsetzen~in~y} ~=~' + vorz_v_aussen(-a/c,'e^{' + vorz_str(-c/a) + r' \cdot \left('
                       + gzahl(-a) + r'x' + vorz_str(-a/c) + r' \right) -1 }') + ' ~=~ ' + vorz_v_aussen(-a/c,'e^{'
                       + vorz_v_aussen(c,'x') + '}') + r' \quad (2BE)'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'h' in teilaufg:
        # Die SuS sollen dem Wendepunkt der Funktion berechnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        liste_punkte.append(punkte)

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Wendepunkte der Parameterfunktion. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' 0 ~=~ f^{ \prime \prime }(x) ~=~ ' + fkt_2_str
                       + r' \quad \mathrm{da} ~ e^{' + vorz_v_aussen(c,'x') + r'} ~ \neq 0 \quad (1BE) \\ 0 ~=~'
                       + vorz_v_aussen( a * c**2 ,r'x') + vorz_str(2*a*c) + vorz_v_innen(c**2, r'b')
                       + r' \quad \vert ~' + vorz_str(-2*a*c) + vorz_v_innen(-1*c**2,'b') + r' \quad \vert \div '
                       + gzahl_klammer(a*c**2) + r' \quad \quad \to \quad x_{WP}~=~' + gzahl(-2/c)
                       + vorz_v_innen(-1/a,'b') + r' \quad (2BE) \\ f^{ \prime \prime \prime } \left( '
                       + gzahl(-2/c) + vorz_v_innen(-1/a,'b') + r' \right) ~=~  \left( '
                       + vorz_v_aussen( a * c**3 ,r' \left( ' + gzahl(-2/c) + vorz_v_innen(-1/a,'b') + r' \right) ')
                       + vorz_str(3*a*c**2) + vorz_v_innen(c**3, r'~ b \right)') + r' e^{'
                       + vorz_v_aussen(c,r' \left( ' + gzahl(-2/c) + vorz_v_innen(-1/a,'b') + r' \right) ') + r'}'
                       + r' (1BE) \\ \mathrm{da~e^{' + vorz_str(-c/a) + r'b -2} ~immer~ \neq 0 } \quad \to \quad '
                       + r'f^{ \prime \prime \prime } \left( ' + gzahl(-2/c) + vorz_v_innen(-1/a,'b')
                       + r' \right) ~=~' + gzahl(a*c**2)+ r' \quad \neq 0 \quad (2BE) \\ \mathbf{Wendepunkt} '
                       + r' \bm{ \left( ' + gzahl(-2/c) + vorz_v_innen(-1/a, 'b') + r' \vert '
                       + vorz_v_aussen(a*c**2, r' e^{' + vorz_v_aussen(-c/a,'b-2') + '}')
                       + r' \right) }  \quad (2BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'i' in teilaufg:
        # Die SuS sollen dem Wendepunkt der Funktion berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        wp_h = -2 / c - b_h / a
        wp_h = float(wp_h) if wp_h % 1 != 0 else wp_h
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie b, wenn die Parameterfunktion die Wendestelle bei '
                       + f' x = {gzahl(wp_h)} hat. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' x_E ~=~ ' + gzahl(-2/c)
                       + vorz_v_innen(-1/a,'b') + r' \quad \vert ' + vorz_str(2/c) + r' \quad \vert \cdot '
                       + gzahl(-1*a) + r' \quad \to \quad b~=~' + vorz_v_aussen(-a,'x_E') + vorz_str(-2*a/c)
                       + r' \quad (2BE) \\ b ~=~' + gzahl(-a) + r' \cdot ' + gzahl_klammer(wp_h) + vorz_str(-2*a/c)
                       + '~=~' + gzahl(b_h) + r' \quad (2BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        liste_punkte.append(punkte)
        i += 1

    if 'j' in teilaufg:
        # Die SuS sollen den Graphen für einen vorgegebenen Wert für b in einem festgelegten Intervall zeichnen.

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        punkte = 5
        b_ij = N(float(b_ij),3) if b_ij%1 !=0 else b_ij
        nst = - b_ij/a
        xe_bij = -1 / c - b_ij / a
        if limit(fkt_b, x, oo) == 0:
            ywerte = [(element, fkt_b.subs(x, element)) for element in range(int(xe_bij), int(xe_bij)+20)]
            wertetabelle = [ywerte[k][0] for k in range(len(ywerte)-1) if abs(ywerte[k+1][1] - ywerte[k][1]) < 0.1*abs(ywert_xe_bij)]
            xmax = wertetabelle[0]
            xmin = round(nst,1)
        else:
            ywerte = [(element, fkt_b.subs(x, element)) for element in range(int(xe_bij)-20, int(xe_bij))]
            wertetabelle = [ywerte[k][0] for k in range(len(ywerte) - 1) if abs(ywerte[k+1][1] - ywerte[k][1]) < 0.1*abs(ywert_xe_bij)]
            xmin = wertetabelle[-1]
            xmax = round(nst,1)

        Graph(xmin, xmax, fkt_b, name=f'Loesung_{nr}{liste_teilaufg[i]}')
        # plt.show()
        aufgabe.append(beschriftung(teilaufg,i) + f'Zeichnen Sie den Graphen für b = {gzahl(b_ij)} im '
                       + f'Intervall [ {xmin} | {xmax} ]. \n\n')
        loesung.extend((beschriftung(teilaufg, i, True)
                        + r' \mathrm{Die~folgende~Abbildung~zeigt~die~Lösung.~(5P)}', 'Figure'))
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der '
                  f'Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# in Entwicklung:
def kurvendiskussion_polynom_parameter_1(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], i=0, BE=[]):
    # Kurvendiskussion einer Polynom- und Parameterfunktion 1
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden (z.B. liste_punkte=[1,2,3]). Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

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
    fkt_a1_str = (vorz(faktor*(nst_1+nst_3)) + '(' + gzahl(abs(faktor * (nst_1 + nst_3))) + r'a'
                  + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
    fkt_a2_str = (vorz(-1 * faktor) + '(' + gzahl(abs(faktor)) + r'a '
                  + vorz_str(-1 * faktor * (nst_1 + nst_3)) + ')')
    fkt_a3_str = gzahl(faktor)

    fkt_a0_str = vorz_str(-1*faktor*nst_1*nst_3) + r' a'

    fkt_str = fkt_a3_str + r'x^3 ~' + fkt_a2_str + r' \cdot x^2 ~' + fkt_a1_str + r' \cdot x ~' + fkt_a0_str

    print(fkt), print(fkt_str)

    if nst_1 < 0:
        db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > 0}'
    else:
        db_bereich = r' \mathrm{mit~a \in \mathbb{R} ~und~ a > ' + gzahl(nst_1) + r'}'

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))),
               r' \mathrm{Gegeben~ist~die~Funktion \quad  f(x)~=~' + fkt_str + r' \quad ' + db_bereich + r'}']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Verhalten im Unendlichen untersuchen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        grenzwert_neg = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(beschriftung(teilaufg,i) + f'Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + gzahl(grenzwert_pos) + r' \\ \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + gzahl(grenzwert_neg) + r' \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'b' in teilaufg:
        # Symmetrie überprüfen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        liste_punkte.append(punkte)
        fkt_a1_str_neg = (vorz(-1*(nst_1 + nst_3)) + '(' + gzahl(abs(faktor * (nst_1 + nst_3))) + r' a'
                          + vorz_str(-1 * faktor * nst_1 * nst_3) + ')')
        fkt_a3_str_neg = gzahl(-1*faktor)
        fkt_sym = (fkt_a3_str_neg + 'x^3' + fkt_a2_str + 'x^2' + fkt_a1_str_neg
                   + 'x' + fkt_a0_str)
        aufgabe.append(beschriftung(teilaufg,i) + f'Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f(-x)~=~' + fkt_sym
                       + r' \neq  f(x)  \neq -f(x) \\ \mathrm{nicht~symmetrisch} \quad (3BE) \\')
        i += 1

    if 'c' in teilaufg:
        # Schnittpunkte mit den Achsen berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 15
        liste_punkte.append(punkte)
        # hier werden die Koeffizenten für das Hornerschema berechnet
        fkt_b2 = nst_1 * faktor
        fkt_c2 = -1 * faktor * a - faktor * nst_3
        fkt_b1 = -1 * faktor * nst_1 * a - faktor * nst_1 * nst_3
        fkt_c1 = faktor * nst_3 * a
        fkt_b0 = faktor * nst_1 * nst_3 * a
        fkt_partial = faktor * x**2 + fkt_c2 *x + fkt_c1

        # hier werden die Koeffizenten als String für das Hornerschema berechnet
        fkt_c2_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-1 * faktor, r' a')
                      + vorz_v_innen(-1 * faktor * nst_3,r') \cdot x'))
        fkt_c1_str = vorz_str(faktor*nst_3) + r' a'
        fkt_p = -1*a - nst_3    # -(a+x_3)
        fkt_q = nst_3 * a
        fkt_disk = ((fkt_p/2)**2)-fkt_q
        fkt_p_str = '-(a' + vorz_str(nst_3) + ')'
        fkt_q_str = vorz_str(nst_3) + r' a'
        fkt_partial_str = gzahl(faktor) + r' \cdot x^2' + fkt_c2_str + fkt_c1_str
        fkt_pq_str = 'x^2' + fkt_p_str + r' \cdot x' + fkt_q_str
        fkt_disk_str = r' \frac{a^2' + vorz_str(-1*2*nst_3) + r' a' + vorz_str(nst_3**2) + '}{4}'

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('',fkt_a3,latex(collect(fkt_a2,a)), latex(collect(fkt_a1,a)), latex(collect(fkt_a0,a)))
        table2.add_hline(2, 5)
        table2.add_row('Partialpolynom mit Horner Schema berechnen: ',' ',
                       latex(collect(fkt_b2,a)), latex(collect(fkt_b1,a)), latex(collect(fkt_b0,a)))
        table2.add_hline(2, 5)
        table2.add_row('',fkt_a3, latex(collect(fkt_c2,a)), latex(collect(fkt_c1,a)), ' 0')

        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie die Schnittpunkte mit den Achsen der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg, i, True) + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~'
                       + fkt_str + r' \quad (1BE) \\ \mathrm{durch~probieren:~x_1~=~}'
                       + vorz_str(nst_1) + r' \quad (1BE) \\ (' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1)
                       + r')~= \\ =~' + fkt_partial_str + r' \quad (4P)')
        loesung.append(table2)
        loesung.append(' 0~=~' + fkt_partial_str + r' \quad \vert ~ \div ' + gzahl_klammer(faktor) +
                       r' \quad \to \quad 0~=~' + fkt_pq_str + r' \quad (2BE) \\'
                       r' x_{2/3}~=~ - \frac{' + fkt_p_str + r'}{2} \pm \sqrt{ \left(' +
                       r' \frac{' + fkt_p_str + r'}{2} \right)^2-(' + latex(fkt_q) +
                       r')} ~=~ ' + gzahl(-1*fkt_p/2) + r' \pm \sqrt{'
                       + fkt_disk_str + r' } \quad (4BE) \\ x_{2/3}~=~' + gzahl(-1*fkt_p/2) + r' \pm ('
                       + gzahl((a-nst_3)/2) + r') \quad \to \quad x_2~=~' + gzahl(nst_3)
                       + r' \quad \mathrm{und} \quad x_3~=~a \quad (3BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'd' in teilaufg:
        # Extrema und deren Art berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 19
        liste_punkte.append(punkte)
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

        fkt_1_a2_str = gzahl(3*faktor)
        fkt_1_a1_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor,r' a')
                        + vorz_v_innen(-2 * faktor * (nst_1 + nst_3),')'))
        fkt_1_a0_str = (vorz(faktor * (nst_1 + nst_3)) + '('
                         + vorz_v_aussen(abs(faktor * (nst_1 + nst_3)), r' a')
                         + vorz_v_innen(-1 * faktor * nst_1 * nst_3, ')'))

        # p und q in der pq-Formel
        fkt_1_p_str = r'-( \frac{2}{3} a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')'
        fkt_1_q_str = (vorz(nst_1+nst_3) + '(' + vorz_v_aussen(Rational(-1 * (nst_1 + nst_3), 3), r' a')
                       + vorz_v_innen(Rational(-1 * (nst_1 * nst_3), 3),')'))
        fkt_1_q2_str = (vorz_v_aussen(Rational((nst_1 + nst_3), 3), r' a')
                        + vorz_str(Rational((nst_1 * nst_3), 3)))

        # p und q in umgeformter pq-Formel
        fkt_1_p2_str = r'( \frac{2}{3} a' + vorz_str(Rational(2 * (nst_1 + nst_3), 3)) + ')^2'
        fkt_1_p3_str = r' \frac{1}{3} a' + vorz_str(Rational((nst_1 + nst_3), 3))
        fkt_1_q3_str = (vorz(-1*(nst_1 + nst_3)) + r' \frac{4 \cdot ('
                        + vorz_v_aussen(Rational(abs(nst_1 + nst_3), 3), r' a')
                        + vorz_v_innen(Rational(-1 * (nst_1 * nst_3), 3), ') }{4}'))

        # Diskriminante der Wurzel
        fkt_1_disk_str = (r' \frac{1}{9} \cdot ((a' + vorz_str(-1*(nst_1+nst_3)) + r')^2'
                          + vorz_str(-4*nst_1*nst_3) + ')')

        fkt_1_str = fkt_1_a2_str + 'x^2' + fkt_1_a1_str + 'x' + fkt_1_a0_str
        fkt_1_pq_str = 'x^2' + fkt_1_p_str + r' \cdot x' + fkt_1_q_str
        fkt_2_str = gzahl(6*faktor) + 'x' + fkt_1_a1_str
        fkt_3_str = gzahl(6*faktor)
        fkt_1_x1 = fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str + r'}'
        fkt_1_x2 = fkt_1_p3_str + r' - \sqrt{' + fkt_1_disk_str + r'}'

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extremstellen der Funktion f und deren Art'
                       + ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str
                       + r' \quad (1BE) \\ f^{ \prime \prime }(x) ~=~' + fkt_2_str
                       + r' \quad \mathrm{und} \quad f^{ \prime \prime \prime } (x) ~=~' + fkt_3_str
                       + r' \quad (2BE) \\ f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_1_str + r' \vert ~ \div ' + gzahl_klammer(3 * faktor) + r' \quad (1BE) \\'
                       r' 0~=~ ' + fkt_1_pq_str + r' \quad (1BE) \\' + r' x_{1/2}~=~ - \frac{'
                       + fkt_1_p_str + r'}{2} \pm \sqrt{ \left(' + r' \frac{'
                       + fkt_1_p_str + r'}{2} \right)^2-(' + fkt_1_q2_str + r')} \quad (2BE) \\ =~ '
                       + fkt_1_p3_str + r' \pm \sqrt{' + r' \frac{' + fkt_1_p2_str
                       + r'}{4}' + fkt_1_q3_str + r'} ~=~' + fkt_1_p3_str + r' \pm \sqrt{' + fkt_1_disk_str
                       + r'} \quad (4BE) \\ x_1~=~' + fkt_1_p3_str + r' + \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{und} \quad x_2~=~' + fkt_1_p3_str + r' - \sqrt{'
                       + fkt_1_disk_str + r'}  \quad (2BE) \\'
                       + r'f^{ \prime \prime } (x_2) ~=~' + gzahl(6*faktor)
                       + r' \cdot \left( ' + fkt_1_x1 + r' \right) ' + fkt_1_a1_str
                       + r' \quad (1BE) \\ ~=~ + \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{>~0} \quad \to TP \quad (2BE) \\ f^{ \prime \prime } (x_2) ~=~'
                       + gzahl(6 * faktor) + r' \cdot \left( ' + fkt_1_x2
                       + r' \right) ' + fkt_1_a1_str + r' \quad (1BE) \\ ~=~ - \sqrt{' + fkt_1_disk_str
                       + r'} \quad \mathrm{<~0} \quad \to HP \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'e' in teilaufg:
        # Mögliche Wendepunkte berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        liste_punkte.append(punkte)
        fkt_1_a1_str = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor, r' a')
                        + vorz_v_innen(-2 * faktor * (nst_1 + nst_3),')'))
        fkt_1_a1_str_neg = (vorz(-1*faktor) + '(' + vorz_v_aussen(-2 * faktor, r' a')
                            + vorz_v_innen(-2 * faktor * (nst_1 + nst_3), ')'))

        xwert_wendepunkt = r' \frac{1}{3} a' + vorz_str(Rational((nst_1+nst_3),3))
        fkt_2_str = gzahl(6*faktor) + 'x' + fkt_1_a1_str
        fkt_3_str = gzahl(6*faktor)

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie mögliche Wendepunkte der Funktion f '
                                                'mithilfe des hinr. Kriteriums. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ~' + fkt_1_a1_str_neg + r' \quad \vert \div '
                       + gzahl_klammer(6 * faktor) + r' \quad (1BE) \\ x_1~=~ \frac{1}{3} a'
                       + vorz_str(Rational((nst_1+nst_3),3))
                       + r' \quad (1BE) \quad \to \quad f^{ \prime \prime \prime }(' + xwert_wendepunkt
                       + r') ~=~ ' + gzahl(6*faktor) + r' \quad \neq 0 \quad \to \quad Wendepunkt \quad (3BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
        i += 1

    if 'f' in teilaufg:
        # Wert a berechnen, bei dem der Wendepunkt an einer gegebenen Stelle ist

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        liste_punkte.append(punkte)
        wert_a_wp = nzahl(1,5)
        xwert_wp = Rational((wert_a_wp + nst_1 + nst_3),3)
        xwert_wendepunkt = r' \frac{1}{3} a' + vorz_str(Rational((nst_1 + nst_3), 3))
        aufgabe.append(beschriftung(teilaufg,i) + f'Berechnen Sie den Wert von a,'
                                                f' bei dem der Wendepunkt an der Stelle x = {xwert_wp} ist. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + gzahl(xwert_wp) + '~=~' + xwert_wendepunkt
                       + r' \quad \vert ~' + gzahl(Rational(-1 * (nst_1 + nst_3), 3))
                       + r' \quad \vert \cdot 3 \quad \to \quad a~=~' + str(wert_a_wp) + r' \quad (3BE) ')
        i += 1
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

# alte Aufgaben, die nicht mehr benötigt werden bzw. von denen eine verbesserte Version existiert
def kurvendiskussion_polynome_alt(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ableitungen=None, nullstellen=None, wendenormale=True, i=0, BE=[]):
    # In dieser Aufgabe sollen die SuS eine vollständige Kurvendiskussion eines Polynoms dritten Grades durchführen.
    # Mit dem Parameter 'ableitungen=' kann Teilaufgabe d) festgelegt werden. Standardmäßig ist 'ableitung=None' und die SuS müssen in Teilaufgabe d) die Ableitungen berechnen. Ist 'ableitungen=True' sind die Ableitungen gegeben und die SuS müssen mithilfe der Ableitungsregeln die Berechnung der Ableitung erläutern.
    # Mit dem Parameter 'nullstellen=' wird die Art der Nullstellen der Funktion festgelegt. Es gibt eine ganzzahlige Nullstelle und dann können die anderen beiden Nullstellen rational bzw. irrational sein. Standardmäßig ist 'nullstellen=None' und die Art der Nullstellen wird zufällig ausgewählt.
    # Mit dem Parameter 'wendenormale=' kann für Teilaufgabe h) festgelegt werden, ob die Wendenormale berechnet werden soll. Standardmäßig ist 'wendenormale=True' und die Wendenormale ist in Teilaufgabe h) enthalten.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden (z.B. liste_punkte=[1,2,3]). Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    if nullstellen == None:
        nullstellen = random.choice(['rational', 'irrational'])
    if nullstellen == 'rational':
        nst_1 = zzahl(1, 3)
        nst_2 = nst_1 + nzahl(1, 3)
        while nst_2 < 1:
            nst_2 + 1
        nst_3 = nst_1 - nzahl(2, 3) + 0.5
        faktor = zzahl(2, 3)

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * (nst_1 + nst_2 + nst_3)
        fkt_a3 = faktor * ((nst_1 * nst_2) + (nst_1 * nst_3) + (nst_2 * nst_3))
        fkt_a4 = -1 * faktor * nst_1 * nst_2 * nst_3
        fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
                   + vorz_str(fkt_a4))
        fkt_h_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3 - 1, 'x')
                     + vorz_str(fkt_a4))
        fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
        fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
        fkt_partial_p = -1 * (nst_2 + nst_3)
        fkt_partial_q = (nst_2 * nst_3)

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_str = (vorz_v_aussen(3*fkt_a1, 'x^2') + vorz_v_innen(2*fkt_a2, 'x') + vorz_str(fkt_a3))
        fkt_2_str = (vorz_v_aussen(6*fkt_a1, 'x') + vorz_str(2*fkt_a2))
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * (nst_1 + nst_2 + nst_3), 3), 'x')
                    + vorz_str(Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)))
        p_fkt_1_pq = Rational(-2 * (nst_1 + nst_2 + nst_3), 3)
        q_fkt_1_pq = Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)
        s_fkt = -1 * faktor * nst_1 * nst_2 * nst_3

    if nullstellen == 'irrational':
        nst_1 = zzahl(1, 3)
        quadr_nst_23 = nzahl(2, 25)
        nst_2 = math.sqrt(quadr_nst_23)
        nst_3 = -1 * nst_2
        faktor = zzahl(3, 8) / 2

        fkt = collect(expand(faktor * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * nst_1
        fkt_a3 = faktor * (-1 * quadr_nst_23)
        fkt_a4 = faktor * nst_1 * quadr_nst_23
        fkt_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3, 'x')
                   + vorz_str(fkt_a4))
        fkt_h_str = (vorz_v_aussen(fkt_a1, 'x^3') + vorz_v_innen(fkt_a2, 'x^2') + vorz_v_innen(fkt_a3 - 1, 'x')
                     + vorz_str(fkt_a4))
        fkt_partial = faktor * (x ** 2 - quadr_nst_23)
        fkt_partial_pq = x ** 2 - quadr_nst_23
        fkt_partial_p = 0
        fkt_partial_q = -1 * quadr_nst_23

        fkt_1 = collect(expand(diff(fkt, x, 1)), x)
        fkt_1_str = (vorz_v_aussen(3*fkt_a1, 'x^2') + vorz_v_innen(2* fkt_a2, 'x') + vorz_str(fkt_a3))
        fkt_2_str = (vorz_v_aussen(6*fkt_a1, 'x') + vorz_str(2* fkt_a2))
        fkt_1_pq = ('x^2' + vorz_v_innen(Rational(-2 * nst_1, 3), 'x') +
                    vorz_str(Rational(quadr_nst_23, -3)))
        p_fkt_1_pq = Rational((-2 * nst_1), 3)
        q_fkt_1_pq = Rational(-1 * quadr_nst_23, 3)
        s_fkt = faktor * nst_1 * quadr_nst_23

    if nullstellen not in (['rational', 'irrational', None]):
        exit("nullstellen müssen None, 'rational' oder 'irrational' sein")

    fkt_b2 = nst_1 * fkt_a1
    fkt_c2 = fkt_a2 + fkt_b2
    fkt_b3 = nst_1 * fkt_c2
    fkt_c3 = fkt_a3 + fkt_b3
    fkt_b4 = nst_1 * fkt_c3
    fkt_c4 = fkt_a4 + fkt_b4

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen das Verhalten der Funktion im Unendlichen untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuchen Sie das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~'
                       + gzahl(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} '
                       + fkt_str + '~=~' + gzahl(grenzwert_min) + r' \quad (2BE)')
        liste_punkte.append(2)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen die Funktion auf Symmetrie untersuchen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        fkt_sym = fkt.subs(x, -x)
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3BE)')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3BE)')
        else:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad '
                                                          r' \mathrm{nicht~symmetrisch} \quad (3BE)')
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie die Symmetrie der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + lsg)
        liste_punkte.append(3)
        i += 1

    if 'c' in teilaufg:
        # DIe SuS die Schnittpunkte der Funktion mit den Achsen berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        table2 = Tabular('c c|c|c|c', row_height=1.2)
        table2.add_row('', fkt_a1, fkt_a2, fkt_a3, fkt_a4)
        table2.add_hline(2, 5)
        table2.add_row('Berechnung der Partialfunktion  mit Hornerschema: ', '', fkt_b2, fkt_b3, fkt_b4)
        table2.add_hline(2, 5)
        table2.add_row('', fkt_a1, fkt_c2, fkt_c3, fkt_c4)

        if nst_1 == 0 or nst_2 == 0 or nst_3 == 0:
            lsg = r' \quad (3BE) \\'
            punkte = 15
        else:
            lsg = r' \quad S_y(0 \vert' + gzahl(s_fkt) + r') \quad (4BE) \\'
            punkte = 16

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Schnittpunkte mit den Achsen der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Ansatz:~f(x)~=~0} \quad \to \quad 0~=~' + fkt_str
                       + r' \quad \mathrm{durch~probieren:~x_1~=~}' + gzahl(nst_1)
                       + r' \quad (2BE) \\' + '(' + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst_1) + ')~=~'
                       + latex(fkt_partial) + r' \quad (4P)')
        loesung.append(table2)
        loesung.append(latex(fkt_partial) + r'~=~0 \quad \vert ~ \div ' + gzahl_klammer(faktor)
                       + r' \quad \to \quad 0~=~' + latex(fkt_partial_pq) + r' \quad (2BE) \\'
                       + r' x_{2/3}~=~ - \frac{' + gzahl_klammer(fkt_partial_p) + r'}{2} \pm \sqrt{ \left('
                       + r' \frac{' + latex(fkt_partial_p) + r'}{2} \right)^2-' + gzahl_klammer(fkt_partial_q)
                       + r'} \quad (2BE) \\' + r' x_2~=~' + gzahl(round(nst_2, 3))
                       + r' \quad \mathrm{und} \quad x_3~=~' + gzahl(round(nst_3, 3)) + r' \quad (2BE) \\'
                       + r'S_{x_1}(' + gzahl(nst_1) + r' \vert 0) \quad S_{x_2}(' + gzahl(round(nst_2, 3))
                       + r' \vert 0) \quad S_{x_3}(' + gzahl(round(nst_3, 3)) + r' \vert 0)' + lsg
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # Je nach gewählten Parameter 'ableitung=' müssen die SuS entweder die ersten drei Ableitungen berechnen bzw. die Berechnung der Ableitung begründen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        fkt_3 = 6 * faktor
        if ableitungen:
            punkte = 4
            aufgabe.extend(('Gegeben sind die ersten drei Ableitungen der Funktion f.',
                            r'f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \hspace{5em} f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \hspace{5em} f^{ \prime \prime \prime } (x) ~=~' + gzahl(fkt_3),
                            beschriftung(teilaufg,i) + 'Erläutern Sie mithilfe der elementaren Ableitungsregeln, '
                                + 'wie diese Ableitungen bestimmt wurden. \n\n'))
            # Tabelle mit dem Text
            table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
            table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l',
                            data='Erklärung der Ableitungen'), 'Punkte')
            table1.add_row('', '-', 'bei der Ableitung fällt der hintere Term (die Konstante) '
                           + 'immer weg (Konstantenregel) ', '1P')
            table1.add_row('', '-', 'die einzelnen Summanden können nach der Summenregel '
                           + 'einzeln abgeleitet werden', '1P')
            table1.add_row('', '-', 'die Potenzen von x werden nach der Potenzregeln abgeleitet, '
                           + 'wobei der bisherige Exponent mit dem Faktor multipliziert wird (Faktorregel)'
                           + ' und der neue Exponent um eins kleiner wird', '2P')
            table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
            loesung.append(table1)
            if teilaufg[i+1] == 'f':
                loesung.append(' \n\n\n')
        else:
            punkte = 3
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die ersten drei Ableitungen der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~' + fkt_1_str
                           + r' \hspace{5em} f^{ \prime \prime }(x) ~=~' + fkt_2_str
                           + r' \hspace{5em} f^{ \prime \prime \prime } (x) ~=~' + gzahl(fkt_3) + r' \quad (3BE) \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Hier sollen die SuS die Extrema und deren Art mithilfe des notwendigen und hinreichenden Kriteriums berechnen.
        punkte = 12
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        x_12_fkt_1 = solve(fkt_1, x)
        x_1_fkt_1 = round(x_12_fkt_1[0], 3)
        x_2_fkt_1 = round(x_12_fkt_1[1], 3)

        fkt_2 = expand(diff(fkt, x, 2))
        fkt_2_str = vorz_v_aussen(6 * faktor, 'x') + vorz_str(-2 * faktor * (nst_1 + nst_2 + nst_3))
        fkt_3 = expand(diff(fkt, x, 3))
        fkt_3 = vorz_str(6 * faktor)

        if fkt_2.subs(x, x_1_fkt_1) < 0:
            loesung_f_monotonie_1 = (r'~<~0~ \to HP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3BE) \\')
        else:
            loesung_f_monotonie_1 = (r'~>~0~ \to TP(~' + gzahl(x_1_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_1_fkt_1), 3)) + r') \quad (3BE) \\')

        if fkt_2.subs(x, x_2_fkt_1) < 0:
            loesung_f_monotonie_2 = (r'~<~0~ \to HP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3BE) \\')
        else:
            loesung_f_monotonie_2 = (r'~>~0~ \to TP(~' + gzahl(x_2_fkt_1) + r'~ \vert ~'
                                     + gzahl(round(fkt.subs(x, x_2_fkt_1), 3)) + r') \quad (3BE) \\')

        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie die Extrema der Funktion f und deren Art'
                                                ' mithilfe des hinreichenden Kriteriums. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + latex(fkt_1) + r' \vert ~ \div ' + gzahl_klammer(3 * faktor) + r' \quad (1BE) \\  0 ~=~'
                       + fkt_1_pq + r' \quad \to \quad ' + r' x_{1/2} ~=~ - \frac{' + gzahl_klammer(p_fkt_1_pq)
                       + r'}{2} \pm \sqrt{ \left(' + r' \frac{' + latex(p_fkt_1_pq) + r'}{2} \right)^2-'
                       + gzahl_klammer(q_fkt_1_pq) + r'} \quad (3BE) \\'
                       + r'x_1~=~' + gzahl(x_1_fkt_1) + r' \quad \mathrm{und} \quad x_2~=~' + gzahl(x_2_fkt_1)
                       + r' \quad (2BE) \\' + r' f^{ \prime \prime }(' + gzahl(x_1_fkt_1) + ')~=~'
                       + gzahl(round(fkt_2.subs(x, x_1_fkt_1), 3)) + loesung_f_monotonie_1 + r' f^{ \prime \prime }('
                       + gzahl(x_2_fkt_1) + ')~=~' + gzahl(round(fkt_2.subs(x, x_2_fkt_1), 3))
                       + loesung_f_monotonie_2 + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        # Die SuS sollen mithilfe der Ergebnisse der vorherigen Teilaufgabe die Existenz eines Wendepunktes begründen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        xwert_Wendepunkt = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor), 3)
        aufgabe.append(beschriftung(teilaufg,i) + 'Begründen Sie mithilfe der vorherigen Ergebnisse, '
                                                'dass diese Funktion einen Wendepunkt besitzt. \n\n')
        table1 = Tabular('p{0.2cm}p{13cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')', 'mögliche Begründung', 'Punkte')
        if 'c' in teilaufg:
            table1.add_row('', f'Da die Funktion drei Nullstellen besitzt und ein Polynom mit ganzrationalen '
                           f'Exponenten ist, hat sie zwei Extrema und damit einen Wendepunkt.' , '3P')
            punkte = 3
        if 'e' in teilaufg and 'c' not in teilaufg:
            table1.add_row('', f'Da die Funktion zwei Extrema hat, besitzt sie auch einen Wendepunkt.' , '2P')
            punkte = 2
        loesung.append(table1)
        loesung.append(' \n')
        liste_punkte.append(punkte)
        i += 1


    if 'g' in teilaufg:
        # Die SuS sollen den Wendepunkt der Funktion berechnen,
        punkte = 5
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        xwert_Wendepunkt = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor), 3)
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Wendepunkt der Funktion f. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' f^{ \prime \prime }(x) ~=~0 \quad \to \quad 0~=~'
                       + fkt_2_str + r' \quad \vert ' + vorz_str(2 * faktor * (nst_1 + nst_2 + nst_3))
                       + r' \quad \vert \div ' + gzahl_klammer(6 * faktor) + r' \quad \to \quad x_1~=~'
                       + gzahl(xwert_Wendepunkt) + r' \quad (2BE) \\ f^{ \prime \prime \prime }('
                       + gzahl(xwert_Wendepunkt) + r') \quad \neq 0 \quad \to \quad WP('
                       + gzahl(xwert_Wendepunkt) + r' \vert ' + gzahl(round(fkt.subs(x, xwert_Wendepunkt), 3))
                       + r') \quad (3BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'h' in teilaufg:
        # Die SuS sollen die Wendetangente bzw. die Wendenormale, abhängig vom gewählten Parameter 'wendenormale', berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        xwert_wp1 = N(Rational(2 * faktor * (nst_1 + nst_2 + nst_3), 6 * faktor), 3)
        ywert_wp1 = N(fkt.subs(x, xwert_wp1), 3)
        ywert_wp1_fkt_1 = N(fkt_1.subs(x, xwert_wp1), 3)
        fkt_t = ywert_wp1_fkt_1 * (x - xwert_wp1) + ywert_wp1
        fkt_n = (-1 / ywert_wp1_fkt_1) * (x - xwert_wp1) + ywert_wp1
        # print('Wendepunkt: ' + str(xwert_wp1))
        # print('f(x)=' + latex(fkt))
        # print('f`(x)=' + latex(fkt_1))
        # print('t(x)=' + latex(fkt_t))

        if wendenormale not in ([True, False]):
            exit("wendenormale muss True oder False sein")
        if wendenormale == True:
            punkte = 6
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Wendetangente und die Wendenormale '
                                                    f'der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                           + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                           + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                           + vorz_v_aussen(ywert_wp1_fkt_1, '(x') + vorz_v_innen(-1 * N(xwert_wp1, 3), ')')
                           + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1, 'x')
                           + vorz_str(N(-1 * ywert_wp1_fkt_1 * xwert_wp1 + ywert_wp1, 3))
                           + r' \quad (3BE) \\ \mathrm{Die~Steigung~der~Normale~am~Wendepunkt~wird~berechnet~mit \quad '
                           + r' m_n ~=~ \frac{-1}{f^{ \prime }(x_{w})} \quad und~daraus~folgt:} \\'
                           + r'n(x)~=~ - \frac{1}{f^{ \prime }(x_{w})} \cdot '
                           + r'(x - x_{w}) + y_{w} ~=~ ' + vorz_v_aussen(-1 / ywert_wp1_fkt_1, '(x')
                           + vorz_v_innen(-1 * N(xwert_wp1, 3), ')') + vorz_str(ywert_wp1) + '~=~'
                           + vorz_v_aussen(-1 / ywert_wp1_fkt_1, 'x')
                           + vorz_str(N(xwert_wp1 / ywert_wp1_fkt_1 + ywert_wp1, 3))
                           + r' \quad (3BE) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        if wendenormale == False:
            punkte = 3
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Funktionsgleichung der Wendetangenten'
                                                    f' der Funktion f. \n\n')
            loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Die~Steigung~der~Tangente~am~Wendepunkt~wird~'
                           + r'berechnet~mit \quad m_t ~= ~f^{ \prime }(x_{w}) \quad und~daraus~folgt:} \\'
                           + r't(x)~=~ f^{ \prime }(x_{w}) \cdot (x - x_{w}) + y_{w} ~=~ '
                           + vorz_v_aussen(ywert_wp1_fkt_1, '(x') + vorz_v_innen(-1 * N(xwert_wp1, 3), ')')
                           + vorz_str(ywert_wp1) + '~=~' + vorz_v_aussen(ywert_wp1_fkt_1, 'x')
                           + vorz_str(N(-1 * ywert_wp1_fkt_1 * xwert_wp1 + ywert_wp1, 3))
                           + r' \quad (3BE) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')


        # xmin = int(round(nst_3 - 0.4, 0))
        # xmax = int(round(nst_2 + 0.4, 0))
        # Graph(xmin,xmax, fkt, name='latex(fkt_t)')
        liste_punkte.append(punkte)
        i += 1

    if 'i' in teilaufg:
        # Die SuS sollen den Graphen der Funktoin zeichnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        xmin = int(round(nst_3 - 0.4, 0))
        xmax = int(round(nst_2 + 0.4, 0))
        # plot(fkt, (x,xmin_f,xmax_f) ,show=False)

        aufgabe.append(str(liste_teilaufg[i])
                       + f') Zeichnen Sie den Graphen im Intervall I[ {gzahl(xmin)} | {gzahl(xmax)} ] \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathrm{Koordinatensystem~(2BE) \quad Werte~(2BE)'
                                                r' \quad Graph~(1BE) \to \quad insgesamt~(5P)}')
        Graph(xmin, xmax, fkt, name=f'Loesung_{nr}{liste_teilaufg[i]}.png')
        loesung.append('Figure')

        liste_punkte.append(5)
        i += 1

    if 'j' in teilaufg: # and (nst_1 > 0 or nst_2 > 0 or nst_3 > 0) and nst_1 * nst_2 * nst_3 != 0:
        # Die SuS sollen die vom Funktionsgraphen im ersten Quadranten eingeschlossene Fläche berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        Fkt = integrate(fkt, x)
        Fkt_str = (vorz_v_aussen(Rational(fkt_a1, 4), 'x^4') + vorz_v_innen(Rational(fkt_a2, 3), 'x^3')
                   + vorz_v_innen(Rational(fkt_a3, 2), 'x^2') + vorz_v_innen(fkt_a4, 'x'))

        def erste_positive_nst(vec):
            # print(vec)
            vec.sort()
            # print(vec)
            for element in vec:
                if element > 0:
                    # print(element)
                    return element

        obere_grenze = N(erste_positive_nst([nst_1, nst_2, nst_3]), 3)
        loesung_integral = Fkt.subs(x, obere_grenze)
        if 'c' in teilaufg:
            aufgabe.extend((f'Der Graph von f schließt, mit der x-Achse und der y-Achse '
                            + ' rechts vom Ursprung eine Fläche ein. \n\n', str(liste_teilaufg[i])
                            + f') Berechnen Sie die eingeschlossen Fläche. \n\n'))
        else:
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Fläche unter dem Graphen '
                                                    f'im Intervall I(0|{gzahl(obere_grenze)}). \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \left| \int \limits_0^{' + gzahl(obere_grenze) + '}' + fkt_str
                       + r'~ \mathrm{d}x \right| ~=~ \left| \left[' + Fkt_str + r' \right]_{0}^{' + gzahl(obere_grenze)
                       + r'} \right| ~=~' + latex(abs(N(loesung_integral, 3))) + r' \quad (4BE) \\')
        liste_punkte.append(4)
        i += 1

    # noch Teilaufgabe mit Flächenberechnung ergänzen
    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def testaufgabe(nr, teilaufg=['a', 'b', 'c'], i=0, BE=[], gleichungen=[]):

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    obj1_1, obj2_1, var_obj1_1, var_obj2_1 = [[1,1,2], [0,0,1]], [[2,2,2],[1,1,0]], ['a'], ['b']
    obj1_2, obj2_2, var_obj2_2 = [[1,1,2]], [[2,2,2],[0,0,1], [1,1,0]], ['a', 'b']
    obj1_3, obj2_3, var_obj2_3 = [[1,1,2]], [[0,0,1], [1,1,0]], ['a','b']
    text1, lsg1, punkte1 = vektor.rechnung(obj1_1, obj2_1, var_obj1_1, var_obj2_1)
    text2, lsg2, punkte2 = vektor.rechnung(obj1_2, obj2_2, var_obj2=var_obj2_2)
    text3, lsg3, punkte3 = vektor.rechnung(obj1_3, obj2_3, var_obj2=var_obj2_3)


    aufgabe.append('Lösen Sie das Gleichungssystem.')
    loesung.append(text1[0])
    loesung.extend((NoEscape(r'Lösung der ersten Rechnung: $' + str(lsg1) + '$ und Punkte: ' + str(punkte1)), ' \n\n'))
    loesung.append(text2[0])
    loesung.extend((NoEscape(r'Lösung der zweiten Rechnung: $' + str(lsg2) + '$ und Punkte: ' + str(punkte2)), ' \n\n'))
    loesung.append(text3[0])
    loesung.extend((NoEscape(r'Lösung der dritten Rechnung: $' + str(lsg3) + '$ und Punkte: ' + str(punkte3)), ' \n\n'))

    liste_punkte = [punkte1 + punkte2]
    liste_bez = ['Test']
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]