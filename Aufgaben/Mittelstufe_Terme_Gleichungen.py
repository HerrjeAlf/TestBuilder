import string

import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *


a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

def basisaufgaben(nr,teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], anzahl=[False, True][0], wdh=[False, True][0], notizfeld=[False, True][0], neue_seite=[None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13][0], BE=[]):
    # Hier sollen SuS Terme addieren bzw. subtrahieren
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) einfache Bruchterme einer Menge berechnen
    # b) Potenzgesetz an einem Beispiel erkennen
    # c) Rechenregeln der Bruchrechnung kennen bzw. Taschenrechner bedienen können
    # d) Mittelwert zweier Zahlen ausrechnen
    # e) Scheitelpunktform einer Parabel ricntig erkennen
    # f) EInkauspreis mit Rabatt berechnen
    # g) Wahrscheinlichkeit für grau markierte Fläche angeben
    # h)
    # i) unbekannten Winkel mit Innenwinkelsumme berechnen
    # j) richtige Bezeichnung für ein gegebenes Viereck benennen
    # k) den richtigen Satz des Pythagoras zum gegebenen Dreieck auswählen
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "notizfeld" kann unter den Teilaufgaben ein Notizfeld angezeigt werden. Standardmäßig ist es nicht dabei
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    if isinstance(neue_seite, int):
        neue_seite = [neue_seite]
    neue_seite[-1] = len(teilaufg) if neue_seite[-1] > len(teilaufg) else neue_seite[-1]

    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh

    i, liste_punkte, liste_bez = 0, [len(teilaufg)], [f'{str(nr)}']

    aufgabe = [MediumText(NoEscape(r' \noindent \textbf{Aufgabe ' + str(nr) + r'}')), ' \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []


    for element in teilaufg:
        if element == 'a':
            nenner = random.choice([2, 3, 4, 5, 6, 8])
            anteil = nzahl(2, 10) * 10
            wert = anteil * nenner
            einheit = random.choice(['kg', 't', 'm', 'l', '€'])
            aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + r'Bestimmen Sie '
                                    + r'$ \frac{1}{' + gzahl(nenner) + '} $ von ' + gzahl(wert) + einheit + '.'))
            loesung.append(beschriftung(len(teilaufg), i, True) + r' \frac{1}{ ' + gzahl(nenner)
                           + r'} \cdot ' + gzahl(wert) + einheit + '~=~' + gzahl(anteil) + einheit + r' \quad (1BE) ')
            if notizfeld:
                aufgabe.append(['Bild', '430px'])
                grafiken_aufgaben.append('notizen_klein')
            else:
                aufgabe.append(' \n\n')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1
            del nenner, einheit

        if element == 'b':
            bas, exp = random_selection(list(range(3,9)), anzahl=2)
            exp_1 = nzahl(1,2)
            exp_2 = exp - exp_1
            aufg_1 = (gzahl(bas) + '^{' + gzahl(exp, exp=True) + '} ~=~' + gzahl(bas) + '^{' + gzahl(exp_1, exp=True)
                      + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp_2, exp=True) + '}')
            aufg_2 = gzahl(bas) + '^{' + gzahl(exp, exp=True) + '} ~=~' + gzahl(bas) + r' \cdot ' + gzahl(exp)
            aufg_3 = gzahl(bas) + '^{' + gzahl(exp, exp=True) + '} ~=~' + gzahl(exp) + '^{' + gzahl(bas, exp=True) + r'}'
            list_aufg = [r' \square \quad '  + aufg_1, r' \square \quad ' + aufg_2, r' \square \quad ' + aufg_3]
            list_lsg = [r' \surd \quad ' + aufg_1, r' \square \quad ' + aufg_2, r' \square \quad ' + aufg_3]
            ausw = [0,1,2]
            random.shuffle(ausw)
            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                     + 'Kreuzen Sie die richtige Aussage an.'),
                            list_aufg[ausw[0]] + r' \hspace{5em} ' + list_aufg[ausw[1]] + r' \hspace{5em} '
                            + list_aufg[ausw[2]] + r' \\'))
            loesung.append(beschriftung(len(teilaufg), i, True) + list_lsg[ausw[0]] + r' \hspace{5em} '
                           + list_lsg[ausw[1]] + r' \hspace{5em} ' + list_lsg[ausw[2]] + r' \quad (1BE) ')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'c':
            werte = random_selection(list(range(1,11)),4)
            bruch1_str = r' \frac{' + gzahl(werte[0]) + r'}{' + gzahl(werte[1]) + '}'
            bruch2_str = r' \frac{' + gzahl(werte[2]) + r'}{' + gzahl(werte[3]) + '}'
            list_terme = [bruch1_str + r' \cdot ' + bruch2_str, bruch1_str + r' \div ' + bruch2_str,
                          bruch1_str + '+' + bruch2_str, bruch1_str + '-' + bruch2_str]
            list_aufg = [r'~ \square \quad '  + element for element in list_terme]
            list_lsg = list_aufg.copy()
            list_erg = [Rational(werte[0]*werte[2],werte[1]*werte[3]), Rational(werte[0]*werte[3],werte[1]*werte[2]),
                        Rational(werte[0]*werte[3] + werte[2]*werte[1],werte[1]*werte[3]),
                        Rational(werte[0]*werte[3] - werte[2]*werte[1],werte[1]*werte[3])]
            erg_ausw = random.choice([0,1,2,3])
            erg = list_erg[erg_ausw]
            list_lsg[erg_ausw] = r' \surd \quad ' + list_terme[erg_ausw] + '~=~' + gzahl(erg)
            ausw = [0,1,2,3]
            random.shuffle(ausw)
            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                     + r'Kreuzen Sie den Term an, dessen Wert $' + gzahl(erg) + '$ beträgt.'),
                            list_aufg[ausw[0]] + r' \hspace{4em} ' + list_aufg[ausw[1]] + r' \hspace{4em} '
                            + list_aufg[ausw[2]] + r' \hspace{4em} ' + list_aufg[ausw[3]] + r' \\'))
            loesung.append(beschriftung(len(teilaufg), i, True) + list_lsg[ausw[0]] + r' \hspace{4em} '
                           + list_lsg[ausw[1]] + r' \hspace{4em} ' + list_lsg[ausw[2]]
                           + r' \hspace{4em} ' + list_lsg[ausw[3]] + r' \quad (1BE) ')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'd':
            erg = nzahl(1,5)
            abstand = nzahl(8,16)/2
            min = erg - abstand
            max = erg + abstand
            aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                    + r'Geben Sie diejenige Zahl an, die auf der Zahlengeraden in der Mitte von '
                                    + gzahl(min) + ' und ' + gzahl(max) + ' liegt.'))
            loesung.append(beschriftung(len(teilaufg), i, True) + r' \frac{' + gzahl(min)
                           + vorz_str(max) + '}{2} ~=~ ' + gzahl(erg) + r' \quad (1BE) ')
            if notizfeld:
                aufgabe.append(['Bild', '430px'])
                grafiken_aufgaben.append('notizen_klein')
            else:
                aufgabe.append(' \n\n')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'e':
            xwert = zzahl(1,5)
            ywert = zzahl(1,5)
            list_fkt = [r' \mathrm{ y~=~ \left( x' + vorz_str(-1*xwert) + r' \right) ^2' + vorz_str(ywert) + '}',
                        r' \mathrm{ y~=~ \left( x' + vorz_str(xwert) + r' \right) ^2' + vorz_str(ywert) + '}',
                        r' \mathrm{ y~=~ \left( x' + vorz_str(xwert) + r' \right) ^2' + vorz_str(-1*ywert) + '}',
                        r' \mathrm{ y~=~ \left( x' + vorz_str(-1*xwert) + r' \right) ^2' + vorz_str(-1*ywert) + '}']
            list_aufg = [r'~ \square \quad ' + element for element in list_fkt]
            list_lsg = list_aufg.copy()
            list_lsg[0] = r' \surd \quad ' + list_fkt[0]
            ausw = [0,1,2,3]
            random.shuffle(ausw)
            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + f'Kreuzen Sie an, welche  '
                                     + f'Parabel den Scheitelpunkt bei S({gzahl(xwert)}|{gzahl(ywert)}) hat.'),
                            list_aufg[ausw[0]] + r' \hspace{2em} ' + list_aufg[ausw[1]] + r' \hspace{2em} '
                            + list_aufg[ausw[2]] + r' \hspace{2em} ' + list_aufg[ausw[3]] + r' \\'))
            loesung.append(beschriftung(len(teilaufg), i, True) + list_lsg[ausw[0]] + r' \hspace{2em} '
                           + list_lsg[ausw[1]] + r' \hspace{2em} ' + list_lsg[ausw[2]] + r' \hspace{2em} '
                           + list_lsg[ausw[3]] + r' \quad (1BE) ')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'f':
            preis = nzahl(10,20) * 50
            rabatt = nzahl(1,5) * 5
            erg = preis*(100-rabatt)/100
            artikel = random_selection(['ein Fahrrad', 'einen Computer',  'ein Handy', 'eine Spielekonsole',
                                        'eine Gitarre', 'ein Paar Sneaker'], 1)[0]
            aufgabe.extend((NoEscape(r' \noindent' + f' Max möchte {artikel} für {preis}€ kaufen und erhält beim Kauf '
                            + f'{rabatt} ' + r' \% Rabatt. '),' \n\n',
                           beschriftung(len(teilaufg), i) + r'Berechnen Sie den Kaufpreis, den Max zahlen muss. '))
            loesung.append(beschriftung(len(teilaufg), i, True) + gzahl(preis) + r' \texteuro \cdot \frac{'
                           + gzahl(100-rabatt) + '}{' + gzahl(100) + '} ~=~' + gzahl(erg) + r' \texteuro \quad (1BE) ')
            if notizfeld:
                aufgabe.append(['Bild', '430px'])
                grafiken_aufgaben.append('notizen_mittel')
            else:
                aufgabe.append(' \n\n')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'g':
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            rows = 4  # Zeilen
            cols = 5  # Spalten

            anz = nzahl(2, rows * cols)
            x_max, y_max_unk = divmod(anz, rows)
            y_max = y_max_unk / rows
            create_rectangle(rows, cols, x_max, y_max, name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                     + f'Geben Sie den Anteil der grau eingefärbten Felder in Prozent an. '),
                            ['Grafik','200px']))
            loesung.append(beschriftung(len(teilaufg), i, True) + gzahl(anz/(rows*cols)*100)
                           + r'~ \% \quad (1BE) ')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'i':
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            gamma = nzahl(16,22)*5
            beta = nzahl(6,12)*5
            alpha = 180 - beta - gamma
            seite_c = nzahl(6, 12)
            seite_a = N(seite_c * math.sin(math.radians(alpha)) / math.sin(math.radians(gamma)), 3)
            seite_b = N(seite_c * math.sin(math.radians(beta)) / math.sin(math.radians(gamma)), 3)
            xwert_punkt_c = N(math.cos(math.radians(alpha))*seite_b,3)
            ywert_punkt_c = N(math.sin(math.radians(alpha))*seite_b,3)

            # Listen für die Zeichung des Dreiecks
            pkt = [[0, 0], [seite_c, 0], [xwert_punkt_c, ywert_punkt_c]]
            pkt_bez = ['', '', '']
            st = ['', '', '']
            st_werte = [seite_a, seite_b, seite_c]
            wk_werte = [alpha, beta, gamma]

            # Auswahl des gesuchten Winkels
            winkel = [r' \alpha ', r' \beta ', r' \gamma ']
            ausw = random.choice([0,1,2])
            wk = [gzahl(wk_werte[0]) + r' ^{ \circ }', gzahl(wk_werte[1]) + r' ^{ \circ }', gzahl(wk_werte[2])+ r' ^{ \circ }']
            wk[ausw] = winkel[ausw]
            dreieck_zeichnen(pkt, pkt_bez, st, wk, f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')

            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                     + r'Geben Sie die Größe des Winkels $ ' + winkel[ausw] + ' $ an.'),
                            ['Grafik','170px'], winkel[ausw] + r' ~=~ .................... '))
            loesung.append(beschriftung(len(teilaufg), i, True) + winkel[ausw] + '~=~' + gzahl(wk_werte[ausw])
                           + r' ^{ \circ } \quad (1BE) \\')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'j':
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')

            # Auswahl des gesuchten Winkels
            quadrat = ([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'k')
            rechteck = ([0, 4, 4, 0, 0], [0, 0, 1, 1, 0], 'k')
            trapez = ([0, 4, 3, 1, 0], [0, 0, 1 , 1, 0], 'k')
            parallelogramm = ([0, 4, 5, 1, 0], [0, 0, 1, 1, 0], 'k')
            auswahl = random.choice([0, 1, 2, 3])
            flaeche = [quadrat, rechteck, trapez, parallelogramm]
            flaeche_zeichnen(flaeche[auswahl], name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            # Erstellen der zufälligen Auswahl
            bezeichnung = ['Quadrat', 'Rechteck', 'Trapez', 'Parallelogramm']
            list_aufg = [r' \square \quad \mathrm{Quadrat} ', r' \square \quad \mathrm{Rechteck} ',
                         r' \square \quad \mathrm{Trapez} ', r' \square \quad \mathrm{Parallelogramm} ']
            rf = [0, 1, 2, 3]
            random.shuffle(rf)
            aufgabe.append(NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i)
                                    + r'Wie heißt diese geometrische Figur. Kreuzen Sie an.'))
            if auswahl == 0:
                aufgabe.append(['Grafik', '50px'])
            else:
                aufgabe.append(['Grafik', '150px'])
            aufgabe.extend((NoEscape(r'$ \hspace{5em} ' + list_aufg[rf[0]] + r' \hspace{4em} ' + list_aufg[rf[1]]
                                    + r' \hspace{4em} ' + list_aufg[rf[2]] + r' \hspace{4em} ' + list_aufg[rf[3]]
                                    + '$'),' \n\n'))
            list_lsg = list_aufg
            list_lsg[auswahl] = r' \surd \quad \mathrm{ ' + bezeichnung[auswahl] + '}'
            loesung.append(beschriftung(len(teilaufg), i, True) + list_lsg[rf[0]]
                           + r' \hspace{4em} ' + list_lsg[rf[1]] + r' \hspace{4em} ' + list_lsg[rf[2]]
                           + r' \hspace{4em} ' + list_lsg[rf[3]] + r' ~ ~ (1BE)')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1

        if element == 'k':
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            n = random.randint(1, 5)
            m = n + random.randint(1, 5)
            # hier werden die Pythagoräischen Zahlentripel für die Seitenlängen berechnet
            l_a = (m ** 2 - n ** 2) / 10
            l_b = 2 * m * n / 10
            l_c = (m ** 2 + n ** 2) / 10
            # hier werden die Winkel berechnet
            w_c = 90
            w_a = round(math.degrees(math.asin(l_a / l_c)))
            w_b = w_c - w_a
            # mithilfe der Seitenlänge werden die Punkte A, B und C im Koordinatensystem berechnet
            pkt = [[0, 0], [l_c, 0], [(l_b ** 2) / l_c, l_a * l_b / l_c]]
            auswahl_beschriftung = random.randint(0, 6)
            bezeichnungen = [
            {'Punkte': ['A', 'B', 'C'], 'Seiten': ['a', 'b', 'c'], 'Winkel': [r' \alpha ', r' \beta ', r'90^{ \circ }']},
            {'Punkte': ['D', 'E', 'F'], 'Seiten': ['d', 'e', 'f'], 'Winkel': [r' \delta ', r' \epsilon ', r'90^{ \circ }']},
            {'Punkte': ['G', 'K', 'L'], 'Seiten': ['g', 'k', 'l'], 'Winkel': [r' \zeta ', r' \eta ', r'90^{ \circ }']},
            {'Punkte': ['M', 'N', 'P'], 'Seiten': ['m', 'n', 'p'], 'Winkel': [r' \mu ', r' \nu ', r'90^{ \circ }']},
            {'Punkte': ['R', 'S', 'T'], 'Seiten': ['r', 's', 't'], 'Winkel': [r' \rho ', r' \sigma ', r'90^{ \circ }']},
            {'Punkte': ['U', 'V', 'W'], 'Seiten': ['u', 'v', 'w'], 'Winkel': [r' \upsilon ', r' \phi ', r'90^{ \circ }']},
            {'Punkte': ['X', 'Y', 'Z'], 'Seiten': ['x', 'y', 'z'], 'Winkel': [r' \chi ', r' \psi ', r'90^{ \circ }']}]

            pkt_bez = (bezeichnungen[auswahl_beschriftung]['Punkte'])
            st = bezeichnungen[auswahl_beschriftung]['Seiten']
            st_werte = [l_a, l_b, l_c]
            wk = bezeichnungen[auswahl_beschriftung]['Winkel']
            wk_werte = [w_a, w_b, w_c]
            dreieck_zeichnen(pkt,st=st,  wk=wk, name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')

            list_gl = [st[0] + '^2 + ' + st[1] + '^2 ~=~ ' + st[2] + '^2',
                       st[1] + '^2 + ' + st[2] + '^2 ~=~ ' + st[0] + '^2',
                       st[0] + '^2 + ' + st[2] + '^2 ~=~ ' + st[1] + '^2']
            list_aufg = [r'~ \square \quad ' + element for element in list_gl]
            list_lsg = list_aufg.copy()
            list_lsg[0] = r' \surd \quad ' + list_gl[0]
            ausw = [0, 1, 2]
            random.shuffle(ausw)

            aufgabe.extend((NoEscape(r' \noindent ' + beschriftung(len(teilaufg), i) + f'Kreuzen Sie an, '
                                     + f'welche Gleichung zur Berechnung der Seite {st[2]} geeignet ist. '),
                            ['Grafik','170px'],
                            r' \hspace{5em} ' + list_aufg[ausw[0]] + r' \hspace{5em} ' + list_aufg[ausw[1]]
                            + r' \hspace{5em} ' + list_aufg[ausw[2]] + r' \\'))
            loesung.append(beschriftung(len(teilaufg), i, True) + list_lsg[ausw[0]] + r' \hspace{2em} '
                           + list_lsg[ausw[1]] + r' \hspace{2em} ' + list_lsg[ausw[2]] + r' \quad (1BE)')
            aufgabe.append('NewPage') if i + 1 in neue_seite else ''
            i += 1


    liste_punkte = BE if len(BE) == len(teilaufg) else liste_punkte
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def terme_addieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], anzahl=False, wdh=False, i = 0, BE=[]):
    # Hier sollen SuS Terme addieren bzw. subtrahieren
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Terme mit einer Basis und ganzzahligen Faktoren (zwei Summanden)
    # b) Terme mit einer Basis und ganzzahligen Faktoren (drei Summanden)
    # c) Terme mit einer Basis und rationalen Faktoren (zwei Summanden)
    # d) Terme mit einer Basis und rationalen Faktoren (drei Summanden)
    # e) Bruchterme mit einer Basis (zwei Summanden)
    # f) Bruchterme mit einer Basis (drei Summanden)
    # g) gemischte Terme mit einer Basis und ganzzahligen Faktoren und Zahlen (3 Summanden)
    # h) gemischte Terme mit einer Basis und ganzzahligen Faktoren und Zahlen (5 Summanden)
    # i) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (4 Summanden)
    # j) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (6 Summanden)
    # k) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (8 Summanden)
    # l) gemischte Bruchterme mit vers. gleichwertigen Termen (4 Summanden)
    # d) gemischte Bruchterme mit vers. gleichwertigen Termen (6 Summanden)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Fasse die Terme zusammen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def einf_ganzz_terme(anz_sum):
        fakt = faktorliste(anz_sum, 1,12)
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = '~' + vorz_v_aussen(fakt[0],bas[0])
        for k in range(len(fakt)-1):
            aufg = aufg + vorz_v_innen(fakt[k + 1],bas[0])
        lsg = aufg + '~=~' + str(sum(fakt)) + bas[0]
        return aufg, lsg

    def einf_ratio_terme(anz_sum):
        fakt = [zzahl(1,20) for step in range(anz_sum)]
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg =  '~' + vorz_v_aussen(fakt[0]/10,bas[0])
        for k in range(len(fakt) - 1):
            aufg = aufg + vorz_v_innen(fakt[k + 1]/10, bas[0])
        lsg = aufg + '~=~' + latex(sum(fakt)/10) + bas[0]
        return aufg, lsg

    def einf_bruch_terme(anz_sum):
        fakt = [random.choice([-1,1])* Rational(nzahl(1,12), random.choice([2, 3, 5, 7, 11])) for _ in range(anz_sum)]
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = '~' + vorz_v_aussen(fakt[0], bas[0])
        for k in range(len(fakt) - 1):
            aufg = aufg + vorz_v_innen(fakt[k + 1], bas[0])
        lsg = aufg + '~=~' + latex(sum(fakt)) + bas[0]
        return aufg, lsg

    def einf_gem_ganzz_terme(anz_sum):
        fakt = faktorliste(anz_sum, 2,12)
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z])
        liste_bas = [['', str(bas[0])][step%2] for step in range(anz_sum)]
        liste_bas_zahl = [1 if element == '' else bas[0] for element in liste_bas]
        summe = 0
        for k in range(len(liste_bas_zahl)):
            summe += fakt[k]*liste_bas_zahl[k]
        aufg =  '~' + vorz_v_aussen(fakt[0],liste_bas[0])
        for k in range(len(liste_bas)-1):
            aufg = aufg + vorz_v_innen(fakt[k+1],liste_bas[k+1])
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg

    def gem_glw_ganzz_terme(anz_sum):
        if anz_sum == 1:
            anz_sum = anz_sum + 1
            anz_glw = 1
        elif anz_sum < 5:
            anz_glw = 2
        else:
            anz_glw = 3
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z], 2,False)
        liste_glw_terme = []
        for step in range(anz_glw):
            glw_term = 1
            for element in bas:
                exp = nzahl(0,5)
                glw_term = glw_term*(element**exp)
            liste_glw_terme.append(glw_term)
        # print(liste_glw_terme)
        liste_terme = []
        for step in range(anz_sum):
            liste_terme.append([zzahl(1,12), liste_glw_terme[step % anz_glw]])
        random.shuffle(liste_terme)
        # print(liste_terme)
        summe = 0
        for element in liste_terme:
            summe += element[0] * element[1]
        aufg = '~' + vorz_v_aussen(liste_terme[0][0], fakt_var(liste_terme[0][1]))
        for k in range(len(liste_terme) - 1):
            aufg = aufg + vorz_v_innen(liste_terme[k + 1][0], fakt_var(liste_terme[k + 1][1]))
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg

    def gem_glw_rat_terme(anz_sum):
        if anz_sum == 1:
            anz_sum = anz_sum + 1
            anz_glw = 1
        elif anz_sum < 5:
            anz_glw = 2
        else:
            anz_glw = 3
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z], 2, False)
        liste_glw_terme = []
        for step in range(anz_glw):
            glw_term = 1
            for element in bas:
                exp = nzahl(0, 5)
                glw_term = glw_term * (element ** exp)
            liste_glw_terme.append(glw_term)
        # print(liste_glw_terme)
        liste_terme = []
        for step in range(anz_sum):
            liste_terme.append([Rational(zzahl(1, 12), zzahl(1, 12)), liste_glw_terme[step % anz_glw]])
        random.shuffle(liste_terme)
        # print(liste_terme)
        summe = 0
        for element in liste_terme:
            summe += element[0] * element[1]
        aufg = '~' + vorz_v_aussen(liste_terme[0][0], fakt_var(liste_terme[0][1]))
        for k in range(len(liste_terme) - 1):
            aufg = aufg + vorz_v_innen(liste_terme[k + 1][0], fakt_var(liste_terme[k + 1][1]))
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg

    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
    aufgaben = {'a': [einf_ganzz_terme, 2], 'b': [einf_ganzz_terme, 3],
                'c': [einf_ratio_terme, 2], 'd': [einf_ratio_terme, 3],
                'e': [einf_bruch_terme, 2], 'f': [einf_bruch_terme, 3],
                'g': [einf_gem_ganzz_terme, 3], 'h': [einf_gem_ganzz_terme, 5],
                'i': [gem_glw_ganzz_terme, 4], 'j': [gem_glw_ganzz_terme, 6],
                'k': [gem_glw_ganzz_terme, 8], 'l': [gem_glw_rat_terme, 4],
                'm': [gem_glw_rat_terme, 6]}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element][0](aufgaben[element][1])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if element in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and i + 1 < len(teilaufg):
            if (i + 1) % 3 != 0 and i + 1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
            elif i + 1 < len(teilaufg):
                aufg = aufg + r' \\\\'
            if (i + 1) % 2 != 0 and i + 1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif i + 1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
            if i + 1 < len(teilaufg):
                aufg = aufg + r' \\\\'
                lsg = lsg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def terme_multiplizieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS das Produkt mehrerer Terme bilden multiplizieren.
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Produkt aus zwei Termen mit einer Variablen und natürlichen Koeffizienten
    # b) Produkt aus drei Termen mit zwei Variablen und ganzzahligen Koeffizienten
    # c) Produkt aus zwei Termen mit einer Variablen und Dezimalbrüchen oder echten Brüchen als Koeffizienten
    # d) Produkt aus drei Termen und zwei Variablen und beliebig ausgewählten Koeffizienten
    # e) Produkt aus drei Termen und zwei Potenzen von Variablen mit ganzzahligen Koeffizienten
    # f) Produkt aus drei Termen und zwei Potenzen von Variablen und beliebig ausgewählten Koeffizienten
    #
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def aufg_lsg(anz_fakt, anz_bas, koef, exp):
        p, q = 1,9
        anz_bas = anz_fakt if anz_bas > anz_fakt else anz_bas
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z], anz_bas, False)
        liste_bas = bas + [1 for _ in range(anz_fakt - anz_bas)]
        random.shuffle(liste_bas)
        liste_exp = [1 for _ in range(anz_fakt)]
        liste_exp = exponenten(anz_fakt, wdh=True) if exp != False else liste_exp
        if koef == False:
            liste_koef = [1 for _ in range(anz_fakt)]
        else:
            koef = random.choice(['nat', 'ganz', 'rat', 'dez']) if koef not in ['nat', 'ganz', 'rat', 'dez'] else koef
            if koef == 'nat':
                liste_koef = [nzahl(p, q) for _ in range(anz_fakt)]
            elif koef == 'ganz':
                liste_koef = [nzahl(p, q) for _ in range(anz_fakt)]
            elif koef == 'rat':
                liste_koef = [Rational(zzahl(p, q), nzahl(p, q)) for _ in range(anz_fakt)]
            else:
                liste_koef = [zzahl(p, 10 * q) / 10 for _ in range(anz_fakt)]
        # print(liste_bas)
        # print(liste_exp)
        # print(liste_koef)
        aufg = '~' + gzahl_klammer(liste_koef[0], fakt_var(liste_bas[0]**liste_exp[0]))
        for k in range(anz_fakt-1):
            aufg += r' \cdot ' + gzahl_klammer(liste_koef[k + 1], fakt_var(liste_bas[k + 1]**liste_exp[k + 1]))
        erg = 1
        for k in range(anz_fakt):
            erg = erg * liste_koef[k]*(liste_bas[k]**liste_exp[k])
        lsg = aufg + '~=~' + latex(erg)
        # print(test)
        return aufg, lsg

    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
    wb = {'a': (2, 1, 'nat', False),
          'b': (3, 2, 'ganz', False),
          'c': (2, 1, random.choice(['rat', 'dez']), False),
          'd': (3, 2, 'egal', False),
          'e': (3, 2, 'ganz', True),
          'f': (3, 2, 'egal', True)}

    aufg = ''
    lsg = ''
    punkte = 0
    for st in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufg_lsg(wb[st][0], wb[st][1], wb[st][2], wb[st][3])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if st in ['a', 'b', 'c', 'd'] and i+1 < len(teilaufg):
            if (i + 1) % 4 != 0 and i + 1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
            elif i + 1 < len(teilaufg):
                aufg = aufg + r' \\\\'
            if (i + 1) % 2 != 0 and i + 1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif i + 1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
                lsg = lsg + r' \hspace{5em} '
            elif i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
                lsg = lsg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def terme_ausmultiplizieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS verschiedene Produkte von Terme mit Klammern ausmultiplizieren
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Klammer mit ganzzahligen Koeffizienten und zwei ganzzahligen Summanden
    # b) Klammer nur mit Vorzeichen und zwei ganzzahligen Summanden mit Variablen
    # c) Klammer mit ganzzahligen Koeffizienten und zwei ganzzahligen Summanden
    # d) Klammer mit ganzzahligen Koeffizienten und zwei ganzzahligen Summanden mit Variablen
    # e) Klammer mit ganzzahligen Koeffizienten und zwei ganzzahligen Summanden mit Variablen und einem weiteren Summanden
    # f) Klammer mit ganzzahligen Koeffizienten sowie einer Variable und drei rationalen Summanden mit einer Variablen
    # g) Klammer mit ganzzahligen Koeffizienten sowie einer Potenz einer Variable und drei Dezimalbrüchen als Summanden mit Potenzen von Variablen
    # h) Klammer mit ganzzahligen Koeffizienten sowie einer Variable und drei rationalen Summanden mit Potenz einer Variablen und einem weiteren Summanden
    # i) Klammer mit rationalen Koeffizienten sowie einer Potenz einer Variable und drei rationalen Summanden mit Potenzen von Variablen
    # j) Klammer mit rationalen Koeffizienten sowie einer Potenz einer Variable und drei rationalen Summanden mit Potenzen von Variablen und einem weiteren Summanden
    #
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Löse die Klammern auf und fasse ggf. zusammen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def terme_in_klammer(anz, fakt=True, exp=False, liste_mit_exp=False, p=1, q=10):
        liste_exp = [1 for _ in range(anz)]
        liste_exp = exponenten(anz, wdh=True) if exp != False else liste_exp
        if fakt == False:
            liste_fakt = [1 for _ in range(anz)]
        else:
            fakt = random.choice(['nat', 'ganz', 'rat', 'dez']) if fakt not in ['nat', 'ganz', 'rat', 'dez'] else fakt
            if fakt == 'nat':
                liste_fakt = [nzahl(p, q) for _ in range(anz)]
            elif fakt == 'ganz':
                liste_fakt = [nzahl(p, q) for _ in range(anz)]
            elif fakt == 'rat':
                liste_fakt = [Rational(zzahl(p, q), nzahl(p, q)) for _ in range(anz)]
            else:
                liste_fakt = [zzahl(p, 10 * q) / 10 for _ in range(anz)]

        liste_var = random_selection([1, a, b, c, d, e, f, g, h, x, y, z], anzahl=anz, wdh=False)
        if liste_mit_exp == False:
            terme = [[liste_fakt[k], liste_var[k % anz] ** liste_exp[k % anz]] for k in range(anz)]
        else:
            terme = [[liste_fakt[k], liste_var[k % anz], liste_exp[k % anz]] for k in range(anz)]
        return terme

    def aufg_lsg(anz, var_aus, fakt_aus, fakt_in, exp_aus, exp_in, summe=False):
        p, q = 1, 10
        art_fakt = ['vorz', 'nat', 'ganz', 'rat', 'dez']
        fakt_aus = random.choice(art_fakt) if (fakt_aus not in art_fakt) else fakt_aus
        faktoren = {'vorz': random.choice([-1, 1]), 'nat': nzahl(1, 9), 'ganz': zzahl(1, 9),
                    'rat': Rational(zzahl(p, q), nzahl(p, q)), 'dez': zzahl(1, 100) / 10}
        fakt = faktoren[fakt_aus]
        if var_aus == True:
            var_aus = random.choice([a, b, c, d, e, f, g, h, x, y, z])
        else:
            var_aus = 1
        if exp_aus == True:
            exp_aus = nzahl(p, q)
        else:
            exp_aus = 1
        # print(fakt), print(var_aus), print(exp_aus), print(anz)
        if summe == False:
            terme = terme_in_klammer(anz, fakt_in, exp_in)
            ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]] for k in range(anz)]
            # print(ausmulti_terme)
            terme_str = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]))
            for k in range(anz-1):
                terme_str += vorz_v_innen(terme[k+1][0], fakt_var(terme[k+1][1]))
            if var_aus ==1:
                aufg = vorz_v_aussen(fakt,r' \left( ' + terme_str + r' \right) ~')
            else:
                aufg = vorz_v_aussen(fakt,latex(var_aus**exp_aus) + r' \left( ' + terme_str + r' \right) ~')

            lsg = aufg + '~=~' + vorz_v_aussen(ausmulti_terme[0][0],fakt_var(ausmulti_terme[0][1]))
            for k in range(anz-1):
                lsg += vorz_v_innen(ausmulti_terme[k+1][0], fakt_var(ausmulti_terme[k+1][1]))
            return aufg, lsg
        elif summe == 'einf':
            terme = terme_in_klammer(anz, fakt_in, exp_in, True)
            ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]**terme[k][2]] for k in range(anz)]
            ausw = random.choice(range(len(terme)))
            summand = [faktoren[fakt_aus], ausmulti_terme[ausw][1]]
            terme_str = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]**terme[0][2]))
            for k in range(anz - 1):
                terme_str += vorz_v_innen(terme[k + 1][0], fakt_var(terme[k + 1][1]**terme[k + 1][2]))
            if nzahl(1,2) == 1:
                if var_aus == 1:
                    aufg = (vorz_v_aussen(fakt, r' \left( ' + terme_str + r' \right) ~')
                            + vorz_v_innen(summand[0],fakt_var(summand[1])))
                else:
                    aufg = (vorz_v_aussen(fakt, latex(var_aus ** exp_aus) + r' \left( ' + terme_str + r' \right) ~')
                            + vorz_v_innen(summand[0],fakt_var(summand[1])))
                lsg_zw = vorz_v_aussen(ausmulti_terme[0][0], fakt_var(ausmulti_terme[0][1]))
                for k in range(anz - 1):
                    lsg_zw += vorz_v_innen(ausmulti_terme[k + 1][0], fakt_var(ausmulti_terme[k + 1][1]))
                lsg_zw += vorz_v_innen(summand[0],fakt_var(summand[1]))
            else:
                if var_aus == 1:
                    aufg = (vorz_v_aussen(summand[0],fakt_var(summand[1]))
                            + vorz_v_innen(fakt, r' \left( ' + terme_str + r' \right) ~'))
                else:
                    aufg = (vorz_v_aussen(summand[0],fakt_var(summand[1]))
                            + vorz_v_innen(fakt, latex(var_aus ** exp_aus) + r' \left( ' + terme_str + r' \right) ~'))
                lsg_zw = vorz_v_aussen(summand[0],fakt_var(summand[1]))
                for k in range(anz):
                    lsg_zw += vorz_v_innen(ausmulti_terme[k][0], fakt_var(ausmulti_terme[k][1]))
            terme_erg = ausmulti_terme.copy()
            terme_erg[ausw][0] = ausmulti_terme[ausw][0] + summand[0]
            lsg = aufg + '~=~' + lsg_zw + '~=~' + vorz_v_aussen(terme_erg[0][0], fakt_var(terme_erg[0][1]))
            for k in range(anz - 1):
                lsg += vorz_v_innen(terme_erg[k + 1][0], fakt_var(terme_erg[k + 1][1]))
            return aufg, lsg
        else:
            aufg = ''
            lsg = ''
            return aufg, lsg

    if anzahl != False:
        exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.") if type(anzahl) != int or anzahl > 26 else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
    wb = {'a': [2, False, 'nat', False, False, False, False],
          'b': [2, False, 'vorz', 'ganz', False, False, False],
          'c': [2, False, 'ganz', False, False, False, False],
          'd': [2, False, 'ganz', 'ganz', False, False, False],
          'e': [2, True, 'ganz', 'ganz', False, False, 'einf'],
          'f': [2, True, 'ganz', random.choice(['rat', 'dezi']), False, False, False],
          'g': [3, True, 'ganz', 'dezi', True, True, False],
          'h': [2, True, 'ganz', 'dezi', False, True, 'einf'],
          'i': [2, True, 'rat', 'rat', True, True, False],
          'j': [3, True, 'rat', 'rat', False, True, 'einf']}

    aufg = ''
    lsg = ''
    punkte = 0
    for st in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufg_lsg(wb[st][0], wb[st][1], wb[st][2], wb[st][3],
                                               wb[st][4], wb[st][5], wb[st][6])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i+1) % 3 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif i+1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def terme_ausklammern(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS aus verschiedene Summen von Terme ausklammern
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) eine natürliche Zahl aus zwei Summanden ausklammern, z.b. 8x+8y = 8(x+y)
    # b) eine nat. Zahl und eine Variable aus zwei Summanden ausklammern, z.b. 14ax+6ay = 2a(7x+3y)
    # c) eine nat. Zahl und Variable ausklammern aus einer Potenz aus zwei Summanden ausklammern, z.b. 14ab²+6a²c = 2a(7b²+3ac)
    # d) eine ganze Zahl und die Potenz einer Variablen aus zwei Summanden ausklammern, z.b. 14a²b²+6a³c = 2a²(7b²+3ac)
    # e) eine ganze Zahl und die Potenz einer Variablen aus drei Summanden ausklammern
    # f) eine ganze Zahl und eine Variable im Zähler eines Bruchs ausklammern und dann mit dem Nenner kürzen
    # g) eine ganze Zahl und die Potenz einer Variablen im Zähler eines Bruchs ausklammern und dann mit dem Nenner kürzen
    # h) eine ganze Zahl und die Potenz einer Variablen im Zählern eines Bruchs, der aus rationalen Brüchen besteht, ausklammern und dann mit dem Nenner kürzen
    # i) eine rationale Zahl und die Potenz einer Variablen im Zählern eines Bruchs, der aus rationalen Brüchen besteht, ausklammern und dann mit dem Nenner kürzen
    #
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    if len([element for element in ['f', 'g', 'h', 'i'] if element in teilaufg]) > 0:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Klammere alle möglichen gemeinsamen Faktoren aus und kürze gegebenenfalls.']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Klammere alle möglichen gemeinsamen Faktoren aus.']

    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def terme_in_klammer(anz, fakt=True, exp=False, p=1, q=10):
        liste_exp = [1 for _ in range(anz)]
        liste_exp = exponenten(anz, wdh=True) if exp != False else liste_exp
        if fakt == False:
            liste_fakt = [1 for _ in range(anz)]
        else:
            fakt = random.choice(['nat', 'ganz', 'rat', 'dez']) if fakt not in ['nat', 'ganz', 'rat', 'dez'] else fakt
            if fakt == 'nat':
                liste_fakt = [nzahl(p, q) for _ in range(anz)]
            elif fakt == 'ganz':
                liste_fakt = [nzahl(p, q) for _ in range(anz)]
            elif fakt == 'rat':
                liste_fakt = [Rational(zzahl(p, q), nzahl(p, q)) for _ in range(anz)]
            else:
                liste_fakt = [zzahl(p, 10 * q) / 10 for _ in range(anz)]

        liste_var = random_selection([1, a, b, c, d, e, f, g, h, x, y, z], anzahl=anz, wdh=False)
        terme = [[liste_fakt[k], liste_var[k % anz] ** liste_exp[k % anz]] for k in range(anz)]
        return terme

    def aufg_lsg(anz, var_aus, fakt_aus, fakt_in, exp_aus, exp_in, bruch=False):
        p, q = 2, 10
        art_fakt = ['nat', 'ganz', 'rat', 'dez']
        fakt_aus = random.choice(art_fakt) if (fakt_aus not in art_fakt) else fakt_aus
        faktoren = {'nat': nzahl(2, 9), 'ganz': zzahl(2, 9),
                    'rat': Rational(zzahl(p, q), nzahl(p, q)), 'dez': zzahl(1, 100) / 10}
        fakt = faktoren[fakt_aus]
        if var_aus == True:
            var_aus = random.choice([a, b, c, d, e, f, g, h, x, y, z])
        else:
            var_aus = 1
        if exp_aus == True:
            exp_aus = nzahl(p, q)
        else:
            exp_aus = 1
        var_str = latex(var_aus ** exp_aus)
        # print(fakt), print(var_aus), print(exp_aus), print(anz)
        if bruch == False:
            terme = terme_in_klammer(anz, fakt_in, exp_in)
            ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]] for k in range(anz)]
            # print(ausmulti_terme)
            aufg = '~' + vorz_v_aussen(ausmulti_terme[0][0],fakt_var(ausmulti_terme[0][1]))
            for k in range(anz-1):
                aufg += vorz_v_innen(ausmulti_terme[k+1][0], fakt_var(ausmulti_terme[k+1][1]))
            terme_str = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]))
            for k in range(anz-1):
                terme_str += vorz_v_innen(terme[k+1][0], fakt_var(terme[k+1][1]))
            if var_aus == 1:
                lsg = aufg + '~=~' + vorz_v_aussen(fakt, r' \left( ' + terme_str + r' \right)')
            else:
                lsg = aufg + '~=~' + vorz_v_aussen(fakt, var_str + r' \left( ' + terme_str + r' \right)')
            return aufg, lsg
        elif bruch == 'einf':
            terme = terme_in_klammer(anz, fakt_in, exp_in)
            ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]] for k in range(anz)]
            terme_str = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]))
            nenner = vorz_v_aussen(ausmulti_terme[0][0],fakt_var(ausmulti_terme[0][1]))
            for k in range(anz-1):
                nenner += vorz_v_innen(ausmulti_terme[k+1][0], fakt_var(ausmulti_terme[k+1][1]))
            aufg = r' \frac{~' + nenner + '~}{' + gzahl(fakt * var_aus**exp_aus) + '}'
            klammer_str = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]))
            for k in range(anz-1):
                klammer_str += vorz_v_innen(terme[k+1][0], fakt_var(terme[k+1][1]))
            if var_aus == 1:
                lsg_zw = (r' \frac{' + vorz_v_aussen(fakt, r' \left( ' + klammer_str + r' \right)')
                          + '~}{' + gzahl(fakt) + '}')
                lsg = aufg + '~=~' + lsg_zw + r'~=~ \left( ' + klammer_str + r' \right)'
            else:
                lsg_zw = (r' \frac{' + vorz_v_aussen(fakt, var_str + r' \left( ' + klammer_str + r' \right) ~')
                          + '~}{' + gzahl(fakt*var_aus**exp_aus) + '}')
                lsg = (aufg + '~=~' + lsg_zw + r'~=~ \left( ' + klammer_str + r' \right)')
            return aufg, lsg
        else:
            aufg = ''
            lsg = ''
            return aufg, lsg

    if anzahl != False:
        exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.") if type(anzahl) != int or anzahl > 26 else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
    wb = {'a': [2, False, 'nat', False, False, False, False],
          'b': [2, True, 'nat', 'ganz', False, False, False],
          'c': [2, True, 'nat', 'ganz', False, True, False],
          'd': [2, True, 'ganz', 'ganz', True, True, False],
          'e': [3, True, 'ganz', 'ganz', True, True, False],
          'f': [2, True, 'ganz', 'ganz', False, False, 'einf'],
          'g': [2, True, 'ganz', 'ganz', True, True, 'einf'],
          'h': [2, True, 'ganz', 'rat', True, True, 'einf'],
          'i': [3, True, 'rat', 'rat', True, True, 'einf']}

    aufg = ''
    lsg = ''
    punkte = 0
    for st in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufg_lsg(wb[st][0], wb[st][1], wb[st][2], wb[st][3],
                                               wb[st][4], wb[st][5], wb[st][6])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i+1) % 3 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif i+1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def gleichungen(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS aus verschiedene Summen von Terme ausklammern
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Gleichung der Form a * x = b mit ganzen Zahlen
    # b) Gleichung der Form a * x = b mit rationalen Zahlen
    # c) Gleichung der Form a * x + b = c mit ganzen Zahlen
    # d) Gleichung der Form a * x + b = c mit rationalen Zahlen
    # e) Gleichung der Form a * x + b = c * x + d mit ganzen Zahlen
    # f) Gleichung der Form a * x + b = c * x + d mit rationalen Zahlen
    # g) Gleichung der Form a * (b * x + c) = d mit ganzen Zahlen
    # h) Gleichung der Form a * (b * x + c) = d mit rationalen Zahlen
    # i) Gleichung der Form a * (b * x + c) = d * x + e mit ganzen Zahlen
    # j) Gleichung der Form a * (b * x + c) = d * x + e mit rationalen Zahlen
    # k) Gleichung der Form (a * x^2 + b * x)/(c * x) = d mit ganzen Zahlen
    # l) Gleichung der Form (a * x^2 + b * x)/(c * x) = d mit rationalen Zahlen
    # m) Gleichung der Form (a * x^2 + b * x)/(c * x) = d * x + e mit ganzen Zahlen
    # n) Gleichung der Form (a * x^2 + b * x)/(c * x) = d * x + e mit rationalen Zahlen
    #
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Teilaufgaben erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Lösen Sie die folgenden Gleichungen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def gl_fakt(rat=False):
        fakt = zzahl(1,6)
        fakt = Rational(fakt, random.choice([2,4,5,10])) if rat else fakt
        xwert = zzahl(1,9)
        erg = xwert * fakt
        aufg = latex(fakt*x) + '~=~' + gzahl(erg)
        if abs(fakt) < 1:
            lsg = (aufg + r' \quad \vert \cdot ' + gzahl_klammer(Rational(1,fakt)) + r' \quad \to \quad x ~=~'
                   + gzahl(xwert))
        else:
            lsg = (aufg + r' \quad \vert \div ' + gzahl_klammer(fakt) + r' \quad \to \quad x ~=~'
                   + gzahl(xwert))
        return aufg, lsg

    def gl_sum(rat=False):
        fakt = zzahl(1,6)
        fakt = Rational(fakt, random.choice([2,4,5,10])) if rat else fakt
        sum = zzahl(1,5)
        xwert = zzahl(1, 9)
        erg = xwert * fakt + sum
        aufg = latex(fakt*x) + vorz_str(sum) + '~=~' + gzahl(erg)
        if abs(fakt) < 1:
            lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \cdot '
                   + gzahl_klammer(Rational(1,fakt)) + r' \quad \to \quad x ~=~' + gzahl(xwert))
        else:
            lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \div ' + gzahl_klammer(fakt)
                   + r' \quad \to \quad x ~=~' + gzahl(xwert))
        return aufg, lsg

    def gl_sum_beids(rat=False):
        fakt1 = zzahl(1,6)
        fakt1 = Rational(fakt1, random.choice([2,4,5,10])) if rat else fakt1
        fakt2 = fakt1 + zzahl(1,5)
        while fakt2 == 0:
            fakt2 = fakt1 + zzahl(1, 5)
        sum = zzahl(1,5)
        xwert = zzahl(1, 9)
        erg = xwert * (fakt1 - fakt2) + sum
        aufg = latex(fakt1 * x) + vorz_str(sum) + '~=~' + latex(fakt2 * x) + vorz_str(erg)
        if fakt1 > fakt2:
            if abs(fakt1-fakt2) < 1:
                lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * fakt2) + r'x \quad \to \quad '
                       + latex((fakt1 - fakt2)*x) + vorz_str(sum) + r' ~=~' + gzahl(erg)
                       + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \cdot '
                       + gzahl_klammer(Rational(1,(fakt1 - fakt2))) + r' \quad \to \quad x ~=~' + gzahl(xwert))
            else:
                lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * fakt2) + r'x \quad \to \quad '
                       + latex((fakt1-fakt2)*x) + vorz_str(sum) + r' ~=~' + gzahl(erg)
                       + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \div ' + gzahl_klammer(fakt1-fakt2)
                       + r' \quad \to \quad x ~=~' + gzahl(xwert))
        else:
            if abs(fakt2-fakt1) < 1:
                lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * fakt1) + r'x \quad \to \quad ' + gzahl(sum) + r' ~=~'
                       + latex((fakt2 - fakt1)*x) + vorz_str(erg) + r' \quad \vert ' + vorz_str(-1 * erg)
                       + r' \quad \vert \cdot ' + gzahl_klammer(Rational(1,(fakt2 - fakt1)))
                       + r' \quad \to \quad x ~=~' + gzahl(xwert))
            else:
                lsg = (aufg + r' \quad \vert ' + vorz_str(-1 * fakt1) + r'x \quad \to \quad ' + gzahl(sum) + r' ~=~'
                       + latex((fakt2 - fakt1) * x) + vorz_str(erg) + r' \quad \vert ' + vorz_str(-1 * erg)
                       + r' \quad \vert \div ' + gzahl_klammer(fakt2 - fakt1) + r' \quad \to \quad x ~=~'
                       + gzahl(xwert))
        return aufg, lsg

    def gl_term(rat=False):
        fakt1 = zzahl(1, 5)
        fakt2 = zzahl(1,6)
        fakt2 = Rational(fakt2, random.choice([2,4,5,10])) if rat else fakt2
        while fakt2 == 0:
            fakt2 = zzahl(1, 6)
            fakt2 = Rational(fakt2, random.choice([2,4,5,10])) if rat else fakt2
        sum = zzahl(1, 9)
        xwert = zzahl(1,9)
        erg = fakt2 * (fakt1 * xwert + sum)
        aufg = (vorz_v_aussen(fakt2, r' \left( ' + latex(fakt1*x) + vorz_str(sum) + r' \right)')
                + ' ~=~' + gzahl(erg))
        if abs(fakt2 * fakt1) < 1:
            lsg = (aufg + r' \quad \to \quad ' + latex(fakt2 * fakt1 * x) + vorz_str(fakt2 * sum) + '~=~'
                   + gzahl(erg) + r' \quad \vert ' + vorz_str(-1 * fakt2 * sum) + r' \quad \vert \cdot '
                   + gzahl_klammer(Rational(1,(fakt2 * fakt1))) + r' \quad \to \quad x ~=~' + gzahl(xwert))
        else:
            lsg = (aufg + r' \quad \to \quad ' + latex(fakt2 * fakt1 * x) + vorz_str(fakt2 * sum) + '~=~'
                   + gzahl(erg) + r' \quad \vert ' + vorz_str(-1*fakt2*sum) + r' \quad \vert \div '
                   + gzahl_klammer(fakt2 * fakt1) + r' \quad \to \quad x ~=~' + gzahl(xwert))
        return aufg, lsg

    def gl_term_beids(rat=False):
        fakt1 = zzahl(1, 5)
        fakt2 = fakt1 + zzahl(1,5)
        while fakt2 == 0:
            fakt2 = fakt1 + zzahl(1,5)
        fakt3 = zzahl(1,6)
        fakt3 = Rational(fakt3, random.choice([2,4,5,10])) if rat else fakt3
        sum = zzahl(1, 9)
        xwert = zzahl(1,9)
        erg = (fakt3 * fakt1 - fakt2) * xwert + fakt3*sum
        aufg = (vorz_v_aussen(fakt3, r' \left( ' + latex(fakt1 * x) + vorz_str(sum) + r' \right)')
                + ' ~=~' + vorz_v_aussen(fakt2,'x') + vorz_str(erg))
        if fakt1 > fakt2:
            if abs(fakt3*fakt1-fakt2) < 1:
                lsg = (aufg + r' \quad \to \quad ' + latex((fakt3 * fakt1) * x) + vorz_str(fakt3 * sum) + '~=~'
                       + latex(fakt2 * x) + vorz_str(erg) + r' \quad \vert ' + vorz(-1*fakt2) + latex(abs(fakt2) * x)
                       + r' \quad \vert ' + vorz_str(-1 * fakt3 * sum) + r' \quad \vert \cdot '
                       + gzahl_klammer(Rational(1,fakt3*fakt1-fakt2)) + r' \quad \to \quad x ~=~' + gzahl(xwert))
            else:
                lsg = (aufg + r' \quad \to \quad ' + latex((fakt3 * fakt1) * x) + vorz_str(fakt3 * sum) + '~=~'
                       + latex(fakt2 * x) + vorz_str(erg) + r' \quad \vert ' + vorz(-1*fakt2) + latex(abs(fakt2) * x)
                       + r' \quad \vert ' + vorz_str(-1 * fakt3 * sum) + r' \quad \vert \div '
                       + gzahl_klammer(fakt3 * fakt1 - fakt2) + r' \quad \to \quad x ~=~' + gzahl(xwert))
        else:
            if abs(fakt2 - fakt3*fakt1) < 1:
                lsg = (aufg + r' \quad \to \quad ' + latex((fakt3 * fakt1) * x) + vorz_str(fakt3 * sum) + '~=~'
                       + latex(fakt2 * x) + vorz_str(erg) + r' \quad \vert ' + vorz(-1*fakt3*fakt1)
                       + latex(abs(fakt3*fakt1) * x)  + r' \quad \vert ' + vorz_str(-1 * erg) + r' \quad \vert \cdot '
                       + gzahl_klammer(Rational(1,fakt2 - fakt3*fakt1)) + r' \quad \to \quad x ~=~' + gzahl(xwert))
            else:
                lsg = (aufg + r' \quad \to \quad ' + latex((fakt3 * fakt1) * x) + vorz_str(fakt3 * sum) + '~=~'
                       + latex(fakt2 * x) + vorz_str(erg) + r' \quad \vert '+ vorz(-1*fakt3*fakt1)
                       + latex(abs(fakt3*fakt1) * x) + r' \quad \vert ' + vorz_str(-1 * erg) + r' \quad \vert \div '
                       + gzahl_klammer(fakt2 - fakt3 * fakt1) + r' \quad \to \quad x ~=~' + gzahl(xwert))

        return aufg, lsg

    def gl_rat(rat=False):
        fakt1 = zzahl(1, 5)
        fakt1 = Rational(fakt1, random.choice([2,4,5,10])) if rat else fakt1
        fakt2 = zzahl(1, 6)
        fakt2 = Rational(fakt2, random.choice([2, 4, 5, 10]))
        while fakt2 == 0:
            fakt2 = zzahl(1, 6)
            fakt2 = Rational(fakt2, random.choice([2,4,5,10]))
        sum = zzahl(1, 9)
        xwert = zzahl(1, 9)
        erg = fakt1 * xwert + sum
        aufg = (r' \frac{' + (vorz_v_aussen(fakt2 * fakt1,'x^2') + vorz_v_innen(fakt2*sum,'x') + '}{'
                + vorz_v_aussen(fakt2,'x')) + '} ~=~' + gzahl(erg))
        lsg = (aufg + r' \quad \to \quad ' + r' \frac{' + vorz_v_aussen(fakt2,'x') + r' \left( '
               + vorz_v_aussen(fakt1,'x') + vorz_str(sum) + r' \right) ' + '}{' +  vorz_v_aussen(fakt2,'x')
               + '} ~=~' + gzahl(erg) + r' \quad \to \quad ' + vorz_v_aussen(fakt1,'x') + vorz_str(sum) + '~=~'
               + gzahl(erg) + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \div ' + gzahl_klammer(fakt1)
               + r' \quad \to \quad x ~=~' + gzahl(xwert))
        return aufg, lsg

    def gl_rat_beids(rat=False):
        fakt1 = zzahl(1, 5)
        fakt1 = Rational(fakt1, random.choice([2,4,5,10])) if rat else fakt1
        fakt2 = fakt1 + zzahl(1,5)
        while fakt2 == 0:
            fakt2 = fakt1 + zzahl(1, 5)
        fakt3 = zzahl(1, 6)
        fakt3 = Rational(fakt3, random.choice([2,4,5,10])) if rat else fakt3
        sum = zzahl(1, 9)
        xwert = zzahl(1, 9)
        erg = xwert * (fakt1 - fakt2) + sum
        aufg = (r' \frac{' + (vorz_v_aussen(fakt3 * fakt1,'x^2') + vorz_v_innen(fakt3*sum,'x') + '}{'
                + vorz_v_aussen(fakt3,'x')) + '} ~=~' + vorz_v_aussen(fakt2,'x') + vorz_str(erg))
        lsg_1 = (aufg + r' \quad \to \quad ' + r' \frac{' + vorz_v_aussen(fakt3,'x') + r' \left( '
               + vorz_v_aussen(fakt1,'x') + vorz_str(sum) + r' \right) ' + '}{' +  vorz_v_aussen(fakt3,'x')
               + '} ~=~'+ vorz_v_aussen(fakt2,'x') + vorz_str(erg) + r' \\' + vorz_v_aussen(fakt1,'x')
                 + vorz_str(sum) + ' ~=~' + vorz_v_aussen(fakt2,'x') + vorz_str(erg))
        if fakt1 > fakt2:
            lsg = (lsg_1 + r' \quad \vert ' + vorz_str(-1 * fakt2) + r'x \quad \to \quad '
                   + vorz_v_aussen(fakt1-fakt2,'x') + vorz_str(sum) + r' ~=~' + gzahl(erg)
                   + r' \quad \vert ' + vorz_str(-1 * sum) + r' \quad \vert \div ' + gzahl_klammer(fakt1-fakt2)
                   + r' \quad \to \quad x ~=~' + gzahl(xwert))
        else:
            lsg = (lsg_1 + r' \quad \vert ' + vorz_str(-1 * fakt1) + r'x \quad \to \quad ' + gzahl(sum) + r' ~=~'
                   + vorz_v_aussen(fakt2 - fakt1,'x') + vorz_str(erg) + r' \quad \vert ' + vorz_str(-1 * erg)
                   + r' \quad \vert \div ' + gzahl_klammer(fakt2 - fakt1) + r' \quad \to \quad x ~=~' + gzahl(xwert))
        return aufg, lsg

    if anzahl != False:
        exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.") if type(
            anzahl) != int or anzahl > 26 else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
        exit("Die Anzahl der sich wiederholenden Teilaufgaben muss eine Zahl sein und insgesamt nicht mehr als "
             "26 Teilaufgaben ergeben.") if type(wdh) != int or len(teilaufg) > 26 else wdh
    wb = {'a': [gl_fakt, False],
          'b': [gl_fakt, True],
          'c': [gl_sum, False],
          'd': [gl_sum, True],
          'e': [gl_sum_beids, False],
          'f': [gl_sum_beids, True],
          'g': [gl_term, False],
          'h': [gl_term, True],
          'i': [gl_term_beids, False],
          'j': [gl_term_beids, True],
          'k': [gl_rat, False],
          'l': [gl_rat, True],
          'm': [gl_rat_beids, False],
          'n': [gl_rat_beids, True]}


    aufg = ''
    lsg = ''
    punkte = 0
    for st in teilaufg:
        teilaufg_aufg, teilaufg_lsg = wb[st][0](wb[st][1])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i + 1) % 3 != 0 and i + 1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif i + 1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]