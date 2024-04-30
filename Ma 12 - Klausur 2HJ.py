from Aufgaben.Aufgaben_Analysis import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 12
Semester = 2
Gesamtzeit = 135
Zeithmft = 25
liste_qualiphase = ['Einführungsphase', 'Qualifikationsphase']
Phase = liste_qualiphase[1]
Thema = 'Analysis'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

# auswahl der Aufgabenteile für Nr. 2 und 3
teilaufg_nr2 = ['a']
teilaufg_nr2.extend(np.random.choice(('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),2, False))
teilaufg_nr3 = ['a']
teilaufg_nr3.extend(np.random.choice(('b', 'c', 'd', 'e', 'f', 'g'),2, False))

# Aufgaben für Teil I
liste_punkte_hmft = ['Punkte']
liste_bez_hmft = ['Aufgabe']

aufgaben_hmft_seite2 = [rekonstruktion(1),
                        ableitungen(2, teilaufg=teilaufg_nr2),
                        unbestimmtes_integral(3, teilaufg=teilaufg_nr3),
                        bestimmtes_integral(4, grad=2)]
k = 1
for element in aufgaben_hmft_seite2:
    liste_bez_hmft.extend(element[5])
    if k == 2 or k == 3:
        liste_punkte_hmft.append(3)
    else:
        liste_punkte_hmft.extend(element[4])
    k += 1

aufgaben_hmft_seite3 = []
for element in aufgaben_hmft_seite3:
    liste_bez_hmft.extend(element[5])
    liste_punkte_hmft.extend(element[4])

liste_seiten_hmft = [seite(aufgaben_hmft_seite2)]
# z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

# Aufgaben für Teil II
liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite1 = [kurvendiskussion_polynom_parameter_2(5)]
# z.B. aufgaben_seite1 = [exponentialfunktionen_01(1,['a', 'b', 'c', 'd', 'e', 'f', 'g'])]
for element in aufgaben_seite1:
    print(element[5])
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

aufgaben_seite2 = []
for element in aufgaben_seite2:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

#  Angaben für die Klausur

Gesamtpunktzahl = sum(liste_punkte_hmft[1:]) + sum(liste_punkte[1:])
angaben_hmft = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_hmft, liste_punkte_hmft]
angaben = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez, liste_punkte]

erzeugen_kl_teil_1(liste_seiten_hmft, angaben_hmft)
erzeugen_kl_teil_2(liste_seiten, angaben)
