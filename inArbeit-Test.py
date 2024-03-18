from inArbeit-Test_erstellen import *
from inArbeit-Test_aufgaben import *
import datetime, string, time

# Angaben für den Test im pdf-Dokument
wann = 1
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = '3. Test (2. Semester)'
Titel = 'Kurvendiskussionen einer Exponentialfunktion'
in_tagen = 1

angaben = [Kurs, Fach, Klasse, Lehrer, Art, Titel, in_tagen]

print(angaben)

aufgaben = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]

liste_seiten = [seite(aufgaben), seite(aufgaben)]

pdf_erzeugen(liste_seiten, angaben, wann)