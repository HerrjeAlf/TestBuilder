import os
from helpers import root_path
os.chdir(root_path())
from Aufgaben import *
from skripte.erstellen import *

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Basisaufgaben in der Form eintragen
Basisaufgaben = [[basisaufgaben(1, neue_seite=6)]]

# Hier die Aufgaben zu den verschiedenen Themen in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
Trigonometrie = [[pruefung_kl10_allg_dr_01(2, pruef_kl10=True, neue_seite=1, BE=[2,3,3,3])]]
Funktionen = [[parabel_und_gerade(3, pruef_kl10=True, neue_seite=2, BE=[1,2,5,3,2,7])]]
Flaechenberechnung = [[pool(4, pruef_kl10=True, neue_seite=1)]]
Wahrscheinlichkeit = [[baumdiagramm(5, ['a', 'b', 'c'], stufen=2, art='zmZ', pruef_kl10=True)]]














# --------------------------------ab hier wird aus den eingegebenen Daten die Klausur erzeugt ---------------------------

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben die Test erzeugt
liste_seiten_teil1 = []
for element in Basisaufgaben:
    for aufgabe in element:
        liste_bez_teil1.extend(aufgabe[5])
        liste_punkte_teil1.extend(aufgabe[4])
    liste_seiten_teil1.append(seite(element))


aufgaben_teil2 = (Trigonometrie, Funktionen, Flaechenberechnung, Wahrscheinlichkeit)
liste_seiten_teil2 = []
liste_punkte_teil2 = []
liste_bez_teil2 = []
for aufgaben in aufgaben_teil2:
    liste_punkte = ['Punkte']
    liste_bez = ['Aufgabe']

    # hier werden aus der Liste der Aufgaben die Tests erzeugt
    liste_seiten = []
    for element in aufgaben:
        for aufgabe in element:
            liste_bez.extend(aufgabe[5])
            liste_punkte.extend(aufgabe[4])
        liste_seiten.append(seite(element))
    liste_seiten_teil2.append(liste_seiten)
    liste_punkte_teil2.append(liste_punkte)
    liste_bez_teil2.append(liste_bez)

#  Angaben für die Klausur
clean_tex = False if clean_tex not in [True, False] else clean_tex
angb_teil1 = [datum_delta, liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [datum_delta, liste_bez_teil2, liste_punkte_teil2]

vorpruefung_kl10(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex)