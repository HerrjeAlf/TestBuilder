import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *


a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

def physikalische_groessen(nr, klasse=8, phys_ein=False, BE=[]):
    # Hier sollen die Schüler und Schülerinnen eine Tabelle mit zwei gegebenen physikalischen Größen vervollständigen.
    # Mit dem Parameter "klasse=" kann festgelegt werden, aus welcher Klassenstufe die physikalischen Größen ausgewählt werden
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    uebersicht = []
    klasse_8 = [['Temperatur', 'T', NoEscape(r'$^\circ\text{C}, ~ ^\circ\text{F}$' + ', K'),'Thermometer', 3],
                ['Zeit', 't', 's, min, h', 'Uhr', 3],
                ['Weg', 's', 'm', 'Lineal', 3],
                ['Fläche', 'A', NoEscape(r'$\text{m}^2 ,~ \text{cm}^2 ,~ \text{mm}^2 $'), ' --- ', 2],
                ['Volumen', 'V', NoEscape(r'$\text{m}^3 ~$' + ', l, ml'), 'Messbecher', 3],
                ['Masse', 'm', 'g, kg, t', 'Waage', 3],
                ['Dichte', NoEscape(r'$\rho $'), NoEscape(r'$\frac{kg}{\text{m}^3}$'), 'Aräometer', 3],
                ['Kraft', 'F', 'N, kN', 'Federkraftmesser', 3],
                ['Druck', 'p', 'Pa, bar', 'Barometer', 3],
                ['Arbeit', 'W', 'J, Nm, Ws', ' --- ', 2],
                ['Energie', 'E', 'J', ' --- ', 2],
                ['Leistung', 'P', 'W', ' --- ', 2],
                ['Wärme', 'Q', 'J', 'Kalorimeter', 3]]
    klasse_9 = [['elektrische Spannung', 'U', 'V, mV', 'Voltmeter', 3],
                ['elektr. Stromstärke', 'I', 'A, mA', 'Amperemeter', 3],
                ['elektr. Widerstand', 'R', NoEscape(r'$\ohm $'), ' --- ', 2]]
    klasse_10 = [['Geschwindigkeit', 'v', NoEscape(r'$\frac{m}{s} ,~ \frac{km}{h}$'), 'Tachometer', 3],
                 ['Beschleunigung', 'a', NoEscape(r'$\frac{m}{ \text{s}^2 }$'), ' --- ', 2]]
    klasse_11 = [['Periodendauer', 'T', 's', 'Uhr', 3],
                 ['Frequenz', 'f', 'Hz', ' --- ', 2],
                 ['Drehzahl', 'n', NoEscape(r'$\frac{1}{s}$'), ' --- ', 2]]
    klasse_12 = [['Kreisfrequenz', NoEscape(r'$\omega $'), NoEscape(r'$\frac{1}{s}$'), ' --- ', 2],
                 ['Impuls', 'p', NoEscape(r'$\frac{ kg \cdot m }{ s }$'), ' --- '],
                 ['Wellenlänge', NoEscape(r'$\lambda $'), 'm', 'Lineal', 3]]
    klasse_13 = [['magn. Flussdichte', 'B', 'T', ' --- ', 2],
                 ['Induktivität', 'L', 'H', ' --- ', 2],
                 ['Kapazität', 'C', 'F', ' --- ', 2],
                 ['elektr. Ladung', 'Q', 'C', 'Elektroskop', 3],
                 ['elektr. Feldstärke', 'E', NoEscape(r'$\frac{ V }{ m }$'), 'Elektroskop', 3]]
    klasse_14 = [[]]

    if klasse == 8:
        uebersicht.extend(klasse_8)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_9[0:phys_ein])
    if klasse == 9:
        uebersicht.extend(klasse_8 + klasse_9)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_10[0:phys_ein])
    if klasse == 10:
        uebersicht.extend(klasse_8 + klasse_9 + klasse_10)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_11[0:phys_ein])
    if klasse == 11:
        uebersicht.extend(klasse_8 + klasse_9 + klasse_10 + klasse_11)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_12[0:phys_ein])
    if klasse == 12:
        uebersicht.extend(klasse_8 + klasse_9 + klasse_10 + klasse_11 + klasse_12)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_13[0:phys_ein])
    if klasse == 13:
        uebersicht.extend(klasse_8 + klasse_9 + klasse_10 + klasse_11 + klasse_12 + klasse_13)
        if phys_ein in list(range(0,phys_ein)):
            uebersicht.extend(klasse_14[0:phys_ein])
    if klasse not in list(range(8,14)):
        print('Der Parameter klasse= muss von 8 bis 13 gehen!')

    ausw = np.random.choice(list(range(len(uebersicht))),2, False)

    table1 = Tabular('|c|c|c|c|', row_height=2)
    table1.add_hline()
    table1.add_row(bold('physikalische Größe'), bold('Formelzeichen'), bold('Einheit(en)'), bold('Messgerät'))
    table1.add_hline()
    table1.add_row(uebersicht[ausw[0]][0], '', '', '')
    table1.add_hline()
    table1.add_row(uebersicht[ausw[1]][0], '', '', '')
    table1.add_hline()

    table2 = Tabular('|c|c|c|c|c|', row_height=1.5)
    table2.add_hline()
    table2.add_row(bold('physikalische Größe'), bold('Formelzeichen'), bold('Einheit(en)'),
                   bold('Messgerät'), bold('Punkte'))
    table2.add_hline()
    table2.add_row(uebersicht[ausw[0]][0], bold(uebersicht[ausw[0]][1]), bold(uebersicht[ausw[0]][2]),
                   bold(uebersicht[ausw[0]][3]), uebersicht[ausw[0]][4])
    table2.add_hline()
    table2.add_row(uebersicht[ausw[1]][0], bold(uebersicht[ausw[1]][1]), bold(uebersicht[ausw[1]][2]),
                   bold(uebersicht[ausw[1]][3]), uebersicht[ausw[1]][4])
    table2.add_hline()

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vervollständige die Tabelle der physikalische Größen. \n\n', table1]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}', table2, ' \n\n']
    grafiken_aufgaben = []
    grafiken_loesung = []
    punkte = uebersicht[ausw[0]][4] + uebersicht[ausw[1]][4]

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2].'
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
