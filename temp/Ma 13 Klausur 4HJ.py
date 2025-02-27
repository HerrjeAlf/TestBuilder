import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Leistungskurs'
Klasse = 13
Gruppe = ''
Semester = 4
Gesamtzeit = 135
Zeithmft = 45
Phase = 'Qualifikationsphase' # hier bitte 'Einführungsphase' oder 'Qualifikationsphase' eintragen
Thema = 'lineare Algebra und Stochastik'
datum_delta = 1  # Wann wird die Klausur (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil1 = [[geraden_lagebeziehung(1, [random.choice(['a', 'b']), 'c'],
                                         lagebeziehung=random.choice(['parallel','windschief'])),
                   geraden_aufstellen(2)],
                  [baumdiagramm(3, ['a', 'b', 'c', 'd'], stufen=2, art='zmZ'),
                   vierfeldertafel_studie(4)]]

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[ebene_ebene(1, F_in_E='parallel'),
                   ebenenschar_buendel(2)],
                  [baumdiagramm(3, ['e', 'f', 'g'], stufen=3, art='zoZ'),
                   baumdiagramm(4, ['h', 'j', 'k'], stufen=3, art='zmZ')]]









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