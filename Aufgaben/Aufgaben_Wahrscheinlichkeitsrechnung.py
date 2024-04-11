from pylatex import (MediumText)
from pylatex.utils import bold

from funktionen import *
from plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def ereignisse_ergebnisse(nr, teilaufg):
    i = 0
    farben = ['Weiß', 'Schwarz', 'Blau', 'Rot', 'Gelb']
    farben_kuerzel = [str(farben[i])[0] for i in range(len(farben))]
    auswahl_farbe = np.random.choice([0, 1, 2, 3, 4], 2, False)
    farbe_1 = farben[auswahl_farbe[0]]
    anzahl_1 = nzahl(5, 15)
    farbe_2 = farben[auswahl_farbe[1]]
    anzahl_2 = 20 - anzahl_1
    anzahl_ziehen = random.choice([[2, 'zweimal'], [3, 'dreimal']])
    ergebnisraum = ergebnisraum_zmZ(anzahl_ziehen[0], farbe1=farbe_1, farbe2=farbe_2)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Urne befinden sich {anzahl_1} Kugeln der Farbe {farbe_1} und {anzahl_2}'
               f' Kugeln der Farbe {farbe_2}. Aus dieser Urne wird nun {anzahl_ziehen[1]} eine Kugel gezogen und '
               f'anschließend wieder zurückgelegt. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['', '']
    grafiken_loesung = ['']

    if 'a' in teilaufg:
        punkte_aufg = 6
        liste_punkte.append(punkte_aufg)
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', ''))
        grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', ''))

        def ereig_1():
            anzahl_kugel = nzahl(1, 2)
            if anzahl_kugel == 1:
                text = r' \mathrm{' + latex(farbe_1) + '~wird~einmal~gezogen}'
            else:
                text = r' \mathrm{' + latex(farbe_1) + '~wird~zweimal~gezogen}'
            lsg_menge = []
            for element in ergebnisraum:
                i = 0
                for ergebnis in element:
                    if ergebnis == farbe_1:
                        i += 1
                if i == anzahl_kugel:
                    lsg_menge.append(element)
            print(lsg_menge)
            return text, lsg_menge

        def ereig_2():
            auswahl = random.choice([farbe_1, farbe_2])
            auswahl_kugel = random.choice(['erste', 'zweite'])
            text = r' \mathrm{Die~' + auswahl_kugel + '~Kugel~ist~' + latex(auswahl) + '}'
            lsg_menge = []
            if auswahl_kugel == 'erste':
                for element in ergebnisraum:
                    if element[0] == auswahl:
                        lsg_menge.append(element)
            else:
                for element in ergebnisraum:
                    if element[1] == auswahl:
                        lsg_menge.append(element)
            return text, lsg_menge

        ereignis_1, lsg_menge_1 = ereig_1()
        ereignis_2, lsg_menge_2 = ereig_2()

        def vereinigung():
            text = r' \mathrm{E_1 \cup E_2}'
            lsg_menge = lsg_menge_1.copy()
            for element2 in lsg_menge_2:
                if element2 not in lsg_menge:
                    lsg_menge.append(element2)
            return text, lsg_menge

        def geschnitten():
            text = r' \mathrm{E_1 \cap E_2}'
            lsg_menge = []
            for element1 in lsg_menge_1:
                for element2 in lsg_menge_2:
                    if element2 == element1:
                        lsg_menge.append(element2)
            return text, lsg_menge

        vereinigung, lsg_vereinigung = vereinigung()
        schnittmenge, lsg_schnittmenge = geschnitten()

        aufgabe.extend((str(liste_teilaufg[i]) + f')  Geben Sie die Ergebnismenge der folgenden Ereignisse an.',
                        r' E_1: ' + ereignis_1 + r', \quad E_2: ' + ereignis_2 + r', \quad '
                        + vereinigung + r' \quad \mathrm{und} \quad ' + schnittmenge))
        loesung.append(str(liste_teilaufg[i]) + ') Lösung E1: ' + str(lsg_menge_1) + ' (2P) \n\n'
                       + ' Lösung E2: ' + str(lsg_menge_2) + '(2P) \n\n'
                       + ' Lösung E1 und E2 vereinigt: ' + str(lsg_vereinigung) + ' (1P) \n\n'
                       + ' Lösung E1 und E2 geschnitten: ' + str(lsg_schnittmenge) + ' (1P) \n\n'
                       + ' insgesamt ' + str(punkte_aufg) + ' Punkte \n\n')
        i += 1

    if 'b' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', ''))
        grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', ''))

        auswahl = random.choice([farbe_1, farbe_2])
        if auswahl == farbe_1:
            auswahl_anzahl = anzahl_1
        else:
            auswahl_anzahl = anzahl_2

        aufgabe.extend((str(liste_teilaufg[i]) + ') Berechnen Sie die Wahrscheinlichkeit für'
                                                 ' die folgenden Ereignisse.',
                        r' \mathrm{i) \quad Die~erste~Kugel~ist~' + auswahl + '.}'))
        loesung.extend((str(liste_teilaufg[i])
                        + ') Berechnung der Wahrscheinlichkeiten der angegebenen Ereignisse',
                        r'i)  \quad P(' + auswahl + r') ~=~ \frac{' + gzahl(auswahl_anzahl) + '}{20} ~=~'
                        + gzahl(auswahl_anzahl / 20 * 100) + r' \% \quad (2P) \\'))
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]


def wahrscheinlichkeit_zoZ(nr, teilaufg):
    i = 0
    farben = ['Weiss', 'Schwarz', 'Blau', 'Rot', 'Gelb']
    farben_kuerzel = [str(farben[i])[0] for i in range(len(farben))]
    auswahl_farbe = np.random.choice([0, 1, 2, 3, 4], 2, False)
    farbe_1 = farben[auswahl_farbe[0]]
    anzahl_1 = nzahl(5, 15)
    farbe_2 = farben[auswahl_farbe[1]]
    anzahl_2 = 20 - anzahl_1
    anzahl_ziehen = random.choice([[2, 'zweimal'], [3, 'dreimal']])
    ergebnisraum = ergebnisraum_zoZ(anzahl_ziehen[0], anzahl_1, anzahl_2,
                                    farbe1=farben_kuerzel[auswahl_farbe[0]],
                                    farbe2=farben_kuerzel[auswahl_farbe[1]])
    # zwischenergebnisse für teilaufgaben
    anzahl_kugel_E1 = nzahl(1, 2)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Urne befinden sich {anzahl_1} Kugeln der Farbe {farbe_1} und {anzahl_2}'
               f' Kugeln der Farbe {farbe_2}. Aus dieser Urne wird ohne Zurücklegen {anzahl_ziehen[1]}'
               f' eine Kugel gezogen. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = ['', '']
    grafiken_loesung = ['']

    if 'a' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.extend(('','',f'Loesung_{nr}{liste_teilaufg[i]}'))
        Baumdiagramm_zoZ(anzahl_ziehen[0], anzahl_1, anzahl_2, f'Loesung_{nr}{liste_teilaufg[i]}',
                         bz1=farben_kuerzel[auswahl_farbe[0]], bz2=farben_kuerzel[auswahl_farbe[1]])
        aufgabe.append(str(liste_teilaufg[i]) + ') Zeichnen Sie das Baumdiagramm für diesen Versuch. \n\n')
        if anzahl_ziehen[0] == 2:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '2 Stufen: 2P, Wkt an den Zweige: 2P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte_aufg = 5
        else:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '3 Stufen: 2P, Wkt an den Zweige: 3P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte_aufg = 6

        liste_punkte.append(punkte_aufg)
        i += 1

    if 'b' in teilaufg:
        punkte_aufg = 6
        liste_punkte.append(punkte_aufg)
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', ''))
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        def ereig_1(p):
            if p == 1:
                text = r' \mathrm{' + latex(farbe_1) + '~wird~einmal~gezogen}'
            else:
                text = r' \mathrm{' + latex(farbe_1) + '~wird~zweimal~gezogen}'
            lsg_menge = []
            for element in ergebnisraum:
                i = 0
                for ergebnis in element:
                    if ergebnis == farben_kuerzel[auswahl_farbe[0]]:
                        i += 1
                if i == p:
                    lsg_menge.append(element)
            print(lsg_menge)
            return text, lsg_menge

        def ereig_2():
            auswahl = random.choice([[farbe_1, farben_kuerzel[auswahl_farbe[0]]],
                                     [farbe_2, farben_kuerzel[auswahl_farbe[1]]]])
            auswahl_kugel = random.choice(['erste', 'zweite'])
            text = r' \mathrm{Die~' + auswahl_kugel + '~Kugel~ist~' + latex(auswahl[0]) + '}'
            lsg_menge = []
            if auswahl_kugel == 'erste':
                for element in ergebnisraum:
                    if element[0] == auswahl[1]:
                        lsg_menge.append(element)
            else:
                for element in ergebnisraum:
                    if element[1] == auswahl[1]:
                        lsg_menge.append(element)
            return text, lsg_menge

        ereignis_1, lsg_menge_1 = ereig_1(anzahl_kugel_E1)
        ereignis_2, lsg_menge_2 = ereig_2()

        def vereinigung():
            text = r' \mathrm{E_1 \cup E_2}'
            lsg_menge = lsg_menge_1.copy()
            for element2 in lsg_menge_2:
                if element2 not in lsg_menge:
                    lsg_menge.append(element2)
            return text, lsg_menge

        def geschnitten():
            text = r' \mathrm{E_1 \cap E_2}'
            lsg_menge = []
            for element1 in lsg_menge_1:
                for element2 in lsg_menge_2:
                    if element2 == element1:
                        lsg_menge.append(element2)
            return text, lsg_menge

        vereinigung, lsg_vereinigung = vereinigung()
        schnittmenge, lsg_schnittmenge = geschnitten()

        aufgabe.extend((str(liste_teilaufg[i]) + f')  Geben Sie die Ergebnismenge der folgenden Ereignisse an.',
                        r' E_1: ' + ereignis_1 + r', \quad E_2: ' + ereignis_2 + r', \quad '
                        + vereinigung + r' \quad \mathrm{und} \quad ' + schnittmenge))
        loesung.append(str(liste_teilaufg[i]) + ') Lösung E1: ' + str(lsg_menge_1) + ' (2P) \n\n'
                       + ' Lösung E2: ' + str(lsg_menge_2) + '(2P) \n\n'
                       + ' Lösung E1 und E2 vereinigt: ' + str(lsg_vereinigung) + ' (1P) \n\n'
                       + ' Lösung E1 und E2 geschnitten: ' + str(lsg_schnittmenge) + ' (1P) \n\n'
                       + ' insgesamt ' + str(punkte_aufg) + ' Punkte \n\n')
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.extend((f'Aufgabe_{nr}{liste_teilaufg[i]}', ''))
        grafiken_loesung.extend((f'Loesung_{nr}{liste_teilaufg[i]}', ''))

        def aufgabe_1():
            auswahl = random.choice([farbe_1, farbe_2])
            if auswahl == farbe_1:
                auswahl_anzahl = anzahl_1
            else:
                auswahl_anzahl = anzahl_2
            punkte = 2
            aufgabe_text = (r' \mathrm{Die~erste~Kugel~ist~' + auswahl + r'.} \hspace{12em} \\')
            aufgabe_loesung = (r' \frac{' + gzahl(auswahl_anzahl) + '}{20} ~=~'
                               + gzahl(auswahl_anzahl / 20 * 100) + r' \% \quad (2P) \\')
            return aufgabe_text, aufgabe_loesung, punkte

        def aufgabe_2():
            if anzahl_ziehen[0] == 2:
                aufgabe_text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbe_2 + r'~wird~mind.~einmal~gezogen.} \\')
                aufgabe_loesung = (r' \frac{' + gzahl(anzahl_2) + r'}{20} \cdot \frac{' + gzahl(anzahl_2 - 1)
                                   + r'}{19} + 2 \cdot \frac{' + gzahl(anzahl_2)
                                   + r' \cdot ' + gzahl(anzahl_1) + r'}{20 \cdot 19} ~=~ '
                                   + gzahl(
                            N((anzahl_2 * (anzahl_2 - 1) + 2 * anzahl_2 * anzahl_1) * 100 / (20 * 19), 3))
                                   + r' \% \quad (3P) \\')
                punkte = 3
            else:
                aufgabe_text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbe_2 + r'~wird~mind.~zweimal~gezogen.} \\')
                aufgabe_loesung = (r' \frac{' + gzahl(anzahl_2) + r'}{20} \cdot \frac{' + gzahl(anzahl_2 - 1)
                                   + r'}{19} \cdot \frac{' + gzahl(anzahl_2 - 2) + r'}{18} + 3 \cdot \frac{'
                                   + gzahl(anzahl_2) + r' \cdot ' + gzahl(anzahl_2 - 1) + r' \cdot '
                                   + gzahl(anzahl_1) + r'}{20 \cdot 19 \cdot 18} ~=~ '
                                   + gzahl(N((anzahl_2 * (anzahl_2 - 1) * (anzahl_2 - 2)
                                              + 3 * anzahl_2 * (anzahl_2 - 1) * anzahl_1) * 100 / (20 * 19 * 18), 3))
                                   + r' \% \quad (4P) \\')
                punkte = 4
            return aufgabe_text, aufgabe_loesung, punkte

        auswahl = np.random.choice([aufgabe_1, aufgabe_2], 2, False)
        aufgabe_1, aufgabe_lsg_1, punkte_1 = auswahl[0]()
        aufgabe_2, aufgabe_lsg_2, punkte_2 = auswahl[1]()
        punkte_aufg = punkte_1 + punkte_2

        aufgabe.extend((str(liste_teilaufg[i]) + (') Berechnen Sie die Wahrscheinlichkeit für'
                                                  ' die folgenden Ereignisse.'),
                        r' \mathrm{ \quad E_3: \quad }' + aufgabe_1
                        + r' \mathrm{ \quad E_4: \quad }' + aufgabe_2))
        loesung.extend((str(liste_teilaufg[i]) + ') Berechnung der Wahrscheinlichkeiten der angegebenen Ereignisse',
                        r' \quad P(E_3) ~=~' + aufgabe_lsg_1
                        + r' \quad P(E_4) ~=~' + aufgabe_lsg_2))

        liste_punkte.append(punkte_aufg)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]