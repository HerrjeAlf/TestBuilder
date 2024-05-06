from Aufgaben.Aufgaben_Analysis import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 12
Semester = 2
Gesamtzeit = 135
Zeithmft = 45
liste_qualiphase = ['Einführungsphase', 'Qualifikationsphase']
Phase = liste_qualiphase[1]
Thema = 'Analysis'
datum_delta = 6  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

# auswahl der Aufgabenteile für Nr. 2 und 3
teilaufg_nr2 = ['a']
teilaufg_nr2.extend(np.random.choice(('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),2, False))
teilaufg_nr3 = ['a']
teilaufg_nr3.extend(np.random.choice(('b', 'c', 'd', 'e', 'f', 'g'),2, False))

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

aufgaben_teil1 = [rekonstruktion(1, xwert_1=-1, xwert_2=1, xwert_3=2),
                  ableitungen(2, teilaufg=teilaufg_nr2),
                  unbestimmtes_integral(3, teilaufg=teilaufg_nr3),
                  bestimmtes_integral(4, grad=2)]
k = 1
for element in aufgaben_teil1:
    liste_bez_teil1.extend(element[5])
    if k == 2 or k == 3:
        liste_punkte_teil1.append(3)
    else:
        liste_punkte_teil1.extend(element[4])
    k += 1

aufgaben_teil1_s2 = []
for element in aufgaben_teil1_s2:
    liste_bez_teil1.extend(element[5])
    liste_punkte_teil1.extend(element[4])

liste_seiten_teil1 = [seite(aufgaben_teil1)]
# z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

# Aufgaben für Teil II
liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_teil2_s1 = [kurvendiskussion_polynom_parameter_2(5)]
# z.B. aufgaben_seite1 = [exponentialfunktionen_01(1,['a', 'b', 'c', 'd', 'e', 'f', 'g'])]
for element in aufgaben_teil2_s1:
    print(element[5])
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

aufgaben_teil2_s2 = []
for element in aufgaben_teil2_s2:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

liste_seiten_teil2 = [seite(aufgaben_teil2_s1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

#  Angaben für die Klausur

Gesamtpunktzahl = sum(liste_punkte_teil1[1:]) + sum(liste_punkte[1:])
angb_teil1 = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez, liste_punkte]

klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2)