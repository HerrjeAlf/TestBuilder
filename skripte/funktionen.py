import math
import random
import time
import numpy as np
import string
from sympy import *
from pylatex import Document, Package,  Tabular, NoEscape

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)
zeilennummer = {1:'I',2: 'II',3: 'III',4: 'IV',5: 'V',6: 'VI',7: 'VII',8: 'VIII',9: 'IX',10: 'X'}
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

# darstellung von Termen in latex

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

def gzahl_klammer(k, string='', null=True, eins=False):
    try:
        if k == 0 and null != True:
            return ''
        k = int(k) if k % 1 == 0 else k
        if k < 0:
            if string != '' and k == -1 and eins == False:
                return r' \left( -' + str(string) + r' \right)'
            return r' \left(' + latex(k) + str(string) + r' \right)'
        else:
            if string != '' and k == 1 and eins == False:
                return str(string)
            return latex(k) + str(string)
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

# Vorzeichen und Faktoren in Gleichungen oder Vektoren
def vorz(k):
    return '-' if k < 0 else '+'

def vorz_aussen(k, null=False):
    if k == 0:
        return '0' if null == True else ''
    return '-' if k < 0 else ''

def vorz_str(k, null=False):
    try:
        if k == 0 and null == False:
            return ''
        if k % 1 == 0:
            k = int(k)
        return latex(k) if k < 0 else f'+{latex(k)}'
    except Exception as fehler:
        print('Fehler:', fehler)

def vorz_v_innen(zahl, string, null=False):
    try:
        if zahl == 0:
            return '0' if null == True else ''
        if zahl == -1:
            return '-1' if string == '' else '-' + string
        if zahl == 1:
            return '+1' if string == '' else '+' + string
        if zahl % 1 == 0:
            zahl = int(zahl)
        return latex(zahl) + string if zahl < 0 else f'+{latex(zahl)}' + string
    except Exception as fehler:
        print('Fehler:', fehler)

def vorz_v_aussen(zahl, string, null=False):
    try:
        if zahl == 0:
            return '0' if null == True else ''
        if zahl == -1:
            return '-1' if string == '' else '-' + string
        if zahl == 1:
            return '1' if string == '' else string
        if zahl % 1 == 0:
            zahl = int(zahl)
        return latex(zahl) + string
    except Exception as fehler:
        print('Fehler:', fehler)

# Darstellung der Faktoren bzw. Vorzeichen neu
def potenz(fakt, exp, bas='x', vrz=[False,True][0]):
    if exp == 1:
        return vorz_str(fakt) + str(bas) if vrz else gzahl(fakt) + str(bas)
    elif exp == 0:
        return vorz_str(fakt) if vrz else gzahl(fakt)
    else:
        return vorz_str(fakt) + str(bas) + '^' + gzahl(exp) if vrz else gzahl(fakt) + str(bas) + '^' + gzahl(exp)

def binom_str(z1, z2, str1='', str2=''):
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

class summe():

    def exponenten(list_term, exp, list_var=[]):
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

    def terme(terme, list_var=[], null=[True,False][0], eins=[True, False][1]):
        n = len(terme)
        summe_str = ''
        if list_var != []:
            if len(list_var) == 1:
                var = [list_var[0] for k in terme]
            elif len(list_var) > 1 and len(list_var) != len(terme):
                exit('Fehler in summe_terme: Die angegebenen Listen sind verschieden lang.')
            else:
                var = list_var
            for step in range(n):
                if terme[0] != 0:
                    summe_str = gzahl(terme[0]) + str(var[0]) if eins and var[0] not in liste_teilaufg else vorz_v_aussen(terme[0],var[0])
                    del terme[0]
                    del var[0]
                    break
                else:
                    del terme[0]
                    del var[0]
            for step in range(len(terme)):
                summand = vorz_str(terme[step]) + str(var[step]) if eins and var[step] not in liste_teilaufg else vorz_v_innen(terme[step], var[step])
                summe_str = summe_str + summand
        else:
            for step in range(n):
                if terme[0] != 0:
                    summe_str = gzahl(terme[0])
                    del terme[0]
                    break
                else:
                    del terme[0]
            for step in range(len(terme)):
                summe_str += vorz_str(terme[step])
        if summe_str == '':
            summe_str = '0' if null else ''
        return summe_str

def umformung(zahl, art=['+', '-', '*', ':'][0]):
    # if zahl == 0:
    #     if art == ':':
    #         exit("Fehler bei umformung(zahl, art): die Zahl ist 0 eine Division damit nicht zulässig.")
    #     elif art in ['+', '-']:
    #         return ''
    if zahl == 1 and art in ['*', ':']:
        return ''
    elif art == '+':
        return r' \quad \vert ' + vorz_str(zahl)
    elif art == '-':
        return r' \quad \vert ' + vorz_str(-1*zahl)
    elif art in ['*', ':'] and zahl == 1:
        return ''
    elif art == '*':
        return r' \quad \vert \cdot ' + gzahl_klammer(zahl)
    elif art == ':':
        return r' \quad \vert \div ' + gzahl_klammer(zahl)
    else:
        exit("Fehler bei Funktion umformung(zahl, art): art muss aus ['+','-', '*', ':'] sein")
# diverses
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

def beschriftung(teilaufg, i, latex_math=False):
    if len(teilaufg) == 1:
        return ''
    if latex_math:
        return str(liste_teilaufg[i]) + r') \quad '
    else:
        return str(liste_teilaufg[i]) + ') '

# Funktionen zur Optimierung von Ergebnissen mit True and False als Ausgabe
class vektor():
    def rational(vec,p,q=1000):
        vec_p = [element*p for element in vec]
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
    def punkt(p,n=3):
        return np.array([zzahl(1,p) for _ in range(n)])

    def runden(vec,p):
        return [N(elements,p) for elements in vec]

    def ganzzahl(vec):
        return np.array([int(element) if element % 1 == 0 else element for element in vec])

    def kuerzen(vec, p = 50, qout=False):
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

    def kollinear(vec1, vec2):
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

    def test_senk(vec1, vec2):
        lsg = [vec1[k] * vec2[k] for k in range(len(vec1))]
        if sum(lsg) != 0:
            return False
        return True

    def max(vec, p):
        vec_p = [element / p for element in vec]
        k = 0
        for element in vec_p:
            if element % 1 == 0:
                k += 1
        if k == len(vec):
            return True
        else:
            return False

    def vergleich(vec1, vec2):
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

    def invers(matrix):
        inverse = []
        for k in range(len(matrix[0])):
            row = [element[k] for element in matrix]
            inverse.append(row)
        return inverse

    def rechnung(obj1, obj2, var_obj1=[], var_obj2=[]):
        punkte = 0
        lsg = []
        # Funktionen, die mehrere Abfragen benötigen
        def quotient(zae, nen, gz='~=~'):
            if nen == 0 :
                text = r' \mathrm{~ ist ~ n.d.}' if zae != 0 else r' \in \mathbb{R} '
                lsg = ()
            else:
                erw = vektor.kuerzen([zae, nen])
                z1, z2 = erw[0], erw[1]
                lsg = Rational(z1, z2)
                text = latex(Rational(z1, z2))
                # print(zae), print(nen), print(lsg), print(text)
            return text, lsg
        # hier werden die Fälle (Vektor-Vektor) und (Vektor-Gerade) betrachtet
        if len(obj1) == len(obj2) == 1 or (len(obj1)== 1 and len(obj2)==2) and len(var_obj2) < 2:
            var = var_obj2[0] if var_obj2 != [] else 'r'
            if len(obj2)==2:
                a1, a2, a3 = obj1[0]
                [[b1, b2, b3], [c1, c2, c3]] = obj2
                text0 = (r' \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\' + gzahl(a3) + r' \\'
                         + r' \end{pmatrix}  ~=~  \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2) + r' \\'
                         + gzahl(b3) + r' \\' + r' \end{pmatrix} + ' + var + r' \cdot \begin{pmatrix} ' + gzahl(c1)
                         + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\' + r' \end{pmatrix} \quad \left\vert '
                         + r' - \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2) + r' \\' + gzahl(b3) + r' \\'
                         + r' \end{pmatrix} \right. \quad (1BE) \\\\ ')
                obj1 = [[a1-b1, a2-b2, a3-b3]]
                obj2 = [[c1, c2, c3]]
                punkte += 1
            else:
                text0 = ''
            if all(zahl == 0 for zahl in obj1[0]) or all(zahl == 0 for zahl in obj2[0]):
                exit('Fehler in vektor.rechnung: Ein Vektor ist der Nullvektor, der keine Richtung hat. '
                     'Es ist keine Rechnung möglich')
            else:
                [a1, a2, a3], [b1, b2, b3] = obj1[0], obj2[0]
                text1, lsg1 = quotient(a1, b1)
                text2, lsg2 = quotient(a2, b2)
                text3, lsg3 = quotient(a3, b3)

                text = [text0 + r' \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\' + gzahl(a3)
                        + r' \\' + r' \end{pmatrix}  ~=~ ' + var + r' \cdot \begin{pmatrix} ' + gzahl(b1) + r' \\'
                        + gzahl(b2) + r' \\' + gzahl(b3) + r' \\'
                        + r' \end{pmatrix} \quad \to \quad \begin{matrix} ' + gzahl(a1) + '~=~'
                        + vorz_v_aussen(b1,var, null=True) + r' \\' + gzahl(a2) + '~=~'
                        + vorz_v_aussen(b2,var, null=True) + r' \\' + gzahl(a3) + '~=~'
                        + vorz_v_aussen(b3,var, null=True) + r' \\'
                        + r' \end{matrix} \quad \to \quad \begin{matrix} ' + var + '~=~' + text1 + r' \\' + var
                        + '~=~' + text2 + r' \\' + var + '~=~' + text3 + r' \\' + r' \end{matrix} \quad (3BE) ']
                lsg = [lsg1, lsg2, lsg3]
                punkte += 3

        # hier werden die Fälle (Gerade-Gerade), (Vektor-Ebene) oder (Vektor-2_Richtungsvektoren) betrachtet
        elif len(obj1) + len(obj2) == 4 or len(var_obj2) == 2:
            def gls_sortieren(gls, zeilnr=[True,False][1]): # diese Funktion sortiert das Gleichungssystem nach den vorhandenen Variablen
                matrix = []
                for k in range(len(gls)):
                    nr = [zeilennummer[k+1]] if zeilnr else []
                    matrix.append(nr + gls[k])
                rsnull, snull, rnull, nnull = [], [], [], []
                bez = 1 if zeilnr else 0
                for element in matrix:
                    if element[2 + bez] == 0 and element[3 + bez] == 0:
                        rsnull.append(element)
                    elif element[3 + bez] == 0:
                        snull.append(element)
                    elif element[2 + bez] == 0:
                        rnull.append(element)
                    else:
                        nnull.append(element)
                return [rsnull, snull, rnull, nnull]

            if len(obj1) == len(obj2) == 2: # hier wird der Text und die Probe für den Fall (Gerade-Gerade) erzeugt
                if all(zahl == 0 for zahl in obj1[1]) or all(zahl == 0 for zahl in obj2[1]):
                    exit('Fehler in vektor.rechnung: Der Richtungsvektor einer der beiden Gerade ist der Nullvektor, '
                         'der keine Richtung hat.')
                [[a1, a2, a3], [b1, b2, b3]], [[c1, c2, c3], [d1, d2, d3]] = obj1, obj2
                gls_us = obj1 + obj2
                var1 = var_obj1[0] if var_obj1 else 'r'
                var2 = var_obj2[0] if var_obj2 else 's'
                text = (r' \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\' + gzahl(a3) + r' \\'
                        + r' \end{pmatrix} + ' + var1 + r' \cdot  \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2)
                        + r' \\' + gzahl(b3) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(c1)
                        + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\' + r' \end{pmatrix} + ' + var2
                        + r' \cdot \begin{pmatrix} ' + gzahl(d1) + r' \\' + gzahl(d2) + r' \\' + gzahl(d3) + r' \\'
                        + r' \end{pmatrix} \quad \to \quad \begin{matrix} I \\ II \\ III \\ \end{matrix} '
                        + r'\quad \begin{matrix} ' + summe.terme([a1, b1], ['', var1]) + '~=~'
                        + summe.terme([c1, d1], ['', var2], null=True) + r' \\'
                        + summe.terme([a2, b2], ['', var1], null=True) + '~=~'
                        + summe.terme([c2, d2], ['', var2], null=True) + r' \\'
                        + summe.terme([a3, b3], ['', var1], null=True) + '~=~'
                        + summe.terme([c3, d3], ['', var2], null=True) + r' \\'
                        + r' \end{matrix} \quad (2BE)')

                gls_usi = vektor.invers([[a1, a2, a3],  [c1, c2, c3], [-1*b1, -1*b2, -1*b3], [d1, d2, d3]])
                erg_sort = gls_sortieren(gls_usi, zeilnr=True)
                punkte += 2

                def rg_rnull(zeile):
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + gzahl(zeile[1]) + '~=~' + summe.terme([zeile[2],zeile[4]], ['', var2])
                            + umformung(zeile[2],'-') + umformung(zeile[4],':') + r' \quad \to \quad '
                            + var2 + '~=~' + gzahl(Rational(zeile[1]-zeile[2],zeile[4])) + r' \quad (1BE)')
                    lsg = Rational(zeile[1]-zeile[2],zeile[4])
                    return text, lsg
                def rg_snull(zeile):
                    bez, a1, b1, c1, d1 = zeile[0], zeile[1], -1*zeile[3], zeile[2], zeile[4]
                    text = (r' \\ \mathrm{aus~' + gzahl(bez) + r'~folgt:} \quad '
                            + summe.terme([a1, b1],['',var1]) + '~=~' + gzahl(c1)
                            + umformung(a1,'-') + umformung(b1,':') + r' \quad \to \quad '
                            + var1 + '~=~' + gzahl(Rational(c1 - a1, b1)) + r' \quad (1BE)')
                    lsg = Rational(c1-a1,b1)
                    return text, lsg
                def rg_nnull(zeilen):
                    pkt = 3
                    bez1, a1, b1, c1, d1 = zeilen[0][0], zeilen[0][1], -1*zeilen[0][3], zeilen[0][2], zeilen[0][4]
                    bez2, a2, b2, c2, d2 = zeilen[1][0], zeilen[1][1], -1*zeilen[1][3], zeilen[1][2], zeilen[1][4]
                    if Rational(b2*d1-d2*b1,b1) != 1:
                        zws3 = (umformung(Rational(b2*d1-d2*b1,b1), ':') + r' \quad \to \quad ' + var2 + '~=~'
                                + gzahl(Rational(c2*b1-a2*b1-b2*c1+b2*a1, b2*d1-d2*b1)) + r' \quad (2BE) \\')
                        pkt += 2
                    else:
                        zws3 = r' \quad (1BE) \quad '
                        pkt += 1

                    text = (r' \\ \mathrm{aus~' + gzahl(bez1) + r'~folgt:} \quad '
                            + summe.terme([a1, b1],['',var1]) + '~=~'
                            + summe.terme([c1, d1], ['', var2]) + umformung(a1,'-')
                            + umformung(b1,':') + r' \quad \to \quad ' + var1 + '~=~'
                            + gzahl(Rational(c1 - a1, b1)) + vorz_v_innen(Rational(d1, b1), var2)
                            + r' \quad (1BE) ')
                    text = (text + r' \\ \mathrm{aus~' + gzahl(bez2) + r'~folgt:} \quad '
                            + summe.terme([a2, b2],['',r' \cdot ' + binom_klammer(Rational(c1 - a1, b1),Rational(d1, b1), str2=var2)]) + '~=~'
                            + summe.terme([c2, d2],['', var2]) + r' \quad \to \quad '
                            + summe.terme([a2, Rational(b2*(c1 - a1),b1), Rational(b2*d1, b1)], ['','', var2])
                            + '~=~' + summe.terme([c2, d2], ['', var2])
                            + umformung(Rational(a2*b1 + b2*c1 - b2*a1,b1), '-') + r' \quad \vert ' + vorz_v_innen(-1*d2, var2)
                            + r' \quad (1BE) \\ ' + vorz_v_aussen(Rational(b2*d1-d2*b1,b1), var2) + '~=~'
                            + gzahl(Rational(c2*b1 - a2*b1 - b2*c1 + b2*a1, b1)))
                    if b2*d1-d2*b1 == 0:
                        text += r' f.A. \quad (1BE) ' if c2*b1 - a2*b1 - b2*c1 + b2*a1 != 0 else r' w.A. \quad (1BE) '
                        lsg = []
                    else:
                        text += (zws3 + r' \mathrm{und} \quad ' + var1 + '~=~'
                                 + summe.terme([Rational(c1 - a1, b1), Rational(d1, b1)],['', r' \cdot ' + gzahl_klammer(Rational(c2*b1-a2*b1-b2*c1+b2*a1, b2*d1-d2*b1))], eins=True)
                                 + '~=~' + gzahl(Rational(c1 - a1, b1) + Rational(d1*(c2*b1-a2*b1-b2*c1+b2*a1), b1*(b2*d1-d2*b1)))
                                 + r' \quad (1BE)')
                        lsg = [Rational(c1 - a1, b1) + Rational(d1*(c2*b1 - a2*b1 - b2*c1 + b2*a1), b1*(b2*d1 - d2*b1)),
                               Rational(c2*b1 - a2*b1 - b2*c1 + b2*a1, b2*d1 - d2*b1)]
                    print(lsg)
                    return text, lsg, pkt
                def rg_nnull_lsgr(zeile,lsgr): # hier wird die Lösung für r in nnull eingesetzt und das Ergebnis ist lsgs
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + summe.terme([zeile[1], -1*zeile[3]],['',r' \cdot ' + gzahl_klammer(lsgr, eins=True)], eins=True)
                            + '~=~' + summe.terme([zeile[2], zeile[4]], ['', var2])
                            + umformung(zeile[2],'-') + umformung(zeile[4],':')
                            + r' \quad \to \quad ' + var2 + '~=~'
                            + gzahl(Rational(zeile[1] - zeile[2] - zeile[3]*lsgr, zeile[4])) + r' \quad (2BE)')
                    lsg = Rational(zeile[1] - zeile[2] - zeile[3]*lsgr, zeile[4])
                    return text, lsg
                def rg_nnull_lsgs(zeile, lsgs): # hier wird die Lösung für s in nnull eingesetzt und das Ergebnis ist lsgr
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + summe.terme([zeile[1], -1*zeile[3]], ['', var1]) + '~=~'
                            + summe.terme([zeile[2], zeile[4]], ['', r' \cdot ' + gzahl_klammer(lsgs, eins=True)], eins=True)
                            + umformung(zeile[1], '-') + umformung(-1*zeile[3], ':')
                            + r' \quad \to \quad ' + var1 + '~=~'
                            + gzahl(Rational(zeile[2] - zeile[1] + zeile[4]*lsgs, -1*zeile[3])) + r' \quad (2BE)')
                    lsg = Rational(zeile[2] - zeile[1] + zeile[4]*lsgs, -1*zeile[3])
                    return text, lsg
                def rg_nnull_probe(zeile, lsg):
                    bez, a1, b1, c1, d1  = zeile[0], zeile[1], -1*zeile[3], zeile[2], zeile[4]
                    var1, var2 = lsg
                    erg1 = a1 + var1*b1 if type(a1 + var1*b1) != float else N(a1+var1*b1,3)
                    erg2 = c1 + var2*d1 if type(c1 + var2*d1) != float else N(c1+var2*d1,3)
                    text = (r' \\\\ \mathrm{Probe~durch~Einsetzen~der~Lösungen~in~Gleichung~' + bez
                            + r' } \\ '
                            + summe.terme([a1,b1], ['', r' \cdot ' + gzahl_klammer(var1)], eins=True)
                            + '~=~' + summe.terme([c1, d1], ['', r' \cdot ' + gzahl_klammer(var2)], eins=True)
                            + r' \quad \to \quad' + gzahl(erg1) + '~=~' + gzahl(erg2))
                    if erg1 - erg2 == 0:
                        text += r' \quad \mathrm{w.A.}  \quad (2BE) '
                        lsg = lsg
                    else:
                        text += r' \quad \mathrm{f.A.}  \quad (2BE) '
                        lsg = []
                    print(lsg)
                    return text, lsg
                def probe(lsg):
                    erg1 = np.array(obj1[0]) + lsg[0]*np.array(obj1[1])
                    erg2 = np.array(obj2[0]) + lsg[1]*np.array(obj2[1])
                    text = (r' \\\\ \mathrm{Probe: \quad } \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2)
                            + r' \\' + gzahl(a3) + r' \\' + r' \end{pmatrix} ' + vorz_str(lsg[0], null=True)
                            + r' \cdot  \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2)
                            + r' \\' + gzahl(b3) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(c1)
                            + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\' + r' \end{pmatrix} '
                            + vorz_str(lsg[1], null=True) + r' \cdot \begin{pmatrix} ' + gzahl(d1) + r' \\' + gzahl(d2)
                            + r' \\' + gzahl(d3) + r' \\' + r' \end{pmatrix} \quad \to \quad \begin{pmatrix} '
                            + gzahl(a1 + lsg[0] * b1) + r'\\' + gzahl(a2 + lsg[0]*b2) + r' \\' + gzahl(a3 + lsg[0]*b3)
                            + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(c1 + lsg[1] * d1) + r'\\'
                            + gzahl(c2 + lsg[1]*d2) + r' \\' + gzahl(c3 + lsg[1]*d3) + r' \\'
                            + r' \end{pmatrix} ')
                    if all(erg1[k]-erg2[k] == 0 for k in range(len(erg1))):
                        text += r' \quad \mathrm{w.A.}  \quad (2BE) '
                        lsg = lsg
                    else:
                        text += r' \quad \mathrm{f.A.}  \quad (2BE) '
                        lsg = []
                    return text, lsg

            elif len(obj1) == 1 and len(obj2) == 3: # hier wird der Text und die Probe für den Fall (Vektor-Ebene) erzeugt
                if all(zahl == 0 for zahl in obj2[1]) or all(zahl == 0 for zahl in obj2[2]):
                    exit('Fehler in vektor.rechnung: Ein Richtungsvektor der Ebene ist der Nullvektor, '
                         'der keine Richtung hat.')
                [[a1, a2, a3]], [[b1, b2, b3], [c1, c2, c3], [d1, d2, d3]] = obj1, obj2
                gls_us = obj1 + obj2
                gls_usi = vektor.invers(gls_us)
                var_obj2 = ['r','s'] if len(var_obj2) != 2 else var_obj2
                var1, var2 = var_obj2[0], var_obj2[1]
                text = (r' \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\' + gzahl(a3) + r' \\'
                        + r' \end{pmatrix} ~=~ ' + r' \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2)
                        + r' \\' + gzahl(b3) + r' \\' + r' \end{pmatrix} + ' + var1 + r' \cdot  \begin{pmatrix} '
                        + gzahl(c1) + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\' + r' \end{pmatrix} + ' + var2
                        + r' \cdot \begin{pmatrix} ' + gzahl(d1) + r' \\' + gzahl(d2) + r' \\' + gzahl(d3) + r' \\'
                        + r' \end{pmatrix} \quad \to \quad \begin{matrix} I \\ II \\ III \\ \end{matrix} \quad '
                        + r' \begin{matrix}' + gzahl(a1) + '~=~'
                        + summe.terme([b1, c1, d1], ['', var1, var2], null=True)
                        + r' \\' + gzahl(a2) + '~=~'
                        + summe.terme([b2, c2, d2], ['', var1, var2], null=True)
                        + r' \\' + gzahl(a3) + '~=~'
                        + summe.terme([b3, c3, d3], ['', var1, var2], null=True) + r' \\'
                        + r' \end{matrix} \quad (2BE)')
                gls_usi = vektor.invers([[a1, a2, a3],  [b1, b2, b3], [c1, c2, c3], [d1, d2, d3]])
                erg_sort = gls_sortieren(gls_usi, zeilnr=True)
                punkte += 2

                def rg_rnull(zeile):
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + gzahl(zeile[1]) + '~=~' + summe.terme([zeile[2], zeile[4]],['', var2])
                            + umformung(zeile[2], '-') + umformung(zeile[4], ':') + r' \quad \to \quad '
                            + var2 + '~=~' + gzahl(Rational(zeile[1] - zeile[2], zeile[4])) + r' \quad (1BE)')
                    lsg = Rational(zeile[1] - zeile[2], zeile[4])
                    return text, lsg
                def rg_snull(zeile):
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + gzahl(zeile[1]) + '~=~' + summe.terme([zeile[2], zeile[3]],['',var1])
                            + umformung(zeile[2], '-') + umformung(zeile[3], ':') + r' \quad \to \quad '
                            + var1 + '~=~' + gzahl(Rational(zeile[1] - zeile[2], zeile[3])) + r' \quad (1BE)')
                    lsg = Rational(zeile[1] - zeile[2], zeile[3])
                    return text, lsg
                def rg_nnull(zeilen):
                    pkt = 0
                    bez1, a1, b1, c1, d1 = zeilen[0]
                    if d1 !=1:
                        zws1 = ((umformung(d1, ':') + r' \quad \to \quad ' + var2 + '~=~'
                                + summe.terme([Rational(a1 - b1, d1), Rational(-1 * c1, d1)], ['', var1]))
                                + r' \quad (2BE) ')
                        pkt += 2
                    else:
                        zws1 = r' \quad (1BE) '
                        pkt += 1
                    bez2, a2, b2, c2, d2 = zeilen[1]
                    if Rational(b2*d1 + d2*a1 - d2*b1, d1) != 0:
                        zws2 = umformung(Rational(b2*d1 + d2*a1 - d2*b1, d1),'-') + r' \quad (2BE) \\ '
                        pkt += 2
                    else:
                        zws2 = r' \quad (1BE)'
                        pkt += 1
                    if Rational(c2*d1 - d2*c1, d1) != 1:
                        zws3 = (umformung(Rational(c2*d1 - d2*c1, d1), ':') + r' \quad \to \quad '
                                + var1 + '~=~' + gzahl(Rational(a2*d1 - b2*d1 - d2*a1 + d2*b1, c2*d1 - d2*c1))
                                + r' \quad (2BE) \\ ')
                        pkt += 2
                    else:
                        zws3 = r' \quad (1BE) \quad '
                        pkt += 1
                    text = (r' \\ \mathrm{aus~' + gzahl(bez1) + r'~folgt:} \quad '
                            + gzahl(a1) + '~=~' + summe.terme([b1, c1, d1], ['', var1, var2])
                            + umformung(b1,'-') + r' \quad \vert ' + vorz_v_innen(-1*c1, var1)
                            + r' \quad \to \quad ' + vorz_v_aussen(d1, var2) + '~=~'
                            + summe.terme([a1-b1,-1*c1],['', var1]) + zws1
                            + r' \\ \mathrm{aus~' + gzahl(bez2) + r'~folgt:} \quad '
                            + gzahl(a2) + '~=~'
                            + summe.terme([b2, c2, d2], ['', var1, r' \cdot ' + binom_klammer(Rational(a1 - b1, d1), Rational(-1*c1, d1), str2=var1)])
                            + r' \quad \to \quad ' + gzahl(a2) + '~=~'
                            + summe.terme([Rational(b2*d1 + d2*a1 - d2*b1, d1), Rational(c2*d1 - d2*c1, d1)],['', var1])
                            + zws2 + vorz_v_aussen(Rational(c2*d1 - d2*c1, d1), var1) + '~=~'
                            + gzahl(Rational(a2*d1 - b2*d1 - d2*a1 + d2*b1, d1)))
                    if c2*d1 - d2*c1 == 0:
                        text += r' f.A. \quad (1BE) ' if a2*d1 - b2*d1 - d2*a1 + d2*b1 != 0 else r' w.A. \quad (1BE) '
                        lsg = []
                    else:
                        text += (zws3 + r' \mathrm{und} \quad ' + var2 + '~=~'
                                 + summe.terme([Rational(a1-b1,d1), Rational(-1*c1,d1)],['', r' \cdot ' + gzahl_klammer(Rational(a2*d1 - b2*d1 - d2*a1 + d2*b1, c2*d1 - d2*c1))], eins=True)
                                 + '~=~' + gzahl(Rational(a1-b1,d1) + Rational(c1*(a2*d1 - b2*d1 - d2*a1 + d2*b1),d1*(c2*d1 - d2*c1)))
                                 + r' \quad (1BE)')
                        lsg = [Rational(a2*d1 - b2*d1 - d2*a1 + d2*b1, c2*d1 - d2*c1),
                               Rational(a1-b1,d1) + Rational(c1*(a2*d1 - b2*d1 - d2*a1 + d2*b1),d1*(c2*d1 - d2*c1))]
                    pkt += 1
                    return text, lsg, pkt
                def rg_nnull_lsgr(zeile, lsgr): # hier wird die Lösung für r in nnull eingesetzt und das Ergebnis ist lsgs
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad ' + gzahl(zeile[1]) + '~=~'
                            + summe.terme([zeile[2], zeile[3], zeile[4]],
                                          ['', r' \cdot ' + gzahl_klammer(lsgr, eins=True), var2], eins=True)
                            + umformung(zeile[2] + zeile[3]*lsgr, '-') + umformung(zeile[4], ':')
                            + r' \quad \to \quad ' + var2 + '~=~'
                            + gzahl(Rational(zeile[1] - zeile[2] - zeile[3] * lsgr, zeile[4])) + r' \quad (2BE)')
                    lsg = Rational(zeile[1] - zeile[2] - zeile[3] * lsgr, zeile[4])
                    return text, lsg
                def rg_nnull_lsgs(zeile, lsgs): # hier wird die Lösung für s in nnull eingesetzt und das Ergebnis ist lsgr
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad ' + gzahl(zeile[1]) + '~=~'
                            + summe.terme([zeile[2], zeile[3], zeile[4]],
                                          ['', var1, r' \cdot ' + gzahl_klammer(lsgs, eins=True)], eins=True)
                            + umformung(zeile[2]+zeile[4]*lsgs, '-') + umformung(zeile[3], ':')
                            + r' \quad \to \quad ' + var1 + '~=~'
                            + gzahl(Rational(zeile[1] - zeile[2] - zeile[4] * lsgs, zeile[3])) + r' \quad (2BE)')
                    lsg = Rational(zeile[1] - zeile[2] - zeile[4] * lsgs, zeile[3])
                    return text, lsg
                def rg_nnull_probe(zeile, lsg):
                    bez, a1, b1, c1, d1  = zeile
                    var1, var2 = lsg
                    erg1 = a1 if type(a1) != float else N(a1,3)
                    erg2 = b1 + var1*c1 + var2*d1 if type(b1 + var1*c1 + var2*d1) != float else N(b1 + var1*c1+var2*d1,3)
                    text = (r' \\\\ \mathrm{Probe~durch~Einsetzen~der~Lösungen~in~Gleichung~} ' + bez
                            + r' \\ ' + gzahl(a1) + '~=~'
                            + summe.terme([b1, c1, d1], ['', r' \cdot ' + gzahl_klammer(var1), r' \cdot ' + gzahl_klammer(var2)], eins=True)
                            + r' \quad \to \quad ' + gzahl(erg1) + '~=~' + gzahl(erg2))
                    if erg1 - erg2 == 0:
                        text += r' \quad \mathrm{ w.A. }  \quad (2BE) '
                        lsg = lsg
                    else:
                        text += r' \quad \mathrm{ f.A. }  \quad (2BE) '
                        lsg = []
                    return text, lsg
                def probe(lsg):
                        erg1 = np.array(obj1[0])
                        erg2 = np.array(obj2[0]) + lsg[0] * np.array(obj2[1]) + lsg[1] * np.array(obj2[2])
                        text = (r' \\\\ \mathrm{Probe: \quad } \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\'
                                + gzahl(a3) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(b1) + r' \\'
                                + gzahl(b2) + r' \\' + gzahl(b3) + r' \\' + r' \end{pmatrix} ' + vorz_str(lsg[0], null=True)
                                + r' \cdot  \begin{pmatrix} ' + gzahl(c1) + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\'
                                + r' \end{pmatrix} ' + vorz_str(lsg[1], null=True) + r' \cdot \begin{pmatrix} '
                                + gzahl(d1) + r' \\' + gzahl(d2) + r' \\' + gzahl(d3) + r' \\'
                                + r' \end{pmatrix} \quad \to \quad \begin{pmatrix} ' + gzahl(a1) + r'\\' + gzahl(a2)
                                + r' \\' + gzahl(a3) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} '
                                + gzahl(b1 + lsg[0] * c1 + lsg[1] * d1) + r'\\'
                                + gzahl(b2 + lsg[0]* c2 + lsg[1] * d2) + r' \\' + gzahl(b3 + lsg[0]*c3 + lsg[1] * d3)
                                + r' \\' + r' \end{pmatrix} ')
                        if all(erg1[k]-erg2[k] == 0 for k in range(len(erg1))):
                            text += r' \quad \mathrm{w.A.}  \quad (2BE) '
                            lsg = lsg
                        else:
                            text += r' \quad \mathrm{f.A.}  \quad (2BE) '
                            lsg = []
                        return text, lsg

            elif len(obj1) == 1 and len(obj2) == 2 and len(var_obj2) == 2: # hier wird der Text und die Probe für den Fall (Vektor-2_Richtungsvektoren) erzeugt
                if all(zahl == 0 for zahl in obj2[0]) or all(zahl == 0 for zahl in obj2[1]):
                    exit('Fehler in vektor.rechnung: Ein Richtungsvektor ist der Nullvektor, '
                         'der keine Richtung hat.')
                [[a1, a2, a3]], [[b1, b2, b3], [c1, c2, c3]] = obj1, obj2
                gls_us = obj1 + obj2
                gls_usi = vektor.invers(gls_us)
                var_obj2 = ['r','s'] if len(var_obj2) != 2 else var_obj2
                var1, var2 = var_obj2[0], var_obj2[1]
                text = (r' \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\' + gzahl(a3) + r' \\'
                        + r' \end{pmatrix} ~=~ ' + var1 + r' \cdot  \begin{pmatrix} '
                        + gzahl(b1) + r' \\' + gzahl(b2) + r' \\' + gzahl(b3) + r' \\' + r' \end{pmatrix} + ' + var2
                        + r' \cdot \begin{pmatrix} ' + gzahl(c1) + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\'
                        + r' \end{pmatrix} \quad \to \quad \begin{matrix} I \\ II \\ III \\ \end{matrix} \quad '
                        + r' \begin{matrix}' + gzahl(a1) + '~=~'
                        + summe.terme([b1, c1], [var1, var2], null=True)
                        + r' \\' + gzahl(a2) + '~=~'
                        + summe.terme([b2, c2], [var1, var2], null=True)
                        + r' \\' + gzahl(a3) + '~=~'
                        + summe.terme([b3, c3], [var1, var2], null=True) + r' \\'
                        + r' \end{matrix} \quad (2BE)')
                gls_usi = vektor.invers([[a1, a2, a3],  [0, 0, 0], [b1, b2, b3], [c1, c2, c3]])
                erg_sort = gls_sortieren(gls_usi, zeilnr=True)
                punkte += 2
                def rg_rnull(zeile):
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + gzahl(zeile[1]) + '~=~' + vorz_v_aussen(zeile[4], var2)
                            + umformung(zeile[4], ':') + r' \quad \to \quad '
                            + var2 + '~=~' + gzahl(Rational(zeile[1], zeile[4])) + r' \quad (1BE)')
                    lsg = Rational(zeile[1], zeile[4])
                    return text, lsg
                def rg_snull(zeile):
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad '
                            + gzahl(zeile[1]) + '~=~' + vorz_v_aussen(zeile[3],var1)
                            + umformung(zeile[3], ':') + r' \quad \to \quad '
                            + var1 + '~=~' + gzahl(Rational(zeile[1], zeile[3])) + r' \quad (1BE)')
                    lsg = Rational(zeile[1], zeile[3])
                    return text, lsg
                def rg_nnull(zeilen):
                    pkt = 0
                    bez1, a1, lz, c1, d1 = zeilen[0]
                    if d1 != 1:
                        zws1 = (umformung(d1, ':') + r' \quad \to \quad ' + var2 + '~=~'
                                      + summe.terme([Rational(a1,d1), Rational(-1*c1,d1)],['', var1])
                                      + r' \quad (2BE) ')
                        pkt += 2
                    else:
                        zws1 = r' \quad (1BE) '
                        pkt += 1
                    bez2, a2, lz, c2, d2 = zeilen[1]
                    if d2 * a1 != 0:
                        zws2 = umformung(Rational(d2*a1, d1),'-') + r' \quad (2BE) \\ '
                        pkt += 2
                    else:
                        zws2 = r' \quad (1BE) '
                        pkt += 1
                    if Rational(c2 * d1 - d2 * c1, d1) != 1:
                        zws3 = (umformung(Rational(c2 * d1 - d2 * c1, d1), ':') + r' \quad \to \quad ' + var1 + '~=~'
                                + gzahl(Rational(a2 * d1 - d2 * a1, c2 * d1 - d2 * c1)) + r' \quad (2BE) \\')
                        pkt += 2
                    else:
                        zws3 = r' \quad (1BE) \quad '
                        pkt += 1
                    text = (r' \\ \mathrm{aus~' + gzahl(bez1) + r'~folgt:} \quad '
                            + gzahl(a1) + '~=~' + summe.terme([c1, d1], [var1, var2])
                            + r' \quad \vert ' + vorz_v_innen(-1*c1, var1)
                            + r' \quad \to \quad ' + vorz_v_aussen(d1, var2) + '~=~'
                            + summe.terme([a1,-1*c1],['', var1]) + zws1 + r' \\ \mathrm{aus~'
                            + gzahl(bez2) + r'~folgt:} \quad ' + gzahl(a2) + '~=~'
                            + summe.terme([c2, d2], [var1, r' \cdot ' + binom_klammer(Rational(a1, d1), Rational(-1*c1, d1), str2=var1)])
                            + r' \quad \to \quad ' + gzahl(a2) + '~=~'
                            + summe.terme([Rational(d2*a1, d1), Rational(c2*d1 - d2*c1, d1)],['', var1])
                            + zws2 + vorz_v_aussen(Rational(c2*d1 - d2*c1, d1), var1) + '~=~'
                            + gzahl(Rational(a2*d1 - d2*a1, d1)))
                    if c2*d1 - d2*c1 == 0:
                        text += r' f.A. \quad (1BE) ' if a2*d1 - d2*a1 != 0 else r' w.A. \quad (1BE) '
                        lsg =[]
                    else:
                        text += (zws3 + r' \mathrm{und} \quad ' + var2 + '~=~'
                        + summe.terme([Rational(a1,d1), Rational(-1*c1,d1)],['', r' \cdot ' + gzahl_klammer(Rational(a2*d1 - d2*a1, c2*d1 - d2*c1))])
                        + '~=~' + gzahl(Rational(a1,d1) + Rational(c1*(a2*d1 - d2*a1),d1*(c2*d1 - d2*c1)))
                        + r' \quad (1BE)')
                        lsg = [Rational(a2*d1 - d2*a1, c2*d1 - d2*c1), Rational(a1,d1) + Rational(c1*(a2*d1 - d2*a1),d1*(c2*d1 - d2*c1))]
                    pkt += 1
                    return text, lsg, pkt
                def rg_nnull_lsgr(zeile, lsgr): # hier wird die Lösung für r in nnull eingesetzt und das Ergebnis ist lsgs
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad ' + gzahl(zeile[1]) + '~=~'
                            + summe.terme([zeile[3], zeile[4]], [r' \cdot ' + gzahl_klammer(lsgr, eins=True), var2], eins=True)
                            + umformung(zeile[3]*lsgr, '-') + umformung(zeile[4], ':') + r' \quad \to \quad '
                            + var2 + '~=~' + gzahl(Rational(zeile[1] - zeile[3] * lsgr, zeile[4])) + r' \quad (2BE)')
                    lsg = Rational(zeile[1] - zeile[3] * lsgr, zeile[4])
                    return text, lsg
                def rg_nnull_lsgs(zeile, lsgs): # hier wird die Lösung für s in nnull eingesetzt und das Ergebnis ist lsgr
                    text = (r' \\ \mathrm{aus~' + gzahl(zeile[0]) + r'~folgt:} \quad ' + gzahl(zeile[1]) + '~=~'
                            + summe.terme([zeile[3], zeile[4]],[var1, r' \cdot ' + gzahl_klammer(lsgs, eins=True)], eins=True)
                            + umformung(zeile[4]*lsgs, '-') + umformung(zeile[3], ':') + r' \quad \to \quad '
                            + var1 + '~=~' + gzahl(Rational(zeile[1] - zeile[4] * lsgs, zeile[3])) + r' \quad (2BE)')
                    lsg = Rational(zeile[1] - zeile[4] * lsgs, zeile[3])
                    return text, lsg
                def rg_nnull_probe(zeile, lsg):
                    bez, a1, lz, c1, d1  = zeile
                    var1, var2 = lsg
                    erg1 = a1 if type(a1) != float else N(a1,3)
                    erg2 = var1*c1 + var2*d1 if type(var1*c1 + var2*d1) != float else N(var1*c1+var2*d1,3)
                    text = (r' \\\\ \mathrm{Probe~durch~Einsetzen~der~Lösungen~in~Gleichung~} ' + bez
                            + r' \\ ' + gzahl(a1) + '~=~'
                            + summe.terme([c1, d1], [r' \cdot ' + gzahl_klammer(var1), r' \cdot ' + gzahl_klammer(var2)], eins=True)
                            + r' \quad \to \quad ' + gzahl(erg1) + '~=~' + gzahl(erg2))
                    if erg1 - erg2 == 0:
                        text += r' \quad \mathrm{ w.A. }  \quad (2BE) '
                        lsg = lsg
                    else:
                        text += r' \quad \mathrm{ f.A. }  \quad (2BE) '
                        lsg = []
                    return text, lsg
                def probe(lsg):
                    erg1 = np.array(obj1[0])
                    erg2 = lsg[0] * np.array(obj2[0]) + lsg[1] * np.array(obj2[1])
                    text = (r' \\\\ \mathrm{Probe: \quad } \begin{pmatrix} ' + gzahl(a1) + r' \\' + gzahl(a2) + r' \\'
                            + gzahl(a3) + r' \\' + r' \end{pmatrix} ~=~ ' + gzahl(lsg[0])
                            + r' \cdot  \begin{pmatrix} ' + gzahl(b1) + r' \\' + gzahl(b2) + r' \\' + gzahl(b3) + r' \\'
                            + r' \end{pmatrix} ' + vorz_str(lsg[1], null=True) + r' \cdot \begin{pmatrix} '
                            + gzahl(c1) + r' \\' + gzahl(c2) + r' \\' + gzahl(c3) + r' \\'
                            + r' \end{pmatrix} \quad \to \quad \begin{pmatrix} ' + gzahl(a1) + r'\\' + gzahl(a2)
                            + r' \\' + gzahl(a3) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} '
                            + gzahl(lsg[0] * b1 + lsg[1] * c1) + r'\\'
                            + gzahl(lsg[0]* b2 + lsg[1] * c2) + r' \\' + gzahl(lsg[0]*b3 + lsg[1] * c3)
                            + r' \\' + r' \end{pmatrix} ')
                    if all(erg1[k]-erg2[k] == 0 for k in range(len(erg1))):
                        text += r' \quad \mathrm{w.A.}  \quad (2BE) '
                        lsg = lsg
                    else:
                        text += r' \quad \mathrm{f.A.}  \quad (2BE) '
                        lsg = []
                    return text, lsg

            # hier werden die Gleichungen nach den gegebenen Variablen sortiert 1 (rsnull): r und s sind null, 2 (snull): r ist null, 3 (rnull): s ist null und 4 (nnull): nichts ist null
            rsnull, snull, rnull, nnull = erg_sort

            # Ab hier werden alle möglichen Varianten der Lösung erzeugt (1!=1, 1-1-4 , 1-2-3, 1-2-4, 1-3-4, 1-4-4, 2!=2, 2-2-3, 2-2-4, 2-3-4, 2-3!=3, 2-3=3, 2-4-4, 2-4!=4, 3!=3, 3=3-4, 3-4!=4, 3-4=4)
            if len(rsnull) == 2: # Ihr werden alle Lösungen erzeugt, wenn rsnull zweimal auftritt
                zeile1 = rsnull[0]
                zeile2 = rsnull[1]
                zeile3 = nnull[0]
                if zeile1[1] != zeile1[2]: # die erste Zeile erzeugt einen Widerspruch
                    text += (r' \\ \mathrm{aus~' + gzahl(zeile1[0]) + r'~folgt: \quad ' + gzahl(zeile1[1])
                            + '~=~' + gzahl(zeile1[2]) + r' \quad f.A.} \quad (1BE)')
                    lsg = []
                    punkte += 1
                elif zeile2[1] != zeile2[2]: # die zweite Zeile erzeugt einen Widerspruch
                    text += (r' \\ \mathrm{aus~' + gzahl(zeile2[0]) + r'~folgt: \quad ' + gzahl(zeile2[1])
                            + '~=~' + gzahl(zeile2[2]) + r' \quad f.A.} \quad (1BE)')
                    lsg = []
                    punkte += 1
                else: # hier kann nur noch 1-1-4 auftreten, alles andere wird ausgeschlossen, weil kein Richtungsvektor [0,0,0] sein darf
                    text += (r' \\ \mathrm{aus~' + gzahl(zeile1[0]) + r'~folgt: \quad ' + gzahl(zeile1[1])
                            + '~=~' + gzahl(zeile1[2]) + r' \quad w.A.} \quad (1BE) \\ \mathrm{aus~' + gzahl(zeile2[0])
                            + r'~folgt: \quad ' + gzahl(zeile2[1]) + '~=~' + gzahl(zeile2[2])
                            + r' \quad w.A.} \quad (1BE) \\ \mathrm{aus~' + gzahl(zeile3[0]) + r'~folgt:} \quad '
                            + vorz_v_aussen(-1*zeile3[3], var1) + '~=~'
                            + summe.terme([zeile3[2] - zeile3[1], zeile3[4]],['', var2])
                            + umformung(-1*zeile3[3],':') + r' \\' + var1 + '~=~'
                            + summe.terme([Rational(zeile3[2] - zeile3[1], -1*zeile3[3]),
                                           Rational(zeile3[4], -1*zeile3[3])],['', var2])
                            + r' \quad \to \quad ' + var1 + r' \in \mathbb{R} \quad (2BE)')
                    lsg = []
                    punkte += 4
            elif len(rsnull) == 1: # hier werden alle Fälle erzeugt, wenn rsnull einmal auftritt
                zeile1 = rsnull[0]
                if zeile1[1] != zeile1[2]: # die erste Zeile rsnull, erzeugt einen Widerspruch
                    text += (r' \\ \mathrm{aus~' + gzahl(zeile1[0]) + r'~folgt: \quad ' + gzahl(zeile1[1])
                            + '~=~' + gzahl(zeile1[2]) + r' \quad f.A.} \quad (1BE)')
                    lsg = []
                    punkte += 1
                else: # die erste Zeile ist eine wahre Aussage 1-...
                    text += (r' \\ \mathrm{aus~' + gzahl(zeile1[0]) + r'~folgt: \quad ' + gzahl(zeile1[1])
                           + '~=~' + gzahl(zeile1[2]) + r' \quad w.A.} \quad (2BE) ')
                    punkte += 2
                    if snull != []: # 1-2-...
                        snull_text, snull_lsg = rg_snull(snull[0])
                        text += snull_text
                        lsg.append(snull_lsg)
                        punkte += 1
                        if rnull != []: # 1-2-3 (erfordert Probe um das Ergebnis zu überprüfen)
                            rnull_text, rnull_lsg = rg_rnull(rnull[0])
                            text += rnull_text
                            lsg.append(rnull_lsg)
                            text_pr, lsg_pr = probe(lsg)
                            text, lsg = text + text_pr, lsg_pr
                            punkte += 3
                        elif nnull != []: # 1-2-4 (erfordert Probe um das Ergebnis zu überprüfen)
                            nnull_text, nnull_lsg = rg_nnull_lsgs(nnull[0], lsg[0])
                            text += nnull_text
                            lsg.append(nnull_lsg)
                            text_pr, lsg_pr = probe(lsg)
                            text, lsg = text + text_pr, lsg_pr
                            punkte += 4
                    elif rnull != []: # 1-3-4 (erfordert Probe um das Ergebnis zu überprüfen)
                        rnull_text, rnull_lsg = rg_rnull(rnull[0])
                        text += rnull_text
                        lsg.append(rnull_lsg)
                        nnull_text, nnull_lsg = rg_nnull_lsgr(nnull[0], lsg[0])
                        text += nnull_text
                        lsg.append( nnull_lsg)
                        text_pr, lsg_pr = probe(lsg)
                        text, lsg = text + text_pr, lsg_pr
                        punkte += 5
                    else: # 1-4-4 (erfordert Probe um das Ergebnis zu überprüfen)
                        text_nnull, lsg_nnull, lsg_pkt = rg_nnull(nnull)
                        text += text_nnull
                        punkte += lsg_pkt
                        lsg = lsg_nnull
                        if lsg_nnull != []:
                            text_pr, lsg_pr = probe(lsg_nnull)
                            text, lsg = text + text_pr, lsg_pr
                            punkte += 2

            elif len(snull) == 2: # hier werden alle Fälle erzeugt, wenn snull (2-2-...) zweimal auftritt
                snull1_text, snull1_lsg = rg_snull(snull[0])
                snull2_text, snull2_lsg = rg_snull(snull[1])
                text += snull1_text + snull2_text
                punkte += 2
                if snull1_lsg != snull2_lsg: # 2 != 2 --> die beiden Lösungen aus den snull-Gleichungen für var2 sind nicht gleich, d.h. das Gleichungssystem ist nicht lösbar
                    lsg = []
                elif snull1_lsg == snull2_lsg: # 2-2 --> die beiden Lösungen aus den snull-Gleichungen für var2 sind gleich und var1 muss mit rnull oder nnull bestimmt werden
                    lsg = [snull1_lsg]
                    if rnull != []: # 2-2-3 (erfordert Probe um das Ergebnis zu überprüfen)
                        rnull_text, rnull_lsg = rg_rnull(rnull[0])
                        text += rnull_text
                        lsg.append( rnull_lsg)
                        text_pr, lsg_pr = probe(lsg)
                        text, lsg = text + text_pr, lsg_pr
                        punkte += 3
                    elif nnull != []: # 2-2-4 (erfordert Probe um das Ergebnis zu überprüfen)
                        nnull_text, nnull_lsg = rg_nnull_lsgs(nnull[0], lsg[0])
                        text_pr, lsg_pr = probe([lsg[0], nnull_lsg])
                        text, lsg = text + nnull_text + text_pr, lsg_pr
                        punkte += 4
            elif len(snull) == 1: # hier werden alle Fälle erzeugt, wenn snull (2-...) einmal auftritt
                snull_text, snull_lsg = rg_snull(snull[0])
                text += snull_text
                lsg = [snull_lsg]
                punkte += 1
                if rnull != []: # 2-3-...
                    rnull_text, rnull_lsg = rg_rnull(rnull[0])
                    text += rnull_text
                    lsg.append(rnull_lsg)
                    punkte += 1
                    if len(rnull) == 2: # 2-3-3
                        rnull_text, rnull_lsg = rg_rnull(rnull[1])
                        text += rnull_text
                        punkte += 1
                        lsg = [] if lsg[0] != rnull_lsg else lsg
                    elif nnull != []: # 2-3-4 --> 4 dient als Probe
                        nnull_text, nnull_lsg = rg_nnull_probe(nnull[0], lsg)
                        text += nnull_text
                        lsg = nnull_lsg
                        punkte += 2
                elif len(nnull) == 2: # 2-4-4
                    nnull_text, nnull_lsg = rg_nnull_lsgr(nnull[0], lsg[0])
                    nnull_probe_text, nnull_probe_lsg = rg_nnull_probe(nnull[1], [lsg[0], nnull_lsg])
                    text += nnull_text + nnull_probe_text
                    lsg = nnull_probe_lsg
                    punkte += 4
            elif len(rnull) == 2: # hier werden alle Fälle erzeugt, wenn rnull (3-3-..) zweimal auftritt
                rnull1_text, rnull1_lsg = rg_rnull(rnull[0])
                rnull2_text, rnull2_lsg = rg_rnull(rnull[1])
                text += rnull1_text + rnull2_text
                punkte += 2
                if rnull1_lsg != rnull2_lsg: # 3 != 3 --> die beiden Lösungen aus den rnull-Gleichungen für var2 sind nicht gleich, d.h. das Gleichungssystem ist nicht lösbar
                    lsg = []
                else: # 3-3-4
                    nnull_text, nnull_lsg = rg_nnull_lsgs(nnull[0], rnull1_lsg)
                    text_pr, lsg_pr = probe([nnull_lsg, rnull1_lsg])
                    text, lsg = text + nnull_text + text_pr, lsg_pr
                    punkte += 4
            elif len(rnull) == 1: # 3-4-4
                rnull_text, rnull_lsg = rg_rnull(rnull[0])
                nnull_text, nnull_lsg = rg_nnull_lsgs(nnull[0], rnull_lsg)
                nnull_probe_text, nnull_probe_lsg = rg_nnull_probe(nnull[1], [nnull_lsg, rnull_lsg])
                text, lsg  = text + rnull_text + nnull_text + nnull_probe_text, nnull_probe_lsg
                punkte += 5
            elif len(nnull) == 3: # 4-4-4
                nnull_text, nnull_lsg, nnull_pkt = rg_nnull(nnull)
                text += nnull_text
                punkte += nnull_pkt
                if nnull_lsg != []:
                    nnull_probe_text, nnull_probe_lsg = rg_nnull_probe(nnull[2], nnull_lsg)
                    text, lsg = text + nnull_probe_text, nnull_probe_lsg
                    punkte += 2
            else:
                print('Vektoren wurde nicht berechnet, weil vektor.rechnung die Kombination nicht kennt.')
            text = [text]
        else:
            text = ['']
            erg_sort = []
            punkte = 1

        return text, lsg, punkte

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
        anzahl = len(list) if anzahl > len(list) else anzahl
        random.shuffle(list)
        return list[:anzahl]
    else:
        print('wdh muss "True" or "False" sein')

def repeat(list, wdh=2):
    new_list = []
    for element in list:
        new_list.extend([element for _ in range(wdh)])
    return new_list[:26]

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
        if vektor.vergleich(tuble, vec) == True:
            return k
        else:
            k+=1
    return print('Element nicht in Liste')

# Teilberechnungen für Analysis
def gaussalgorithmus(gleichungen, variablen=[]):

    zeilennummer_reverse = {value: key for key, value in zeilennummer.items()}
    n = len(gleichungen)
    variablen = [liste_teilaufg[step] for step in range(len(gleichungen[0]) - 1)] if variablen == [] else variablen
    zw_lsg = []
    for i in range(n):
        zw_gl = gleichungen.copy()
        k = len(zw_lsg)
        for element in zw_gl:
            if element[i] != 0:
                if element[i] == -1:
                    zw_lsg.insert(k,element)
                elif element[i] == 1:
                    zw_lsg.insert(k,element)
                    k += 1
                else:
                    zw_lsg.append(element)
                gleichungen.remove(element)
    gleichungen = zw_lsg

    loesung = [[zeilennummer.get(k+1, 'zu groß'), ''] + gleichungen[k] for k in range(n)]

    for i in range(n):
        for k in range(i+1, n):
            if gleichungen[k][i] != 0:
                text = (gzahl(gleichungen[k][i]) + r' \cdot ' + zeilennummer.get(i+1, 'zu groß')
                        + vorz_str(-1 * gleichungen[i][i]) + r' \cdot ' + zeilennummer.get(k+1, 'zu groß'))
                neue_zeile = [gleichungen[k][i] * gleichungen[i][step] - gleichungen[i][i] * gleichungen[k][step]
                              for step in range(0, len(gleichungen[0]))]
                gleichungen[k] = neue_zeile
                loesung.append([zeilennummer.get(k+1, 'zu groß'), text] + neue_zeile)

    k = zeilennummer_reverse[loesung[-1][0]]
    gleich_lsg = []
    for anz in range(n, 0, -1):
        gleich_lsg.append(next(e for e in reversed(loesung) if e[0] == zeilennummer[anz]))

    # und hier eine Funktion die aus gleich_lsg den Lösungstext erstellt "aus III folgte c = ..."
    text_lsg = ''
    lsg = []
    for k, tubel in enumerate(gleich_lsg, 1):
        if all(x == 0 for x in tubel[-1 - k:]):
            text_lsg = r' 0~=~0 \mathrm{Das~Gleichungssystem~hat~unendlich~viele~Lösungen} '
            break
        elif all(x == 0 for x in tubel[-1-k: -1]):
            text_lsg = r' 0 ~ \neq ~' + tubel[-1] + r' \mathrm{Das~Gleichungssystem~ist~nicht~lösbar!} '
            break
        else:
            text_lsg = text_lsg + r' \mathrm{aus~ ' + gzahl(tubel[0]) + r'~folgt: } \quad '
            text_zw = '~=~' + gzahl(tubel[-1])
            konst = 0
            trennung = r' \quad \to \quad ' if k <= 3 else r' \\'
            for step in range(len(lsg)):
                text_zw = vorz_str(tubel[-2-step]) + r' \cdot '+ gzahl_klammer(lsg[step]) + text_zw
                konst += tubel[-2-step]*lsg[step]
            text_zw = (vorz_v_aussen(tubel[-1-k], variablen[-k]) + text_zw + umformung(konst,'-')
                       + umformung(tubel[-1-k],':') + trennung + variablen[-k]
                       + '~=~' + gzahl(Rational(tubel[-1] - konst, tubel[-1-k])))
            lsg.append(Rational(tubel[-1] - konst, tubel[-1-k]))
            text_lsg = text_lsg + text_zw + r' \\'
        k += 1

    # Funktion, die loesung als Tabelle darstellt
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

    text = [table1, text_lsg]
    lsg.reverse()
    punkte = len(loesung)
    return text, lsg, punkte

def quadr_gl(koeff, i=1, schnittpkt=False, var='x'):
    n1, n2 = (0 + i, 1 + i)
    punkte = 0
    fkt = koeff[0]*x**2 + koeff[1]*x + koeff[2]
    text = ''
    if all(x == 0 for x in koeff):
        text += r'0 ~=~ 0 ~ w.A. \mathrm{für~alle~' + var + '~aus~dem~Definitionsbereich} '
        lsg = []
        punkte += 1
    elif koeff[0] == 0:
        if koeff[1] == 0:
            text += '0 ~=~ ' + gzahl(koeff[2]) + ' ~ f.A. '
            lsg = []
            punkte += 1
        elif koeff[2] == 0:
            text = (text + ' 0 ~=~ ' + vorz_v_aussen(koeff[1], var) + r' \quad \to \quad ' + var
                    + '_{' + gzahl(n1) + '} ~=~ 0')
            lsg = [0]
            punkte += 2
        else:
            lsg1 = Rational(-1 * koeff[2], koeff[1])
            text = (text + ' 0 ~=~ ' + vorz_v_aussen(koeff[1], var) + vorz_str(koeff[2])
                    + r' \quad \vert ' + vorz_str(-1 * koeff[2]) + r' \quad \vert \div ' + gzahl_klammer(koeff[1])
                    + r' \quad \to \quad ' + var + ' ~=~' + gzahl(lsg1) + r' \\')
            lsg = [lsg1]
            punkte += 2
    elif koeff[1] == 0 and koeff[2] == 0:
        text = (text + ' 0 ~=~ ' + vorz_v_aussen(koeff[0], var + '^2') + r' \quad \to \quad ' + var
                + '_{' + gzahl(n1) + '} ~=~ 0')
        lsg = [0]
        punkte += 2
    elif koeff[2] == 0:
        text = (text + ' 0 ~=~ ' + vorz_v_aussen(koeff[0], var + '^2') + vorz_v_innen(koeff[1],str(var))
                + '~=~' + var + r' \cdot \left( ' + vorz_v_aussen(koeff[0], var) + vorz_str(koeff[1])
                + r' \right) \quad \to \quad ' + var + '_{' + gzahl(n1) + r' } = 0  \quad (2BE) \\ 0 ~=~ f(' + var
                + ') ~=~ ' + vorz_v_aussen(koeff[0], var) + vorz_str(koeff[1]) + r' \quad \vert ' + vorz_str(-1*koeff[1])
                + r' \quad \vert \div ' + gzahl_klammer(koeff[0]) + r' \quad \to \quad ' + var + '_{ ' + gzahl(n2)
                + ' } ~=~ ' + gzahl(Rational(-1*koeff[1], koeff[0])) + '~=~' + gzahl(N(-1*koeff[1]/ koeff[0],3)))
        lsg = [0, Rational(-1*koeff[1], koeff[0])]
        lsg.sort()
        punkte += 4
    elif koeff[1] == 0:
        text = (text + r' 0 ~=~ ' + vorz_v_aussen(koeff[0], var + '^2') + vorz_str(koeff[2]) + r' \quad \vert '
                + vorz_str(-1*koeff[2]) + r' \quad \vert \div ' + gzahl_klammer(koeff[0]) + r' \quad \to \quad '
                + var + '^2 ~=~' + gzahl(Rational(-1*koeff[2],koeff[0])) + r' \vert \sqrt{ ~ } \\')
        punkte += 2
        if Rational(-1*koeff[2],koeff[0]) < 0:
            text = (text + r' ' + var + '_{ ' + gzahl(n1) + ',' + gzahl(n2) + r' } ~=~ \pm \sqrt{ '
                    + gzahl(Rational(-1*koeff[2],koeff[0])) + r' } \quad \mathrm{ n.d. }')
            lsg = []
            punkte += 2
        else:
            disk = Rational(-1 * koeff[2], koeff[0])
            lsg_sq = N(sqrt(-1 * koeff[2]/ koeff[0]),3)
            text = (text + var + '_{' + gzahl(n1) + ',' + gzahl(n2) + r' } ~=~ \pm \sqrt{ ' + gzahl(disk)
                    + r' } \quad \to \quad ' + var + '_{ ' + gzahl(n1) + r'} = \sqrt{ ' + gzahl(disk) + ' } ~=~'
                    + gzahl(lsg_sq) + r' \quad \mathrm{und} \quad ' + var + '_{ ' + gzahl(n2) + r' }= - \sqrt{ '
                    + gzahl(disk) + r' } ~=~' + gzahl(-1*lsg_sq))
            lsg = [-1*lsg_sq, lsg_sq]
            punkte += 1
    else:
        p = Rational(koeff[1], koeff[0])
        q = Rational(koeff[2], koeff[0])
        text = (text + '0 ~=~ ' + vorz_v_aussen(koeff[0], var + '^2') + vorz_v_innen(koeff[1],var) + vorz_str(koeff[2])
                + r' \quad \vert \div ' + gzahl_klammer(koeff[0]) + r' \quad \to \quad '
                + r' 0 ~=~ ' + var + '^2 ' + vorz_v_innen(Rational(koeff[1], koeff[0]), var)
                + vorz_str(Rational(koeff[2], koeff[0])) + r' \quad (2BE) \\'
                + var + '_{' + gzahl(n1) + ',' + gzahl(n2) + r' } ~=~ - \frac{' + gzahl(p) +  r'}{2} \pm \sqrt{ \left( '
                + r' \frac{' + gzahl(p) + r'}{2} \right) ^2 ' + vorz_str(-1*q) + ' } ~=~ '
                + gzahl(Rational(-1*koeff[1],2*koeff[0])) + r' \pm \sqrt{ '
                + gzahl(Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2)) + r'} \quad (2BE) \\ ')
        punkte += 4
        if Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2) < 0:
            text += r' \mathrm{ n.d. }'
            lsg = []
            punkte += 1
        elif Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2) == 0:
            text += var + '_{' + gzahl(n1) + '} ~=~ ' + gzahl(Rational(-1*koeff[1],2*koeff[0]))
            lsg = [Rational(-1*koeff[1], 2*koeff[0])]
            punkte += 2
        else:
            lsg1 = Rational(-1*koeff[1],2*koeff[0]) - sqrt(Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2))
            lsg2 = Rational(-1*koeff[1],2*koeff[0]) + sqrt(Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2))
            text = (text + var + '_{' + gzahl(n1) + '} ~=~ ' + gzahl(Rational(-1*koeff[1],2*koeff[0]))
                    + vorz_str(-1*N(sqrt(Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2)),3))
                    + '~=~' + gzahl(N(lsg1,3)) + r' \quad \mathrm{und} \quad ' + var + '_{' + gzahl(n2) + '} ~=~ '
                    + gzahl(Rational(-1*koeff[1],2*koeff[0]))
                    + vorz_str(N(sqrt(Rational(koeff[1]**2 - 4*koeff[2]*koeff[0], 4*koeff[0]**2)),3))
                    + '~=~' + gzahl(N(lsg2,3)) + r' \quad (2BE) ')
            lsg = [lsg1, lsg2]
            punkte += 2

    if schnittpkt:
        text4 = r' \\'
        k = 1
        y_wert = round(fkt.subs(x, 0),2)
        for element in lsg:
            if element != 0:
                text4 = (text4 + r' \mathrm{ S_{x_{' + gzahl(k) + '}} (' + gzahl(N(element, 3))
                         + r' \vert 0)} \quad ')
            else:
                text4 = (text4 + r' \mathrm{ S_y = S_{x_{' + gzahl(k) + '} } (' + gzahl(N(element, 3))
                         + r' \vert 0 ) } \quad ')
            k += 1
        text4 += r' S_y( 0 \vert ' + gzahl(y_wert) + ')' if all(x != 0 for x in lsg) else ''
        text4 += r' \quad (2BE) '
        punkte += 2


    text = [text]
    return text, lsg, punkte

def hornerschema(koeff, nst=[]):
    if nst == []: # hier werden die ganzzahligen Nullstellen des Polynoms bestimmt, die zum Lösen mit dem Hornerscheme benötigt wedren
        fkt = 0
        n = len(koeff)
        for step in range(len(koeff)):
            fkt = fkt + koeff[step]*x**n
            n -= 1
        lsg = solve(fkt,x)
        nst = [element for element in lsg if element%1 == 0]
        if nst == []:
            exit('Fehler bei der Funktion "hornerschema": Die gegebene Funktion hat keine Nullstellen')
    laenge = len(koeff)
    # Berechnung der Werte für Hornerschema
    nst1 = nst[int(len(nst)/2)]
    zeile1 = ['', ''] + [element for element in koeff]
    zeile2 = ['Berechnung der Partialfunktion  mit Hornerschema: ', nst1,'']
    zeile3 = ['', '', koeff[0]]
    for step in range(len(koeff) - 1):
        zeile2.append(zeile3[step + 2] * nst1)
        zeile3.append(koeff[step + 1] + zeile3[step + 2] * nst1)
    zeilen = [zeile1, zeile2, zeile3]
    # Tabelle Hornerschema
    spalten = 'c|c|'
    for element in koeff:
        spalten = spalten + 'c|'
    table1 = Tabular(spalten, row_height=1.2)
    table1.add_hline(2)
    for zeile in zeilen:
        table1.add_row([gzahl(element) for element in zeile])
        table1.add_hline(2)

    lsg = [zeile3[i+2] for i in range(laenge-1)]
    punkte = len(lsg)

    return table1, lsg, punkte

def kubische_gl(koeff, nst=[], schnittpkt=False):
    fkt = koeff[0]*x**3 + koeff[1]*x**2 + koeff[2]*x + koeff[3]
    fkt_str = (vorz_v_aussen(koeff[0], 'x^3') + vorz_v_innen(koeff[1], 'x^2')
               + vorz_v_innen(koeff[2], 'x') + vorz_str(koeff[3]))
    lsg_float = solve(fkt, x) if nst == [] else nst
    lsg = [N(element,3) for element in lsg_float]
    if koeff[3] == 0:
        if koeff[1]== 0:
            text_quadr, lsg_quadr, punkte_quadr = quadr_gl([koeff[0], 0, koeff[2]])
            fkt_x_ausgekl_str = vorz_v_aussen(koeff[0], 'x^2') + vorz_str(koeff[2])
        else:
            text_quadr, lsg_quadr, punkte_quadr = quadr_gl([koeff[0], koeff[1], koeff[2]])
            fkt_x_ausgekl_str = (vorz_v_aussen(koeff[0], 'x^2') + vorz_v_innen(koeff[1], 'x')
                                 + vorz_str(koeff[2]))
        lsg_quadr.append(0)
        lsg_quadr.sort()
        text = ('0~=~' + fkt_str + r' ~=~ x \cdot (' + fkt_x_ausgekl_str + r') \quad \to \quad x = 0 \quad (2BE) \\ '
                + text_quadr[0])
        punkte = 2 + punkte_quadr
        text = [text]
    else:
        nst = [element for element in lsg if element%1 == 0]
        nst2 = nst[int(len(nst)/2)]
        table1, koeff_hs, pkt_hs = hornerschema(koeff, nst)
        p1, p2, p3 = koeff_hs
        fkt_partial_str = vorz_v_aussen(p1,'x^2') + vorz_v_innen(p2, 'x') + vorz_str(p3)
        text_quadr, lsg_quadr, pkt_quadr = quadr_gl(koeff_hs, i=2)
        text1 = ('0~=~' + fkt_str + r' \quad \mathrm{durch~probieren:~x~=~}' + gzahl(nst2) + r' \quad (2BE) \\' + '('
                 + fkt_str + r')~ \div ~(x' + vorz_str(-1 * nst2) + ')~=~' + fkt_partial_str + r' \quad ('
                 + gzahl(1 + pkt_hs) + 'BE)')
        text2 = (r' \mathrm{Ansatz: \quad p(x) } ~=~ 0 \quad \to \quad ' + text_quadr[0])
        lsg_quadr.append(nst2)
        lsg_quadr.sort()
        punkte = 3 + pkt_hs + pkt_quadr
        text = [text1, table1, text2]

    if schnittpkt:
        text4 = r' \\'
        k = 1
        y_wert = round(fkt.subs(x, 0),2)
        for element in lsg:
            if element == 0:
                text4 = (text4 + r' \mathrm{ S_y = S_{x_{' + gzahl(k) + '} } (' + gzahl(N(element, 3))
                         + r' \vert 0 ) } \quad ')
            else:
                text4 = (text4 + r' \mathrm{ S_{x_{' + gzahl(k) + '}} (' + gzahl(N(element, 3))
                         + r' \vert 0)} \quad ')
                k += 1
        text4 += r' S_y( 0 \vert ' + gzahl(y_wert) + ')' if all(x != 0 for x in lsg) else ''
        text4 += r' \quad (2BE) '
        text[-1] += text4
        punkte += 2

    return text, lsg, punkte