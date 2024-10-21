import random, math

from sympy import *
from decimal import *
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

# def schreibweise(zahl, darstellung='wiss'):

def darstellung_zahl(zahl, darstellung='wiss'):
    def liste(zahl):
        exp = math.floor(math.log10(zahl))
        if zahl < 1:
            zahl_str = ('%.*f' % (int(-exp + 15), zahl)).rstrip('0.').lstrip('0.')
            ziffern = [ziffer for ziffer in zahl_str]
            ziffern.remove('.') if '.' in ziffern else ziffern
        else:
            zahl_str = str(zahl).rstrip('0.').lstrip('0.')
            ziffern = [ziffer for ziffer in zahl_str]
            ziffern.remove('.') if '.' in ziffern else ziffern
        return [ziffern, exp]

    list = liste(zahl)
    darstellung = 'wiss' if darstellung not in ['wiss', 'dezi'] else darstellung

    if darstellung == 'wiss':
        zahl = ''
        laenge = len(list[0])
        div, rest = divmod(abs(laenge), 3)
        zp = 0
        for k in range(div):
            if k == 0:
                zahl = list[0][zp] + '.' + list[0][zp+1] + list[0][zp+2] + '~'
            else:
                zahl = zahl + list[0][zp] + list[0][zp+1] + list[0][zp+2]
                if k < div-1:
                    zahl += '~'
                elif rest != 0:
                    zahl += '~'
            zp += 3
        for k in range(rest):
            zahl = zahl + list[0][zp+k]
        zahl = zahl + r' \cdot 10^{' + gzahl(list[1]) + '}'
    
    elif darstellung == 'dezi':
        laenge = len(list[0])
        exp = list[1]
        print(laenge)
        print(exp)
        if exp < 0:
            for step in range(abs(exp)):
                list[0].insert(0,'0')
            zp = 0
            div, rest = divmod(len(list[0]), 3)
            print(div)
            print(rest)
            for k in range(div):
                if k == 0:
                    zahl = list[0][zp] + '.' + list[0][zp + 1] + list[0][zp + 2] + '~'
                else:
                    zahl = zahl + list[0][zp] + list[0][zp + 1] + list[0][zp + 2]
                    if k < div - 1:
                        zahl += '~'
                    elif rest != 0:
                        zahl += '~'
                zp += 3
            for k in range(rest):
                zahl = zahl + list[0][zp + k]

        elif exp > 0 and exp >= laenge:
            print(list)
            for step in range(exp+1):
                if step >= laenge:
                    list[0].append('0')
            print(list[0])
            div, rest = divmod(len(list[0]), 3)
            print(div)
            print(rest)
            zahl = ''
            for k in range(rest):
                zahl = zahl + list[0][k]
            print(zahl)
            if div != 0:
                zahl += '~'
            zp = rest
            for k in range(div):
                if k == 0:
                    zahl = zahl + list[0][zp] + list[0][zp + 1] + list[0][zp + 2] + '~'
                else:
                    zahl = zahl + list[0][zp] + list[0][zp + 1] + list[0][zp + 2]
                    if k < div - 1:
                        zahl += '~'
                zp += 3

        elif abs(exp) <= laenge:
            new_list = [[list[0][k] for k in range(abs(exp)+1)], [list[0][k] for k in range(laenge) if k > abs(exp)], exp]
            zahl = ''
            # Ziffern vorm Komma
            div, rest = divmod(len(new_list[0]), 3)
            for k in range(rest):
                zahl = zahl + new_list[0][k]
            zahl += '~'
            zp = rest
            for k in range(div):
                zahl = zahl + new_list[0][zp] + new_list[0][zp + 1] + new_list[0][zp + 2]
                if k < div - 1:
                    zahl += '~'
                zp += 3
            zahl = zahl + '.'
            # Ziffern hinter dem Komma
            if len(new_list[1]) < 3:
                for element in new_list[1]:
                    zahl += element
            else:
                zahl += new_list[1][0] + new_list[1][1]
                zahl += '~'
                zp = 2
                div, rest = divmod(len(new_list[1])-2,3)
                print(new_list[1])
                print(div)
                print(rest)
                for k in range(div):
                    zahl = zahl + new_list[1][zp] + new_list[1][zp + 1] + new_list[1][zp + 2]
                    if k < div - 1:
                        zahl += '~'
                    zp += 3
                for k in range(rest):
                    zahl = zahl + list[0][zp + k]

    return zahl

zahl = darstellung_zahl(4323.423274* 10**3, darstellung='dezi')
print(zahl)



