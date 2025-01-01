import os
from helpers import root_path
os.chdir(root_path())

from Aufgaben import *
from skripte.erstellen import *

# ----------------------------------ab hier ist der Bereich zur Dateneingabe -----------------------------------------

# Angaben für die Klausur im pdf-Dokument
Kurs = ('Leistungskurs')
Klasse = 13
Gruppe = ''
Gesamtzeit = 300 # der Leistungskurs hat 300 min und der Grundkurs 270 min
Zeithmft = 100 # der Leistungskurs hat 100 min und der Grundkurs 90 min
datum_delta = 1  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
clean_tex = True # Hier kann mit True oder False festgelegt werden, ob die Latex-Datei gelöscht werden soll
if Kurs not in ['Grundkurs', 'Leistungskurs']:
    exit("Kurs muss 'Grundkurs' oder 'Leistungskurs' sein.")

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], [ ..., aufgabe(10)]] eintragen
aufgaben_teil1 = [[aenderungsrate(1, teilaufg=[ 'c', 'd'], ableitung=True, BE=[2,3]),
                   rekonstruktion(2, BE=[5]),
                   rechnen_mit_vektoren(3,['c'], BE=[5])],
                  [vierfeldertafel(4, ['a', 'b'], BE=[1,4]),
                   grafisches_ableiten(5, ['a', 'b'], BE=[2,3]),
                   bestimmtes_integral(6, grad=2, BE=[2,3])],
                  [rechnen_mit_vektoren(7, ['f'], BE=[5]),
                   vektoren_koll_ortho(8, BE=[5]),
                   faires_spiel(9, BE=[5]),
                   baumdiagramm(10, ['a', 'b'], stufen=2, art='zoZ', BE=[3,2])]]

# Hier die Aufgaben in der Form [[aufgabe1(), aufgabe2()],[aufgabe3(), aufgabe4()], usw.] eintragen
ana1 = [[kurvendiskussion_polynom_parameter(1, BE=[2,3,10,3,8,3,3,1,3,4])]]
ana2 = [[kurvendiskussion_exponentialfkt_parameter(2,  BE=[2,1,6,3,8,2,4,8,3,3])]]
algebra = [[geraden_aufstellen(3.1),
            geraden_lagebeziehung(3.2, teilaufg=['a', 'c', 'e'], lagebeziehung='schneiden',
                                  gerade_k=False, BE=[4,10,5])]]
stochastik = [[baumdiagramm(3,teilaufg=['c', 'd', 'e', 'f', 'g', 'h', 'i'],
                            art='zoZ', BE=[9,4,7,2,4,2,2])]]


# --------------------------------ab hier wird aus der Liste der Aufgaben die Klausur erzeugt ---------------------------

# Aufgaben für Teil I
liste_punkte_teil1 = ['Punkte']
liste_bez_teil1 = ['Aufgabe']

# hier werden aus der Liste der Aufgaben dieTest erzeugt
liste_seiten_teil1 = []
i = 0
for element in aufgaben_teil1:
    for aufgabe in element:
        liste_bez_teil1.append(str(i+1))
        liste_punkte_teil1.append(sum(aufgabe[-2]))
        i += 1
    liste_seiten_teil1.append(seite(element))

if Kurs == 'Grundkurs':
    exit('Es müssen 9 Aufgaben für den hilfsmittelfreien Teil ausgewählt werden.') if i != 9 else i
else:
    exit('Es müssen 10 Aufgaben für den hilfsmittelfreien Teil ausgewählt werden.') if i != 10 else i

aufgaben_teil2 = (ana1, ana2, algebra, stochastik)
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
angb_teil1 = [Kurs, datum_delta, liste_bez_teil1, liste_punkte_teil1]
angb_teil2 = [Kurs, datum_delta, liste_bez_teil2, liste_punkte_teil2]

vorabiturklausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex)