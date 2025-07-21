import numpy as np
import string
import random, math
from math import degrees
from sympy import *
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)

from scipy.stats import norm, binom
from skripte.funktionen import *
from collections import Counter
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

[[[MediumText([NoEscape(\textbf{Aufgabe 1 \newline%
\newline%
})], [NoEscape(\textbf{Aufgabe 1 \newline%
\newline%
})]), NoEscape(Im unteren Koordinatensystem ist der Graph der Parabel p(x) = $ x^2 +2x-3$ dargestellt.), ['Grafik', '200px'], NoEscape( \noindent a) Lesen Sie den Scheitelpunkt S$ \left( \qquad \vert \qquad \right) $ der Parabel ab. ), ' \n\n', NoEscape( \noindent b) Stellen Sie die Parabelgleichung in Scheitelpunktform auf.), ' \n\n', 'NewPage', NoEscape( \noindent c) Berechnen Sie die Nullstellen und vergleichen Sie ihre Ergebnisse mit dem Graphen.), ' \n\n', NoEscape( \noindent Gegeben sind zwei Punkte der linearen Funktion g mit P$ \left( -4 \vert -5 \right) $ und Q$ \left( 5 \vert 4 \right). $), ' \n\n ', NoEscape( \noindent d) Zeichnen Sie den Graphen der linearen Funktion g in das obere Koordinatensystem ein.), ' \n\n', NoEscape( \noindent e) Erläutern Sie anhand des Graphen die Funktionsgleichung von $ g(x) =  x-1$. ), ' \n\n', NoEscape( \noindent f) Berechnen Sie die Schnittpunkte der linearen Funktion mit dem Graphen der Parabel.), ' \n\n'], [' \\mathbf{Lösung~Aufgabe~}1 \\hspace{35em}', 'a) \\quad  \\mathrm{der~Scheitelpunkt~lautet:} \\quad S \\left( -1 \\vert -4 \\right) \\quad (1BE)', 'b) \\quad  p(x) ~=~ \\left( x+1 \\right) ^2 -4 \\quad (2BE)', 'c) \\quad  p(x) ~=~ 0 \\quad \\to \\quad 0 ~=~ x^2 +2x-3 \\quad (1BE) \\hspace{10em} \\\\ x_{ 1,2 } ~=~ - \\frac{p}{2} \\pm \\sqrt{ \\left( \\frac{p}{2} \\right) ^2 - q }  ~=~ - \\frac{ 2 }{2} \\pm \\sqrt{ \\left( \\frac{ 2}{2} \\right) ^2 +3} ~=~ -1 \\pm \\sqrt{ 4 } \\quad (1BE) \\\\ x_1 ~=~ -3 \\quad \\mathrm{und} \\quad x_2 ~=~ 1 \\quad \\to \\quad \\mathrm{Sie~stimmen~mit~Graphen~überein} \\quad (3BE)', 'd) \\quad  \\mathrm{Punkte~(2BE) \\quad Graph~(1BE)} ', ['Grafik', '150px'], Tabular(NoEscape(p{0.2cm} p{0.2cm} p{13cm} p{2cm}), [NoEscape(e)&\multicolumn{2}{l}{Erläuterung der Funktionsgleichung}&Punkte\\), NoEscape(&{-}&die Zahl hinter dem x ist der y{-}Achsenabschnitt n und entspricht dem Schnittpunkt des Graphen mit dem y{-}Achse&2BE\\), NoEscape(&{-}&die Zahl vorm x entspricht der Steigung m und kann mithilfe des Steigungsdreiecks bestimmt werden.&1BE\\), NoEscape(&{-}&dafür geht man vom Punkt ( 0 | {-}1 ) eins nach recht und dann 1LE nach oben, was der Steigung entspricht&1BE\\), NoEscape(&&&insg.: 4BE\\)], None, [NoEscape(e)&\multicolumn{2}{l}{Erläuterung der Funktionsgleichung}&Punkte\\), NoEscape(&{-}&die Zahl hinter dem x ist der y{-}Achsenabschnitt n und entspricht dem Schnittpunkt des Graphen mit dem y{-}Achse&2BE\\), NoEscape(&{-}&die Zahl vorm x entspricht der Steigung m und kann mithilfe des Steigungsdreiecks bestimmt werden.&1BE\\), NoEscape(&{-}&dafür geht man vom Punkt ( 0 | {-}1 ) eins nach recht und dann 1LE nach oben, was der Steigung entspricht&1BE\\), NoEscape(&&&insg.: 4BE\\)]), ' \n\n', 'f) \\quad  g(x) ~=~ p(x) \\quad \\to \\quad  x-1~=~ x^2 +2x-3 \\quad \\vert +1 \\quad \\vert -x \\quad \\to \\quad 0 ~=~ x^2 +x-2 \\quad (2BE) \\\\ x_{ 1,2 } ~=~ - \\frac{p}{2} \\pm \\sqrt{ \\left( \\frac{p}{2} \\right) ^2 - q}  ~=~ - \\frac{ 1 }{2} \\pm \\sqrt{ \\left( \\frac{ 1}{2} \\right) ^2 +2 } ~=~~=~ - \\frac{1}{2} \\pm \\sqrt{ \\frac{9}{4} } \\quad (1BE) \\\\ x_1 ~=~ 1 \\quad \\mathrm{und} \\quad x_2 ~=~ -2 \\quad (2BE) \\\\ S_1 \\left( 1 \\vert 0 \\right) \\quad \\mathrm{und} \\quad S_2 \\left( -2 \\vert -3 \\right) \\quad (2BE) '], ['Aufgabe_1'], ['Loesung_1_d)'], [1, 2, 5, 3, 4, 7], ['1.a)', '1.b)', NoEscape(1.c)), '1.d)', '1.e)', NoEscape(1.f))]]