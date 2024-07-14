from Aufgaben.Oberstufe_Analysis import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 11
Gruppe = ''
Gesamtzeit = 135
Zeithmft = 25
Thema = 'Analysis'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

aufgaben_teil1_s1 = [ableitungen(1,['a', 'a', 'b', 'b', 'c'])]
for element in aufgaben_teil1_s1:
    liste_bez_teil1.extend(element[5])
    liste_punkte_teil1.extend(element[4])


aufgaben_teil1_s2 = []
for element in aufgaben_teil1_s2:
    liste_bez_teil1.extend(element[5])
    liste_punkte_teil1.extend(element[4])

liste_seiten_teil1 = [seite(aufgaben_teil1_s1)]
# z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

# Aufgaben für Teil II - Analysis - Wahlaufgabe 1
liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_teil2_s1_ana1 = [kurvendiskussion_polynom_parameter_2(5)]
# z.B. aufgaben_teil2_s1_ana1 = [exponentialfunktionen_01(1,['a', 'b', 'c', 'd', 'e', 'f', 'g'])]
for element in aufgaben_teil2_s1_ana1:
    print(element[5])
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

aufgaben_teil2_s2_ana1 = []
for element in aufgaben_teil2_s2_ana1:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

liste_seiten_teil2_ana1 = [seite(aufgaben_teil2_s1_ana1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

#  Angaben für die Klausur

Gesamtpunktzahl = sum(liste_punkte_teil1[1:]) + sum(liste_punkte[1:])
angb_teil1 = [Kurs, Klasse, Gruppe, Gesamtzeit, Zeithmft, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_teil1, liste_punkte_teil1]
angb_teil2_ana1 = [Kurs, Klasse, Gruppe, Gesamtzeit, Zeithmft, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez, liste_punkte]

klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2_ana1, angb_teil2_ana1)