import random
import numpy as np
from sympy import *
from decimal import *
from skripte.funktionen import *
from skripte.plotten import *
from sympy.stats import Binomial, P


a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
# b = list(range(1,4))
# print(b)

# i = 0
# for m in range(1,7):
#     for n in range(1,7):
#         if m + n > 9:
#             print ('m: ' + str(m) + ' und n: ' + str(n) + ' und m+n:' + str(m+n))
#             i += 1
# print(i)

# a = [[1,2],[2,3]]

# wert = 123.3
# wert_neu = str(wert).replace('.', ',')

# b = zzahl(2,5)
# print(b)
# extrema_xwert = zzahl(1,4)
# nst= vorz_fakt(extrema_xwert) * (abs(extrema_xwert) + nzahl(1,3))
# c = -1*nst*b
# print(c)
# fkt_v = exp(a * x)*(b*x + c)
# fkt_a1 = diff(fkt_v, x)
# gleichung2 = Eq(fkt_a1.subs(x, extrema_xwert), 0)
# lsg = solve(fkt_a1.subs(x, extrema_xwert), a)
# fkt = exp(lsg[0]*x)*(b*x+c)
# fkt_1 = diff(fkt,x)
# fkt_2 = diff(fkt, x, 2)
# fkt_3 = diff(fkt,x,3)
# fkt_1_str_zw = (gzahl(b) + r' \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} + (' + vorz_v_aussen(b, 'x')
#                 + vorz_str(c) + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} \cdot '
#                 + gzahl_klammer(lsg[0]))
# fkt_1_str = ('(' + vorz_v_aussen(lsg[0] * b, 'x') + vorz_str(lsg[0] * c + b)
#              + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'}')
# fkt_2_str_zw = (gzahl(lsg[0] * b) + r' \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} + '
#                 + '(' + vorz_v_aussen(lsg[0] * b, 'x') + vorz_str(lsg[0] * c + b)
#                 + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} \cdot '
#                 + gzahl_klammer(lsg[0]))
# fkt_2_str = ('(' + vorz_v_aussen(lsg[0] ** 2 * b, 'x') + vorz_str(lsg[0] ** 2 * c + 2 * lsg[0] * b)
#              + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'}')
# fkt_3_str_zw = (gzahl(lsg[0] ** 2 * b) + r' \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} + '
#                 + '(' + vorz_v_aussen(lsg[0] ** 2 * b, 'x') + vorz_str(lsg[0] ** 2 * c + 2 * lsg[0] * b)
#                 + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'} \cdot '
#                 + gzahl_klammer(lsg[0]))
# fkt_3_str = ('(' + vorz_v_aussen(lsg[0] ** 3 * b, 'x') + vorz_str(lsg[0] ** 3 * c + 3 * lsg[0] ** 2 * b)
#              + r') \cdot e^{' + vorz_v_aussen(lsg[0], 'x') + r'}')
# ywerte = [(element, fkt.subs(x, element)) for element in range(-20, 20)]
# k = 0
# wertebereich = []
# for zahl in range(len(ywerte)-1):
#     if abs(ywerte[k][1]) < 6 and abs(ywerte[k][1] - ywerte[k + 1][1]) > 0.5:
#         wertebereich.append(ywerte[k][0])
#     k += 1
# print(wertebereich)
# xmin = wertebereich[0]
# xmax = wertebereich[-1]
# plot(fkt, (x,xmin,xmax))
# print(fkt)
# print(lsg)
# print('x_E: ' + str(extrema_xwert))
# # print('y_E: ' + str(extrema_ywert))
# print('nst: ' + str(nst))
# print(fkt_1_str_zw)
# print(fkt_1_str)
# print(latex(fkt_1))
# print(fkt_2_str_zw)
# print(fkt_2_str)
# print(latex(fkt_2))
# print(fkt_2_str_zw)
# print(fkt_2_str)
# print(latex(fkt_3))

#extrema_xwert = zzahl(1, 3)
#extrema_ywert = zzahl(1, 3)
#if extrema_xwert > 0:
#    y_vers = -1 * nzahl(1, 3)
#else:
#    y_vers = nzahl(1, 3)
#fkt_v = exp(b * x + 2) * a * x ** 2
#fkt_a1 = diff(fkt_v, x)
#gleichung1 = Eq(fkt_v.subs(x, extrema_xwert), extrema_ywert)
#gleichung2 = Eq(fkt_a1.subs(x, extrema_xwert), 0)
#lsg = solve((gleichung1, gleichung2), (a, b))
#lsg_a = lsg[0][0]
#lsg_b = lsg[0][1]
# print(lsg)
#fkt = exp(lsg_b * x + 2) * lsg_a * x ** 2 + y_vers
#fkt_str = (vorz_v_aussen(lsg_a, 'x^2') + r' \cdot e^{' + vorz_v_aussen(lsg_b, 'x+2') + '}'
#           + vorz_str(y_vers))

# Werte für Angaben zum Zeichnen des Graphen
#ywerte = [(element, fkt.subs(x, element)) for element in range(-5, 6)]
#wertebereich = [element[0] for element in ywerte if abs(element[1]) < 6]
#xmin = wertebereich[0]
#xmax = wertebereich[-1]
#plot(fkt,(x,xmin,xmax))
#print(lsg)

# def schreibweise(zahl, darstellung='wiss'):

# def lsg1(wert_a):
#     g1 = N(1-19*a,3)
#     g2 = N(-1*(4+3*a),3)*x + N(2-2*a,3)*y+N(3-2*a,3)*z
#     print('a:')
#     wert_a = 0 if wert_a == '' else wert_a
#     print(latex(g2.subs(a, wert_a)) + ' = ' + latex(g1.subs(a, wert_a)))
#
# def lsg2(ywerte):
#     xwerte = [0,1,2,3]
#     E_wert = N(sum([xwert*ywert for xwert, ywert in zip(xwerte, ywerte)]),3)
#     V_wert = N(sum([(xwert - E_wert)**2*ywert for xwert, ywert in zip(xwerte, ywerte)]),3)
#     sigma = N(sqrt(V_wert),3)
#     print('E(X) = ' + str(E_wert))
#     print('V(X) = ' + str(V_wert))
#     print('sigma(X) = ' + str(sigma))
#
# lsg1(0.53)
# lsg2([0.105,0.263,0.263,0.105])


def gauss_elimination(gleichungen, variablen=[]):
    """
    Löst ein lineares Gleichungssystem mit der Methode der Gaußschen Elimination.

    :param gleichungen: Liste der Koeffizienten (Matrix A).
    :param ergebnisse: Liste der Ergebnisse (Vektor b).
    :return: Liste der Lösungen oder eine Beschreibung der Schritte.
    """
    beschrift = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
    beschrift_reverse = {value: key for key, value in beschrift.items()}
    n = len(gleichungen)
    variablen = [liste_teilaufg[step] for step in range(len(gleichungen[0]) - 1)] if variablen == [] else variablen
    print(gleichungen)
    zw_lsg = gleichungen.copy()
    gleichungen = []
    for i in range(n):
        for element in zw_lsg:
            if element[i] != 0:
                gleichungen.append(element)
                zw_lsg.remove(element)

    loesung = [[beschrift.get(k + 1, 'zu groß'), ''] + gleichungen[k] for k in range(n)]
    print(gleichungen)
    print(loesung)

    for i in range(n):
        for k in range(i + 1, n):
            if gleichungen[k][i] != 0:
                text = (NoEscape(
                    '$' + gzahl(gleichungen[i][i]) + r' \cdot ' + beschrift.get(i + 1, 'zu groß') + vorz_str(
                        -1 * gleichungen[k][i])
                    + r' \cdot ' + beschrift.get(k + 1, 'zu groß' + ' $')))
                neue_zeile = [gleichungen[i][i] * gleichungen[k][step] - gleichungen[k][i] * gleichungen[i][step]
                              for step in range(0, len(gleichungen[0]))]
                gleichungen[k] = neue_zeile
                loesung.append([beschrift.get(k + 1, 'zu groß'), text] + neue_zeile)

    print(loesung)
    k = beschrift_reverse[loesung[-1][0]]
    gleich_lsg = []
    for anz in reversed(list(range(k))):
        for eintrag in reversed(loesung):  # Liste von hinten durchgehen
            if eintrag[0] == beschrift[anz + 1]:
                gleich_lsg.append(eintrag)  # Letztes Element zurückgeben
                break

    print(gleich_lsg)

    # und hier eine Funktion die aus gleich_lsg den Lösungstext erstellt "aus III folgte c = ..."

    # noch eine Funktion, die loesung als Tabelle darstellt
    anz_sp = len(loesung[0]) + 1
    spalten = '|'
    for step in range(anz_sp):
        spalten += 'c|'
    table1 = Tabular(spalten, row_height=1.2)
    table1.add_hline(2)
    table1.add_row(['Berechnung mit dem Gauß-Algorithmus', ' Nr', 'Berechnung'] + variablen + ['lsg'])
    table1.add_hline(2)
    for zeile in loesung:
        liste = [''] + [str(element) for element in zeile]
        table1.add_row(liste)
        table1.add_hline(2)
    print(table1)

    print(loesung)
    return loesung, table1


# Beispiel

gleichungen = [[-4,1,1,-15], [1,-3,-4,25], [0, 2, 3, -18]]
erg = gauss_elimination(gleichungen)
print(erg)



