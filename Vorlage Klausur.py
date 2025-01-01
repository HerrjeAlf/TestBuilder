import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Kurs auf erhöhtem Niveau'
Klasse = 11
Gruppe = ''
Semester = 1
Gesamtzeit = 135
Zeithmft = 25
Phase = 'Einführungsphase' # hier bitte 'Einführungsphase' oder 'Qualifikationsphase' eintragen
Thema = 'Analysis'
datum_delta = 1  # Wann wird die Klausur (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil1 = [[brueche_add_subr(1, ['e', 'j'], anzahl=4),
                   brueche_mul_div(2, ['b', 'c', 'e', 'f']),
                   potenzgesetz_eins(3, ['d', 'g'], anzahl=3),
                   potenzgesetz_zwei(4, ['d', 'g', 'i']),
                   potenzgesetz_eins_erw(5, ['f', 'h', 'i', 'j']),
                   potenzgesetz_eins_mehrfach(6, ['c', 'e']),
                   potenzgesetz_zwei_erw(7, ['f', 'h', 'i', 'j']),
                   potenzgesetz_drei_vier(8, ['c', 'e'])]]

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[wiss_schreibweise(1, anzahl=4),
                   einheiten_umrechnen(2, anzahl=4),
                   terme_addieren(3, ['b', 'g', 'j', 'l']),
                   terme_multiplizieren(4, ['a', 'c', 'd']),
                   terme_ausmultiplizieren(5, ['a', 'c', 'e', 'h', 'j']),
                   terme_ausklammern(6, ['a', 'd', 'e']),
                   gleichungen(7, ['c', 'f', 'i', 'k'])],
                  [stirb_langsam_2(8, ['a', 'b', 'c', 'd', 'e'])]]









# --------------------------------ab hier wird aus den eingegebenen Daten die Klausur erzeugt ----------------------------

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

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

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil2 = []
for element in aufgaben_teil2:
    for aufgabe in element:
        liste_bez_teil2.extend(aufgabe[5])
        liste_punkte_teil2.extend(aufgabe[4])
    liste_seiten_teil2.append(seite(element))


#  Angaben für die Klausur
clean_tex = True if clean_tex not in [True, False] else clean_tex
Gesamtpunktzahl = sum(liste_punkte_teil1[1:]) + sum(liste_punkte_teil2[1:])
angb_teil1 = [Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
                liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema, datum_delta,
              liste_bez_teil2, liste_punkte_teil2]

klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex)