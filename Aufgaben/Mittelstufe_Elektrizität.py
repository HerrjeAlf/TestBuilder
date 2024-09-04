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

def physikalische_groessen(nr, klasse=8, BE=[]):
    # Hier sollen die Schüler und Schülerinnen eine Tabelle mit zwei gegebenen physikalischen Größen vervollständigen.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{nr}']
    uebersicht = [['Temperatur', 'T', NoEscape(r'$^\circ\text{C}, ~ ^\circ\text{F}$' + ', K'),'Thermometer', 3],
                  ['Weg', 's', 'm', 'Lineal', 3],
                  ['Volumen', 'V', NoEscape(r'$\text{m}^3 ~$' + ', l, ml'), 'Messbecher', 3],
                  ['Masse', 'm', 'g, kg, t', 'Waage', 3],
                  ['Dichte', NoEscape(r'$\rho $'), NoEscape(r'$\frac{kg}{\text{m}^3}$'), 'Aräometer', 3],
                  ['Kraft', 'F', 'N, kN', 'Federkraftmesser', 3],
                  ['Druck', 'p', 'Pa, bar', 'Barometer', 3],
                  ['Arbeit', 'W', 'J, Nm, Ws', ' --- ', 2],
                  ['Energie', 'E', 'J', ' --- ', 2]]

    ausw = np.random.choice(list(range(len(uebersicht))),2, False)

    table1 = Tabular('|c|c|c|c|', row_height=1.2)
    table1.add_hline()
    table1.add_row(bold('physikalische Größe'), bold('Formelzeichen'), bold('Einheit(en)'), bold('Messgerät'))
    table1.add_hline()
    table1.add_row(uebersicht[0][0], '', '', '')
    table1.add_hline()
    table1.add_row(uebersicht[1][0], '', '', '')
    table1.add_hline()

    table2 = Tabular('|c|c|c|c|', row_height=1.2)
    table2.add_hline()
    table2.add_row(bold('physikalische Größe'), bold('Formelzeichen'), bold('Einheit(en)'), bold('Messgerät'))
    table2.add_hline()
    table2.add_row(uebersicht[ausw[0]][0], uebersicht[ausw[0]][1], uebersicht[ausw[0]][2], uebersicht[ausw[0]][3])
    table2.add_hline()
    table2.add_row(uebersicht[ausw[1]][0], uebersicht[ausw[1]][1], uebersicht[ausw[1]][2], uebersicht[ausw[1]][3])
    table2.add_hline()

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vervollständigen Sie die Tabelle der physikalische Größen. \n\n', table1]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}', table2, ' \n\n']
    grafiken_aufgaben = []
    grafiken_loesung = []
    punkte = uebersicht[ausw[0]][4] + uebersicht[ausw[1]][4]

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
