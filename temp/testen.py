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

for i in range(anzahl):
    Aufgaben = [geraden_lagebeziehung(1, lagebeziehung='windschief', notizfeld=True, neue_seite=[1,2,3,4,5,6]), geraden_aufstellen(2, T_auf_g=True, spurpunkt='all', notizfeld=True, neue_seite=[3])]

    liste_punkte, liste_bez = ['Punkte'], ['Aufgabe']
    for aufgabe in Aufgaben:
        liste_bez.extend(aufgabe[5])
        liste_punkte.extend(aufgabe[4])
    sheets = seite(Aufgaben)


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
        code = generate_mixed_code()
        angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte, code]

    # Erstellt die Tests und nimmt die Pfade, welche zurückgegeben werden
    pdfs = test_erzeugen(sheets, angaben, i, probe, clean_tex)

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
