from Aufgaben_Differentialrechung import *
from Klausur_erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 11
Semester = 1
Gesamtzeit = 135
Zeithmft = 25
liste_qualiphase = ['Einführungsphase', 'Qualifikationsphase']
Phase = liste_qualiphase[1]
Thema = 'Analysis'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)

# Aufgaben für Teil I
liste_punkte_hmft = ['Punkte']
liste_bez_hmft = ['Aufgabe']

aufgaben_hmft_seite2 = [kurvendiskussion_polynome(1,['a', 'b', 'c', 'd', 'e', 'f'])]
# z.B. aufgaben_seite1 = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]
for element in aufgaben_hmft_seite2:
    liste_bez_hmft.extend(element[5])
    liste_punkte_hmft.extend(element[4])

# aufgaben_hmft_seite3 = []
# for element in aufgaben_seite2:
#     liste_bez_hmft.extend(element[5])
#     liste_punkte_hmft.extend(element[4])


liste_seiten_hmft = [seite(aufgaben_hmft_seite2)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

# Aufgaben für Teil II
liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite1 = [kurvendiskussion_polynome(1,['a', 'b', 'c', 'd', 'e', 'f'])]
# z.B. aufgaben_seite1 = [ereignisse_ergebnisse(1, ['a', 'b', 'c'])]
for element in aufgaben_seite1:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

# aufgaben_seite2 = []
# for element in aufgaben_seite2:
#     liste_bez.extend(element[5])
#     liste_punkte.extend(element[4])

liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

#  Angaben für die Klausur

Gesamtpunktzahl = sum(liste_punkte_hmft[1:]) + sum(liste_punkte[1:])
angaben_hmft = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_hmft, liste_punkte_hmft]
angaben = [Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez, liste_punkte]

erzeugen_kl_teil_1(liste_seiten_hmft, angaben_hmft)
erzeugen_kl_teil_2(liste_seiten, angaben)
