from Aufgaben.Aufgaben_Analysis import *
from Aufgaben.Aufgaben_Algebra import *
from Aufgaben.Aufgaben_Wahrscheinlichkeitsrechnung import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = 'HAK 15'
Titel = 'Passwörter und Binomialkoeffizient'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe =True    # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for i in range(anzahl):
    aufgaben_seite1 = [begriffe_wahrscheinlichkeit(1, anzahl=2),
                       baumdiagramm_zoZ(2, ['a', 'b', 'c', 'd', 'e'], stufen=2),
                       faires_spiel(3),
                       sicheres_passwort(4)]

    for element in aufgaben_seite1:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    aufgaben_seite2 = [lotto_modell_01(5)]
    for element in aufgaben_seite2:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

    test_erzeugen(liste_seiten, angaben, i, probe)

