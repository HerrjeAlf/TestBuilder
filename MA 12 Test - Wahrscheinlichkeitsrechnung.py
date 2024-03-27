from Aufgaben_Wahrscheinlichkeitsrechnung import *
from Test_erstellen import *

# Angaben für den Test im pdf-Dokument
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = '3. Test (2. Semester)'
Titel = 'Kurvendiskussionen einer Exponentialfunktion'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1
probe = True

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite1 = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]
for element in aufgaben_seite1:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

aufgaben_seite2 = [ereignisse_ergebnisse(2, ['a', 'b', 'c'])]
for element in aufgaben_seite2:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
angaben = [Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

pdf_erzeugen(liste_seiten, angaben, anzahl, probe)
