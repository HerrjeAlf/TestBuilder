from Aufgaben.Aufgaben_Algebra import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'Test'
Titel = 'Punkte und Vektoren'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1  # wie viele verschiedenen Tests sollen erzeugt werden
probe = True    # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for i in range(anzahl):
    aufgaben_seite1 = [punkte_und_vektoren(1, ['a', 'b', 'c']),
                       rechnen_mit_vektoren(2,['a', 'b', 'c', 'd', 'e', 'f'], linearkombination=True, kollinear=False)]
    for element in aufgaben_seite1:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])
    # print(element[0][4])
    # print(element[2][4])

#    aufgaben_seite2 = [aenderungsrate(2, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])]
#    for element in aufgaben_seite2:
#        liste_bez.extend(element[5])
#        liste_punkte.extend(element[4])

    liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
    angaben = [Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

    pdf_erzeugen(liste_seiten, angaben, i, probe)

