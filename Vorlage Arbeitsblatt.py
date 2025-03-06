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
Klasse = '13'
Thema = 'Kurvendiskussion'
datum_delta = 1  # Wann bekommen die SuS das Arbeitsblatt (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll

Aufgabenliste = [[aenderungsrate(1),
                  kurvendiskussion_polynome(2, ['c']),
                  kurvendiskussion_polynome(3, ['c'], grad=4)],
                 [grafisches_ableiten(4)]]













# --------------------------------ab hier werden aus den eingegebenen Daten die Arbeitsblätter erzeugt ----------------------------

clean_tex = True if clean_tex not in [True, False] else clean_tex

test = PdfMerger()
erwartungshorizont = PdfMerger()
pdfs = ['pdf/name']

for i in range(anzahl):
    # Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
    Aufgaben = Aufgabenliste

    # hier werden aus der Liste der Aufgaben dieTest erzeugt
    liste_seiten = []
    for element in Aufgaben:
        liste_seiten.append(seite(element)) # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Klasse, Thema, datum_delta]

    # Erstellt die Arbeitsblätter und nimmt die Pfade, welche zurückgegeben werden
    pdfs = arbeitsblatt_erzeugen(liste_seiten, angaben, i, clean_tex)

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
