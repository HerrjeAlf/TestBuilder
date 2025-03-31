import math
import random
import time
import numpy as np
import string
from fractions import Fraction
from sympy import *
from pylatex import Document, Package,  Tabular, NoEscape, math

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)
# Timer Funktion
def timer(func):
    """
    Timer-Dekorator zur Messung der Ausführungszeit einer Funktion.
    """
    def wrapper(*args, **kwargs):  # Erklärung eines Dekorators -> https://t1p.de/lqn4d
        start_time = time.perf_counter()  # Zeit vorm ausführen nehmen
        result = func(*args, **kwargs)  # Aufruf der eigentlichen Funktion mit ihren Argumenten
        end_time = time.perf_counter()  # Zeit nachm ausführen
        execution_time = end_time - start_time  # Vergangene Zeit berechnen

        print(f'\033[38;2;0;220;120m\033[1m"{func.__name__}" wurde in {round(execution_time, 3)} Sekunden ausgeführt\033[0m')
        return result
    return wrapper

def packages(doc: Document):
    """
    Fügt unsere benutzten Pakete an jeweiliges Dokument an.
    """
    packages_lst = ['amsfonts', 'bm', 'textcomp']

    for package in packages_lst:
        doc.packages.append(Package(package))

def ganze_zahl(zahl):
    # überprüft ob die gegebene Zahl eine ganze Zahl ist
    try:
        int(abs(zahl))  # positive und negative Int-Werte
        return True
    except ValueError:
        return print('Sie haben keine ganze Zahl angegeben!')

def gzahl(k, exp=False, null=True):
    if k == 0 and exp==False:
        return '0' if null == True else ''
    if type(k) == str:
        return k
    if exp == True:
        if k == 1:
            return ''
        else:
            return '^' + latex(k)
    return latex(int(k)) if k % 1 == 0 else latex(k)

def gzahl_klammer(k, str='', null=True, eins=False):
    try:
        if k == 0 and null != True:
            return ''
        k = int(k) if k % 1 == 0 else k
        if k < 0:
            if str != '' and k == -1 and eins == False:
                return r' \left( -' + str + r' \right)'
            return r' \left(' + latex(k) + str + r' \right)'
        else:
            if str != '' and k == 1 and eins == False:
                return str
            return latex(k) + str
    except Exception as fehler:
        print('Fehler:', fehler)

# Funktionen zur Darstellung von Zahlen
def darstellung_zahl(zahl, exponent=None, darstellung='wiss'):
    # schreibt Zahlen in wissenschaftlicher Schreibweise oder als Dezimalbruch
    def liste(zahl):
        if exponent and ganze_zahl(exponent)==True:
            exp = exponent
            zahl_str = str(zahl)
            zahl_str.rstrip('0.').lstrip('0.')
            ziffern = [ziffer for ziffer in zahl_str]
            ziffern.remove('.') if '.' in ziffern else ziffern
        else:
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
                zahl = list[0][zp] + '.' + list[0][zp + 1] + list[0][zp + 2] + '~'
            else:
                zahl = zahl + list[0][zp] + list[0][zp + 1] + list[0][zp + 2]
                if k < div - 1:
                    zahl += '~'
                elif rest != 0:
                    zahl += '~'
            zp += 3
        if div == 0 and rest == 2:
            zahl = zahl + list[0][zp] + '.' + list[0][zp + 1]
        else:
            for k in range(rest):
                zahl = zahl + list[0][zp + k]
        zahl = zahl + r' \cdot 10^{' + gzahl(list[1]) + '}'

    elif darstellung == 'dezi':
        laenge = len(list[0])
        exp = list[1]
        if exp < 0:
            for step in range(abs(exp)):
                list[0].insert(0, '0')
            zp = 0
            div, rest = divmod(len(list[0]), 3)
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
            for step in range(exp + 1):
                if step >= laenge:
                    list[0].append('0')
            div, rest = divmod(len(list[0]), 3)
            zahl = ''
            for k in range(rest):
                zahl = zahl + list[0][k]
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
            new_list = [[list[0][k] for k in range(abs(exp) + 1)], [list[0][k] for k in range(laenge) if k > abs(exp)],
                        exp]
            zahl = ''
            # Ziffern vorm Komma
            div, rest = divmod(len(new_list[0]), 3)
            for k in range(rest):
                zahl = zahl + new_list[0][k]
            if div != 0:
               zahl += '~'
            zp = rest
            for k in range(div):
                zahl = zahl + new_list[0][zp] + new_list[0][zp + 1] + new_list[0][zp + 2]
                if k < div - 1:
                    zahl += '~'
                zp += 3
            zahl = zahl + '.' if len(new_list[1]) > 0 else zahl
            # Ziffern hinter dem Komma
            if len(new_list[1]) < 3:
                for element in new_list[1]:
                    zahl += element
            else:
                zahl += new_list[1][0] + new_list[1][1]
                zahl += '~'
                zp = 2
                div, rest = divmod(len(new_list[1]) - 2, 3)
                for k in range(div):
                    zahl = zahl + new_list[1][zp] + new_list[1][zp + 1] + new_list[1][zp + 2]
                    if k < div - 1:
                        zahl += '~'
                    zp += 3
                for k in range(rest):
                    zahl = zahl + list[0][zp + k]

    return zahl

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def vorz(k):
    return '-' if k < 0 else '+'

def vorz_aussen(k, null=False):
    if k == 0:
        return '0' if null == True else ''
    return '-' if k < 0 else ''

# Vorzeichen und Faktoren in Gleichungen oder Vektoren

def vorz_str(k, null=False):
    try:
        if k == 0 and null == False:
            return ''
        if k % 1 == 0:
            k = int(k)
        return latex(k) if k < 0 else f'+{latex(k)}'
    except Exception as fehler:
        print('Fehler:', fehler)

# Darstellung der Faktoren bzw. Vorzeichen neu
def vorz_v_innen(zahl,string, null=False):
    try:
        if zahl == 0:
            return '0' if null == True else ''
        if zahl == -1:
            return '-1' if string == '' else '-' + string
        if zahl == 1:
            return '+1' if string == '' else '+' + string
        if zahl%1 == 0:
            zahl = int(zahl)
        return latex(zahl) + string if zahl < 0 else f'+{latex(zahl)}' + string
    except Exception as fehler:
        print('Fehler:', fehler)

def vorz_v_aussen(zahl,string, null=False):
    try:
        if zahl == 0:
            return '0' if null == True else ''
        if zahl == -1:
            return '-1' if string == '' else '-' + string
        if zahl == 1:
            return '1' if string == '' else string
        if zahl%1 == 0:
            zahl = int(zahl)
        return latex(zahl) + string
    except Exception as fehler:
        print('Fehler:', fehler)

def potenz(fakt, exp, bas='x', vorz=False):
    if exp == 1:
        return gzahl(fakt) + str(bas)
    elif exp == 0:
        return vorz_str(fakt) if vorz else gzahl(fakt)
    else:
        return vorz_str(fakt) + str(bas) + '^' + gzahl(exp) if vorz else gzahl(fakt) + str(bas) + '^' + gzahl(exp)

def binom(z1, z2, str1='', str2=''):
    if z1 != 0 and z2 != 0:
        if z1 < 0 and z2 < 0:
            return (r'- \left( ' + vorz_v_aussen(abs(z1), str(str1))
                    + vorz_v_innen(abs(z2), str(str2)) + r' \right) ')
        elif z1 < 0:
            return vorz_v_aussen(z2, str(str2)) + vorz_v_innen(z1, str(str1))
        elif z2 < 0:
            return vorz_v_aussen(z1, str(str1)) + vorz_v_innen(z2, str(str2))
        else:
            return vorz_v_aussen(z1,str(str1)) + vorz_v_innen(z2,str(str2))
    else:
        return vorz_v_aussen(z1,str(str1)) + vorz_v_aussen(z2, str(str2))

def binom_klammer(z1, z2, str1='', str2=''):
    if z1 != 0 and z2 != 0:
            return r' \left(' + vorz_v_aussen(z1, str(str1)) + vorz_v_innen(z2, str(str2)) + r' \right) '
    else:
        return gzahl_klammer(z1,str(str1), null=False) + gzahl_klammer(z2, str(str2), null=False)


def binom_aussen(z1, z2, str1='', str2='', var=''):
    if z1 != 0 and z2 != 0:
        if z1 < 0 and z2 < 0:
            return (r'- \left( ' + vorz_v_aussen(abs(z1), str(str1))
                    + vorz_v_innen(abs(z2), str(str2)) + r' \right) ' + str(var))
        elif z1 < 0:
            return (r' \left( ' + vorz_v_aussen(z2, str(str2))
                    + vorz_v_innen(z1, str(str1)) + r' \right) ' + str(var))
        elif z2 < 0:
            return (r' \left( ' + vorz_v_aussen(z1, str(str1))
                    + vorz_v_innen(z2, str(str2)) + r' \right) ' + str(var))
        else:
            return (r' \left( ' + vorz_v_aussen(z1,str(str1))
                    + vorz_v_innen(z2,str(str2)) + r' \right) ' + str(var))
    else:
        return vorz_v_aussen(z1,str(str1 + var)) + vorz_v_aussen(z2, str(str2 + var))

def binom_innen(z1, z2, str1='', str2='', var=''):
    if z1 != 0 and z2 != 0:
        if z1 < 0 and z2 < 0:
            return (r'- \left( ' + vorz_v_aussen(abs(z1), str(str1))
                    + vorz_v_innen(abs(z2), str(str2)) + r' \right) ' + str(var))
        elif z1 < 0:
            return (r' + \left( ' + vorz_v_aussen(z2, str(str2))
                    + vorz_v_innen(z1, str(str1)) + r' \right) ' + str(var))
        elif z2 < 0:
            return (r' + \left( ' + vorz_v_aussen(z1, str(str1))
                    + vorz_v_innen(z2, str(str2)) + r' \right) ' + str(var))
        else:
            return (r' + \left( ' + vorz_v_aussen(z1,str(str1))
                    + vorz_v_innen(z2,str(str2)) + r' \right) ' + str(var))
    else:
        return vorz_v_innen(z1,str(str1 + var)) + vorz_v_innen(z2, str(str2 + var))

def fakt_var(k):
    if k == 1:
        return ''
    else:
        return latex(k)

def summe_exp(list_term, exp, list_var=[]):
    list_exp = [exp for n in range(len(list_term))] if type(exp) != list else exp
    if len(list_term) != len(list_exp):
        exit('Fehler bei der Funktion "summe_potenz" in funktionen.py - die verwendeten Listen sind verschieden lang!')
    list_exp = ['^' + gzahl(exp) if exp != 1 else '' for exp in list_exp]
    for n in range(len(list_term)):
        if list_term[n] != 0:
            if list_var != []:
                summe_str = r' \left( ' + gzahl(list_term[n]) + str(list_var[n]) + r' \right) ' + list_exp[n]
                del list_var[n]
            else:
                summe_str = gzahl_klammer(list_term[n]) + list_exp[n]
            del list_term[n]
            del list_exp[n]

            break
    for n in range(len(list_term)):
        if list_term[n] != 0:
            if list_var != []:
                summe_str = (summe_str + r'+ \left( ' + gzahl(list_term[n]) + str(list_var[n])
                             + r' \right) ' + list_exp[n])
            else:
                summe_str = summe_str + '+' + gzahl_klammer(list_term[n]) + list_exp[n]
    return summe_str

def exponenten(n,p=1,q=6, wdh=True, ganzz=False):
    if wdh != True:
        if ganzz == True:
            liste = list(range(-1*(q+n), q + n))
            random.shuffle(liste)
            liste = liste[0:n]
        else:
            liste = list(range(p, q + n))
            random.shuffle(liste)
            liste = liste[0:n]
    else:
        liste = [zzahl(p,q) for _ in range(n)] if ganzz == True else [nzahl(p,q) for _ in range(n)]
    return liste

def kgv(q, p):
    if q == 0 or p == 0:
        return 0
    if q == p:
        return p
    if q > p:
        max = q
        min = p
    else:
        max = p
        min = q
    quotient = max/min
    if quotient % 1 == 0:
        return int(max)
    for zahl in range(1,max):
        if (zahl * min) % max == 0:
            return int(zahl*min)
    return max*min

# Funktionen zur Optimierung von Ergebnissen mit True and False als Ausgabe
def vektor_rational(vec,p,q=1000):
    vec_p = [element*p for element in vec]
    print(vec_p)
    k = 0
    i = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
        if int(k/q) == 0:
            i += 1
    if k == len(vec) and i == len(vec):
        return True
    else:
        return False

# Funktionen zur linearen Algebra
def punkt_vektor(p,n=3):
    return np.array([zzahl(1,p) for _ in range(n)])

def vektor_runden(vec,p):
    return [N(elements,p) for elements in vec]

def vektor_ganzzahl(vec):
    return np.array([int(element) if element % 1 == 0 else element for element in vec])

def vektor_kuerzen(vec, p = 50, qout=False):
    # print('wird an Vektor kürzen übergeben: ' + str(vec))
    faktor = [x + 1 for x in range(p)]
    list = np.array(vec)
    i = 0
    for element in vec:
        k = 0
        if list[i] % 1 == 0:
            i += 1
        else:
            while (list[i] * faktor[k]) % 1 != 0 and k+1 < p:
                k += 1
            list = list * faktor[k]
            i += 1
    # print('Liste mit erweiterten Faktoren: ' + str(list)), print('erweitert: ' + str(list))
    list_pos = [abs(x) for x in list]
    # print('Liste mit positiven Elementen:' + str(list_pos))
    teiler = [x+1 for x in range(int(max(list_pos)))]
    teiler.reverse()
    # print('Liste der möglichen Teiler: ' + str(teiler))
    for zahl in teiler:
        treffer = [1 for x in list if abs(x) % zahl == 0]
        if sum(treffer) == len(vec):
            list = [element / zahl for element in list]
    # print('Liste nach Division mit möglichen Teilern: ' + str(list))
    if len([element for element in list if element < 0]) == len(list):
        list = [-1 * element for element in list]
    # print('gekürzt: ' + str(list))
    list = np.array([int(element) if element % 1 == 0 else element for element in list])
    faktor = [Rational(vec[i],list[i]) for i in range(len(list)) if list[i] !=0 and vec[i] != 0]
    if qout == False:
        return np.array(list)
    else:
        return np.array(list), faktor[0]

def vektor_kollinear(vec1, vec2):
    i = 0
    lsg = []
    for i in range(len(vec1)):
        if vec2[i] == 0:
            if vec1[i] == 0:
                pass
            else:
                return False
        else:
            lsg.append(vec1[i] / vec2[i])
    # print(lsg)
    for element in lsg:
        # print(element / lsg[0])
        if element / lsg[0] != 1:
            return False
    return True

def test_vektor_senk(vec1, vec2):
    lsg = [vec1[k] * vec2[k] for k in range(len(vec1))]
    if sum(lsg) != 0:
        return False
    return True

def vektor_max(vec, p):
    vec_p = [element / p for element in vec]
    k = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
    if k == len(vec):
        return True
    else:
        return False

def vektor_vergleich(vec1, vec2):
    if len(vec1) != len(vec2):
        return print('Vektoren verschieden lang.')
    i = 0
    for element in vec1:
        if vec1[i] == vec2[i]:
            i += 1
        else:
            return False
    return True

def skalarprodukt(vec1, vec2):
    if len(vec1) != len(vec2):
        exit('Die Vektoren müssen die gleiche Dimension haben (gleiche Anzahl an Koordinaten)!')
    return sum([x * y for x, y in zip(vec1, vec2)])

# Wahrscheinlichkeitsrechnung
def darstellung_mengen(lsg_menge):
    # korrekte Darstellung der Lösungsmenge
    lsg = '{ '
    m = 1
    for tubel in lsg_menge:
        n = 1
        lsg = lsg + '('
        for element in tubel:
            lsg = lsg + str(element)
            if n < len(tubel):
                lsg = lsg + ','
            n += 1
        lsg = lsg + ')'
        if m < len(lsg_menge):
            lsg = lsg + '; '
        m += 1
    lsg = lsg + ' }'
    return lsg

def ergebnisraum_zmZ(anzahl_ziehen, farbe1='weiß', farbe2='schwarz'):
    omega = [[farbe1 for element in range(anzahl_ziehen)]]
    for anzahl in omega:
        i = 0
        for stelle in anzahl:
            tubel = anzahl.copy()
            tubel[i] = farbe2
            for element in omega:
                if tubel not in omega:
                    omega.append(tubel)
            i += 1
    return omega

def ergebnisraum_zoZ(az, anz_1, anz_2, farbe1='weiß', farbe2='schwarz'):
    anz_ges = anz_1 + anz_2
    if az > anz_ges:
        az = anz_ges
    omega1 = [[farbe1 for element in range(az)]]
    if az > anz_1:
        omega = []
    else:
        omega = [[farbe1 for element in range(az)]]
    for anzahl in omega1:
        i = 0
        for stelle in anzahl:
            tubel = anzahl.copy()
            tubel[i] = farbe2
            for element in omega1:
                if tubel not in omega1:
                    omega1.append(tubel)
                    if tubel.count(farbe2) <= anz_2 and tubel.count(farbe1) <= anz_1:
                        omega.append(tubel)
            i += 1
    return omega

def wkt_baumdiagramm(menge_aufg, bez1='A', bez2='B', anz1=10, anz2=10, art='zmZ'):
    obermenge = []
    menge = []
    for element in menge_aufg:
        element_neu = []
        for tubel in element:
            if tubel == bez1:
                element_neu.append(bez1)
            else:
                pass
        while len(element) > len(element_neu):
            element_neu.append(bez2)
        menge.append(element_neu)
    for element in menge:
        teilmenge = []
        while element in menge:
            teilmenge.append(element)
            menge.remove(element)
        obermenge.append(teilmenge)
        if len(menge) == 1:
            obermenge.append([menge[-1]])
    wkt = ''
    ergebnis = 0
    for elements in obermenge:
        if elements == obermenge[0] and len(elements) == 1:
            pass
        elif len(elements) == 1 and not elements == obermenge[0]:
            wkt = wkt + '+'
        elif elements == obermenge[0] and len(elements) > 1:
            wkt = wkt + latex(len(elements)) + r' \cdot '
        else:
            wkt = wkt + vorz_str(len(elements)) + r' \cdot '
        i = 1
        zaehler = ''
        nenner = ''
        erg_zaehler = 1
        erg_nenner = 1
        a1 = anz1
        a2 = anz2
        for string in elements[0]:
            # print(string)
            # print(a1)
            if i == len(elements[0]):
                if string == bez1:
                    zaehler = zaehler + gzahl(a1)
                    erg_zaehler = erg_zaehler * a1
                else:
                    zaehler = zaehler + gzahl(a2)
                    erg_zaehler = erg_zaehler * a2
                nenner = nenner + gzahl(a1 + a2)
                erg_nenner = erg_nenner * (a1+a2)
                break
            elif string == bez1:
                zaehler = zaehler + gzahl(a1) + r' \cdot '
                nenner = nenner + gzahl(a1 + a2) + r' \cdot '
                erg_zaehler = erg_zaehler * a1
                erg_nenner = erg_nenner * (a1+a2)
                if art == 'zoZ':
                    a1 -= 1
            else:
                zaehler = zaehler + gzahl(a2) + (r' \cdot ')
                nenner = nenner + gzahl(a1 + a2) + r' \cdot '
                erg_zaehler = erg_zaehler * a2
                erg_nenner = erg_nenner * (a1+a2)
                if art == 'zoZ':
                    a2 -= 1
            i += 1
        wkt = wkt + r' \frac{' + zaehler + '}{' + nenner + '}'
        # print(erg_zaehler)
        # print(erg_nenner)
        ergebnis = ergebnis + len(elements)*Rational(erg_zaehler,erg_nenner)
        # print(ergebnis)
    punkte = len(obermenge) + 1
    wkt_erg = ergebnis
    wkt_str = wkt + '~=~' + latex(N(ergebnis*100,3)) + r' \% '
    if len(obermenge) == 0:
        wkt_str = r'0 \% \quad (1P)'
    return wkt_erg, wkt_str, punkte

# Funktionen zur Analysis
def faktorliste(n, p, q):
    return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

def elemente_sort(st_werte):
    t = 0
    st_werte_sort = []
    for element in st_werte:
        k = 0
        while k < len(st_werte):
            if element >= st_werte[k]:
                st_werte_sort.insert(k, t)
                k = len(st_werte)
            else:
                k += 1
        t += 1
    return st_werte_sort

def random_selection(list, anzahl=2, wdh=True):
    if wdh == True:
        liste = []
        random.shuffle(list)
        for k in range(anzahl):
            liste.append(list[k % len(list)])
        random.shuffle(liste)
        return liste
    elif wdh == False:
        if anzahl > len(list):
            anzahl = len(list)
        random.shuffle(list)
        Liste = [list[k] for k in range(anzahl)]
        return Liste
    else:
        print('wdh muss "True" or "False" sein')

def repeat(list, anzahl=2):
    new_list = []
    for element in list:
        new_list.extend([element for _ in range(anzahl)])
    return new_list

def polynom(p):  # erzeugt eine Funktion und deren Ableitungen mit p Summanden und maximal p-Grades
    fkt = random.choice([zzahl(1, 10), 0])
    koeffizienten = faktorliste(1, 15, p)
    potenzen = exponenten(p)

    for koeffizient in koeffizienten:
        fkt = koeffizient * (x ** potenzen.pop()) + fkt
        fkt = collect(fkt, x)
    fkt_abl_1 = collect(expand(diff(fkt, x)), x)
    fkt_abl_2 = collect(expand(diff(fkt, x, 2)), x)

    return fkt, fkt_abl_1, fkt_abl_2

# keine Ahnung wo ich das noch brauche

def stelle(liste, vec):
    # hier wird die Stelle eines gesuchten Elements in der Liste ausgegeben
    k = 0
    for tuble in liste:
        if vektor_vergleich(tuble, vec) == True:
            return k
        else:
            k+=1
    return print('Element nicht in Liste')

# in Entwicklung:
def gaussalgorithmus(gleichungen, variablen=[]):
    """
    Löst ein lineares Gleichungssystem mit der Methode der Gaußschen Elimination.

    :param koeffizienten: Liste der Koeffizienten (Matrix A).
    :param ergebnisse: Liste der Ergebnisse (Vektor b).
    :return: Liste der Lösungen oder eine Beschreibung der Schritte.
    """
    beschrift = {1:'I',2: 'II',3: 'III',4: 'IV',5: 'V',6: 'VI',7: 'VII',8: 'VIII',9: 'IX',10: 'X'}
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

    loesung = [[beschrift.get(k+1, 'zu groß'), ''] + gleichungen[k] for k in range(n)]
    print(gleichungen)
    print(loesung)

    for i in range(n):
        for k in range(i+1, n):
            if gleichungen[k][i] != 0:
                text = (gzahl(gleichungen[k][i]) + r' \cdot ' + beschrift.get(i+1, 'zu groß')
                        + vorz_str(-1 * gleichungen[i][i]) + r' \cdot ' + beschrift.get(k+1, 'zu groß'))
                neue_zeile = [gleichungen[i][i] * gleichungen[k][step] - gleichungen[k][i] * gleichungen[i][step]
                              for step in range(0, len(gleichungen[0]))]
                gleichungen[k] = neue_zeile
                loesung.append([beschrift.get(k+1, 'zu groß'), text] + neue_zeile)

    print(loesung)
    k = beschrift_reverse[loesung[-1][0]]
    gleich_lsg = []
    for anz in reversed(list(range(k))):
        for eintrag in reversed(loesung):  # Liste von hinten durchgehen
            if eintrag[0] == beschrift[anz+1]:
                gleich_lsg.append(eintrag) # Letztes Element zurückgeben
                break

    print(gleich_lsg)

    # und hier eine Funktion die aus gleich_lsg den Lösungstext erstellt "aus III folgte c = ..."


    # noch eine Funktion, die loesung als Tabelle darstellt
    anz_sp = len(loesung[0])
    spalten = 'c|'
    for step in range(anz_sp):
        spalten += 'c|'
    table1 = Tabular(spalten, row_height=1.2)
    table1.add_hline(2)
    table1.add_row(['Berechnung mit dem Gauß-Algorithmus',' Nr','Berechnung'] + variablen + ['Lsg'])
    table1.add_hline(2)
    for zeile in loesung:
        liste = [''] + [NoEscape('$' + str(element) + '$')  for element in zeile]
        table1.add_row(liste)
        table1.add_hline(2)
    print(table1)


    print(loesung)
    return loesung, table1

def quadr_gl(koeff, i=1):
    n1, n2, n3 = list(range(i,i+3))
    punkte = 0
    if all(x == 0 for x in koeff):
        text = r'0 ~=~ 0 ~ w.A. \mathrm{für~alle~x~aus~dem~Definitionsbereich} '
        lsg = [r' \mathbb{R} ']
        punkte += 1
    elif koeff[0] == 0:
        if koeff[1] == 0:
            text = r'0 ~=~ ' + gzahl(koeff[2]) + ' ~ f.A. '
            lsg = []
            punkte += 1
        elif koeff[2] == 0:
            text = r' 0 ~=~ ' + vorz_v_aussen(koeff[1], 'x') + r' \quad \to \quad x_{' + gzahl(n1) + '} ~=~ 0'
            lsg = [0]
            punkte += 2
        else:
            lsg1 = Fraction(-1 * koeff[2], koeff[1])
            text = (r' 0 ~=~ ' + vorz_v_aussen(koeff[1], 'x') + vorz_str(koeff[2]) + r' \quad \vert '
                    + vorz_str(-1 * koeff[2]) + r' \quad \vert \div ' + gzahl_klammer(koeff[1])
                    + r' \quad \to \quad x ~=~' + gzahl(lsg1) + r' \\')
            lsg = [lsg1]
            punkte += 2
    elif koeff[1] == 0 and koeff[2] == 0:
        text = r' 0 ~=~ ' + vorz_v_aussen(koeff[0], 'x^2') +  r' \quad \to \quad x_{' + gzahl(n1) + '} ~=~ 0'
        lsg = [0]
        punkte += 2
    elif koeff[2] == 0:
        text = (r' 0 ~=~ ' + vorz_v_aussen(koeff[0], 'x^2') + vorz_v_innen(koeff[1],'x')
                + r' ~=~ x \cdot \left( ' + vorz_v_aussen(koeff[0], 'x') + vorz_str(koeff[1]) + r' \right) '
                + r' \quad \to \quad x_{' + gzahl(n1) + r'} = 0 \\ 0 ~=~ ' + vorz_v_aussen(koeff[0], 'x')
                + vorz_str(koeff[1]) + r' \quad \vert ' + vorz_str(-1*koeff[1]) + r' \quad \vert \div '
                + gzahl_klammer(koeff[0]) + r' \quad \to \quad x_{' + gzahl(n2) + '} ~=~ '
                + gzahl(Fraction(-1*koeff[1], koeff[0])) + '~=~' + gzahl(N(-1*koeff[1]/ koeff[0],3)))
        lsg = [0, Fraction(-1*koeff[1], koeff[0])]
        lsg.sort()
        punkte += 4
    elif koeff[1]==0:
        text = (r' 0 ~=~ ' + vorz_v_aussen(koeff[0], 'x^2') + vorz_str(koeff[2]) + r' \quad \vert '
                + vorz_str(-1*koeff[2]) + r' \quad \vert \div ' + gzahl_klammer(koeff[0]) + r' \quad \to \quad x^2 ~=~'
                + gzahl(Fraction(-1*koeff[2],koeff[0])) + r' \vert \sqrt{ ~ } \\')
        punkte += 2
        if Fraction(-1*koeff[2],koeff[0]) < 0:
            text = (text + r' x_{ ' + gzahl(n1) + ',' + gzahl(n2) + ' } ~=~ \pm \sqrt{ '
                    + gzahl(Fraction(-1*koeff[2],koeff[0])) + r' } \quad \mathrm{ n.d. }')
            lsg = []
            punkte += 2
        else:
            disk = Fraction(-1 * koeff[2], koeff[0])
            lsg_de = N(sqrt(-1 * koeff[2]/ koeff[0]),3)
            text = (text + r' x_{ ' + gzahl(n1) + ',' + gzahl(n2) + ' } ~=~ \pm \sqrt{ ' + gzahl(disk)
                    + r' } \quad \to \quad x_{ ' + gzahl(n1) + '} = \sqrt{ ' + gzahl(disk) + '~=~' + gzahl(lsg_de)
                    + r' } \quad \mathrm{und} \quad x_{ ' + gzahl(n2) + ' }= - \sqrt{ ' + gzahl(disk)
                    + r' } + ~=~' + gzahl(-1*lsg_de))
            lsg = [-1*lsg_de, lsg_de]
            punkte += 1
    else:
        p = Fraction(koeff[1], koeff[0])
        q = Fraction(koeff[2], koeff[0])
        text = (r' 0 ~=~ ' + vorz_v_aussen(koeff[0], 'x^2') + vorz_v_innen(koeff[1],'x')
                + vorz_str(koeff[2]) + r' \quad \vert \div ' + gzahl_klammer(koeff[0]) + r' \quad \to \quad '
                + r' 0 ~=~ x^2 ' + vorz_v_innen(Fraction(koeff[1], koeff[0]), 'x')
                + vorz_str(Fraction(koeff[2], koeff[0])) + r' \\'
                + r' x_{ ' + gzahl(n1) + ',' + gzahl(n2) + r' } ~=~ - \frac{' + gzahl(p) +  r'}{2} \pm \sqrt{ \left( '
                + r' \frac{' + gzahl(p) + '}{2} \left) ^2 ' + vorz_str(-1*q) + '} ~=~ '
                + gzahl(Fraction(-1*koeff[1],2*koeff[0])) + r' \pm \sqrt{ '
                + gzahl(Fraction(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2)) + r'} \\')
        punkte += 3
        if Fraction(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2) < 0:
            text = text + r' \mathrm{ n.d. }'
            lsg = []
            punkte += 1
        elif Fraction(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2) == 0:
            text = text + r' x_{' + gzahl(n1) + '} ~=~ ' + gzahl(Fraction(-1*koeff[1],2*koeff[0]))
            lsg = [Fraction(-1*koeff[1],2*koeff[0])]
            punkte += 2
        else:
            pass


        punkte += 4



    return text, lsg, punkte