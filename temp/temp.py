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
def terme_in_klammer(anz_terme, anz_var, fakt=True, exp=False, p=1, q=10):
    anz_var = anz_terme if anz_var > anz_terme else anz_var
    liste_exp = [1 for _ in range(anz_var)]
    liste_exp = exponenten(anz_var, wdh=True) if exp != False else liste_exp
    if fakt == False:
        liste_fakt = [1 for _ in range(anz_terme)]
    else:
        fakt = random.choice(['nat', 'ganz', 'rat', 'dez']) if fakt not in ['nat', 'ganz', 'rat', 'dez'] else fakt
        if fakt == 'nat':
            liste_fakt = [nzahl(p, q) for _ in range(anz_terme)]
        elif fakt == 'ganz':
            liste_fakt = [nzahl(p, q) for _ in range(anz_terme)]
        elif fakt == 'rat':
            liste_fakt = [Rational(zzahl(p, q), nzahl(p, q)) for _ in range(anz_terme)]
        else:
            liste_fakt = [zzahl(p, 10 * q) / 10 for _ in range(anz_terme)]

    liste_var = random_selection([1, a, b, c, d, e, f, g, h, x, y, z], anzahl=anz_var, wdh=False)
    terme = [[liste_fakt[k], liste_var[k % anz_var] ** liste_exp[k % anz_var]] for k in range(anz_terme)]
    return terme


def einf(anz_terme, anz_var, var_aus=False, fakt_aus='vorz', fakt_in=True, exp_aus=False, exp_in=False, p=1, q=10):
    terme = terme_in_klammer(anz_terme, anz_var, fakt_in, exp_in)
    #print(terme)
    fakt_aus = random.choice(['vorz', 'nat', 'ganz', 'rat', 'dez']) if fakt_aus not in ['vorz', 'nat', 'ganz', 'rat',
                                                                                        'dez'] else fakt_aus
    faktoren = {'vorz': random.choice([-1, 1]), 'nat': nzahl(1, 9), 'ganz': zzahl(1, 9),
                'rat': Rational(zzahl(p, q), nzahl(p, q)), 'dez': zzahl(1, 100) / 10}
    fakt = faktoren[fakt_aus]
    if var_aus == True:
        var_aus = random.choice([1, a, b, c, d, e, f, g, h, x, y, z])
    else:
        var_aus = 1
    if exp_aus == True:
        exp_aus = nzahl(p, q)
    else:
        exp_aus = 1
    #print(fakt)
    #print(var_aus)
    #print(exp_aus)
    #print(anz_terme)
    ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]] for k in range(anz_terme)]
    #print(ausmulti_terme)
    kopie_terme = ausmulti_terme.copy()
    print(kopie_terme)
    gleiche_terme = []
    while len(kopie_terme) != 0:
        gleichartiger_term = []
        for element in kopie_terme:
            var = element[1]
            print(element)
            for element1 in kopie_terme:
                if element1[1] == var:
                    gleichartiger_term.append(element1)
                    kopie_terme.remove(element1)
                    print(element1)
            print(gleichartiger_term)
        gleiche_terme.append(gleichartiger_term)
        # print(gleiche_terme)
    terme_erg = []
    print(gleiche_terme)
    for element in gleiche_terme:
        zahl = 0
        for k in range(len(element)):
            zahl += element[k][0]
        terme_erg.append([zahl, element[0][1]])
    print(terme_erg)
    return ausmulti_terme, terme_erg

einf(3, 3, fakt_aus='rat', fakt_in='rat')