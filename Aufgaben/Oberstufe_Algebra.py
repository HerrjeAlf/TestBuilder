from pylatex.utils import bold
import string, sys
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure, MultiColumn
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.vector import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *


# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

# Berechnung für die Aufgaben
def punkte_und_vektoren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ks=None, i=0, BE=[]):
    # Aufgabe zur Darstellung von Punkten im 3-dim-Kordinatensystem und Vektorechnung.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Der Parameter "ks=" legt fest, ob die Aufgabe ein leeres dreidimensionales Koordinatensystem oder kariertes Papier enthält. Der Parameter kann "None", "True" oder "False" sein". Standardmäßig ist "ks=None" und somit gibt kein Koordinatensystem und kein kariertes Papier.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    def zf_vorz(q):
        return random.choice([-1, 1]) * q
    ortsvektor_a = [ax, ay, az] = punkt_vektor(3)
    vektor_ab = [abx, aby, abz] = punkt_vektor(4)
    laenge_vektor_ab = (r' \sqrt{' + gzahl(sum(a*a for a in vektor_ab)) + '}'
                        + '~=~' + gzahl(N(sqrt(sum(a*a for a in vektor_ab)),3)))
    ortsvektor_b = np.array(ortsvektor_a) + np.array(vektor_ab)
    vektoren_auswahl = [[zf_vorz(abx), zf_vorz(abz), zf_vorz(aby)],
                        [zf_vorz(aby), zf_vorz(abz), zf_vorz(abx)],
                        [zf_vorz(aby), zf_vorz(abx), zf_vorz(abz)],
                        [zf_vorz(abz), zf_vorz(abx), zf_vorz(aby)],
                        [zf_vorz(abz), zf_vorz(aby), zf_vorz(abx)]]



    if random.random() < 0.5:
        vektor_ac = [acx, acy, acz] = random.choice(vektoren_auswahl)
        while vektor_vergleich(vektor_ac, vektor_ab) == True:
            vektor_ac = [acx, acy, acz] = random.choice(vektoren_auswahl)
        laenge_vektor_ac = (r' \sqrt{' + gzahl(sum(a * a for a in vektor_ac)) + '}' + '~=~'
                            + gzahl(N(sqrt(sum(a * a for a in vektor_ac)), 3)))
        ortsvektor_c = np.array(ortsvektor_a) + np.array(vektor_ac)
        ortsvektor_d = np.array(ortsvektor_c) - np.array(vektor_ab)
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
                     + r'  \end{pmatrix}  \quad (3P) \\')
    else:
        vektor_bc = random.choice(vektoren_auswahl)
        while vektor_vergleich(vektor_bc, vektor_ab) == True:
            vektor_bc = random.choice(vektoren_auswahl)
        laenge_vektor_bc = (r' \sqrt{' + gzahl(sum(a*a for a in vektor_bc)) + '}' + '~=~'
                            + gzahl(N(sqrt(sum(a*a for a in vektor_bc)),3)))
        ortsvektor_c = np.array(ortsvektor_b) + np.array(vektor_bc)
        vektor_ac = [acx, acy, acz] = ortsvektor_c - ortsvektor_a
        laenge_vektor_ac = (r' \sqrt{' + gzahl(sum(a * a for a in vektor_ac)) + '}' + '~=~'
                            + gzahl(N(sqrt(sum(a * a for a in vektor_ac)), 3)))
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
                     + r'  \end{pmatrix}  \quad (3P) \\')

    # print('a = ' + str(ortsvektor_a)), print('b = ' + str(ortsvektor_b)), print('c = ' + str(ortsvektor_c))
    # print('d=' + str(ortsvektor_d)), print(vektor_ab), print(vektor_ac)
    if len([element for element in ['g', 'h'] if element in teilaufg]) > 0:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Punkte '
                   + 'A( ' + gzahl(ortsvektor_a[0]) + ' | ' + gzahl(ortsvektor_a[1]) + ' | ' + gzahl(ortsvektor_a[2]) + ' ), '
                   + 'B( ' + gzahl(ortsvektor_b[0]) + ' | ' + gzahl(ortsvektor_b[1]) + ' | ' + gzahl(ortsvektor_b[2]) + ' ), '
                   + 'C( ' + gzahl(ortsvektor_c[0]) + ' | ' + gzahl(ortsvektor_c[1]) + ' | ' + gzahl(ortsvektor_c[2]) + ' ) ']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Punkte '
                   + 'A( ' + gzahl(ortsvektor_a[0]) + ' | ' + gzahl(ortsvektor_a[1]) + ' | ' + gzahl(ortsvektor_a[2]) + ' ), '
                   + 'B( ' + gzahl(ortsvektor_b[0]) + ' | ' + gzahl(ortsvektor_b[1]) + ' | ' + gzahl(ortsvektor_b[2]) + ' ) und '
                   + 'C( ' + gzahl(ortsvektor_c[0]) + ' | ' + gzahl(ortsvektor_c[1]) + ' | ' + gzahl(ortsvektor_c[2]) + ' ). \n\n']

    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        pkt = 2
        # Punkte im 3-dim-Koordinatensystem einzeichnen und verbinden
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if ks == True:
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichnen Sie die Punkte A, B und C im Koordinatensystem ein '
                                              f'und verbinden diese. \n\n')
        else:
            aufgabe.append(str(liste_teilaufg[i]) + f') Zeichnen Sie die Punkte A, B und C in einem Koordinatensystem ein '
                                              f'und verbinden diese. \n\n')
            pkt += 2
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Punkte~(1P),~Seiten~vom~Dreieck~(1P)}')
        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Abstände von Punkten berechnen und vergleichen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 5
        aufgabe.append(str(liste_teilaufg[i]) + f') Weisen Sie nach, dass das Dreieck ABC gleichschenklig ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + (r') \quad ~ \overrightarrow{AB} ~=~ \begin{pmatrix}'
                                           + gzahl(vektor_ab[0]) + r' \\' + gzahl(vektor_ab[1]) + r' \\'
                                           + gzahl(vektor_ab[2]) + r' \\ \end{pmatrix} \to \mathrm{d(A,B)~=~} \sqrt{('
                                           + gzahl(vektor_ab[0]) + ')^2 ~+~(' + gzahl(vektor_ab[1]) + ')^2 ~+~('
                                           + gzahl(vektor_ab[2]) + ')^2 } ~=~' + laenge_vektor_ab + r' \quad (2P) \\'
                                           + loesung_1 + r' \mathrm{Die~beiden~Seiten~sind~gleichlang,'
                                           + r'~somit~ist~das~Dreieck~gleichschenklig.} \quad (1P) \\'
                                           + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}'))

        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # mithilfe von Vektorrechnung einen vierten Punkt für ein Parallelogramm berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        aufgabe.append(str(liste_teilaufg[i]) + (f') Bestimmen Sie einen Punkt D so, dass die Punkte A,B,C und D'
                                           + f' das Parallelogramm ABCD bilden.'))
        loesung.append(str(liste_teilaufg[i]) + loesung_2 + r' \mathrm{Punkt~D~hat~die~Koordinaten:~}~D('
                       + gzahl(ortsvektor_d[0]) + ' | ' + gzahl(ortsvektor_d[1]) + ' | ' + gzahl(ortsvektor_d[2])
                       + r') \quad (1P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # Hier sollen die SuS mithilfe des Skalarproduktes die Fläche des Dreiecks ABC ausrechnen
        sprod = skalarprodukt(vektor_ab, vektor_ac)
        diskr_ab = sum(a * a for a in vektor_ab)
        diskr_ac = sum(a * a for a in vektor_ac)
        erg = N(0.5 * sqrt(diskr_ab*diskr_ac-sprod**2),3)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Fläche des Dreiecks ABC mithilfe des '
                       f'Skalarproduktes. \n\n')
        if 'b' in teilaufg:
            pkt = 3
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A~=~ \frac{1}{2} \sqrt{{ \left| \overrightarrow{AB} \right| }^2 \cdot '
                           + r' { \left| \overrightarrow{AC} \right| }^2 - { \left( \overrightarrow{AB} \cdot '
                           + r' \overrightarrow{AC} \right) }^2 }~=~ \frac{1}{2} \sqrt{{ \left( \sqrt{'
                           + gzahl(diskr_ab) + r'} \right) }^2 \cdot { \left( \sqrt{' + gzahl(diskr_ac)
                           + r'} \right) }^2 - \left( ' + gzahl(N(sprod,3)) + r' \right) ^2 } ~=~' + gzahl(erg)
                           + r' \quad (3BE) ')
        else:
            pkt = 5
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A~=~ \frac{1}{2} \sqrt{{ \left| \overrightarrow{AB} \right| }^2 \cdot '
                           + r' { \left| \overrightarrow{AC} \right| }^2 - { \left( \overrightarrow{AB} \cdot '
                           + r' \overrightarrow{AC} \right) }^2 } \quad (1BE) \hspace{10em} \\ '
                           + r' \overrightarrow{AB} ~=~ \begin{pmatrix} ' + gzahl(vektor_ab[0]) + r' \\'
                           + gzahl(vektor_ab[1]) + r' \\' + gzahl(vektor_ab[2]) + r' \\ '
                           + r' \end{pmatrix} ~ \to ~ \left| \overrightarrow{AB} \right| ~=~ '
                           + laenge_vektor_ab + r' \quad \mathrm{sowie} \quad \overrightarrow{AC} ~=~ \begin{pmatrix}'
                           + gzahl(vektor_ac[0]) + r' \\' + gzahl(vektor_ac[1]) + r' \\' + gzahl(vektor_ac[2]) + r' \\'
                           + r' \end{pmatrix} ~ \to ~ \left| \overrightarrow{AC} \right| ~=~ ' + laenge_vektor_ac
                           + r' \\ A ~=~ \frac{1}{2} \sqrt{{ \left( \sqrt{' + gzahl(diskr_ab)
                           + r'} \right) }^2 \cdot { \left( \sqrt{' + gzahl(diskr_ac) + r'} \right) }^2 - \left( '
                           + gzahl(N(sprod, 3)) + r' \right) ^2} ~=~' + gzahl(erg) + r' \quad (4BE)')
        liste_punkte.append(pkt)
        i += 1

    if 'e' in teilaufg:
        # Hier sollen die SuS mithilfe des Kreuzproduktes die Fläche des Dreiecks ABC ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        kprod = [kx, ky, kz] = np.cross(vektor_ab, vektor_ac)
        laenge_kprod =  N(sqrt(sum(a*a for a in kprod)),3)
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Fläche des Dreiecks ABC mithilfe des '
                       + f'Kreuzproduktes. \n\n')
        if len([element for element in ['b', 'd'] if element in teilaufg]) > 0:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A ~=~ \frac{1}{2} \cdot \left| \overrightarrow{AB} \times \overrightarrow{AC} \right| '
                           + r'~=~ \frac{1}{2} \cdot \left| \begin{pmatrix} ' + gzahl(kx) + r' \\' + gzahl(ky)
                           + r' \\' + gzahl(kz) + r' \\ ' + r' \end{pmatrix} \right| ~=~ \frac{1}{2} \cdot '
                           + gzahl(laenge_kprod) + '~=~' + gzahl(N(0.5*laenge_kprod,3)) + r' \quad (3BE)')
            pkt = 3
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A ~=~ \frac{1}{2} \cdot \left| \overrightarrow{AB} \times \overrightarrow{AC} \right| '
                           + r' \quad (1BE) \hspace{10em} \\ \overrightarrow{AB} ~=~ \begin{pmatrix} '
                           + gzahl(vektor_ab[0]) + r' \\' + gzahl(vektor_ab[1]) + r' \\' + gzahl(vektor_ab[2])
                           + r' \\ ' + r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AC} ~=~ '
                           + r' \begin{pmatrix}' + gzahl(vektor_ac[0]) + r' \\' + gzahl(vektor_ac[1]) + r' \\'
                           + gzahl(vektor_ac[2]) + r' \\ \end{pmatrix} \quad \to \quad '
                           + r' A ~=~ \frac{1}{2} \cdot \left| \begin{pmatrix} ' + gzahl(kx) + r' \\' + gzahl(ky)
                           + r' \\' + gzahl(kz) + r' \\ \end{pmatrix} \right| ~=~ \frac{1}{2} \cdot '
                           + gzahl(laenge_kprod) + '~=~' + gzahl(N(0.5*laenge_kprod,3)) + r' \quad (4BE)')
            pkt = 5
        liste_punkte.append(pkt)
        i += 1

    if 'f' in teilaufg:
        # mithilfe des Kreuzproduktes die Fläche des Parallelogramms ABCD ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        kprod = [kx, ky, kz] = np.cross(vektor_ab, vektor_ac)
        laenge_kprod = N(sqrt(sum(a * a for a in kprod)), 3)
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Fläche des Parallelogramms ABCD mithilfe des '
                       + f'Kreuzproduktes. \n\n')
        if len([element for element in ['b', 'd', 'e'] if element in teilaufg]) > 0:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A ~=~ \left| \overrightarrow{AB} \times \overrightarrow{AC} \right| '
                           + r'~=~ \left| \begin{pmatrix} ' + gzahl(kx) + r' \\' + gzahl(ky)
                           + r' \\' + gzahl(kz) + r' \\ ' + r' \end{pmatrix} \right| ~=~ '
                           + gzahl(laenge_kprod) + r' \quad (3BE)')
            pkt = 3
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Die~Fläche~wird~berechnet~mit:} \quad'
                           + r' A ~=~ \left| \overrightarrow{AB} \times \overrightarrow{AC} \right| '
                           + r' \quad (1BE) \hspace{10em} \\ \overrightarrow{AB} ~=~ \begin{pmatrix} '
                           + gzahl(vektor_ab[0]) + r' \\' + gzahl(vektor_ab[1]) + r' \\' + gzahl(vektor_ab[2])
                           + r' \\ ' + r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AC} ~=~ '
                           + r' \begin{pmatrix}' + gzahl(vektor_ac[0]) + r' \\' + gzahl(vektor_ac[1]) + r' \\'
                           + gzahl(vektor_ac[2]) + r' \\ \end{pmatrix} \quad \to \quad '
                           + r' A ~=~ \left| \begin{pmatrix} ' + gzahl(kx) + r' \\' + gzahl(ky)
                           + r' \\' + gzahl(kz) + r' \\ \end{pmatrix} \right| ~=~ ' + gzahl(laenge_kprod)
                           + r' \quad (4BE)')
            pkt = 5
        liste_punkte.append(pkt)
        i += 1

    if 'g' in teilaufg:
        # mithilfe des Kreuz- und Skalarproduktes das Volumen eines Quaders ABCE (Spat) ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        kprod = [kx, ky, kz] = np.cross(vektor_ab, vektor_ac)
        kprod_gek = vektor_kuerzen(kprod)
        punkt_e = [ex, ey, ez] = ortsvektor_a + zzahl(1,4) / 2 * vektor_ab + kprod_gek
        vektor_ae = [aex,aey,aez] = [ex - ax, ey - ay, ez - az]
        erg = N(abs(skalarprodukt(kprod, vektor_ae)),3)
        if len([element for element in ['a', 'b', 'c', 'd', 'e', 'f'] if element in teilaufg]) > 0:
            aufgabe.extend(('Gegeben ist ein weiterer Punkt E( ' + gzahl(ex) + ' | ' + gzahl(ey) + ' | ' + gzahl(ez)
                            + '), der mit den Punkten A, B und C ein Spat bildet. \n\n',
                            str(liste_teilaufg[i]) + f') Berechnen Sie das Volumen des Spates. \n\n'))
        else:
                aufgabe.extend(('und ein weiterer \n Punkt E( ' + gzahl(ex) + ' | ' + gzahl(ey) + ' | ' + gzahl(ez)
                                + '), der mit den Punkten A, B und C ein Spat bildet. \n\n',
                                str(liste_teilaufg[i]) + f') Berechnen Sie das Volumen des Spates. \n\n'))

        if len([element for element in ['b', 'd', 'e', 'f'] if element in teilaufg]) > 0:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Das~Volumen~wird~berechnet~mit:} \quad'
                           + r' V ~=~ \left| \left( \overrightarrow{AB} \times \overrightarrow{AC} \right) \cdot '
                           + r' \overrightarrow{AE} \right| ~=~ \left| \begin{pmatrix} ' + gzahl(kx)
                           + r' \quad (1BE) \\' + gzahl(ky) + r' \\' + gzahl(kz) + r' \\ '
                           + r' \end{pmatrix} \cdot \begin{pmatrix} ' + gzahl(aex) + r' \\' + gzahl(aey) + r' \\'
                           + gzahl(aez) + r' \\ ' + r' \end{pmatrix} \right| ~=~ ' + gzahl(erg) + r' \quad (4BE)')
            pkt = 5
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Das~Volumen~wird~berechnet~mit:} \quad'
                           + r' V ~=~ \left| \left( \overrightarrow{AB} \times \overrightarrow{AC} \right) \cdot '
                           + r' \overrightarrow{AE}  \right| \hspace{10em} \quad (1BE) \\ \overrightarrow{AB} ~=~ '
                           + r'\begin{pmatrix} ' + gzahl(abx) + r' \\' + gzahl(aby) + r' \\' + gzahl(abz) + r' \\ '
                           + r' \end{pmatrix} , \quad \overrightarrow{AC} ~=~ '
                           + r' \begin{pmatrix}' + gzahl(acx) + r' \\' + gzahl(acy) + r' \\' + gzahl(acz)
                           + r' \\ \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AE} ~=~'
                           + r' \begin{pmatrix}' + gzahl(aex) + r' \\' + gzahl(aey) + r' \\'
                           + gzahl(aez) + r' \\ \end{pmatrix} \quad \to \quad V ~=~ \left| \begin{pmatrix} '
                           + gzahl(kx) + r' \\' + gzahl(ky) + r' \\' + gzahl(kz) + r' \\ '
                           + r' \end{pmatrix} \cdot \begin{pmatrix} ' + gzahl(aex) + r' \\' + gzahl(aey)
                           + r' \\' + gzahl(aez) + r' \\ ' + r' \end{pmatrix} \right| ~=~ ' + gzahl(erg)
                           + r' \quad (6BE)')
            pkt = 7
        liste_punkte.append(pkt)
        i += 1

    if 'h' in teilaufg:
        # mithilfe des Kreuz- und Skalarproduktes das Volumen einer Pyramide ABCS (Spat) ausrechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        kprod = [kx, ky, kz] = np.cross(vektor_ab, vektor_ac)
        kprod_gek = vektor_kuerzen(kprod)
        punkt_s = [sx, sy, sz] = ortsvektor_a + 0.5 * (vektor_ab + vektor_ac) + kprod_gek
        vektor_as = [asx, asy, asz] = [sx - ax, sy - ay, sz - az]
        erg = Rational(abs(skalarprodukt(kprod, vektor_as)),6)
        if len([element for element in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if element in teilaufg]) > 0:
            aufgabe.extend(('Gegeben ist ein weiterer Punkt S( ' + gzahl(sx) + ' | ' + gzahl(sy) + ' | ' + gzahl(sz)
                            + '), der mit Dreieck ABC die dreiseitige Pyramide ABCS bildet. \n\n',
                            str(liste_teilaufg[i]) + f') Berechnen Sie das Volumen der Pyramide. \n\n'))
        else:
            aufgabe.extend(('sowie ein weiterer \n Punkt S( ' + gzahl(sx) + ' | ' + gzahl(sy) + ' | ' + gzahl(sz)
                            + '), der mit Dreieck ABC die dreiseitige Pyramide ABCS bildet. \n\n',
                            str(liste_teilaufg[i]) + f') Berechnen Sie das Volumen der Pyramide. \n\n'))
        if len([element for element in ['b', 'd', 'e', 'f', 'g'] if element in teilaufg]) > 0:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Das~Volumen~wird~berechnet~mit:} \quad'
                           + r' V ~=~ \frac{1}{6} \cdot \left| \left( \overrightarrow{AB} \times \overrightarrow{AC} '
                           + r' \right) \cdot \overrightarrow{AE} \right| ~=~ \frac{1}{6} \cdot \left| \begin{pmatrix} '
                           + gzahl(kx) + r' \\' + gzahl(ky) + r' \\' + gzahl(kz) + r' \\ '
                           + r' \end{pmatrix} \cdot \begin{pmatrix} ' + gzahl(asx) + r' \\' + gzahl(asy) + r' \\'
                           + gzahl(asz) + r' \\ ' + r' \end{pmatrix} \right| ~=~ ' + gzahl(erg) + r' \quad (5BE)')
            pkt = 5
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Das~Volumen~wird~berechnet~mit:} \quad'
                           + r' V ~=~ \frac{1}{6} \cdot \left| \left( \overrightarrow{AB} \times \overrightarrow{AC} '
                           + r' \right) \cdot \overrightarrow{AS}  \right| \quad (1BE) \hspace{10em} \\'
                           + r'\overrightarrow{AB} ~=~ \begin{pmatrix} ' + gzahl(abx) + r' \\' + gzahl(aby)
                           + r' \\' + gzahl(abz) + r' \\ ' + r' \end{pmatrix} , \quad \overrightarrow{AC} ~=~ '
                           + r' \begin{pmatrix}' + gzahl(acx) + r' \\' + gzahl(acy) + r' \\' + gzahl(acz)
                           + r' \\ \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AS} ~=~'
                           + r' \begin{pmatrix}' + gzahl(asx) + r' \\' + gzahl(asy) + r' \\'
                           + gzahl(asz) + r' \\ \end{pmatrix} \quad \to \quad V ~=~ \frac{1}{6} \cdot \left| '
                           + r' \begin{pmatrix} ' + gzahl(kx) + r' \\' + gzahl(ky) + r' \\' + gzahl(kz) + r' \\'
                           + r' \end{pmatrix} \cdot \begin{pmatrix} ' + gzahl(asx) + r' \\' + gzahl(asy)
                           + r' \\' + gzahl(asz) + r' \\ ' + r' \end{pmatrix} \right| ~=~ ' + gzahl(erg)
                           + r' \quad (6BE)')
            pkt = 7
        liste_punkte.append(pkt)
        i += 1

    if ks != None:
        if ks == True:
            grafiken_loesung = grafiken_aufgaben = ['3dim_Koordinatensystem']
            aufgabe.append(['Bild','300px'])
            loesung.append(['Bild','300px'])
        else:
            grafiken_loesung = grafiken_aufgaben = ['kariertes_Papier']
            aufgabe.append(['Bild','400px'])
            loesung.append(['Bild','400px'])

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def rechnen_mit_vektoren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], linearkombination=None, kollinear=None, i=0, BE=[]):
    # Aufgabe zum Rechnen mit Vektoren, Mittelpunkten, Linearkombination bzw. Kollinarität und Streckenverhältnissen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "linearkombination=" kann festgelegt werden, ob sich die Vektoren bei Teilaufgabe c) als Linearkombination darstellen lassen. Standardmäßig ist "linearkombination=None" und damit die Auswahl zufällig.  Er kann auch True oder False sein.
    # Mit dem Parameter "kollinear=" kann festgelegt werden, ob sich die Vektoren bei Teilaufgabe e) kollinear sind. Standardmäßig ist "linearkombination=None" und damit die Auswahl zufällig. Er kann auch True oder False sein.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

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
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den resultierenden Vektor.')
        aufgabe.append(gzahl(faktor_1) + r' \cdot \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\'
                       + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~'
                       + vorz_str(faktor_2) + r' \cdot' + r'  \begin{pmatrix} ' + gzahl(vektor_2[0]) + r' \\'
                       + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                       + r' \end{pmatrix} ~=~ \hspace{20em} \\')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(faktor_1) + r'  \cdot \begin{pmatrix} ' + gzahl(vektor_1[0])
                       + r' \\' + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~'
                       + vorz_str(faktor_2) + r' \cdot' + r'  \begin{pmatrix} ' + gzahl(vektor_2[0]) + r' \\'
                       + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} '
                       + gzahl(ergebnis[0]) + r' \\' + gzahl(ergebnis[1]) + r' \\' + gzahl(ergebnis[2]) + r' \\'
                       + r'  \end{pmatrix}  \quad (2P)')
        liste_punkte.append(2)
        i += 1

    if 'b' in teilaufg:
        # Mittelpunkt zweier gegebener Punkte berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        vektor_1 = punkt_vektor(5)
        vektor_2 = punkt_vektor(7)
        ergebnis = 0.5 * (np.array(vektor_1) + np.array(vektor_2))
        # print(ergebnis)
        punkte = 3

        aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie den Mittelpunkt der folgenden Punkte '
                       'A( ' + gzahl(vektor_1[0])  + ' | ' + gzahl(vektor_1[1]) + ' | ' + gzahl(vektor_1[2]) + ' ) und '
                       'B( ' + gzahl(vektor_2[0])  + ' | ' + gzahl(vektor_2[1]) + ' | ' + gzahl(vektor_2[2])
                       + ' ). \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{OM} ~=~ \frac{1}{2} \cdot \begin{pmatrix}'
                       + r'  \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\' + gzahl(vektor_1[1]) + r' \\'
                       + gzahl(vektor_1[2]) + r' \\' + r' \end{pmatrix} ~+~ \begin{pmatrix} ' + gzahl(vektor_2[0])
                       + r' \\' + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                       + r' \end{pmatrix} \end{pmatrix}  ~=~ \begin{pmatrix}' + gzahl(ergebnis[0]) + r' \\'
                       + gzahl(ergebnis[1]) + r' \\' + gzahl(ergebnis[2]) + r' \\'
                       + r' \end{pmatrix} \quad (2P) \\ \mathrm{Punkt~M~hat~die~Koordinaten:~}~M('
                       + gzahl(ergebnis[0]) + ' | ' + gzahl(ergebnis[1]) + ' | ' + gzahl(ergebnis[2])
                       + r') \quad (1P) \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # Linearkombination von Vektoren überprüfen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 9
        faktor_1, faktor_2 = random.randint(1,10)/2, random.randint(1,10)/2
        # print('r =' + gzahl(faktor_1)), print('s =' + gzahl(faktor_2))
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

        aufgabe.extend((str(liste_teilaufg[i]) + ') Überprüfen Sie, ob der gegebenen Vektor a als Linearkombination'
                        + ' von b und c dargestellt werden kann.',
                        r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(x_1) + r' \\' + gzahl(y_1) + r' \\'
                        + gzahl(z_1) + r' \\' + r' \end{pmatrix} ~,~ \overrightarrow{b} ~=~ \begin{pmatrix} '
                        + gzahl(x_2) + r' \\' + gzahl(y_2) + r' \\' + gzahl(z_2) + r' \\'
                        + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{c} ~=~\begin{pmatrix}'
                        + gzahl(x_3) + r' \\' + gzahl(y_3) + r' \\' + gzahl(z_3) + r' \\'
                        + r' \end{pmatrix} \\'))

        loesung_1 = (r' \mathrm{aus~I~folgt:} \quad ' + gzahl(x_1) + '~=~' + vorz_v_aussen(x_2,r' \cdot r')
                     + vorz_v_innen(x_3,'s') + r' \cdot \quad \to \quad r~=~'
                     + gzahl(Rational(x_1,x_2)) + vorz_str(Rational(-1*x_3,x_2))
                     + r' \cdot s \quad (2P) \\')

        if y_3 != 0:
            lsg_s = N((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2),3)
            lsg_r = N((x_1 / x_2) - (x_3/ x_2) * ((y_1 - (x_1*y_2)/x_2)/(y_3 - (x_3*y_2)/x_2)),3)
            loesung_1 = (loesung_1 + r' \mathrm{r~einsetzen~in~II} \quad ' + gzahl(y_1) + '~=~'
                         + gzahl(y_2) + r' \cdot \left(' + gzahl(Rational(x_1,x_2))
                         + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \right)'
                         + vorz_str(y_3) + r' \cdot s \quad (1P) \\'
                         + gzahl(y_1) + vorz_str(Rational(-1*x_1*y_2,x_2)) + r' ~=~ s \cdot \left('
                         + gzahl(Rational(-1*x_3*y_2,x_2)) + vorz_str(y_3)
                         + r' \right) \quad (1P) \quad \to \quad '
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
                         + gzahl(z_2) + r' \cdot \left(' + gzahl(Rational(x_1,x_2))
                         + vorz_str(Rational(-1*x_3,x_2)) + r' \cdot s \right)'
                         + vorz_str(z_3) + r' \cdot s \quad (2P) \\'
                         + gzahl(z_1) + vorz_str(Rational(-1* x_1*z_2,x_2)) + r' ~=~ s \cdot \left('
                         + gzahl(Rational(-1*x_3*z_2,x_2)) + vorz_str(z_3)
                         + r' \cdot s \right) \quad (2P) \quad \to \quad '
                         + r' s ~=~ ' + gzahl(Rational((z_1 - (x_1*z_2)/x_2),(z_3 - (x_3*z_2)/x_2)))
                         + r' \quad (1P) \quad  r~=~ '
                         + gzahl(N(x_1 / x_2 - (x_3/ x_2)*((z_1 + (x_1*z_2)/x_2)/(z_3 - (x_3*z_2)/x_2)),3))
                         + r' \quad (1P) \\ \mathrm{Einsetzen~in~II: ' + gzahl(y_1) + '~=~' + gzahl(lsg_r)
                         + r' \cdot ' + gzahl_klammer(y_2) + vorz_str(lsg_s) + r' \cdot ' + gzahl_klammer(y_3)
                         + r' ~=~ ' + gzahl(N(y_2*lsg_r+y_3*lsg_s,3)) + r'} \quad (1P)')
        else:
            pass

        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Überprüfe,~ob~der~gegebenen~Vektor~a~als~Linearkombination'
                       + r'~von~b~und~c~dargestellt~werden~kann.} \\' + r' \begin{pmatrix} ' + gzahl(x_1) + r' \\'
                       + gzahl(y_1) + r' \\' + gzahl(z_1) + r' \\' + r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                       + gzahl(x_2) + r' \\' + gzahl(y_2) + r' \\' + gzahl(z_2) + r' \\'
                       + r' \end{pmatrix}  ~+~s \cdot \begin{pmatrix}' + gzahl(x_3) + r' \\' + gzahl(y_3) + r' \\'
                       + gzahl(z_3) + r' \\' + r' \end{pmatrix} \quad (1P) \\' + loesung_1 + r' \\ ' + loesung_2
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'd' in teilaufg:
        # Parameter a für Linearkombination von Vektoren berechnen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 0
        faktor_1, faktor_2 = random.randint(1,10)/2, random.randint(1,10)/2
        # print('r =' + gzahl(faktor_1)), print('s =' + gzahl(faktor_2))
        vektor_a = [a1, a2, a3] = np.array(punkt_vektor(5))
        vektor_b = [b1, b2, b3] = np.array(punkt_vektor(5))
        vektor_c = [c1, c2, c3] = np.array(vektor_a * faktor_1) + np.array(vektor_b * faktor_2)
        while 0 in vektor_c:
            faktor_1, faktor_2 = random.randint(1, 10) / 2, random.randint(1, 10) / 2
            vektor_c = [c1, c2, c3] = np.array(vektor_a * faktor_1) + np.array(vektor_b * faktor_2)
        vektor_c_var = [c1, c2, 'a']
        rf = random.choice([[0,1,2], [1,0,2], [2,1,0]])
        vektor_1 = [x_1, y_1, z_1] = [vektor_a[rf[0]], vektor_a[rf[1]], vektor_a[rf[2]]]
        vektor_2 = [x_2, y_2, z_2] = [vektor_b[rf[0]], vektor_b[rf[1]], vektor_b[rf[2]]]
        vektor_3 = [x_3, y_3, z_3] = [vektor_c_var[rf[0]], vektor_c_var[rf[1]], vektor_c_var[rf[2]]]
        zl = ['I', 'II', 'III']

        table1 = Tabular('r r r r', row_height=1.2)
        table1.add_row(str(liste_teilaufg[i]) + ') aus den gegebenen Vektoren ergeben sich folgende Gleichungen: ',
                        'I:', NoEscape('$' + vorz_v_aussen(x_1,'r') + vorz_v_innen(x_2,'s') + ' = '
                                                 + gzahl(x_3) + '$'), '(1P)')
        table1.add_row('', 'II:', NoEscape('$' + vorz_v_aussen(y_1,'r') + vorz_v_innen(y_2,'s')
                                                           + ' = ' + gzahl(y_3) + '$'), '(1P)')
        table1.add_row('', 'III:', NoEscape('$' + vorz_v_aussen(z_1,'r') + vorz_v_innen(z_2,'s')
                                                           + ' = ' + gzahl(z_3) + '$'),'(1P)')
        loesung.append(table1)
        punkte += 3
        if faktor_1 == 1:
            lsg_1 = (r' \mathrm{aus~' + zl[rf[0]] + r'~folgt:} \quad ' + vorz_v_aussen(a1,'r') + vorz_v_innen(b1,'s')
                     + '~=~' + gzahl(c1) + r' \quad \vert ' + vorz_v_innen(-1*b1,'s') + r' \quad \to \quad r~=~'
                     + gzahl(c1) + vorz_v_innen(-1*b1,'s') + r' \quad (2P) \\')
            punkte += 2
            lsg_2 = (r'  \mathrm{r~in~' + zl[rf[1]] + r'~einsetzen:} \quad ' + gzahl(a2) + r' \cdot \left( ' + gzahl(c1)
                     + vorz_v_innen(-1*b1,'s') + r' \right) ' + vorz_v_innen(b2,'s') + '~=~' + gzahl(c2)
                     + r' \quad \to \quad ' + gzahl(a2*c1) + vorz_v_innen(-1*a2*b1, 's') + vorz_v_innen(b2,'s')
                     + '~=~' + gzahl(c2) + r' \quad (2P) \\' + gzahl(a2*c1) + vorz_v_innen(-1*a2*b1+b2, 's')
                     + '~=~' + gzahl(c2) + r' \quad \vert' + vorz_str(-1*a2*c1) + r' \quad \vert \div '
                     + gzahl_klammer(-1*a2*b1+b2) + r' \quad \to \quad s~=~' + gzahl(faktor_2)
                     + r' \quad \to \quad r~=~' + gzahl(c1) + vorz_str(-1*b1) + r' \cdot ' + gzahl_klammer(faktor_2)
                     + '~=~' + gzahl(faktor_1) + r' \quad (2P) \\')
            punkte += 4

        else:
            lsg_1 = (r' \mathrm{aus~' + zl[rf[0]] + r'~folgt:} \quad ' + vorz_v_aussen(a1,'r') + vorz_v_innen(b1,'s')
                     + '~=~' + gzahl(c1) + r' \quad \vert ' + vorz_v_innen(-1*b1,'s') + r' \quad \vert \div '
                     + gzahl_klammer(a1) + r' \quad \to \quad r~=~' + gzahl(Rational(c1,a1))
                     + vorz_v_innen(Rational(-1*b1,a1),'s') + r' \quad 2P) \\')
            punkte += 2
            lsg_2 = (r' \mathrm{r~in~' + zl[rf[1]] + r'~einsetzen:} \quad ' + gzahl(a2) + r' \cdot \left( '
                     + gzahl(Rational(c1,a1)) + vorz_v_innen(Rational(-1*b1,a1),'s') + r' \right) '
                     + vorz_v_innen(b2,'s') + '~=~' + gzahl(c2)
                     + r' \quad \to \quad ' + gzahl(Rational(a2*c1,a1)) + vorz_v_innen(Rational(-1*a2*b1,a1), 's')
                     + vorz_v_innen(b2,'s') + '~=~' + gzahl(c2) + r' \quad (2P) \\' + gzahl(Rational(a2*c1,a1))
                     + vorz_v_innen(Rational(-1*a2*b1,a1)+b2, 's') + '~=~' + gzahl(c2) + r' \quad \to \vert'
                     + vorz_str(Rational(-1*a2*c1,a1)) + r' \quad \vert \div '
                     + gzahl_klammer(Rational(-1*a2*b1,a1)+b2) + r' \quad \to \quad s~=~' + gzahl(faktor_2)
                     + r' \quad \to \quad r~=~' + gzahl(Rational(c1,a1)) + vorz_str(Rational(-1*b1,a1)) + r' \cdot '
                     + gzahl_klammer(faktor_2) + '~=~' + gzahl(faktor_1) + r' \quad (2P) \\')
            punkte += 4
        lsg_3 = (r' \mathrm{r ~=~ ' + gzahl(faktor_1) + r' \quad und \quad s~=~' + gzahl(faktor_2) + r' \quad in ~ '
                 + zl[rf[2]] + r'~einsetzen: \quad } \\ ' + gzahl(a3) + r' \cdot ' + gzahl_klammer(faktor_1)
                 + vorz_str(b3) + r' \cdot ' + gzahl_klammer(faktor_2)
                 + r'~=~a \quad \to \quad \mathrm{für \quad a ~=~' + gzahl(c3)
                 + r' \quad sind~die~Vektoren~lin.~abhängig. \quad (2P) }')
        punkte += 2

        aufgabe.extend((str(liste_teilaufg[i]) + ') Berechnen Sie den Wert des Parameters a, '
                        + 'für den die gegebenen Vektoren linear abhängig sind.',
                        r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(x_1) + r' \\' + gzahl(y_1) + r' \\'
                        + gzahl(z_1) + r' \\' + r' \end{pmatrix} ~,~ \overrightarrow{b} ~=~ \begin{pmatrix} '
                        + gzahl(x_2) + r' \\' + gzahl(y_2) + r' \\' + gzahl(z_2) + r' \\'
                        + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{c} ~=~\begin{pmatrix}'
                        + gzahl(x_3) + r' \\' + gzahl(y_3) + r' \\' + gzahl(z_3) + r' \\'
                        + r' \end{pmatrix} \\'))
        loesung.append(lsg_1+lsg_2+lsg_3)
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
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
            vektor_1 = (faktor*vektor_2[0],faktor*vektor_2[1],faktor * vektor_2[2] + zzahl(1,6)/2)
            ergebnis = r' \mathrm{Die~Vektoren~sind~nicht~kollinear.} '

        aufgabe.extend((str(liste_teilaufg[i]) + f') Prüfen Sie, ob die gegebenen Vektoren kollinear sind.',
                        r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(vektor_1[0]) + r' \\'
                        + gzahl(vektor_1[1]) + r' \\' + gzahl(vektor_1[2]) + r' \\'
                        + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{b} ~=~ \begin{pmatrix} '
                        + gzahl(vektor_2[0]) + r' \\' + gzahl(vektor_2[1]) + r' \\' + gzahl(vektor_2[2]) + r' \\'
                        + r' \end{pmatrix} \\'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Prüfen~Sie,~ob~die~gegebenen~Vektoren~kollinear~sind.} \\'
                       + gzahl(N(vektor_1[0],3)) + '~=~' + gzahl(vektor_2[0]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[0]/vektor_2[0],3)) + r' \\' + gzahl(N(vektor_1[1],3)) + '~=~'
                       + gzahl(vektor_2[1]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[1]/vektor_2[1],3)) + r' \\' + gzahl(N(vektor_1[2],3)) + '~=~'
                       + gzahl(vektor_2[2]) + r' \cdot r \quad \to \quad r~=~'
                       + gzahl(N(vektor_1[2]/vektor_2[2],3)) + r' \\' + ergebnis
                       + r' \quad \to \quad \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        # Berechnen des Streckenverhältnisses, in die ein Punkt T eine Strecke teilt
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 4
        vektor_a = punkt_vektor(5)
        vektor_ab = punkt_vektor(5)
        vektor_b = np.array(vektor_a) + np.array(vektor_ab)
        faktor = nzahl(1,9)
        vektor_t = [vektor_a[0] + vektor_ab[0]*faktor/10,
                    vektor_a[1] + vektor_ab[1]*faktor/10,
                    vektor_a[2] + vektor_ab[2]*faktor/10]
        vektor_at = np.array(vektor_t) - np.array(vektor_a)
        vektor_tb = vektor_b - np.array(vektor_t)
        aufgabe.append(str(liste_teilaufg[i]) + ') In welchem Verhältnis teilt der Punkt T die Strecke AB?')
        aufgabe.append(r' \mathrm{A(~' + gzahl(vektor_a[0]) + r'~ \vert ~' + gzahl(vektor_a[1]) + r'~ \vert ~'
                       + gzahl(vektor_a[2]) + r'~ ), \quad B(~' + gzahl(vektor_b[0]) + r'~ \vert ~' + gzahl(vektor_b[1])
                       + r'~ \vert ~' + gzahl(vektor_b[2]) + r'~) \quad und \quad T( ~' + gzahl(N(vektor_t[0],3))
                       + r'~ \vert ~' + gzahl(N(vektor_t[1],3)) + r'~ \vert ~' + gzahl(N(vektor_t[2],3))
                       + r'~ ).} \\')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Das~Verhältnis~entspricht~dem~Streckungsfaktor~r~}'
                       + r' \mathrm{der~Vektoren~ \overrightarrow{AT} ~und~ \overrightarrow{TB}.} \\'
                       + r' \overrightarrow{AT} ~=~ \begin{pmatrix} ' + gzahl(vektor_at[0]) + r' \\'
                       + gzahl(vektor_at[1]) + r' \\' + gzahl(vektor_at[2]) + r' \\ \end{pmatrix} \quad \mathrm{und} '
                       + r' \quad \overrightarrow{TB} ~=~ \begin{pmatrix} ' + gzahl(vektor_tb[0]) + r' \\'
                       + gzahl(vektor_tb[1]) + r' \\' + gzahl(vektor_tb[2]) + r' \\ \end{pmatrix} \quad \to \quad '
                       + r'  \begin{matrix}' + gzahl(vektor_at[0]) + '~=~' + gzahl(vektor_tb[0])
                       + r' \cdot r \quad \to \quad r~=~ \frac{' + gzahl(faktor) + '}{' + gzahl(10-faktor)
                       + r'} \\' + gzahl(vektor_at[1]) + r'~=~' + gzahl_klammer(vektor_tb[1])
                       + r' \cdot r \quad \to \quad r~=~ \frac{' + gzahl(faktor) + '}{' + gzahl(10-faktor)
                       + r'} \\' + gzahl(vektor_at[2]) + r'~=~' + gzahl_klammer(vektor_tb[2])
                       + r' \cdot r \quad \to \quad r~=~ \frac{' + gzahl(faktor) + '}{' + gzahl(10-faktor)
                       + r'} \\ \end{matrix} \\' + r' \mathrm{insgesamt~}' + str(punkte) + r'BE')
        # alternative Variante

        # laenge_vektor_at = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_at),4)) + '} ~=~'
        #                     + gzahl(sqrt(N(sum(a*a for a in vektor_at),3))))
        # ergebnis_at = sqrt(N(sum(a*a for a in vektor_at),3))
        # laenge_vektor_tb = (r' \sqrt{' + gzahl(N(sum(a*a for a in vektor_tb),3)) + '} ~=~'
        #                     + gzahl(N(sqrt(sum(a*a for a in vektor_tb)),3)))
        # ergebnis_tb = sqrt(N(sum(a*a for a in vektor_tb),3))
        # loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{d(A,T)~=~} \sqrt{(' + gzahl(vektor_t[0]) + vorz_str(-1*vektor_a[0])
        #                + ')^2 ~+~(' + gzahl(vektor_t[1]) + vorz_str(-1*vektor_a[1]) + ')^2 ~+~(' + gzahl(vektor_t[2])
        #                + vorz_str(-1*vektor_a[2]) + ')^2 } ~=~' + laenge_vektor_at + r' \quad (1P) \\'
        #                + r' \mathrm{d(T,B)~=~} \sqrt{(' + gzahl(vektor_b[0]) + vorz_str(-1*vektor_t[0])
        #                + ')^2 ~+~(' + gzahl(vektor_b[1]) + vorz_str(-1*vektor_t[1]) + ')^2 ~+~(' + gzahl(vektor_b[2])
        #                + vorz_str(-1*vektor_t[2]) + ')^2 } ~=~' + laenge_vektor_tb + r' \quad (1P) \\'
        #                + r' r~=~ \frac{ ' + gzahl(ergebnis_at) + '}{' + gzahl(ergebnis_tb) + '} ~=~'
        #                + gzahl(ergebnis_at/ergebnis_tb) + r' \quad (2P) \\'
        #                + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')

        liste_punkte.append(punkte)
        i += 1

    if 'g' in teilaufg:
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
        aufgabe.append(str(liste_teilaufg[i]) + ') Der Punkt T teilt die Strecke AB im Verhältnis r. Bestimme den Punkt B.')
        aufgabe.append(r' \mathrm{A(~' + gzahl(vektor_a[0]) + r'~ \vert ~' + gzahl(vektor_a[1]) + r'~ \vert ~'
                       + gzahl(vektor_a[2]) + r'~), \quad T(~' + gzahl(vektor_t[0]) + r'~ \vert ~' + gzahl(vektor_t[1])
                       + r'~ \vert ~' + gzahl(vektor_t[2]) + r'~) \quad und~r~=~' + gzahl(faktor_r) + r'.} \\')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{OB} = \overrightarrow{OA} ~+~ \overrightarrow{AT} '
                       + r' \cdot \mathrm{ (~1~+~ \frac{1}{r} ~)}  ~=~ \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
                       + gzahl(vektor_a[1]) + r' \\' + gzahl(vektor_a[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} '
                       + gzahl(N(vektor_at[0],3))+ r' \\' + gzahl(N(vektor_at[1],3)) + r' \\'
                       + gzahl(N(vektor_at[2],3)) + r' \\ \end{pmatrix} \cdot \left( ~1~+~ '
                       + gzahl(Rational(10-a1,a1)) + r' \right) \\ ~=~ \begin{pmatrix} ' + gzahl(vektor_a[0]) + r' \\'
                       + gzahl(vektor_a[1]) + r' \\' + gzahl(vektor_a[2]) + r' \\ \end{pmatrix} ~+~ \begin{pmatrix} '
                       + gzahl(N(vektor_at[0]*(1+(10-a1)/a1),3)) + r' \\'
                       + gzahl(N(vektor_at[1]*(1+(10-a1)/a1),3)) + r' \\'
                       + gzahl(N(vektor_at[2]*(1+(10-a1)/a1),3)) + r' \\'
                       + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(N(vektor_b[0],3)) + r' \\'
                       + gzahl(N(vektor_b[1],3)) + r' \\' + gzahl(N(vektor_b[2],3)) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad B(~' + gzahl(vektor_b[0]) + r'~ \vert ~' + gzahl(vektor_b[1])
                       + r'~ \vert ~' + gzahl(vektor_b[2]) + r' ~) \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        liste_punkte.append(punkte)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def vektoren_koll_ortho(nr, BE=[]):
    # Hier sollen die SuS Vektoren zuordnen, die kollinear oder orthogonal sind.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    i = 0
    vec_a = vec_b = vec_c = [ax, ay, az] = punkt_vektor(4)
    # Vektor der kollinear zu Vektor a ist
    fakt_a = zzahl(3, 10) / 2
    vec_k = [kx, ky, kz] = fakt_a * vec_a
    # Vektor der Orthogonal zu Vektor a ist
    vx, vy = zzahl(1, 3), zzahl(1, 3)  # x und y Koordinate von u kann frei gewählt werden
    vz = (ax * vx + ay * vy) / (-1* az)
    vec_s = [sx, sy, sz] = vektor_kuerzen([vx, vy, vz])
    # beliebige Vektoren
    while vektor_kollinear(vec_a, vec_b) == True or test_vektor_senk(vec_a, vec_b) == True:
        vec_b = [bx, by, bz] = punkt_vektor(3)
    while vektor_kollinear(vec_a, vec_c) == True or test_vektor_senk(vec_a, vec_c) == True or vektor_vergleich(vec_c, vec_b) == True:
        vec_c = [cx, cy, cz] = punkt_vektor(3)
    ausw = random.sample([vec_b, vec_c, vec_s, vec_k], 4)

    ausw_k = stelle(ausw, vec_k)
    ausw_s = stelle(ausw, vec_s)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               NoEscape(r'Nennen Sie alle Vektoren, die zum Vektor $ \overrightarrow{a} $ kollinear bzw. '
                        r'orthogonal sind. Begründen Sie ihre Zuordnung.'),
               r' \overrightarrow{a} ~=~ \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\'
               + gzahl(az) + r' \\' + r' \end{pmatrix} ~ ~ \overrightarrow{b} ~=~ \begin{pmatrix} '
               + gzahl(ausw[0][0]) + r' \\' + gzahl(ausw[0][1]) + r' \\' + gzahl(ausw[0][2]) + r' \\'
               + r' \end{pmatrix} ~ ~ \overrightarrow{c} ~=~\begin{pmatrix}'
               + gzahl(ausw[1][0]) + r' \\' + gzahl(ausw[1][1]) + r' \\' + gzahl(ausw[1][2]) + r' \\'
               + r' \end{pmatrix} ~ ~ \overrightarrow{d} ~=~\begin{pmatrix}'
               + gzahl(ausw[2][0]) + r' \\' + gzahl(ausw[2][1]) + r' \\' + gzahl(ausw[2][2]) + r' \\'
               + r' \end{pmatrix} ~ \mathrm{und} ~ \overrightarrow{e} ~=~\begin{pmatrix}'
               + gzahl(ausw[3][0]) + r' \\' + gzahl(ausw[3][1]) + r' \\' + gzahl(ausw[3][2]) + r' \\'
               + r' \end{pmatrix} \\']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}',
               r' \mathrm{Der~Vektor~ \overrightarrow{' + liste_teilaufg[ausw_k+1] + '} ~ist~kollinear~zu~'
               + r'  \overrightarrow{a} ,~da:~} \begin{pmatrix}' + gzahl(kx) + r' \\' + gzahl(ky) + r' \\' + gzahl(kz)
               + r' \\' + r' \end{pmatrix} ~=~ ' + gzahl(fakt_a) + r' \cdot \begin{pmatrix} ' + gzahl(ax) + r' \\'
               + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} \quad (3P) \\'
               + r' \mathrm{Der~Vektor~ \overrightarrow{' + liste_teilaufg[ausw_s + 1] + '} ~ist~ortogonal~zu~'
               + r'  \overrightarrow{a} ,~da:~} ' + gzahl(ax) + r' \cdot ' + gzahl_klammer(sx) + '+' + gzahl_klammer(ay)
               + r' \cdot ' + gzahl_klammer(sy) + '+' + gzahl_klammer(az) + r' \cdot ' + gzahl_klammer(sz)
               + r' ~=~ 0 \quad (3P)']
    grafiken_aufgaben = []
    grafiken_loesung = []
    pkt = 6
    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [pkt]
        liste_punkte = BE
    else:
        liste_punkte = [pkt]


    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_aufstellen(nr, teilaufg=['a', 'b', 'c'], T_auf_g=False, spurpunkt=None, i=0, BE=[]):
    # Aufgabe zum Aufstellen von Geraden und Überprüfen der Lagebeziehung Punkt-Gerade.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "T_auf_g=" kann festgelegt werden, ob der Punkt T auf g liegt "T_auf_g=True" oder auch nicht "T_auf_g=False". Standardmäßig wird das zufällig ausgewählt.
    # Mit dem Parameter "spurpunkt=" kann für Teilaufgabe c) festgelegt werden, welcher Spurpunkt berechnet werden soll. Standardmäßig ist "spurpunkt=None" und die Auswahl zufällig. Er kann 'x-y', 'x-z', 'y-z' oder 'all' (für alle) sein.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    punkt_a = [ax, ay, az] = punkt_vektor(3)
    v = [vx, vy, vz] = punkt_vektor(4)
    punkt_b = [bx, by, bz] = punkt_a + v
    p = random.choice([0,1])
    punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1, 10) / 2) * np.array([vy, vx, vz + zzahl(1, 3)]))
    while (tx - ax) / vx == (ty - ay) / ty == (tz - az) / tz:
        punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1, 10) / 2) * np.array([vy, vx, vz + zzahl(1, 3)]))
    T_auf_g = random.choice([True, False]) if T_auf_g not in [None, True, False] else T_auf_g
    punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1, 30) / 5) * v) if T_auf_g else punkt_t
    lx, ly, lz = vektor_ganzzahl([(tx-ax)/vx, (ty-ay)/vy, (tz-az)/vz])
    if 'a' in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + gzahl(ax)  + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
                   'B( ' + gzahl(bx)  + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
                   'T( ' + gzahl(N(tx,3))  + ' | ' + gzahl(N(ty,3)) + ' | ' + gzahl(N(tz,3)) + ' ).  \n\n']
        if 'b' not in teilaufg:
            aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Punkte '
                       + 'A( ' + gzahl(ax) + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), '
                       + 'B( ' + gzahl(bx) + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) \n\n']
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
        loesung_1 = (r' \overrightarrow{AB} ~=~ \begin{pmatrix} ' + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\'
                     + gzahl(v[2]) + r' \\ \end{pmatrix} \quad \to \quad g: \overrightarrow{x} \ ~=~'
                     r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} ' + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\'
                     + gzahl(v[2]) + r' \\ \end{pmatrix} \quad (3P) \\')

        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                          f' welche die Punkte A und B enthält. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + loesung_1
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
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
            loesung_2 = r' \mathrm{Der~Punkt~liegt~auf~der~Geraden.} \quad (4BE) \\'
        else:
            loesung_2 = r' \mathrm{Der~Punkt~liegt~nicht~auf~der~Geraden.} \quad (4BE) \\'

        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T auf g liegt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + loesung_1 + loesung_2
                       + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE}')
        i +=1

    if 'c' in teilaufg:
        # Berechnung der Spurpunkte der Gerade mit den Koordinatenebenen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 0
        spurpunkt = random.choice(['x-y', 'x-z', 'y-z']) if spurpunkt not in ['x-y', 'x-z', 'y-z', 'all', None] else spurpunkt
        spurpunkt = random.choice(['x-y', 'x-z', 'y-z']) if spurpunkt == None else spurpunkt
        if spurpunkt == 'all':
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Spurpunkte der Geraden g mit den '
                           + f' Achsenebenen. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Berechnung~der~Spurpunkte~'
                           + r'mit~den~Achsenebenen.} \hspace{10em}')
        else:
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Spurpunkt der Geraden g mit der '
                           + spurpunkt + f'-Achsenebene. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Berechnung~des~Spurpunktes~'
                           + r'mit~der~' + spurpunkt + r'-Achsenebene.} \hspace{10em}')

        if spurpunkt == 'x-y' or spurpunkt == 'all':
            lsg_xy = Rational(-az,vz)
            punkt_s1 = [s1x, s1y, s1z] = punkt_a + lsg_xy * v
            loesung.append(r' z=0 \quad \to \quad 0~=~' + gzahl(az) + vorz_str(vz) + r'r \quad \vert '
                           + vorz_str(-1*az) + r' \quad \vert \div ' + gzahl_klammer(vz) + r' \quad \to \quad r~=~'
                           + gzahl(lsg_xy) + r' \quad (2BE) \\' + r' \overrightarrow{OS_{xy}} ~=~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} ~+~'
                           + gzahl(lsg_xy) + r' \cdot \begin{pmatrix} '
                           + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\' + gzahl(v[2]) + r' \\' + r' \end{pmatrix} ~=~'
                           + r' \begin{pmatrix} ' + gzahl(s1x) + r' \\' + gzahl(s1y) + r' \\' + gzahl(s1z) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad S_{xy} ~=~ \left( ' + gzahl(s1x) + r' \vert '
                           + gzahl(s1y) + r' \vert ' + gzahl(s1z) + r' \right) \quad (2BE)')
            punkte += 4

        if spurpunkt == 'x-z' or spurpunkt == 'all':
            lsg_xz = Rational(-ay,vy)
            punkt_s2 = [s2x, s2y, s2z] = punkt_a + lsg_xz * v
            loesung.append(r' y=0 \quad \to \quad 0~=~' + gzahl(ay) + vorz_str(vy) + r'r \quad \vert '
                           + vorz_str(-1*ay) + r' \quad \vert \div ' + gzahl_klammer(vy) + r' \quad \to \quad r~=~'
                           + gzahl(lsg_xz) + r' \quad (2BE) \\' + r' \overrightarrow{OS_{xz}} ~=~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} ~+~'
                           + gzahl(lsg_xz) + r' \cdot \begin{pmatrix} '
                           + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\' + gzahl(v[2]) + r' \\' + r' \end{pmatrix} ~=~'
                           + r' \begin{pmatrix} ' + gzahl(s2x) + r' \\' + gzahl(s2y) + r' \\' + gzahl(s2z) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad S_{xz} ~=~ \left( ' + gzahl(s2x) + r' \vert '
                           + gzahl(s2y) + r' \vert ' + gzahl(s2z) + r' \right) \quad (2BE)')
            punkte += 4

        if spurpunkt == 'y-z' or spurpunkt == 'all':
            lsg_yz = Rational(-ax,vx)
            punkt_s3 = [s3x, s3y, s3z] = punkt_a + lsg_yz * v
            loesung.append(r' x=0 \quad \to \quad 0~=~' + gzahl(ax) + vorz_str(vx) + r'r \quad \vert '
                           + vorz_str(-1*ax) + r' \quad \vert \div ' + gzahl_klammer(vx) + r' \quad \to \quad r~=~'
                           + gzahl(lsg_yz) + r' \quad (2BE) \\' + r' \overrightarrow{OS_{yz}} ~=~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} '
                           + vorz_str(lsg_yz) + r' \cdot \begin{pmatrix} '
                           + gzahl(v[0]) + r' \\' + gzahl(v[1]) + r' \\' + gzahl(v[2]) + r' \\' + r' \end{pmatrix} ~=~'
                           + r' \begin{pmatrix} ' + gzahl(s3x) + r' \\' + gzahl(s3y) + r' \\' + gzahl(s3z) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad S_{yz} ~=~ \left( ' + gzahl(s3x) + r' \vert '
                           + gzahl(s3y) + r' \vert ' + gzahl(s3z) + r' \right) \quad (2BE)')
            punkte += 4

        liste_punkte.append(punkte)
        i +=1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def geraden_lagebeziehung(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], lagebeziehung=None, gerade_k=False, i=0, BE=[]):
    # Aufgabe zur Lagebeziehung zweier Geraden und ggf. des Abstandes beider Geraden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "lagebeziehung=" kann festgelegt werden, ob Lagebeziehung die beiden Geraden haben. Sie kann 'identisch', 'parallel', 'windschief' oder 'schneiden' sein. Standardmäßig wird das zufällig ausgewählt.
    # Mit dem Parameter "gerade_k=" kann festgelegt ('True' oder 'False') werden, ob der Schnittwinkel bei Geraden, die sich schneiden zwischen den gegebenen Geraden g und h oder einer neuen Geraden k berechnet werden soll. Standardmäßig wird dann keine Gerade k erzeugt.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    if lagebeziehung not in ['identisch', 'parallel', 'windschief', 'schneiden', None]:
        sys.exit("Lagebeziehung muss 'identisch' , 'parallel', 'windschief', 'schneiden', oder None sein")
    if lagebeziehung == None:
        lagebeziehung = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
    v_teiler = random.choice([1, 2, 5])
    punkt_a = [ax, ay, az] = punkt_vektor(3) # Punkt A liegt auf Gerade g_1
    # Vektor v ist der Richtungsvektor von Geraden g_1
    v = [vx, vy, vz] = vektor_kuerzen([zzahl(1, 6) / 2 * v_teiler, zzahl(1, 6) / 2 * v_teiler, v_teiler])
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    uz = (vx*ux + vy * uy)/ (-1 * vz)
    u = vektor_kuerzen([ux, uy, uz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # lagebeziehungen zweier Geraden und die dafür nötigen Eigenschaften erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8
        liste_punkte.append(punkte)

        aufgabe.append(str(liste_teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen zweier Geraden und '
                                          'deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{12cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')',
                       MultiColumn(2, align='l', data='Die Geraden '), 'Punkte')
        table1.add_row('', '-', 'sind parallel, d.h. die Richtungsvektoren '
                       + 'sind kollinear, aber die Geraden haben keine gemeinsamen Punkte', '2BE')
        table1.add_row('', '-', 'sind identisch, d.h. die Richtungsvektoren sind kollinear und die Geraden '
                       + 'haben alle Punkte gemeinsam ', '2BE')
        table1.add_row('', '-', 'schneiden sich, d.h. die Richtungsvektoren sind nicht kollinear '
                       + 'und die Geraden haben einen Punkt gemeinsam', '2BE')
        table1.add_row('', '-', 'sind windschief, d.h. die Richtungsvektoren sind nicht kollinear '
                       + 'und die Geraden haben keine gem. Punkte.', '2P')
        table1.add_row('', '', '', 'insg.: ' + str(punkte) + ' BE')
        loesung.append(table1)

        if 'b' in teilaufg:
            loesung.append(' \n\n')
        i += 1

    if 'b' in teilaufg:
        # mathematisches Vorgehen zur Bestimmung der Lagebeziehung zweier Geraden erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)
        aufgabe.append(str(liste_teilaufg[i]) + ') Erläutern Sie, wie man die Lagebeziehung zweier '
                                          'Geraden mathematisch überprüfen kann. \n\n')
        # Tabelle mit dem Text
        table2 = Tabular('p{0.2cm} p{0.2cm} p{12cm} p{2cm}')
        table2.add_row(str(liste_teilaufg[i]) + ')',
                       MultiColumn(2, align='l', data=' Lagebeziehung zweier Geraden'),
                       'Punkte')
        table2.add_row('', '-', 'Zuerst prüft man ob die Geraden parallel sind, '
                       + 'indem man die Richtungsvektoren gleichsetzt und r bestimmt.', '2BE')
        table2.add_row('', '-', 'Sind die Geraden parallel (d.h. die Richtungsvektoren sind kollinear), '
                       + 'setzt man einen Stützvektor in die andere Geradengleichung ein. Ist dieser in der anderen '
                       + 'Geraden enthalten, sind die Geraden identisch, ansonsten "echt" parallel.', '2BE')
        table2.add_row('', '-', 'Sind die Geraden nicht parallel, setzt man beide Geraden gleich und '
                       + 'löst das Gleichungssystem. Erhält man eine Lösung für r und s, schneiden sich die Geraden. '
                       + 'erhält man keine Lösung, sind die Geraden windschief. ', '2BE')
        table2.add_row('', '', '', 'insg.: ' + str(punkte) + 'BE')
        loesung.append(table2)

        i += 1

    if 'c' in teilaufg:
        # Lagebeziehung zweier gegebener Geraden bestimmen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        if lagebeziehung == 'identisch':
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            punkt_c = [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(v)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor_kuerzen(zzahl(1,30)/10 * np.array(v)) # Vektor w ist der Richtungsvektor von h
            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'  \begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3BE) \\\\'
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
                         r' \mathrm{Die~Geraden~g~und~h~sind~identisch.} \quad (4BE) \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
        elif lagebeziehung == 'parallel':
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            punkt_c = [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(u)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor_kuerzen(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
            while (cx-ax)/vx == (cy-ay)/vy == (cz-az)/vz:
                punkt_c = [cx, cy, cz] = vektor_ganzzahl((punkt_a) + zzahl(1, 30) / 5 * np.array(u))  # Punkt C liegt auf h
            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'  \begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3BE) \\\\'
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
                         r' \mathrm{Die~Geraden~g~und~h~sind~echt~parallel.} \quad (4BE) \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
        elif lagebeziehung == 'windschief':
            punkte_aufg = 15
            liste_punkte.append(punkte_aufg)
            fakt_r = zzahl(1, 7) / 2
            [dx, dy, dz] = vektor_ganzzahl(punkt_a + fakt_r * np.array(v))
            punkt_d = [dx, dy, dz + zzahl(1,3)]
            fakt_s = zzahl(1, 7) / 2
            punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_d + fakt_s * np.array(u))
            w = [wx, wy, wz]= vektor_kuerzen(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            # while (vx * wy - vy * wx) == 0 or (vx * wy - vy * wx) == 0:
            #     fakt_r = zzahl(1, 7) / 2
            #     [dx, dy, dz] = vektor_ganzzahl(punkt_a + fakt_r * np.array(v))
            #     punkt_d = [dx, dy, dz + zzahl(1, 3)]
            #     fakt_s = zzahl(1, 7) / 2
            #     punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_d + fakt_s * np.array(u))
            #     w = [wx, wy, wz] = vektor_kuerzen(punkt_d - punkt_c)  # Vektor w ist der Richtungsvektor von h
            lsgs = (dx-cx)/wx
            lsgr = fakt_r
            # lsgr = -1 * (ax * wy - ay * wx - cx * wy + cy * wx) / (vx * wy - vy * wx)
            # lsgs = (-1 * (ax * vy) + (ay * vx) + (cx * vy) - (cy * vx)) / (vx * wy - vy * wx)

            if vx != 0 and wx != 0:
                loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                             + gzahl(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1*cx)
                             + r' ~ \vert \div ' + gzahl_klammer(wx) + r' \quad \to \quad s ~=~ '
                             + gzahl(N((ax-cx)/wx,3)) + vorz_str(N(vx/wx,3)) + r' \cdot r \quad (2BE) \\')
                if vy != 0 and wy != 0:
                    loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                 + gzahl(cy) + vorz_str(wy) + r' \cdot \big( ' + gzahl(N((ax-cx)/wx,3))
                                 + vorz_str(N(vx/wx,3)) + r' \cdot r \big) \\'
                                 + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + gzahl(N((wx*cy + wy*(ax - cx))/wx,3))
                                 + vorz_str(N(wy*vx/wx,3)) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1*vy) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1*N((wx*cy + wy*(ax - cx))/wx,3)) + r' \quad (2BE) \\'
                                 + gzahl(N(ay-(wx*cy+wy*(ax-cx))/wx,3)) + '~=~' + gzahl(N((vx*wy-vy*wx)/wx,3))
                                 + r' \cdot r \quad \vert \div ' + gzahl_klammer(N((vx*wy-vy*wx)/wx,3))
                                 + r' \quad \to \quad r~=~' + gzahl(lsgr)
                                 + r' \quad \mathrm{und} \quad s ~=~'
                                 + gzahl(lsgs) + r' \quad (3BE) \\')
                    if vz != 0 and wz != 0:
                        loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + gzahl(az) + vorz_str(vz)
                                     + r' \cdot (' + gzahl(lsgr) + r') ~=~ ' + gzahl(cz) + vorz_str(wz)
                                     + r' \cdot (' + gzahl(lsgs) + r') \quad \to \quad ' + gzahl(N(az+vz*lsgr,3))
                                     + '~=~' + gzahl(N(cz+wz*lsgs,3))
                                     + r' \quad (2BE) \\ \to \mathrm{Widerspruch} ~ \to ~ '
                                       r'  \mathrm{Die~Geraden~sind~Windschief.} \quad (1BE)')
                    else:
                        sys.exit('vz oder wz ist null.')
                else:
                    sys.exit('vy oder wy ist null.')
            else:
                sys.exit('va oder wa ist null.')


            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'  \begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3BE) \\\\'
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
                         r' \end{matrix} \quad (2BE) \\\\'  + loesung_2 + loesung_3 + loesung_4 + r' \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
        else:
            punkte_aufg = 17
            liste_punkte.append(punkte_aufg)
            fakt_r = zzahl(1, 7) / 2
            fakt_s = zzahl(1, 7) / 2
            punkt_d = [dx,dy,dz] = vektor_ganzzahl(punkt_a + fakt_r * np.array(v)) # Punkte C und D liegen auf h
            punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_a + fakt_s * np.array(u))
            [wx, wy, wz] = w = vektor_kuerzen(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            while (vx * wy - vy * wx) == 0 or (vx * wy - vy * wx) == 0:
                fakt_r = zzahl(1, 7) / 2
                fakt_s = zzahl(1, 7) / 2
                punkt_d = [dx, dy, dz] = vektor_ganzzahl(punkt_a + fakt_r * np.array(v))  # Punkte C und D liegen auf h
                punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_a + fakt_s * np.array(u))
                [wx, wy, wz] = w = vektor_kuerzen(punkt_d - punkt_c)  # Vektor w ist der Richtungsvektor von h
            lsgs = (dx-cx)/wx
            lsgr = fakt_r
            # lsgr = -1 * (ax * wy - ay * wx - cx * wy + cy * wx) / (vx * wy - vy * wx)
            # lsgs_alt = (-1*(ax*vy)+(ay*vx)+(cx*vy)-(cy*vx))/(vx*wy-vy*wx)
            # print('vektor d-c: ' + str(np.array(punkt_d-punkt_c)))
            # print('Vektor w ist: ' + str(w))
            # print('Punkt D: ' + str(punkt_d))
            # print('faktor r ist:' + str(fakt_r) + ' und r ist:' + str(lsgr))
            # print('faktor p ist:' + str(fakt_p) + ' und s ist:' + str(lsgs_alt))
            schnittpunkt_s = [sx, sy, sz] = (vektor_ganzzahl(punkt_c + lsgs*w))

            if vx != 0 and wx != 0:
                loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                             + gzahl(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1 * cx)
                             + r' ~ \vert \div ' + gzahl_klammer(wx) + r' \quad \to \quad s ~=~ '
                             + gzahl(N((ax - cx) / wx, 3)) + vorz_str(N(vx / wx, 3)) + r' \cdot r \quad (2BE) \\')
                if vy != 0 and wy != 0:
                    loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                 + gzahl(cy) + vorz_str(wy) + r' \cdot \big( ' + gzahl(N((ax - cx) / wx, 3))
                                 + vorz_str(N(vx / wx, 3)) + r' \cdot r \big) \\'
                                 + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + gzahl(N((wx * cy + wy * (ax - cx)) / wx, 3))
                                 + vorz_str(N(wy * vx / wx, 3)) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1 * vy) + r' \cdot r \quad \vert ~'
                                 + vorz_str(-1 * N((wx * cy + wy * (ax - cx)) / wx, 3)) + r' \quad (2BE) \\'
                                 + gzahl(N(ay - (wx * cy + wy * (ax - cx)) / wx, 3)) + '~=~'
                                 + gzahl(N((vx * wy - vy * wx) / wx, 3)) + r' \cdot r \quad \vert \div '
                                 + gzahl_klammer(N((vx * wy - vy * wx) / wx, 3))
                                 + r' \quad \to \quad r~=~' + gzahl(lsgr)
                                 + r' \quad \mathrm{und} \quad s ~=~'
                                 + gzahl(lsgs) + r' \quad (3BE) \\')
                    if vz != 0 and wz != 0:
                        loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + gzahl(az) + vorz_str(vz)
                                     + r' \cdot (' + gzahl(lsgr) + r') ~=~ ' + gzahl(cz) + vorz_str(wz)
                                     + r' \cdot (' + gzahl(lsgs) + r') \quad \to \quad ' + gzahl(N(az + vz * lsgr, 3))
                                     + '~=~' + gzahl(N(cz + wz * lsgs, 3))
                                     + r' \quad (2BE) \\ \to \mathrm{wahre~Aussage} ~ \to ~ '
                                       r'  \mathrm{Die~Geraden~schneiden~sich~in~S(' + str(sx) + r' \vert '
                                     + str(sy) + r' \vert ' + str(sz) + r').} \quad (2BE)')
                    else:
                        sys.exit('vz oder wz ist null.')
                else:
                    sys.exit('vy oder wy ist null.')
            else:
                sys.exit('va oder wa ist null.')


            loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                         r'  \begin{pmatrix}' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                         r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                         + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                         r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                         'r~=~' + gzahl(N(vx/wx,3)) + r' \\'
                         'r~=~' + gzahl(N(vy/wy,3)) + r' \\'
                         'r~=~' + gzahl(N(vz/wz,3)) + r' \\'
                         r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3BE) \\\\'
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
                         r' \end{matrix} \quad (2BE) \\\\' + loesung_2 + loesung_3 + loesung_4 + r' \\'
                         + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')

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
        aufgabe.append(str(liste_teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathit{Die~Auswahl~war~' + lagebeziehung + r'} \hspace{25em} \\'
                       + loesung_1)
        i += 1

    if len([element for element in ['c', 'd'] if element in teilaufg]) > 0 and lagebeziehung in ['parallel', 'windschief']:
        # Bestimmung des Abstandes zweier paralleler bzw. windschiefer Geraden
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if lagebeziehung == 'parallel':
            if 'c' not in teilaufg:
                punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_a * zzahl(1,7)/2 + vektor_kuerzen(u)) # Punkt C liegt auf h
                w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
                while (cx-ax)/vx == (cy-ay)/vy == (cz-az)/vz:
                    punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_a * zzahl(1,7)/2 + vektor_kuerzen(u))  # Punkt C liegt auf h
            fakt_r = Rational(skalarprodukt(punkt_c - punkt_a, v), skalarprodukt(v, v))
            erg = N(sqrt((cx - ax - fakt_r * vx) ** 2 + (cy - ay - fakt_r * vy) ** 2 + (cz - az - fakt_r * vz) ** 2), 3)
            erg_cross = [crx, cry, crz] = vektor_ganzzahl(np.cross(punkt_c - punkt_a, v))
            erg_alt_disk = Rational(crx ** 2 + cry ** 2 + crz ** 2, vx ** 2 + vy ** 2 + vz ** 2)
            erg_alt = N(sqrt(erg_alt_disk), 3)
        elif lagebeziehung == 'windschief':
            if 'c' not in teilaufg:
                fakt_r = zzahl(1, 7) / 2
                [dx, dy, dz] = vektor_ganzzahl(punkt_a + fakt_r * np.array(v))
                punkt_d = [dx, dy, dz + zzahl(1, 3)]
                fakt_s = zzahl(1, 7) / 2
                punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_d + fakt_s * np.array(u))
                w = [wx, wy, wz] = vektor_kuerzen(punkt_d - punkt_c)
            vec_n, fakt_n = [nx, ny, nz], fakt_n = vektor_kuerzen(np.cross(v,w), qout=True)
            fakt_n_str = '' if fakt_n == 1 else gzahl(fakt_n) + r' \cdot '
            erg= N(abs(((cx-ax)*nx+(cy-ay)*ny+(cz-az)*nz)/sqrt(nx**2+ny**2+nz**2)),3)
        if 'c' not in teilaufg:
            aufgabe.extend(('Gegeben sind die beiden Geraden mit folgenden Gleichungen:',
                            r'g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                            + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                            + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                            + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                            + r' \end{pmatrix} \quad \mathrm{und} \quad h: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                            + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                            + r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                            + gzahl(wx) + r' \\' + gzahl(wy) + r' \\' + gzahl(wz) + r' \\'
                            + r' \end{pmatrix}\\'))
            if lagebeziehung == 'parallel':
                    aufgabe.append(str(liste_teilaufg[i])
                                   + ') Berechnen Sie den Abstand der parallelen Geraden g und h. \n\n')
            elif lagebeziehung == 'windschief':
                    aufgabe.append(str(liste_teilaufg[i])
                                   + ') Berechnen Sie den Abstand der windschiefen Geraden g und h. \n\n')
        else:
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie den Abstand der parallelen Geraden g und h. \n\n')


        if lagebeziehung == 'parallel':
            punkte = 7
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Hilfsebene~aufstellen: } \hspace{25em} \\'
                           + r' H: ~\begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                           + gzahl(cx) + r' \\' + gzahl(cy) + r' \\' + gzahl(cz) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                           + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                           + r' \end{pmatrix} ~=~ 0 \quad \to \quad H: ~ ' + vorz_v_aussen(vx,'x')
                           + vorz_v_innen(vy,'y') + vorz_v_innen(vz,'z') + '~=~'
                           + gzahl(np.dot(punkt_c, v)) + r' \quad (2BE) \\\\ \mathrm{g~in~H~einsetzen:} \quad '
                           + gzahl(np.dot(punkt_c, v)) + '~=~' + gzahl(vx) + r' \cdot ' + binom_klammer(ax,vx,str2='r')
                           + vorz_str(vy) + r' \cdot ' + binom_klammer(ay,vy,str2='r') + vorz_str(vz)+ r' \cdot '
                           + binom_klammer(az,vz,str2='r') + r' \\ '+ gzahl(np.dot(punkt_c, v)) + '~=~'
                           + gzahl(vx*ax) + vorz_v_innen(vx**2,'r') + vorz_str(vy*ay)
                           + vorz_v_innen(vy**2,'r') + vorz_str(vz*az) + vorz_v_innen(vz**2,'r') + '~=~'
                           + gzahl(skalarprodukt(punkt_a,v)) + vorz_v_innen(skalarprodukt(v,v),'r')
                           + r' \quad \vert ' + vorz_str(-1*skalarprodukt(punkt_a,v)) + r' \quad \vert \div '
                           + gzahl_klammer(skalarprodukt(v,v)) + r' \quad (1BE) \\\\' + r' r~=~ ' + gzahl(fakt_r)
                           + r' \quad \to \quad \overrightarrow{OS} ~=~ ' + r' \begin{pmatrix} ' +gzahl(ax) + r' \\'
                           + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} ' + vorz_str(fakt_r, null=True)
                           + r' \cdot \begin{pmatrix} ' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz) + r' \\'
                           + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ax+fakt_r*vx) + r' \\'
                           + gzahl(ay+fakt_r*vy) + r' \\' + gzahl(az+fakt_r*vz) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad S \left( ' + gzahl(ax+fakt_r*vx) + r' \vert '
                           + gzahl(ay+fakt_r*vy) + r' \vert ' + gzahl(az+fakt_r*vz) + r' \right) \quad (2BE) \\'
                           + r' \mathrm{Abstand~zwischen~g~und~h~berechnen:} \hspace{15em} \\ '
                           + r' d(g,h) ~=~ \sqrt{ ' + binom_klammer(cx, -1 * (ax + fakt_r*vx)) + '^2 +'
                           + binom_klammer(cy, -1 * (ay + fakt_r*vy)) + '^2 + '
                           + binom_klammer(cz, -1 * (az + fakt_r*vz)) + '^2} ~=~ ' + gzahl(erg) + r' \quad (2BE) \\\\'
                           + r' \mathrm{alternative~Berechnung~mit:} \hspace{15em} \\'
                           + r' d(g,h) ~=~ \frac{ \left| \overrightarrow{P_g Q_h} \times \overrightarrow{v} \right| }'
                           + r' { \left| \overrightarrow{v} \right| } ~=~ \frac{ \left| \begin{pmatrix} '
                           + gzahl(cx-ax) + r' \\' + gzahl(cy-ay) + r' \\' + gzahl(cz-az) + r' \\' + r' \end{pmatrix}'
                           + r' \times \begin{pmatrix} ' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz)
                           + r' \\' + r' \end{pmatrix} \right| }{ \left| \begin{pmatrix} ' + gzahl(vx) + r' \\'
                           + gzahl(vy) + r' \\' + gzahl(vz) + r' \\' + r' \end{pmatrix} \right| } \quad (4BE) \\'
                           + r' d(g,h) ~=~  \frac{ \left| \begin{pmatrix} ' + gzahl(crx) + r' \\' + gzahl(cry) + r' \\'
                           + gzahl(crz) + r' \\' + r' \end{pmatrix} \right| }{ \sqrt{' + summe_exp([vx,vy,vz],2)
                           + r'}} ~=~ \frac{ \sqrt{ ' + summe_exp([crx, cry, crz],2) + r' }}{ \sqrt{ '
                           + gzahl(vx**2 + vy**2 + vz**2) + r'}} ~=~' + gzahl(erg_alt) + r' \quad (3BE)')
        elif lagebeziehung == 'windschief':
            punkte = 7
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Berechnung~mithilfe~der~hessischen~Normalform'
                           + r'~der~Hilfsebene~H~deren~Normalenvektor}, \\'
                           + r' \mathrm{~das~Kreuzprodukt~der~Richtungsvektoren~von~g~und~h~ist:} \\'
                           + r' \overrightarrow{n} ~=~ \overrightarrow{v} \times \overrightarrow{u} ~=~'
                           + r' \begin{pmatrix} ' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz)
                           + r' \\' + r' \end{pmatrix} \times \begin{pmatrix} ' + gzahl(wx) + r' \\' + gzahl(wy)
                           + r' \\' + gzahl(wz) + r' \\' + r' \end{pmatrix} ~=~ ' + fakt_n_str
                           + r' \begin{pmatrix} ' + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad \left| \overrightarrow{n} \right| ~=~ \sqrt{'
                           + summe_exp([nx,ny,nz],2)+ r'} ~=~ \sqrt{' + gzahl(nx**2+ny**2+nz**2)
                           + r'} ~=~' + gzahl(N(sqrt(nx**2+ny**2+nz**2),3)) + r' \quad (4BE) \\\\'
                           + r' d(g,h) ~=~ \left| \overrightarrow{P_g Q_h} \cdot \overrightarrow{n_0} \right| ~=~'
                           + r' \left| \begin{pmatrix} ' + gzahl(cx-ax) + r' \\' + gzahl(cy-ay) + r' \\' + gzahl(cz-az)
                           + r' \\' + r' \end{pmatrix} \cdot \frac{1}{ \sqrt{' + gzahl(nx**2+ny**2+nz**2)
                           + r'}} \cdot \begin{pmatrix} ' + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz)
                           + r' \\' + r' \end{pmatrix} \right| ~=~ \left| \frac{ '
                           + gzahl((cx-ax)*nx) + vorz_str((cy-ay)*ny) + vorz_str((cz-az)*nz) + r' }{ \sqrt{'
                           + gzahl(nx**2+ny**2+nz**2) + r'}} \right|  ~=~ ' + gzahl(erg) + r' \quad (3BE)')

        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Schnittwinkel zweier gegebener Geraden berechnen.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte_aufg = 7
        fakt_r = zzahl(1, 3)
        fakt_s = zzahl(1, 7) / 2
        punkt_f = [fx,fy,fz] = vektor_ganzzahl(np.array(punkt_a) + fakt_r * np.array(v)) # Punkte C und D liegen auf h
        punkt_e = [ex,ey,ez] = vektor_ganzzahl(np.array(punkt_a) + fakt_s * np.array(u))
        [px, py, pz] = p = vektor_kuerzen(np.array(punkt_f) - np.array(punkt_e)) # Vektor w ist der Richtungsvektor von h


        if 'c' in teilaufg and lagebeziehung == 'schneiden' and gerade_k == False:
            [ex, ey, ez] = [cx,cy,cz]
            [px, py, pz] = [wx, wy, wz]
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und h. \n\n')
        elif 'c' not in teilaufg:
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
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')

        else:
            aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
            aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                           r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                           + gzahl(px) + r' \\' + gzahl(py) + r' \\' + gzahl(pz) + r' \\'
                           r' \end{pmatrix} ')
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')

        sp_vp = skalarprodukt([vx, vy, vz], [px, py, pz])
        l_v = sqrt(vx ** 2 + vy ** 2 + vz ** 2)
        l_p = sqrt(px ** 2 + py ** 2 + pz ** 2)
        schnittwinkel = N(acos(sp_vp / (l_v * l_p)) * 180 / pi, 3)

        loesung.append(str(liste_teilaufg[i]) + r') \quad cos( \gamma ) = \frac{ \vert \overrightarrow{v}'
                       r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                       r' \vert \overrightarrow{u} \vert } \quad \vert ~ cos^{-1} \quad \to \quad '
                       r' \gamma ~=~ cos^{-1} \left( \frac{ \vert \overrightarrow{v}'
                       r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                       r' \vert \overrightarrow{u} \vert } \right) \quad (1BE) \\'
                       r' \vert \overrightarrow{v} \cdot \overrightarrow{u} \vert'
                       r'~=~ \vert ' + gzahl_klammer(vx) + r' \cdot ' + gzahl_klammer(px)
                       + '+' + gzahl_klammer(vy) + r' \cdot ' + gzahl_klammer(py)
                       + '+' + gzahl_klammer(vz) + r' \cdot ' + gzahl_klammer(pz) + r' \vert ~=~'
                       + gzahl(abs(N(sp_vp,3))) + r' \quad (2BE) \\'
                       r' \vert \overrightarrow{u} \vert ~=~ \sqrt{ (' + str(vx) + ')^2 ~+~('
                       + str(vy) + ')^2 ~+~(' + str(vz) + ')^2} ~=~ ' + gzahl(N(l_v,3))
                       + r' \quad \mathrm{und} \quad \vert \overrightarrow{v} \vert ~=~ \sqrt{ ('
                       + str(px) + ')^2 ~+~(' + str(py) + ')^2 ~+~(' + str(pz)
                       + ')^2} ~=~ ' + gzahl(N(l_p,3)) + r' \quad (2BE) \\'
                       + r' \gamma ~=~ cos^{-1} \left( \frac{' + gzahl(abs(N(sp_vp,3))) + '}{'
                       + gzahl(N(l_v,3)) + r' \cdot ' + gzahl(N(l_p,3))
                       + r'} \right) ~=~' + gzahl(schnittwinkel)
                       + r' \quad (2BE) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
        liste_punkte.append(punkte_aufg)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben '
                  f'({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_und_punkt(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], lagebeziehung_t_ebene=None, i=0, BE=[]):
    # Aufgaben zum Aufstellen der Ebenengleichung und Lagebziehung Punkt-Ebene.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "lagebeziehung_t_ebene=" kann festgelegt werden, ob der Punkt T in Ebene E "lagebeziehung_t_ebene=True" liegt oder auch nicht "lagebeziehung_t_ebene=False". Standardmäßig wird das zufällig ausgewählt.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_punkte = []
    liste_bez = []

    if lagebeziehung_t_ebene == None:
        lagebeziehung_t_ebene = random.choice([True, False])
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
    vektor_ab = [abx, aby, abz] = [bx - ax, by - ay, bz - az]
    while len([element for element in vektor_ab if element == 0]) > 0:
        punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_a + v)  # Punkte C und D liegen auf h
        vektor_ab = [abx, aby, abz] = [bx - ax, by - ay, bz - az]
    punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_b + zzahl(1, 4) * np.array(u))
    vektor_ac = [acx, acy, acz] = [cx - ax, cy - ay, cz - az]
    while len([element for element in vektor_ac if element == 0]) > 0:
        punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_b + zzahl(1, 4) * np.array(u))
        vektor_ac = [acx, acy, acz] = [cx - ax, cy - ay, cz - az]
    w = vektor_ganzzahl(punkt_c - punkt_a)  # Vektor w ist der Richtungsvektor von h
    [wx, wy, wz] = vektor_runden(w, 3)
    n = [nx, ny, nz] = vektor_ganzzahl(np.cross(v, w))
    n_gk = [nx_gk, ny_gk, nz_gk] = vektor_kuerzen(n)
    n_betrag = np.linalg.norm(n_gk)
    koordinatenform = ('E:~' + vorz_v_aussen(nx_gk, 'x') + vorz_v_innen(ny_gk,'y') + vorz_v_innen(nz_gk, 'z')
                       + '~=~' + gzahl(np.dot(punkt_a, n_gk)))

    # lagebeziehung_t_ebene == False if 'f' in teilaufg else lagebeziehung_t_ebene
    # if lagebeziehung_t_ebene == None and 'f' not in teilaufg:
    #     lagebeziehung_t_ebene = random.choice([False, 'Ebene', 'Dreieck', 'Parallelogramm'])
    # if lagebeziehung_t_ebene == 'Ebene':
    #     parameter_r = zzahl(2,6)/2
    #     parameter_s = zzahl(2,6)/2
    #     punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
    #     lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~in~der~Ebene~E.} \quad (3BE) \\'
    # elif lagebeziehung_t_ebene == 'Dreieck':
    #     parameter_r = nzahl(1, 6) / 10
    #     parameter_s = 1 - nzahl(1,2)/10 - parameter_r
    #     punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
    #     lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~im~Dreieck~ABC.} \quad (3BE) \\'
    # elif lagebeziehung_t_ebene == 'Parallelogramm':
    #     parameter_r = nzahl(1, 6) / 10
    #     parameter_s = 1 - nzahl(1,2)/10 - parameter_r
    #     punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
    #     lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~im~Parallelogramm~ABCD.} \quad (3BE) \\'
    # else:
    #     parameter_r = zzahl(2, 6) / 2
    #     parameter_s = zzahl(2, 6) / 2
    #     [x, y, z] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
    #     punkt_t = [tx, ty, tz] = [x, y, z + zzahl(1,3)]
    #     lsg = r' \quad \mathrm{f.A.} \\ \mathrm{Der~Punkt~T~liegt~nicht~in~der~Ebene.} \quad (3BE) \\'

    if n_betrag%1 == 0:
        ergebnis_n0 = gzahl(n_betrag)
    else:
        ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk**2 + ny_gk**2 + nz_gk**2) + r'}'

    if 'a' in teilaufg:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + gzahl(ax) + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
                   'B( ' + gzahl(bx) + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
                   'C( ' + gzahl(cx) + ' | ' + gzahl(cy) + ' | ' + gzahl(cz) + ' ). \n\n']
    elif 'a' not in teilaufg and len([element for element in ['b', 'd', 'e'] if element in teilaufg]) > 0:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Gegeben sind drei Punkte A, B und C der Ebene E, so dass gilt: ',
                   r'E: \overrightarrow{x} ~=~ \overrightarrow{OA} + r \cdot \overrightarrow{AB} + s \cdot '
                   + r' \overrightarrow{AC} ~=~ \begin{pmatrix} '
                   + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                   + gzahl(bx - ax) + r' \\' + gzahl(by - ay) + r' \\' + gzahl(bz - az) + r' \\'
                   + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                   + gzahl(cx - ax) + r' \\' + gzahl(cy - ay) + r' \\' + gzahl(cz - az) + r' \\'
                   + r' \end{pmatrix}']
    else:
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Gegeben ist die Ebene E mit: ',
                   r' E: \begin{bmatrix} \overrightarrow{x} ~-~'
                   r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                   + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                   r' \end{pmatrix} ~=~0']
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
                       r' \end{pmatrix} \quad (3BE) \\'
                       r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if 'b' in teilaufg:
        # gegebene Ebenengleichung von Parameterform in Normalen- und Koordinatenform umformen
        punkte = 7
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        fakt_n = Rational(nx, nx_gk)
        fakt_n = Rational(ny, ny_gk) if nx_gk == 0 else fakt_n
        fakt_n = Rational(nz, nz_gk) if nx_gk == 0 and ny_gk == 0 else fakt_n

        aufgabe.append(str(liste_teilaufg[i]) + ') Formen Sie die Gleichung für Ebene E in '
                       + 'Normalen- und Koordinatenform um. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                       + gzahl(vy * wz) + '-' + gzahl_klammer(vz * wy) + r' \\'
                       + gzahl(vz * wx) + '-' + gzahl_klammer(vx * wz) + r' \\'
                       + gzahl(vx * wy) + '-' + gzahl_klammer(vy * wx) + r' \\ \end{pmatrix} ~=~ \begin{pmatrix} '
                       + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                       + r' \end{pmatrix} ~=~ ' + gzahl(fakt_n) + r' \cdot \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} \quad (3BE) \\\\'
                       + r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       + r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} ~=~0 \quad (2BE) \\\\ E:~' + vorz_v_aussen(nx_gk,'x')
                       + vorz_v_innen(ny_gk,'y') + vorz_v_innen(nz_gk,'z') + '~=~'
                       + gzahl(np.dot(punkt_a, n_gk)) + r' \quad (2BE) \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if 'c' in teilaufg:
        # Überprüfen, ob ein Punkt in der Ebene liegt
        punkte = 3
        liste_punkte.append(punkte)

        if lagebeziehung_t_ebene == True:
            parameter_r = zzahl(2, 6) / 2
            parameter_s = zzahl(2, 6) / 2
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~in~der~Ebene~E.} \quad (3BE) \\'
        else:
            parameter_r = zzahl(2, 6) / 2
            parameter_s = zzahl(2, 6) / 2
            [x, y, z] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            punkt_t = [tx, ty, tz] = [x, y, z + zzahl(1, 3)]
            lsg = r' \quad \mathrm{f.A.} \\ \mathrm{Der~Punkt~T~liegt~nicht~in~der~Ebene~E.} \quad (3BE) \\'
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T( {gzahl(tx)} | {gzahl(ty)} | '
                       + f'{gzahl(tz)} ) in der Ebene E liegt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad E:~' + vorz_v_aussen(nx_gk, r' \cdot ' + gzahl_klammer(tx))
                       + vorz_v_innen(ny_gk, r' \cdot ' + gzahl_klammer(ty))
                       + vorz_v_innen(nz_gk, r' \cdot ' + gzahl_klammer(tz)) + '~=~' + gzahl(np.dot(punkt_a, n_gk))
                       + r' \quad \to \quad ' + gzahl(np.dot(n_gk, punkt_t)) + '~=~' + gzahl(np.dot(punkt_a, n_gk))
                       + lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if 'd' in teilaufg:
        # Die SuS sollen überprüfen, ob der Punkt P im von den Punkten ABC aufgespannte Parallelogramm liegt.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 9

        if nzahl(1,2) == 1:
            parameter_r = nzahl(1, 5) / 5
            parameter_s = nzahl(1, 5) / 5
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg_0 = (r' \mathrm{r~=~' + gzahl(parameter_r) + '~und~s~=~' + gzahl(parameter_s)
                     + r'~in~III~einsetzen: \quad }' + gzahl(tz) + '~=~' + gzahl(az) + vorz_str(abz)
                     + r' \cdot ' + gzahl_klammer(parameter_r) + vorz_str(acz) + r' \cdot '
                     + gzahl_klammer(parameter_s) + r' \\' + gzahl(tz) + '~=~' + gzahl(tz)
                     + r' \mathrm{ \quad w.A. \quad \to  \quad P~liegt~in~Ebene~E \quad (3BE)} \\')
            lsg_1 = (r' \mathrm{r~und~s~\leq~1 \quad \to \quad Der~Punkt~P~liegt~im~Parallelogramm.} \quad (1BE) \\')
            punkte += 3
            if lagebeziehung_t_ebene == False:
                tz = tz + zzahl(1, 3)
                lsg_0 = (r' \mathrm{r~=~' + gzahl(parameter_r) + '~und~s~=~' + gzahl(parameter_s)
                         + r'~in~III~einsetzen: \quad }' + gzahl(tz) + '~=~' + gzahl(az) + vorz_str(abz)
                         + r' \cdot ' + gzahl_klammer(parameter_r) + vorz_str(acz) + r' \cdot '
                         + gzahl_klammer(parameter_s) + r' \\' + gzahl(tz) + '~=~'
                         + gzahl(az + abz * parameter_r + acz * parameter_s)
                         + r' \mathrm{ \quad f.A. \quad \to  \quad P~liegt~nicht~in~Ebene~E~und~damit~nicht~im~'
                         + r'Parallelogramm~ABCD. \quad (3BE)}')
                lsg_1 = ''
                punkte += -1
        else:
            parameter_r = nzahl(1,5) / 5
            parameter_s = 1 + random.choice([1,2,3,4,5]) / 5
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg_0 = ''
            lsg_1 = r' s > 1 \quad \mathrm{Der~Punkt~P~liegt~nicht~im~Parallelogramm.} \quad (1BE) \\'

        aufgabe.extend(('Die Punkte A, B und C aus der Ebene E bilden das Parallelogramm ABCD. \n\n',
                        str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt P( {gzahl(tx)} | {gzahl(ty)} | '
                        + f'{gzahl(tz)} ) im Parallelogramm liegt. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Überprüfen~Sie,~ob~der~gegebenen~Punkt~P~im'
                       + r'~Parallelogramm~liegt.} \\' + r' \begin{pmatrix} ' + gzahl(tx) + r' \\' + gzahl(ty) + r' \\'
                       + gzahl(tz) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ax) + r' \\'
                       + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} + r \cdot \begin{pmatrix} '
                       + gzahl(abx) + r' \\' + gzahl(aby) + r' \\' + gzahl(abz) + r' \\'
                       + r' \end{pmatrix}  ~+~s \cdot \begin{pmatrix}'
                       + gzahl(acx) + r' \\' + gzahl(acy) + r' \\' + gzahl(acz) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                       + 'I: ~~' + gzahl(tx) + '~=~' + r' \\'
                       + 'II: ~~' + gzahl(ty) + '~=~' + r' \\'
                       + 'III: ~~' + gzahl(tz) + '~=~' + r' \\' + r' \end{matrix} \begin{matrix}'
                       + gzahl(ax) + vorz_v_innen(abx,'r') + vorz_v_innen(acx,'s') + r' \\'
                       + gzahl(ay) + vorz_v_innen(aby,'r') + vorz_v_innen(acy,'s') + r' \\'
                       + gzahl(az) + vorz_v_innen(abz,'r') + vorz_v_innen(acz,'s') + r' \\'
                       + r' \end{matrix} \quad (2BE) \\\\' + r' \mathrm{I~nach~s~umstellen:} \quad '
                       + gzahl(tx) + '~=~' + gzahl(ax) + vorz_v_innen(abx,'r') + vorz_v_innen(acx,'s')
                       + r' \quad \vert ' + vorz_str(-1 * ax) + r' \quad \vert ' + vorz_v_innen(-1 * abx,'r')
                       + r' \quad \vert \div ' + gzahl_klammer(acx) + r' \quad \to \quad s ~=~ '
                       + gzahl(N((tx - ax) / acx, 3)) + vorz_v_innen(round(-1*abx / acx, 3), 'r')
                       + r' \quad (2BE) \\' + r' \mathrm{s~in~II~einsetzen:} \quad ' + gzahl(ty) + '~=~' + gzahl(ay)
                       + vorz_v_innen(aby,'r') + vorz_str(acy) + r' \left( ' + gzahl(round((tx - ax)/acx,3))
                       + vorz_v_innen(round(-1*abx/acx,3), 'r') + r' \right) ~=~' + gzahl(ay)
                       + vorz_v_innen(aby,'r') + vorz_str(round(acy * (tx - ax)/acx,3))
                       + vorz_v_innen(round(-1*acy*abx/acx,3), 'r') + r' \quad \vert '
                       + vorz_str(-1 * (ay - round(acy * (ax - tx)/acx, 3))) + r' \quad (2BE) \\'
                       + gzahl(round(((ty-ay)*acx + acy * (ax-tx))/acx,3)) + '~=~' + vorz_v_aussen(aby,'r')
                       + vorz_v_innen(round(-1*acy*abx/acx,3), 'r') + '~=~'
                       + vorz_v_aussen(round((aby*acx - acy*abx)/acx,3),'r') + r' \quad \vert \div '
                       + gzahl_klammer(round((aby*acx - acy*abx)/acx,3)) + r' \quad \to \quad r ~=~'
                       + gzahl(parameter_r) + r' \quad \to \quad s ~=~' + gzahl(parameter_s) + r' \quad (2BE) \\\\'
                       + lsg_0 + lsg_1)
        liste_punkte.append(punkte)
        i += 1

    if 'e' in teilaufg:
        # Die SuS sollen überprüfen, ob der Punkt Q im Dreieck ABC der Ebene E liegt.
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 9

        if nzahl(1,2) == 1:
            parameter_r = nzahl(2, 6) / 10
            parameter_s = 1 - nzahl(1,2)/10 - parameter_r
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg_0 = (r' \mathrm{r~=~' + gzahl(parameter_r) + '~und~s~=~' + gzahl(parameter_s)
                     + r'~in~III~einsetzen: \quad }' + gzahl(tz) + '~=~' + gzahl(az) + vorz_str(abz)
                     + r' \cdot ' + gzahl_klammer(parameter_r) + vorz_str(acz) + r' \cdot '
                     + gzahl_klammer(parameter_s) + r' \\' + gzahl(tz) + '~=~' + gzahl(tz)
                     + r' \mathrm{ \quad w.A. \quad \to  \quad Q~liegt~in~Ebene~E \quad (3BE)} \\')
            lsg_1 = (r' \mathrm{r~und~s~\leq~1 \quad \to \quad Der~Punkt~Q~liegt~im~Dreieck~ABC.} \quad (1BE) \\')
            punkte += 3
            if lagebeziehung_t_ebene == False:
                tz = tz + zzahl(1,3)
                lsg_0 = (r' \mathrm{r~=~' + gzahl(parameter_r) + '~und~s~=~' + gzahl(parameter_s)
                         + r'~in~III~einsetzen: \quad }' + gzahl(tz) + '~=~' + gzahl(az) + vorz_str(abz)
                         + r' \cdot ' + gzahl_klammer(parameter_r) + vorz_str(acz) + r' \cdot '
                         + gzahl_klammer(parameter_s) + r' \\' + gzahl(tz) + '~=~'
                         + gzahl(az+abz*parameter_r+acz*parameter_s)
                         + r' \mathrm{ \quad f.A. \quad \to \quad Q~liegt~nicht~in~Ebene~E~und~damit~nicht~im~'
                         + r'Dreieck~ABC. \quad (3BE)}')
                lsg_1 = ''
                punkte += -1

        else:
            parameter_r = nzahl(2,8) / 10
            parameter_s = 1 + random.choice([1,2,3,4,5])/10 - parameter_r
            while parameter_s + parameter_r <= 1:
                parameter_r = nzahl(4,8) / 10
                parameter_s = 1 + random.choice([1,2,3,4,5])/10 - parameter_r
            lsg_2 = 'r + s  > 1'
            lsg_2 = 's > 1' if parameter_s > 1 else lsg_2
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg_0 = ''
            lsg_1 = lsg_2 + r' \quad \mathrm{Der~Punkt~Q~liegt~nicht~im~Dreieck~ABC.} \quad (1BE) \\'

        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt Q( {gzahl(tx)} | {gzahl(ty)} | '
                        + f'{gzahl(tz)} ) im Dreieck der Punkte A, B und C aus Ebene E liegt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Überprüfe,~ob~der~gegebenen~Punkt~Q~im~Dreieck~'
                       + r'ABC~liegt.} \\' + r' \begin{pmatrix} ' + gzahl(tx) + r' \\' + gzahl(ty) + r' \\'
                       + gzahl(tz) + r' \\' + r' \end{pmatrix} ~=~ \begin{pmatrix} ' + gzahl(ax) + r' \\'
                       + gzahl(ay) + r' \\' + gzahl(az) + r' \\' + r' \end{pmatrix} + r \cdot \begin{pmatrix} '
                       + gzahl(abx) + r' \\' + gzahl(aby) + r' \\' + gzahl(abz) + r' \\'
                       + r' \end{pmatrix}  ~+~s \cdot \begin{pmatrix}'
                       + gzahl(acx) + r' \\' + gzahl(acy) + r' \\' + gzahl(acz) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                       + 'I: ~~' + gzahl(tx) + '~=~' + r' \\'
                       + 'II: ~~' + gzahl(ty) + '~=~' + r' \\'
                       + 'III: ~~' + gzahl(tz) + '~=~' + r' \\' + r' \end{matrix} \begin{matrix}'
                       + gzahl(ax) + vorz_v_innen(abx,'r') + vorz_v_innen(acx,'s') + r' \\'
                       + gzahl(ay) + vorz_v_innen(aby,'r') + vorz_v_innen(acy,'s') + r' \\'
                       + gzahl(az) + vorz_v_innen(abz,'r') + vorz_v_innen(acz,'s') + r' \\'
                       + r' \end{matrix} \quad (2BE) \\\\' + r' \mathrm{I~nach~s~umstellen:} \quad '
                       + gzahl(tx) + '~=~' + gzahl(ax) + vorz_v_innen(abx,'r') + vorz_v_innen(acx,'s')
                       + r' \quad \vert ' + vorz_str(-1 * ax) + r' \quad \vert ' + vorz_v_innen(-1 * abx,'r')
                       + r' \quad \vert \div ' + gzahl_klammer(acx) + r' \quad \to \quad s ~=~ '
                       + gzahl(N((tx - ax) / acx, 3)) + vorz_v_innen(round(-1*abx / acx, 3), 'r')
                       + r' \quad (2BE) \\' + r' \mathrm{s~in~II~einsetzen:} \quad ' + gzahl(ty) + '~=~' + gzahl(ay)
                       + vorz_v_innen(aby,'r') + vorz_str(acy) + r' \left( ' + gzahl(round((tx - ax)/acx,3))
                       + vorz_v_innen(round(-1*abx/acx,3), 'r') + r' \right) ~=~' + gzahl(ay)
                       + vorz_v_innen(aby,'r') + vorz_str(round(acy * (tx - ax)/acx,3))
                       + vorz_v_innen(round(-1*acy*abx/acx,3), 'r') + r' \quad \vert '
                       + vorz_str(-1 * (ay - round(acy * (ax - tx)/acx, 3))) + r' \quad (2BE) \\'
                       + gzahl(round(((ty-ay)*acx + acy * (ax-tx))/acx,3)) + '~=~' + vorz_v_aussen(aby,'r')
                       + vorz_v_innen(round(-1*acy*abx/acx,3), 'r') + '~=~'
                       + vorz_v_aussen(round(aby - acy*abx/acx,3),'r') + r' \quad \vert \div '
                       + gzahl_klammer(round((aby*acx - acy*abx)/acx,3)) + r' \quad \to \quad r ~=~'
                       + gzahl(parameter_r) + r' \quad \to \quad s ~=~' + gzahl(parameter_s) + r' \quad (2BE) \\\\'
                       + lsg_0 + lsg_1)
        liste_punkte.append(punkte)
        i += 1

    if 'f' in teilaufg:
        # Die SuS sollen die hessische Normalform der Ebene aufstellen
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \left| \overrightarrow{n} \right| ~=~ \sqrt{('
                       + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                       + ergebnis_n0 + r' \quad \to \quad '
                       + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                       + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                       + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                       + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                       + r' \end{pmatrix} ~=~0 \\'
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if 'g' in teilaufg:
        # Berechnung des Abstandes eines Punktes R von der Ebene
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkt_r = [rx, ry, rz] = vektor_ganzzahl(punkt_a + np.array(v) + np.array(w)) + n
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand des Punktes R( {gzahl(rx)} | '
                       + f'{gzahl(ry)} | {gzahl(rz)} ) zur Ebene E. \n\n')
        if 'f' not in teilaufg:
            punkte += 4
            loesung.append(str(liste_teilaufg[i]) + r') \quad \left| \overrightarrow{n} \right| ~=~ \sqrt{('
                           + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                           + ergebnis_n0 + r' \quad \to \quad '
                           + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                           + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                           + r' \end{pmatrix} ~=~0 \quad (4BE) \\'
                           + r' d~=~ \left| \begin{bmatrix} \begin{pmatrix} '
                           + gzahl(rx) + r' \\' + gzahl(ry) + r' \\' + gzahl(rz) + r' \\ '
                           + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                           + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                           + r' \end{pmatrix} \right| ~=~ \frac{1}{' + ergebnis_n0 + r'} \cdot '
                           + r' \left| ' + gzahl_klammer(rx - ax) + r' \cdot ' + gzahl_klammer(nx_gk)
                           + vorz_str(ry - ay, null=True) + r' \cdot ' + gzahl_klammer(ny_gk)
                           + vorz_str(rz - az, null=True) + r' \cdot '
                           + gzahl_klammer(nz_gk) + r' \right| ~=~ '
                           + gzahl(abs(N(np.dot((punkt_r - punkt_a), (1 / n_betrag * n_gk)), 3)))
                           + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        else:
            loesung.append(str(liste_teilaufg[i]) + r') \quad d~=~ \left| \begin{bmatrix} \begin{pmatrix} '
                           + gzahl(rx) + r' \\' + gzahl(ry) + r' \\' + gzahl(rz) + r' \\ '
                           + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                           + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                           + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                           + r' \end{pmatrix} \right| ~=~ \left| \frac{1}{' + ergebnis_n0 + r'} \cdot '
                           + r' \left( ' + gzahl_klammer(rx - ax) + r' \cdot '
                           + gzahl_klammer(nx_gk) + vorz_str(ry - ay, null=True) + r' \cdot '
                           + gzahl_klammer(ny_gk) + vorz_str(rz - az, null=True) + r' \cdot '
                           + gzahl_klammer(nz_gk) + r' \right) \right|  ~=~ '
                           + gzahl(abs(N(np.dot((punkt_r - punkt_a),(1 / n_betrag * n_gk)),3)))
                           + r' \\ \mathrm{insgesamt~' + str(punkte) + r'~BE}')
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebenen_umformen(nr, teilaufg=['a', 'b'], form=None, koordinatensystem=False, i=0, BE=[]):
    # Aufgaben zum Umformen der Ebenengleichungen aus Normalen- oder Koordinatenform und mithilfe der Achsenabschnittsform Ebene zeichnen.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "form=" kann die Form der Ebenengleichung festgelegt werden. Sie kann "form="normalenform" oder "form=koordinatenform" sein. Standardmäßig wird die Form zufällig ausgewählt.
    # Mit dem Parameter "koordinatensystem=" kann den SuS ein leeres Koordinatensystem "koordinatensystem=True" erzeugt werden.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []
    teiler = zzahl(1,3)
    schnittpunkte = [sx,sy,sz,e]=[zzahl(1,5),zzahl(1,5),zzahl(1,5),1]
    fkt_kf = [kfx,kfy,kfz,kfe] = vektor_kuerzen([1 / sx, 1 / sy, 1 / sz, e])
    n = [nx,ny,nz] = vektor_kuerzen([int(kfx), int(kfy), int(kfz)])
    # print(schnittpunkte), print(fkt_kf), print(n)
    punkt_a = [ax,ay,az] = random.choice([np.array([kfe/kfx,0,0]),np.array([0,kfe/kfy,0]),np.array([0,0,kfe/kfz])])
    # print(punkt_a)
    normalenform = (r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                    + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                    r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                    + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                    r' \end{pmatrix} ~=~ 0')
    koordinatenform = ('E:~' + vorz_v_aussen(nx,'x')  + vorz_v_innen(ny,'y')
                       + vorz_v_innen(nz,'z') + '~=~' + gzahl(np.dot(punkt_a,n)))

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
        aufgabe.append(str(liste_teilaufg[i]) + f') Formen Sie die Ebenengleichung in die '
                                          f'anderen beiden Darstellungsformen um. \n\n ')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                       + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                       r' \end{pmatrix} \quad \to \quad ' + andere_darstellungsform + r' \quad (3BE) \\'
                       r' \overrightarrow{u} ~=~ \begin{pmatrix}'
                       + gzahl(-1*ny) + r' \\' + gzahl(nx) + r' \\' + gzahl(0) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{v} ~=~ \begin{pmatrix}'
                       + gzahl(0) + r' \\' + gzahl(-1*nz) + r' \\' + gzahl(ny) + r' \\'
                       r' \end{pmatrix} \quad \to\ \quad E: \overrightarrow{x} ~=~ '
                       + lsg + r' ~+~r \cdot \begin{pmatrix} '
                       + gzahl(-1*ny) + r' \\' + gzahl(nx) + r' \\' + gzahl(0) + r' \\'
                       r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                       + gzahl(0) + r' \\' + gzahl(-1*nz) + r' \\' + gzahl(ny) + r' \\'
                       r' \end{pmatrix} \quad (4BE) \\')
        i += 1

    if 'b' in teilaufg:
        # Aufstellen der Achsenabschnittsform der Ebene und zeichnen der Ebene in 3-dim-Koordinatenform
        punkte = 3
        liste_punkte.append(punkte)
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die Achsenabschnittsform von E auf '
                       + f'und zeichnen Sie ein Schrägbild der Ebene.')
        if koordinatensystem:
            grafiken_loesung = grafiken_aufgaben = ['3dim_Koordinatensystem']
            aufgabe.append(['Bild', '300px'])
            loesung.append(['Bild', '300px'])
        loesung.extend((str(liste_teilaufg[i]) + r') \quad ' + koordinatenform + r' \quad \vert \div '
                       + gzahl(np.dot(punkt_a,n)) + r' \quad \to \quad ' + r'E:~ \frac{x}{' + gzahl_klammer(sx)
                       + r'} + \frac{y}{' + gzahl_klammer(sy) + r'} + \frac{z}{' + gzahl_klammer(sz) + r'} ~=~'
                       + str(1) + r' \quad (1BE) \\ \mathrm{Zeichnung: \quad (2BE)}', ''))
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_und_gerade(nr, teilaufg=['a', 'b', 'c', 'd', 'e'], g_in_E=None, i=0, BE=[]):
    # Lagebeziehungen einer Ebene mit einer Geraden und ggf. Abstandsberechnung.# Mit dem Parameter "koordinatensystem=" kann den SuS ein leeres Koordinatensystem "koordinatensystem=True" erzeugt werden.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "g_in_E=" kann die Lagebeziehung der Geraden g zur Ebene E festgelegt werden. Sie kann 'identisch', 'parallel' oder 'schneiden' sein. Standardmäßig wird das zufällig ausgewählt.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

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
               + r' \quad \mathrm{w.A. \quad Die~Gerade~liegt~in~der~Ebene. \quad (2BE) } \\')
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
               + gzahl(ergebnis_r) + r' \quad (2BE) \\'
               + r' \mathrm{Die~Gerade~schneidet~die~Ebene~im~Punkt:}  \quad (1BE) \\ \begin{pmatrix} '
               + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
               + r' \end{pmatrix}' + vorz_str(ergebnis_r) + r' \cdot \begin{pmatrix} '
               + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
               + r' \end{pmatrix} ~=~ \begin{pmatrix} '
               + gzahl(ex + ergebnis_r * g_vx) + r' \\' + gzahl(ey + ergebnis_r * g_vy) + r' \\'
               + gzahl(ez + ergebnis_r * g_vz) + r' \\ \end{pmatrix} \quad \to \quad S('
               + gzahl(ex + ergebnis_r * g_vx) + r' \vert ' + gzahl(ey + ergebnis_r * g_vy) + r' \vert '
               + gzahl(ez + ergebnis_r * g_vz) + r') \quad (3BE) \\')
    elif g_in_E == 'parallel' or 'e' in teilaufg:
        abstand = zzahl(1, 7) / 2 * np.array(n_gk)
        punkt_e = [ex, ey, ez] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v) + abstand)
        punkt_f = [fx, fy, fz] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(u) + abstand)
        g_v = [g_vx, g_vy, g_vz] = np.array(punkt_f - punkt_e)
        lsg = (gzahl(np.dot(n_gk, punkt_e)) + '~=~'
               + gzahl(np.dot(punkt_a, n_gk))
               + r' \quad \mathrm{f.A. \quad Die~Gerade~ist~parallel~zur~Ebene. \quad (2BE)} \\')
    else:
        exit("g_in_E muss None, 'identisch', 'parallel' oder 'schneiden' sein!")

    if 'a' in teilaufg:
        # die Lagebeziehung einer Geraden mit einer Ebene und die dafür nötigen Eigenschaften erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        liste_punkte.append(punkte)
        aufgabe.append(str(liste_teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen einer Geraden '
                                          'mit einer Ebene und deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Gerade und die Ebene:'),
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
        text = 'Gegeben ist die Gerade g durch die Punkte: ' if 'a' in teilaufg else 'und die Gerade g durch die Punkte: '
        aufgabe.extend((text + 'A( ' + gzahl(ex) + ' | ' + gzahl(ey) + ' | ' + gzahl(ez) + ' ) und ' 
                        'B( ' + gzahl(fx) + ' | ' + gzahl(fy) + ' | ' + gzahl(fz) + ' ).  \n\n',
                        str(liste_teilaufg[i]) + f') Bestimmen Sie Gleichung der Geraden g. \n\n'))
        loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{AB} ~=~ \begin{pmatrix} '
                       + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       + r' \end{pmatrix} \quad \to \quad g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                       + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       + r' \end{pmatrix} \quad (2BE) \\ '
                       + r' \mathrm{insgesamt~' + str(punkte) + r'~BE}')
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
            aufgabe.append(r' \mathrm{Gleichung~der~Geraden~g: \overrightarrow{x} \ ~ = ~ \begin{pmatrix}'
                           + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                           + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                           + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\' + r' \end{pmatrix} ')
        loesung.append(str(liste_teilaufg[i]) + r') \quad '
                       + gzahl(nx_gk) + r' \cdot (' + gzahl(ex) + vorz_str(g_vx) + 'r)'
                       + vorz_str(ny_gk) + r' \cdot (' + gzahl(ey) + vorz_str(g_vy) + 'r)'
                       + vorz_str(nz_gk) + r' \cdot (' + gzahl(ez) + vorz_str(g_vz) + 'r) ~=~'
                       + gzahl(np.dot(punkt_a, n_gk)) + r' \quad (1BE) \\'
                       + lsg + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
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
                       + r' \end{pmatrix} ~=~0 \\ \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
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
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \quad (4BE) \\'
                               + r' d: \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + latex(abs(N(np.dot((punkt_e - punkt_a),(1 / n_betrag * n_gk)),3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad d: \left| \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + latex(abs(N(np.dot((punkt_e - punkt_a),(1 / n_betrag * n_gk)),3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebene_ebene(nr, teilaufg=['a', 'b', 'c', 'd'], F_in_E=None, i=0, BE=[]):
    # Lagebeziehungen zweier Ebenen und ggf. der Abstandsberechnung.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "F_in_E=" kann die Lagebeziehung der Ebene F zur Ebene E festgelegt werden. Sie kann 'identisch', 'parallel' oder 'schneiden' sein. Standardmäßig wird das zufällig ausgewählt.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

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
               + r' \quad \mathrm{w.A. \quad Die~Ebene~F~liegt~in~der~Ebene~E. \quad (2BE) } \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')

    elif F_in_E == 'schneiden':
        punkte = 8
        n = [nx, ny, nz] = punkt_vektor(4)
        punkt_a = [ax, ay, az] = punkt_vektor(3)
        while vektor_kollinear(n, n_gk) == True:
            n = [nx, ny, nz] = punkt_vektor(4)

        g_v = [g_vx, g_vy, g_vz] = vektor_kuerzen(zzahl(1, 7) / 2 * np.array([nz, 0, -1 * nx]))
        k_v = [k_vx, k_vy, k_vz] = vektor_kuerzen(zzahl(1, 7) / 2 * np.array([-1 * ny, nx, 0]))
        while np.dot(n_gk, k_v) == 0 or np.dot(n_gk, g_v) == 0:
            g_v = [g_vx, g_vy, g_vz] = vektor_kuerzen(zzahl(1, 7) / 2 * np.array([nz, 0, -1 * nx]))
            k_v = [k_vx, k_vy, k_vz] = vektor_kuerzen(zzahl(1, 7) / 2 * np.array([-1 * ny, nx, 0]))

        # print('Vektor n: ' + str(n))
        # print('Vektor g_v: ' + str(g_v))
        # print('Vektor k_v: ' + str(k_v))
        # print(-1 * np.dot(n_gk, k_v))
        # print(np.dot(n_gk, g_v))
        g_stütz = [g_sx, g_sy, g_sz] = punkt_a + Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)) * g_v
        g_richtung = [g_rx, g_ry, g_rz] = Rational(-1 * np.dot(n_gk, k_v), np.dot(n_gk, g_v)) * g_v + k_v

        lsg = (gzahl(np.dot(punkt_a, n_gk)) + vorz_v_innen(np.dot(n_gk, g_v),'r')
               + vorz_v_innen(np.dot(n_gk, k_v),'s') +  '~=~' + gzahl(np.dot(punkt_d, n_gk)) + r' \quad \vert '
               + vorz_str(-1 * np.dot(punkt_a, n_gk)) + r' \quad \vert '
               + vorz_v_innen(-1 * np.dot(n_gk, k_v),'s')
               + r' \quad \to \quad ' + vorz_v_aussen(np.dot(n_gk, g_v),'r') + '~=~'
               + gzahl(np.dot(punkt_d - punkt_a, n_gk)) + vorz_v_innen(-1*np.dot(n_gk, k_v), 's')
               + r' \quad \vert \div' + gzahl_klammer(np.dot(n_gk, g_v)) + r' \quad (2BE) \\ r ~=~'
               + gzahl(Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)))
               + vorz_str(Rational(-1* np.dot(n_gk, k_v), np.dot(n_gk, g_v)))
               + r's \quad \mathrm{Die~Ebene~F~schneidet~die~Ebene~E. \quad (2BE) } \\'
               + r' \quad \mathrm{Schnittgerade~bestimmen,~indem~man~r~in~F~einsetzt} \\'
               + r' \overrightarrow{x} ~=~ \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az)
               + r' \\' + r' \end{pmatrix} ~+~ (' + gzahl(Rational(np.dot(punkt_d - punkt_a, n_gk), np.dot(n_gk, g_v)))
               + vorz_str(Rational(-1*np.dot(n_gk, k_v), np.dot(n_gk, g_v))) + r's) \cdot \begin{pmatrix} ' + gzahl(g_vx)
               + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\' + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
               + gzahl(k_vx) + r' \\' + gzahl(k_vy) + r' \\' + gzahl(k_vz) + r' \\'
               + r' \end{pmatrix} ~=~ \begin{pmatrix}' + gzahl(g_sx) + r' \\' + gzahl(g_sy) + r' \\' + gzahl(g_sz)
               + r' \\' + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}' + gzahl(g_rx) + r' \\' + gzahl(g_ry) + r' \\'
               + gzahl(g_rz) + r' \\' + r' \end{pmatrix} \quad (2BE) \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')

    elif F_in_E == 'parallel' or 'd' in teilaufg:
        punkte = 4
        abstand = zzahl(1, 7) / 2
        punkt_a = [ax, ay, az] = vektor_ganzzahl(punkt_d + abstand * np.array(n_gk))
        punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_a + zzahl(1, 3) * np.array(v))
        punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_a - zzahl(1, 3) * np.array(u))
        g_v = [g_vx, g_vy, g_vz] = np.array(punkt_b - punkt_a)
        k_v = [k_vx, k_vy, k_vz] = np.array(punkt_c - punkt_a)

        lsg = (gzahl(np.dot(punkt_a, n_gk)) + '~=~' + gzahl(np.dot(punkt_d, n_gk))
               + r' \quad \mathrm{f.A. \quad Die~Ebene~F~ist~parallel~zur~Ebene~E. \quad (2BE) } \\'
               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')

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
        aufgabe.append(str(liste_teilaufg[i]) + ') Erläutern Sie die möglichen Lagebeziehungen zweier Ebenen '
                                          'und deren Eigenschaften. \n\n')
        # Tabelle mit dem Text
        table1 = Tabular('p{0.2cm} p{0.2cm} p{13cm} p{2cm}')
        table1.add_row(str(liste_teilaufg[i]) + ')', MultiColumn(2, align='l', data='Die Ebenen:'), 'Punkte')
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
                       + vorz_v_innen(g_vx,'r') + vorz_v_innen(k_vx, 's') + ')' + vorz_str(ny_gk)
                       + '(' + gzahl(ay) + vorz_v_innen(g_vy,'r') + vorz_v_innen(k_vy, 's') + ')'
                       + vorz_str(nz_gk) + '(' + gzahl(az) + vorz_v_innen(g_vz, 'r')
                       + vorz_v_innen(k_vz,'s') + ') ~=~ ' + gzahl(np.dot(punkt_d, n_gk))
                       + r' \quad (1BE) \\' + gzahl(nx_gk * ax) + vorz_v_innen(nx_gk * g_vx, 'r')
                       + vorz_v_innen(nx_gk * k_vx, 's') + vorz_str(ny_gk * ay) + vorz_v_innen(ny_gk * g_vy, 'r')
                       + vorz_v_innen(ny_gk * k_vy, 's') + vorz_str(nz_gk * az) + vorz_v_innen(nz_gk * g_vz, 'r')
                       + vorz_v_innen(nz_gk * k_vz, 's') + '~=~' + gzahl(np.dot(punkt_d, n_gk)) + r' \quad (1BE) \\'
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
                       + r' \end{pmatrix} ~=~0 \\' + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
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
                               + r' \end{pmatrix} ~=~0 \quad (4BE) \\' + r' d~=~ \left| \begin{bmatrix}'
                               + r' \begin{pmatrix}' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_a - punkt_aE), 1 / n_betrag * n_gk), 3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad d~=~ \left| \begin{bmatrix}'
                               + r' \begin{pmatrix}' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \right| ~=~'
                               + gzahl(abs(N(np.dot((punkt_a - punkt_aE), 1 / n_betrag * n_gk), 3))) + r' \\'
                               + r' \mathrm{insgesamt~' + str(punkte) + r'~BE} \\')
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def ebenenschar_buendel(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], i=0, BE=[]):
    # Lagebeziehungen einer Ebenenschar mit den Koordinatenachsen, geg. Geraden und verschiedenen Ebenen der Schar.
    # Mit dem Parameter "teilaufg=" können die Teilaufgaben ausgewählt werden. Zum Beispiel "teilaufg=['a', 'c']" erzeugt eine Aufgabe, in der nur Teilaufgabe 'a' und 'c' enthalten sind.
    # Mit dem Parameter "i=" kann wird festgelegt mit welchen Buchstaben die Teilaufgaben beginnen. Standardmäßig ist "i=0" und die Teilaufgaben starten mit a.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.
    liste_punkte = []
    liste_bez = []

    # Normalenvektorschar der Ebene erzeugen
    punkt_d = [dx, dy, dz] = punkt_vektor(4)
    nv = [nx, ny, nz] = punkt_vektor(4)
    ave = [aex, aey, aez] = [zzahl(0,3), zzahl(0,3), zzahl(0,3)]
    while vektor_kollinear(nv,ave) == True:
        ave = [aex, aey, aez] = [zzahl(0,3), zzahl(0,3), zzahl(0,3)]
    ebene = (nx+aex*a)*x + (ny+aey*a)*y + (nz+aez*a)*z
    erg = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * a
    erg_str = gzahl(np.dot(punkt_d, nv)) + vorz_v_innen(np.dot(punkt_d, ave),'a')

    # Gerade g erzeugen
    g_var = zzahl(1, 4)
    g_rv  = random.choice([[ny + aey * g_var, -1 * (nx + aex * g_var), 0],
                           [0, nz + aez * g_var, -1 * (ny + aey * g_var)],
                           [nz + aez * g_var, 0, -1 * (nx + aex * g_var)]])
    g_rv = [g_vx, g_vy, g_vz] = vektor_kuerzen(g_rv)
    punkt_g = [gx, gy, gz] = punkt_d + g_rv

    # Gerade h erzeugen
    h_var = zzahl(1,4)
    h_rv = random.choice([[ny + aey * h_var, -1*(nx + aex * h_var), 0],
                          [0, nz + aez * h_var, -1*(ny + aey * h_var)],
                          [nz + aez * h_var, 0, -1 * (nx + aex * h_var)]])
    h_rv = [h_vx, h_vy, h_vz] = vektor_kuerzen(h_rv)
    while skalarprodukt(h_rv, [nx + aex*a, ny + aey*a, nz + aez*a]) == 0:
        h_var = zzahl(1, 4)
        h_rv = random.choice([[ny + aey * h_var, -1 * (nx + aex * h_var), 0],
                              [0, nz + aez * h_var, -1 * (ny + aey * h_var)],
                              [nz + aez * h_var, 0, -1 * (nx + aex * h_var)]])
        h_rv = [h_vx, h_vy, h_vz] = vektor_kuerzen(h_rv)
    punkt_h = [hx, hy, hz] = punkt_d + h_rv + vektor_kuerzen(nv)*zzahl(1,3)

    if 'b' in teilaufg and len([element for element in ['d', 'e'] if element in teilaufg]) > 0:
        text = r' \mathrm{und~die~Geraden~g~und~h~mit} \quad '
    elif 'b' in teilaufg:
        text = r' \mathrm{und~die~Gerade~g~mit} \quad '
    elif len([element for element in ['d', 'e'] if element in teilaufg]) > 0:
        text = r' \mathrm{und~die~Gerade~h~mit} \quad '
    else:
        text = ''

    if 'b' in teilaufg:
        gerade_g = (r' g: \overrightarrow{x} ~=~ \begin{pmatrix} '
                    + gzahl(gx) + r' \\' + gzahl(gy) + r' \\' + gzahl(gz) + r' \\'
                    + r' \end{pmatrix} ~+~ r \cdot \begin{pmatrix} '
                    + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                    + r' \end{pmatrix} ')
    else:
        gerade_g = ''

    if len([element for element in ['d', 'e'] if element in teilaufg]) > 0:
        konjunktion = ''
        konjunktion = r', \quad ' if 'b' in teilaufg else konjunktion
        gerade_h = (konjunktion + r' h: \overrightarrow{x} ~=~ \begin{pmatrix} '
                    + gzahl(hx) + r' \\' + gzahl(hy) + r' \\' + gzahl(hz) + r' \\'
                    + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                    + gzahl(h_vx) + r' \\' + gzahl(h_vy) + r' \\' + gzahl(h_vz) + r' \\'
                    + r' \end{pmatrix}')
    else:
        gerade_h = ''


    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))),
               r' \mathrm{Gegeben~sei~die~Ebenenschar~E_a:~} '+ binom_aussen(nx, aex, str2='a', var='x')
               + binom_innen(ny, aey, str2='a', var='y') + binom_innen(nz, aez, str2='a', var='z') + '~=~'
               + erg_str + r' \\' + text + gerade_g + gerade_h]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # Die SuS sollen die Ebene der Schar bestimmen, die den Punkt T enthält
        t_var = zzahl(1,4)
        t_rv = random.choice([[ny + aey * t_var, -1 * (nx + aex * t_var), 0],
                              [0, nz + aez * t_var, -1 * (ny + aey * t_var)],
                              [nz + aez * t_var, 0, -1 * (nx + aex * t_var)]])
        punkt_t = [tx, ty, tz] = punkt_d + vektor_kuerzen(t_rv)
        pkt = 4
        erg_k = skalarprodukt(punkt_d, nv)
        erg_a = skalarprodukt(punkt_d, ave)
        erg_ebene = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * t_var
        if punkt_t == punkt_d:
            lsg = r' \quad \to \quad \mathrm{w.A.~T~liegt~in~allen~Ebenen~von~E_a} \quad (2BE)'
        else:
            if  erg_a != 0:
                lsg = r' \quad \vert ' + vorz_v_innen(-1*skalarprodukt(punkt_d, ave),'a')
            else:
                lsg = ''
            lsg = (lsg + r' \quad \vert ' + vorz_str(-1*(nx*tx+ny*ty+nz*tz)) + r' \quad \to \quad '
                   + gzahl(erg_k - (nx*tx+ny*ty+nz*tz)) + '~=~'
                   + vorz_v_aussen(aex*tx + aey*ty + aez*tz - erg_a,'a') + r' \quad \vert \div '
                   + gzahl_klammer(aex*tx+aey*ty+aez*tz - erg_a) + r' \quad \to \quad a~=~' + gzahl(t_var)
                   + r' \quad (2BE) \\ E_{' + gzahl(t_var) + '}:' + vorz_v_aussen(nx+aex*t_var, 'x')
                   + vorz_v_innen(ny+aey*t_var, 'y') + vorz_v_innen(nz+aez*t_var,'z')
                   + '~=~' + gzahl(erg_ebene) +  r' \quad (1BE)')
            pkt += 1

        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie diejenige Ebene der Ebenenschar die den '
                       + f'Punkt T( {gzahl(tx)} | {gzahl(ty)} | {gzahl(tz)} ) enthält. \n\n')
        loesung.append(str(liste_teilaufg[i])  + r') \quad \mathrm{T~in~E_a~einsetzen~und~die~entstandene~'
                       + r'Gleichung~nach~a~umstellen} \hspace{10em} \\' + erg_str + '~=~'
                       + binom_aussen(nx, aex, str2='a') + r' \cdot ' + gzahl_klammer(tx)
                       + binom_innen(ny, aey, str2='a',) + r' \cdot ' + gzahl_klammer(ty)
                       + binom_innen(nz, aez, str2='a') + r' \cdot ' + gzahl_klammer(tz) + '~=~'
                       + gzahl(nx*tx) + vorz_str(ny*ty) + vorz_str(nz*tz) + vorz_v_innen(aex*tx,'a') 
                       + vorz_v_innen(aey*ty,'a') + vorz_v_innen(aez*tz,'a') + r' \quad (2BE) \\'
                       + erg_str + '~=~' + gzahl(nx*tx+ny*ty+nz*tz) + vorz_v_innen(aex*tx+aey*ty+aez*tz,'a')
                       + lsg)

        liste_punkte.append(pkt)
        i += 1

    if 'b' in teilaufg:
        # Die SuS sollen diejenige Ebene bestimmen, in der die Gerade g liegt
        erg = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * g_var
        pkt = 7
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob es eine Ebene der Ebenenschar gibt, '
                       + f'in der die Gerade g liegt. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Skalarprodukt~des~Richtungsvektor~von~g~und~dem'
                       + r'~Normalenvektor~von~E_a~aufstellen~und~a~berechnen} \\'
                       + r' 0~=~ \begin{pmatrix} ' + binom(nx, aex, str2='a') + r' \\'
                       + binom(ny, aey, str2='a') + r' \\' + binom(nz, aez, str2='a') + r' \\ \end{pmatrix} '
                       + r' \cdot \begin{pmatrix} ' + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       + r' \end{pmatrix} ~=~' + binom_aussen(nx, aex, str2='a') + r' \cdot '
                       + gzahl_klammer(g_vx) + binom_innen(ny, aey, str2='a',) + r' \cdot ' + gzahl_klammer(g_vy)
                       + binom_innen(nz, aez, str2='a') + r' \cdot ' + gzahl_klammer(g_vz) + r' \quad (1BE) \\'
                       + ' 0~=~' + gzahl(nx*g_vx) + vorz_str(ny*g_vy) + vorz_str(nz*g_vz)
                       + vorz_v_innen(aex*g_vx,'a') + vorz_v_innen(aey*g_vy,'a')
                       + vorz_v_innen(aez*g_vz,'a') + r'~=~' + gzahl(nx*g_vx + ny*g_vy + nz*g_vz)
                       + vorz_v_innen(aex*g_vx + aey*g_vy + aez*g_vz,'a')
                       + r' \quad \vert ' + vorz_str(-1*(nx*g_vx + ny*g_vy + nz*g_vz)) + r' \quad \vert \div '
                       + gzahl_klammer(aex*g_vx + aey*g_vy + aez*g_vz) + r' \quad \to \quad a~=~' + gzahl(g_var)
                       + r' \quad (2BE) \\ E_{' + gzahl(g_var) + '}:' + vorz_v_aussen(nx+aex*g_var, 'x')
                       + vorz_v_innen(ny+aey*g_var, 'y') + vorz_v_innen(nz+aez*g_var,'z')
                       + '~=~' + gzahl(erg) + r' \quad (1BE) \\'
                       + r' \mathrm{Stützvektor~von~g~in~E_{' + gzahl(g_var) + r'}~einsetzen:} \hspace{20em} \\'
                       + gzahl(nx+aex*g_var, null=True) + r'\cdot' + gzahl_klammer(gx, null=True)
                       + vorz_str(ny+aey*g_var, null=True) + r'\cdot' + gzahl_klammer(gy, null=True)
                       + vorz_str(nz+aez*g_var, null=True) + r'\cdot' + gzahl_klammer(gz, null=True)
                       + '~=~' + gzahl(erg) + r' \quad (1BE) \\' + gzahl(erg) + '~=~' + gzahl(erg)
                       + r' \quad \to \quad \mathrm{g~liegt~in~E_{' + gzahl(g_var) + r'} } \quad (2BE)')
        liste_punkte.append(pkt)
        i += 1

    if 'c' in teilaufg:
        # Die SuS sollen diejenige Ebene bestimmen, in die parallel zu gegebenen Koordinatenachse ist
        pkt = 3
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        achse = random_selection([['x',[1,0,0]],['y',[0,1,0]],['z',[0,0,1]]],1)
        bez = achse[0][0]
        vec = achse[0][1]
        if aex * vec[0] + aey * vec[1] + aez * vec[2] == 0:
            lsg = (r' \quad \to \quad \mathrm{Widerspruch \quad \to \quad es~gibt~keine~parallele~Ebene~zur~' + bez
                   + r'-Achse \quad (3BE)')
        else:
            erg = Rational(-1 * (nx * vec[0] + ny * vec[1] + nz * vec[2]), aex * vec[0] + aey * vec[1] + aez * vec[2])
            erg_ebene = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * erg
            lsg = (r' \quad \vert ' + vorz_str(-1 * (nx * vec[0] + ny * vec[1] + nz * vec[2])) + r' \quad \vert \div '
                   + gzahl_klammer(aex * vec[0] + aey * vec[1] + aez * vec[2])+ r' \quad \to \quad a~=~'
                   + gzahl(erg) + r' \quad (3BE) \\ E_{' + gzahl(erg) + r'}:' + vorz_v_aussen(nx+aex*erg, 'x')
                   + vorz_v_innen(ny+aey*erg, 'y') + vorz_v_innen(nz+aez*erg,'z') + '~=~'
                   + gzahl(erg_ebene) + r' \quad (1BE)')
            pkt += 2
        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie diejenige Ebene der Ebenenschar, '
                       + f' die zur {bez} - Achse parallel ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Skalarprodukt~des~Richtungsvektor~der~' + str(bez)
                       + r'-Achse~und~dem~Normalenvektor~von~E_a~aufstellen~und~a~berechnen} \\'
                       + r' 0~=~ \begin{pmatrix} ' + binom(nx, aex, str2='a') + r' \\'
                       + binom(ny, aey, str2='a') + r' \\' + binom(nz, aez, str2='a') + r' \\ \end{pmatrix} '
                       + r' \cdot \begin{pmatrix} ' + gzahl(vec[0]) + r' \\' + gzahl(vec[1]) + r' \\' + gzahl(vec[2])
                       + r' \\' + r' \end{pmatrix} ~=~' + binom_aussen(nx, aex, str2='a') + r' \cdot '
                       + gzahl_klammer(vec[0]) + binom_innen(ny, aey, str2='a', ) + r' \cdot ' + gzahl_klammer(vec[1])
                       + binom_innen(nz, aez, str2='a') + r' \cdot ' + gzahl_klammer(vec[2]) + r' \quad (1BE) \\'
                       + ' 0~=~' + gzahl(nx * vec[0]) + vorz_str(ny * vec[1]) + vorz_str(nz * vec[2])
                       + vorz_v_innen(aex * vec[0], 'a') + vorz_v_innen(aey * vec[1], 'a')
                       + vorz_v_innen(aez * vec[2], 'a') + lsg)
        liste_punkte.append(pkt)
        i += 1

    if 'd' in teilaufg:
        # Die SuS sollen diejenige Ebene bestimmen, in die parallel zur Geraden h ist
        erg = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * h_var
        pkt = 4
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie diejenige Ebene der Ebenenschar, '
                       + f'die parallel zur Geraden h ist. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Skalarprodukt~des~Richtungsvektor~von~h~und~dem'
                       + r'~Normalenvektor~von~E_a~aufstellen~und~a~berechnen} \\'
                       + r' 0~=~ \begin{pmatrix} ' + binom(nx, aex, str2='a') + r' \\'
                       + binom(ny, aey, str2='a') + r' \\' + binom(nz, aez, str2='a') + r' \\ \end{pmatrix} '
                       + r' \cdot \begin{pmatrix} ' + gzahl(h_vx) + r' \\' + gzahl(h_vy) + r' \\' + gzahl(h_vz) + r' \\'
                       + r' \end{pmatrix} ~=~' + binom_aussen(nx, aex, str2='a') + r' \cdot '
                       + gzahl_klammer(h_vx) + binom_innen(ny, aey, str2='a',) + r' \cdot ' + gzahl_klammer(h_vy)
                       + binom_innen(nz, aez, str2='a') + r' \cdot ' + gzahl_klammer(h_vz) + r' \quad (1BE) \\'
                       + ' 0~=~' + gzahl(nx*h_vx) + vorz_str(ny*h_vy) + vorz_str(nz*h_vz)
                       + vorz_v_innen(aex*h_vx,'a') + vorz_v_innen(aey*h_vy,'a')
                       + vorz_v_innen(aez*h_vz,'a') + r'~=~' + gzahl(nx*h_vx + ny*h_vy + nz*h_vz)
                       + vorz_v_innen(aex*h_vx + aey*h_vy + aez*h_vz,'a')
                       + r' \quad \vert ' + vorz_str(-1*(nx*h_vx + ny*h_vy + nz*h_vz)) + r' \quad \vert \div '
                       + gzahl_klammer(aex*h_vx + aey*h_vy + aez*h_vz) + r' \quad \to \quad a~=~' + gzahl(h_var)
                       + r' \quad (2BE) \\ \mathrm{Die~folgende~Ebene~ist~parallel~zu~h} \quad  E_{' + gzahl(h_var)
                       + r'}:' + vorz_v_aussen(nx+aex*h_var, 'x') + vorz_v_innen(ny+aey*h_var, 'y')
                       + vorz_v_innen(nz+aez*h_var,'z') + '~=~' + gzahl(erg) + r' \quad (1BE)')
        liste_punkte.append(pkt)
        i += 1

        if 'e' in teilaufg:
            # Abstandsberechnung der Geraden h zur parallelen Ebene aus der vorherigen Teilaufgabe
            na = [nax, nay, naz] = [nx + aex * h_var, ny + aey * h_var, nz + aez * h_var]
            laenge_na = N(1/sqrt(nax**2 + nay**2 + naz**2),3)
            laenge_na_str = r' \sqrt{' + gzahl(nax**2 + nay**2 + naz**2) + r'}'
            erg = N(laenge_na * np.dot((punkt_d - punkt_h),(na)),3)
            pkt = 6
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand der Geraden h zur parallelen Ebene '
                           + f'der Schar. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \left| \overrightarrow{n} \right| ~=~ \sqrt{ '
                           + summe_exp([nax, nay, naz], 2) + r' } ~=~ '
                           + laenge_na_str + r' \quad (2BE) \quad \mathrm{und~ein~Punkt~in~E_{'
                           + gzahl(h_var) + r'} ~ist:} \quad P \left( ' + gzahl(dx) + r' \vert ' + gzahl(dy) + r' \vert '
                           + gzahl(dz) + r' \right) \quad (1BE) \\ '
                           + r' d(E,h) ~=~ \left| \begin{bmatrix} \begin{pmatrix} '
                           + gzahl(hx) + r' \\' + gzahl(hy) + r' \\' + gzahl(hz) + r' \\ '
                           + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                           + gzahl(dx) + r' \\' + gzahl(dy) + r' \\' + gzahl(dz) + r' \\'
                           + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + laenge_na_str + r'} \begin{pmatrix} '
                           + gzahl(nax) + r' \\' + gzahl(nay) + r' \\' + gzahl(naz) + r' \\'
                           + r' \end{pmatrix} \right| ~=~ \left| \frac{1}{' + laenge_na_str + r'} \cdot '
                           + r' \left( ' + gzahl_klammer(hx - dx) + r' \cdot '
                           + gzahl_klammer(nax) + vorz_str(hy - dy, null=True) + r' \cdot '
                           + gzahl_klammer(nay) + vorz_str(hz - dz, null=True) + r' \cdot '
                           + gzahl_klammer(naz) + r' \right) \right|  ~=~ ' + gzahl(abs(erg)) + r' \quad (3BE)')
            liste_punkte.append(pkt)
            i += 1

    if 'f' in teilaufg:
        # die SuS sollen die Schnittgerade zweier Ebenen der Schar bestimmen
        pkt = 11
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')

        var1 = -1 * nzahl(1,2)
        var2 = var1 + nzahl(2,3)
        erg_var_1 = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * var1
        erg_var_2 = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * var2
        nx_var1 = [nx_1, ny_1, nz_1] = np.array([nx + aex * var1, ny + aey * var1, nz + aez * var1])
        nx_var2 = [nx_2, ny_2, nz_2] = np.array([nx + aex * var2, ny + aey * var2, nz + aez * var2])
        nx_var1_gk = [nx1, ny1, nz1, erg_var1] = vektor_kuerzen([nx_1, ny_1, nz_1, erg_var_1])
        nx_var2_gk = [nx2, ny2, nz2, erg_var2] = vektor_kuerzen([nx_2, ny_2, nz_2, erg_var_2])
        while (nz1*ny2 - ny1*nz2) == 0:
            var1 = -1 * nzahl(1, 2)
            var2 = var1 + nzahl(2, 3)
            erg_var_1 = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * var1
            erg_var_2 = skalarprodukt(punkt_d, nv) + skalarprodukt(punkt_d, ave) * var2
            nx_var1 = [nx_1, ny_1, nz_1] = np.array([nx + aex * var1, ny + aey * var1, nz + aez * var1])
            nx_var2 = [nx_2, ny_2, nz_2] = np.array([nx + aex * var2, ny + aey * var2, nz + aez * var2])
            nx_var1_gk = [nx1, ny1, nz1, erg_var1] = vektor_kuerzen([nx_1, ny_1, nz_1, erg_var_1])
            nx_var2_gk = [nx2, ny2, nz2, erg_var2] = vektor_kuerzen([nx_2, ny_2, nz_2, erg_var_2])

        lsg_kon = Rational(erg_var1 - (nx1 * dx + ny1 * dy + nz1 * dz), nz1 * ny2 - ny1 * nz2)
        lsg_var = Rational(ny2 * nx1 - nx2 * ny1, nz1 * ny2 - ny1 * nz2)

        if nx_1 == nx1 and ny_1 == ny1 and nz_1 == nz1:
            lsg_1 = r' \quad (1BE) \quad '
            lsg_3 = ''
        else:
            lsg_1 = (r' \quad \to \quad E_{' + gzahl(var1) + '}:' + vorz_v_aussen(nx1, 'x')
                     + vorz_v_innen(ny1, 'y') + vorz_v_innen(nz1, 'z') + '~=~' + gzahl(erg_var1))
            lsg_3 = r' \quad (1BE) \\'

        if nx_2 == nx2 and ny_2 == ny2 and nz_2 == nz2:
            lsg_2 = ''
            lsg_3 = ''
        else:
            lsg_2 = (r' \quad \to \quad E_{' + gzahl(var2) + '}:' + vorz_v_aussen(nx2, 'x')
                     + vorz_v_innen(ny2, 'y') + vorz_v_innen(nz2,'z') + '~=~' + gzahl(erg_var2))
            lsg_3 = r' \quad (1BE) \\'

        aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Schnittgerade s der Ebenen a = {gzahl(var1)} '
                       + f'und a = {gzahl(var2)} der Schar. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad E_{' + gzahl(var1) + '}:'
                       + vorz_v_aussen(nx_1, 'x') + vorz_v_innen(ny_1, 'y')
                       + vorz_v_innen(nz_1,'z') + '~=~' + gzahl(erg_var_1) + lsg_1 + lsg_3
                       + r' \mathrm{und} \quad E_{' + gzahl(var2) + '}:' + vorz_v_aussen(nx_2, 'x')
                       + vorz_v_innen(ny_2, 'y') + vorz_v_innen(nz_2,'z') + '~=~' + gzahl(erg_var_2)
                       + lsg_2 + r' \quad (1BE) \\' + r' \mathrm{E_{' + gzahl(var2)
                       + r'}~umformen~in~Parameterform:} \quad E_{' + gzahl(var2) + '}: '
                       + r' \overrightarrow{x} ~=~ \begin{pmatrix} ' + gzahl(dx) + r' \\'
                       + gzahl(dy) + r' \\' + gzahl(dz) + r' \\ \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(-1*ny2) + r' \\' + gzahl(nx2) + r' \\' + gzahl(0) + r' \\'
                       + r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}' + gzahl(0) + r' \\' + gzahl(-1*nz2) + r' \\'
                       + gzahl(ny2) + r' \\' + r' \end{pmatrix} \quad (3BE) \\' + r' \mathrm{und~in~E_{' + gzahl(var1)
                       + r'} ~einsetzen:} \quad '+ gzahl(erg_var1) + '~=~' + gzahl(nx1) + r' \cdot \left( ' + gzahl(dx)
                       + vorz_v_innen(-1*ny2, ' r ') + r' \right) ' + vorz_str(ny1) + r' \cdot \left( '
                       + gzahl(dy) + vorz_v_innen(nx2,'r') + vorz_v_innen(-1*nz2,'s') + r' \right) '
                       + vorz_str(nz1) + r' \cdot \left( ' + gzahl(dz) + vorz_v_innen(ny2,'s')
                       + r' \right) \quad (1BE) \\ ' + gzahl(erg_var1) + '~=~' + gzahl(nx1*dx)  + vorz_str(ny1*dy)
                       + vorz_str(nz1*dz) + vorz_v_innen(-1*ny2*nx1,'r') + vorz_v_innen(nx2*ny1,'r')
                       + vorz_v_innen(nz1*ny2,'s') + vorz_v_innen(-1*ny1*nz2, 's') + '~=~'
                       + gzahl(nx1*dx+ny1*dy+nz1*dz) + vorz_v_innen(nx2*ny1 - ny2*nx1,'r')
                       + vorz_v_innen(nz1*ny2 - ny1*nz2, 's') + r' \quad (1BE) \\' + gzahl(erg_var1) + '~=~'
                       + gzahl(nx1*dx+ny1*dy+nz1*dz) + vorz_v_innen(nx2*ny1 - ny2*nx1,'r')
                       + vorz_v_innen(nz1*ny2 - ny1*nz2, 's') + r' \quad \vert '
                       + vorz_str(-1*(nx1*dx+ny1*dy+nz1*dz)) + r' \quad \vert '
                       + vorz_v_innen(ny2*nx1-nx2*ny1,' r ') + r' \quad \vert \div '
                       + gzahl_klammer(nz1*ny2 - ny1*nz2) + r' \quad \to \quad s~=~'
                       + binom_klammer(lsg_kon, lsg_var, '', 'r') + r' \quad (2BE) \\'
                       + r' \mathrm{s~einsetzen~in~E_{' + gzahl(var2) + r'~}} \quad s: '
                       + r' \overrightarrow{x} ~=~ \begin{pmatrix} ' + gzahl(dx) + r' \\'
                       + gzahl(dy) + r' \\' + gzahl(dz) + r' \\' + r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + gzahl(-1*ny2) + r' \\' + gzahl(nx2) + r' \\' + gzahl(0) + r' \\'
                       + r' \end{pmatrix} ~+~ ' + binom_klammer(lsg_kon, lsg_var, '', 'r') + r' \cdot \begin{pmatrix}' + gzahl(0) + r' \\' + gzahl(-1*nz2) + r' \\' + gzahl(ny2)
                       + r' \\' + r' \end{pmatrix} \quad (1BE) \\ s: \overrightarrow{x} ~=~ \begin{pmatrix} '
                       + gzahl(dx) + r' \\' + gzahl(dy - lsg_kon * nz2) + r' \\'
                       + gzahl(dz + lsg_kon * ny2) + r' \\' + r' \end{pmatrix} ~+~ r \cdot \begin{pmatrix} '
                       + gzahl(-1*ny2) + r' \\' + gzahl(nx2 - lsg_var * nz2)
                       + r' \\' + gzahl(lsg_var*ny2) + r' \\' + r' \end{pmatrix} \quad (1BE)')
        liste_punkte.append(pkt)
        i += 1

        if 'g' in teilaufg:
            # die SuS sollen nachweisen, dass die Schnittgerade zweier Ebenen in allen Ebenen liegt
            pkt = 4
            liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
            aufgabe.append(str(liste_teilaufg[i]) + f') Weisen Sie nach, dass die Schnittgerade s in allen '
                           + f'Ebenen der Schar liegt. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Einsetzen~der~Schnittgerade~s~in~E_a:} '
                           + r' \hspace{20em} \\' + erg_str + '~=~'
                           + binom_aussen(nx, aex, str2='a', var=binom_klammer(dx,-1*ny2,str2='r'))
                           + binom_innen(ny, aey, str2='a', var=binom_klammer(dy-lsg_kon*nz2,nx2-lsg_var*nz2, str2='r'))
                           + binom_innen(nz, aez, str2='a', var=binom_klammer(dz+lsg_kon*ny2,lsg_var*ny2, str2='r'))
                           + r' \quad (1BE) \\' + erg_str + '~=~' + gzahl(nx*dx) + vorz_v_innen(-1*nx*ny2,'r')
                           + vorz_v_innen(aex*dx,'a')
                           + vorz_v_innen(-1*aex*ny2,'ar') + vorz_str(ny*(dy-lsg_kon * nz2))
                           + vorz_v_innen(ny*(nx2-lsg_var*nz2),'r') + vorz_v_innen(aey*(dy-lsg_kon*nz2),'a')
                           + vorz_v_innen(aey*(nx2-lsg_var*nz2),'ar') + vorz_str(nz*(dz+lsg_kon*ny2))
                           + vorz_v_innen(nz*lsg_var*ny2,'r') + vorz_v_innen(aez*(dz+lsg_kon*ny2),'a')
                           + vorz_v_innen(aez*lsg_var*ny2,'ar')
                           + r' \quad (1BE) \\' + erg_str + '~=~'
                           + gzahl(nx*dx + ny*(dy-lsg_kon * nz2) + nz*(dz+lsg_kon*ny2))
                           + vorz_v_innen(-1*nx*ny2 + ny*(nx2-lsg_var*nz2) + nz*lsg_var*ny2,'r')
                           + vorz_v_innen(aex*dx + aey*(dy-lsg_kon*nz2) + aez*(dz+lsg_kon*ny2), 'a')
                           + vorz_v_innen(-1*aex*ny2 + aey*(nx2-lsg_var*nz2) + aez*lsg_var*ny2, 'ar')
                           + r' \quad \mathrm{w.A. \quad \to ~ Schnittgerade~s~liegt~für~alle~a~in~der~Ebenenschar.} '
                           + r' \quad (2BE)')
            liste_punkte.append(pkt)
            i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben ({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]



# in Entwicklung