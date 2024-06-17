from Aufgaben.Aufgaben_Analysis import *
from Aufgaben.Aufgaben_Algebra import *
from Aufgaben.Aufgaben_Wahrscheinlichkeitsrechnung import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
schuljahr = '2023 - 2024' # Schuljahr in dem das Abitur stattfindet
pruefungsfach = '4. Abiturprüfungsfach'  # 4. Abiturprüfungsfach oder mündliche Zusatzprüfung
lehrkraft = 'Herr Herrys'
vorschlag = 'Nr. 1'
Thema_teil1 = 'Analysis (1. und 2. Semester)' # Thema (Semester)
Thema_teil2 = 'Analytische Geometrie (3. Semester)'

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

aufg_teil1 = [kurvendiskussion_polynome_01(1, ['a', 'c', 'd', 'f', 'g'], ableitungen=True,
                                        nullstellen='rational', wendenormale=False)]
for element in aufg_teil1:
    liste_bez_teil1.extend(element[5])
    liste_punkte_teil1.extend(element[4])

# Aufgaben für Prüfungsgespräch
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']

aufg_teil2_s1 = [geraden_aufstellen(2, T_auf_g=True),
                 geraden_lagebeziehung(3, lagebeziehung='parallel')]
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

angb = [schuljahr, pruefungsfach, lehrkraft, vorschlag, Thema_teil1, Thema_teil2, liste_bez_teil1, liste_punkte_teil1]
muendliche_pruefung(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb)

