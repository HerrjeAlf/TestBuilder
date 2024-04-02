from Aufgaben_Differentialrechung import *
from Klausur_Teil1_erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 11
Semester = 1
Gesamtzeit = 135
Zeithmft = 25
liste_qualiphase = ['Einführungsphase', 'Qualifikationsphase']
Phase = liste_qualiphase[1]
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite2 = [kurvendiskussion_polynome(1,['a'])] # z.B. aufgaben_seite1 = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]
for element in aufgaben_seite2:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

# aufgaben_seite3 = []
# for element in aufgaben_seite2:
#     liste_bez.extend(element[5])
#     liste_punkte.extend(element[4])

liste_seiten = [seite(aufgaben_seite2)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
angaben = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, datum_delta, liste_bez, liste_punkte]

erzeugen_kl_hmft(liste_seiten, angaben)
