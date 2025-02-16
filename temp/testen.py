import os

from Aufgaben import terme_ausmultiplizieren
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'Testen'
Titel = 'Hier wird getestet'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False   # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll
clean_tex = True if clean_tex not in [True, False] else clean_tex

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for ziffer in range(anzahl):
    # Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()]] eintragen
    Aufgaben = [[basisaufgaben(1, neue_seite=5)]]

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


# def stationbahn(radius, width, height):
#     fig, ax = plt.subplots()
#
#     # Halbrechkreis links
#     theta = np.linspace(-np.pi/2, np.pi/2, 100)
#     x1 = radius * np.cos(theta)
#     y1 = radius * np.sin(theta)
#     ax.plot(x1, y1, 'b')
#
#     # Rechteck
#     x2 = [radius, radius + width, radius + width, radius]
#     y2 = [-radius, -radius, radius, radius]
#     ax.plot(x2, y2, 'b')
#
#     # Halbrechkreis rechts
#     theta = np.linspace(np.pi/2, -np.pi/2, 100)
#     x3 = radius * np.cos(theta) + radius + width
#     y3 = radius * np.sin(theta)
#     ax.plot(x3, y3, 'b')
#
#     ax.set_aspect('equal')
#     plt.xlabel('Länge')
#     plt.ylabel('Breite')
#     plt.title('Stationbahn')
#     plt.grid(False)
#     plt.show()
#
# stationbahn(2, 5, 3)