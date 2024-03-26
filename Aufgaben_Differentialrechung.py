from pylatex import (MediumText)
from pylatex.utils import bold
import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *

from funktionen import *
from plotten import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def kurvendiskussion_polynome(nr, teilaufg):
    liste_punkte = []
    liste_bez = []
    i = 0

    if random.random() < 0.5:
        nst_1 = zzahl(0, 2)
        nst_2 = nst_1 + nzahl(1, 2) + 0.5
        nst_3 = nst_1 - nzahl(2, 3) - 0.5
        faktor = zzahl(2, 8) / 2

        fkt = collect(expand(faktor_f * (x - nst_1) * (x - nst_2) * (x - nst_3)), x)
        fkt_a1 = faktor
        fkt_a2 = -1 * faktor * (nst_1 + nst_2 + nst_3)
        fkt_a3 = faktor * ((nst_1 * nst_2) + (nst_1 * nst_3) + (nst_2 * nst_3))
        fkt_a4 = -1 * faktor * nst_1 * nst_2 * nst_3
        fkt_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3,'x')
                   + vorz_str(fkt_a4))

        fkt_partial = expand(faktor * (x - nst_2) * (x - nst_3))
        fkt_partial_pq = expand((x - nst_2) * (x - nst_3))
        fkt_partial_p = -1 * (nst_2 + nst_3)
        fkt_partial_q = (nst_2 * nst_3)

        fkt_1 = expand(diff(fkt, x, 1))
        fkt_1_pq = 'x^2' + vorz_str(Rational(-2 * (nst_1 + nst_2 + nst_3), 3)) + \
                     'x~' + vorz_str(Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3))
        p_fkt_1_pq = Rational(-2 * (nst_1 + nst_2 + nst_3), 3)
        q_fkt_1_pq = Rational((nst_1 * (nst_2 + nst_3)) + (nst_2 * nst_3), 3)
        s_fkt = -1 * faktor * nst_1 * nst_2 * nst_3


    else:
        nst_1 = zzahl(0,2)
        quadr_nst_23 = nzahl(2, 25)
        nst_2 = math.sqrt(quadr_nst_23)
        nst_3 = -1 * nst_2
        faktor_f = zzahl(2,8) / 2

        fkt = collect(expand(faktor_f * (x - nst_1) * (x - nst_2) * (x - nst_3)),x)
        fkt_a1 = faktor_f
        fkt_a2 = -1 * faktor_f * nst_1
        fkt_a3 = faktor_f * (-1 * quadr_nst_23)
        fkt_a4 = faktor_f * nst_1 * quadr_nst_23
        fkt_str = (vorz_v_aussen(fkt_a1,'x^3') + vorz_v_innen(fkt_a2,'x^2') + vorz_v_innen(fkt_a3,'x')
                   + vorz_str(fkt_a4))

        fkt_partial = faktor_f * (x ** 2 - quadr_nst_23)
        fkt_partial_pq = x ** 2 - quadr_nst_23
        fkt_partial_p = 0
        fkt_partial_q = -1 * quadr_nst_23

        fkt_1 = expand(diff(fkt, x, 1))
        fkt_1_pq = 'x^2' + vorz_str(Rational(-2 * nst_1, 3)) + \
                     'x~' + vorz_str(Rational(quadr_nst_23, -3))
        p_fkt_1_pq = Rational((-2 * nst_1), 3)
        q_fkt_1_pq = Rational(-1 * quadr_nst_23, 3)
        s_fkt = faktor_f * nst_1 * quadr_nst_23

    fkt_b2 = nst_1 * fkt_a1
    fkt_c2 = fkt_a2 + fkt_b2
    fkt_b3 = nst_1 * fkt_c2
    fkt_c3 = fkt_a3 + fkt_b3
    fkt_b4 = nst_1 * fkt_c3
    fkt_c4 = fkt_a4 + fkt_b4

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben ist die Funktion:',
               r' f(x)~=~' + fkt_str]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']
    grafiken_aufgaben = ['', '', '']
    grafiken_loesung = ['']


    
    if 'a' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        grenzwert_min = limit(fkt, x, -oo)
        grenzwert_pos = limit(fkt, x, oo)

        aufgabe.append(str(liste_teilaufg[i]) + f') Untersuche das Verhalten der Funktion im Unendlichen. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \lim\limits_{x \to \infty} ' + fkt_str + '~=~' + \
                       latex(grenzwert_pos) + r' \quad \mathrm{und} \quad \lim\limits_{x \to - \infty} ' + \
                       fkt_str + '~=~' + latex(grenzwert_min) + r' \quad (2P) \\\\')

        i += 1

    if 'b' in teilaufg:
        punkte_aufg = 2
        liste_punkte.append(punkte_aufg)
        liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
        grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
        grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

        fkt_sym = fkt.subs(x, -x)
        if fkt_sym == fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~f(x) \quad \to \quad \mathrm{Achsensymmetrie} \quad (3P) \\\\')
        elif fkt_sym == -1 * fkt:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym)
                   + r'~=~-f(x) \quad \to \quad \mathrm{Punktsymmetrie} \quad (3P) \\\\')
        else:
            lsg = (r') \quad f(-x)~=~' + latex(fkt_sym) + r' \neq  f(x)  \neq -f(x) \quad \to \quad'
                                                          r'\mathrm{nicht~symmetrisch} \quad (3P) \\\\')
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Symmetrie der Funktion f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + lsg)

        i += 1
        
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]