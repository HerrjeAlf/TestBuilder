import os
import sys
import json
from helpers import root_path
from PyPDF2 import PdfMerger
from Aufgaben import *
from skripte.erstellen import *

os.chdir(root_path())

test = PdfMerger()
erwartungshorizont = PdfMerger()
pdfs = ['pdf/name']

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'E-Kurs'
Fach = 'Mathematik'
Klasse = '10'
Lehrer = 'Herr Herrys'
Art = 'Test'
Titel = 'Vorlage'
datum_delta = 1  # Wann wird der Test geschrieben (in Tagen - 0 ist Heute, 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = [True, False][0] # True: Probe 01, 02 usw. oder False: Gr. A, Gr. B usw
clean_tex = [True, False][0]

aufgabenliste = [[(lineare_funktionen, [1])]]

for i in range(anzahl):
    Aufgaben = [[titel(*args) for titel, args in teil_liste] for teil_liste in aufgabenliste]

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

    if len(sys.argv) > 1 and sys.argv[1] == 'website':
        schnell = True if sys.argv[2] == 'True' else False
        if schnell:
            uuid, identifier = sys.argv[-1], sys.argv[-2]
            angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, None, liste_bez, liste_punkte, schnell, identifier, uuid]
        else:
            probe = True if sys.argv[8] == 'Probe' else False
            schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum, identifier, uuid = sys.argv[3:]
            angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum, liste_bez, liste_punkte, identifier, uuid]
    else:
        code = create_unique_code('daten/aufgaben')
        aufgabenliste_serialisiert = serialisiere_aufgaben_liste(aufgabenliste)
        save_new_entry("daten/aufgaben.json", code, aufgabenliste_serialisiert)
        angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte, code]



    # Erstellt die Tests und nimmt die Pfade, welche zurückgegeben werden
    pdfs = test_erzeugen(liste_seiten, angaben, i, probe, clean_tex)

    test.append(f'{pdfs[0]}.pdf')
    erwartungshorizont.append(f'{pdfs[1]}.pdf')

if anzahl > 1:
    pfad = ' '.join(pdfs[0].split(' ')[:-2])

    test.write(f'{pfad}.pdf')
    print(f'\033[38;2;100;141;229m\033[1mTests zusammengefügt\033[0m')
    test.close()

    erwartungshorizont.write(f'{pfad} - Lsg.pdf')
    print(f'\033[38;2;100;141;229m\033[1mErwartungshorizonte zusammengefügt\033[0m')
    erwartungshorizont.close()
