import string
import numpy as np
import random, math
from collections import Counter
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

def brueche_erweitern(nr, teilaufg=['a', 'b', 'c'], anzahl=False, wdh=False, anzahl_fakt=3, i=0, BE=[]):
    # Die SuS sollen Brüche mit vorgebenen Zahlen erweitern.
    # Mithilfe von "teilaufg=[]" können folgenden Funktionstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) trivialer Bruch
    # b) einfacher Bruch
    # c) schwerer Bruch
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Der Parameter "anzahl_fakt=" gibt die Anzahl der Faktoren, mit denen die Brüche erweitert werden, vor.

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    # Erstellen der Liste der Brüche mit Zähler und NenneR
    if teilaufg.count('a') > 9:
        print('Die maximale Anzahl an trivialen Brüchen ist 9.')
        trivial = 9
    else:
        trivial = teilaufg.count('a')
    liste_nenner = np.random.choice(list(range(2,12)), trivial, False)
    liste_nenner.sort()
    liste_brueche = [[1,element] for element in liste_nenner]

    if teilaufg.count('b') > 9:
        print('Die maximale Anzahl an einfachen Brüchen ist 9.')
        einfach = 9
    else:
        einfach = teilaufg.count('b')
    for zahl in range(einfach):
        zaehler, nenner = np.random.choice([2, 3, 5, 7], 2, False)
        while [zaehler, nenner] in liste_brueche:
            zaehler, nenner = np.random.choice([2, 3, 5, 7], 2, False)
        liste_brueche.append([zaehler, nenner])

    if teilaufg.count('c') > 9:
        print('Die maximale Anzahl an schwierigen Brüchen ist 9.')
        schwer = 9
    else:
        schwer = teilaufg.count('c')
    for zahl in range(schwer):
        zaehler, nenner = np.random.choice([5, 7, 11, 13], 2, False)
        while [zaehler, nenner] in liste_brueche:
            zaehler, nenner = np.random.choice([5, 7, 11, 13], 2, False)
        liste_brueche.append([zaehler, nenner])

    # Erstellen der Faktorliste
    anzahl_fakt = 6 if anzahl_fakt > 6 else anzahl_fakt
    liste_faktoren = np.random.choice([2, 3, 5, 7, 11, 13], anzahl_fakt, False)
    liste_faktoren.sort()

    # Erstellen der Aufgabenstellung
    aufg_faktoren = ''
    for faktor in liste_faktoren:
        if faktor != liste_faktoren[-1]:
            aufg_faktoren = aufg_faktoren + gzahl(faktor) + ', '
        else:
            aufg_faktoren = aufg_faktoren + gzahl(faktor)

    liste_bez = [f'{str(nr)}']
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Erweitern Sie die gegebenen Brüche mit {aufg_faktoren}.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    aufg = ''
    lsg = ''
    punkte = 0
    for element in liste_brueche:
        zaehler, nenner = element[0], element[1]
        if (i + 1) % 6 != 0:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + '~}'
            if i + 1 < trivial + einfach + schwer:
                aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 6 == 0 and element != liste_brueche[-1]:
            aufg = (aufg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
                    + r'~} \\\\')
        else:
            aufg = aufg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + '~}'
        liste_brueche_lsg = [[zaehler*faktor, nenner*faktor] for faktor in liste_faktoren]
        lsg_teilaufg = ''
        for tubel in liste_brueche_lsg:
            if tubel != liste_brueche_lsg[-1]:
                lsg_teilaufg = lsg_teilaufg + r' \frac{' + gzahl(tubel[0]) + '}{' + gzahl(tubel[1]) + '} ~=~ '
            else:
                lsg_teilaufg = lsg_teilaufg + r' \frac{' + gzahl(tubel[0]) + '}{' + gzahl(tubel[1]) + r'}'
        if (i + 1) % 2 != 0 and i + 1 != trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner) + '} ~=~ '
                   + lsg_teilaufg + r' \hspace{5em}')
        else:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner) + '} ~=~ '
                   + lsg_teilaufg + r' \\\\')
        punkte += 1
        i += 1
    lsg = lsg + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    if BE != []:
        if len(BE) > 1:
            print(
                'Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def brueche_kuerzen(nr, teilaufg=['a', 'b', 'c'], anzahl=False, wdh=False, i=0, BE=[]):
    # Die SuS sollen Brüche mit so weit wie möglich kürzen.
    # Mithilfe von "teilaufg=[]" können folgenden Funktionstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) trivialer Bruch
    # b) einfacher Bruch
    # c) schwerer Bruch
    # Der Parameter "anzahl_fakt=" gibt die Anzahl der Faktoren, mit denen die Brüche erweitert werden, vor.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    aufg = ''
    lsg = ''
    punkte = 0

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    # Erstellen der Liste der Brüche mit Zähler und NenneR
    if teilaufg.count('a') > 9:
        print('Die maximale Anzahl an trivialen Brüchen ist 9.')
        trivial = 9
    else:
        trivial = teilaufg.count('a')
    liste_nenner = np.random.choice(list(range(2,12)), trivial, False)
    liste_nenner.sort()
    liste_brueche_aufg = []
    for zahl in liste_nenner:
        faktor = random.choice([2, 3, 5, 7, 10])
        liste_brueche_aufg.append([faktor, faktor*zahl])
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(faktor) + '~}{~' + gzahl(faktor * zahl)
               + r'~} ~=~ \frac{ ~' + gzahl(1) + '~}{~' + gzahl(zahl) + r'~}')
        if (i + 1) % 3 != 0 and i + 1 < len(teilaufg):
            lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 or i + 1 == trivial and i + 1 < len(teilaufg):
            lsg = lsg + r' \\\\'
        else:
            pass
        i += 1
        punkte += 1
    if teilaufg.count('b') > 9:
        print('Die maximale Anzahl an einfachen Brüchen ist 9.')
        einfach = 9
    else:
        einfach = teilaufg.count('b')

    for zahl in range(einfach):
        fkt = np.random.choice([2, 3, 4, 5, 6, 7, 10], 2, False)
        fkt.sort()
        zaehler, nenner = np.random.choice([2, 3, 5, 7, 11], 2, False)
        while [zaehler, nenner] in liste_brueche_aufg:
            zaehler, nenner = np.random.choice([2, 3, 5, 7, 11], 2, False)
        liste_brueche_aufg.append([zaehler*fkt[0]*fkt[1], nenner*fkt[0]*fkt[1]])
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler * fkt[0] * fkt[1]) + '~}{~'
               + gzahl(nenner * fkt[0] * fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler * fkt[0]) + '~}{~'
               + gzahl(nenner * fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
        if (i + 1) % 3 != 0 and i + 1 < len(teilaufg):
            lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 or i + 1 == einfach and i + 1 < len(teilaufg):
            lsg = lsg + r' \\\\'
        else:
            pass
        i += 1
        punkte += 1

    if teilaufg.count('c') > 9:
        print('Die maximale Anzahl an schwierigen Brüchen ist 9.')
        schwer = 9
    else:
        schwer = teilaufg.count('c')
    for zahl in range(schwer):
        fkt = np.random.choice([2, 3, 4, 5, 6, 7, 10], 3, False)
        fkt.sort()
        zaehler, nenner = np.random.choice([3, 5, 7, 11, 13], 2, False)
        while [zaehler, nenner] in liste_brueche_aufg:
            zaehler, nenner = np.random.choice([3, 5, 7, 11, 13], 2, False)
        liste_brueche_aufg.append([zaehler*fkt[0]*fkt[1]*fkt[2], nenner*fkt[0]*fkt[1]*fkt[2]])
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler * fkt[0] * fkt[1] * fkt[2]) + '~}{~'
               + gzahl(nenner * fkt[0] * fkt[1] * fkt[2]) + r'~} ~=~ \frac{ ~' + gzahl(
                    zaehler * fkt[0] * fkt[1]) + '~}{~'
               + gzahl(nenner * fkt[0] * fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler * fkt[0]) + '~}{~'
               + gzahl(nenner * fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
        if (i + 1) % 2 != 0 and i + 1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 2 == 0 or i + 1 == einfach and i + 1 < len(teilaufg):
            lsg = lsg + r' \\\\'
        else:
            pass
        i += 1
        punkte += 1

    # Erstellen der Aufgabenstellung
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Kürzen Sie die gegebenen Brüche soweit wie möglich.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    k = 0

    for element in liste_brueche_aufg:
        zaehler, nenner = element[0], element[1]
        if (k + 1) % 5 != 0:
            aufg = aufg + str(liste_teilaufg[k]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + '~}'
            if k + 1 < trivial + einfach + schwer:
                aufg = aufg + r' \hspace{5em} '
        elif (k + 1) % 5 == 0 and (k + 1) < trivial + einfach + schwer:
            aufg = (aufg + str(liste_teilaufg[k]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
                    + r'~} \\\\')
        else:
            aufg = aufg + str(liste_teilaufg[k]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + '~}'
        k += 1

    lsg = lsg + r' \\\\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    if BE != []:
        if len(BE) > 1:
            print(
                'Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def brueche_ergaenzen(nr, teilaufg=['a', 'b'], anzahl=False, wdh=False, i=0, BE=[]):
    # Die SuS sollen eine vorgegebene Gleichung von Bruchtermen so ergänzen, dass diese richtig ist.
    # Mithilfe von "teilaufg=[]" können folgenden Funktionstypen (auch mehrfach der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Gleichung von Bruchtermen mit unbekannten Nenner
    # b) Gleichung von Bruchtermen mit unbekannten Zähler

    # Der Parameter "anzahl_fakt=" gibt die Anzahl der Faktoren, mit denen die Brüche erweitert werden, vor.
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Funktionstypen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    punkte = 0

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Ergänzen Sie die Terme so, dass die jeweilige Gleichung stimmt.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    liste_brueche = []
    aufg = ''
    lsg = ''
    unbek_nenner = teilaufg.count('a')
    for zahl in range(unbek_nenner):
        fakt = random.choice([2, 3, 4, 5, 6, 7, 10])
        zaehler, nenner = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, False)
        while [zaehler, nenner] in liste_brueche:
            zaehler, nenner = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, False)
        liste_brueche.append([zaehler, nenner])
        aufg = (aufg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
               + r'~} ~=~ \frac{~' + gzahl(zaehler * fakt) + r'~}{ \quad }')
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
               + r'~} ~=~ \frac{~' + gzahl(zaehler * fakt) + r'~}{~ \mathbf{' + gzahl(nenner * fakt) + '}~}')
        if (i + 1) % 3 != 0 and i + 1 < nenner + zaehler:
                aufg = aufg + r' \hspace{5em} '
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and (i + 1) < len(teilaufg):
            aufg = aufg + r' \\\\'
            lsg = lsg + r' \\\\'
        else:
            pass
        punkte += 1
        i += 1
    unbek_zaehler = teilaufg.count('b')
    for zahl in range(unbek_zaehler):
        fakt = random.choice([2, 3, 4, 5, 6, 7, 10])
        zaehler, nenner = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, False)
        while [zaehler, nenner] in liste_brueche:
            zaehler, nenner = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, False)
        liste_brueche.append([zaehler, nenner])
        aufg = (aufg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
                + r'~} ~=~ \frac{ \quad }{~' + gzahl(nenner * fakt) + r'~}')
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler) + '~}{~' + gzahl(nenner)
               + r'~} ~=~ \frac{~ \mathbf{' + gzahl(zaehler * fakt) + r'} ~}{~' + gzahl(nenner * fakt) + '~}')
        if (i + 1) % 3 != 0 and i + 1 < nenner + zaehler:
                aufg = aufg + r' \hspace{5em} '
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and (i + 1) < len(teilaufg):
            aufg = aufg + r' \\\\'
            lsg = lsg + r' \\\\'
        else:
            pass
        punkte += 1
        i += 1
    lsg = lsg + r' \\\\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
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

def bruchteile_berechnen(nr, anzahl=2, BE=[]):
    # Die SuS sollen von einer gegebenen Menge den angegebenen Bruchteil berechnen.
    # Der Parameter "anzahl=" legt die Anzahl der Teilaufgaben fest. Sie kann maximal 12 betragen.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    i = 0
    punkte = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Berechne.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    anzahl = 12 if anzahl > 12 else anzahl

    aufg = ''
    lsg = ''
    for zahl in range(anzahl):
        bruch = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, False)
        bruch.sort()
        zaehler, nenner = bruch
        einheiten = random.choice(['min', 'l', 'kg', 'g', 'qm', 'km'])
        zahl = random.randint(20, 100)
        wert = zaehler * zahl
        punkte += 1
        aufg = (aufg + str(liste_teilaufg[i]) + r') \quad  \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner)
                + r'} ~ \mathrm{von} ~ ' + gzahl(zahl * nenner) + einheiten)
        lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner) + r'} \cdot '
               + gzahl(zahl * nenner) + einheiten + '~=~' + gzahl(wert) + einheiten)
        if (i + 1) % 3 != 0 and i + 1 < anzahl:
            aufg = aufg + r' \hspace{5em} '
            lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and i + 1 < anzahl:
            aufg = aufg + r' \\\\'
            lsg = lsg + r' \\\\'
        i += 1

    lsg = lsg + r' \\\\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
    if BE != []:
        if len(BE) > 1:
            print(
                'Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def brueche_add_subr(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS gleichnamige und ungleichnamige Brüche addieren und subtrahieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) einfacher gleichnamiger Bruchterm (beide positiv)
    # b) gleichnamiger Bruchterm (beide positiv)
    # c) gleichnamiger Bruchterm (zweiter negativ)
    # d) gleichnamiger Bruchterm (beide negativ)
    # e) beliebiger gleichnamiger Bruch
    # f) einfacher ungleichnamiger Bruchterme (beide positiv)
    # g) ungleichnamiger Bruchterm (beide positiv)
    # h) ungleichnamiger Bruchterm (zweiter negativ)
    # i) ungleichnamiger Bruchterm (beide negativ)
    # j) beliebiger ungleichnamiger Bruchterm
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Berechne den angegebenen Bruchterm.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def einf_pp_gleichn_bruchterm():
        zaehler_2, zaehler_1 = np.random.choice([1, 2, 3, 4, 5, 6], 2, False)
        nenner = zaehler_1 + zaehler_2 + nzahl(2,4)
        loesung = Rational(zaehler_1 + zaehler_2, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner) + r'} ~+~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner) + r'} ~+~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner) + r'} ~=~ \frac{' + gzahl(zaehler_1) + '+' + gzahl(zaehler_2) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def pp_gleichn_bruchterm():
        zaehler_2, zaehler_1, nenner = np.random.choice(range(2,12), 3, False)
        loesung = Rational(zaehler_1 + zaehler_2, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner) + r'} ~+~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner) + r'} ~+~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner) + r'} ~=~ \frac{' + gzahl(zaehler_1) + '~+~' + gzahl(zaehler_2) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def pn_gleichn_bruchterm():
        zaehler_2, zaehler_1, nenner = np.random.choice(range(2,12), 3, False)
        loesung = Rational(zaehler_1 - zaehler_2, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~-~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~-~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner) + r'} ~=~ \frac{' + gzahl(zaehler_1) + '~-~' + gzahl(zaehler_2) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def nn_gleichn_bruchterm():
        zaehler_2, zaehler_1, nenner = np.random.choice(range(2,12), 3, False)
        loesung = Rational(-1*(zaehler_1 + zaehler_2), nenner)
        aufg = (r' - \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~-~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner) + r'}')
        lsg = (r' - \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~-~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner) + r'} ~=~ \frac{ - ' + gzahl(zaehler_1) + '~-~' + gzahl(zaehler_2) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def bel_gleichn_bruchterm():
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        loesung = Rational(vorz1*zaehler_1 + vorz2*zaehler_2, nenner)
        aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~' + vorz(vorz2) + r'~ \frac{'
                + gzahl(zaehler_2) + '}{' + gzahl(nenner) + r'}')
        lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner) + r'} ~' + vorz(vorz2)
               + r'~ \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner) + r'} ~=~ \frac{' + gzahl(vorz1*zaehler_1)
               + vorz_str(vorz2*zaehler_2) + '}{' + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def einf_pp_ungl_bruchterm():
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2,10), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        loesung = Rational(zaehler_1_erw + zaehler_2_erw, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~+~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner_2) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~+~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner_2) + r'} ~=~ \frac{' + gzahl(zaehler_1_erw) + '+' + gzahl(zaehler_2_erw) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def pp_ungl_bruchterm():
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2,12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        loesung = Rational(zaehler_1_erw + zaehler_2_erw, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~+~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner_2) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~+~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner_2) + r'} ~=~ \frac{' + gzahl(zaehler_1_erw) + '+' + gzahl(zaehler_2_erw) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def pn_ungl_bruchterm():
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2,12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        loesung = Rational(zaehler_1_erw - zaehler_2_erw, nenner)
        aufg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~-~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner_2) + r'}')
        lsg = (r' \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~-~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner_2) + r'} ~=~ \frac{' + gzahl(zaehler_1_erw) + '-' + gzahl(zaehler_2_erw) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def nn_ungl_bruchterm():
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2,12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        loesung = Rational(-1*(zaehler_1_erw + zaehler_2_erw), nenner)
        aufg = (r' - \frac{' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~-~ \frac{' + gzahl(zaehler_2)
                + '}{' + gzahl(nenner_2) + r'}')
        lsg = (r' - \frac{ ' + gzahl(zaehler_1) +'}{' + gzahl(nenner_1) + r'} ~-~ \frac{' + gzahl(zaehler_2)
               + '}{' + gzahl(nenner_2) + r'} ~=~ \frac{ - ' + gzahl(zaehler_1_erw) + '-' + gzahl(zaehler_2_erw) + '}{'
               + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    def bel_ungl_bruchterm():
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2,12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        loesung = Rational(zaehler_1_erw + zaehler_2_erw, nenner)
        aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + r'} ~' + vorz(vorz2)
                + r'~ \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + r'}')
        lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + r'} ~' + vorz(vorz2)
                + r'~ \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + r'} ~=~ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + r'} ~=~ ' + gzahl(loesung))
        return aufg, lsg

    aufgaben = {'a': einf_pp_gleichn_bruchterm, 'b': pp_gleichn_bruchterm, 'c': pn_gleichn_bruchterm,
                'd': nn_gleichn_bruchterm, 'e': bel_gleichn_bruchterm, 'f': einf_pp_ungl_bruchterm,
                'g': pp_ungl_bruchterm, 'h': pn_ungl_bruchterm, 'i': nn_ungl_bruchterm, 'j':bel_ungl_bruchterm}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 4 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        if (i+1) % 2 != 0 and i+1 < len(teilaufg):
            lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
            lsg = lsg + r' \\\\'
        else:
            pass
        punkte += 1
        i += 1

    lsg = lsg + r' \\\\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'
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

def brueche_mul_div(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS Brüche multiplizieren und dividieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) einfachen Bruchterm multiplizieren (beide positiv)
    # b) einfachen Bruchterm multiplizieren (beliebige Vorzeichen)
    # c) Bruchterm kürzen und multiplizieren (beliebige Vorzeichen)
    # d) einfachen Bruchterm dividieren (beide positiv)
    # e) einfachen Bruchterm dividieren (beliebige Vorzeichen)
    # f) Bruchterm kürzen und dividieren (beliebige Vorzeichen)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Berechne den gegebenen Bruchterm.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def einf_pp_bruchterm_multi():
        zahlen = np.random.choice(range(1,10), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        bruch1 = Rational(zaehler1, nenner1)
        bruch2 = Rational(zaehler2, nenner2)
        ergebnis = Rational(zaehler1 * zaehler2, nenner1 * nenner2)
        aufg = gzahl(bruch1) + r'~ \cdot ~' + gzahl(bruch2)
        lsg = gzahl(bruch1) + r'~ \cdot ~' + gzahl(bruch2) + '~=~' + gzahl(ergebnis)
        return aufg, lsg

    def einf_bruchterm_multi():
        zahlen = np.random.choice(range(1,10), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        bruch1 = Rational(vorz1 * zaehler1, nenner1)
        bruch2 = Rational(vorz2 * zaehler2, nenner2)
        ergebnis = Rational(vorz1 * vorz2 * zaehler1 * zaehler2, nenner1 * nenner2)
        aufg = gzahl(bruch1) + r'~ \cdot ~' + gzahl_klammer(bruch2)
        lsg = gzahl(bruch1) + r'~ \cdot ~' + gzahl_klammer(bruch2) + '~=~' + gzahl(ergebnis)
        return aufg, lsg

    def bruchterm_kuerz_multi():
        zahlen = np.random.choice(range(1,12), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        while (nenner1/zaehler1) % 1 == 0 or (nenner2/zaehler2) % 1 == 0:
            zahlen = np.random.choice(range(1, 12), 4, False)
            zahlen.sort()
            zaehler1, zaehler2, nenner1, nenner2 = zahlen
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        fakt1, fakt2 = np.random.choice(range(2,12), 2, False)
        ergebnis = Rational(vorz1 * vorz2 * zaehler1 * zaehler2, nenner1 * nenner2)
        if vorz2 < 0:
            aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2*zaehler1) + '}{' + gzahl(fakt1*nenner1)
                    + r'}~ \cdot ~ \left(' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt1 * zaehler2) + '}{'
                    + gzahl(fakt2 * nenner2) + r'} \right)')
            lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                   + r'} ~ \cdot ~ \left( ' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt1 * zaehler2) + '}{'
                   + gzahl(fakt2 * nenner2) + r'} \right) ~=~' + vorz_aussen(vorz1*vorz2) + r' \frac{'
                   + gzahl(zaehler1) + '}{' + gzahl(nenner1) + r'} \cdot \frac{' + gzahl(zaehler2) + '}{'
                   + gzahl(nenner2) + r'} ~=~' + gzahl(ergebnis))
        else:
            aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                    + r'} ~ \cdot ~' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt1 * zaehler2) + '}{'
                    + gzahl(fakt2 * nenner2) + r'}')
            lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                   + r'} ~ \cdot ~' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt1 * zaehler2) + '}{'
                   + gzahl(fakt2 * nenner2) + r'} ~=~' + vorz_aussen(vorz1 * vorz2) + r' \frac{'
                   + gzahl(zaehler1) + '}{' + gzahl(nenner1) + r'} \cdot \frac{'
                   + gzahl(zaehler2) + '}{' + gzahl(nenner2) + r'} ~=~' + gzahl(ergebnis))
        return aufg, lsg
    def einf_pp_bruchterm_div():
        zahlen = np.random.choice(range(1, 10), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        bruch1 = Rational(zaehler1, nenner1)
        bruch2 = Rational(zaehler2, nenner2)
        bruch2_kw = Rational(nenner2, zaehler2)
        ergebnis = Rational(zaehler1 * nenner2, nenner1 * zaehler2)
        aufg = gzahl(bruch1) + r'~ \div ~' + gzahl(bruch2)
        lsg = (gzahl(bruch1) + r' \div ' + gzahl(bruch2) + '~=~' + gzahl(bruch1) + r' \cdot '
               + gzahl(bruch2_kw) + '~=~' + gzahl(ergebnis))
        return aufg, lsg

    def einf_bruchterm_div():
        zahlen = np.random.choice(range(1,10), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        bruch1 = Rational(zaehler1, nenner1)
        bruch2 = Rational(zaehler2, nenner2)
        bruch2_kw = Rational(nenner2, zaehler2)
        ergebnis = Rational(vorz1 * vorz2 * zaehler1 * nenner2, nenner1 * zaehler2)
        aufg = gzahl(vorz1 * bruch1) + r'~ \div ~' + gzahl_klammer(vorz2 * bruch2)
        lsg = (gzahl(vorz1 * bruch1) + r' \div ' + gzahl_klammer(vorz2*bruch2) + '~=~' + vorz_aussen(vorz1*vorz2)
               + gzahl(bruch1) + r' \cdot ' + gzahl(bruch2_kw) + '~=~' + gzahl(ergebnis))
        return aufg, lsg

    def bruchterm_kuerz_div():
        zahlen = np.random.choice(range(1, 12), 4, False)
        zahlen.sort()
        zaehler1, zaehler2, nenner1, nenner2 = zahlen
        while (nenner1 / zaehler1) % 1 == 0 or (nenner2 / zaehler2) % 1 == 0:
            zahlen = np.random.choice(range(1, 12), 4, False)
            zahlen.sort()
            zaehler1, zaehler2, nenner1, nenner2 = zahlen
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        fakt1, fakt2 = np.random.choice(range(2, 12), 2, False)
        ergebnis = Rational(vorz1 * vorz2 * zaehler1 * nenner2, nenner1 * zaehler2)
        if vorz2 < 0:
            aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                    + r'} ~ \div ~ \left(' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt2 * zaehler2) + '}{'
                    + gzahl(fakt1 * nenner2) + r'} \right)')
            lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                   + r'} ~ \div \left(' + vorz_aussen(vorz2) + r'~ \frac{' + gzahl(fakt2 * zaehler2) + '}{'
                   + gzahl(fakt1 * nenner2) + r'} \right) ~=~' + vorz_aussen(vorz1 * vorz2) + r' \frac{'
                   + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1) + r'} \cdot \frac{'
                   + gzahl(fakt1 * nenner2) + '}{' + gzahl(fakt2 * zaehler2) + r'} ~=~'
                   + vorz_aussen(vorz1 * vorz2) + r' \frac{' + gzahl(zaehler1) + '}{' + gzahl(nenner1)
                   + r'} \cdot \frac{' + gzahl(nenner2) + '}{' + gzahl(zaehler2) + r'} ~=~' + gzahl(ergebnis))
        else:
            aufg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                    + r'}~ \div ~' + vorz_aussen(vorz2) + r' \frac{' + gzahl(fakt2 * zaehler2) + '}{'
                    + gzahl(fakt1 * nenner2) + r'} ')
            lsg = (vorz_aussen(vorz1) + r' \frac{' + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1)
                   + r'} ~ \div ' + vorz_aussen(vorz2) + r'~ \frac{' + gzahl(fakt2 * zaehler2) + '}{'
                   + gzahl(fakt1 * nenner2) + r'} ~=~' + vorz_aussen(vorz1) + r' \frac{'
                   + gzahl(fakt2 * zaehler1) + '}{' + gzahl(fakt1 * nenner1) + r'} ~ \cdot \frac{'
                   + gzahl(fakt1 * nenner2) + '}{' + gzahl(fakt2 * zaehler2) + r'} ~=~' + vorz_aussen(vorz1)
                   + r' \frac{' + gzahl(zaehler1) + '}{' + gzahl(nenner1) + r'} \cdot \frac{' + gzahl(nenner2)
                   + '}{' + gzahl(zaehler2)+ r'} ~=~' + gzahl(ergebnis))
        return aufg, lsg

    aufgaben = {'a': einf_pp_bruchterm_multi, 'b': einf_bruchterm_multi, 'c': bruchterm_kuerz_multi,
                'd': einf_pp_bruchterm_div, 'e': einf_bruchterm_div, 'f': bruchterm_kuerz_div}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 4 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        if element != 'f':
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
            lsg = lsg + r' \\\\'
        punkte += 1
        i += 1

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

def potenzgesetze(nr, anzahl=1, BE=[]):
    # Hier sollen die Schüler und Schülerinnen Logarithmusgesetze vervollständigen.
    # Mit dem Argument "anzahl=" kann die Anzahl der zufällig ausgewählten Logarithmusgesetze festgelegt werden.
    # Standardmäßig wird immer ein Gesetz erstellt.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    # hier wird die Funktion erstellt.
    regeln_aufgabe = {r' a^m \cdot a^n ~=~ \hspace{15em}': r' a^m \cdot a^n ~=~ a^{m+n} ',
                      r' \frac{a^m}{a^n} ~=~ \hspace{15em}': r' \frac{a^m}{a^n} ~=~ a^{m-n} ',
                      r' a^n \cdot b^n ~=~ \hspace{15em}': r' a^n \cdot b^n ~=~ \left( a \cdot b \right) ^n',
                      r' \left( a^m \right) ^n ~=~ \hspace{15em}': r' \left( a^m \right) ^n ~=~ a^{m \cdot n}',
                      r' \frac{a^n}{b^n} ~=~ \hspace{15em}': r' \frac{a^n}{b^n} ~=~ \left( \frac{a}{b} \right) ^n ',
                      r' a^0 ~=~ \hspace{15em}': r' a^0 ~=~ 1',
                      r' \frac{1}{a^n} ~=~ \hspace{15em}': r' \frac{1}{a^n} ~=~ a^{-n} ',
                      r' \sqrt[m]{a^n} ~=~ \hspace{15em}': r'\sqrt[m]{a^n} ~=~ a^{ \frac{n}{m}} '}

    exit("Die Eingabe bei anzahl muss eine Zahl sein") if type(anzahl) != int else anzahl
    anzahl = len(regeln_aufgabe) if anzahl > len(regeln_aufgabe) else anzahl
    auswahl = np.random.choice(list(regeln_aufgabe.keys()), anzahl, False)
    if anzahl == 1:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Vervollständigen Sie das folgende Potenzgesetz.']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Vervollständigen Sie die folgenden Potenzgesetze.']
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
        lsg = lsg + regeln_aufgabe[auswahl[element]] + r' \\' if (element+1) != anzahl \
            else lsg + regeln_aufgabe[auswahl[element]]


    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [anzahl]
        liste_punkte = BE
    else:
        liste_punkte = [anzahl]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def potenzgesetz_eins(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], anzahl=False, wdh= False, i=0, BE=[]):
    # Hier sollen die SuS zwei Potenzen multiplizieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Potenzen mit nat. Zahlen und Exponenten
    # b) Potenzen mit nat. Zahlen und ganzz. Exponenten
    # c) Potenzen mit neg. Zahlen und ganzz. Exponenten
    # d) Potenzen mit bel. ganzen Zahlen und Exponenten
    # e) Potenzen mit Variablen und nat. Exponenten
    # f) Potenzen mit Variablen und ganzz. Exponenten
    # g) Potenzen mit Variablen, Faktoren und ganzz. Exponenten
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def pos_zahl_bas_exp():
        bas = nzahl(2,6)
        exp1, exp2 = np.random.choice(range(1,5), 2, False)
        aufg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~ ' + gzahl(bas) + '^{' + gzahl(exp1+exp2, exp=True) + '}')
        return aufg, lsg

    def pos_zahl_bas():
        bas = nzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~ ' + gzahl(bas) + '^{' + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def neg_zahl_bas():
        bas = -1 * nzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = ('(' + gzahl(bas) + ')^{' + gzahl(exp1) + r'} \cdot (' + gzahl(bas) + ')^{' + gzahl(exp2) + '} ~')
        lsg = ('(' + gzahl(bas) + ')^{' + gzahl(exp1) + r'} \cdot (' + gzahl(bas) + ')^{' + gzahl(exp2) + '} ~=~ ('
               + gzahl(bas) + ')^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~ (' + gzahl(bas) + ')^{'
               + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def bel_zahl_bas():
        bas = zzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (gzahl_klammer(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl_klammer(bas) + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl_klammer(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl_klammer(bas) + '^{' + gzahl(exp2)
               + '} ~=~ ' + gzahl_klammer(bas) + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~ ' + gzahl_klammer(bas)
               + '^{' + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_bas_pos_exp():
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (bas+ '^{' + gzahl(exp1) + r'} ~ \cdot ~' + bas + '^{' + gzahl(exp2) + '} ~')
        lsg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~=~ ' + bas + '^{'
               + gzahl(exp1) + vorz_str(exp2) + '} ~=~ ' + bas + '^{' + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_bas_exp():
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~')
        lsg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~=~ ' + bas + '^{'
               + gzahl(exp1) + vorz_str(exp2) + '} ~=~ ' + bas + '^{' + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_bas_fakt():
        fakt1, fakt2 = faktorliste(2, 2, 12)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 + exp2 == 0:
            w_erg = '~=~ ' + gzahl(fakt1*fakt2)
        else:
            w_erg = ''
        aufg = (gzahl(fakt1) + bas + '^{' + gzahl(exp1) + r'} \cdot '
                + gzahl_klammer(fakt2) + r'\cdot ' + bas + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl(fakt1) + r' \cdot ' + bas + '^{' + gzahl(exp1) + r'} \cdot '
               + gzahl_klammer(fakt2) + r' \cdot ' + bas + '^{' + gzahl(exp2) + '}' + ' ~=~ ' + gzahl(fakt1)
               + r' \cdot ' + gzahl_klammer(fakt2) + r' \cdot ' + bas + '^{' + gzahl(exp1) + vorz_str(exp2)
               + '} ~=~ ' + gzahl(fakt1*fakt2) + r' \cdot ' + bas + '^{' + gzahl(exp1+exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    aufgaben = {'a': pos_zahl_bas_exp, 'b': pos_zahl_bas, 'c': neg_zahl_bas, 'd': bel_zahl_bas,
                'e': var_bas_pos_exp, 'f': var_bas_exp, 'g': var_bas_fakt}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 4 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \\\\'
        if element != 'g':
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
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

def potenzgesetz_zwei(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS zwei Potenzen dividieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Potenzen mit nat. Zahlen und Exponenten
    # b) Potenzen mit nat. Zahlen und ganzz. Exponenten
    # c) Potenzen mit neg. Zahlen und ganzz. Exponenten
    # d) Potenzen mit bel. ganzen Zahlen und Exponenten
    # e) Potenzen mit Variablen und nat. Exponenten
    # f) Potenzen mit Variablen und ganzz. Exponenten
    # g) Potenzen mit Variablen, Faktoren und ganzz. Exponenten
    # h) Potenzen mit zwei Variablen, Faktoren und ganzz. Exponenten
    # i) Produkt von Potenzen mit jeweils zwei Variablen, Faktoren und ganzz. Exponenten
    # j) Division von Potenzen mit jeweils zwei Variablen, Faktoren und ganzz. Exponenten
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def pos_zahl_bas_exp():
        bas = nzahl(2,6)
        exp1, exp2 = np.random.choice(range(1,5), 2, False)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~=~ '
               + gzahl(bas) + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def pos_zahl_bas():
        bas = nzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~=~ '
               + gzahl(bas) + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def neg_zahl_bas():
        bas = -1 * nzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{(' + gzahl(bas) + ')^{' + gzahl(exp1) + r'}} {(' + gzahl(bas) + ')^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{(' + gzahl(bas) + ')^{' + gzahl(exp1) + r'}} {(' + gzahl(bas) + ')^{' + gzahl(exp2) + '}} ~=~ ('
               + gzahl(bas) + ')^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ (' + gzahl(bas)
               + ')^{' + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def bel_zahl_bas():
        bas = zzahl(2,6)
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl_klammer(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl_klammer(bas) + '^{'
                + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl_klammer(bas) + '^{' + gzahl(exp1) + r'}} {' + gzahl_klammer(bas) + '^{' + gzahl(exp2)
               + '}} ~=~ ' + gzahl_klammer(bas) + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ ' + gzahl_klammer(bas)
               + '^{' + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_bas_pos_exp():
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}} {' + bas + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}} {' + bas + '^{' + gzahl(exp2) + '}} ~=~ ' + bas
               + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ ' + bas
               + '^{' + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_bas_exp():
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}} {' + bas + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}} {' + bas + '^{' + gzahl(exp2) + '}} ~=~ ' + bas
               + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~ ' + bas + '^{'
               + gzahl(exp1-exp2, exp=True) + '}' + w_erg)
        return aufg, lsg


    def triv_var_bas_fakt():
        fakt = zzahl(2,7)
        fakt1, fakt2 = np.random.choice([fakt, fakt*zzahl(1,7)],2, False)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = exponenten(2,2,7, ganzz=True)
        if exp1 - exp2 == 0:
            w_erg = '~=~ ' + gzahl(Rational(fakt1,fakt2))
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(fakt1) + '~' + bas + '^{' + gzahl(exp1) + r'}}{'
                + gzahl(fakt2) + '~' + bas + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl(fakt1) + bas + '^{' + gzahl(exp1) + r'}}{' + gzahl(fakt2) + '~' + bas + '^{'
               + gzahl(exp2) + '}} ~=~ ' + gzahl(Rational(fakt1,fakt2)) + r' \cdot ' + bas + '^{' + gzahl(exp1)
               + vorz_str(-1*exp2) + '} ~=~ '
               + vorz_v_aussen(Rational(fakt1,fakt2), bas + '^{' + gzahl(exp1-exp2, exp=True) + '}') + w_erg)
        return aufg, lsg

    def einf_var_bas_fakt():
        zaehler, nenner = np.random.choice([2,3,5,7,9,11],2, False)
        fakt_erw = zzahl(2, 10)
        fakt1, fakt2 = np.random.choice([zaehler*fakt_erw, nenner * fakt_erw], 2, False)
        bas = np.random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'],2,False)
        bas.sort()
        bas1, bas2 = bas
        exp1, exp2, exp3, exp4 = exponenten(4,2,12, wdh=True, ganzz=True)
        if exp1 - exp3 == 0 or exp2 - exp4 == 0:
            w_erg = ' ~=~ ' + gzahl(Rational(fakt1, fakt2))
            if exp1 - exp3 != 0:
                w_erg = w_erg + bas1 + '^{' + gzahl(exp1 - exp3) + '}'
            if exp2 - exp4 != 0:
                w_erg = w_erg + bas2 + '^{' + gzahl(exp2 - exp4) + '}'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(fakt1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2) + r'}}{'
                + gzahl(fakt2) + '~' + bas1 + '^{' + gzahl(exp3) + '}' + bas2 + '^{' + gzahl(exp4) + '}} ~')
        lsg = (r' \frac{' + gzahl(fakt1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2) + r'}}{'
                + gzahl(fakt2) + '~' + bas1 + '^{' + gzahl(exp3) + '}' + bas2 + '^{' + gzahl(exp4) + r'}} ~=~ \frac{'
               + gzahl(fakt1) + '}{' + gzahl(fakt2) + r'} \cdot ' + bas1 + '^{' + gzahl(exp1) + vorz_str(-1 * exp3)
               + '}' + bas2 + '^{' + gzahl(exp2) + vorz_str(-1 * exp4) + '} ~=~ ' + gzahl(Rational(fakt1, fakt2))
               + '~' + bas1 + '^{' + gzahl(exp1 - exp3, exp=True) + '}' + bas2 + '^{' + gzahl(exp2 - exp4, exp=True) + '}' + w_erg)
        return aufg, lsg

    def nor_var_bas_fakt():
        ausw_bruch = np.random.choice([2,3,5,7,9], 3, False)
        erw1, erw2 = np.random.choice(range(2, 10), 2, False)
        zaehler1, nenner1 = random.choice([-1,1])*ausw_bruch[0]*erw1, random.choice([-1,1])*ausw_bruch[1]*erw2
        zaehler2, nenner2 = random.choice([-1,1])*erw2, random.choice([-1,1])*ausw_bruch[2]*erw1
        bas = np.random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'],4,False)
        bas.sort()
        bas1, bas2, bas3, bas4 = bas
        list_exp = exponenten(8,2,12, ganzz=True)
        exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 = list_exp
        list_exp_diff = [exp1 - exp3, exp2 - exp4, exp5 - exp7, exp6 - exp8]
        exp_diff1, exp_diff2, exp_diff3, exp_diff4 = list_exp_diff
        if 0 in list_exp_diff:
            w_erg = gzahl(Rational(zaehler1*zaehler2, nenner1*nenner2))
            n = 0
            for element in list_exp_diff:
                if element != 0:
                    w_erg = w_erg + bas[n] + '^{' + gzahl(element) + '}'
                n += 1
        else:
            w_erg = (gzahl(Rational(zaehler1*zaehler2, nenner1*nenner2)) + '~' + bas1 + '^{' + gzahl(exp1 - exp3) + '}'
                     + bas2 + '^{' + gzahl(exp2 - exp4) + '}' + bas3 + '^{' + gzahl(exp5 - exp7) + '}' + bas4 + '^{'
                     + gzahl(exp6 - exp8) + '}')

        aufg = (r' \frac{' + gzahl(zaehler1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2)
                + r'}}{' + gzahl(nenner1) + '~' + bas3 + '^{' + gzahl(exp7) + '}' + bas4 + '^{' + gzahl(exp8)
                + r'}} ~ \cdot ~' + r' \frac{' + gzahl(zaehler2) + '~' + bas3 + '^{' + gzahl(exp5) + r'}' + bas4 + '^{'
                + gzahl(exp6) + r'}}{' + gzahl(nenner2) + '~' + bas1 + '^{' + gzahl(exp3) + '}' + bas2
                + '^{' + gzahl(exp4) + '}}')
        lsg = (r' \frac{' + gzahl(zaehler1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2)
                + r'}}{' + gzahl(nenner1) + '~' + bas3 + '^{' + gzahl(exp7) + '}' + bas4 + '^{' + gzahl(exp8)
                + r'}} ~ \cdot ~' + r' \frac{' + gzahl(zaehler2) + '~' + bas3 + '^{' + gzahl(exp5) + r'}' + bas4 + '^{'
                + gzahl(exp6) + r'}}{' + gzahl(nenner2) + r' \cdot ' + bas1 + '^{' + gzahl(exp3) + '}' + bas2
                + '^{' + gzahl(exp4) + r'}} ~=~ \frac{' + gzahl(zaehler1) + '}{' + gzahl(nenner1) + r'} \cdot \frac{'
                + gzahl(zaehler2) + '}{' + gzahl(nenner2) + '}' + bas1 + '^{' + gzahl(exp1) + vorz_str(-1 * exp3)
               + '}' + bas2 + '^{' + gzahl(exp2) + vorz_str(-1 * exp4) + '}' + bas3 + '^{' + gzahl(exp5)
               + vorz_str(-1 * exp7) + '}' + bas4 + '^{' + gzahl(exp6) + vorz_str(-1 * exp8) + '} ~=~ '
               + w_erg)
        return aufg, lsg

    def schw_var_bas_fakt():
        ausw_bruch = np.random.choice([2,3,5,7,9], 3, False)
        erw1, erw2 = np.random.choice(range(2, 10), 2, False)
        zaehler1, nenner1 = random.choice([-1,1])*ausw_bruch[0]*erw1, random.choice([-1,1])*ausw_bruch[1]*erw2
        zaehler2, nenner2 = random.choice([-1,1])*erw2, random.choice([-1,1])*ausw_bruch[2]*erw1
        bas = np.random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'],4,False)
        bas.sort()
        bas1, bas2, bas3, bas4 = bas
        list_exp = exponenten(8,2,12, ganzz=True)
        exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 = list_exp
        list_exp_diff = [exp1 - exp3, exp2 - exp4, exp5 - exp7, exp6 - exp8]
        exp_diff1, exp_diff2, exp_diff3, exp_diff4 = list_exp_diff
        if 0 in list_exp_diff:
            w_erg = gzahl(Rational(zaehler1*zaehler2, nenner1*nenner2))
            n = 0
            for element in list_exp_diff:
                if element != 0:
                    w_erg = w_erg + bas[n] + '^{' + gzahl(element) + '}'
                n += 1
        else:
            w_erg = (gzahl(Rational(zaehler1*zaehler2, nenner1*nenner2)) + '~' + bas1 + '^{' + gzahl(exp1 - exp3) + '}'
                     + bas2 + '^{' + gzahl(exp2 - exp4) + '}' + bas3 + '^{' + gzahl(exp5 - exp7) + '}' + bas4 + '^{'
                     + gzahl(exp6 - exp8) + '}')

        aufg = (r' \frac{' + gzahl(zaehler1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2)
                + r'}}{' + gzahl(nenner1) + '~' + bas3 + '^{' + gzahl(exp7) + '}' + bas4 + '^{' + gzahl(exp8)
                + r'}} ~ \div ~' + r' \frac{' + gzahl(nenner2) + '~' + bas1 + '^{' + gzahl(exp3) + '}' + bas2
                + '^{' + gzahl(exp4) + r'}}{' + gzahl(zaehler2) + '~' + bas3 + '^{' + gzahl(exp5) + r'}' + bas4 + '^{'
                + gzahl(exp6) + '}}')
        lsg = (r' \frac{' + gzahl(zaehler1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2 + '^{' + gzahl(exp2)
               + r'}}{' + gzahl(nenner1) + '~' + bas3 + '^{' + gzahl(exp7) + '}' + bas4 + '^{' + gzahl(exp8)
               + r'}} ~ \div ~' + r' \frac{' + gzahl(nenner2) + '~' + bas1 + '^{' + gzahl(exp3) + '}' + bas2
               + '^{' + gzahl(exp4) + r'}}{' + gzahl(zaehler2) + '~' + bas3 + '^{' + gzahl(exp5) + r'}' + bas4 + '^{'
               + gzahl(exp6) + r'}} ~=~ \frac{' + gzahl(zaehler1) + '~' + bas1 + '^{' + gzahl(exp1) + r'}' + bas2
               + '^{' + gzahl(exp2) + r'}}{' + gzahl(nenner1) + '~' + bas3 + '^{' + gzahl(exp7) + '}' + bas4 + '^{'
               + gzahl(exp8) + r'}} ~ \cdot ~' + r' \frac{' + gzahl(zaehler2) + '~' + bas3 + '^{' + gzahl(exp5) + r'}'
               + bas4 + '^{' + gzahl(exp6) + r'}}{' + gzahl(nenner2) + r' \cdot ' + bas1 + '^{' + gzahl(exp3) + '}'
               + bas2 + '^{' + gzahl(exp4) + r'}} \\\\ =~ \frac{' + gzahl(zaehler1) + '}{' + gzahl(nenner1)
               + r'} \cdot \frac{' + gzahl(zaehler2) + '}{' + gzahl(nenner2) + '}' + bas1 + '^{' + gzahl(exp1)
               + vorz_str(-1 * exp3) + '}' + bas2 + '^{' + gzahl(exp2) + vorz_str(-1 * exp4) + '}' + bas3 + '^{'
               + gzahl(exp5) + vorz_str(-1 * exp7) + '}' + bas4 + '^{' + gzahl(exp6) + vorz_str(-1 * exp8) + '} ~=~ '
               + w_erg)
        return aufg, lsg

    aufgaben = {'a': pos_zahl_bas_exp, 'b': pos_zahl_bas, 'c': neg_zahl_bas, 'd': bel_zahl_bas,
                'e': var_bas_pos_exp, 'f': var_bas_exp, 'g': triv_var_bas_fakt, 'h': einf_var_bas_fakt,
                'i': nor_var_bas_fakt, 'j': schw_var_bas_fakt}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if element not in ['h', 'i', 'j']:
            if (i+1) % 4 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
            elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
        if element not in ['h', 'i', 'j']:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
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

def potenzgesetz_eins_erw(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS zwei Potenzen multiplizieren, deren Exponenten aus rationalen Zahlen (Brüchen) besteht.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Potenzen mit nat. Zahlen und gleichnamigen positiven rationalen Exponenten
    # b) Potenzen mit nat. Zahlen und gleichnamigen rationalen Exponenten
    # c) Potenzen mit Variablen und gleichnamigen positiven rationalen Exponenten
    # d) Potenzen mit Variablen und gleichnamigen rationalen Exponenten
    # e) Potenzen mit nat. Zahlen und ungleichnamigen positiven rationalen Exponenten
    # f) Potenzen mit nat. Zahlen und ungleichnamigen rationalen Exponenten
    # g) Potenzen mit Variablen und ungleichnamigen positiven rationalen Exponenten
    # h) Potenzen mit Variablen und ungleichnamigen rationalen Exponenten
    # i) Potenzen mit Variablen und ungleichnamigen positiven rationalen Exponenten, dargestellt als Wurzel
    # j) Potenzen mit Variablen und ungleichnamigen rationalen Exponenten, dargestellt als Quostient und Wurzel
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def pos_zahl_und_gln_exp(): # Teilaufgabe a)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(zaehler_1+zaehler_2,nenner)
        bas = nzahl(2,8)
        aufg = (gzahl(bas) + '^{' + exp1 + r'} \cdot ' + gzahl(bas) + '^{' + exp2 + '} ~')
        lsg = (gzahl(bas) + '^{' + exp1 + r'} \cdot ' + gzahl(bas) + '^{' + exp2 + '} ~=~ ' + gzahl(bas)
               + '^{' + exp1 + '+' + exp2 + '} ~=~ ' + gzahl(bas) + '^{' + gzahl(erg) + '}')
        return aufg, lsg

    def zahl_gln_exp(): # Teilaufgabe b)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(vorz1*zaehler_1 + vorz2*zaehler_2, nenner)
        bas = nzahl(2,8)
        if erg == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot ' + gzahl(bas) + '^{' + vorz_aussen(vorz2)
                + exp2 + '} ~')
        lsg = (gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot ' + gzahl(bas) + '^{' + vorz_aussen(vorz2)
               + exp2 + '} ~=~ ' + gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + vorz(vorz2) + exp2 + '} ~=~ '
               + gzahl(bas) + '^{' + gzahl(erg, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_pos_gln_exp(): # Teilaufgabe c)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(zaehler_1+zaehler_2,nenner)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = (bas + '^{' + exp1 + r'} \cdot ' + bas + '^{' + exp2 + '} ~')
        lsg = (bas + '^{' + exp1 + r'} \cdot ' + bas + '^{' + exp2 + '} ~=~ ' + bas + '^{' + exp1 + '+' + exp2
               + '} ~=~ ' + bas + '^{' + gzahl(erg, exp=True) + '}')
        return aufg, lsg

    def var_gln_exp(): # Teilaufgabe d)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(vorz1*zaehler_1 + vorz2*zaehler_2, nenner)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        if erg == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (bas + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot ' + bas + '^{' + vorz_aussen(vorz2) + exp2 + '} ~')
        lsg = (bas + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot ' + bas + '^{' + vorz_aussen(vorz2) + exp2
               + '} ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1 + vorz(vorz2) + exp2 + '} ~=~ '
               + bas + '^{' + gzahl(erg, exp=True) + '}' + w_erg)
        return aufg, lsg

    def pos_zahl_und_ungln_exp(): # Teilaufgabe e)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = (nenner / nenner_1) * zaehler_1
        zaehler_2_erw = (nenner / nenner_2) * zaehler_2
        bas = nzahl(2, 8)
        exp1, exp2 = Rational(zaehler_1, nenner_1), Rational(zaehler_2, nenner_2)
        aufg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~' + gzahl(bas) + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + gzahl(bas) + '^{'
               + gzahl(exp1 + exp2) + '}')
        return aufg, lsg

    def zahl_ungln_exp():  # Teilaufgabe f)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = nzahl(2, 6)
        exp1, exp2 = Rational(vorz1 * zaehler_1, nenner_1), Rational(vorz2 * zaehler_2, nenner_2)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~')
        lsg = (gzahl(bas) + '^{' + gzahl(exp1) + r'} \cdot ' + gzahl(bas) + '^{' + gzahl(exp2) + '} ~=~ ' + gzahl(bas)
               + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~' + gzahl(bas) + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + gzahl(bas) + '^{'
               + gzahl(exp1 + exp2) + '}' + w_erg)
        return aufg, lsg

    def var_pos_ungln_exp():  # Teilaufgabe g)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        exp1, exp2 = Rational(zaehler_1, nenner_1), Rational(zaehler_2, nenner_2)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~')
        lsg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~=~ ' + bas
               + '^{' + gzahl(exp1) + vorz_str(exp2) + r'}  ~=~ ' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(exp1 + exp2) + '}')
        return aufg, lsg

    def var_ungln_exp(): # Teilaufgabe h)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = Rational(vorz1 * zaehler_1, nenner_1), Rational(vorz2 * zaehler_2, nenner_2)
        exp1_erw, exp2_erw = Rational(vorz1 * zaehler_1_erw, nenner), Rational(vorz2 * zaehler_2_erw, nenner)
        if exp1 + exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~')
        lsg = (bas + '^{' + gzahl(exp1) + r'} \cdot ' + bas + '^{' + gzahl(exp2) + '} ~=~ ' + bas
               + '^{' + gzahl(exp1) + vorz_str(exp2) + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(exp1 + exp2) + '}'
               + w_erg)
        return aufg, lsg

    def var_pos_sqrt(): # Teilaufgabe i)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1 = r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + '}'
        exp2 = r' \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + '}'
        pot1 = r' \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}'
        pot2 = r' \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}'

        erg = Rational(zaehler_1 * nenner_2 + zaehler_2 * nenner_1, nenner_1 * nenner_2)
        exp1_erw, exp2_erw = Rational(zaehler_1_erw, nenner), Rational(zaehler_2_erw, nenner)
        aufg = pot1 + r'~ \cdot ~' + pot2
        lsg = (pot1 + r'~ \cdot ~' + pot2 + '~=~' + bas + '^{' + exp1 + r'} \cdot ' + bas + '^{' + exp2 + '} ~=~ '
               + bas + '^{' + exp1 + '+' + exp2 + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(erg, exp=True) + '}')
        return aufg, lsg

    def var_sqrt(): # Teilaufgabe j)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1 = r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + '}'
        exp2 = r' \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + '}'
        if vorz1 == -1:
            pot1 = r' \frac{1}{ \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}}'
        else:
            pot1 = r' \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}'
        if vorz2 == -1:
            pot2 = r' \frac{1}{ \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}}'
        else:
            pot2 = r' \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}'

        erg = Rational(vorz1*zaehler_1*nenner_2 + vorz2*zaehler_2*nenner_1,nenner_1*nenner_2)
        if zaehler_1/nenner_1 + zaehler_2/nenner_2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = pot1 + r'~ \cdot ~' + pot2
        lsg = (pot1 + r'~ \cdot ~' + pot2 + r' ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot ' + bas
               + '^{' + vorz(vorz2) + exp2 + '} ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1 + vorz(vorz2) + exp2
               + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw) + vorz_str(zaehler_2_erw) + '}{'
               + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(erg, exp=True) + '}' + w_erg)
        return aufg, lsg

    aufgaben = {'a': pos_zahl_und_gln_exp, 'b': zahl_gln_exp, 'c': var_pos_gln_exp, 'd': var_gln_exp,
                'e': pos_zahl_und_ungln_exp, 'f': zahl_ungln_exp, 'g': var_pos_ungln_exp, 'h': var_ungln_exp,
                'i': var_pos_sqrt, 'j': var_sqrt}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 4 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
        if element not in ['i', 'j']:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
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

def potenzgesetz_eins_mehrfach(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS mehrere Potenzen, mit verschiedenen Exponenten, multiplizieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) vier Faktoren aus zwei Basen und ganzzahligen Exponenten
    # b) sechs Faktoren aus zwei Basen und ganzzahligen Exponenten
    # c) sechs Faktoren aus drei Basen und ganzzahligen Exponenten
    # d) vier Faktoren aus zwei Basen und rationalen Exponenten
    # e) sechs Faktoren aus drei Basen und rationalen Exponenten
    # f) vier Faktoren aus zwei Basen und rationalen Exponenten (als Dezimalbruch)
    # g) sechs Faktoren aus drei Basen und rationalen Exponenten (als Dezimalbruch)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def aufg_lsg(exp, anz_bas):
        ar_ausw_bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'], anz_bas, False)
        ausw_bas = [element for element in ar_ausw_bas]
        list_basen = ausw_bas.copy()
        for step in range(len(exp)-len(ausw_bas)):
            random.shuffle(ausw_bas)
            list_basen.append(random.choice(ausw_bas))
        bas_exp = [[list_basen[k], exp[k]] for k in range(len(exp))]
        random.shuffle(bas_exp)
        ausw_bas.sort()
        aufg = ''
        m = 1
        for element in bas_exp:
            if m != len(bas_exp):
                aufg = aufg + element[0] + '^{' + gzahl(element[1]) + r'}~ \cdot ~'
            else:
                aufg = aufg + element[0] + '^{' + gzahl(element[1]) + '}'
            m += 1
        lsg = aufg + '~=~'
        exp_sort = []
        for basis in ausw_bas:
            exp_der_basis = []
            for element in bas_exp:
                if basis == element[0]:
                    exp_der_basis.append(element[1])
            lsg = lsg + basis + '^{' + gzahl(exp_der_basis[0])
            k = 1
            for zahl in range(len(exp_der_basis) - 1):
                lsg = lsg + vorz_str(exp_der_basis[k])
                k += 1
            lsg = lsg + '}'
            if basis != ausw_bas[-1]:
                lsg = lsg + r'~ \cdot ~'
            exp_sort.append(exp_der_basis)
        lsg = lsg + '~=~'
        k = 0
        for basis in ausw_bas:
            if basis != ausw_bas[-1]:
                if sum(exp_sort[k]) == 0:
                    pass
                else:
                    lsg = lsg + basis + '^{' + gzahl(sum(exp_sort[k])) + r'} \cdot '
            else:
                if sum(exp_sort[k]) == 0:
                    pass
                else:
                    lsg = lsg + basis + '^{' + gzahl(sum(exp_sort[k])) + '}'
            k += 1

        return aufg, lsg

    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    aufgaben = {'a': [aufg_lsg, [zzahl(2,9) for zahl in range(4)], 2],
                'b': [aufg_lsg, [zzahl(2,9) for zahl in range(6)], 2],
                'c': [aufg_lsg, [zzahl(2,9) for zahl in range(6)], 3],
                'd': [aufg_lsg, [Rational(nzahl(1,9), nzahl(2,9)) for zahl in range(4)], 2],
                'e': [aufg_lsg, [Rational(nzahl(1,9), nzahl(2,9)) for zahl in range(6)], 3],
                'f': [aufg_lsg, [zzahl(2,9)/10 for zahl in range(4)], 2],
                'g': [aufg_lsg, [zzahl(2,9)/10 for zahl in range(6)], 3]}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element][0](aufgaben[element][1], aufgaben[element][2])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i+1) % 2 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        elif i+1 != len(teilaufg):
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

def potenzgesetz_zwei_erw(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS zwei Potenzen dividieren, deren Exponenten aus rationalen Zahlen (Brüchen) besteht.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Potenzen mit nat. Zahlen und gleichnamigen positiven rationalen Exponenten
    # b) Potenzen mit nat. Zahlen und gleichnamigen rationalen Exponenten
    # c) Potenzen mit Variablen und gleichnamigen positiven rationalen Exponenten
    # d) Potenzen mit Variablen und gleichnamigen rationalen Exponenten
    # e) Potenzen mit nat. Zahlen und ungleichnamigen positiven rationalen Exponenten
    # f) Potenzen mit nat. Zahlen und ungleichnamigen rationalen Exponenten
    # g) Potenzen mit Variablen und ungleichnamigen positiven rationalen Exponenten
    # h) Potenzen mit Variablen und ungleichnamigen rationalen Exponenten
    # i) Potenzen mit Variablen und ungleichnamigen positiven rationalen Exponenten, dargestellt als Wurzel
    # j) Potenzen mit Variablen und ungleichnamigen rationalen Exponenten, dargestellt als Quotient und Wurzel
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def pos_zahl_und_gln_exp(): # Teilaufgabe a)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(zaehler_1-zaehler_2,nenner)
        bas = nzahl(2,8)
        aufg = r' \frac{' + (gzahl(bas) + '^{' + exp1 + r'}}{' + gzahl(bas) + '^{' + exp2 + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + exp1 + r'}}{' + gzahl(bas) + '^{' + exp2 + '}} ~=~ ' + gzahl(bas)
               + '^{' + exp1 + '-' + exp2 + '} ~=~ ' + gzahl(bas) + '^{' + gzahl(erg, exp=True) + '}')
        return aufg, lsg

    def zahl_gln_exp(): # Teilaufgabe b)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(vorz1*zaehler_1 - vorz2*zaehler_2, nenner)
        bas = nzahl(2,8)
        if erg == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + r'}}{' + gzahl(bas) + '^{'
                + vorz_aussen(vorz2) + exp2 + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + r'}}{' + gzahl(bas) + '^{'
               + vorz_aussen(vorz2) + exp2 + '}} ~=~ ' + gzahl(bas) + '^{' + vorz_aussen(vorz1) + exp1 + vorz(-1*vorz2)
               + exp2 + '} ~=~ ' + gzahl(bas) + '^{' + gzahl(erg, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_pos_gln_exp(): # Teilaufgabe c)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(zaehler_1-zaehler_2,nenner)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = (r' \frac{' + bas + '^{' + exp1 + '}}{' + bas + '^{' + exp2 + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + exp1 + r'}}{' + bas + '^{' + exp2 + '}} ~=~ ' + bas + '^{' + exp1 + '-' + exp2
               + '} ~=~ ' + bas + '^{' + gzahl(erg, exp=True) + '}')
        return aufg, lsg

    def var_gln_exp(): # Teilaufgabe d)
        zaehler_1, zaehler_2, nenner = np.random.choice(range(2,12), 3, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        exp1 = r' \frac{' + str(zaehler_1) + '}{' + str(nenner) + '}'
        exp2 = r' \frac{' + str(zaehler_2) + '}{' + str(nenner) + '}'
        erg = Rational(vorz1*zaehler_1 - vorz2*zaehler_2,nenner)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        if erg == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + bas + '^{' + vorz_aussen(vorz1) + exp1 + r'}}{' + bas + '^{' + vorz_aussen(vorz2)
                + exp2 + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + vorz_aussen(vorz1) + exp1 + r'}}{' + bas + '^{' + vorz_aussen(vorz2)
               + exp2 + '}} ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1 + vorz(-1*vorz2) + exp2 + '} ~=~ '
               + bas + '^{' + gzahl(erg, exp=True) + '}' + w_erg)
        return aufg, lsg

    def pos_zahl_und_ungln_exp(): # Teilaufgabe e)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = (nenner / nenner_1) * zaehler_1
        zaehler_2_erw = (nenner / nenner_2) * zaehler_2
        bas = nzahl(2, 8)
        exp1, exp2 = Rational(zaehler_1, nenner_1), Rational(zaehler_2, nenner_2)
        aufg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}}{' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}}{' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~=~ '
               + gzahl(bas) + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~' + gzahl(bas) + r'^{ \frac{'
               + gzahl(zaehler_1_erw) + vorz_str(-1*zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + gzahl(bas)
               + '^{' + gzahl(exp1 - exp2, exp=True) + '}')
        return aufg, lsg

    def zahl_ungln_exp():  # Teilaufgabe f)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = nzahl(2, 6)
        exp1, exp2 = Rational(vorz1 * zaehler_1, nenner_1), Rational(vorz2 * zaehler_2, nenner_2)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}}{' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + gzahl(bas) + '^{' + gzahl(exp1) + r'}}{' + gzahl(bas) + '^{' + gzahl(exp2) + '}} ~=~ '
               + gzahl(bas) + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~' + gzahl(bas) + r'^{ \frac{'
               + gzahl(zaehler_1_erw) + vorz_str(-1 * zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + gzahl(bas)
               + '^{' + gzahl(exp1 - exp2, exp=True) + '}' + w_erg)
        return aufg, lsg

    def var_pos_ungln_exp():  # Teilaufgabe g)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        exp1, exp2 = Rational(zaehler_1, nenner_1), Rational(zaehler_2, nenner_2)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}}{' + bas + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}}{' + bas + '^{' + gzahl(exp2) + '}} ~=~ ' + bas + '^{'
               + gzahl(exp1) + vorz_str(-1*exp2) + r'}  ~=~ ' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(-1 * zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{'
               + gzahl(exp1 - exp2, exp=True) + '}')
        return aufg, lsg

    def var_ungln_exp(): # Teilaufgabe h)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1, exp2 = Rational(vorz1 * zaehler_1, nenner_1), Rational(vorz2 * zaehler_2, nenner_2)
        if exp1 - exp2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}}{' + bas + '^{' + gzahl(exp2) + '}} ~')
        lsg = (r' \frac{' + bas + '^{' + gzahl(exp1) + r'}}{ ' + bas + '^{' + gzahl(exp2) + '}} ~=~ ' + bas
               + '^{' + gzahl(exp1) + vorz_str(-1*exp2) + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(-1*zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{'
               + gzahl(exp1 - exp2, exp=True) + '}'
               + w_erg)
        return aufg, lsg

    def var_pos_sqrt(): # Teilaufgabe i)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = nenner / nenner_1 * zaehler_1
        zaehler_2_erw = nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1 = r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + '}'
        exp2 = r' \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + '}'
        pot1 = r' \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}'
        pot2 = r' \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}'

        erg = Rational(zaehler_1 * nenner_2 - zaehler_2 * nenner_1, nenner_1 * nenner_2)
        aufg = r' \frac{~' + pot1 + r'~}{~' + pot2 + '~}'
        lsg = (r' \frac{' + pot1 + r'~ }{ ~' + pot2 + r'} ~=~ \frac{' + bas + '^{' + exp1 + r'}}{' + bas + '^{' + exp2
               + '}} ~=~ ' + bas + '^{' + exp1 + '-' + exp2 + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(-1 * zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(erg, exp=True)
               + '}')
        return aufg, lsg

    def var_sqrt(): # Teilaufgabe j)
        zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        while (zaehler_1 / nenner_1) % 1 == 0 or (zaehler_2 / nenner_2) % 1 == 0:
            zaehler_1, zaehler_2, nenner_1, nenner_2 = np.random.choice(range(2, 12), 4, False)
        vorz1, vorz2 = np.random.choice([1, -1], 2, True)
        nenner = kgv(nenner_1, nenner_2)
        zaehler_1_erw = vorz1 * nenner / nenner_1 * zaehler_1
        zaehler_2_erw = vorz2 * nenner / nenner_2 * zaehler_2
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        exp1 = r' \frac{' + gzahl(zaehler_1) + '}{' + gzahl(nenner_1) + '}'
        exp2 = r' \frac{' + gzahl(zaehler_2) + '}{' + gzahl(nenner_2) + '}'
        if vorz1 == -1:
            pot1 = r' \frac{1}{ \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}}'
        else:
            pot1 = r' \sqrt[' + gzahl(nenner_1) + ']{' + bas + '^{' + gzahl(zaehler_1) + '}}'
        if vorz2 == -1:
            pot2 = r' \frac{1}{ \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}}'
        else:
            pot2 = r' \sqrt[' + gzahl(nenner_2) + ']{' + bas + '^{' + gzahl(zaehler_2) + '}}'

        erg = Rational(vorz1*zaehler_1*nenner_2 - vorz2*zaehler_2*nenner_1,nenner_1*nenner_2)
        if zaehler_1/nenner_1 -zaehler_2/nenner_2 == 0:
            w_erg = '~=~ 1'
        else:
            w_erg = ''
        aufg = r' \frac{' + pot1 + r'~ }{ ~' + pot2 + '}'
        lsg = (r' \frac{' + pot1 + r'~ }{ ~' + pot2 + r'} ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1 + r'} \cdot '
               + bas + '^{' + vorz(-1*vorz2) + exp2 + '} ~=~ ' + bas + '^{' + vorz_aussen(vorz1) + exp1
               + vorz(-1 * vorz2) + exp2 + '} ~=~' + bas + r'^{ \frac{' + gzahl(zaehler_1_erw)
               + vorz_str(-1 * zaehler_2_erw) + '}{' + gzahl(nenner) + '}} ~=~' + bas + '^{' + gzahl(erg, exp=True)
               + '}' + w_erg)
        return aufg, lsg

    aufgaben = {'a': pos_zahl_und_gln_exp, 'b': zahl_gln_exp, 'c': var_pos_gln_exp, 'd': var_gln_exp,
                'e': pos_zahl_und_ungln_exp, 'f': zahl_ungln_exp, 'g': var_pos_ungln_exp, 'h': var_ungln_exp,
                'i': var_pos_sqrt, 'j': var_sqrt}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 4 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 4 == 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
        if element not in ['i', 'j']:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
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

def potenzgesetz_drei_vier(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS das Produkt und die Potenz mehrerer Potenzen multiplizieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Potenz einer Potenz mit ganzzahligen Exponenten
    # b) Potenz einer Potenz mit positiven rationalen Exponenten
    # c) Potenz einer Potenz mit rationalen Exponenten
    # d) Produkt zweier Potenzen mit gleichem ganzzahligem Exponenten
    # e) Produkt zweier Potenzen mit gleichem rationalen Exponenten
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def var_pot_ganzz_exp(): # Teilaufgabe a)
        exp1, exp2 = exponenten(2)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = r' \left( ~' + bas + r'^{' + gzahl(exp1) + r'}~ \right) ^{' + gzahl(exp2) + '}'
        lsg = (r' \left( ' + bas + r'^{' + gzahl(exp1) + r'} \right) ^{' + gzahl(exp2) + '} ~=~' + bas + r'^{'
               + gzahl(exp1) + r' \cdot ' + gzahl(exp2) + r'} ~=~' + bas + '^{' + gzahl(exp1*exp2, exp=True) + '}')
        return aufg, lsg

    def var_pot_pos_rat_exp(): # Teilaufgabe b)
        zaehler_1,nenner_1 = random_selection([1, 2, 3, 5, 7], 2, False)
        zaehler_2,nenner_2 = random_selection([1, 2, 3, 5, 7], 2, False)
        fakt1, fakt2 = random_selection(list(range(1, 8)), 2, False)
        exp1 = r' \frac{' + str(fakt1*zaehler_1) + '}{' + str(fakt2*nenner_1) + '}'
        exp2 = r' \frac{' + str(fakt2*zaehler_2) + '}{' + str(fakt1*nenner_2) + '}'
        erg = gzahl(Rational(zaehler_1*zaehler_2,nenner_1*nenner_2))
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = r' \left( ~' + bas + r'^{' + exp1 + r'}~ \right) ^{' + exp2 + '}'
        lsg = (r' \left(' + bas + r'^{' + exp1 + r'} \right) ^{' + exp2 + '} ~=~' + bas + r'^{' + exp1
               + r' \cdot' + exp2 + r'} ~=~' + bas + '^{' + erg + '}')
        return aufg, lsg

    def var_pot_rat_exp(): # Teilaufgabe c)
        zaehler_1,nenner_1 = random_selection([1, 2, 3, 5, 7], 2, False)
        zaehler_2,nenner_2 = random_selection([1, 2, 3, 5, 7], 2, False)
        vorz1, vorz2 = random_selection([-1, 1], 2, True)
        fakt1, fakt2 = random_selection(list(range(1, 8)), 2, False)
        exp1 = r' \frac{' + str(fakt1*zaehler_1) + '}{' + str(fakt2*nenner_1) + '}'
        exp2 = r' \frac{' + str(fakt2*zaehler_2) + '}{' + str(fakt1*nenner_2) + '}'
        erg = gzahl(Rational(vorz1*zaehler_1*vorz2*zaehler_2,nenner_1*nenner_2), exp=True)
        bas = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = (r' \left( ~' + bas + r'^{' + vorz_aussen(vorz1) + exp1 + r'} \right) ~ ^{' + vorz_aussen(vorz2) + exp2
                + '}')
        lsg = (r' \left(' + bas + r'^{' + vorz_aussen(vorz1) + exp1 + r'} \right) ^{' + vorz_aussen(vorz2) + exp2
               + '} ~=~' + bas + r'^{ \left(' + vorz_v_aussen(vorz1*vorz2, exp1) + r' \cdot' + exp2
               + r' \right) } ~=~' + bas + '^{' + erg + '}')
        return aufg, lsg

    def mult_var_ganzz_exp(): # Teilaufgabe d)
        fakt = zzahl(2,9)
        bas1, bas2 = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'], 2, False)
        aufg = bas1 + r'^{' + gzahl(fakt) + r'}~ \cdot ~' + bas2 + r'^{' + gzahl(fakt) + r'}'
        lsg = (bas1 + r'^{' + gzahl(fakt) + r'} \cdot ' + bas2 + r'^{' + gzahl(fakt) + r'} ~=~ \left(' + bas1 + bas2
               + r' \right)^{' + gzahl(fakt) + r'}')
        return aufg, lsg

    def mult_var_rat_exp(): # Teilaufgabe d)
        zaehler, nenner = random_selection(list(range(2,12)), 2, False)
        bas1, bas2 = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'], 2, False)
        aufg = (bas1 + r'^{ \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner) + r'}}~ \cdot ~' + bas2 + r'^{ \frac{'
                + gzahl(zaehler) + '}{' + gzahl(nenner) + r'}}')
        lsg = (bas1 + r'^{ \frac{' + gzahl(zaehler) + '}{' + gzahl(nenner) + r'}} \cdot ' + bas2 + r'^{ \frac{'
               + gzahl(zaehler) + '}{' + gzahl(nenner) + r'}} ~=~ \left(' + bas1 + bas2 + r' \right)^{'
               + gzahl(Rational(zaehler, nenner), exp=True) + r'}')
        return aufg, lsg

    aufgaben = {'a': var_pot_ganzz_exp, 'b': var_pot_pos_rat_exp, 'c': var_pot_rat_exp,
                'd': mult_var_ganzz_exp, 'e': mult_var_rat_exp}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 3 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
        if (i + 1) % 2 != 0 and i + 1 < len(teilaufg):
            lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 2 == 0 and i + 1 < len(teilaufg):
            lsg = lsg + r' \\\\'
        else:
            pass
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

def wiss_schreibweise(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS Zahlen in wissenschaftliche Schreibweise oder als Dezimalzahl umformen.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) grosse natürliche Zahl in wissenschaftliche Schreibweise (exp > 5) umformen
    # b) grosse Zahl in wissenschaftliche Schreibweise (exp > 5) in eine natürliche Zahl umformen
    # c) kleine natürliche Zahl in wissenschaftliche Schreibweise (exp < 0) umformen
    # d) kleine Zahl in wissenschaftliche Schreibweise (exp < 0) in Dezimalzahl umformen
    # e) Dezimalzahl in wissenschaftliche Schreibweise (1 < exp < 5) umformen
    # e) Zahl in wissenschaftliche Schreibweise (1 < exp < 5) in Dezimalzahl umformen
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Notiere die gegebene Zahl in wissenschaftlicher Schreibweise bzw. als Dezimalbruch.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def zahldarstellung(exp, art_ein):
        zp, komma, zahl = nzahl(2, 5), nzahl(0,2), nzahl(1, 9)
        art_aus = 'wiss'
        art_aus = 'dezi' if art_ein != 'dezi' else art_aus
        for k in range(zp):
            zahl += nzahl(1, 9) * 10 ** k
        aufg = darstellung_zahl(zahl, exponent=(zp+exp-komma), darstellung=art_ein)
        lsg = aufg + '~=~' + darstellung_zahl(zahl, exponent=(zp+exp-komma), darstellung=art_aus)
        return aufg, lsg

    aufgaben = {'a': [nzahl(6,12), 'dezi'],
                'b': [nzahl(6,12), 'wiss'],
                'c': [-1* nzahl(6,12), 'dezi'],
                'd': [-1*nzahl(6,12), 'wiss'],
                'e': [0, 'dezi'],
                'f': [0, 'wiss']}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = zahldarstellung(aufgaben[element][0], aufgaben[element][1])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if (i+1) % 2 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
            lsg = lsg + r' \hspace{2em} '
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

def einheiten_umrechnen(nr, teilaufg=['a', 'b', 'c', 'd'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS gegebenen Zahlen mit verschiedenen Vorsätzen einer Einheit ineinander umrechnen.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Umrechnen von physikalischen Einheiten wie s, V oder W
    # b) Umrechnen von Längeneinheiten
    # c) Umrechnen von Flächeneinheiten
    # d) Umrechnen von Volumeneinheiten
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Rechne um.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def vorsaetze(n, p=1):
        if p == 1:
            return random_selection([['n', -9], [r' \mu ', -6], ['m', -3], ['c', -2], ['d', -1], ['k', 3]], n, False)
        elif p == 2:
            return random_selection([['p', -12], ['n', -9], [r' \mu', -6], ['m', -3], ['c', -2], ['d', -1],
                                         ['k', 3], ['M', 6], ['G', 9], ['T', 12]], n, False)
        elif p == 3:
            return random_selection([['p', -12], ['n', -9], [r' \mu', -6], ['m', -3], ['c', -2], ['d', -1],
                                         ['da', 1], ['h', 2], ['k',3], ['M', 6], ['G', 9], ['T', 12]], n, False)
        else:
            print('p muss 1, 2 odere 3 sein.')


    def bel_groessen():
        vors = [['p', -12], ['n', -9], [r' \mu ', -6], ['m', -3], ['k', 3], ['M', 6], ['G', 9], ['T', 12]]
        ausw_gr = random.choice(['s', 'J', 'N', 'C', 'V', 'A', 'W'])
        ausw = nzahl(0,7)
        komma = nzahl(1,2)
        exp = vors[ausw][1]
        anz_ziffern = nzahl(1, 2)
        zahl = nzahl(1,9)
        for step in range(anz_ziffern):
            zahl = zahl + nzahl(1,9) * 10**(step+1)
        zahl_str = darstellung_zahl(zahl, exponent=anz_ziffern-exp-komma, darstellung='dezi')
        aufg = (zahl_str + '~' + vors[ausw][0] + ausw_gr + r'~=~ ...' + ausw_gr)
        lsg = (zahl_str + '~' + vors[ausw][0] + ausw_gr + r'~=~' + zahl_str + r' \cdot 10^{' + gzahl(exp) + '}~'
               + ausw_gr + '~=~' + gzahl(zahl*10**(-1*komma)) + '~' + ausw_gr)
        return aufg, lsg

    def laengen():
        vors = [['n', -9], [r' \mu ', -6], ['m', -3], ['c', -2], ['d', -1], ['k', 3]]
        ausw, schritt, komma = nzahl(0, 5), nzahl(1,2), nzahl(1,2)
        schritt = -1 * nzahl(1,2) if ausw >= 3 else schritt
        vors1, exp1, vors2, exp2 = vors[ausw][0], vors[ausw][1], vors[ausw+schritt][0], vors[ausw+schritt][1]
        anz_ziffern, zahl = nzahl(1, 2), nzahl(1,9)
        exp_anf = exp2-exp1-komma
        for step in range(anz_ziffern):
            zahl = zahl + nzahl(1,9) * 10**(step+1)
        zahl_str_anf = darstellung_zahl(zahl, exponent=exp2-exp1-komma+anz_ziffern, darstellung='dezi')
        zahl_str_erg = gzahl(zahl * (10 ** (-1*komma)))
        aufg = zahl_str_anf + '~' + vors1 + r'm ~=~ ...' + vors2 + 'm'
        lsg = (zahl_str_anf + '~' + vors1 + r' m ~=~' + zahl_str_anf + r' \cdot \frac{10^{'
               + gzahl(exp1) + '}}{10^{' + gzahl(exp2) + r'}} \cdot 10^{' + gzahl(exp2)
               + r'}~ m ~=~' + zahl_str_erg + '~' + vors2 + 'm')
        return aufg, lsg

    def flaechen():
        ausw = random.randint(0,5)
        vors = [['n', -9], [r' \mu ', -6], ['m', -3], ['c', -2], ['d', -1], ['k', 3]]
        ausw, schritt, komma = nzahl(0, 5), nzahl(1,2), nzahl(1,2)
        schritt = -1 * nzahl(1,2) if ausw >= 3 else schritt
        vors1, exp1, vors2, exp2 = vors[ausw][0], vors[ausw][1], vors[ausw + schritt][0], vors[ausw + schritt][1]
        anz_ziffern, zahl = nzahl(1, 2), nzahl(1, 9)
        exp_anf = exp2 - exp1 - komma
        for step in range(anz_ziffern):
            zahl = zahl + nzahl(1, 9) * 10 ** (step + 1)
        zahl_str_anf = darstellung_zahl(zahl, exponent=((exp2*2 - exp1*2) - komma + anz_ziffern), darstellung='dezi')
        zahl_str_erg = gzahl(zahl * (10 ** (-1 * komma)))
        aufg = zahl_str_anf + '~' + vors1 + r'm^2 ~=~ ...' + vors2 + 'm^2'
        lsg = (zahl_str_anf + '~' + vors1 + r'm^2 ~=~' + zahl_str_anf + r' \cdot \frac{(10^{'
               + gzahl(exp1) + '})^2}{(10^{' + gzahl(exp2) + r'})^2} \cdot (10^{' + gzahl(exp2)
               + r'})^2~ m^2 ~=~' + zahl_str_erg + '~' + vors2 + 'm^2')
        return aufg, lsg

    def volumen():
        ausw = random.randint(0,5)
        vors = [['n', -9], [r' \mu ', -6], ['m', -3], ['c', -2], ['d', -1], ['k', 3]]
        ausw, schritt, komma = nzahl(0, 5), 1, nzahl(1,2)
        schritt = -1 if ausw >= 3 else schritt
        vors1, exp1, vors2, exp2 = vors[ausw][0], vors[ausw][1], vors[ausw + schritt][0], vors[ausw + schritt][1]
        anz_ziffern, zahl = nzahl(1, 2), nzahl(1, 9)
        exp_anf = exp2 - exp1 - komma
        for step in range(anz_ziffern):
            zahl = zahl + nzahl(1, 9) * 10 ** (step + 1)
        zahl_str_anf = darstellung_zahl(zahl, exponent=((exp2*3 - exp1*3) - komma + anz_ziffern), darstellung='dezi')
        zahl_str_erg = gzahl(zahl * (10 ** (-1 * komma)))
        aufg = zahl_str_anf + '~' + vors1 + r'm^3 ~=~ ...' + vors2 + 'm^3'
        lsg = (zahl_str_anf + '~' + vors1 + r'm^3 ~=~' + zahl_str_anf + r' \cdot \frac{(10^{'
               + gzahl(exp1) + '})^3}{(10^{' + gzahl(exp2) + r'})^3} \cdot (10^{' + gzahl(exp2)
               + r'})^3~ m^3 ~=~' + zahl_str_erg + '~' + vors2 + 'm^3')
        return aufg, lsg

    aufgaben = {'a': bel_groessen, 'b': laengen, 'c': flaechen, 'd': volumen}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]()
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i+1) % 2 != 0 and i+1 < len(teilaufg):
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

def schreibweise_prozent_dezimal(nr, teilaufg=['a', 'b', 'c', 'd'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die SuS gegebenen Zahlen in Prozent-, Bruch- und Dezimalschreibweise umwandeln
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.



    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 26 if anzahl > 26 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    elif wdh != False:
        teilaufg = repeat(teilaufg, wdh)
    anz_teilaufg = Counter(teilaufg)
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen einfache Dezimalbrüche in Bruch- und Prozentschreibweise notieren
        anz_aufg = anz_teilaufg['a'] if anz_teilaufg['a'] < 10 else 10
        zahlen = random_selection([element*5 for element in range(1,20)], anz_aufg, wdh=False)
        aufgabe.append('Notiere in Bruch- und Prozentschreibweise.')
        lsg = text = ''
        for step in range(anz_aufg):
            text += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step] / 100)
                     + r' ~=~ \frac{ \hspace{2em} }{100} ~=~ \hspace{2em} \% ')
            lsg += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step] / 100) + r' ~=~ \frac{ '
                    + gzahl(zahlen[step]) + ' }{100} ~=~ ' + gzahl(zahlen[step]) + r' \% ')
            text += r' \hspace{5em} ' if step % 2 == 0 else r' \\\\ '
            lsg += r' \hspace{5em} ' if step % 2 == 0 else r' \\ '
            i += 1
        if anz_aufg % 2 != 0:
            text += r' \hspace{12em} '
            lsg += r' \hspace{11em} '
        aufgabe.append(text)
        loesung.append(lsg)
    if 'b' in teilaufg:
        # Die SuS sollen einfache  in Bruch- und Prozentschreibweise notieren
        anz_aufg = anz_teilaufg['b'] if anz_teilaufg['b'] < 10 else 10
        zahlen = random_selection([element*5 for element in range(1,20)], anz_aufg, wdh=False)
        aufgabe.append('Notiere als Bruch und Dezimalbruch.')
        lsg = text = ''
        for step in range(anz_aufg):
            text += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step])
                     + r' \% ~=~ \frac{ \hspace{2em} }{100} ~=~ \hspace{2em} ')
            lsg += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step]) + r' \% ~=~ \frac{ '
                    + gzahl(zahlen[step]) + ' }{100} ~=~ ' + gzahl(zahlen[step] / 100))
            text += r' \hspace{5em} ' if step % 2 == 0 else r' \\\\ '
            lsg += r' \hspace{5em} ' if step % 2 == 0 else r' \\ '
            i += 1
        if anz_aufg % 2 != 0:
            text += r' \hspace{12em} '
            lsg += r' \hspace{11em} '
        aufgabe.append(text)
        loesung.append(lsg)
    if 'c' in teilaufg:
        # Die SuS sollen einfache Dezimalbrüche oder Prozente mit der Bruchdarstellung als Zwischenschritt ineinander umwandeln
        anz_aufg = anz_teilaufg['b'] if anz_teilaufg['b'] < 10 else 10
        zahlen = random_selection([element*5 for element in range(1,20)], anz_aufg, wdh=False)
        aufgabe.append('Notiere als echter Bruch und als Dezimalbruch bzw. als Prozentangabe.')
        if anz_aufg % 2 != 0:
            step = anz_aufg - 1
            liste = [[gzahl(zahlen[step]) + r' \% ~=~ \frac{ \hspace{2em} }{100} ~=~ \hspace{2em} ',
                      gzahl(zahlen[step]) + r' \% ~=~ \frac{ ' + gzahl(zahlen[step]) + ' }{100} ~=~ '
                      + gzahl(zahlen[step] / 100)]]
            anz_aufg -= 1
        else:
            liste = []
        for step in range(0, anz_aufg, 2):
            liste.extend(([gzahl(zahlen[step]/100) + r' ~=~ \frac{ \hspace{2em} }{100} ~=~ \hspace{2em} \% ',
                           gzahl(zahlen[step] / 100) + r' ~=~ \frac{ ' + gzahl(zahlen[step]) + ' }{100} ~=~ '
                           + gzahl(zahlen[step]) + r' \% '],
                          [gzahl(zahlen[step+1]) + r' \% ~=~ \frac{ \hspace{2em} }{100} ~=~ \hspace{2em} ',
                           gzahl(zahlen[step + 1]) + r' \% ~=~ \frac{ ' + gzahl(zahlen[step + 1]) + ' }{100} ~=~ '
                           + gzahl(zahlen[step + 1] / 100)]))
        random.shuffle(liste)
        for step, element in enumerate(liste):
            liste[step] = [beschriftung(len(teilaufg), i, True) + element[0],
                           beschriftung(len(teilaufg), i, True) + element[1]]
            i += 1
        text = lsg = ''
        for step, element in enumerate(liste):
            text += element[0] + r' \hspace{5em} ' if step % 2 == 0 else element[0] + r' \\\\ '
            lsg += element[1] + r' \hspace{5em} ' if step % 2 == 0 else element[1] + r' \\ '
            i += 1
        if len(liste) % 2 != 0:
            text += r' \hspace{13em} '
            lsg += r' \hspace{12em} '
        aufgabe.append(text)
        loesung.append(lsg)

    if 'd' in teilaufg:
        # Die SuS sollen einfache Dezimalbrüche in Prozentschreibweise notieren
        anz_aufg = anz_teilaufg['d'] if anz_teilaufg['d'] < 9 else 9
        zahlen = random_selection(list(range(1,200)), anzahl=anz_aufg, wdh=False)
        aufgabe.append('Notiere in Prozentschreibweise.')
        lsg = text = ''
        for step in range(anz_aufg):
            text += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step] / 100)
                     + r' ~=~ \hspace{2em} \% ')
            lsg += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step] / 100) + r' ~=~ '
                    + gzahl(zahlen[step]) + r' \% ')
            text += r' \hspace{5em} ' if (step + 1) % 3 != 0 else r' \\\\ '
            lsg += r' \hspace{5em} ' if (step + 1) % 3 != 0 else r' \\ '
            i += 1
        if anz_aufg % 3 != 0:
            text += r' \hspace{9em} '
            lsg += r' \hspace{8em} '
        aufgabe.append(text)
        loesung.append(lsg)
    if 'e' in teilaufg:
        # Die SuS sollen einfache  in Bruch- und Prozentschreibweise notieren
        anz_aufg = anz_teilaufg['d'] if anz_teilaufg['d'] < 9 else 9
        zahlen = random_selection(list(range(1, 200)), anzahl=anz_aufg, wdh=False)
        aufgabe.append('Notiere als Dezimalbruch.')
        lsg = text = ''
        for step in range(anz_aufg):
            text += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step])
                     + r' \% ~=~ \hspace{2em} ')
            lsg += (beschriftung(len(teilaufg), i, True) + gzahl(zahlen[step]) + r' \% ~=~ '
                    + gzahl(zahlen[step] / 100) + r' \% ')
            text += r' \hspace{5em} ' if (step + 1) % 3 != 0 else r' \\\\ '
            lsg += r' \hspace{5em} ' if (step + 1)% 3 != 0 else r' \\ '
            i += 1
        if anz_aufg % 3 != 0:
            text += r' \hspace{9em} '
            lsg += r' \hspace{8em} '
        aufgabe.append(text)
        loesung.append(lsg)
    if 'f' in teilaufg:
        # Die SuS sollen einfache Dezimalbrüche oder Prozente mit der Bruchdarstellung als Zwischenschritt ineinander umwandeln
        anz_aufg = anz_teilaufg['d'] if anz_teilaufg['d'] < 9 else 9
        zahlen = random_selection(list(range(1,200)), anzahl=anz_aufg, wdh=False)
        aufgabe.append('Notiere als Dezimalbruch bzw. in Prozentschreibweise.')
        if anz_aufg % 2 != 0:
            step = anz_aufg - 1
            liste = [[gzahl(zahlen[step]) + r' \% ~=~ \hspace{2em} ',
                      gzahl(zahlen[step]) + r' \%  ~=~ ' + gzahl(zahlen[step] / 100)]]
            anz_aufg -= 1
        else:
            liste = []
        for step in range(0, anz_aufg, 2):
            liste.extend(([gzahl(zahlen[step] / 100) + r' ~=~ \hspace{2em} \% ',
                           gzahl(zahlen[step] / 100) + r' ~=~ ' + gzahl(zahlen[step]) + r' \% '],
                          [gzahl(zahlen[step + 1]) + r' \% ~=~ \hspace{2em} ',
                           gzahl(zahlen[step + 1]) + r' \% ~=~ ' + gzahl(zahlen[step + 1] / 100)]))
        random.shuffle(liste)
        for step, element in enumerate(liste):
            liste[step] = [beschriftung(len(teilaufg), i, True) + element[0],
                           beschriftung(len(teilaufg), i, True) + element[1]]
            i += 1
        text = lsg = ''
        for step, element in enumerate(liste):
            text += element[0] + r' \hspace{5em} ' if (step + 1) % 3 != 0 else element[0] + r' \\\\ '
            lsg += element[1] + r' \hspace{5em} ' if (step + 1) % 3 != 0 else element[1] + r' \\ '
            i += 1
        if len(liste) % 3 != 0:
            text += r' \hspace{9em} '
            lsg += r' \hspace{8em} '
        aufgabe.append(text)
        loesung.append(lsg)

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [len(teilaufg)]
        liste_punkte = BE
    else:
        liste_punkte = [len(teilaufg)]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def darstellung_prozente(nr, teilaufg=['a', 'b'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die Schüler und Schülerinnen verschiedene Aufgaben mit dem Prozentfeld bearbeiten
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']

    if anzahl != False:
        anzahl = 12 if anzahl > 12 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh) if wdh < 7 else repeat(teilaufg, wdh)
    anz_teilaufg = Counter(teilaufg)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    if 'a' in teilaufg:
        # Die SuS sollen den grau eingefärbten Anteil eines Prozentfeldes als Bruch und in Prozentschreibweise notieren
        aufgabe.append('Gib den Anteil der grau eingefärbten Felder in Prozent an.')
        lsg = ''
        for step in range(anz_teilaufg['a']):
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            ausw = random.choice([[5,1], [5,2], [10,1], [10,2], [10,5]])
            cols = ausw[0] # Spalten
            rows = ausw[1] # Zeilen
            anz = nzahl(min([rows,cols]), rows * cols - 1)
            x_max, y_max_unk = divmod(anz, rows)
            y_max = y_max_unk / rows
            prozentfeld(rows, cols, x_max, y_max, name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            aufgabe.extend((['Grafik', '200px', None], NoEscape(beschriftung(len(teilaufg),i)
                            + r' p = $ \frac{ \hspace{3em} }{ \hspace{3em} } $ = .......... \% '), ' \n\n'))
            lsg += str(liste_teilaufg[i]) + r') \quad ' + gzahl(int(anz / (rows * cols) * 100)) + r'~ \% \quad '
            i += 1
        loesung.append(lsg)

    if 'b' in teilaufg:
        # Die SuS sollen zu einem gegebenen Prozentsatz ein Prozentfeld grau markieren
        aufgabe.append('Gib den Anteil der grau eingefärbten Felder in Prozent an. \n\n')
        for step in range(anz_teilaufg['b']):
            grafiken_aufgaben.append(f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')
            grafiken_loesung.append(f'Loesung_{str(nr)}_{str(liste_teilaufg[i])})')
            ausw = random.choice([[5,1], [5,2], [10,1], [10,2], [10,5]])
            cols = ausw[0] # Spalten
            rows = ausw[1] # Zeilen
            anz = nzahl(min([rows,cols]), rows * cols - 1)
            x_max, y_max_unk = divmod(anz, rows)
            y_max = y_max_unk / rows
            prozentfeld(rows, cols, x_max, y_max, name=f'Loesung_{str(nr)}_{str(liste_teilaufg[i])})',
                        text='.............................' + beschriftung(len(teilaufg),i))
            prozentfeld(rows, cols, 0, 0, name=f'Aufgabe_{str(nr)}_{str(liste_teilaufg[i])})')

            aufgabe.extend((NoEscape(beschriftung(len(teilaufg),i) + 'p = ' + gzahl(int(anz / (rows * cols) * 100)))
                            + ' % ', ['Grafik', '200px', None]))
            loesung.append(['Grafik', '200px'])
            i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [len(teilaufg)]
        liste_punkte = BE
    else:
        liste_punkte = [len(teilaufg)]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def prozentrechenaufgaben(nr, teilaufg=['a'], anzahl=False, wdh=False, i=0, BE=[]):
    # Hier sollen die Schüler und Schülerinnen verschiedene Aufgaben zur Prozentrechnung bearbeiten
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten erstellt werden.
    # Mit dem Parameter 'wdh=' kann festgelegt werden, wie oft die angegebenen Teilaufgaben wiederholt werden. Also ['a', 'b'] mit 'wdh=2' ergibt ['a','a','b','b'] als Teilaufgabe.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = []
    liste_punkte = []
    if anzahl != False:
        anzahl = 27 if anzahl > 27 or type(anzahl) != int else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    if wdh != False:
        teilaufg = repeat(teilaufg, wdh) if wdh < 7 else repeat(teilaufg, wdh)
    anz_teilaufg = Counter(teilaufg)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    k = 1

    if 'a' in teilaufg:
        # Die SuS sollen eine einfache Aufgabe zum Berechnen des Prozentwertes bearbeiten
        anz = anz_teilaufg['a'] if anz_teilaufg['a'] < 10 else 10
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        liste_punkte.append(anz)
        grundwerte = random_selection([element * 10**exp for element in range(1, 19) for exp in range(1,4)],
                                      anzahl=anz, wdh=True)
        einheiten = random_selection([' Euro', ' Kilogramm', ' Liter', ' Meter', ' US-Dollar'], anzahl=anz)
        prozentwerte = random_selection([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
                                        anzahl=anz, wdh=True)
        aufgabe.append(beschriftung(len(anz_teilaufg), i) + 'Berechne den Prozentwert. \n\n')
        for step in range(anz_teilaufg['a']):
            pw = prozentwerte[step]
            gw = grundwerte[step]
            eh = einheiten[step]
            aufgabe.extend((NoEscape(r' \indent ' + int_to_roman(k) + r') ' + gzahl(pw) + r'\% von ' + gzahl(gw)
                                     + eh + '.'),' \n\n'))
            loesung.append(int_to_roman(k) + r') \mathrm{ \quad W ~=~ ' + gzahl(pw/100) + r' \cdot '
                           + gzahl(gw) + eh + '~=~' + gzahl(pw*gw/100) + eh + '}')
            k += 1
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]