import os

from Aufgaben import terme_ausmultiplizieren
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Kurs'
Fach = 'Fach'
Klasse = 'Test'
Lehrer = 'Mustermann'
Art = 'Test'
Titel = 'Hier wird getestet'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False   # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw
clean_tex = [False, True][0]

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for ziffer in range(anzahl):
    # Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()]] eintragen
    Aufgaben = [[basisaufgaben(1)]]

    # Aufgaben = [[rechnen_mit_vektoren(1),
    #              geraden_aufstellen(2, ['b']),
    #              geraden_lagebeziehung(3, ['c'], lagebeziehung=[None, 'identisch', 'parallel', 'windschief', 'schneiden'][1]),
    #              geraden_lagebeziehung(3, ['c'], lagebeziehung=[None, 'identisch', 'parallel', 'windschief', 'schneiden'][2]),
    #              geraden_lagebeziehung(3, ['c'], lagebeziehung=[None, 'identisch', 'parallel', 'windschief', 'schneiden'][3]),
    #              geraden_lagebeziehung(3, ['c'], lagebeziehung=[None, 'identisch', 'parallel', 'windschief', 'schneiden'][4]),
    #              testaufgabe(3)]]

    # hier werden aus der Liste der Aufgaben die Tests erzeugt
    liste_seiten = []
    for element in Aufgaben:
        for aufgabe in element:
            liste_bez.extend(aufgabe[5])
            liste_punkte.extend(aufgabe[4])
        liste_seiten.append(seite(element)) # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez,
               liste_punkte]
    test_erzeugen(liste_seiten, angaben, ziffer, probe, clean_tex)

