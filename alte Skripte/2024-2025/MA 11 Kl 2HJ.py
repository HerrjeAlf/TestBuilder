import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Mathematik Grundkurs'
Klasse = 11
Gruppe = ''
Semester = 2
Gesamtzeit = 90
Zeithmft = 25
Phase = ['Einführungsphase', 'Qualifikationsphase'][0]
Thema = 'Analysis'
datum_delta = 1  # Wann wird die Klausur (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = [True, False][0] # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil1 = [[logarithmusgesetze(1, anzahl=2),
                   potenzgesetze(2, anzahl=2),
                   polynome_kennenlernen(3, BE=[2,3]),
                   extremalproblem_einfach(4, BE=[5]),
                   polynome_untersuchen(5, ['a', 'c'], grad=2, BE=[3,2])]]

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[rekonstruktion(1),
                   polynome_untersuchen(2, ['d'], grad=3),
                   exponentialgleichungen(3, ['a', 'b', 'c'], anzahl=2),
                   wachstumsfunktion(4)]]









# --------------------------------ab hier wird aus den eingegebenen Daten die Klausur erzeugt ----------------------------

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben der erste Teil der Klausur erzeugt
liste_seiten_teil1 = []
for element in aufgaben_teil1:
    for aufgabe in element:
        liste_bez_teil1.extend(aufgabe[5])
        liste_punkte_teil1.extend(aufgabe[4])
    liste_seiten_teil1.append(seite(element))

# Aufgaben für Teil II
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben der zweite Teil der Klausur erzeugt
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