import string
import numpy as np
import random, math
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
nr_aufgabe = 0

def brueche_erweitern(nr, trivial=1, einfach=1, schwer=1, anzahl_fakt=3):
    # Die SuS sollen Brüche mit vorgebenen Zahlen erweitern.
    # Die Parameter "trivial=",  "einfach=" und "schwer=" geben die Anzahl der trivialen Brüche (Zähler 1), der einfachen sowie der schweren Brüchen vor. Die Parameter "trivial" und "einfach" können maximal 9 sein, der Parameter "schwer" kann maximal 8 sein.
    # Der Parameter "anzahl_fakt=" gibt die Anzahl der Faktoren, mit denen die Brüche erweitert werden, vor.

    # Erstellen der Liste der Brüche mit Zähler und Nenner
    trivial = 9 if trivial > 9 else trivial
    liste_nenner = np.random.choice(list(range(2,12)), trivial, False)
    liste_nenner.sort()
    liste_brueche = [[1,element] for element in liste_nenner]
    einfach = 9 if einfach > 9 else einfach
    for zahl in range(einfach):
        zaehler, nenner = np.random.choice([2, 3, 5, 7], 2, False)
        while [zaehler, nenner] in liste_brueche:
            zaehler, nenner = np.random.choice([2, 3, 5, 7], 2, False)
        liste_brueche.append([zaehler, nenner])
    schwer = 8 if schwer > 8 else schwer
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
    for faktoren in liste_faktoren:
        aufg_faktoren = aufg_faktoren + gzahl(faktoren) + ', '

    liste_bez = [f'{str(nr)}']
    i = 0
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
    liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def brueche_kuerzen(nr, trivial=1, einfach=1, schwer=1):
    # Die SuS sollen Brüche mit soweit wie möglich kürzen.
    # Die Parameter "trivial=",  "einfach=" und "schwer=" geben die Anzahl der trivialen Brüche (Zähler 1), der einfachen sowie der schweren Brüchen vor. Die Parameter "trivial" und "einfach" können maximal 9 sein, der Parameter "schwer" kann maximal 8 sein.

    liste_bez = [f'{str(nr)}']
    i = 0
    aufg = ''
    lsg = ''
    punkte = 0

    # Erstellen der Liste der Brüche mit Zähler und Nenner
    trivial = 9 if trivial > 9 else trivial
    liste_nenner = np.random.choice(list(range(2,12)), trivial, False)
    liste_nenner.sort()
    liste_brueche_aufg = []
    for zahl in liste_nenner:
        faktor = random.choice([2, 3, 5, 7, 10])
        liste_brueche_aufg.append([faktor, faktor*zahl])
        if (i + 1) % 3 != 0:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(faktor) + '~}{~' + gzahl(faktor*zahl)
                   + r'~} ~=~ \frac{ ~' + gzahl(1) + '~}{~' + gzahl(zahl) + r'~}')
            if i + 1 < trivial + einfach + schwer:
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(faktor) + '~}{~' + gzahl(faktor*zahl)
                   + r'~} ~=~ \frac{ ~' + gzahl(1) + '~}{~' + gzahl(zahl) + r'~} \\\\')
        elif i + 1 == trivial and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(faktor) + '~}{~' + gzahl(faktor*zahl)
                   + r'~} ~=~ \frac{ ~' + gzahl(1) + '~}{~' + gzahl(zahl) + r'~} \\\\')
        else:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(faktor) + '~}{~' + gzahl(faktor*zahl)
                   + r'~} ~=~ \frac{ ~' + gzahl(1) + '~}{~' + gzahl(zahl) + '~}')
        i += 1
        punkte += 1

    einfach = 9 if einfach > 9 else einfach
    for zahl in range(einfach):
        fkt = np.random.choice([2, 3, 4, 5, 6, 7, 10], 2, False)
        fkt.sort()
        zaehler, nenner = np.random.choice([2, 3, 5, 7, 11], 2, False)
        while [zaehler, nenner] in liste_brueche_aufg:
            zaehler, nenner = np.random.choice([2, 3, 5, 7, 11], 2, False)
        liste_brueche_aufg.append([zaehler*fkt[0]*fkt[1], nenner*fkt[0]*fkt[1]])
        if (i + 1) % 3 != 0:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
            if i + 1 < trivial + einfach + schwer:
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 3 == 0 and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~} \\\\')
        elif i + 1 == einfach and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~} \\\\')
        else:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
        i += 1
        punkte += 1

    schwer = 9 if schwer > 9 else schwer
    for zahl in range(schwer):
        fkt = np.random.choice([2, 3, 4, 5, 6, 7, 10], 3, False)
        fkt.sort()
        zaehler, nenner = np.random.choice([3, 5, 7, 11, 13], 2, False)
        while [zaehler, nenner] in liste_brueche_aufg:
            zaehler, nenner = np.random.choice([3, 5, 7, 11, 13], 2, False)
        liste_brueche_aufg.append([zaehler*fkt[0]*fkt[1]*fkt[2], nenner*fkt[0]*fkt[1]*fkt[2]])
        if (i + 1) % 2 != 0:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]*fkt[2]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]*fkt[2]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
            if i + 1 < trivial + einfach + schwer:
                lsg = lsg + r' \hspace{5em} '
        elif (i + 1) % 2 == 0 and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]*fkt[2]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]*fkt[2]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~} \\\\')
        elif i + 1 == einfach and i + 1 < trivial + einfach + schwer:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]*fkt[2]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]*fkt[2]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~} \\\\')
        else:
            lsg = (lsg + str(liste_teilaufg[i]) + r') \quad \frac{~' + gzahl(zaehler*fkt[0]*fkt[1]*fkt[2]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]*fkt[2]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]*fkt[1]) + '~}{~'
                   + gzahl(nenner*fkt[0]*fkt[1]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler*fkt[0]) + '~}{~'
                   + gzahl(nenner*fkt[0]) + r'~} ~=~ \frac{ ~' + gzahl(zaehler) + '~}{~' + gzahl(nenner) + r'~}')
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
    liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def brueche_ergaenzen(nr, nenner=3, zaehler=3):
    # Die SuS sollen eine vorgegebene Gleichung von Bruchtermen so ergänzen, dass diese richtig ist.
    # Die Parameter "nenner=" und "zaehler=" legen die Anzahl der Teilaufgaben fest, in denen der Nenner bzw. der Zähler ergänzt werden muss. Maximal sind jeweils 6 Teilaufgaben möglich.

    liste_bez = [f'{str(nr)}']
    i = 0
    punkte = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               f'Ergänzen Sie die Terme so, dass die jeweilige Gleichung stimmt.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    for zahl in range(nenner+zaehler):
        fkt = random.choice([2, 3, 4, 5, 6, 7, 10])
        zaehler, nenner = np.random.choice([2, 3, 5, 7, 11], 2, False)


    liste_punkte = [punkte]


    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
