from pylatex.utils import bold
import string, sys
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure, MultiColumn
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *

# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

# Berechnung für die Aufgaben
def punkte_und_vektoren(nr, teilaufg=['a', 'b', 'c'], ks=None, BE=[]):
    # Aufgabe zur Darstellung von Punkten im 3-dim-Kordinatensystem und Vektorechnung
    # Mithilfe von "teilaufg=[]" können Teilaufgaben der Aufgabe festgelegt werden.
    # Der Parameter "ks=" legt fest, ob die Aufgabe ein leeres dreidimensionales Koordinatensystem oder kariertes Papier enthält. Der Parameter kann "None", "True" oder "False" sein". Standardmäßig ist "ks=None" und somit gibt kein Koordinatensystem und kein kariertes Papier.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
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
                     r' \begin{pmatrix} ' + gzahl(ortsvektor_c[0]) + r' \\' + gzahl(ortsvektor_c[1]) + r' \\'
                     + gzahl(ortsvektor_c[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(-1*vektor_ab[0])
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
                     + ')^2 } ~=~' + laenge_vektor_bc + r' \quad (2P) \\')
        loesung_2 = (r') \quad \overrightarrow{OD} = \overrightarrow{OA} ~+~ \overrightarrow{BC} ~=~ '
                     + r' \begin{pmatrix} ' + gzahl(ortsvektor_a[0]) + r' \\' + gzahl(ortsvektor_a[1]) + r' \\'
                     + gzahl(ortsvektor_a[2]) + r' \\' + r' \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(vektor_bc[0])
                     + r' \\' + gzahl(vektor_bc[1]) + r' \\' + gzahl(vektor_bc[2]) + r' \\'
                     + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ortsvektor_d[0]) + r' \\'
                     + gzahl(ortsvektor_d[1]) + r' \\' + gzahl(ortsvektor_d[2]) + r' \\'
                     + r'\end{pmatrix}  \quad (3P) \\')

    # print('a = ' + str(ortsvektor_a)), print('b = ' + str(ortsvektor_b)), print('c = ' + str(ortsvektor_c))
    # print('d=' + str(ortsvektor_d)), print(vektor_ab), print(vektor_ac)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Punkte '
               'A(' + gzahl(ortsvektor_a[0]) + '|' + gzahl(ortsvektor_a[1]) + '|' + gzahl(ortsvektor_a[2]) + '), ' 
               'B(' + gzahl(ortsvektor_b[0]) + '|' + gzahl(ortsvektor_b[1]) + '|' + gzahl(ortsvektor_b[2]) + ') und ' 
               'C(' + gzahl(ortsvektor_c[0]) + '|' + gzahl(ortsvektor_c[1]) + '|' + gzahl(ortsvektor_c[2]) + '). \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        pkt = 2
        # Punkte im 3-dim-Koordinatensystem einzeichnen und verbinden
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if ks == True:
            aufgabe.append(str(teilaufg[i]) + f') Zeichnen Sie die Punkte A, B und C im Koordinatensystem ein '
                                              f'und verbinden diese. \n\n')
        else:
            aufgabe.append(str(teilaufg[i]) + f') Zeichnen Sie die Punkte A, B und C in einem Koordinatensystem ein '
                                              f'und verbinden diese. \n\n')
            pkt += 2
        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Punkte~(1P),~Seiten~vom~Dreieck~(1P)}')
        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Abstände von Punkten berechnen und vergleichen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        aufgabe.append(str(teilaufg[i]) + f') Weisen Sie nach, dass das Dreieck ABC gleichschenklig ist. \n\n')
        loesung.append(str(teilaufg[i]) + (r') \quad ~ \overrightarrow{AB} ~=~ \begin{pmatrix}'
                                           + gzahl(vektor_ab[0]) + r' \\' + gzahl(vektor_ab[1]) + r' \\'
                                           + gzahl(vektor_ab[2]) + r' \\ \end{pmatrix} \to \mathrm{d(A,B)~=~} \sqrt{('
                                           + gzahl(vektor_ab[0]) + ')^2 ~+~(' + gzahl(vektor_ab[1]) + ')^2 ~+~('
                                           + gzahl(vektor_ab[2]) + ')^2 } ~=~' + laenge_vektor_ab + r' \quad (2P) \\'
                                           + loesung_1 + r' \mathrm{Die~beiden~Seiten~sind~gleichlang,'
                                           + r'~somit~ist~das~Dreieck~gleichschenklig.} \quad (1P) \\'
                                           + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}'))

        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # mithilfe von Vektorrechnung einen vierten Punkt für ein Parallelogramm berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.append(str(teilaufg[i]) + (f') Bestimmen Sie einen Punkt D so, dass die Punkte A,B,C und D'
                                           + f' ein Parallelogramm bilden.'))
        loesung.append(str(teilaufg[i]) + loesung_2 + r' \mathrm{Punkt~D~hat~die~Koordinaten:~}~D('
                       + gzahl(ortsvektor_d[0]) + ' | ' + gzahl(ortsvektor_d[1]) + ' | ' + gzahl(ortsvektor_d[2])
                       + r') \quad (1P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1
    if ks != None:
        if ks == True:
            aufgabe.append('3dim_Koordinatensystem')
            loesung.append('3dim_Koordinatensystem')
        else:
            aufgabe.append('kariertes_Papier')
            loesung.append('kariertes_Papier')

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rechnen_mit_vektoren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], linearkombination=None, kollinear=None, BE=[]):
    # Aufgabe zum Rechnen mit Vektoren, Mittelpunkten, Linearkombination bzw. Kollinarität und Streckenverhältnissen
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # resultierenden Vektor einer Vektoraddition berechnen
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
        # Mittelpunkt zweier gegebener Punkte berechnen
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
        # Linearkombination von Vektoren überprüfen
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
        # Vektoren auf Kollinearität überprüfen
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
        # Berechnen des Streckenverhältnisses, in die ein Punkt T eine Strecke teilt
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
        # Berechnung eines Punktes aus gegebenen Streckenverhältnissen
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

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_aufstellen(nr, teilaufg=['a', 'b'], T_auf_g=False, BE=[]):
    # Aufgabe zum Aufstellen von Geraden und Überprüfen der Lagebeziehung Punkt-Gerade
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    punkt_a = [ax, ay, az] = punkt_vektor(3)
    punkt_b = [bx, by, bz] = punkt_a + punkt_vektor(3)
    v = [vx, vy, vz] = vektor_ganzzahl((punkt_b) - (punkt_a))

    p = random.choice([0,1])
    if T_auf_g == None:
        T_auf_g = random.choice([True,False])
    if T_auf_g:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,30)/5)*v)
    elif T_auf_g == False:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,10)/2)*[vy,vx,vz+zzahl(1,3)])
        while (tx-ax)/vx == (ty-ay)/ty == (tz-az)/tz:
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1, 10) / 2) * [vy, vx, vz + zzahl(1, 3)])
    else:
        exit("T_auf_g muss None, True oder False sein!")

    lx, ly, lz = vektor_ganzzahl([(tx-ax)/vx, (ty-ay)/vy, (tz-az)/vz])
    if 'a' in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + gzahl(ax)  + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
                   'B( ' + gzahl(bx)  + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
                   'T( ' + gzahl(N(tx,3))  + ' | ' + gzahl(N(ty,3)) + ' | ' + gzahl(N(tz,3)) + ' ).  \n\n']
    if 'a' not in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   r' \mathrm{Gegeben~ist~die~Gerade g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                   + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} ' + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\'
                   + gzahl(v[2]) + r' \\' + r' \end{pmatrix} .} ']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Aufstellen der Geradengleichung bei gegebenen Punkten
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
        # Überprüfen der Lagebeziehung der Geraden g mit dem Punkt T
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

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_lagebeziehung(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], lagebeziehung=None, BE=[]):
    # Aufgabe zur Lagebeziehung zweier Geraden und ggf. des Abstandes beider Geraden
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    if lagebeziehung == None:
        lagebeziehung = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
    elif 'e' in teilaufg:
        lagebeziehung = random.choice(['windschief', 'schneiden'])
    elif lagebeziehung not in ['identisch', 'parallel', 'windschief', 'schneiden', None]:
        sys.exit("Lagebeziehung muss 'identisch' , 'parallel', 'windschief', 'schneiden', oder None sein")
    v_teiler = zzahl(1, 3)
    punkt_a = [ax, ay, az] = punkt_vektor(3) # Punkt A liegt auf Gerade g_1
    v = [vx, vy, vz] = vektor_ganzzahl([zzahl(1, 6) / 2 * v_teiler,
                                        zzahl(1, 6) / 2 * v_teiler, v_teiler]) # Vektor v ist der Richtungsvektor von Geraden g_1
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    uz = (vx*ux + vy * uy)/vz
    u = vektor_ganzzahl([ux, uy, uz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    if 'a' in teilaufg:
        # lagebeziehungen zweier Geraden und die dafür nötigen Eigenschaften erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        liste_punkte.append(punkte)

        aufgabe.append(str(teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen zweier Geraden und '
                                          'deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Geraden:'), 'Punkte')
        table1.add_row('', '-', 'sind parrallel, d.h. die Richtungsvektoren '
                       + 'sind kollinear, aber die Geraden haben keine gemeinsamen Punkte', '2P' )
        table1.add_row('', '-', 'sind identisch, d.h. die Richtungsvektoren sind kollinear und die Geraden '
                       + 'haben alle Punkte gemeinsam ', '2P' )
        table1.add_row('', '-', 'schneiden sich, d.h. die Richtungsvektoren sind nicht kollinear '
                       + 'und die Geraden haben einen Punkt gemeinsam', '2P' )
        table1.add_row('', '-', 'sind windschief, d.h. die Richtungsvektoren sind nicht kollinear '
                       + 'und die Geraden haben keine gem. Punkte.', '2P' )
        table1.add_row('','','', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)
        if 'b' in teilaufg:
            loesung.append(' \n\n')
        i += 1

    if 'b' in teilaufg:
        # mathematisches Vorgehen zur Bestimmung der Lagebeziehung zweier Geraden erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)
        aufgabe.append(str(teilaufg[i]) + ') Erläutern Sie, wie man die Lagebeziehung zweier '
                                          'Geraden mathematisch überprüfen kann. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(teilaufg[i]) + ')', MultiColumn(2, align='l', data=' Lagebeziehung zweier Geraden'),
                       'Punkte')
        table1.add_row('', '-', 'Zuerst prüft man ob die Geraden parallel sind, '
                       + 'indem man die Richtungsvektoren gleichsetzt und r bestimmt.', '2P')
        table1.add_row('', '-', 'Sind die Geraden parallel (d.h. die Richtungsvektoren sind kollinear), '
                       + 'setzt man einen Stützvektor in die andere Geradengleichung ein. Ist dieser in der anderen '
                       + 'Geraden enthalten, sind die Geraden identisch, ansonsten "echt" parallel.', '2P')
        table1.add_row('', '-', 'Sind die Geraden nicht parallel, setzt man beide Geraden gleich und '
                       + 'löst das Gleichungssystem. Erhält man eine Lösung für r und s, schneiden sich die Geraden. '
                       + 'erhält man keine Lösung, sind die Geraden windschief. ', '2P')
        table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)

        i += 1

    if 'c' in teilaufg:
        # Lagebeziehung zweier gegebener Geraden bestimmen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

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
            punkt_c = [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(u)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
            while (cx-ax)/vx == (cy-ay)/vy == (cz-az)/vz:
                punkt_c = [cx, cy, cz] = vektor_ganzzahl((punkt_a) + zzahl(1, 30) / 5 * np.array(u))  # Punkt C liegt auf h
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
            punkt_d = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v))
            punkt_d = [dx,dy,dz] = [punkt_d[0], punkt_d[1], punkt_d[2] + zzahl(1,3)]
            punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(u))
            w = [wx, wy, wz]= vektor_ganzzahl(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
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

        aufgabe.extend(('Gegeben sind die beiden Geraden mit folgenden Gleichungen:',
                        r'g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad h: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                       r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                       + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                       r' \end{pmatrix}\\'))
        aufgabe.append(str(teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \mathit{Die~Auswahl~war~' + lagebeziehung + r'} \hspace{25em} \\'
                       + loesung_1)
        i += 1

    if 'e' in teilaufg and lagebeziehung in ['parallel', 'windschief']:
        # Bestimmung des Abstandes zweier paralleler bzw. windschiefer Geraden
        pass

    if 'f' in teilaufg:
        # Schnittwinkel zweier gegebener Geraden berechnen
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

        if 'c' in teilaufg:
            aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
            aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                   + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                   r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                   + gzahl(px) + r' \\' + gzahl(py) + r' \\' + gzahl(pz) + r' \\'
                   r' \end{pmatrix} ')
        if 'c' not in teilaufg:
            aufgabe.append('Gegeben sind die beiden Geraden mit folgenden Gleichungen:')
            aufgabe.append(r' \mathrm{g: \overrightarrow{x} ~=~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                           + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                           + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'+
                           r' \end{pmatrix} \quad und \quad k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                           + r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                           + gzahl(px) + r' \\' + gzahl(py) + r' \\' + gzahl(pz) + r' \\'
                           + r' \end{pmatrix} }')
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

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_und_punkt(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], t_in_ebene=None, BE=[]):
    # Aufgaben zum Aufstellen der Ebenengleichung und Lagebziehung Punkt-Ebene
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []
    i = 0
    n_gk = np.array([100,100,100])
    v_teiler = zzahl(1, 3)
    punkt_a = [ax, ay, az] = punkt_vektor(3)  # Punkt A liegt auf Gerade g_1
    v = [vx, vy, vz] = vektor_ganzzahl(np.array([zzahl(1, 3) * v_teiler,
                                                 zzahl(1, 3) * v_teiler,
                                                 v_teiler]))  # Vektor v ist der Richtungsvektor von Geraden g_1
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1, 3)  # x und y Koordinate von u kann frei gewählt werden
    uz = - 1 * (vx * ux + vy * uy) / vz
    u = vektor_ganzzahl([ux, uy, uz])
    punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_a + v)  # Punkte C und D liegen auf h
    punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_b + zzahl(1, 4) * np.array(u))
    w = vektor_ganzzahl(punkt_c - punkt_a)  # Vektor w ist der Richtungsvektor von h
    [wx, wy, wz] = vektor_runden(w, 3)
    n = [nx, ny, nz] = vektor_ganzzahl(np.cross(v, w))
    n_gk = [nx_gk, ny_gk, nz_gk] = vektor_kürzen(n)
    n_betrag = np.linalg.norm(n_gk)
    koordinatenform = ('E:~' + vorz_v_aussen(nx_gk, 'x') + vorz_v_innen(ny_gk,'y') + vorz_v_innen(nz_gk, 'z')
                       + '~=~' + gzahl(np.dot(punkt_a, n_gk)))
    if n_betrag%1 == 0:
        ergebnis_n0 = gzahl(n_betrag)
    else:
        ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk**2 + ny_gk**2 + nz_gk**2) + r'}'
    parameter_r = zzahl(1, 2)
    parameter_s = zzahl(1, 2)
    if t_in_ebene == None and 'e' not in teilaufg:
        t_in_ebene = random.choice([True,False])
    if t_in_ebene == True:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
        lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~in~der~Ebene~E.} \quad (3P) \\'
    else:
        [x, y, z] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
        punkt_t = [tx, ty, tz] = [x, y, z + zzahl(1,3)]
        lsg = r' \quad \mathrm{f.A.} \\ \mathrm{Der~Punkt~T~liegt~nicht~in~der~Ebene.} \quad (3P) \\'

    if 'a' in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + gzahl(ax) + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
                   'B( ' + gzahl(bx) + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
                   'C( ' + gzahl(cx) + ' | ' + gzahl(cy) + ' | ' + gzahl(cz) + ' ). \n\n']

    elif 'b' in teilaufg and 'a' not in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   r' \mathrm{Gegeben~ist~die~Ebene} \quad E: \overrightarrow{x} ~=~ \begin{pmatrix} '
                   + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                   + gzahl(bx - ax) + r' \\' + gzahl(by - ay) + r' \\' + gzahl(bz - az) + r' \\'
                   r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                   + gzahl(cx - ax) + r' \\' + gzahl(cy - ay) + r' \\' + gzahl(cz - az) + r' \\'
                   r' \end{pmatrix}']
    elif 'a' and 'b' not in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   r' \mathrm{Gegeben~ist~die~Ebene} \quad E: \begin{bmatrix} \overrightarrow{x}'
                   r'~-~ \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                   + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                   r' \end{pmatrix} ~=~0']
    else:
        pass
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Ebenengleichung in Parameterform aus drei gegebenen Punkten aufstellen
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die Parametergleichung der Ebene E auf, '
                                          f'welche die Punkte A, B und C enthält. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{AB} ~=~ \begin{pmatrix} '
                       + gzahl(bx-ax) + r' \\' + gzahl(by-ay) + r' \\' + gzahl(bz-az) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AC} ~=~ \begin{pmatrix} '
                       + gzahl(cx-ax) + r' \\' + gzahl(cy-ay) + r' \\' + gzahl(cz-az) + r' \\'
                       r' \end{pmatrix} \quad \to \quad E: \overrightarrow{x} ~=~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(bx - ax) + r' \\' + gzahl(by - ay) + r' \\' + gzahl(bz - az) + r' \\'
                       r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                       + gzahl(cx - ax) + r' \\' + gzahl(cy - ay) + r' \\' + gzahl(cz - az) + r' \\'
                       r' \end{pmatrix} \quad (3P) \\'
                       r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        i += 1

    if 'b' in teilaufg:
        # gegebene Ebenengleichung von Parameterform in Normalen- und Koordinatenform umformen
        punkte = 7
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + ') Formen Sie die Gleichung für Ebene E in '
                       + 'Normalen- und Koordinatenform um. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                       + gzahl(vy * wz) + '-' + gzahl_klammer(vz * wy) + r' \\'
                       + gzahl(vz * wx) + '-' + gzahl_klammer(vx * wz) + r' \\'
                       + gzahl(vx * wy) + '-' + gzahl_klammer(vy * wx) + r' \\ \end{pmatrix} ~=~ \begin{pmatrix} '
                       + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                       + r' \end{pmatrix} ~=~ ' + gzahl(Rational(ny,ny_gk)) + r' \cdot \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} \quad (3P) \\\\'
                       + r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       + r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} ~=~0 \quad (2P) \\\\ E:~' + gzahl(nx_gk) + r' \cdot x'
                       + vorz_str(ny_gk) + r' \cdot y' + vorz_str(nz_gk) + r' \cdot z' + '~=~'
                       + gzahl(np.dot(punkt_a, n_gk)) + r' \quad (2P) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        i += 1

    if 'c' in teilaufg:
        # Überprüfen, ob ein Punkt in der Ebene liegt
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append('Gegeben ist ein weiterer Punkt T(' + gzahl(tx) + '|' + gzahl(ty) + '|'
                       + gzahl(tz) + '), \n\n')
        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T in der Ebene E liegt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad E:~' + gzahl(nx_gk) + r' \cdot (' + gzahl(tx) + ')'
                       + vorz_str(ny_gk) + r' \cdot (' + gzahl(ty) + ')' + vorz_str(nz_gk) + r' \cdot ('
                       + gzahl(tz) + ') ~=~' + gzahl(np.dot(punkt_a, n_gk)) + r' \quad \to \quad '
                       + gzahl(np.dot(n_gk, punkt_t)) + '~=~' + gzahl(np.dot(punkt_a, n_gk)) + lsg
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')

        i += 1

    if t_in_ebene == False:
        # Aufstellen der hessischen Normalform der Ebenengleichung
        if 'd' in teilaufg:
            punkte = 4
            liste_punkte.append(punkte)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                           + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                           + ergebnis_n0 + r' \quad \to \quad '
                           + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                           + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                           + r' \end{pmatrix} ~=~0 \\'
                           + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
            i += 1

        if 'e' in teilaufg:
            # Berechnung des Abstandes eines Punktes von der Ebene
            punkte = 3
            liste_punkte.append(punkte)
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand des Punktes T zur Ebene E. \n\n')
            if 'd' not in teilaufg:
                punkte += 4
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                               + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                               + ergebnis_n0 + r' \quad \to \quad '
                               + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} ~=~0 \quad (4P) \\'
                               + r' d~=~ \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(tx) + r' \\' + gzahl(tx) + r' \\' + gzahl(tz) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_t - punkt_a),(1 / n_betrag * n_gk)),3)))
                               + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad d~=~ \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(tx) + r' \\' + gzahl(tx) + r' \\' + gzahl(tz) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_t - punkt_a),(1 / n_betrag * n_gk)),3)))
                               + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebenen_umformen(nr, teilaufg=['a', 'b'], form=None, koordinatensystem=False, BE=[]):
    # Aufgaben zum Umformen der Ebenengleichungen aus Normalen- oder Koordinatenform und mithilfe der Achsenabschnittsform Ebene zeichnen
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    teiler = zzahl(1,3)
    schnittpunkte = [sx,sy,sz,e]=[zzahl(1,5),zzahl(1,5),zzahl(1,5),1]
    fkt_kf = [kfx,kfy,kfz,kfe] = vektor_kürzen([1/sx,1/sy,1/sz,e])
    n = [nx,ny,nz] = vektor_kürzen([int(kfx),int(kfy),int(kfz)])
    print(schnittpunkte)
    print(fkt_kf)
    print(n)
    punkt_a = [ax,ay,az] = random.choice([np.array([kfe/kfx,0,0]),np.array([0,kfe/kfy,0]),np.array([0,0,kfe/kfz])])
    print(punkt_a)
    normalenform = (r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                    + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                    r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                    + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                    r' \end{pmatrix} ~=~ 0')
    koordinatenform = ('E:~' + gzahl(nx) + 'x' + vorz_str(ny) + 'y'
                       + vorz_str(nz) + 'z') + '~=~' + gzahl(np.dot(punkt_a,n))

    if form == None:
        form = random.choice(['normalenform', 'koordinatenform'])
    if form == 'normalenform' and 'a' in teilaufg:
        ebenengleichung = normalenform
        andere_darstellungsform = koordinatenform
        lsg = (r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ \end{pmatrix}')
    elif form == 'koordinatenform' or 'a' not in teilaufg:
        ebenengleichung = koordinatenform
        andere_darstellungsform = (r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                                   + latex(Rational(np.dot(punkt_a,n),nx)) + r' \\' + gzahl(0)
                                   + r' \\' + gzahl(0) + r' \\  \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                                   + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                                   r' \end{pmatrix} ~=~ 0')
        lsg = (r' \begin{pmatrix} ' + latex(Rational(np.dot(punkt_a,n),nx)) + r' \\' + gzahl(0)
               + r' \\' + gzahl(0) + r' \\ \end{pmatrix}')
    else:
        exit("form kann nur None, 'normalenform' oder 'koordinatenform' sein ")

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Gegeben ist die Ebene E mit der folgenden Gleichung:',
               ebenengleichung]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    if 'a' in teilaufg:
        # gegebene Normalen- bzw. Koordinatenform in Parameter-, Koordinaten- bzw. Normalenform umformen
        punkte = 7
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(teilaufg[i]) + f') Formen Sie die Ebenengleichung in die '
                                          f'anderen beiden Darstellungsformen um. \n\n ')
        loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                       + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                       r' \end{pmatrix} \quad \to \quad ' + andere_darstellungsform + r' \quad (3P) \\'
                       r' \overrightarrow{u} ~=~ \begin{pmatrix}'
                       + gzahl(-1*ny) + r' \\' + gzahl(nx) + r' \\' + gzahl(0) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{v} ~=~ \begin{pmatrix}'
                       + gzahl(0) + r' \\' + gzahl(-1*nz) + r' \\' + gzahl(ny) + r' \\'
                       r' \end{pmatrix} \quad \to\ \quad E: \overrightarrow{x} ~=~ '
                       + lsg + r' ~+~r \cdot \begin{pmatrix} '
                       + gzahl(-1*ny) + r' \\' + gzahl(nx) + r' \\' + gzahl(0) + r' \\'
                       r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                       + gzahl(0) + r' \\' + gzahl(-1*nz) + r' \\' + gzahl(ny) + r' \\'
                       r' \end{pmatrix} \quad (4P) \\')
        i += 1

    if 'b' in teilaufg:
        # Aufstellen der Achsenabschnittsform der Ebene und zeichnen der Ebene in 3-dim-Koordinatenform
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Achsenabschnittsform von E auf '
                       + f'und zeichnen Sie ein Schrägbild der Ebene.')
        aufgabe.append('3dim_Koordinatensystem') if koordinatensystem else aufgabe.append(' \n\n')
        loesung.extend((str(teilaufg[i]) + r') \quad ' + koordinatenform + r' \quad \vert \div '
                       + gzahl(np.dot(punkt_a,n)) + r' \quad \to \quad ' + r'E:~ \frac{x}{' + gzahl_klammer(sx)
                       + r'} + \frac{y}{' + gzahl_klammer(sy) + r'} + \frac{z}{' + gzahl_klammer(sz) + r'} ~=~'
                       + str(1) + r' \quad (1P) \\ \mathrm{Zeichnung: \quad (2P)}', ''))
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_und_gerade(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], g_in_E=None, BE=[]):
    # Lagebeziehungen einer Ebene mit einer Geraden und ggf. Abstandsberechnung
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    n_gk = [nx_gk, ny_gk, nz_gk] = punkt_vektor(5)
    punkt_a = [ax, ay, az] = punkt_vektor(3)  # Punkt A liegt in Ebene E
    v = [vx,vy,vz] = np.array([-nz_gk,0,nx_gk])
    u = [ux,uy,uz] = np.array([-ny_gk,nx_gk,0])
    n_betrag = np.linalg.norm(n_gk)
    if n_betrag % 1 == 0:
        ergebnis_n0 = gzahl(n_betrag)
    else:
        ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk ** 2 + ny_gk ** 2 + nz_gk ** 2) + r'}'
    # auswahl = 'schneiden'
    # print('a: ' + str(punkt_a)), print('b: ' + str(punkt_b)), print('c: ' + str(punkt_c), print('vektor v: ' + str(v))
    # print('vektor u: ' + str(u)), print('vektor w: ' + str(w)), print('vektor n: ' + str(n)), print('vektor n_gk: ' + str(n_gk))

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), ' Gegeben ist die Ebene E in der Koordinatenform ',
               r' E:~ ' + vorz_v_aussen(nx_gk,'x') + vorz_v_innen(ny_gk,'y')
               + vorz_v_innen(nz_gk,'z ~=~') + gzahl(np.dot(punkt_a,n_gk))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []
    if g_in_E == None and 'e' not in teilaufg:
        g_in_E = random.choice(['identisch', 'parallel', 'schneiden'])

    if g_in_E == 'identisch':
        punkt_e = [ex, ey, ez] = punkt_a + zzahl(1, 7) / 2 * v + zzahl(1, 7) / 2 * u
        punkt_f = [fx, fy, fz] = punkt_a + zzahl(1, 7) / 2 * v + zzahl(1, 7) / 2 * u
        while vektor_vergleich(punkt_e, punkt_f) == True:
            punkt_f = [fx, fy, fz] = punkt_a + zzahl(1, 7) / 2 * v + zzahl(1, 7) / 2 * u
        g_v = [g_vx, g_vy, g_vz] = punkt_f - punkt_e
        lsg = (gzahl(nx_gk * ex + ny_gk * ey + nz_gk * ez) + '~=~'
               + gzahl(np.dot(punkt_a, n_gk))
               + r' \quad \mathrm{w.A. \quad Die~Gerade~liegt~in~der~Ebene. \quad (2P) } \\')
    elif g_in_E == 'schneiden':
        g_v = n_gk
        while vektor_kollinear(g_v, n_gk) == True:
            punkt_s = punkt_a + zzahl(1, 3) * v + zzahl(1, 3) * u
            g_v = [g_vx, g_vy, g_vz] = punkt_vektor(4)
            ergebnis_r = zzahl(1, 6) / 2
            punkt_e = [ex, ey, ez] = punkt_s - ergebnis_r * g_v
            punkt_f = [fx, fy, fz] = punkt_e + g_v

        lsg = (gzahl(nx_gk * ex + ny_gk * ey + nz_gk * ez)
               + vorz_str(nx_gk * g_vx + ny_gk * g_vy + nz_gk * g_vz) + r' \cdot r ~=~'
               + gzahl(np.dot(punkt_a, n_gk)) + r' \quad \vert '
               + vorz_str(-1 * (nx_gk * ex + ny_gk * ey + nz_gk * ez)) + r' \quad \vert \div '
               + gzahl_klammer(nx_gk * g_vx + ny_gk * g_vy + nz_gk * g_vz) + r' \quad \to \quad r~=~'
               + gzahl(ergebnis_r) + r' \quad (2P) \\'
               + r' \mathrm{Die~Gerade~schneidet~die~Ebene~im~Punkt:}  \quad (1P) \\ \begin{pmatrix} '
               + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
               + r' \end{pmatrix}' + vorz_str(ergebnis_r) + r' \cdot \begin{pmatrix} '
               + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
               + r' \end{pmatrix} ~=~ \begin{pmatrix} '
               + gzahl(ex + ergebnis_r * g_vx) + r' \\' + gzahl(ey + ergebnis_r * g_vy) + r' \\'
               + gzahl(ez + ergebnis_r * g_vz) + r' \\ \end{pmatrix} \quad \to \quad S('
               + gzahl(ex + ergebnis_r * g_vx) + r' \vert ' + gzahl(ey + ergebnis_r * g_vy) + r' \vert '
               + gzahl(ez + ergebnis_r * g_vz) + r') \quad (3P) \\')
    elif g_in_E == 'parallel' or 'e' in teilaufg:
        abstand = zzahl(1, 7) / 2 * np.array(n_gk)
        punkt_e = [ex, ey, ez] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v) + abstand)
        punkt_f = [fx, fy, fz] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(u) + abstand)
        g_v = [g_vx, g_vy, g_vz] = np.array(punkt_f - punkt_e)
        lsg = (gzahl(np.dot(n_gk, punkt_e)) + '~=~'
               + gzahl(np.dot(punkt_a, n_gk))
               + r' \quad \mathrm{f.A. \quad Die~Gerade~ist~parallel~zur~Ebene. \quad (2P)} \\')
    else:
        exit("g_in_E muss None, 'identisch', 'parallel' oder 'schneiden' sein!")

    if 'a' in teilaufg:
        # die Lagebeziehung einer Geraden mit einer Ebene und die dafür nötigen Eigenschaften erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)
        aufgabe.append(str(teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen einer Geraden '
                                          'mit einer Ebene und deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Gerade und die Ebene:'),
                       'Punkte')
        table1.add_row('', '-', 'sind parallel, d.h. der Richtungsvektor der Geraden und der Normalenvektor '
                                'der Ebene sind senkrecht zueinander und haben keine gemeinsamen Punkte', '2P')
        table1.add_row('', '-', 'sind identisch, d.h. der Richtungsvektor der Geraden und der Normalenvektor '
                                'der Ebene sind senkrecht zueinander und alle Punkte der Geraden liegen in der Ebene',
                                '2P')
        table1.add_row('', '-', 'schneiden sich, d.h. der Richtungsvektor der Geraden und der Normalenvektor '
                                'der Ebene sind nicht senkrecht zueinander und haben den Schnittpunkt gemeinsam', '2P')
        table1.add_row('','','', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)
        i += 1

    if 'b' in teilaufg:
        # Geradengleichung aus zwei gegebenen Punkten aufstellen
        punkte = 2
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.extend(('Gegeben ist  die Gerade g durch die Punkte: '
                        'A( ' + gzahl(ex) + ' | ' + gzahl(ey) + ' | ' + gzahl(ez) + ' ) und ' 
                        'B( ' + gzahl(fx) + ' | ' + gzahl(fy) + ' | ' + gzahl(fz) + ' ).  \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie Gleichung der Geraden g. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{AB} ~=~ \begin{pmatrix} '
                       + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                       + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       + r' \end{pmatrix} \quad (2P) \\ '
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte}')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # die Lagebeziehung einer Ebene mit einer Geraden bestimmen
        punkte = 3
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if g_in_E == 'schneiden':
            punkte += 4
        liste_punkte.append(punkte)


        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die Lagebeziehung der Geraden g '
                                                f'zur Ebene E und berechne ggf. den Schnittpunkt. \n\n')
        if 'b' not in teilaufg:
            aufgabe.appemnd(r' \mathrm{Gleichung~der~Geraden~g: \overrightarrow{x} \ ~ = ~ \begin{pmatrix}'
                            + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                            + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                            + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\' + r' \end{pmatrix} ')
        loesung.append(str(liste_teilaufg[i]) + r') \quad '
                       + gzahl(nx_gk) + r' \cdot (' + gzahl(ex) + vorz_str(g_vx) + 'r)'
                       + vorz_str(ny_gk) + r' \cdot (' + gzahl(ey) + vorz_str(g_vy) + 'r)'
                       + vorz_str(nz_gk) + r' \cdot (' + gzahl(ez) + vorz_str(g_vz) + 'r) ~=~'
                       + gzahl(np.dot(punkt_a, n_gk)) + r' \quad (1P) \\'
                       + lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

    if 'd' in teilaufg:
        # Aufstellen der hessischen Normalform einer Ebene
        punkte = 4
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        liste_punkte.append(punkte)
        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                       + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                       + ergebnis_n0 + r' \quad \to \quad '
                       + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} ~=~0 \\ \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

        if 'e' in teilaufg:
            # Berechnung des Abstandes einer parallelen Geraden zur Ebene
            punkte = 3
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            liste_punkte.append(punkte)
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand der Geraden zur Ebene E. \n\n')
            if 'd' not in teilaufg:
                punkte += 4
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                               + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                               + ergebnis_n0 + r' \quad \to \quad '
                               + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \quad (4P) \\'
                               + r' d: \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(ex) + r' \\' + gzahl(ex) + r' \\' + gzahl(ez) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + latex(abs(N(np.dot((punkt_e - punkt_a),(1 / n_betrag * n_gk)),3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad d: \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(ex) + r' \\' + gzahl(ex) + r' \\' + gzahl(ez) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + latex(abs(N(np.dot((punkt_e - punkt_a),(1 / n_betrag * n_gk)),3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_ebene(nr, teilaufg=['a', 'b', 'c', 'd'], F_in_E=None, BE=[]):
    # Lagebeziehungen zweier Ebenen und ggf. der Abstandsberechnung
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    i = 0
    n_gk = [nx_gk, ny_gk, nz_gk] = punkt_vektor(4)
    n_betrag = np.linalg.norm(n_gk)
    if n_betrag % 1 == 0:
        ergebnis_n0 = gzahl(n_betrag)
    else:
        ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk ** 2 + ny_gk ** 2 + nz_gk ** 2) + r'}'
    punkt_d = [dx, dy, dz] = punkt_vektor(3)
    v = np.array([ny_gk, -1 * nx_gk, 0])
    u = np.array([0, nz_gk, -1 * ny_gk])
    print('n_gk: ' + str(n_gk))
    print('Punkt D: ' + str(punkt_d))
    print('Vektor v: ' + str(v))
    print('Vektor u: ' + str(u))

    if F_in_E == None and 'd' not in teilaufg:
        F_in_E = random.choice(['identisch', 'parallel', 'schneiden'])

    # auswahl = 'schneiden'
    if F_in_E == 'identisch':
        punkte = 4
        punkt_a = [ax, ay, az] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(v))
        punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(u))
        punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_b + zzahl(1, 3) * np.array(u))
        g_v = [g_vx, g_vy, g_vz] = np.array(punkt_b - punkt_a)
        k_v = [k_vx, k_vy, k_vz] = np.array(punkt_c - punkt_a)

        lsg = (gzahl(np.dot(punkt_a, n_gk)) + '~=~' + gzahl(np.dot(punkt_d, n_gk))
               + r' \quad \mathrm{w.A. \quad Die~Ebene~F~liegt~in~der~Ebene~E. \quad (2P) } \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')

    elif F_in_E == 'schneiden':
        punkte = 10
        n = [nx, ny, nz] = punkt_vektor(4)
        punkt_a = [ax, ay, az] = punkt_vektor(3)
        while vektor_kollinear(n, n_gk) == True:
            n = [nx, ny, nz] = punkt_vektor(4)

        g_v = [g_vx, g_vy, g_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([nz, 0, -1 * nx]))
        k_v = [k_vx, k_vy, k_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([-1 * ny, nx, 0]))
        while np.dot(n_gk, k_v) == 0 or np.dot(n_gk, g_v) == 0:
            g_v = [g_vx, g_vy, g_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([nz, 0, -1 * nx]))
            k_v = [k_vx, k_vy, k_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([-1 * ny, nx, 0]))

        # print('Vektor n: ' + str(n))
        # print('Vektor g_v: ' + str(g_v))
        # print('Vektor k_v: ' + str(k_v))
        # print(-1 * np.dot(n_gk, k_v))
        # print(np.dot(n_gk, g_v))
        g_stütz = [g_sx, g_sy, g_sz] = punkt_a + Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)) * g_v
        g_richtung = [g_rx, g_ry, g_rz] = Rational(-1 * np.dot(n_gk, k_v), np.dot(n_gk, g_v)) * g_v + k_v

        lsg = (gzahl(np.dot(punkt_a, n_gk)) + vorz_str(np.dot(n_gk, g_v)) + 'r'
               + vorz_str(np.dot(n_gk, k_v)) + 's ~=~' + gzahl(np.dot(punkt_d, n_gk)) + r' \quad \vert '
               + vorz_str(-1 * np.dot(punkt_a, n_gk)) + r' \quad \vert ' + vorz_str(-1 * np.dot(n_gk, k_v))
               + r's \quad \to \quad ' + gzahl(np.dot(n_gk, g_v)) + 'r ~=~'
               + gzahl(np.dot(punkt_d - punkt_a, n_gk)) + vorz_str(np.dot(n_gk, k_v))
               + r's \quad \vert \div' + gzahl_klammer(np.dot(n_gk, g_v)) + r' \quad (2P) \\ r ~=~'
               + gzahl(Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)))
               + vorz_str(Rational(-1 * np.dot(n_gk, k_v), np.dot(n_gk, g_v)))
               + r's \quad \mathrm{Die~Ebene~F~liegt~in~der~Ebene~E. \quad (2P) } \\'
               + r' \quad \mathrm{Schnittgerade~bestimmen,~indem~man~r~in~F~einsetzt} \\'
               + r' \overrightarrow{x} ~=~ \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az)
               + r' \\' + r' \end{pmatrix} ~+~ (' + gzahl(Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)))
               + vorz_str(Rational(np.dot(n_gk, k_v), np.dot(n_gk, g_v))) + r's) \cdot \begin{pmatrix} ' + gzahl(g_vx)
               + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\' + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
               + gzahl(k_vx) + r' \\' + gzahl(k_vy) + r' \\' + gzahl(k_vz) + r' \\'
               + r' \end{pmatrix} ~=~ \begin{pmatrix}' + gzahl(g_sx) + r' \\' + gzahl(g_sy) + r' \\' + gzahl(g_sz)
               + r' \\' + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}' + gzahl(g_rx) + r' \\' + gzahl(g_ry) + r' \\'
               + gzahl(g_rz) + r' \\' + r' \end{pmatrix} \quad (2P) \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')

    elif F_in_E == 'parallel' or 'd' in teilaufg:
        punkte = 4
        abstand = zzahl(1, 7) / 2
        punkt_a = [ax, ay, az] = vektor_ganzzahl(punkt_d + abstand * np.array(n_gk))
        punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_a + zzahl(1, 3) * np.array(v))
        punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_a - zzahl(1, 3) * np.array(u))
        g_v = [g_vx, g_vy, g_vz] = np.array(punkt_b - punkt_a)
        k_v = [k_vx, k_vy, k_vz] = np.array(punkt_c - punkt_a)

        lsg = (gzahl(np.dot(punkt_a, n_gk)) + '~=~' + gzahl(np.dot(punkt_d, n_gk))
               + r' \quad \mathrm{f.A. \quad Die~Ebene~F~ist~parallel~zur~Ebene~E. \quad (2P) } \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')

    if F_in_E not in (None,'identisch', 'parallel', 'schneiden'):
        exit("F_in_E muss None, 'identisch', 'parallel' oder 'schneiden' sein.")

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Ebenen E und F mit',
               r' E: ~' + vorz_v_aussen(nx_gk, 'x') + vorz_v_innen(ny_gk,'y') + vorz_v_innen(nz_gk, 'z ~=~')
               + gzahl(np.dot(punkt_d, n_gk))
               + r' \quad \mathrm{und} \quad F: \overrightarrow{x} ~=~ \begin{pmatrix} '
               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
               + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
               + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
               + gzahl(k_vx) + r' \\' + gzahl(k_vy) + r' \\' + gzahl(k_vz) + r' \\'
               + r' \end{pmatrix} ']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # lagebeziehungen zwischen zwei Ebenen erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)
        aufgabe.append(str(teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen zweier Ebenen '
                                          'und deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Ebenen:'), 'Punkte')
        table1.add_row('', '-', 'sind parallel, d.h. die Normalenvektoren der Ebenen sind parallel und '
                                'sie haben keine gemeinsamen Punkte', '2P')
        table1.add_row('', '-', 'sind identisch, d.h. die Normalenvektoren der Ebenen sind parallel und '
                                'sie haben alle Punkte gemeinsam', '2P')
        table1.add_row('', '-', 'schneiden sich, d.h. die Normalenvektoren der Ebenen sind nicht parallel und '
                                'die gemeinsamen Punkte liegen auf einer Geraden ', '2P')
        table1.add_row('','','', 'insg.: ' + str(punkte) + ' P')
        loesung.append(table1)
        i += 1

    if 'b' in teilaufg:
        # Lagebeziehung bestimmen und ggf. Schnittegrade berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Bestimmen Sie die Lagebeziehung der Ebenen E und F '
                                                f'und berechnen Sie ggf. die Schnittgerade. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(nx_gk) + r' \cdot (' + gzahl(ax)
                       + vorz_str(g_vx) + 'r' + vorz_str(k_vx) + 's)' + vorz_str(ny_gk) + '(' + gzahl(ay)
                       + vorz_str(g_vy) + 'r' + vorz_str(k_vy) + 's)' + vorz_str(nz_gk) + '(' + gzahl(az)
                       + vorz_str(g_vz) + 'r' + vorz_str(k_vz) + 's) ~=~ ' + gzahl(np.dot(punkt_d, n_gk))
                       + r' \quad (1P) \\' + gzahl(nx_gk * ax) + vorz_v_innen(nx_gk * g_vx, 'r')
                       + vorz_v_innen(nx_gk * k_vx, 's') + vorz_str(ny_gk * ay) + vorz_v_innen(ny_gk * g_vy, 'r')
                       + vorz_v_innen(ny_gk * k_vy, 's') + vorz_str(nz_gk * az) + vorz_v_innen(nz_gk * g_vz, 'r')
                       + vorz_v_innen(nz_gk * k_vz, 's ~=~ ') + gzahl(np.dot(punkt_d, n_gk)) + r'\quad (1P) \\'
                       + lsg)
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # hessische Normalenform der Ebene aufstellen
        punkte = 4
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        liste_punkte.append(punkte)
        punkt_aE = [ax_E, ay_E, az_E] = np.array([Rational(np.dot(punkt_d, n_gk), nx_gk), 0, 0])
        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                       + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk)
                       + r')^2 } ~=~ ' + ergebnis_n0
                       + r' \quad \to \quad ' + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                       + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                       + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} ~=~0 \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
        i += 1

        if 'd' in teilaufg:
            # hier soll der Abstand zwischen zwei parallelen Ebenen berechnet werden
            punkte = 3
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            liste_punkte.append(punkte)
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand der Ebenen E und F. \n\n')
            if 'c' not in teilaufg:
                punkte =+ 4
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                               + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk)
                               + r')^2 } ~=~ ' + ergebnis_n0
                               + r' \quad \to \quad ' + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} ~=~0 \quad (4P) \\' + r' d~=~ \left| \begin{bmatrix}'
                               + r' \begin{pmatrix}' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_a - punkt_aE), 1 / n_betrag * n_gk), 3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad d~=~ \left| \begin{bmatrix}'
                               + r' \begin{pmatrix}' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_a - punkt_aE), 1 / n_betrag * n_gk), 3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~Punkte} \\')
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]