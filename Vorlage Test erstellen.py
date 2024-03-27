from Aufgaben_Wahrscheinlichkeitsrechnung import *
from Test_erstellen import *

# Angaben für den Test im pdf-Dokument
Kurs = 'Kursart'
Fach = 'Mathematik'
Klasse = 'Klasse'
Lehrer = 'Lehrkraft'
Art = 'Test oder Hausaufgabenkontrolle usw'
Titel = 'Was ist der Inhalt'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = True    # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite1 = [] # z.B. aufgaben_seite1 = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]
for element in aufgaben_seite1:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

# aufgaben_seite2 = []
# for element in aufgaben_seite2:
#     liste_bez.extend(element[5])
#     liste_punkte.extend(element[4])

liste_seiten = [] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
angaben = [Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

pdf_erzeugen(liste_seiten, angaben, anzahl, probe)
