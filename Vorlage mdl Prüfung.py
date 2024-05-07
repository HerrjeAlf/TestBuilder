from Aufgaben.Aufgaben_Analysis import *
from Aufgaben.Aufgaben_Algebra import *
from Aufgaben.Aufgaben_Wahrscheinlichkeitsrechnung import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
schuljahr = '2023 - 2024' # Schuljahr in dem das Abitur stattfindet
pruefungsfach = '4. Abiturprüfungsfach'  # 4. Abiturprüfungsfach oder mündliche Zusatzprüfung
lehrkraft = 'Herr Herrys'
Thema_teil1 = 'Analytische Geometrie (3. Semester)' # Thema (Semester)
Thema_teil2 = 'Analysis (1. und 2. Semester)'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

aufg_teil1 = [geraden_lagebeziehung(1, lagebeziehung='schneiden')]
for element in aufg_teil1:
    liste_bez_teil1.extend(element[5])
    liste_punkte_teil1.extend(element[4])

# Aufgaben für Prüfungsgespräch
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']

aufg_teil2_s1 = [grafisches_ableiten(2)]
for element in aufg_teil2_s1:
    liste_bez_teil2.extend(element[5])
    liste_punkte_teil2.extend(element[4])

aufg_teil2_s2 = []
for element in aufg_teil2_s2:
    liste_bez_teil2.extend(element[5])
    liste_punkte_teil2.extend(element[4])

liste_aufg_lsg_teil1 = [seite(aufg_teil1)]
liste_aufg_lsg_teil2 = [seite(aufg_teil2_s1), seite(aufg_teil2_s2)]

#  Angaben für die Klausur

angb = [schuljahr, pruefungsfach, lehrkraft, Thema_teil1, Thema_teil2, datum_delta,
        liste_bez_teil1, liste_punkte_teil1]
muendliche_pruefung(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb)

