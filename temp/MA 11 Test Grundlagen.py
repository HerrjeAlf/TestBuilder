import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '11'
Lehrer = 'Herr Herrys'
Art = 'Test 01'
Titel = 'Brüche und Potenzgesetze'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False # True: Probe 01, 02 usw. oder False: Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for i in range(anzahl):
    # Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
    Aufgaben = [[brueche_erweitern(1), brueche_kuerzen(2), brueche_ergaenzen(3), bruchteile_berechnen(4),
                 brueche_add_subr(5, ['e', 'j']), brueche_mul_div(6, ['b', 'c', 'e', 'f']),
                 potenzgesetze(7), potenzgesetz_eins(8, ['d', 'g'], anzahl=3)],
                [potenzgesetz_zwei(9, ['d', 'g', 'i', 'j']),
                 potenzgesetz_eins_erw(10, ['f', 'h', 'i', 'j']),
                 potenzgesetz_eins_mehrfach(11, ['c', 'e', 'g']),
                 potenzgesetz_zwei_erw(12, ['f', 'h', 'i', 'j']),
                 potenzgesetz_drei_vier(13, ['c', 'e'])]]
    # hier werden aus der Liste der Aufgaben dieTest erzeugt
    liste_seiten = []
    for element in Aufgaben:
        for aufgabe in element:
            liste_bez.extend(aufgabe[5])
            liste_punkte.extend(aufgabe[4])
        liste_seiten.append(seite(element)) # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]
    test_erzeugen(liste_seiten, angaben, i, probe)

