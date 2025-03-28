import random
import sympy, sys
import string
from sympy.stats import Binomial, P
from scipy.stats import norm
from pylatex import MediumText, Tabular, NoEscape, MultiColumn, MultiRow, SmallText
from pylatex.utils import bold
from skripte.funktionen import *
from skripte.plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

def begriffe_wahrscheinlichkeit(nr, anzahl=1, BE=[]):
    # Grundbegriffe der Wahrscheinlichkeitsrechnung erläutern
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    i = 0
    begriffe = {r' \mathrm{Zufallsversuch: ~ \hspace{30em}}':
                    r' \mathrm{Zufallsversuch: \quad Ein~Versuch~dessen~Resultat~nicht~vorhersehbar~sind} \quad (1BE) \\',
                r' \mathrm{Ergebnis ~ e_i : \hspace{30em}}':
                    r' \mathrm{Ergebnis ~ e_i : \quad Die~möglichen~Resultate~des~Zufallsversuches} \quad (1BE) \\',
                r' \mathrm{Ergebnisraum ~ \Omega : \hspace{30em}}':
                    r' \mathrm{Ergebnisraum ~ \Omega : \quad Die~Menge~aller~möglichen~Ergebnisse} \quad (1BE) \\',
                r' \mathrm{Ereignis ~ E: \hspace{30em}}':
                    r' \mathrm{Ereignis ~ E: \quad Teilmenge~des~Ergebnisraumes} \quad (1BE) \\',
                r' \mathrm{unmögliches~Ereignis: \hspace{30em}}':
                    r' \mathrm{unmögliches~Ereignis: \quad Ergebnisse,~die~nicht~eintreten~können} \quad (1BE) \\',
                r' \mathrm{sicheres~Ereignis: \hspace{30em}}':
                    r' \mathrm{sicheres~Ereignis: \quad Ergebnisse~die~immer~eintreten} \quad (1BE) \\'}

    anzahl = len(begriffe) if anzahl > len(begriffe) else anzahl
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [len(anzahl)]
        liste_punkte = BE
    else:
        liste_punkte = [len(anzahl)]
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

def baumdiagramm(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], stufen=None, art='zmZ', pruef_kl10=False, neue_seite=None, i=0, BE=[]):
    # Hier sollen die Schüler und Schülerinnen am Urnenmodell verschiedene Berechnungen durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "stufen=" kann festgelegt werden, wie viele Stufen das Baumdiagramm haben soll. Standardmäßig ist "stufen=None" und es wird zufällig zwischen zwei und drei Stufen ausgewählt. Es kann auch "stufen=2" und "stufen=3" gewählt werden.
    # Mit dem Parameter "art=" kann festgelegt werden, welche Art von Ziehung beim Baumdiagramm vorliegt. Standardmäßig ist "art=zmz" Ziehen mit Zurücklegen ausgewählt. Es kann auch "art=zoz" (Ziehen ohne Zurücklegen) ausgewählt werden.
    # Ist der Parameter "pruef_kl10=True" dann wird unter der Teilaufgabe ein Notizfeld für die Berechnungen angezeigt. Standardmäßig idst "pruef_kl10=False" und es wird kein Notizfeld unter der Teilaufgabe angezeigt.
    # Mit dem Parameter "neue_seite_nach_teilaufg=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    if art not in ['zmZ', 'zoZ']:
        exit("art muss 'zmZ' oder 'zoZ' sein!")
    if stufen == None:
        anzahl_ziehen = random.choice([[2, 'zweimal'], [3, 'dreimal']])
        stufen = anzahl_ziehen[0]
    elif stufen == 2:
        anzahl_ziehen = [2, 'zweimal']
    elif stufen == 3:
        anzahl_ziehen = [3, 'dreimal']
    else:
        exit("anzahl_ziehen muss None, 2 oder 3 sein")

    farben = ['Weiß', 'Schwarz', 'Blau', 'Rot', 'Gelb']
    farben_kuerzel = [str(farben[i])[0] for i in range(len(farben))]
    auswahl_farbe = np.random.choice([0, 1, 2, 3, 4], 2, False)
    farbe_1 = farben[auswahl_farbe[0]]
    farben_kuerzel_1 = farben_kuerzel[auswahl_farbe[0]]
    anzahl_1 = nzahl(5, 15)
    farbe_2 = farben[auswahl_farbe[1]]
    farben_kuerzel_2 = farben_kuerzel[auswahl_farbe[1]]
    anzahl_2 = 20 - anzahl_1
    if art == 'zoZ':
        ergebnisraum = ergebnisraum_zoZ(anzahl_ziehen[0], anzahl_1, anzahl_2, farbe1=farben_kuerzel_1,
                                        farbe2=farben_kuerzel_2)
    else:
        ergebnisraum = ergebnisraum_zmZ(anzahl_ziehen[0], farbe1=farben_kuerzel_1, farbe2=farben_kuerzel_2)
    # zwischenergebnisse für teilaufgaben
    anzahl_n = anzahl_1 + nzahl(2, 3)
    anzahl_k = anzahl_1 - nzahl(1, 2)
    if anzahl_n - anzahl_k > anzahl_2:
        anzahl_k = anzahl_n - anzahl_2

    # Werte für Aufgabe e, f und g
    x_werte = []
    y_werte = []
    ew_wert = 0
    ew_wert_str = ''

    def auswahl():
        auswahl = random.choice([[farbe_1, farben_kuerzel_1],
                                 [farbe_2, farben_kuerzel_2]])
        return auswahl[0], auswahl[1]

    # definieren der Ereignisse
    def ereig_1():
        p = 1
        p = random.choice([1,2]) if anzahl_ziehen[0] == 3 else p
        if p == 1:
            text = r' \mathrm{' + latex(farbe_1) + '~wird~einmal~gezogen.}'
        elif p == 2:
            text = r' \mathrm{' + latex(farbe_1) + '~wird~zweimal~gezogen.}'
        lsg_menge = []
        for element in ergebnisraum:
            i = 0
            for ergebnis in element:
                if ergebnis == farben_kuerzel_1:
                    i += 1
            if i == p:
                lsg_menge.append(element)
        wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                             anz1=anzahl_1, anz2=anzahl_2,art=art)
        lsg = darstellung_mengen(lsg_menge)
        return text, lsg_menge, lsg, wkt, wkt_str, pkt

    def ereig_2():
        farbwahl, kuerzelwahl = auswahl()
        auswahl_kugel = random.choice(['erste', 'zweite'])
        # auswahl_kugel = 'erste'
        text = r' \mathrm{Die~' + auswahl_kugel + '~Kugel~ist~' + latex(farbwahl) + '.}'
        lsg_menge = []
        if auswahl_kugel == 'erste':
            for element in ergebnisraum:
                if element[0] == kuerzelwahl:
                    lsg_menge.append(element)
        else:
            for element in ergebnisraum:
                if element[1] == kuerzelwahl:
                    lsg_menge.append(element)
        wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                             anz1=anzahl_1, anz2=anzahl_2,art=art)
        lsg = darstellung_mengen(lsg_menge)
        return text, lsg_menge, lsg, wkt, wkt_str, pkt

    def ereig_3():
        farbwahl, kuerzelwahl = auswahl()
        if stufen == 2:
            text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbwahl + r'~wird~mind.~einmal~gezogen.}')
            p = 1
        elif stufen == 3:
            text = (r' \mathrm{Die~Kugel~der~Farbe~' + farbwahl +r'~wird~mind.~zweimal~gezogen.}')
            lsg_menge = ergebnisraum.copy()
            p = 2
        lsg_menge = []
        for element in ergebnisraum:
            i = 0
            for ergebnis in element:
                if ergebnis == kuerzelwahl:
                    i += 1
            if i >= p:
                lsg_menge.append(element)
        wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                             anz1=anzahl_1, anz2=anzahl_2,art=art)
        lsg = darstellung_mengen(lsg_menge)
        return text, lsg_menge, lsg, wkt, wkt_str, pkt


    # Auswahl für Aufgabe b, c und d
    ereignis_1, menge_1, lsg_1, wkt1, wkt1_str, pkt1 = ereig_1()
    ereignis_2, menge_2, lsg_2, wkt2, wkt2_str, pkt2 = random.choice([ereig_2(), ereig_3()])

    def vereinigung(menge1, menge2, bez1='E_1', bez2='E_2'):
        text = r' \mathrm{' + bez1 + r' \cup ' + bez2 + '}'
        lsg_menge = menge1.copy()
        for element2 in menge2:
            if element2 not in lsg_menge:
                lsg_menge.append(element2)
        wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                             anz1=anzahl_1, anz2=anzahl_2,art=art)
        lsg = darstellung_mengen(lsg_menge)
        return text, lsg_menge, lsg, wkt, wkt_str, pkt

    def geschnitten(menge1, menge2, bez1='E_1', bez2='E_2'):
        text = r' \mathrm{' + bez1 + r' \cap ' + bez2 + '}'
        lsg_menge = []
        for element1 in menge1:
            for element2 in menge2:
                if element2 == element1:
                    lsg_menge.append(element2)
        wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                             anz1=anzahl_1, anz2=anzahl_2,art=art)
        lsg = darstellung_mengen(lsg_menge)
        return text, lsg_menge, lsg, wkt, wkt_str, pkt

    # Auswahl für Aufgabe b, c und d
    vereinigung, menge_verein, lsg_vereinigung, wkt4, wkt4_str, pkt4 = vereinigung(menge_1, menge_2, 'E_1', 'E_2')
    schnittmenge, menge_schnitt, lsg_schnittmenge, wkt5, wkt5_str, pkt5 = geschnitten(menge_1, menge_2, 'E_1', 'E_2')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Urne befinden sich {anzahl_1} Kugeln der Farbe {farbe_1} und {anzahl_2}'
               f' Kugeln der Farbe {farbe_2}. ']
    bez_ziehung = 'mit' if art=='zmZ' else 'ohne'
    if len([element for element in teilaufg if element in liste_teilaufg[0:6]]) > 0:
        aufgabe.append(f'Aus dieser Urne wird {bez_ziehung} Zurücklegen {anzahl_ziehen[1]} eine Kugel gezogen. \n\n')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Baumdiagramm zeichnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
        if art == 'zoZ':
            Baumdiagramm_zoZ(anzahl_ziehen[0], anzahl_1, anzahl_2, f'Loesung_{nr}{liste_teilaufg[i]}',
                             bz1=farben_kuerzel_1, bz2=farben_kuerzel_2)
        else:
            # print(farben_kuerzel_1)
            Baumdiagramm_zmZ(stufen, Rational(anzahl_1,(anzahl_1+anzahl_2)),
                             f'Loesung_{nr}{liste_teilaufg[i]}',
                             bz=farben_kuerzel_1, bz2=farben_kuerzel_2)
        aufgabe.append(str(liste_teilaufg[i]) + ') Zeichnen Sie das Baumdiagramm für diesen Versuch.')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_gross')
        else:
            aufgabe.append(' \n\n')
        if anzahl_ziehen[0] == 2:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '2 Stufen: 2P, Wkt an den Zweige: 2P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 5
        else:
            loesung.extend((str(liste_teilaufg[i]) + ') Baumdiagramm wie in der folgenden Abbildung dargestellt. \n\n',
                            '3 Stufen: 2P, Wkt an den Zweige: 3P, Beschriftung an den Knoten: 1P', 'Figure'))
            punkte = 6
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # Ergebnismengen angeben
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if pruef_kl10 == True:
            aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + f')  Markieren Sie im Baumdiagramm alle '
                                     + f'Pfade vom Ereignis:'),'E_1: ' + ereignis_1))
            loesung.append(str(liste_teilaufg[i]) + r') ~ \quad ' + str(lsg_1) + r' \quad (2BE) ')
            punkte = 2
        else:
            aufgabe.extend((str(liste_teilaufg[i]) + f')  Geben Sie die Ergebnismenge der folgenden Ereignisse an.',
                            r' E_1: ' + ereignis_1 + r' \\ E_2: ' + ereignis_2 + r' \\ '
                            + vereinigung + r' \quad \mathrm{und} \quad ' + schnittmenge))
            punkte = 6
            # Tabelle mit dem Text
            table1 = Tabular('p{0.2cm} p{3cm} p{7cm} p{2cm}')
            table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='c',
                                                                     data='Die Ergebnismengen'), 'Punkte')
            table1.add_row(MultiColumn(2, align='r', data='E1: '), str(lsg_1), '2P')
            table1.add_row(MultiColumn(2, align='r', data='E2: '), str(lsg_2), '2P')
            table1.add_row(MultiColumn(2, align='r', data=NoEscape(r'$E1 \cup E2: $')),
                           str(lsg_vereinigung), '1P')
            table1.add_row(MultiColumn(2, align='r', data=NoEscape(r'$E1 \cap E2: $')),
                           str(lsg_schnittmenge), '1P')
            table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
            loesung.append(table1)
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # Wahrscheinlichkeit von Ereignissen berechnen
        stern = r'$ ^{ \star } $' if pruef_kl10 else ''
        liste_bez.append(NoEscape(f'{str(nr)}.{stern + str(liste_teilaufg[i])})'))

        if pruef_kl10:
            if 'b' not in teilaufg:
                aufgabe.extend((NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i])
                                        + f') Berechnen Sie die Wahrscheinlichkeit für das Ereignis '),
                                        r' E_1: ' + ereignis_1))
            else:
                aufgabe.append(NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i])
                                         + f') Berechnen Sie die Wahrscheinlichkeit für das Ereignis $ E_1 $.'))
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
            loesung.append(r' ^{ \star } ' + str(liste_teilaufg[i])
                           + r') \quad \mathrm{Berechnung~der~Wahrscheinlichkeit} ' + r' \quad P(E_1) ~=~' + wkt1_str)
            punkte = pkt1
        else:
            if 'b' not in teilaufg:
                aufgabe.extend((NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i])
                                        +  f')  Berechnen Sie die Wahrscheinlichkeit für die folgenden Ereignisse.'),
                                r' E_1: ' + ereignis_1 + r', \quad E_2: ' + ereignis_2
                                + r',~E_1 \cap E_2,~ \mathrm{und} ~E1 \cup E2'))
            else:
                aufgabe.extend((NoEscape(r' \noindent ' + stern + str(liste_teilaufg[i])
                                         + f')  Berechnen Sie die Wahrscheinlichkeit für '
                                         + f'die folgenden Ereignisse.'),
                                r' E_1,~E_2,~E_1 \cap E_2,~ \mathrm{und} ~E1 \cup E2'))
            loesung.extend((str(liste_teilaufg[i]) + ') Berechnung der Wahrscheinlichkeiten der angegebenen Ereignisse',
                            r' \quad P(E_1) ~=~' + wkt1_str + r' \quad (' + gzahl(pkt1) + r'BE) \qquad P(E_2) ~=~'
                            + wkt2_str + r' \quad (' + gzahl(pkt2) + r'BE) \\\\ P(E_1 \cap E_2) ~=~' + wkt5_str
                            + r' \quad (' + gzahl(pkt5) + r'BE) \qquad P( E1 \cup E2 ) ~=~' + wkt4_str
                            + r' \quad (' + gzahl(pkt4) + r'BE)'))
            punkte = pkt1 + pkt2 + pkt4 + pkt5

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # bedingte Wahrscheinlichkeit berechnen und überprüfen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if wkt5/wkt2 == wkt1:
            lsg = (' ~=~ P(E_1) ~=~' + gzahl(N(wkt1,3) * 100) + r' \% \quad (3BE) \\'
                   + r' \mathrm{E_1~und~E_2~sind~stochastisch~unabhängig} \quad (1BE)')
        else:
            lsg = (r' \neq P(E_1) ~=~' + gzahl(N(wkt1, 3) * 100) + r' \% \quad (3BE) \\'
                   + r' \mathrm{E_1~und~E_2~sind~stochastisch~abhängig} \quad (1BE)')
        if 'b' in teilaufg or 'c' in teilaufg:
            aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                    + ') Überprüfen Sie die stochastische Unabhängigkeit von $ E_1 $ und $ E_2 $.'))
        else:
            aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i]) + f') Überprüfen Sie die stochastische '
                           + f'Unabhängigkeit von $ E_1 $ und $ E_2 $, mit: '), ' E_1: ' + ereignis_1 + r', \quad E_2: '
                           + ereignis_2))
        loesung.append(NoEscape(str(liste_teilaufg[i])
                                + r') \quad P_{E_2} (E_1) ~=~ \frac{P(E_1 \cap E_2)}{P(E_2)}~=~ \frac{'
                                + gzahl(N(wkt5,3)*100) + r' \% }{' + gzahl(N(wkt2,3)*100) + r' \%} ~=~'
                                + gzahl(N(wkt5/wkt2,3)*100) + r' \% ' + lsg))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(4)
        i += 1

    if len([element for element in teilaufg if element in ['e', 'f', 'g']]) > 0:
        # Wahrscheinlichkeitsverteilung und Histogramm einer Zufallsgröße

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        grafiken_loesung.append(f'Loesung_{nr} {liste_teilaufg[i]}')
        pkt = 0
        farbwahl, kuerzelwahl = auswahl()
        aufgabe.extend((NoEscape(r' \noindent ' + f'Die Zufallsgröße X ist die Anzahl der gezogenen Kugeln der '
                                 + f'Farbe {farbwahl}.'),' \n\n',
                        str(liste_teilaufg[i]) + f') Geben Sie die Wahrscheinlichkeitsverteilung von X an und'
                                                 f' zeichnen Sie das zugehörige Histogramm.'))
        # Tabelle der Wahrscheinlichkeitsverteilung:
        spalten = 'c|c|'
        for p in range(stufen+1):
            spalten += 'c|'
        wkt_berechn = ''

        liste_x = ['Wahrscheinlichkeitsverteilung von X ', NoEscape(r'$ x_i $')]
        liste_wkt = ['', NoEscape(r'$ P(X=x_i) $')]
        for zahl in list(range(stufen+1)):
            lsg_menge_x = []
            for element in ergebnisraum:
                k = 0
                for tubel in element:
                    if tubel == kuerzelwahl:
                        k += 1
                if k == zahl:
                    lsg_menge_x.append(element)
            wkt, wkt_str, pkt = wkt_baumdiagramm(lsg_menge_x, bez1=farben_kuerzel_1, bez2=farben_kuerzel_2,
                                                 anz1=anzahl_1, anz2=anzahl_2, art=art)
            x_werte.append(zahl)
            y_werte.append(N(wkt,2))
            liste_x.append(gzahl(zahl))
            liste_wkt.append(gzahl(N(wkt,2)))
            wkt_berechn = wkt_berechn + r' P(X=' + str(zahl) + ') ~=~' + wkt_str + r' \quad \\'
            pkt += 1
        table1 = Tabular(spalten, row_height=1.2)
        table1.add_hline(2)
        table1.add_row(liste_x)
        table1.add_hline(2)
        table1.add_row(liste_wkt)
        table1.add_hline(2)
        loesung.extend((str(liste_teilaufg[i]) + r') \quad ' + wkt_berechn + r' \\', table1,
                        r' \mathrm{Tabelle~(' + gzahl(pkt) + r'BE) }'))
        punkte = 2*pkt + 1
        # erstellen vom Histogramm
        loeschen()
        histogramm(x_werte, y_werte,f'Loesung_{nr} {liste_teilaufg[i]}.png','Histogramm')
        loesung.extend(('Figure', r' \mathrm{Koordinatensystem~1BE,~Balken~' + str(pkt) + r'BE} \\'
                        + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}'))
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in teilaufg if element in ['f', 'g']]) > 0:
        # Erwartungswert einer Zufallsgröße
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = int(len(x_werte)/2)+1
        # print(x_werte), print(y_werte)
        for x, y in zip(x_werte, y_werte):
            if x == x_werte[0] and y == y_werte[0]:
                ew_wert_str = gzahl(x, null=True) + r' \cdot ' + gzahl(y)
            else:
                ew_wert_str = ew_wert_str + vorz_str(x) + r' \cdot ' + gzahl(y)
        ew_wert = sum([x*y for x, y in zip(x_werte, y_werte)])
        aufgabe.append(NoEscape(r' \noindent ' +str(liste_teilaufg[i]) + ') Berechnen Sie den Erwartungswert der '
                                 + 'Zufallsgröße X.'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad E(X)~=~' + ew_wert_str + r' \\ E(X) ~=~'
                       + gzahl(N(ew_wert,3)) + r' \quad (' + str(punkte) + 'BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'g' in teilaufg:
        # Varianz und Standardabweichung einer Zufallsgröße
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        var_wert_str = ''
        var_wert = 0
        punkte = 4
        for x, y in zip(x_werte,y_werte):
            if x == x_werte[0]:
                var_wert_str = (var_wert_str + r'(' + gzahl(x) + '-' + gzahl(N(ew_wert,3))
                                + r')^2 \cdot ' + gzahl(y))
            else:
                var_wert_str = (var_wert_str + r'~+~ (' + gzahl(x) + '-' + gzahl(N(ew_wert, 3))
                                + r')^2 \cdot ' + gzahl(y))
            var_wert = var_wert + (x - ew_wert)**2*y
        aufgabe.append(NoEscape(r' \noindent ' +str(liste_teilaufg[i])
                                + ') Berechnen Sie die Varianz und die Standardabweichung der Zufallsgröße X.'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{V(X)~=~ \sum_{i=1}^{' + latex(stufen)
                       + r'} (x_i ~-~ E(x))^2 \cdot P(X ~=~ x_i) \quad und \quad \sigma (X) ~=~ \sqrt{V(X)}} \\'
                       + r' V(X)~=~' + var_wert_str + '~=~' + latex(N(var_wert,3)) + r' \quad (2BE) \\'
                       + r' \sigma (X) ~=~ \sqrt{' + gzahl((N(var_wert,3))) + '} ~=~ ' + gzahl(N(sqrt(var_wert),3))
                       + r' \quad (2BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if len([element for element in teilaufg if element in liste_teilaufg[8:12]]) > 0:
        if art == 'zoZ':
            aufgabe.append(f'Nun wird {anzahl_n} mal eine Kugel ohne Zurücklegen gezogen. \n\n')
        if art == 'zmZ':
            aufgabe.append(f'Nun wird {anzahl_n} mal eine Kugel mit Zurücklegen gezogen. \n\n')

    if 'h' in teilaufg:
        # mit Bernoullikoeffizient die Anzahl möglicher Ergebnisse berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.extend((NoEscape(r' \noindent ' +str(liste_teilaufg[i])
                                + f') Berechnen Sie die Anzahl der möglichen Ergebnisse, wenn {farbe_1}'
                                + f' genau {gzahl(anzahl_k)} mal gezogen wird. '), '\n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad N ~=~   \begin{pmatrix} ' + r' n  \\' + r' k \\ '
                       + r' \end{pmatrix} ~=~ \begin{pmatrix}' + gzahl(anzahl_n) + r' \\'
                       + gzahl(anzahl_k) + r' \\ ' + r' \end{pmatrix} ~=~ '
                       + gzahl(N(binomial(anzahl_n,anzahl_k),3)) + r' \quad (2BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(2)
        i += 1

    if 'i' in teilaufg and art == 'zoZ':
        # Berechnung der Wahrscheinlichkeit mit Lottomodell beim Ziehen ohne Zurücklegen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(NoEscape(r' \noindent ' +str(liste_teilaufg[i])
                                + f') Berechnen Sie die Wahrscheinlichkeit, dass {farbe_1}'
                                + f' genau {gzahl(anzahl_k)} mal gezogen wird.'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{P(' + gzahl(anzahl_k) + '~' + farbe_1
                       + r'e)} ~=~ \frac{ \begin{pmatrix}' + gzahl(anzahl_1) + r' \\'
                       + gzahl(anzahl_k) + r' \\ ' + r' \end{pmatrix} \cdot \begin{pmatrix}' + gzahl(anzahl_2) + r' \\'
                       + gzahl(anzahl_n - anzahl_k) + r' \\ ' + r' \end{pmatrix} } { \begin{pmatrix}'
                       + str(20) + r' \\' + gzahl(anzahl_n) + r' \\ ' + r' \end{pmatrix} } ~=~ '
                       + latex(N(binomial(anzahl_1,anzahl_k)
                                 * binomial(anzahl_2,anzahl_n-anzahl_k)
                                 / binomial(20,anzahl_n),3)) + r'~=~'
                       + latex(N(binomial(anzahl_1,anzahl_k)
                                 * binomial(anzahl_2,anzahl_n-anzahl_k)
                                 / binomial(20,anzahl_n),3) * 100)
                       + r' \% \quad (2BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(2)
        i += 1

    if 'j' in teilaufg and art == 'zmZ':
        # Berechnung der Wahrscheinlichkeit mit Bernoulli beim Ziehen mit Zurücklegen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        wkt = Rational(anzahl_1,anzahl_1 + anzahl_2)
        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                + f') Berechnen Sie die Wahrscheinlichkeit, dass {farbe_1} '
                                + f'genau {gzahl(anzahl_k)} mal gezogen wird. '))
        loesung.append(str(liste_teilaufg[i]) + r') \quad P(X=' + gzahl(anzahl_k) + ') ~=~'
                       + r' \begin{pmatrix} ' + gzahl(anzahl_n) + r' \\' + gzahl(anzahl_k) + r' \\'
                       + r' \end{pmatrix} \cdot \left(' + gzahl(wkt) + r' \right)^{' + gzahl(anzahl_k) + r'} \cdot \left( '
                       + gzahl(1-wkt) + r' \right) ^{' + gzahl(anzahl_n-anzahl_k) + '} ~=~ '
                       + gzahl(N(binomial(anzahl_n,anzahl_k) * wkt**anzahl_k*(1-wkt)**(anzahl_n-anzahl_k),3)*100)
                       + r' \% \quad (4BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(2)
        i += 1

    if 'k' in teilaufg and art == 'zmZ':
        # mit kumulierter Bernoullikette Wahrscheinlichkeit berechnen beim Ziehen mit Zurücklegen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        wkt = Rational(anzahl_1,anzahl_1 + anzahl_2)
        anz = anzahl_k - nzahl(2,5) if anzahl_k > 5 else anzahl_k - 1
        aufgabe.append(NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                + f') Berechnen Sie die Wahrscheinlichkeit, dass {farbe_1} '
                                + f'bis zu {gzahl(anz)} mal gezogen wird. '))
        loesung.append(str(liste_teilaufg[i]) + r') \quad P(X \leq ' + gzahl(anz) + ') ~=~'
                       + r' \sum_{i=0}^{' + gzahl(anz) + r'} \begin{pmatrix} ' + gzahl(anzahl_n) + r' \\' + 'i'
                       + r' \\' + r' \end{pmatrix} \cdot \left(' + gzahl(wkt) + r' \right)^{ i }\cdot \left( '
                       + gzahl(1-wkt) + r' \right) ^{' + gzahl(anzahl_n) + ' - i } ~=~ '
                       + gzahl(N(sum([binomial(anzahl_n,step) * wkt**step*(1-wkt)**(anzahl_n-step)
                                    for step in range(0,anz+1)]),3)*100)
                       + r' \% \quad (4BE)')
        if pruef_kl10:
            aufgabe.append(['Bild', '430px'])
            grafiken_aufgaben.append('notizen_mittel')
        else:
            aufgabe.append(' \n\n')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(2)
        i += 1


    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def faires_spiel(nr, BE=[]):
    # Überprüfung eines Zufallsversuches (zweimal Würfeln) auf "faires Spiel"
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    pkt = 5
    liste_bez = [str(nr)]
    i = 0
    produkt = lambda a, b: a*b
    summe = lambda a, b: a+b
    einsatz = nzahl(1,5)/2
    operation = [['das Produkt', produkt, nzahl(20,30), 36], ['die Summe', summe, nzahl(8,11), 36]]
    auswahl = random.choice(operation)
    i = 0
    for n in range(1,7):
        for m in range(1,7):
            if auswahl[1](m,n) > auswahl[2]:
                i += 1
    wkt = i/auswahl[3]
    wkt_proz = i/auswahl[3]*100
    einsatz = 1
    preis_fair = N(einsatz/wkt,3)
    preis = int(preis_fair - int(preis_fair/5))
    gewinn = N(preis*wkt-einsatz,3)
    if gewinn != 0:
        lsg = (r' \quad \mathrm{Das~Spiel~ist~nicht~fair} \quad (3BE) \\'
               + r' \mathrm{für~ein~faires~Spiel~müsste~P ~=~ \frac{E}{p \% } ~=~ \frac{'
               + gzahl(einsatz) + r' \text{ \texteuro }}{' + gzahl(N(wkt_proz,3)) + r' \% } ~=~ '
               + gzahl(preis_fair) + r' ~ \text{ \texteuro }~sein \quad (3BE)}')
        pkt += 3
    else:
        lsg = (r' \mathrm{Das~Spiel~ist~fair} \quad (3BE) \\')
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Ein Wurf mit zwei Würfeln kostet {gzahl(einsatz)}€ Einsatz. Ist {auswahl[0]} '
               f'der beiden Augenzahlen größer als {gzahl(auswahl[2])}, werden {gzahl(preis)}€ ausbezahlt. '
               f'Ist das Spiel fair? Wenn es unfair ist, wie müsste der Preis geändert werden, '
               f'damit es fair ist?  \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
               r' \mathrm{Legende: \quad G~ \to ~Gewinn~(im~Mittel~pro~Spiel) \quad P~ \to ~Preis} \quad '
               r' \mathrm{p~ \to ~Wahrscheinlichkeit~für~Preis \quad E~ \to ~Einsatz} \\'
               + r' \mathrm{Anzahl~der~günstigen~Ergebnisse ~' + str(i) + r'~von~insgesamt ~ 36 \quad \to \quad '
               + r' p ~=~ \frac{' + str(i) + '}{36} ~=~ ' + str(N(wkt_proz,3)) + r' \% \quad (2BE)} \\'
               + r' \mathrm{G~=~P \cdot p\% - E ~=~' + gzahl(preis) + r' \text{\texteuro} \cdot '
               + gzahl(N(wkt_proz,3)) + r' \% - ' + gzahl(einsatz) + r' \text{\texteuro} ~=~ '
               + gzahl(gewinn) + r' \text{\texteuro}}' + lsg]
    grafiken_aufgaben = []
    grafiken_loesung = []
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [pkt]
        liste_punkte = BE
    else:
        liste_punkte = [pkt]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def vierfeldertafel_studie(nr, teilaufg=['a', 'b', 'c'], vierfeldertafel=True, i=0, BE=[]):
    # bedingte Wahrscheinlichkeit in einer Vierfeldertafel am Beispiel einer med. Studie
    # Mit dem Parameter "vierfeldertafel=" kann festgelegt werden, ob eine Vierfeldertafel vorgegeben ist oder nicht. Standardmäßig ist "vierfeldertafel=True" und eine Vierfeldertafel vorgegeben, es kann aber auch "vierfeldertafel=False" gewählt werden.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

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
        # Vierfeldertafel vervollständigen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if vierfeldertafel == True:
            punkte = 3
            aufgabe.extend((Tabelle(A=A, P=P, P_H=P_H, H=H),' \n\n\n',
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
        # bedingte Wahrscheinlichkeiten aus gegebenen Größen berechnen

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
                       + r' \%  \quad (2BE)  \quad und \quad P_{P}(H) = \frac{ \vert P \cap H \vert }'
                       + r'{ \vert P \vert } ~=~ \frac{' + gzahl(P_H) + '}{' + gzahl(P) + '} ~=~ '
                       + gzahl(Rational(P_H,P)) + '~=~' + gzahl(Rational(P_H*100,P))
                       + r' \% \quad (2BE) } \\ \mathrm{Die~Gruppe,~welche~die~Medikamente~erhalten~hat,~'
                       + r'hat~eine~höhere~Heilungschance. \quad (1BE)} \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # bedingte Wahrscheinlichkeit aus vervollst. Vierfeldertafel berechnen

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

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben '
                  f'({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def vierfeldertafel_test(nr, teilaufg=['a', 'b', 'c'], vierfeldertafel=True, i=0, BE=[]):
    # bedingte Wahrscheinlichkeit in einer Vierfeldertafel am Beispiel eines medizinischen Tests
    # Mit dem Parameter "vierfeldertafel=" kann festgelegt werden, ob eine Vierfeldertafel vorgegeben ist oder nicht. Standardmäßig ist "vierfeldertafel=True" und eine Vierfeldertafel vorgegeben, es kann aber auch "vierfeldertafel=False" gewählt werden.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    A = int(nzahl(10,20) * 100) # alle Personen, die getestet wurden
    K = int(nzahl(4,7)/10 * A) # Krank - Personen die erkrankt sind
    G = int(A-K) # Gesund - Personen die gesund sind
    K_p = int(nzahl(7,9)/10 * K) # Personen die erkrankt sind und bei denen der medizinsche Test postiv ist
    G_p = int(nzahl(1,3)/10 * G) # Personen die gesund sind und bei denen der medizinische Test positiv ist
    p = int(K_p + G_p) # positiv - Personen bei denen der medizinische Test positiv ausfällt
    K_n = int(K - K_p) # Personen die Krank sind und deren Test negativ ist
    G_n = int(G - G_p) # Personen die Gesund sind und deren Test negativ ist
    n = int(K_n + G_n) # negativ - Personen bei denen der medizinischge Test negativ ist

    def Tabelle(A='', K='', G='', K_p='', G_p='', p='', K_n='', G_n='', n=''):
        table1 = Tabular('p{0.3cm} | p{2cm} | p{2cm} | p{0.7cm} p{1cm} p{3cm}')
        table1.add_row('', 'K', 'G', '', '', 'K: Krank')
        table1.add_hline(1, 4)
        table1.add_row('p', K_p, G_p, p, '', 'G: Gesund')
        table1.add_hline(1, 4)
        table1.add_row('n', K_n, G_n, n, '', 'p: positiv')
        table1.add_hline(1, 4)
        table1.add_row('', K, G, A, '', 'n: negativ')
        return table1
    auswahl = nzahl(1,2)
    if auswahl == 1:
        text1 = gzahl(p) + ' Personen positiv'
        text2 = 'aber ' + gzahl(G_p) + ' gesund'
    else:
        text1 = gzahl(n) + (' Personen negativ')
        text2 = 'aber ' + gzahl(K_n) + ' krank'

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Studie wird die Zuverlässigkeit eines neuen medizinischen Tests auf eine Krankheit '
               f'untersucht. An dieser Studie nahmen insgesamt {gzahl(A)} Personen teil. Davon sind {gzahl(G)} '
               f'Personen Teil einer Vergleichsgruppe, welche gesund sind und nicht an dieser Krankheit leiden. \n'
               f'Insgesamt wurden ' + text1 + ' getestet, von denen ' + text2 + ' waren . \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Vierfeldertafel vervollständigen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if vierfeldertafel == True:
            punkte = 3
            if auswahl == 1:
                aufgabe.extend((Tabelle(A=A, p=p, G_p=G_p, G=G),' \n\n\n',
                            str(liste_teilaufg[i]) + f')  Vervollständigen Sie die obere Vierfeldertafel. \n\n'))
            else:
                aufgabe.extend((Tabelle(A=A, n=n, K_n=K_n, G=G), ' \n\n\n',
                                str(liste_teilaufg[i]) + f')  Vervollständigen Sie die obere Vierfeldertafel. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + f') Tabelle wie unten ergibt {punkte} P. \n\n',
                            Tabelle(A=A, p=p, n=n, K_p=K_p, G_p=G_p, K=K, K_n=K_n, G_n=G_n, G=G), ' \n\n'))
            liste_punkte.append(punkte)
        else:
            punkte = 6
            aufgabe.extend((Tabelle(),' \n\n\n', str(liste_teilaufg[i]) + f')  Stellen Sie den oberen Sachverhalt '
                            + f'mithilfe der Vierfeldertafel dar. \n\n'))
            loesung.extend((str(liste_teilaufg[i]) + f') Tabelle wie unten ergibt {punkte} P. \n\n',
                            Tabelle(A=A, p=p, n=n, K_p=K_p, G_p=G_p, K=K, K_n=K_n, G_n=G_n, G=G), ' \n\n'))
            liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # bedingte Wahrscheinlichkeiten aus gegebenen Größen berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        aufgabe.extend(('Um die Zuverlässigkeit des Tests zu bewerten, ist es erforderlich, am Ende der Studie die '
                        'Wahrscheinlichkeit zu bestimmen, mit welcher eine erkrankte Person positiv (Sensitivität) und '
                        'eine gesunde Person negativ (Spezifität) getestet wird. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie die Sensitivität und Spezifität des Tests und '
                                                 'beurteilen Sie dessen Zuverlässigkeit. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{P_{K}(p) ~=~ \frac{ \vert K \cap p \vert }'
                       + r'{ \vert K \vert } ~=~ \frac{' + gzahl(K_p) + '}{' + gzahl(K) + '} ~=~ '
                       + gzahl(Rational(K_p,K)) + '~=~' + gzahl(N(K_p*100/K,3))
                       + r' \%  \quad (2BE)  \quad und \quad P_{G}(n) = \frac{ \vert G \cap n \vert }'
                       + r'{ \vert G \vert } ~=~ \frac{' + gzahl(G_n) + '}{' + gzahl(G) + '} ~=~ '
                       + gzahl(Rational(G_n,G)) + '~=~' + gzahl(N(G_n*100/G,3))
                       + r' \% \quad (2BE) }')
        loesung.append(f'Die Zuverlässigkeit des Tests ist nicht besonders groß. Bei dieser geringen Sensitivität '
                       f'werden von 100 Personen mit einer Krankheit {gzahl(round(K_n/K*100))} nicht erkannt. '
                       f'Das ist besonders bei ansteckenden Krankheiten ein Problem, da sich die Krankheit dann '
                       f'schnell verbreiten kann. (2BE)')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # bedingte Wahrscheinlichkeit aus vervollst. Vierfeldertafel berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3
        if auswahl == 1: # krank unter der Bed. negativer Test
            aufgabe.extend(('Eine Person hat ein negatives Testergebnis und befürchtet aber krank zu sein. \n\n',
                            str(liste_teilaufg[i]) + ') Berechnen Sie die Wahrscheinlichkeit, dass '
                            + 'eine Person krank ist, obwohl der Test negativ war. \n\n'))
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{ P_{n}(K) = \frac{' + gzahl(K_n) + '}{'
                           + gzahl(n) + '} }~=~ ' + gzahl(Rational(K_n,n)) + '~=~' + gzahl(N(K_n*100/n,3))
                           + r' \% \quad (3BE) ')
        else: # gesund unter der Bed. postiver Test
            aufgabe.extend(('Eine Person hat ein positives Testergebnis und hofft aber trotzdem gesund zu sein. \n\n',
                            str(liste_teilaufg[i]) + ') Berechnen Sie die Wahrscheinlichkeit, dass '
                            + 'eine Person gesund ist, obwohl der Test positiv war. \n\n'))
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{P_{p}(G) = \frac{' + gzahl(G_p) + '}{'
                           + gzahl(p) + '}} ~=~ ' + gzahl(Rational(G_p,p)) + '~=~' + gzahl(N(G_p*100/p,3))
                           + r' \% \quad (3BE) ')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben '
                  f'({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def sicheres_passwort(nr, teilaufg=['a', 'b'], i=0, BE=[]):
    # Berechnung von Permutationen am Beispiel eines sicheren Passwortes
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    laenge = nzahl(6,12)
    liste_zeichen = [['Zahlen', 10], ['Kleinbuchstaben', 26], ['Großbuchstaben', 26], ['Sonderzeichen', 33]]
    wiederholung = random.choice(['nicht', ''])
    auswahl_z = np.random.choice(list(range(len(liste_zeichen))), nzahl(1,len(liste_zeichen)), False)
    auswahl_zeichen = [liste_zeichen[element][0] for element in auswahl_z]
    anzahl = sum([liste_zeichen[element][1] for element in auswahl_z])
    if wiederholung == '':
        ergebnis = anzahl ** laenge
        lsg = gzahl(anzahl) + r'^{' + gzahl(laenge) + r'}~=~' + latex(N(ergebnis, 3))
    else:
        ergebnis = 1
        faktor = anzahl
        for x in range(laenge):
            ergebnis = ergebnis * faktor
            faktor = faktor - 1
        lsg = (r' \frac{' + gzahl(anzahl) + '!}{(' + gzahl(anzahl) + '-' + gzahl(laenge) + ')!} ~=~'
               + latex(N(ergebnis, 3)))

    auswahl_text = auswahl_zeichen[-1]
    if len(auswahl_zeichen) > 1:
        auswahl_text = auswahl_zeichen[-2] + ' und ' + auswahl_text
        if len(auswahl_zeichen) > 2:
            del auswahl_zeichen[-2:]
            for element in auswahl_zeichen:
                auswahl_text = element + ', ' + auswahl_text
    grafikkarten = [['Geforce RTX 4090', 'eine Billion', 10**12],
                            ['Radeon RX 7900 XTX', '800 Milliarden', 8*10**11],
                            ['Geforce RTX 4070', '500 Milliarden', 5*10**11],
                            ['Radeon RX 6700 XT', '340 Milliarden', 3.4*10**11]]
    auswahl_g = random.choice(list(range(len(grafikkarten))))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Passwörter können mit der sogenannten "Brute Force Methode" durch das Ausprobieren '
               f'aller möglichen Zeichen herausgefunden werden. So kann eine {grafikkarten[auswahl_g][0]} '
               f'{grafikkarten[auswahl_g][1]} Passwörter pro Sekunde ausprobieren. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Anzahl möglichen Kombinationen eines Passwortes berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2

        aufgabe.extend((f'Es wird ein Passwort aus {auswahl_text} mit {gzahl(laenge)} Stellen erstellt, '
                        f'wobei sich die Zeichen {wiederholung} wiederholen dürfen. \n'
                        'Hinweis: Zahlen haben 10 Zeichen, Buchstaben 26 Zeichen und Sonderzeichen 33 Zeichen \n\n',
                        str(liste_teilaufg[i]) + ') Berechne die Anzahl der möglichen Kombinationen für ein '
                                                 'Passwort. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad N= ' + lsg + r' \quad (2BE)')
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # Zeit für Brute Force Attacke (Ausprobieren aller Kombinationen) des Passwortes berechnen

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        zeit = N(ergebnis/grafikkarten[auswahl_g][2],3)
        aufgabe.append(str(liste_teilaufg[i]) + f') Wie lange benötigt die {grafikkarten[auswahl_g][0]} '
                                                ' zum Ausprobieren aller Kombinationen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad t ~=~ \frac{' + latex(N(ergebnis,3)) + r'}{ '
                       + latex(N(grafikkarten[auswahl_g][2],3)) + r' \frac{1}{s} } ~=~'
                       + latex(zeit) + r's \quad (2BE)')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben '
                  f'({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def lotto_modell(nr, BE=[]):
    # Berechnung der Wahrscheinlichkeit nach dem Lottomodell
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{str(nr)}']
    begriff = random.choice(['Transistoren', 'Batterien', 'Stiften', 'Fußbällen'])
    anzahl = nzahl(5,10)*100
    defekte = int(nzahl(2,5)*anzahl/100)
    ziehungen = nzahl(5,15)
    ziehungen_defekt = round(ziehungen*nzahl(1,2)/10)
    ziehungen_defekt = ziehungen if ziehungen_defekt > ziehungen else ziehungen_defekt
    if ziehungen_defekt == 1:
        ende = str('ist. \n\n')
    else:
        ende = str('sind. \n\n')
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'In einer Lieferung von {gzahl(anzahl)} {begriff} sind {gzahl(defekte)} defekt. '
               f'Berechnen Sie die Wahrscheinlichkeit, dass in einer Stichprobe von {ziehungen} {begriff} '
               f'genau {ziehungen_defekt} defekt ' + ende]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
               r' \mathrm{P(' + gzahl(ziehungen_defekt) + r'~von~' + gzahl(ziehungen)
               + r'~defekt)~=~ \frac{ \begin{pmatrix}' + gzahl(defekte) + r' \\' + gzahl(ziehungen_defekt) + r' \\ '
               + r' \end{pmatrix} \cdot \begin{pmatrix}' + gzahl(anzahl-defekte) + r' \\'
               + gzahl(ziehungen-ziehungen_defekt) + r' \\ ' + r' \end{pmatrix} } { \begin{pmatrix}' + str(anzahl)
               + r' \\' + gzahl(ziehungen) + r' \\ ' + r' \end{pmatrix} }} ~=~ '
               + latex(N(binomial(defekte, ziehungen_defekt)
                         * binomial(anzahl-defekte, ziehungen-ziehungen_defekt)
                         / binomial(anzahl, ziehungen), 3))
               + r'~=~' + latex(N(binomial(defekte, ziehungen_defekt)
                                  * binomial(anzahl-defekte, ziehungen-ziehungen_defekt)
                                  / binomial(anzahl, ziehungen), 3) * 100)
               + r' \% \quad (3BE)']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [3]
        liste_punkte = BE
    else:
        liste_punkte = [3]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def binomialverteilung(nr, teilaufg=['a', 'b', 'c'], laplace=True, neue_seite=None, i=0, BE=[]):
    # Hier sollen die Schüler und Schülerinnen verschiedene Berechnungen zu einer binomialverteilten Zufallsgröße X durchführen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    Dp = nzahl(3,8)
    p = Dp/10
    n = int(nzahl(10,100)*100/(Dp*(10-Dp))) if laplace else int(nzahl(1,9)*100/(Dp*(10-Dp)))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Die Zufallsgröße X sei mit den Parametern p = {gzahl(p)} und n = {gzahl(n)} binomialverteilt. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS den Erwartungswert und die Standardabweichung der Binomialverteilung ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        mu = n*p
        sigma = N(sqrt(n*p*(1-p)),3)
        aufgabe.extend((NoEscape(str(liste_teilaufg[i]) + r') Berechnen Sie den Erwartungswert $ \mu $ und '
                                + r'die Standardabweichung $ \sigma $ von X.'),' \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mu ~=~ n \cdot p ~=~' + gzahl(n) + r' \cdot ' + gzahl(p)
                       + '~=~' + gzahl(mu) + r' \quad \mathrm{und} \quad \sigma ~=~ \sqrt{n \cdot p \cdot (1-p) } '
                       + r' ~=~ \sqrt{' + gzahl(n) + r' \cdot ' + gzahl(p) + r' \cdot (1- '+ gzahl(p) + ')} ~=~ '
                       + gzahl(sigma) + r' \quad (4BE)')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

        if 'b' in teilaufg:
            # die SuS sollen beurteilen, ob die Binomialverteilung die Laplace-Bedingung erfüllt´(diese Teilaufgabe wird nur angezeigt, wenn auch Teilaufgabe a ausgewählt wurde)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 1
            aufgabe.extend((NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                     + r') Geben Sie an, ob die Laplace-Bedingung erfüllt ist.'), ' \n\n'))
            text = (r' \mathrm{da ~ \sigma ~=~ ' + gzahl(sigma)
                    + r' > 3, \quad ist~die~Laplace-Bedingung~erfüllt.} \quad (1BE)') \
                if sigma > 3 else (r' \mathrm{da ~ \sigma ~=~ ' + gzahl(sigma)
                                   + r' \leq 3, \quad ist~die~Laplace-Bedingung~nicht~erfüllt.} \quad (1BE)')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + text)

            aufgabe.append('NewPage') if neue_seite == i else ''
            liste_punkte.append(punkte)
            i += 1

        if 'c' in teilaufg and laplace:
            # die SuS sollen die Intervallgrenzen für die gegebene Intervallwahrscheinlichkeit berechnen (diese Teilaufgabe wird nur angezeigt, wenn auch Teilaufgabe a ausgewählt wurde)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            punkte = 7
            ausw_sigm = nzahl(2,6)/2
            untere_grenze = N(mu - ausw_sigm * sigma,4)
            obere_grenze = N(mu + ausw_sigm * sigma,4)
            untere_grenze_ger = int(untere_grenze) if untere_grenze%1 != 0 else untere_grenze
            obere_grenze_ger = round(obere_grenze+0.5)
            Verteilung = Binomial('X', n, p)
            F_obere_grenze = N(P(Verteilung <= obere_grenze_ger).evalf(),4)
            F_untere_grenze = round(P(Verteilung <= (untere_grenze_ger - 1)).evalf(),3)
            wkt_intervall = F_obere_grenze - F_untere_grenze
            aufgabe.extend((NoEscape(r' \noindent Berechnen Sie das symmetrisch zum Erwartungswert $ \mu $'
                                     r' der Zufallsgröße X liegendes ' + gzahl(ausw_sigm)
                                     + r'$ \sigma $ Intervall I.'), ' \n\n',
                            NoEscape(r' \noindent ' + str(liste_teilaufg[i])
                                     + r') Berechnen Sie die Grenzen und die Wahrscheinlichkeit des Intervalls.'),
                            ' \n\n'))
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{untere~Grenze: ~~ \mu }'
                           + vorz_v_innen(-1*ausw_sigm,r' \sigma ') + '~=~' + gzahl(mu)
                           + vorz_str(N(-1*ausw_sigm*sigma,3)) + '~=~' + gzahl(untere_grenze)
                           + r' \quad \to \quad ' + gzahl(untere_grenze_ger) + r' \quad (2BE) \\'
                           + r' \mathrm{obere~Grenze: ~~ \mu }' + vorz_v_innen(ausw_sigm, r' \sigma ')
                           + '~=~' + gzahl(mu) + vorz_str(N(ausw_sigm * sigma,3)) + '~=~' + gzahl(obere_grenze)
                           + r' \quad \to \quad ' + gzahl(obere_grenze_ger) + r' \quad (2BE) \\ P('
                           + gzahl(int(untere_grenze_ger)) + r' \leq X \leq ' + gzahl(obere_grenze_ger)
                           + r') ~=~ P(X \leq ' + gzahl(obere_grenze_ger) + r') - P(X \leq '
                           + gzahl(untere_grenze_ger - 1) + ') ~=~' + gzahl(F_obere_grenze)
                           + vorz_str(-1 * F_untere_grenze) + '~=~' + gzahl(wkt_intervall)  + r'~=~'
                           + gzahl(wkt_intervall*100) + r' \% \quad (3BE) ')

            aufgabe.append('NewPage') if neue_seite == i else ''
            liste_punkte.append(punkte)
            i += 1


    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def prognoseintervall(nr, teilaufg=['a', 'b', 'c'], neue_seite=None, i=0, BE=[]):
    # Berechnung des absoluten und relativen Prognoseintervalls am Beispiel der Keimfähigkeit von Pflanzensamen
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = []
    liste_punkte = []
    auswahl = random_selection([['Rosen','Samen'], [ 'Tulpen', 'Zwiebeln'], ['Orchideen', 'Samen'],
                                ['Lilien', 'Zwiebeln'], ['Dahlien', 'Samen']], anzahl=1)
    sorte = auswahl[0][0]
    samen = auswahl[0][1]
    anzahl = nzahl(5, 10) * 100
    keimen = int(nzahl(4, 8) * 10)
    auswahl = random_selection([[1, 0.683], [1.64, 0.9], [1.96, 0.95], [2, 0.954], [2.58, 0.99], [3, 0.997]], anzahl=2)
    wkt_intv = int(auswahl[0][1]*100) if auswahl[0][1]*100%1 == 0 else N(auswahl[0][1]*100,3)
    c = auswahl[0][0]
    mu = int(anzahl*keimen/100)
    sigma = round(sqrt(anzahl*keimen*(100-keimen))/100,2)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Ein Pflanzenhändler vertreibt wertvolle {sorte}. Die von ihm verkauften {samen} haben eine '
               f'Keimfähigkeit von {gzahl(keimen)}%. Bei einer Lieferung von {gzahl(anzahl)} {samen} an eine Gärtnerei,'
               f' muss er Zusagen, wie viele {samen} mit einer Sicherheit von {wkt_intv}% keimen '
               f'werden. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg and sigma > 3:
        # Hier sollen die SuS das Prognoseintervall der keimenden Samen in der absoluten Häufigkeit (Anzahl) angeben
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 9
        aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie das Prognoseintervall, '
                       + 'dass der Pflanzenhändler angeben sollte. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mu ~=~ n \cdot p ~=~' + gzahl(anzahl)
                       + r' \cdot ' + gzahl(keimen/100) + '~=~' + gzahl(mu) + r' \quad \mathrm{und} \quad '
                       + r' \sigma ~=~ \sqrt{n \cdot p \cdot (1-p) } ~=~ \sqrt{'
                       + gzahl(anzahl) + r' \cdot ' + gzahl(keimen/100) + r' \cdot (1- '+ gzahl(keimen/100)
                       + ') } ~=~ ' + gzahl(sigma) + r' \quad (4BE) \\' + r' \mathrm{untere~Grenze: ~~ \mu }'
                       + vorz_v_innen(-1*c,r' \sigma ') + '~=~' + gzahl(mu)
                       + vorz_str(round(-1*c*sigma,1)) + '~=~' + gzahl(round(mu-c*sigma,1))
                       + r' \quad (2BE) \\ \mathrm{obere~Grenze: ~~ \mu }' + vorz_v_innen(c, r' \sigma ')
                       + '~=~' + gzahl(mu) + vorz_str(round(c * sigma,1)) + '~=~' + gzahl(round(mu+c*sigma,1))
                       + r' \quad (2BE) \\' + r' \mathrm{Intervall ~~ I} \left[ ~' + gzahl(int(mu-c*sigma))
                       + r'~ \vert ~' + gzahl(round(mu+c*sigma+0.5)) + r'~ \right] \quad (1BE)')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1


    if 'b' in teilaufg:
        # Hier sollen die SuS überprüfen, ob die Laplace-Bedingung erfüllt ist und überhaupt eine Zusage möglich ist
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob die Anzahl der gelieferten {samen} überhaupt '
                                                f'eine Zusage über die Keimfähigkeit zulässt. \n\n')
        text = (r' \mathrm{da ~ \sigma ~=~ ' + gzahl(sigma)
                + r' > 3, \quad ist~die~Laplace-Bedingung~erfüllt~und~eine~Zusage~möglich.} \quad (1BE)') \
            if sigma > 3 else (r' \mathrm{da ~ \sigma ~=~ ' + gzahl(sigma)
                               + r' \leq 3, \quad ist~die~Laplace-Bedingung~nicht~erfüllt~und~keine~Zusage~möglich.} '
                               + r' \quad (1BE)')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + text)

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # Hier sollen die SuS den Erwartungswert und die Standardabweichung der Binomialverteilung ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        grenze = int(10 / ((keimen * (100 - keimen)) / 100**2))
        anzahl = nzahl(grenze, grenze + 10)*10
        wkt_intv_2 = int(auswahl[1][1] * 100) if auswahl[0][1] * 100 % 1 == 0 else N(auswahl[1][1] * 100, 3)
        c_2 = auswahl[1][0]
        mu = int(anzahl * keimen / 100)
        sigma = N(sqrt(anzahl * keimen * (100 - keimen)) / 100, 3)
        aufgabe.extend((f'Bei einer anderen Lieferung von {gzahl(anzahl)} {samen} soll der Pflanzenhändler mit einer '
                        f'Sicherheit von {gzahl(wkt_intv_2)}% zusichern wie viel Prozent der {sorte} keimen. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie das Prognoseintervall in Prozent, '
                       + 'dass der Pflanzenhändler angeben sollte. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \sigma ~=~ \sqrt{n \cdot p \cdot (1-p) } ~=~ \sqrt{'
                       + gzahl(anzahl) + r' \cdot ' + gzahl(keimen / 100) + r' \cdot (1- ' + gzahl(keimen / 100)
                       + ') } ~=~ ' + gzahl(sigma) + r' \quad (2BE) \\'
                       + r' \mathrm{Intervall ~~ I} \left[ p - c \cdot \frac{ \sigma }{n} \left\vert '
                       + r' p + c \cdot \frac{ \sigma }{n} \right. \right] ~=~ \left[ ' + gzahl(keimen / 100)
                       + vorz_str(-1*c_2) + r' \cdot \frac{ ' + gzahl(sigma) + '}{' + gzahl(anzahl) + r'} ~ \left\vert ~'
                       + gzahl(keimen / 100) + vorz_str(c_2) + r' \cdot \frac{ ' + gzahl(sigma) + '}{' + gzahl(anzahl)
                       + r'} ~ \right. \right] ~=~ \left[ ' + gzahl(N(keimen/100 - c_2 * sigma / anzahl, 3))
                       + r' \left\vert ' + gzahl(N(keimen/100 + c_2 * sigma / anzahl, 3))
                       + r' \right. \right] ~=~ \left[ ' + gzahl(N(keimen - c_2 * sigma / anzahl*100, 3))
                       + r' \% \left\vert ' + gzahl(N(keimen + c_2 * sigma / anzahl*100, 3))
                       + r' \% \right. \right] \quad (3BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(
                f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def konfidenzintervall(nr, teilaufg=['a', 'b'], BE=[]):
    # Berechnung des Konfidenzintervall am Beispiel der Wiederwahl eines Verbandspräsidenten
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
     # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = [f'{nr}']
    liste_punkte = [7]
    auswahl = random_selection(['Deutschen Fußball Bundes DFB', 'Deutschen Ruder Verbandes DRV',
                                'Deutschen Schwimmverbandes DSV'], anzahl=1)
    verband = auswahl[0]
    anz_mitgl = nzahl(5, 10) * 10
    zusage = int(nzahl(4, 8) / 10 * anz_mitgl)
    auswahl = random_selection([[1, 0.683], [1.64, 0.9], [1.96, 0.95], [2, 0.954], [2.58, 0.99], [3, 0.997]], anzahl=1)
    wkt_intv = int(auswahl[0][1]*100) if auswahl[0][1]*100%1 == 0 else N(auswahl[0][1]*100,3)
    c = auswahl[0][0]
    h_rel = Rational(zusage,anz_mitgl)
    p_1 = N(h_rel - c*sqrt(h_rel*(1-h_rel)/anz_mitgl),3)
    p_2 = N(h_rel + c*sqrt(h_rel*(1-h_rel)/anz_mitgl),3)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Der Präsident des {verband} möchte wissen, ob er bei der nächsten Wahl des Verbandes '
               f'wiedergewählt werden wird. Dazu läßt er insgesamt {gzahl(anz_mitgl)} Mitglieder aus verschiedenen '
               f'Vereinen befragen. Dabei haben {gzahl(zusage)} Mitglieder angegeben, das Sie ihn wiederwählen '
               f'würden. \n Bestimmen Sie mit einem Konfidenzintervall und einer Sicherheitswahrscheinlichkeit von '
               f'{gzahl(wkt_intv)}%, wie hoch der prozentuale Zustimmungswert des Präsidenten in der Gesamtheit der '
               f'Vereine geschätzt werden kann. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
               r' \mathrm{Berechnung~der~relativen~Häufigkeit: \quad h_n } ~=~ \frac{ X }{ n } ~=~ \frac{' + gzahl(zusage)
               + '}{' + gzahl(anz_mitgl) + '} ~=~ ' + gzahl(h_rel) + r' \quad (2BE) \\ p_{1,2} ~=~ '
               + r' h_n \pm c \cdot \sqrt{ \frac{ h_n \cdot \left( 1 - h_n \right) }{n} } ~=~ ' + gzahl(h_rel)
               + r' \pm ' + gzahl(c) +  r' \cdot \sqrt{ \frac{ ' + gzahl(h_rel) + r' \cdot \left( 1 '
               + vorz_str(-1*h_rel) + r' \right) }{' + gzahl(anz_mitgl) + r'}} \quad \to \quad p_1 ~=~'
               + gzahl(p_1) + r' \quad \mathrm{und} \quad p_2 ~=~ ' + gzahl(p_2) + r' \quad (4BE) \\'
               + r' \mathrm{mit~einer~Sicherheit~von~' + gzahl(wkt_intv) + r' \%,~liegt~die~Zustimmung~bei~ '
               + gzahl(N(p_1*100,3)) + '~bis~ ' + gzahl(N(p_2*100,3)) + '~Prozent.}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def normalverteilung(nr, teilaufg=['a', 'b'], neue_seite=None, i=0, BE=[]):
    # Berechnung der kumulierten Wahrscheinlichkeit der normalverteilten Blutdruckwerte der Bevölkerung
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_bez = []
    liste_punkte = []
    # Berechnungen für die Aufgabe
    mu = nzahl(115,125) # Erwartungswert
    sigma = nzahl(8,12) # Standardabweichung

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Der systolische Blutdruck in einer Bevölkerung '
               + f'folgt näherungsweise einer Normalverteilung mit einem Mittelwert (Erwartungswert) von {gzahl(mu)} '
               + f'mmHg und einer Standardabweichung von {gzahl(sigma)} mmHg. \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS den Prozentsatz der Bevölkerung angeben, die in einem bestimmten Bereich des Blutdrucks liegen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 2

        abst = nzahl(5,15)
        untere_gr = mu - abst
        obere_gr = mu + abst

        # Berechne den Prozentsatz zwischen den Grenzen
        prozentsatz = norm.cdf(obere_gr, loc=mu, scale=sigma) - norm.cdf(untere_gr, loc=mu, scale=sigma)

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie, welcher Prozentsatz der Bevölkerung einen '
                       + f' Blutdruck zwischen {gzahl(untere_gr)} und {gzahl(obere_gr)} mmHg hat. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad P(' + gzahl(untere_gr) + r' \leq X \leq ' + gzahl(obere_gr)
                       + ') ~=~ ' + gzahl(N(prozentsatz,3)) + r' ~=~ ' + gzahl(N(prozentsatz*100,3))
                       + r' \% \quad (2BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1


    if 'b' in teilaufg:
        # Hier sollen die SuS das Prognoseintervall der keimenden Samen in der absoluten Häufigkeit (Anzahl) angeben
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 3

        einstufung = random_selection([['leichte', 140,
                                        'kann langfristig das Risiko für Herz-Kreislauf-Erkrankungen erhöhen'],
                                       ['mittelschwere', 160,
                                        'erfordert in der Regel eine medikamentöse Behandlung.'],
                                       ['schwere', 180, 'erfordert eine sofortige medizinische Intervention']],
                                      anzahl=1)
        grad = einstufung[0][0]
        wert = einstufung[0][1]
        folgen = einstufung[0][2]

        # Berechne den Prozentsatz zwischen den Grenzen
        prozentsatz = 1 - norm.cdf(wert,loc=mu,scale=sigma)

        aufgabe.extend(('Nach den Leitlinien der Europäischen Gesellschaft für Kardiologie (ESC) und der Deutschen'
                        f'Hochdruckliga gilt ein Blutdruck von mehr als {gzahl(wert)} als {grad} Hypertonie und '
                        f'{folgen}. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie, wie viel Prozent der Bevölkerung einen '
                        + f'Blutdruck von {gzahl(wert)} mmHg oder höher haben. \n\n'))

        loesung.append(str(liste_teilaufg[i]) + r') \quad P( X \geq ' + gzahl(wert) + r' ) ~=~ 1 - P( X \leq '
                       + gzahl(wert) + r' ) ~=~ ' + gzahl(N(prozentsatz,3))
                       + r' ~=~ ' + gzahl(N(prozentsatz*100,3)) + r' \% \quad (3BE)')
        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1



    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def invertierte_normalverteilung(nr, teilaufg=['a', 'b', 'c'], neue_seite=None, i=0, BE=[]):
    # Hier sollen die Schüler und Schülerinnen die Zufallsgröße X, den Erwartungswert und die Standardabweichung mithilfe der Invertierung einer Normalverteilung berechnen
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "neue_seite=" kann festgelegt werden, nach welcher Teilaufgabe eine neue Seite für die restlichen Teilaufgaben erzeugt wird. Standardmäßig ist das "neue_seite=None" und es erfolgt keine erzwungener Seitenumbruch.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    stichprobe = nzahl(10,20)*10
    mu = nzahl(10,15)
    sigma = nzahl(5,10)/10

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               NoEscape(f'Die Keksfabrik „Knuspertraum“ produziert täglich Tausende von Keksen. Ein wichtiges '
                        f'Qualitätsmerkmal ist das normalverteilte Gewicht der Kekse. Die Qualitätsprüfer'
                        f' ziehen täglich Stichproben, um sicherzustellen, dass die Maschinen korrekt kalibriert sind.'
                        f' \n Ein Qualitätsprüfer hat eine Stichprobe von {gzahl(stichprobe)} Keksen entnommen. Dabei'
                        f' wurde das durchschnittliches Gewicht der Stichprobe mit ' + r'$ \mu $ ' + f' = {gzahl(mu)}g'
                        + f' und die' + ' Standardabweichung ' + r'mit $ \sigma $' + f' = {sigma}g bestimmt.'), ' \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Hier sollen die SuS das Gewicht (Hilfsvariable z) berechnen, das ein gegebener Prozentsatz der Kekse mindestens haben
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pwert = nzahl(15,19)*5
        inverse_wert = round(norm.ppf(pwert/100, loc=mu, scale=sigma),0)

        punkte = 2
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie das Gewicht das mindestens {gzahl(pwert)} % der '
                       + f'Kekse haben. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \Phi (z) ~=~ ' + gzahl(pwert/100)
                       + r' \quad \to \quad z \approx ' + gzahl(N(inverse_wert,3)) + r'g \quad (2BE)')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # die SuS sollen den Erwartungswert
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        pwert = nzahl(85,95)
        mu2 = mu + zzahl(5,10)/10
        inverse_wert = round(norm.ppf(pwert/100, loc=0, scale=1), 0)
        r = inverse_wert * sigma + mu2
        lsg = round(norm.ppf(pwert/100, loc=mu2, scale=sigma), 1)
        print(r)
        print(lsg)

        punkte = 4
        aufgabe.extend((f'Die Maschine wurde neu kalibriert. Jetzt liegt das Gewicht von {gzahl(pwert)}% der Kekse '
                        f'unter {gzahl(r)}g. Da sich die Präzision nicht geändert hat, ist von der '
                        f'bisherigen Standardabweichung bei der Produktion auszugehen. \n\n',
                        str(liste_teilaufg[i]) + ') Berechnen Sie das durchschnittliche Gewicht der Kekse,'
                        + ' nach der Kalibrierung. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \Phi (z) ~=~ ' + gzahl(pwert/100)
                       + r' \quad \to \quad z \approx ' + gzahl(inverse_wert)
                       + r' ~=~ \frac{r - \mu }{ \sigma }~=~ \frac{ ' + gzahl(r)
                       + r' - \mu }{ ' + gzahl(sigma) + r' } \quad \vert \cdot ' + gzahl(sigma)
                       + r' \quad \vert + \mu \quad \vert ' + vorz_str(-1*inverse_wert*sigma)
                       + r' \quad \to \quad \mu ~=~ ' + gzahl(r - inverse_wert*sigma) + r'g \quad (4BE)')

        aufgabe.append('NewPage') if neue_seite == i else ''
        liste_punkte.append(punkte)
        i += 1
        
        if 'c' in teilaufg:
            # die SuS sollen den Erwartungswert
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            sigma = sigma - nzahl(1,4)/10
            pwert = nzahl(90,99)
            grenzwert = round(norm.ppf(pwert/100, loc=mu, scale=sigma), 1)
            inverse_wert = round(norm.ppf(pwert / 100, loc=0, scale=1), 1)
            lsg = (grenzwert - mu)/inverse_wert
            print(sigma)
            print(lsg)

            punkte = 4
            aufgabe.extend((NoEscape(f'Die Qualitätskontrolle fordert eine präzisere Produktion. Die Maschine soll so '
                                     f'eingestellt werden, dass sie beim bisherigen durchschnittliches Gewicht der '
                                     f'Kekse mit ' + r'$ \mu $ = ' + f'{gzahl(mu)}g nur {gzahl(100 - pwert)} '
                                     + r' \% ' + f' der Kekse mehr als ' + f'{gzahl(grenzwert)}g wiegen.'), ' \n\n',
                                     str(liste_teilaufg[i]) + ') Welche Standardabweichung muss die Maschine '
                                     + 'erreichen, um diese Anforderungen zu erfüllen. \n\n'))
            loesung.append(str(liste_teilaufg[i]) + r') \quad P(X \geq ' + gzahl(grenzwert) + ') ~=~ '
                           + gzahl(1 - pwert/100) + r' \quad \to \quad 1 - P( X \leq ' + gzahl(grenzwert)
                           + r') ~=~ ' + gzahl(1 - pwert/100) + r' \quad \to \quad P( X \leq ' + gzahl(grenzwert)
                           + ') ~=~' + gzahl(pwert / 100) + r' \\ \Phi (z) ~=~ ' + gzahl(pwert / 100)
                           + r' \quad \to \quad z \approx ' + gzahl(inverse_wert)
                           + r' ~=~ \frac{ r - \mu }{ \sigma }~=~ \frac{ ' + gzahl(grenzwert)
                           + vorz_str(-1*mu) + r' }{ \sigma } \quad \vert \cdot \sigma \quad \vert \div '
                           + gzahl_klammer(inverse_wert) + r' \quad \to \quad \sigma ~=~ '
                           + gzahl(round(lsg, 2)) + r'g \quad (4BE)')

            aufgabe.append('NewPage') if neue_seite == i else ''
            liste_punkte.append(punkte)
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
