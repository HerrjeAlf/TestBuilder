import sympy
from pylatex import MediumText, Tabular, NoEscape, MultiColumn, MultiRow, SmallText
from pylatex.utils import bold

from skripte.funktionen import *
from skripte.plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def begriffe_wahrscheinlichkeit(nr, anzahl=1):
    liste_punkte = [anzahl]
    liste_bez = [f'{nr}']
    i = 0

    anzahl = 6 if anzahl > 6 else anzahl
    begriffe = {r' \mathrm{Zufallsversuch: ~ \hspace{30em}}':
                    r' \mathrm{Zufallsversuch: \quad Ein~Versuch~dessen~Resultat~nicht~vorhersehbar~sind} \quad (1P) \\',
                r' \mathrm{Ergebnis ~ e_i : \hspace{30em}}':
                    r' \mathrm{Ergebnis ~ e_i : \quad Die~möglichen~Resultate~des~Zufallsversuches} \quad (1P) \\',
                r' \mathrm{Ergebnisraum ~ \Omega : \hspace{30em}}':
                    r' \mathrm{Ergebnisraum ~ \Omega : \quad Die~Menge~aller~möglichen~Ergebnisse} \quad (1P) \\',
                r' \mathrm{Ereignis ~ E: \hspace{30em}}':
                    r' \mathrm{Ereignis ~ E: \quad Teilmenge~des~Ergebnisraumes} \quad (1P) \\',
                r' \mathrm{unmögliches~Ereignis: \hspace{30em}}':
                    r' \mathrm{unmögliches~Ereignis: \quad Ergebnisse,~die~nicht~eintreten~können} \quad (1P) \\',
                r' \mathrm{sicheres~Ereignis: \hspace{30em}}':
                    r' \mathrm{sicheres~Ereignis: \quad Ergebnisse~die~immer~eintreten} \quad (1P) \\'}

    auswahl = np.random.choice(list(begriffe.keys()), anzahl, False)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Erläutern Sie die folgenden Grundbegriffe der Wahrscheinlichkeitsrechnung.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    aufg = lsg = ''
    for element in range(anzahl):
        aufg = aufg + auswahl[element]
        if element != range(anzahl)[-1]:
            aufg = aufg + r' \\\\'
        lsg = lsg + begriffe[auswahl[element]]

    lsg = lsg + r' \\ \mathrm{insgesamt~' + str(len(auswahl)) + r'~Punkte}'
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def baumdiagramm_zmZ_und_bernoulli(nr, teilaufg=['a', 'b', 'c', 'd'], stufen=None):
    liste_punkte = []
    liste_bez = []
    i = 0

    if stufen == None:
        anzahl_ziehen = random.choice([[2, 'zweimal'], [3, 'dreimal']])
    elif stufen == 2:
        anzahl_ziehen = [2, 'zweimal']
    elif stufen == 3:
        anzahl_ziehen = [3, 'dreimal']
    else:
        exit("anzahl_ziehen muss None, 2 oder 3 sein")

    farben = ['Weiss', 'Schwarz', 'Blau', 'Rot', 'Gelb']
    farben_kuerzel = [str(farben[i])[0] for i in range(len(farben))]
    auswahl_farbe = np.random.choice([0, 1, 2, 3, 4], 2, False)
    farbe_1 = farben[auswahl_farbe[0]]
    anzahl_1 = nzahl(5, 15)
    farbe_2 = farben[auswahl_farbe[1]]
    anzahl_2 = 20 - anzahl_1

    ergebnisraum = ergebnisraum_zmZ(anzahl_ziehen[0],
                                    farbe1=farben_kuerzel[auswahl_farbe[0]],
                                    farbe2=farben_kuerzel[auswahl_farbe[1]])
    # zwischenergebnisse für teilaufgaben
    anzahl_kugel_E1 = nzahl(1, 2)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Urne befinden sich {anzahl_1} Kugeln der Farbe {farbe_1} und {anzahl_2}'
               f' Kugeln der Farbe {farbe_2}. Aus dieser Urne wird {anzahl_ziehen[1]}'
               f' eine Kugel gezogen und anschließend wieder zurückgelegt. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        Baumdiagramm_zmZ(anzahl_ziehen[0], Rational(anzahl_1,20) ,f'Loesung_{nr}{liste_teilaufg[i]}',
                         bz=farben_kuerzel[auswahl_farbe[0]], bz2=farben_kuerzel[auswahl_farbe[1]])
        aufgabe.append(str(liste_teilaufg[i]) + ') Zeichnen Sie das Baumdiagramm für diesen Versuch. \n\n')
        if anzahl_ziehen[0] == 2:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '2 Stufen: 1P, Wkt an den Zweige: 1P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 3
        else:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '3 Stufen: 2P, Wkt an den Zweige: 1P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 4

        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        punkte = 4
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
            lsg = darstellung_mengen(lsg_menge)
            return text, lsg_menge, lsg

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
            lsg = darstellung_mengen(lsg_menge)
            return text, lsg_menge, lsg

        ereignis_1, lsg_menge_1, lsg_1 = ereig_1(anzahl_kugel_E1)
        ereignis_2, lsg_menge_2, lsg_2 = ereig_2()

        def vereinigung():
            text = r' \mathrm{E_1 \cup E_2}'
            lsg_menge = lsg_menge_1.copy()
            for element2 in lsg_menge_2:
                if element2 not in lsg_menge:
                    lsg_menge.append(element2)
            lsg = darstellung_mengen(lsg_menge)
            return text, lsg_menge, lsg

        def geschnitten():
            text = r' \mathrm{E_1 \cap E_2}'
            lsg_menge = []
            for element1 in lsg_menge_1:
                for element2 in lsg_menge_2:
                    if element2 == element1:
                        lsg_menge.append(element2)
            lsg = darstellung_mengen(lsg_menge)
            return text, lsg_menge, lsg

        vereinigung, lsg_menge_vereinigung, lsg_vereinigung = vereinigung()
        schnittmenge, lsg_menge_schnittmenge, lsg_schnittmenge = geschnitten()

        aufgabe.extend((str(liste_teilaufg[i]) + f')  Geben Sie die Ergebnismenge der folgenden Ereignisse an.',
                        r' E_1: ' + ereignis_1 + r', \quad E_2: ' + ereignis_2 + r', \quad '
                        + vereinigung + r' \quad \mathrm{und} \quad ' + schnittmenge))

        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{1cm} p{8cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Ergebnismengen'), 'Punkte')
        table1.add_row(MultiColumn(2, align='r', data='E1: '), str(lsg_1), '1P')
        table1.add_row(MultiColumn(2, align='r', data='E2: '), str(lsg_2), '1P')
        table1.add_row(MultiColumn(2, align='r', data= NoEscape(r'$E1 \cup E2: $')),
                       str(lsg_vereinigung), '1P')
        table1.add_row(MultiColumn(2, align='r', data= NoEscape(r'$E1 \cap E2: $')),
                       str(lsg_schnittmenge), '1P')
        table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)
        loesung.append(' \n\n\n')
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        def aufgabe_1():
            auswahl = random.choice([farbe_1, farbe_2])
            if auswahl == farbe_1:
                auswahl_anzahl = anzahl_1
            else:
                auswahl_anzahl = anzahl_2
            punkte = 2
            aufgabe_text = (r' \mathrm{Die~erste~Kugel~ist~' + auswahl + r'.} \hspace{12em}')
            aufgabe_loesung = (r' \frac{' + gzahl(auswahl_anzahl) + '}{20} ~=~'
                               + gzahl(auswahl_anzahl / 20 * 100) + r' \% \quad (2P)')
            return aufgabe_text, aufgabe_loesung, punkte

        def aufgabe_2():
            if anzahl_ziehen[0] == 2:
                aufgabe_text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbe_2 + r'~wird~mind.~einmal~gezogen.}')
                aufgabe_loesung = (r' \left( \frac{' + gzahl(anzahl_2) + r'}{20} \right)^2 '
                                   + r'2 \cdot \frac{' + gzahl(anzahl_2)
                                   + r' \cdot ' + gzahl(anzahl_1) + r'}{20^2} ~=~ '
                                   + gzahl(N((anzahl_2**2 + 2 * anzahl_2 * anzahl_1)*100 / (20**2), 3))
                                   + r' \% \quad (3P)')
                punkte = 3
            else:
                aufgabe_text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbe_2 + r'~wird~mind.~zweimal~gezogen.}')
                aufgabe_loesung = (r' \left( \frac{' + gzahl(anzahl_2) + r'}{20} \right)^3 + 3 \cdot \frac{'
                                   + gzahl(anzahl_2) + r'^2 \cdot ' + gzahl(anzahl_1) + r'}{20^3} ~=~ '
                                   + gzahl(N((anzahl_2**3 + 3*(anzahl_2**2)*anzahl_1)*100/20**3,3))
                                   + r' \% \quad (4P)')
                punkte = 4
            return aufgabe_text, aufgabe_loesung, punkte

        auswahl = np.random.choice([aufgabe_1, aufgabe_2], 2, False)
        aufgabe_1, aufgabe_lsg_1, punkte_1 = auswahl[0]()
        aufgabe_2, aufgabe_lsg_2, punkte_2 = auswahl[1]()
        punkte = punkte_1 + punkte_2

        aufgabe.extend((str(liste_teilaufg[i]) + (') Berechnen Sie die Wahrscheinlichkeit für'
                        + ' die folgenden Ereignisse.'), r' \mathrm{ \quad E_3: \quad }' + aufgabe_1
                        + r' \\ \mathrm{ \quad E_4: \quad }' + aufgabe_2))
        loesung.extend((str(liste_teilaufg[i]) + ') Berechnung der Wahrscheinlichkeiten der angegebenen Ereignisse',
                        r' \quad P(E_3) ~=~' + aufgabe_lsg_1 + r' \\ \quad P(E_4) ~=~' + aufgabe_lsg_2))

        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        anzahl_n = random.choice([25,50,75,100])
        anzahl_k = int((anzahl_1+zzahl(1,2))/20*anzahl_n)
        wkt = Rational(anzahl_1,20)

        aufgabe.extend((f'Diesmal wird {anzahl_n} mal eine Kugel mit Zurücklegen gezogen. \n\n',
                        str(liste_teilaufg[i]) + f') Berechnen Sie die Wahrscheinlichkeit, dass {farbe_1} '
                        + f'genau {gzahl(anzahl_k)} mal gezogen wird. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad P(X=' + gzahl(anzahl_k) + ') ~=~'
                       + r' \begin{pmatrix} ' + gzahl(anzahl_n) + r' \\' + gzahl(anzahl_k) + r' \\'
                       + r' \end{pmatrix} \cdot \left(' + gzahl(wkt) + r' \right)^{' + gzahl(anzahl_k) + r'} \cdot \left( '
                       + gzahl(1-wkt) + r' \right) ^{' + gzahl(anzahl_n-anzahl_k) + '} ~=~ '
                       + gzahl(N(binomial(anzahl_n,anzahl_k) * wkt**anzahl_k*(1-wkt)**(anzahl_n-anzahl_k),3)*100)
                       + r' \% \quad (4P) \\')

        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        pass # hier noch eine Aufgabe zur kummulierten Binomialverteilung einfügen

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def baumdiagramm_zoZ(nr, teilaufg=['a', 'b', 'c']):
    liste_punkte = []
    liste_bez = []
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
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        Baumdiagramm_zoZ(anzahl_ziehen[0], anzahl_1, anzahl_2, f'Loesung_{nr}{liste_teilaufg[i]}',
                         bz1=farben_kuerzel[auswahl_farbe[0]], bz2=farben_kuerzel[auswahl_farbe[1]])
        aufgabe.append(str(liste_teilaufg[i]) + ') Zeichnen Sie das Baumdiagramm für diesen Versuch. \n\n')
        if anzahl_ziehen[0] == 2:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '2 Stufen: 2P, Wkt an den Zweige: 2P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 5
        else:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '3 Stufen: 2P, Wkt an den Zweige: 3P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 6

        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        punkte = 6
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
            # print(lsg_menge)
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

        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{3cm} p{8cm} p{2cm}')
        table1.add_row(str(teilaufg[i]) + ')', MultiColumn(2, align='c', data='Die Ergebnismengen'), 'Punkte')
        table1.add_row(MultiColumn(2, align='r', data='E1: '), str(lsg_menge_1), '2P')
        table1.add_row(MultiColumn(2, align='r', data='E2: '), str(lsg_menge_2), '2P')
        table1.add_row(MultiColumn(2, align='r', data= NoEscape(r'$E1 \cup E2: $')),
                       str(lsg_vereinigung), '1P')
        table1.add_row(MultiColumn(2, align='r', data= NoEscape(r'$E1 \cap E2: $')),
                       str(lsg_schnittmenge), '1P')
        table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)
        loesung.append(' \n\n\n')
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
        punkte = punkte_1 + punkte_2

        aufgabe.extend((str(liste_teilaufg[i]) + (') Berechnen Sie die Wahrscheinlichkeit für'
                        + ' die folgenden Ereignisse.'), r' \mathrm{ \quad E_3: \quad }' + aufgabe_1
                        + r' \mathrm{ \quad E_4: \quad }' + aufgabe_2))
        loesung.extend((str(liste_teilaufg[i]) + ') Berechnung der Wahrscheinlichkeiten der angegebenen Ereignisse',
                        r' \quad P(E_3) ~=~' + aufgabe_lsg_1 + r' \quad P(E_4) ~=~' + aufgabe_lsg_2))

        liste_punkte.append(punkte)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def vierfeldertafel_01(nr, teilaufg=['a', 'b', 'c'], vierfeldertafel=True):
    liste_punkte = []
    liste_bez = []
    i = 0

    A = int(nzahl(10,20) * 100)
    M = int(nzahl(6,8)/10 * A)
    P = int(A-M)
    M_H = int(nzahl(3,7)/10 * M)
    P_H = int(nzahl(1,3)/10 * P)
    H = int(M_H + P_H)
    M_nH = int(M - M_H)
    P_nH = int(P - P_H)
    nH = int(M_nH + P_nH)

    def Tabelle(A='', M='', P='', M_H='', P_H='', H='', M_nH='', P_nH='', nH=''):
        table1 = Tabular('p{0.3cm} | p{2cm} | p{2cm} | p{0.7cm} p{1cm} p{3cm}')
        table1.add_row('', 'H', NoEscape(r'$ \mathrm{ \overline{H} }$'), '', '', 'M: Medikament')
        table1.add_hline(1, 4)
        table1.add_row('M', M_H, M_nH, M, '', 'P: Placebo')
        table1.add_hline(1, 4)
        table1.add_row('P', P_H, P_nH, P, '', 'H: geheilt')
        table1.add_hline(1, 4)
        table1.add_row('', H, nH, A, '', NoEscape(r'$ \mathrm{ \overline{H}: } $ nicht geheilt '))
        return table1

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In Phase III einer klinischen Doppelblindstudie wird die Wirksamkeit eines neuen Medikaments '
               f'untersucht. An dieser Studie nahmen insgesamt {gzahl(A)} Personen teil. Davon sind {gzahl(P)} '
               f'Personen Teil einer Vergleichsgruppe, die ein Placebo erhalten. '
               f'Am Ende der Studie wurde festgestellt, dass insgesamt {gzahl(H)} Personen, '
               f'aber in der \n Vergleichsgruppe nur {gzahl(P_H)} Personen geheilt wurden. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if vierfeldertafel == True:
            punkte = 3
            aufgabe.extend((Tabelle(A=A, P=P, P_nH=P_nH, H=H),' \n\n\n',
                            str(liste_teilaufg[i]) + f')  Vervollständigen Sie die obere Vierfeldertafel. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + f') Tabelle wie unten ergibt {punkte} P. \n\n',
                            Tabelle(A=A, M=M, P=P, M_H=M_H, P_H=P_H, H=H, M_nH=M_nH, P_nH=P_nH, nH=nH), ' \n\n'))
            liste_punkte.append(punkte)
        else:
            punkte = 6
            aufgabe.extend((Tabelle(),' \n\n\n', str(liste_teilaufg[i]) + f')  Stellen Sie den oberen Sachverhalt '
                            + f'mithilfe der Vierfeldertafel dar. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + f') Tabelle wie unten ergibt {punkte} P. \n\n',
                            Tabelle(A=A, M=M, P=P, M_H=M_H, P_H=P_H, H=H, M_nH=M_nH, P_nH=P_nH, nH=nH), ' \n\n'))
            liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        aufgabe.extend(('Zum Schluss der Studie werden die Heilungschancen beider Gruppen verglichen. '
                        'D.h. die Personen, die ein Medikament erhalten haben mit denjenigen, '
                        'die nur das Placebo erhalten haben. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie die Heilungschancen beider Gruppen '
                        + 'und vergleichen Sie diese. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{P_{M}(H) ~=~ \frac{ \vert M \cap H \vert }'
                       + r'{ \vert M \vert } ~=~ \frac{' + gzahl(M_H) + '}{' + gzahl(M) + '} ~=~ '
                       + gzahl(Rational(M_H,M)) + '~=~' + gzahl(Rational(M_H*100,M))
                       + r' \%  \quad (2P)  \quad und \quad P_{P}(H) = \frac{ \vert P \cap H \vert }'
                       + r'{ \vert P \vert } ~=~ \frac{' + gzahl(P_H) + '}{' + gzahl(P) + '} ~=~ '
                       + gzahl(Rational(P_H,P)) + '~=~' + gzahl(Rational(P_H*100,P))
                       + r' \% \quad (2P) } \\ \mathrm{Die~Gruppe,~welche~die~Medikamente~erhalten~hat,~'
                       + r'hat~eine~höhere~Heilungschance. \quad (1P)} \\'
                       + r'\mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3

        aufgabe.extend(('Ein Patient wurde geheilt und weiß nicht, '
                        + 'ob er das Placebo oder das Medikament erhalten hat. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie die Wahrscheinlichkeit, dass '
                        + 'dieser Patient ein Placebo erhalten hat. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{P_{H}(P) = \frac{' + gzahl(P_H) + '}{'
                       + gzahl(H) + '} ~=~ ' + gzahl(Rational(P_H,H)) + '~=~' + gzahl(N(P_H*100/H,2))
                       + r' \% \quad } \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
