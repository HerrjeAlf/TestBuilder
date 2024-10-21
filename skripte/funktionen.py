import math
import random
import time
import numpy as np
import string
from sympy import *
from pylatex import Document, Package

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

# Funktionen zur Darstellung von Zahlen

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
            if div == 0:
                zahl += '.'
            else:
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
    if k < 0:
        return '-'
    else:
        return '+'

def vorz_aussen(k, null=False):
    if k == 0:
        return '+0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k < 0:
        return '-'
    else:
        return ''

# Vorzeichen und Faktoren in Gleichungen oder Vektoren
def vorz_fakt(k):
    if k < 0:
        return -1
    else:
        return 1

def vorz_str(k, null=False):
    if k == 0:
        return '+0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

# Darstellung der Faktoren bzw. Vorzeichen neu
def vorz_v_innen(k,v, null=False):
    if k == 0:
        return '0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k == -1:
        return '-' + v
    if k == 1:
        return '+' + v
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k) + v
    else:
        return f'+{latex(k)}' + v

def vorz_v_aussen(k,v, null=False):
    if k == 0:
        return '0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k == -1:
        return '-' + v
    if k == 1:
        return v
    if k%1 == 0:
        k = int(k)
    return latex(k) + v

def ganz(k):
    if k % 1 == 0:
        return int(k)
    else:
        return k

def gzahl(k, exp=False):
    if type(k) == str:
        return k
    if exp == True:
        if k == 1:
            return ''
    if k % 1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def gzahl_klammer(k,string=''):
    if k % 1 == 0:
        k = int(k)
    if k < 0:
        return r' \left(' + latex(k) + string + r' \right)'
    else:
        return latex(k) + string

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
def punkt_vektor(p):
    return np.array([zzahl(1,p), zzahl(1,p), zzahl(1,p)])

def vektor_runden(vec,p):
    return [N(elements,p) for elements in vec]

def vektor_ganzzahl(vec):
    return np.array([int(element) if element % 1 == 0 else element for element in vec])

def vektor_kürzen(vec, p = 50):
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
    # print('erweitert: ' + str(list))
    teiler = [x + 1 for x in range(int(max(list)/2),-1,-1)]
    for zahl in teiler:
        treffer = [1 for x in list if x % zahl == 0]
        if sum(treffer) == len(vec):
            list = list / zahl
    # print('gekürzt: ' + str(list))
    list = np.array([int(element) if element % 1 == 0 else element for element in list])
    return np.array(list)

def vektor_kollinear(vec1, vec2):
    i = 0
    lsg = []
    for element in vec1:
        lsg.append(element / vec2[i])
        i += 1
    # print(lsg)
    for element in lsg:
        # print(element / lsg[0])
        if element / lsg[0] != 1:
            return False
    return True

def vektor_senk(vec1, vec2):
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

def exponenten(n):
    menge = set()  # ich habe hier eine Menge verwendet, weil diese keine gleichen Elemente enthält
    while len(menge) < n:
        menge.add(nzahl(2, 6 + n))
    return menge

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

def ganzz_exponenten(n,p=1,q=6, wdh=True):
    if wdh == True:
        liste = []
        while len(liste) < n:
            liste.append(zzahl(p,q))
        return liste
    elif wdh == False:
        menge = set()  # ich habe hier eine Menge verwendet, weil diese keine gleichen Elemente enthält
        while len(menge) < n:
            menge.add(zzahl(p, q))
        return menge
    else:
        print('wdh muss "True" or "False" sein')

def random_selection(list, anzahl=2, wdh=True):
    if wdh == True:
        liste = []
        random.shuffle(list)
        for k in range(anzahl):
            liste.append(list[k % len(list)])
        random.shuffle(liste)
        return liste
    elif wdh == False:
        if anzahl > len(set(list)):
            anzahl = len(set(list))
        menge = set()  # ich habe hier eine Menge verwendet, weil diese keine gleichen Elemente enthält
        while len(menge) < anzahl:
            menge.add(random.choice(list))
        return menge
    else:
        print('wdh muss "True" or "False" sein')

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
    k = 0
    for tuble in liste:
        if vektor_vergleich(tuble, vec) == True:
            return k
        else:
            k+=1
    return print('Element nicht in Liste')



