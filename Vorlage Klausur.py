import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *


# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 11
Gruppe = ''
Semester = 1
Gesamtzeit = 135
Zeithmft = 25
# hier bitte 'Einführungsphase' oder 'Qualifikationsphase' eintragen
Phase = 'Einführungsphase'
Thema = 'Analysis'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll
clean_tex = True if clean_tex not in [True, False] else clean_tex

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil1 = [[ableitungen(1)]]

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil1 = []
for element in aufgaben_teil1:
    for aufgabe in element:
        liste_bez_teil1.extend(aufgabe[5])
        liste_punkte_teil1.extend(aufgabe[4])
    liste_seiten_teil1.append(seite(element))

# Aufgaben für Teil II
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']


# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[kurvendiskussion_polynome(2)]]

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil2 = []
for element in aufgaben_teil2:
    for aufgabe in element:
        liste_bez_teil2.extend(aufgabe[5])
        liste_punkte_teil2.extend(aufgabe[4])
    liste_seiten_teil2.append(seite(element))


#  Angaben für die Klausur

Gesamtpunktzahl = sum(liste_punkte_teil1[1:]) + sum(liste_punkte_teil2[1:])
angb_teil1 = [Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
              liste_bez_teil2, liste_punkte_teil2]

klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex)