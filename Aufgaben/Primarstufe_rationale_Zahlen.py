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
    # die Parameter "trivial=",  "einfach=" und "schwer=" geben die Anzahl der trivialen Brüche (Zähler 1), der einfachen sowie der schweren Brüchen vor.
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
