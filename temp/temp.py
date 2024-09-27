import random, math

from sympy import *
from skripte.funktionen import *

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

anz_ziffern = nzahl(3, 8)
ziffern = [nzahl(1, 9)]
ziffern.extend(([nzahl(0, 9) for step in range(anz_ziffern)]))
ziffern.append(nzahl(1, 9))
print(ziffern)
zahl = []
k = 1
ziffern.reverse()
for step in range(len(ziffern) - 2):
    zahl.append(ziffern[(step)])
    if k % 3 == 0 and k != len(ziffern) - 2:
        zahl.append(' ')
    k += 1
print(zahl)
print(ziffern)
zahl.extend((ziffern[-2:]))
zahl.insert(-2, '.')
aufg = ''
for zeichen in zahl:
    aufg = aufg + str(zeichen)
lsg = aufg + '~=~' + str(ziffern[0]) + '.'
for zeichen in ziffern:
    lsg = lsg + str(zeichen)
lsg = lsg + r' \cdot 10^{' + gzahl(len(ziffern)-3) + '}'
print(aufg)
print(lsg)

def min_float_to_str(zahl): # geklaut von Sirius3 im python-forum.de
    exponent = math.floor(math.log10(zahl))
    stellen = max(1,int(-exponent+15))
    return ('%.*f' % (stellen, zahl)).rstrip('0').rstrip('.')

print(min_float_to_str(Rational(1,12500000000000000000)))