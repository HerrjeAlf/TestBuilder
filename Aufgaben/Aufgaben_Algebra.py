from pylatex import (MediumText)
from pylatex.utils import bold
import string, sys
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *

# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
nr_aufgabe = 0

# Berechnung für die Aufgaben
def punkte_und_vektoren(nr, teilaufg=['a', 'b', 'c']):
    liste_punkte = []
    liste_bez = []
    i = 0

    def zf_vorz(q):
        return random.choice([-1, 1]) * q

    ortsvektor_a = punkt_vektor(3)
    a_x, a_y, a_z = punkt_vektor(4)
    vektor_ab = [a_x, a_y, a_z]
    laenge_vektor_ab = (r' \sqrt{' + gzahl(sum(a*a for a in vektor_ab)) + '}'
                        + '~=~' + gzahl(sqrt(N(sum(a*a for a in vektor_ab),3))))
    ortsvektor_b = np.array(ortsvektor_a) + np.array(vektor_ab)
    vektoren_auswahl = [[zf_vorz(a_x), zf_vorz(a_z), zf_vorz(a_y)],
                        [zf_vorz(a_y), zf_vorz(a_z), zf_vorz(a_x)],
                        [zf_vorz(a_y), zf_vorz(a_x), zf_vorz(a_z)],
                        [zf_vorz(a_z), zf_vorz(a_x), zf_vorz(a_y)],
                        [zf_vorz(a_z), zf_vorz(a_y), zf_vorz(a_x)]]

    if random.random() < 0.5:
        vektor_ac = random.choice(vektoren_auswahl)
        while vektor_ac == vektor_ab:
            vektor_ac = random.choice(vektoren_auswahl)
        laenge_vektor_ac = (r' \sqrt{' + gzahl(sum(a*a for a in vektor_ac)) + '}' + '~=~'
                            + gzahl(sqrt(N(sum(a*a for a in vektor_ac),3))))
        ortsvektor_c = np.array(ortsvektor_a) + np.array(vektor_ac)
        ortsvektor_d = np.array(ortsvektor_a) - np.array(vektor_ab)
        loesung_1 = (r' \overrightarrow{AC} ~=~ \begin{pmatrix}' + gzahl(vektor_ac[0]) + r' \\'
                     + gzahl(vektor_ac[1]) + r' \\' + gzahl(vektor_ac[2]) + r' \\'
                     + r' \end{pmatrix} \to \mathrm{d(A,C)~=~} \sqrt{(' + gzahl(vektor_ac[0]) + ')^2 ~+~('
                     + gzahl(vektor_ac[1]) + ')^2 ~+~(' + gzahl(vektor_ac[2]) + ')^2 } ~=~' + laenge_vektor_ac
                     + r' \quad (3P) \\')
        loesung_2 = (r') \quad \overrightarrow{OD} = \overrightarrow{OC} ~+~ \overrightarrow{BA} ~=~'
                     r' \begin{pmatrix} ' + gzahl(ortsvektor_a[0]) + r' \\' + gzahl(ortsvektor_a[1]) + r' \\'
                     + gzahl(ortsvektor_a[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(-1*vektor_ab[0])
                     + r' \\' + gzahl(-1*vektor_ab[1]) + r' \\' + gzahl(-1*vektor_ab[2]) + r' \\'
                     + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ortsvektor_d[0]) + r' \\'
                     + gzahl(ortsvektor_d[1]) + r' \\' + gzahl(ortsvektor_d[2]) + r' \\'
                     + r'\end{pmatrix}  \quad (3P) \\')

    else:
        vektor_bc = random.choice(vektoren_auswahl)
        while vektor_bc == vektor_ab:
            vektor_bc = random.choice(vektoren_auswahl)
        laenge_vektor_bc = r' \sqrt{' + gzahl(sum(a*a for a in vektor_bc)) + '}' + '~=~' + gzahl(sqrt(N(sum(a*a for a in vektor_bc),3)))
        ortsvektor_c = np.array(ortsvektor_b) + np.array(vektor_bc)
        vektor_ac = np.array(vektor_ab) + np.array(vektor_bc)
        ortsvektor_d = np.array(ortsvektor_a) + np.array(vektor_bc)
        loesung_1 = (r' \overrightarrow{BC} ~=~ \begin{pmatrix}' + gzahl(vektor_bc[0]) + r' \\' + gzahl(vektor_bc[1])
                     + r' \\' + gzahl(vektor_bc[2]) + r' \\' + r' \end{pmatrix} \to \mathrm{d(B,C)~=~} \sqrt{('
                     + gzahl(vektor_bc[0]) + ')^2 ~+~(' + gzahl(vektor_bc[1]) + ')^2 ~+~(' + gzahl(vektor_bc[2])
                     + ')^2 } ~=~' + laenge_vektor_bc + r' \quad (3P) \\')
        loesung_2 = (r') \quad \overrightarrow{OD} = \overrightarrow{OA} ~+~ \overrightarrow{BC} ~=~ '
                     + r' \begin{pmatrix} ' + gzahl(ortsvektor_a[0]) + r' \\' + gzahl(ortsvektor_a[1]) + r' \\'
                     + gzahl(ortsvektor_a[2]) + r' \\' + r' \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(vektor_bc[0])
                     + r' \\' + gzahl(vektor_bc[1]) + r' \\' + gzahl(vektor_bc[2]) + r' \\'
                     + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ortsvektor_d[0]) + r' \\'
                     + gzahl(ortsvektor_d[1]) + r' \\' + gzahl(ortsvektor_d[2]) + r' \\'
                     + r'\end{pmatrix}  \quad (3P) \\')

    print('a = ' + str(ortsvektor_a)), print('b = ' + str(ortsvektor_b)), print('c = ' + str(ortsvektor_c))
    print('d=' + str(ortsvektor_d)), print(vektor_ab), print(vektor_ac)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
               'A( ' + gzahl(ortsvektor_a[0])  + ' | ' + gzahl(ortsvektor_a[1]) + ' | ' + gzahl(ortsvektor_a[2]) + ' ), ' 
               'B( ' + gzahl(ortsvektor_b[0])  + ' | ' + gzahl(ortsvektor_b[1]) + ' | ' + gzahl(ortsvektor_b[2]) + ' ) und ' 
               'C( ' + gzahl(ortsvektor_c[0])  + ' | ' + gzahl(ortsvektor_c[1]) + ' | ' + gzahl(ortsvektor_c[2]) + ' ). \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(teilaufg[i]) + f') Zeichnen Sie das Dreieck ABC im Koordinatensystem ein. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Punkte~(1P),~Seiten~vom~Dreieck~(1P)}')
        liste_punkte.append(2)
        i +=1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 7
        aufgabe.append(str(teilaufg[i]) + f') Weisen Sie nach, dass das Dreieck ABC gleichschenklig ist. \n\n')
        loesung.append(str(teilaufg[i]) + (r') \quad ~ \overrightarrow{AB} ~=~ \begin{pmatrix}'
                                           + gzahl(vektor_ab[0]) + r' \\' + gzahl(vektor_ab[1]) + r' \\'
                                           + gzahl(vektor_ab[2]) + r' \\ \end{pmatrix} \to \mathrm{d(A,B)~=~} \sqrt{('
                                           + gzahl(vektor_ab[0]) + ')^2 ~+~(' + gzahl(vektor_ab[1]) + ')^2 ~+~('
                                           + gzahl(vektor_ab[2]) + ')^2 } ~=~' + laenge_vektor_ab + r' \quad (3P) \\'
                                           + loesung_1 + r' \mathrm{Die~beiden~Seiten~sind~gleichlang,'
                                           + r'~somit~ist~das~Dreieck~gleichschenklig.} \quad (1P) \\'
                                           + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'))

        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 7
        aufgabe.append(str(teilaufg[i]) + (f') Bestimmen Sie einen Punkt D so, dass die Punkte A,B,C und D'
                                           + f' ein Parallelogramm bilden. \n\n'))
        loesung.append(str(teilaufg[i]) + loesung_2 + r' \mathrm{Punkt~D~hat~die~Koordinaten:~}~D('
                       + gzahl(ortsvektor_d[0]) + ' | ' + gzahl(ortsvektor_d[1]) + ' | ' + gzahl(ortsvektor_d[2])
                       + r') \quad (1P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rechnen_mit_vektoren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], linearkombination=None, kollinear=None):
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        vektor_1 = punkt_vektor(5)
        vektor_2 = punkt_vektor(7)
        faktor_1, faktor_2 = zzahl(2,8),zzahl(2,5)
        ergebnis = faktor_1 * np.array(vektor_1) + faktor_2 * np.array(vektor_2)
        aufgabe.append(str(teilaufg[i]) + f') Berechnen Sie den resultierenden Vektor.')
        aufgabe.append(gzahl(faktor_1) + r' \cdot \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\'
                       + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~'
                       + vorz_str(faktor_2) + r' \cdot' + r'\begin{pmatrix} ' + gzahl(vektor_2[0]) + r' \\'
                       + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                       + r' \end{pmatrix} ~=~ \hspace{20em} \\')
        loesung.append(str(teilaufg[i]) + r') \quad ' + gzahl(faktor_1) + r'\cdot \begin{pmatrix} ' + gzahl(vektor_1[0])
                       + r' \\' + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~'
                       + vorz_str(faktor_2) + r' \cdot' + r'\begin{pmatrix} ' + gzahl(vektor_2[0]) + r' \\'
                       + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} '
                       + gzahl(ergebnis[0]) + r' \\' + gzahl(ergebnis[1]) + r' \\' + gzahl(ergebnis[2]) + r' \\'
                       + r'\end{pmatrix}  \quad (2P)')
        liste_punkte.append(2)
        i += 1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        vektor_1 = punkt_vektor(5)
        vektor_2 = punkt_vektor(7)
        ergebnis = 0.5 * (np.array(vektor_1) + np.array(vektor_2))
        print(ergebnis)
        punkte = 3

        aufgabe.append(str(teilaufg[i]) + ') Berechnen Sie den Mittelpunkt der folgenden Punkte '
                       'A( ' + gzahl(vektor_1[0])  + ' | ' + gzahl(vektor_1[1]) + ' | ' + gzahl(vektor_1[2]) + ' ) und '
                       'B( ' + gzahl(vektor_2[0])  + ' | ' + gzahl(vektor_2[1]) + ' | ' + gzahl(vektor_2[2])
                       + ' ). \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{OM} ~=~ \frac{1}{2} \cdot \begin{pmatrix}'
                       + r'\begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\' + gzahl(vektor_1[1]) + r' \\'
                       + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(vektor_2[0])
                       + r' \\' + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                       + r' \end{pmatrix} \end{pmatrix}  ~=~ \begin{pmatrix}' + gzahl(ergebnis[0]) + r' \\'
                       + gzahl(ergebnis[1]) + r' \\' + gzahl(ergebnis[2]) + r' \\'
                       + r' \end{pmatrix} \quad (2P) \\ \mathrm{Punkt~D~hat~die~Koordinaten:~}~M('
                       + gzahl(ergebnis[0]) + ' | ' + gzahl(ergebnis[1]) + ' | ' + gzahl(ergebnis[2])
                       + r') \quad (1P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        faktor_1, faktor_2 = random.randint(1,10)/2, random.randint(1,10)/2
        print('r =' + gzahl(faktor_1))
        print('s =' + gzahl(faktor_2))
        vektor_2 = [x_2, y_2, z_2] = np.array(punkt_vektor(5))
        vektor_3 = [x_3, y_3, z_3] = np.array([zzahl(1,7), zzahl(0,5),zzahl(1,7)])

        if linearkombination == None:
            linearkombination = random.choice([True,False])

        if linearkombination == True:
            vektor_1 = [x_1, y_1, z_1] = np.array(vektor_2*faktor_1) + np.array(vektor_3*faktor_2)
            loesung_2 = (r' \mathrm{w.A. \quad \to \quad Vektor~ \overrightarrow{a} ~lässt~sich~als~Linearkombination~'
                         r'von~ \overrightarrow{b} ~und~ \overrightarrow{c} ~darstellen.} \quad (1P) \\')
        else:
            vektor_1 = [x_1, y_1, z_1] = (vektor_2[0] * faktor_1 + vektor_3[0] * faktor_2,
                                          vektor_2[1] * faktor_1 + vektor_3[1] * faktor_2,
                                          vektor_2[2] * faktor_1 + vektor_3[2] * faktor_2 + zzahl(1,3))
            loesung_2 = (r' \mathrm{f.A. \quad \to \quad Vektor~ \overrightarrow{a} ~lässt~sich~nicht~als~'
                         r' Linearkombination~von~ \overrightarrow{b} ~und~ \overrightarrow{c} ~darstellen.}'
                         r' \quad (1P) \\')

        aufgabe.extend((str(teilaufg[i]) + ') Überprüfen Sie, ob der gegebenen Vektor a als Linearkombination'
                        + ' von b und c dargestellt werden kann.',
                        r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(x_1) + r' \\' + gzahl(y_1) + r' \\'
                        + gzahl(z_1) + r' \\' + r' \end{pmatrix} ~,~ \overrightarrow{b} ~=~ \begin{pmatrix} '
                        + gzahl(x_2) + r' \\' + gzahl(y_2) + r' \\' + gzahl(z_2) + r' \\'
                        + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{c} ~=~\begin{pmatrix}'
                        + gzahl(x_3) + r' \\' + gzahl(y_3) + r' \\' + gzahl(z_3) + r' \\'
                        + r' \end{pmatrix} \\'))

        loesung_1 = (r' \mathrm{aus~I~folgt:} \quad ' + gzahl(x_1) + '~=~' + gzahl(x_2) + r' \cdot r'
                     + vorz_str(x_3) + r's \cdot \quad \to \quad r~=~'
                     + gzahl(Rational(x_1,x_2)) + vorz_str(Rational(-1*x_3,x_2))
                     + r' \cdot s \quad (2P) \\')

        if y_3 != 0:
            lsg_s = N((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2),3)
            lsg_r = N((x_1 / x_2) - (x_3/ x_2) * ((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2)),3)
            print(lsg_r)
            print(lsg_s)
            loesung_1 = (loesung_1 + r' \mathrm{r~einsetzen~in~II} \quad ' + gzahl(y_1) + '~=~'
                         + gzahl(y_2) + r' \cdot \Big(' + gzahl(Rational(x_1,x_2))
                         + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \Big)'
                         + vorz_str(y_3) + r' \cdot s \quad (1P) \\'
                         + gzahl(y_1) + vorz_str(Rational(-1*x_1*y_2,x_2)) + r' ~=~ s \cdot \Big('
                         + gzahl(Rational(-1*x_3*y_2,x_2)) + vorz_str(y_3)
                         + r' \Big) \quad (1P) \quad \to \quad'
                         + r' s ~=~ ' + gzahl(lsg_s) + r' \quad (1P) \quad \to \quad r ~=~' + gzahl(lsg_r)
                         + r' \quad (1P) \\ \mathrm{Einsetzen~in~III: ' + gzahl(z_1) + '~=~' + gzahl(lsg_r)
                         + r' \cdot ' + gzahl_klammer(z_2) + vorz_str(lsg_s) + r' \cdot ' + gzahl_klammer(z_3)
                         + r' ~=~ ' + gzahl(N(z_2*lsg_r+z_3*lsg_s,3)) + r'} \quad (1P)')
        elif z_3 != 0:
            lsg_r = N(Rational((z_1 - (x_1*z_2)/x_2),(z_3 - (x_3*z_2)/x_2)),3)
            lsg_s = N(x_1 / x_2 - (x_3/ x_2)*((z_1 + (x_1*z_2)/x_2)/(z_3 - (x_3*z_2)/x_2)),3)
            print(lsg_r)
            print(lsg_s)
            loesung_1 = (loesung_1 + r' \mathrm{r~einsetzen~in~III} \quad ' + gzahl(z_1) + '~=~'
                         + gzahl(z_2) + r' \cdot \Big(' + gzahl(Rational(x_1,x_2))
                         + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \Big)'
                         + vorz_str(z_3) + r' \cdot s \quad (2P) \\'
                         + gzahl(z_1) + vorz_str(Rational(-1* x_1*z_2,x_2)) + r' ~=~ s \cdot \Big('
                         + gzahl(Rational(-1*x_3*z_2,x_2)) + vorz_str(z_3)
                         + r' \cdot s \Big) \quad (2P) \quad \to \quad'
                         + r' s ~=~ ' + gzahl(Rational((z_1 - (x_1*z_2)/x_2),(z_3 - (x_3*z_2)/x_2)))
                         + r' \quad (1P) \quad  r~=~ '
                         + gzahl(N(x_1 / x_2 - (x_3/ x_2)*((z_1 + (x_1*z_2)/x_2)/(z_3 - (x_3*z_2)/x_2)),3))
                         + r' \quad (1P) \\ \mathrm{Einsetzen~in~II: ' + gzahl(y_1) + '~=~' + gzahl(lsg_r)
                         + r' \cdot ' + gzahl_klammer(y_2) + vorz_str(lsg_s) + r' \cdot ' + gzahl_klammer(y_3)
                         + r' ~=~ ' + gzahl(N(y_2*lsg_r+y_3*lsg_s,3)) + r'} \quad (1P)')
        else:
            pass

        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Überprüfe,~ob~der~gegebenen~Vektor~a~als~Linearkombination'
                       + r'~von~b~und~c~dargestellt~werden~kann.} \\' + r' \begin{pmatrix} ' + gzahl(x_1) + r' \\'
                       + gzahl(y_1) + r' \\' + gzahl(z_1) + r' \\' + r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                       + gzahl(x_2) + r' \\' + gzahl(y_2) + r' \\' + gzahl(z_2) + r' \\'
                       + r' \end{pmatrix}  ~+~s \cdot \begin{pmatrix}' + gzahl(x_3) + r' \\' + gzahl(y_3) + r' \\'
                       + gzahl(z_3) + r' \\' + r' \end{pmatrix} \quad (1P) \\' + loesung_1 + r' \\' + loesung_2
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        vektor_2 = punkt_vektor(5)
        faktor = zzahl(2, 40) / 10
        punkte = 4

        if kollinear == None:
            kollinear = random.choice([True,False])

        if kollinear == True:
            faktor = zzahl(2,40)/5
            vektor_1 = (faktor * vektor_2[0],faktor * vektor_2[1],faktor * vektor_2[2])
            ergebnis = r' \mathrm{Die~Vektoren~sind~kollinear.} '
        else:
            vektor_1 = (vektor_2[0]*zzahl(1,6)/2,vektor_2[1]*zzahl(3,8)/2,vektor_2[2]*zzahl(5,10)/2)
            ergebnis = r' \mathrm{Die~Vektoren~sind~nicht~kollinear.} '

        aufgabe.extend((str(teilaufg[i]) + f') Prüfen Sie, ob die gegebenen Vektoren kollinear sind.',
                        r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\'
                        + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\'
                        + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{b} ~=~ \begin{pmatrix} '
                        + gzahl(vektor_2[0]) + r' \\' + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                        + r' \end{pmatrix} \\'))
        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Prüfen~Sie,~ob~die~gegebenen~Vektoren~kollinear~sind.} \\'
                       + gzahl(N(vektor_1[0],3)) + '~=~' + gzahl(vektor_2[0]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[0]/vektor_2[0],3)) + r' \\' + gzahl(N(vektor_1[1],3)) + '~=~'
                       + gzahl(vektor_2[1]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[1]/vektor_2[1],3)) + r' \\' + gzahl(N(vektor_1[2],3)) + '~=~'
                       + gzahl(vektor_2[2]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[2]/vektor_2[2],3)) + r' \\' + ergebnis
                       + r' \quad \to \quad \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        vektor_a = punkt_vektor(5)
        vektor_ab = punkt_vektor(5)
        vektor_b = np.array(vektor_a) + np.array(vektor_ab)
        faktor = nzahl(1,9)/10
        vektor_t = [N(vektor_a[0] + vektor_ab[0]*faktor,3),
                    N(vektor_a[1] + vektor_ab[1]*faktor,3),
                    N(vektor_a[2] + vektor_ab[2]*faktor,3)]
        vektor_at = np.array(vektor_t) - np.array(vektor_a)
        vektor_tb = vektor_b - np.array(vektor_t)
        laenge_vektor_at = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_at),4)) + '} ~=~'
                            + gzahl(sqrt(N(sum(a*a for a in vektor_at),3))))
        ergebnis_at = sqrt(N(sum(a*a for a in vektor_at),3))
        laenge_vektor_tb = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_tb),3)) + '} ~=~'
                            + gzahl(N(sqrt(sum(a*a for a in vektor_tb)),3)))
        ergebnis_tb = sqrt(N(sum(a*a for a in vektor_tb),3))
        aufgabe.append(str(teilaufg[i]) + ') In welchem Verhältnis teilt der Punkt T die Strecke AB?')
        aufgabe.append(r' \mathrm{A(~' + gzahl(vektor_a[0]) + r'~ \vert ~' + gzahl(vektor_a[1]) + r'~ \vert ~'
                       + gzahl(vektor_a[2]) + r'~ ), \quad B(~' + gzahl(vektor_b[0]) + r'~ \vert ~' + gzahl(vektor_b[1])
                       + r'~ \vert ~' + gzahl(vektor_b[2]) + r'~) \quad und \quad T( ~' + gzahl(N(vektor_t[0],3))
                       + r'~ \vert ~' + gzahl(N(vektor_t[1],3)) + r'~ \vert ~' + gzahl(N(vektor_t[2],3))
                       + r'~ ).} \\')
        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{d(A,T)~=~} \sqrt{(' + gzahl(vektor_t[0]) + vorz_str(-1*vektor_a[0])
                       + ')^2 ~+~(' + gzahl(vektor_t[1]) + vorz_str(-1*vektor_a[1]) + ')^2 ~+~(' + gzahl(vektor_t[2])
                       + vorz_str(-1*vektor_a[2]) + ')^2 } ~=~' + laenge_vektor_at + r' \quad (2P) \\'
                       + r' \mathrm{d(T,B)~=~} \sqrt{(' + gzahl(vektor_b[0]) + vorz_str(-1*vektor_t[0])
                       + ')^2 ~+~(' + gzahl(vektor_b[1]) + vorz_str(-1*vektor_t[1]) + ')^2 ~+~(' + gzahl(vektor_b[2])
                       + vorz_str(-1*vektor_t[2]) + ')^2 } ~=~' + laenge_vektor_tb + r' \quad (2P) \\'
                       + r' r~=~ \frac{ ' + gzahl(ergebnis_at) + '}{' + gzahl(ergebnis_tb) + '} ~=~'
                       + gzahl(ergebnis_at/ergebnis_tb) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        vektor_a = punkt_vektor(5)
        vektor_b = np.array(vektor_a) + np.array(punkt_vektor(5))
        vektor_ab = vektor_b - np.array(vektor_a)
        a1 = nzahl(1,9)
        faktor = a1/10
        vektor_t = np.array(vektor_a) + faktor * vektor_ab
        vektor_at = vektor_t - np.array(vektor_a)
        vektor_tb = vektor_b - vektor_t
        laenge_vektor_at = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_at),3)) + '} ~=~'
                            + gzahl(N(sqrt(sum(a*a for a in vektor_at)),3)))
        laenge_vektor_tb = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_tb),4)) + '} ~=~'
                            + gzahl(sqrt(N(sum(a*a for a in vektor_tb),3))))
        faktor_r = Rational(a1,(10-a1))
        aufgabe.append(str(teilaufg[i]) + ') Der Punkt T teilt die Strecke AB im Verhältnis r. Bestimme den Punkt B.')
        aufgabe.append(r' \mathrm{A(~' + gzahl(vektor_a[0]) + r'~ \vert ~' + gzahl(vektor_a[1]) + r'~ \vert ~'
                       + gzahl(vektor_a[2]) + r'~), \quad T(~' + gzahl(vektor_t[0]) + r'~ \vert ~' + gzahl(vektor_t[1])
                       + r'~ \vert ~' + gzahl(vektor_t[2]) + r'~) \quad und~r~=~' + gzahl(faktor_r) + r'.} \\')
        loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{OB} = \overrightarrow{OA} ~+~ \overrightarrow{AT} '
                       + r' \cdot \mathrm{ (~1~+~ \frac{1}{r} ~)}  ~=~ \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
                       + gzahl(vektor_a[1]) + r' \\' + gzahl(vektor_a[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} '
                       + gzahl(N(vektor_at[0],3))+ r' \\' + gzahl(N(vektor_at[1],3)) + r' \\'
                       + gzahl(N(vektor_at[2],3)) + r' \\ \end{pmatrix} \cdot \Big( ~1~+~ '
                       + gzahl(Rational(10-a1,a1)) + r' \Big) \\ ~=~ \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
                       + gzahl(vektor_a[1]) + r' \\' + gzahl(vektor_a[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} '
                       + gzahl(N(vektor_at[0]*(1+(10-a1)/a1),3)) + r' \\'
                       + gzahl(N(vektor_at[1]*(1+(10-a1)/a1),3)) + r' \\'
                       + gzahl(N(vektor_at[2]*(1+(10-a1)/a1),3)) + r' \\'
                       + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(N(vektor_b[0],3)) + r' \\'
                       + gzahl(N(vektor_b[1],3)) + r' \\' + gzahl(N(vektor_b[2],3)) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad B(~' + gzahl(vektor_b[0]) + r'~ \vert ~' + gzahl(vektor_b[1])
                       + r'~ \vert ~' + gzahl(vektor_b[2]) + r' ~) \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_aufstellen(nr, teilaufg=['a', 'b'], T_auf_g=None):
    liste_punkte = []
    liste_bez = []
    i = 0
    punkt_a = [ax, ay, az] = punkt_vektor(3)
    punkt_b = [bx, by, bz] = punkt_a + punkt_vektor(3)
    v = [vx, vy, vz] = vektor_ganzzahl((punkt_b) - (punkt_a))
    p = random.choice([0,1])
    if T_auf_g == None:
        T_auf_g = random.choice([True,False])
    if T_auf_g == True:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,30)/5)*v)
    else:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,30)/5)*v + [1, 1, 1])

    lx, ly, lz = vektor_ganzzahl([(tx-ax)/vx, (ty-ay)/vy, (tz-az)/vz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
               'A( ' + gzahl(ax)  + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
               'B( ' + gzahl(bx)  + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
               'T( ' + gzahl(N(tx,3))  + ' | ' + gzahl(N(ty,3)) + ' | ' + gzahl(N(tz,3)) + ' ).  \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 3
        liste_punkte.append(punkte_aufg)
        loesung_1 = (r' \overrightarrow{AB} ~=~'
                     r' \begin{pmatrix} '
                     + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\' + gzahl(v[2]) + r' \\'
                     r' \end{pmatrix} \quad \to \quad '
                     r' g: \overrightarrow{x} \ ~=~'
                     r' \begin{pmatrix} '
                     + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\' + gzahl(v[2]) + r' \\'
                     r' \end{pmatrix} \quad (3P) \\')

        aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                          f' welche die Punkte A und B enthält. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i +=1

    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 4
        liste_punkte.append(punkte_aufg)
        loesung_1 =  (r' \begin{pmatrix} '
                     + gzahl(N(tx,3)) + r' \\' + gzahl(N(ty,3)) + r' \\' + gzahl(N(tz,3)) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                     r' \end{pmatrix} \to \begin{matrix} '
                     + gzahl(N(tx,3)) + '~=~' + gzahl(ax) + vorz_str(vx) + r' \cdot r' + r' \\'
                     + gzahl(N(ty,3)) + '~=~' + gzahl(ay) + vorz_str(vy) + r' \cdot r' + r' \\'
                     + gzahl(N(tz,3)) + '~=~' + gzahl(az) + vorz_str(vz) + r' \cdot r' + r' \\'
                     r' \end{matrix} \quad \to \quad \begin{matrix} '
                     + 'r=' + gzahl(N(lx,3)) + r' \\' + 'r=' + gzahl(N(ly,3)) + r' \\'
                     + 'r=' + gzahl(N(lz,3)) + r' \\'
                     r' \end{matrix} \\')
        if lx == ly == lz:
            loesung_2 = r' \mathrm{Der~Punkt~liegt~auf~der~Geraden.} \quad (4P) \\'
        else:
            loesung_2 = r' \mathrm{Der~Punkt~liegt~nicht~auf~der~Geraden.} \quad (4P) \\'

        aufgabe.append(str(teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T auf g liegt. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1 + loesung_2
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i +=1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_lagebeziehung(nr, teilaufg=['a', 'b'], lagebeziehung=None):
    liste_punkte = []
    liste_bez = []
    i = 0
    if lagebeziehung not in ['identisch', 'parallel', 'windschief', 'schneiden', None]:
        sys.exit("Lagebeziehung muss 'identisch' , 'parallel', 'windschief', 'schneiden', oder None sein")
    v_teiler = zzahl(1, 3)
    punkt_a = [ax, ay, az] = punkt_vektor(3) # Punkt A liegt auf Gerade g_1
    v = [vx, vy, vz] = vektor_ganzzahl([zzahl(1, 6) / 2 * v_teiler,
                                        zzahl(1, 6) / 2 * v_teiler, v_teiler]) # Vektor v ist der Richtungsvektor von Geraden g_1
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    uz = - 1 * (vx*ux + vy * uy)/vz
    u = vektor_ganzzahl([ux, uy, uz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Gegeben sind die beiden Geraden mit folgenden Gleichungen:']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if lagebeziehung == None:
            lagebeziehung = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
        if lagebeziehung == 'identisch':
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            punkt_c = [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(v)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10 * np.array(v)) # Vektor w ist der Richtungsvektor von h
            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'\begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3P) \\\\'
                         r' \mathrm{Überprüfen~ob~Stützvektor~von~g~auf~h~liegt.} \hspace{15em} \\'
                         r' \begin{pmatrix} '
                         + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                         r' \end{pmatrix} ~=~ \begin{pmatrix} '
                         + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         + gzahl(ax) + '~=~' + gzahl(cx) + vorz_str(wx) + r' \cdot r' + r' \\'
                         + gzahl(ay) + '~=~' + gzahl(cy) + vorz_str(wy) + r' \cdot r' + r' \\'
                         + gzahl(az) + '~=~' + gzahl(cz) + vorz_str(wz) + r' \cdot r' + r' \\'
                         r' \end{matrix} \quad \to \quad \begin{matrix} '
                         + 'r=' + gzahl(N((ax-cx)/wx,3)) + r' \\' + 'r=' + gzahl(N((ay-cy)/wy,3)) + r' \\'
                         + 'r=' + gzahl(N((az-cz)/wz,3)) + r' \\ \end{matrix} \\'
                         r' \mathrm{Die~Geraden~g~und~h~sind~identisch.} \quad (4P) \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        elif lagebeziehung == 'parallel':
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            punkt_c =  [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(u)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'\begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3P) \\\\'
                         r' \mathrm{Überprüfen~ob~Stützvektor~von~g~auf~h~liegt.} \hspace{15em} \\'
                         r' \begin{pmatrix} '
                         + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                         r' \end{pmatrix} ~=~ \begin{pmatrix} '
                         + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         + gzahl(ax) + '~=~' + gzahl(cx) + vorz_str(wx) + r' \cdot r' + r' \\'
                         + gzahl(ay) + '~=~' + gzahl(cy) + vorz_str(wy) + r' \cdot r' + r' \\'
                         + gzahl(az) + '~=~' + gzahl(cz) + vorz_str(wz) + r' \cdot r' + r' \\'
                         r' \end{matrix} \quad \to \quad \begin{matrix} '
                         + 'r=' + gzahl(N((ax-cx)/wx,3)) + r' \\' + 'r=' + gzahl(N((ay-cy)/wy,3)) + r' \\'
                         + 'r=' + gzahl(N((az-cz)/wz,3)) + r' \\ \end{matrix} \\'
                         r' \mathrm{Die~Geraden~g~und~h~sind~echt~parallel.} \quad (4P) \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        elif lagebeziehung == 'windschief':
            punkte_aufg = 15
            liste_punkte.append(punkte_aufg)
            punkt_c =  [cx,cy,cz] = vektor_ganzzahl((punkt_a) + nzahl(1,6)/2 * np.array(u)) # Punkte C und D liegen auf h
            punkt_d =  [dx,dy,dz] = vektor_ganzzahl((punkt_c) - nzahl(1,6)/2
                                                    * np.cross(np.array(u),np.array(v)))
            w = [wx, wy, wz] = vektor_ganzzahl(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            lsgr = -1*(ax*wy-ay*wx-cx*wy+cy*wx)/(vx*wy-vy*wx)
            lsgs = (-1*(ax*vy)/(vx*wy-vy*wx))+((ay*vx)/(vx*wy-vy*wx))+((cx*vy)/(vx*wy-vy*wx))-((cy*vx)/(vx*wy-vy*wx))
            if vx != 0 and wx != 0:
                loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                             + gzahl(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1*cx)
                             + r' ~ \vert \div ' + gzahl_klammer(wx) + r' \quad \to \quad s ~=~ '
                             + gzahl(N((ax-cx)/wx,3)) + vorz_str(N(vx/wx,3)) + r' \cdot r \quad (2P) \\')
                if vy != 0 and wy != 0:
                    loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                 + gzahl(cy) + vorz_str(wy) + r' \cdot \big( ' + gzahl(N((ax-cx)/wx,3))
                                 + vorz_str(N(vx/wx,3)) + r' \cdot r \big) \\'
                                 + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + gzahl(N((wx*cy + wy*(ax - cx))/wx,3))
                                 + vorz_str(N(wy*vx/wx,3)) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1*vy) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1*N((wx*cy + wy*(ax - cx))/wx,3)) + r' \quad (2P) \\'
                                 + gzahl(N(ay-(wx*cy+wy*(ax-cx))/wx,3)) + '~=~' + gzahl(N((vx*wy-vy*wx)/wx,3))
                                 + r' \cdot r \quad \vert \div ' + gzahl_klammer(N((vx*wy-vy*wx)/wx,3))
                                 + r' \quad \to \quad r~=~' + gzahl(N(lsgr,3))
                                 + r' \quad \mathrm{und} \quad s ~=~'
                                 + gzahl(N(lsgs,3)) + r' \quad (3P) \\')
                    if vz != 0 and wz != 0:
                        loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + gzahl(az) + vorz_str(vz)
                                     + r' \cdot (' + gzahl(N(lsgr,3)) + r') ~=~ ' + gzahl(cz) + vorz_str(wz)
                                     + r' \cdot (' + gzahl(N(lsgs,3)) + r') \quad \to \quad ' + gzahl(N(az+vz*lsgr,3))
                                     + '~=~' + gzahl(N(cz+wz*lsgs,3))
                                     + r' \quad (2P) \\ \to \mathrm{Widerspruch} ~ \to ~ '
                                       r'\mathrm{Die~Geraden~sind~Windschief.} \quad (1P)')
                    else:
                        sys.exit('vz oder wz ist null.')
                else:
                    sys.exit('vy oder wy ist null.')
            else:
                sys.exit('va oder wa ist null.')


            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'\begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3P) \\\\'
                         r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g~=~h} \hspace{5em} \\'
                         r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ \begin{pmatrix} '
                         + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                         r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                         'I: ~~' + gzahl(ax) + vorz_str(vx) + r' \cdot r ~=~' + r' \\'
                         'II: ~' + gzahl(ay) + vorz_str(vy) + r' \cdot r ~=~' + r' \\'
                         'III: ~' + gzahl(az) + vorz_str(vz) + r' \cdot r~=~' + r' \\'
                         r' \end{matrix} \begin{matrix} '
                         + gzahl(cx) + vorz_str(wx) + r' \cdot s' + r' \\'
                         + gzahl(cy) + vorz_str(wy) + r' \cdot s' + r' \\'
                         + gzahl(cz) + vorz_str(wz) + r' \cdot s' + r' \\'
                         r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4 + r' \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')


        else:
            punkte_aufg = 17
            liste_punkte.append(punkte_aufg)
            punkt_d =  [dx,dy,dz] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v)) # Punkte C und D liegen auf h
            punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(u))
            w = vektor_ganzzahl(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            [wx, wy, wz] = vektor_ganzzahl(vektor_runden(w,3))
            lsgr = -1 * (ax * wy - ay * wx - cx * wy + cy * wx) / (vx * wy - vy * wx)
            lsgs = (-1*(ax*vy)+(ay*vx)+(cx*vy)-(cy*vx))/(vx*wy-vy*wx)
            schnittpunkt_s = punkt_c + lsgs*w
            [sx, sy, sz] = vektor_ganzzahl(vektor_runden(schnittpunkt_s,3))
            if vx != 0 and wx != 0:
                loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                             + gzahl(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1 * cx)
                             + r' ~ \vert \div ' + gzahl_klammer(wx) + r' \quad \to \quad s ~=~ '
                             + gzahl(N((ax - cx) / wx, 3)) + vorz_str(N(vx / wx, 3)) + r' \cdot r \quad (2P) \\')
                if vy != 0 and wy != 0:
                    loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                 + gzahl(cy) + vorz_str(wy) + r' \cdot \big( ' + gzahl(N((ax - cx) / wx, 3))
                                 + vorz_str(N(vx / wx, 3)) + r' \cdot r \big) \\'
                                 + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + gzahl(N((wx * cy + wy * (ax - cx)) / wx, 3))
                                 + vorz_str(N(wy * vx / wx, 3)) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1 * vy) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1 * N((wx * cy + wy * (ax - cx)) / wx, 3)) + r' \quad (2P) \\'
                                 + gzahl(N(ay - (wx * cy + wy * (ax - cx)) / wx, 3)) + '~=~'
                                 + gzahl(N((vx * wy - vy * wx) / wx, 3)) + r' \cdot r \quad \vert \div '
                                 + gzahl_klammer(N((vx * wy - vy * wx) / wx, 3))
                                 + r' \quad \to \quad r~=~' + gzahl(N(lsgr, 3))
                                 + r' \quad \mathrm{und} \quad s ~=~'
                                 + gzahl(N(lsgs, 3)) + r' \quad (3P) \\')
                    if vz != 0 and wz != 0:
                        loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + gzahl(az) + vorz_str(vz)
                                     + r' \cdot (' + gzahl(N(lsgr, 3)) + r') ~=~ ' + gzahl(cz) + vorz_str(wz)
                                     + r' \cdot (' + gzahl(N(lsgs, 3)) + r') \quad \to \quad ' + gzahl(N(az + vz * lsgr, 3))
                                     + '~=~' + gzahl(N(cz + wz * lsgs, 3))
                                     + r' \quad (2P) \\ \to \mathrm{wahre~Aussage} ~ \to ~ '
                                       r'\mathrm{Die~Geraden~schneiden~sich~in~S(' + str(sx) + r' \vert '
                                     + str(sy) + r' \vert ' + str(sz) + r').} \quad (2P)')
                    else:
                        sys.exit('vz oder wz ist null.')
                else:
                    sys.exit('vy oder wy ist null.')
            else:
                sys.exit('va oder wa ist null.')


            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'\begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3P) \\\\'
                         r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g~=~h} \hspace{5em} \\'
                         r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ \begin{pmatrix} '
                         + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                         r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                         'I: ~~' + gzahl(ax) + vorz_str(vx) + r' \cdot r ~=~' + r' \\'
                         'II: ~' + gzahl(ay) + vorz_str(vy) + r' \cdot r ~=~' + r' \\'
                         'III: ~' + gzahl(az) + vorz_str(vz) + r' \cdot r~=~' + r' \\'
                         r' \end{matrix} \begin{matrix} '
                         + gzahl(cx) + vorz_str(wx) + r' \cdot s' + r' \\'
                         + gzahl(cy) + vorz_str(wy) + r' \cdot s' + r' \\'
                         + gzahl(cz) + vorz_str(wz) + r' \cdot s' + r' \\'
                         r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4 + r' \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')

            # print(v), print(w), print(punkt_c)

        aufgabe.append(r'g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad h: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                       r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                       + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                       r' \end{pmatrix}\\')
        aufgabe.append(str(teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \mathit{Die~Auswahl~war~' + lagebeziehung + r'} \hspace{25em} \\'
                       + loesung_1)
        i += 1


    if 'b' in teilaufg:
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 7
        liste_punkte.append(punkte_aufg)
        punkt_f =  [fx,fy,fz] = vektor_ganzzahl(np.array(punkt_a) + zzahl(1, 7) / 2 * np.array(v)) # Punkte C und D liegen auf h
        punkt_e =  [ex,ey,ez] = vektor_ganzzahl(np.array(punkt_f) - nzahl(1,7) / 2 * np.array(punkt_vektor(4)))
        p = vektor_ganzzahl(np.array(punkt_f) - np.array(punkt_e)) # Vektor w ist der Richtungsvektor von h
        [px, py, pz] = vektor_ganzzahl(vektor_runden(p, 3))
        sp_vp = np.vdot(v,p)
        l_v = np.linalg.norm(v)
        l_p = np.linalg.norm(p)

        aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
        aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
               r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
               + gzahl(px) + r' \\' + gzahl(py) + r' \\' + gzahl(pz) + r' \\'
               r' \end{pmatrix} \quad ')
        aufgabe.append(str(teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad cos( \gamma ) = \frac{ \vert \overrightarrow{v}'
                       r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                       r' \vert \overrightarrow{u} \vert } \quad \vert ~ cos^{-1} \quad \to \quad '
                       r' \gamma ~=~ cos^{-1} \Big( \frac{ \vert \overrightarrow{v}'
                       r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                       r' \vert \overrightarrow{u} \vert } \Big) \quad (1P) \\'
                       r' \vert \overrightarrow{v} \cdot \overrightarrow{u} \vert'
                       r'~=~ \vert ' + gzahl_klammer(vx) + r' \cdot ' + gzahl_klammer(px)
                       + '+' + gzahl_klammer(vy) + r' \cdot ' + gzahl_klammer(py)
                       + '+' + gzahl_klammer(vz) + r' \cdot ' + gzahl_klammer(pz) + r' \vert ~=~'
                       + gzahl(abs(N(sp_vp,3))) + r' \quad (2P) \\'
                       r' \vert \overrightarrow{u} \vert ~=~ \sqrt{ (' + str(vx) + ')^2 ~+~('
                       + str(vy) + ')^2 ~+~(' + str(vz) + ')^2} ~=~ ' + gzahl(N(l_v,3))
                       + r' \quad \mathrm{und} \quad \vert \overrightarrow{v} \vert ~=~ \sqrt{ ('
                       + str(px) + ')^2 ~+~(' + str(py) + ')^2 ~+~(' + str(pz)
                       + ')^2} ~=~ ' + gzahl(N(l_p,3)) + r' \quad (2P) \\'
                       + r' \gamma ~=~ cos^{-1} \Big( \frac{' + gzahl(abs(N(sp_vp,3))) + '}{'
                       + gzahl(N(l_v,3)) + r' \cdot ' + gzahl(N(l_p,3))
                       + r'} \Big) ~=~' + gzahl(N(np.degrees(np.arccos(abs(sp_vp)/(l_v*l_p))),3))
                       + r' \quad (2P) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
        i += 1
    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
