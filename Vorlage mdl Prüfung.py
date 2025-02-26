import os
from helpers import root_path
os.chdir(root_path())
from Aufgaben import *
from skripte.erstellen import *
# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
schuljahr = '2023 - 2024' # Schuljahr in dem das Abitur stattfindet
pruefungsfach = '4. Abiturprüfungsfach'  # 4. Abiturprüfungsfach oder mündliche Zusatzprüfung
vorschlag = 'Nr. 1'
lehrkraft = 'Herr Herrys'
Thema_teil1 = 'Analysis (1. Semester)' # Thema (Semester)
Thema_teil2 = 'Stochastik (2. und 4. Semester)'
datum_delta = 1  # Wann ist die mdl. Prüfung (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil1 = [[kurvendiskussion_polynome(1, ['a', 'd', 'e', 'f', 'g'], ableitungen=True, wendenormale=False)]]

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[baumdiagramm(2, ['a', 'c', 'd']), vierfeldertafel_studie(3)]]








# --------------------------------ab hier wird aus den eingegebenen Daten die mdl. Prüfung erzeugt ----------------------------

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben die Tests erzeugt
liste_seiten_teil1 = []
for element in aufgaben_teil1:
    for aufgabe in element:
        liste_bez_teil1.extend(aufgabe[5])
        liste_punkte_teil1.extend(aufgabe[4])
    liste_seiten_teil1.append(seite(element))

# Aufgaben für Teil II - Prüfungsgespräch
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben die Tests erzeugt
liste_seiten_teil2 = []
for element in aufgaben_teil2:
    for aufgabe in element:
        liste_bez_teil2.extend(aufgabe[5])
        liste_punkte_teil2.extend(aufgabe[4])
    liste_seiten_teil2.append(seite(element))

#  Angaben für die Klausur
clean_tex = True if clean_tex not in [True, False] else clean_tex
angb = [schuljahr, pruefungsfach, lehrkraft, vorschlag, Thema_teil1, Thema_teil2, datum_delta,
        liste_bez_teil1, liste_punkte_teil1]
muendliche_pruefung(liste_seiten_teil1, liste_seiten_teil2, angb, clean_tex)

