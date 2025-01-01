import os
from helpers import root_path
os.chdir(root_path())
from Aufgaben import *
from skripte.erstellen import *
# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = ('E-Kurs')
Fach = 'Mathematik'
Klasse = '10'
Lehrer = 'Herr Herrys'
Art = 'Test'
Titel = 'Vorlage'
datum_delta = 1  # Wann wird der Test geschrieben (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False # True: Probe 01, 02 usw. oder False: Gr. A, Gr. B usw
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
Aufgabenliste = [[kongruente_Dreiecke(1), rechtwinkliges_dreieck(2), verhaeltnisgleichgungen(3)],
                 [sachaufgabe_wetterballon(4), sachaufgabe_rampe(5)]]












# --------------------------------ab hier werden aus der Liste der Aufgaben die Tests erzeugt ----------------------------

clean_tex = True if clean_tex not in [True, False] else clean_tex

for i in range(anzahl):
    Aufgaben = Aufgabenliste

    # Bezeichnung der Punktetabelle
    liste_punkte = ['Punkte']
    liste_bez = ['Aufgabe']

    # auslesen der Bezeichung und der Punkte aus den Aufgaben
    liste_seiten = []
    for element in Aufgaben:
        for aufgabe in element:
            liste_bez.extend(aufgabe[5])
            liste_punkte.extend(aufgabe[4])
        liste_seiten.append(seite(element)) # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]
    test_erzeugen(liste_seiten, angaben, i, probe, clean_tex)

