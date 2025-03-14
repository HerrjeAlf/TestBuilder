import os
from helpers import root_path
from PyPDF2 import PdfMerger
from Aufgaben import *
from skripte.erstellen import *

os.chdir(root_path())

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'HAK 04'
Titel = 'Binomialverteilung'
datum_delta = 1  # Wann wird der Test geschrieben (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 2 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False # True: Probe 01, 02 usw. oder False: Gr. A, Gr. B usw
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
Aufgabenliste = [[binomialverteilung(1), prognoseintervall(2)]]












# --------------------------------ab hier werden aus den eingegebenen Daten die Tests erzeugt ----------------------------

clean_tex = True if clean_tex not in [True, False] else clean_tex

test = PdfMerger()
erwartungshorizont = PdfMerger()
pdfs = ['pdf/name']

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

    # Erstellt die Tests und nimmt die Pfade, welche zurückgegeben werden
    pdfs = test_erzeugen(liste_seiten, angaben, i, probe, clean_tex)

    test.append(f'{pdfs[0]}.pdf')
    erwartungshorizont.append(f'{pdfs[1]}.pdf')

if anzahl > 1:
    pfad = ' '.join(pdfs[0].split(' ')[:-2])

    test.write(f'{pfad}.pdf')
    print(f'\033[38;2;100;141;229m\033[1mAufgaben PDF zusammengeführt\033[0m')
    test.close()

    erwartungshorizont.write(f'{pfad} - Lsg.pdf')
    print(f'\033[38;2;100;141;229m\033[1mErwartungshorizont PDF zusammengeführt\033[0m')
    erwartungshorizont.close()
