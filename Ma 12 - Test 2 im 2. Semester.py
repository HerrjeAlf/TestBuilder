from Aufgaben.Aufgaben_Analysis import *
from Aufgaben.Aufgaben_Algebra import *
from Aufgaben.Aufgaben_Wahrscheinlichkeitsrechnung import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = 'Test 2 (2. Sem.)'
Titel = 'höhere Ableitungsregeln und Wachstum'
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = False   # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']
# Berechnung der Aufgabenteile
teilaufg_nr1 = np.random.choice(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'), 2, False)
teilaufg_nr2 = np.random.choice(('a', 'b', 'c', 'd', 'e', 'f'), 2, False)
teilaufg_nr4 = np.random.choice(('e', 'f', 'g', 'h', 'i', 'j'), 2, False)
print(teilaufg_nr1)
print(teilaufg_nr2)
print(teilaufg_nr4)

for i in range(anzahl):
    aufgaben_seite1 = [logarithmusgesetze(1, teilaufg_nr1),
                       exponentialgleichungen(2, teilaufg_nr2),
                       wachstumsfunktion(3),
                       ableitungen(4, teilaufg_nr4)]
    for element in aufgaben_seite1:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    aufgaben_seite2 = []
    for element in aufgaben_seite2:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]
    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

    test_erzeugen(liste_seiten, angaben, i, probe)

