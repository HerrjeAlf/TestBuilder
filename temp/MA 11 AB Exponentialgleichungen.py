import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Klasse = '11c'
Thema = 'Exp-Gl lösen'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden

for i in range(anzahl):
    # Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
    Aufgaben = [[exponentialgleichungen(1,['a'], anzahl=4),
                 exponentialgleichungen(2,['b'], anzahl=6),
                 exponentialgleichungen(3,['c'], anzahl=6)]]

    # hier werden aus der Liste der Aufgaben dieTest erzeugt
    liste_seiten = []
    for element in Aufgaben:
        liste_seiten.append(seite(element)) # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Klasse, Thema, datum_delta]
    arbeitsblatt_erzeugen(liste_seiten, angaben, i)

