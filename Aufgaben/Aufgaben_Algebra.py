from pylatex import (MediumText)
from pylatex.utils import bold
import string
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
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

# Berechnung für die Aufgaben
def punkte_und_vektoren(nr, teilaufg):
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

def rechnen_mit_vektoren(nr, teilaufg):
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
                       + r') \quad (1P) \\'+ r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    # if c in teilaufg:
    #     faktor_1, faktor_2 = random.randint(1,10)/2, random.randint(1,10)/2
    #     print('r =' + gzahl(faktor_1))
    #     print('s =' + gzahl(faktor_2))
    #     vektor_2 = punkt_vektor(5)
    #     vektor_3 = [zzahl(1,7), zzahl(0,5),zzahl(1,7)]
    #     vektor_1 = (vektor_2[0] * faktor_1 + vektor_3[0] * faktor_2,
    #                 vektor_2[1] * faktor_1 + vektor_3[1] * faktor_2,
    #                 vektor_2[2] * faktor_1 + vektor_3[2] * faktor_2)
    #     x_1, y_1, z_1 = vektor_1[0], vektor_1[1], vektor_1[2]
    #     x_2, y_2, z_2 = vektor_2[0], vektor_2[1], vektor_2[2]
    #     x_3, y_3, z_3 = vektor_3[0], vektor_3[1], vektor_3[2]
    #
    #
    #     aufgabe.append(str(teilaufg[i]) + ') Überprüfe, ob der gegebenen Vektor a als Linearkombination'
    #                                             ' von b und c dargestellt werden kann. \n\n')
    #     aufgabe.append(r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(x_1) + r' \\'
    #                                                                + gzahl(y_1) + r' \\'
    #                                                                + gzahl(z_1) + r' \\'
    #                   r' \end{pmatrix} ~,~ \overrightarrow{b} ~=~ \begin{pmatrix} ' + gzahl(x_2) + r' \\'
    #                                                                                 + gzahl(y_2) + r' \\'
    #                                                                                 + gzahl(z_2) + r' \\'
    #                   r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{c} ~=~\begin{pmatrix}' + gzahl(x_3) + r' \\'
    #                                                                                            + gzahl(y_3) + r' \\'
    #                                                                                            + gzahl(z_3) + r' \\'
    #                    r' \end{pmatrix} \\')
    #
    #     loesung.append(str(teilaufg[i]) + ') \quad \mathrm{Überprüfe,~ob~der~gegebenen~Vektor~a~als~Linearkombination'
    #                                             '~von~b~und~c~dargestellt~werden~kann.}')
    #     loesung.append(r' \begin{pmatrix} ' + gzahl(x_1) + r' \\'
    #                                         + gzahl(y_1) + r' \\'
    #                                         + gzahl(z_1) + r' \\'
    #                   r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} ' + gzahl(x_2) + r' \\'
    #                                                                  + gzahl(y_2) + r' \\'
    #                                                                  + gzahl(z_2) + r' \\'
    #                   r' \end{pmatrix}  ~+~s \cdot \begin{pmatrix}' + gzahl(x_3) + r' \\'
    #                                                                 + gzahl(y_3) + r' \\'
    #                                                                 + gzahl(z_3) + r' \\'
    #                    r' \end{pmatrix}')
    #     loesung_1 = (r' \mathrm{aus~I~folgt:} \quad ' + gzahl(x_1) + '~=~' + gzahl(x_2) + r' \cdot r'
    #                  + vorz_str(x_3) + r's \cdot \quad \to \quad r~=~'
    #                  + latex(Rational(x_1,x_2)) + vorz_str(Rational(-1*x_3,x_2))
    #                  + r' \cdot s \quad (2P) \\')
    #
    #     if y_3 != 0:
    #         loesung_1 = (loesung_1 + r' \mathrm{r~einsetzen~in~II} \quad ' + gzahl(y_1) + '~=~'
    #                      + gzahl(y_2) + r' \cdot \Big(' + latex(Rational(x_1,x_2))
    #                      + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \Big)'
    #                      + vorz_str(y_3) + r' \cdot s \quad (1P) \\'
    #                      + gzahl(y_1) + vorz_str(Rational(-1*x_1*y_2,x_2)) + r' ~=~ s \cdot \Big('
    #                      + gzahl(Rational(-1*x_3*y_2,x_2)) + vorz_str(y_3)
    #                      + r' \Big) \quad (1P) \quad \to \quad'
    #                      + r' s ~=~ ' + latex((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2))
    #                      + r' \quad (1P) \quad \to \quad r ~=~'
    #                      + latex(N((x_1 / x_2) - (x_3/ x_2) * ((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2)),3))
    #                      + r' \quad (1P) \quad \mathrm{Probe} ~ (1P)')
    #     elif z_3 != 0:
    #         loesung_1 = (loesung_1 + r' \mathrm{r~einsetzen~in~III} \quad ' + gzahl(z_1) + '~=~'
    #                      + gzahl(z_2) + r' \cdot \Big(' + latex(Rational(x_1,x_2))
    #                      + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \Big)'
    #                      + vorz_str(z_3) + r' \cdot s \quad (2P) \\'
    #                      + gzahl(z_1) + vorz_str(Rational(-1* x_1*z_2,x_2)) + r' ~=~ s \cdot \Big('
    #                      + gzahl(Rational(-1*x_3*z_2,x_2)) + vorz_str(z_3)
    #                      + r' \cdot s \Big) \quad (2P) \quad \to \quad'
    #                      + r' s ~=~ ' + latex((z_1 - (x_1*z_2)/x_2)/(z_3 - (x_3*z_2)/x_2))
    #                      + r' \quad (1P) \quad  r~=~ '
    #                      + latex(N(x_1 / x_2 - (x_3/ x_2)*((z_1 + (x_1*z_2)/x_2)/(z_3 - (x_3*z_2)/x_2)),3))
    #                      + r' \quad \mathrm{Probe} ~ (1P)')
    #     else:
    #         pass
    #     loesung.append(loesung_1)
    #
    #     i += 1
    #     Punkte += 7
    #
    # if d in teilaufg:
    #     vektor_2 = punkt_vektor(5)
    #     faktor = zzahl(2, 40) / 10
    #     if random.random() < 0.5:
    #             faktor = zzahl(2,40)/5
    #             vektor_1 = (faktor * vektor_2[0],faktor * vektor_2[1],faktor * vektor_2[2])
    #             ergebnis = r' \mathrm{Die~Vektoren~sind~kollinear.} \quad (4P) \\'
    #     else:
    #         vektor_1 = (vektor_2[0]*zzahl(1,6)/2,vektor_2[1]*zzahl(3,8)/2,vektor_2[2]*zzahl(5,10)/2)
    #         ergebnis = r' \mathrm{Die~Vektoren~sind~nicht~kollinear.} \quad (4P) \\'
    #
    #     aufgabe.append(str(teilaufg[i]) + f') Prüfen Sie, ob die gegebenen Vektoren kollinear sind.')
    #     aufgabe.append(r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\'
    #                                                                + gzahl(vektor_1[1]) + r' \\'
    #                                                                + gzahl(vektor_1[2]) + r' \\'
    #                   r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{b} ~=~ \begin{pmatrix} ' + gzahl(vektor_2[0]) + r' \\'
    #                                                                                              + gzahl(vektor_2[1]) + r' \\'
    #                                                                                              + gzahl(vektor_2[2]) + r' \\'
    #                   r' \end{pmatrix} \\')
    #     loesung.append(r'~ \\\\')
    #     loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Prüfen~Sie,~ob~die~gegebenen~Vektoren~kollinear~sind.}')
    #     loesung.append(latex(N(vektor_1[0],3)) + '~=~' + gzahl(vektor_2[0]) + r' \cdot r \quad \to \quad r~=~'  + latex(N(vektor_1[0]/vektor_2[0],3)) + r' \\'
    #                    + latex(N(vektor_1[1],3)) + '~=~' + gzahl(vektor_2[1]) + r' \cdot r \quad \to \quad r~=~'  + latex(N(vektor_1[1]/vektor_2[1],3)) + r' \\'
    #                    + latex(N(vektor_1[2],3)) + '~=~' + gzahl(vektor_2[2]) + r' \cdot r \quad \to \quad r~=~'  + latex(N(vektor_1[2]/vektor_2[2],3)) + r' \\'
    #                    + ergebnis)
    #     i += 1
    #     Punkte += 4
    #
    # if e in teilaufg:
    #     vektor_a = punkt_vektor(5)
    #     vektor_ab = punkt_vektor(5)
    #     vektor_b = np.array(vektor_a) + np.array(vektor_ab)
    #     faktor = nzahl(1,9)/10
    #     vektor_t = [N(vektor_a[0] + vektor_ab[0]*faktor,3),
    #                 N(vektor_a[1] + vektor_ab[1]*faktor,3),
    #                 N(vektor_a[2] + vektor_ab[2]*faktor,3)]
    #     print('Aufgabe 1e')
    #     print('a =' + gzahl(vektor_a))
    #     print('ab = ' + gzahl(vektor_ab))
    #     print('b = ' + gzahl(vektor_b))
    #     print('faktor = ' + gzahl(faktor))
    #     print('vektor t = ' + gzahl(vektor_t))
    #     vektor_at = np.array(vektor_t) - np.array(vektor_a)
    #     vektor_tb = vektor_b - np.array(vektor_t)
    #     print('at = ' + gzahl(vektor_at))
    #     print('tb = ' + gzahl(vektor_tb))
    #     laenge_vektor_at = (r' \sqrt{' + latex(N(sum(a*a for a in vektor_at),4)) + '} ~=~'
    #                         + latex(sqrt(N(sum(a*a for a in vektor_at),3))))
    #     ergebnis_at = sqrt(N(sum(a*a for a in vektor_at),3))
    #     laenge_vektor_tb = (r' \sqrt{' + latex(N(sum(a*a for a in vektor_tb),3)) + '} ~=~'
    #                         + latex(N(sqrt(sum(a*a for a in vektor_tb)),3)))
    #     ergebnis_tb = sqrt(N(sum(a*a for a in vektor_tb),3))
    #     aufgabe.append(str(teilaufg[i]) + ') In welchem Verhältnis teilt der Punkt T die Strecke AB? \n\n')
    #     aufgabe.append('A( ' + gzahl(vektor_a[0]) + ' | ' + gzahl(vektor_a[1]) + ' | ' + gzahl(vektor_a[2]) + ' ), '
    #                    'B( ' + gzahl(vektor_b[0]) + ' | ' + gzahl(vektor_b[1]) + ' | ' + gzahl(vektor_b[2]) + ' ) und '
    #                    'T( ' + latex(N(vektor_t[0],3)) + ' | ' + latex(N(vektor_t[1],3))
    #                    + ' | ' + latex(N(vektor_t[2],3)) + ' ). \n\n')
    #     loesung.append(str(teilaufg[i]) + r') \quad \mathrm{d(A,T)~=~} \sqrt{(' + gzahl(vektor_t[0]) + vorz_str(-1*vektor_a[0])
    #                    + ')^2 ~+~(' + gzahl(vektor_t[1]) + vorz_str(-1*vektor_a[1]) + ')^2 ~+~(' + gzahl(vektor_t[2])
    #                    + vorz_str(-1*vektor_a[2]) + ')^2 } ~=~' + laenge_vektor_at + r' \quad (2P) \\'
    #                    + r' \mathrm{d(T,B)~=~} \sqrt{(' + gzahl(vektor_b[0]) + vorz_str(-1*vektor_t[0])
    #                    + ')^2 ~+~(' + gzahl(vektor_b[1]) + vorz_str(-1*vektor_t[1]) + ')^2 ~+~(' + gzahl(vektor_b[2])
    #                    + vorz_str(-1*vektor_t[2]) + ')^2 } ~=~' + laenge_vektor_tb + r' \quad (2P) \\'
    #                    + r' r~=~ \frac{ ' + latex(ergebnis_at) + '}{' + latex(ergebnis_tb) + '} ~=~'
    #                    + latex(ergebnis_at/ergebnis_tb) + r' \quad (2P) \\')
    #     i += 1
    #     Punkte += 6
    #
    # if f in teilaufg:
    #     vektor_a = punkt_vektor(5)
    #     vektor_b = np.array(vektor_a) + np.array(punkt_vektor(5))
    #     vektor_ab = vektor_b - np.array(vektor_a)
    #     a1 = nzahl(1,9)
    #     faktor = a1/10
    #     vektor_t = np.array(vektor_a) + faktor * vektor_ab
    #     vektor_at = vektor_t - np.array(vektor_a)
    #     vektor_tb = vektor_b - vektor_t
    #     laenge_vektor_at = (r' \sqrt{' + latex(N(sum(a*a for a in vektor_at),3)) + '} ~=~'
    #                         + latex(N(sqrt(sum(a*a for a in vektor_at)),3)))
    #     laenge_vektor_tb = (r' \sqrt{' + latex(N(sum(a*a for a in vektor_tb),4)) + '} ~=~'
    #                         + latex(sqrt(N(sum(a*a for a in vektor_tb),3))))
    #     faktor_r = Rational(a1,(10-a1))
    #     print('1f) faktor = ' + gzahl(faktor))
    #     print('1f) r =' + gzahl(faktor_r))
    #     # print('r_2 = ' + gzahl(faktor_r))
    #     aufgabe.append(str(teilaufg[i]) + ') Der Punkt T teilt die Strecke AB im Verhältnis r. Bestimme den Punkt B.')
    #     aufgabe.append('A(~' + latex(vektor_a[0]) + r'~ \vert ~' + latex(vektor_a[1]) + r'~ \vert ~' + latex(vektor_a[2])
    #                    + '~), \quad T(~' + latex(vektor_t[0]) + r'~ \vert ~' + latex(vektor_t[1]) + r'~ \vert ~'
    #                    + latex(vektor_t[2]) + '~) \quad \mathrm{und~r~=~}' + latex(faktor_r) + r'. \\')
    #     loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{OB} = \overrightarrow{OA} ~+~ \overrightarrow{AT} '
    #                                       r' \cdot \mathrm{ (~1~+~ \frac{1}{r} ~)}  ~=~'
    #                    r' \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
    #                                         + gzahl(vektor_a[1]) + r' \\'
    #                                         + gzahl(vektor_a[2]) + r' \\'
    #                    r' \end{pmatrix} ~+~ \begin{pmatrix} ' + latex(N(vektor_at[0],3))+ r' \\'
    #                                                           + latex(N(vektor_at[1],3)) + r' \\'
    #                                                           + latex(N(vektor_at[2],3)) + r' \\'
    #                    r' \end{pmatrix} \cdot \Big( ~1~+~ ' + latex(Rational(10-a1,a1)) + r' \Big) \\'
    #                    r' ~=~ \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
    #                                             + gzahl(vektor_a[1]) + r' \\'
    #                                             + gzahl(vektor_a[2]) + r' \\'
    #                    r' \end{pmatrix} ~+~ \begin{pmatrix} ' + latex(N(vektor_at[0]*(1+(10-a1)/a1),3)) + r' \\'
    #                                                           + latex(N(vektor_at[1]*(1+(10-a1)/a1),3)) + r' \\'
    #                                                           + latex(N(vektor_at[2]*(1+(10-a1)/a1),3)) + r' \\'
    #                    r' \end{pmatrix} ~=~ \begin{pmatrix} ' + latex(N(vektor_b[0],3)) + r' \\'
    #                                                           + latex(N(vektor_b[1],3)) + r' \\'
    #                                                           + latex(N(vektor_b[2],3)) + r' \\'
    #                    r' \end{pmatrix} \quad \to \quad B(~' + gzahl(vektor_b[0]) + r'~ \vert ~' + gzahl(vektor_b[1])
    #                    + r'~ \vert ~' + gzahl(vektor_b[2]) + r' ~) \quad (4P) \\')
    #     i += 1

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]