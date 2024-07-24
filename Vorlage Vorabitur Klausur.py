from Aufgaben.Oberstufe_Analysis import *
from skripte.erstellen import *

# Angaben für die Klausur im pdf-Dokument
Kurs = 'Leistungskurs'
Klasse = 13
Gruppe = ''
Gesamtzeit = 285
Zeithmft = 90
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
if Kurs != 'Grundkurs' and Kurs != 'Leistungskurs':
    exit("Kurs muss 'Grundkurs' oder 'Leistungskurs' sein.")

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], [ ..., aufgabe(10)]] eintragen
aufgaben_teil1 = [[ableitungen(1, ['a', 'b', 'c']), ableitungen(2, ['b']), ableitungen(3, ['c'])],
                  [ableitungen(4, ['d']), ableitungen(5, ['e']), ableitungen(6, ['f'])],
                  [ableitungen(7, ['a']), ableitungen(8, ['b']), ableitungen(9, ['c'])],
                  [ableitungen(10, ['a'])]]

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil1 = []
i = 1
for element in aufgaben_teil1:
    for aufgabe in element:
        liste_bez_teil1.append(str(i))
        liste_punkte_teil1.append(sum(aufgabe[-2]))
        i += 1
    liste_seiten_teil1.append(seite(element))
print(liste_bez_teil1)
print(liste_punkte_teil1)
if i < 10:
    exit('Es müssen 10 Aufgaben für den hilfsmittelfreien Teil ausgewählt werden.')

# Aufgaben für Teil II
liste_punkte_teil2 = ['Punkte']
liste_bez_teil2 = ['Aufgabe']


# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
aufgaben_teil2 = [[kurvendiskussion_polynome_01(1)],]

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil2 = []
for element in aufgaben_teil2:
    for aufgabe in element:
        liste_bez_teil2.extend(aufgabe[5])
        liste_punkte_teil2.extend(aufgabe[4])
    liste_seiten_teil2.append(seite(element))

#  Angaben für die Klausur
angb_teil1 = [Kurs, datum_delta, liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [Kurs, datum_delta, liste_bez_teil2, liste_punkte_teil2]

vorabiturklausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2)