from pylatex import (MediumText)
from pylatex.utils import bold

from funktionen import *
from plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0


def ereignisse_ergebnisse(nr, teilaufg):
    liste_punkte = []
    liste_bez = []
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

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
