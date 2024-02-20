import datetime
import string
import numpy as np
import random, math
from funktionen import *
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow, Package)
from pylatex.utils import bold
from sympy import *
from plotten import Graph
# Definition der Funktionen

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nr_aufgabe = 0

def erstellen(Teil):
    print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']


    # Auswahl der Lagebeziehungen
    auswahl_punkt_ebene = random.choice(['liegt in der Ebene', 'liegt nicht in der Ebene'])
    if auswahl_punkt_ebene == 'liegt in der Ebene':
        auswahl_gerade_ebene = random.choice(['identisch', 'parallel', 'schneiden'])
    else:
        auswahl_gerade_ebene = random.choice(['identisch', 'schneiden'])
    if not auswahl_gerade_ebene == 'parallel' and auswahl_punkt_ebene == 'liegt in der Ebene':
        auswahl_ebene_ebene = 'parallel'
    else:
        auswahl_ebene_ebene = random.choice(['identisch', 'schneiden'])
    print(auswahl_punkt_ebene)
    print(auswahl_gerade_ebene)
    print(auswahl_ebene_ebene)


    def punkte_ebene(nr, teilaufg):
        i = 0
        n_gk = np.array([100,100,100])
        v_teiler = zzahl(1, 3)
        punkt_a = [ax, ay, az] = punkt_vektor(3)  # Punkt A liegt auf Gerade g_1
        v = [vx, vy, vz] = vektor_ganzzahl(np.array([zzahl(1, 6) / 2 * v_teiler,
                                                     zzahl(1, 6) / 2 * v_teiler,
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
        if n_betrag%1 == 0:
            ergebnis_n0 = gzahl(n_betrag)
        else:
            ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk**2 + ny_gk**2 + nz_gk**2) + r'}'
        parameter_r = zzahl(1, 7)/2
        parameter_s = zzahl(1, 7)/2
        if auswahl_punkt_ebene == 'liegt in der Ebene':
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + parameter_r * np.array(v) + parameter_s * np.array(w))
            lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~T~liegt~in~der~Ebene~E.} \quad (3P) \\'
        else:
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_c + parameter_r * np.array(v)
                                                     + parameter_s * np.array(w)
                                                     + zzahl(1, 7) / 2 * np.array(n_gk))
            lsg = r' \quad \mathrm{f.A.} \\ \mathrm{Der~Punkt~T~liegt~nicht~in~der~Ebene.} \quad (3P) \\'

        if 'a' in teilaufg:
            aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                       'A( ' + gzahl(ax) + ' | ' + gzahl(ay) + ' | ' + gzahl(az) + ' ), ' 
                       'B( ' + gzahl(bx) + ' | ' + gzahl(by) + ' | ' + gzahl(bz) + ' ) und '
                       'C( ' + gzahl(cx) + ' | ' + gzahl(cy) + ' | ' + gzahl(cz) + ' ).  \n\n']
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
        grafiken_aufgaben = ['','']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

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
                           r' \end{pmatrix} \quad (5P) \\'
                           r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'b' in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            aufgabe.append(str(liste_teilaufg[i]) + f') Formen Sie die Gleichung für Ebene E in '
                                              f'Normalen- und Koordinatenform um. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                           + gzahl(vy * wz) + '-' + vorz_str_minus(vz * wy) + r' \\'
                           + gzahl(vz * wx) + '-' + vorz_str_minus(vx * wz) + r' \\'
                           + gzahl(vx * wy) + '-' + vorz_str_minus(vy * wx) + r' \\ \end{pmatrix} ~=~ \begin{pmatrix} '
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
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if 'c' in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append('')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
            aufgabe.append('Gegeben ist ein weiterer Punkt T( ' + gzahl(tx) + ' | ' + gzahl(ty) + ' | '
                           + gzahl(tz) + ' ), \n\n')
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T in der Ebene E liegt. \n\n')
            loesung.append(str(liste_teilaufg[i]) + (r') \quad E:~' + gzahl(nx_gk) + r' \cdot (' + gzahl(tx) + ')'
                                               + vorz_str(ny_gk) + r' \cdot (' + gzahl(ty) + ')'
                                               + vorz_str(nz_gk) + r' \cdot (' + gzahl(tz) + ') ~=~'
                                               + gzahl(np.dot(punkt_a, n_gk)) + r' \quad \to \quad '
                                               + gzahl(np.dot(n_gk, punkt_t)) + '~=~'
                                               + gzahl(np.dot(punkt_a, n_gk)) + lsg
                                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\'))

            i += 1
        if auswahl_punkt_ebene == 'liegt nicht in der Ebene':
            if 'd' in teilaufg:
                punkte_aufg = 4
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)

                aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                               + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                               + ergebnis_n0 + r' \quad \to \quad '
                               + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} ~=~0'
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1

            if 'e' in teilaufg:
                punkte_aufg = 3
                print()
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand des Punktes T zur Ebene E. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad E: \vert \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(tx) + r' \\' + gzahl(tx) + r' \\' + gzahl(tz) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \vert ~=~'
                               + gzahl(abs(N(np.dot((punkt_t - punkt_a),(1 / n_betrag * n_gk)),3)))
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1
        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def gerade_ebene(nr, teilaufg):
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
                   r' E:~ ' + gzahl(nx_gk) + 'x' + vorz_str(ny_gk) + 'y'
                   + vorz_str(nz_gk) + 'z ~=~' + gzahl(np.dot(punkt_a,n_gk))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['', '']
        grafiken_loesung = ['']

        if 'a' in teilaufg:
            punkte_aufg = 5
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')


            if auswahl_gerade_ebene == 'identisch':
                punkt_e = [ex, ey, ez] = punkt_a + zzahl(1,7)/2*v + zzahl(1,7)/2*u
                punkt_f = [fx, fy, fz] = punkt_a + zzahl(1,7)/2*v + zzahl(1,7)/2*u
                while vektor_vergleich(punkt_e, punkt_f) == True:
                    punkt_f = [fx, fy, fz] = punkt_a + zzahl(1, 7) / 2 * v + zzahl(1, 7) / 2 * u
                g_v = [g_vx, g_vy, g_vz] = zzahl(1,7)/2*v + zzahl(1,7)/2*u
                lsg = (gzahl(nx_gk * ex + ny_gk * ey + nz_gk * ez) + '~=~'
                       + gzahl(np.dot(punkt_a,n_gk))
                       + r' \quad \mathrm{w.A. \quad Die~Gerade~liegt~in~der~Ebene. \quad (2P) } \\')
            elif auswahl_gerade_ebene == 'parallel':
                abstand = zzahl(1, 7) / 2 * np.array(n_gk)
                punkt_e = [ex, ey, ez] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v) + abstand)
                punkt_f = [fx, fy, fz] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(u) + abstand)
                g_v = [g_vx, g_vy, g_vz] = np.array(punkt_f - punkt_e)
                lsg = (gzahl(np.dot(n_gk,punkt_e)) + '~=~'
                       + gzahl(np.dot(punkt_a, n_gk))
                       + r' \quad \mathrm{f.A. \quad Die~Gerade~ist~parallel~zur~Ebene. \quad (2P)} \\')
            else:
                g_v = n_gk
                while vektor_kollinear(g_v, n_gk) == True:
                    punkt_s = punkt_a + zzahl(1,7)/2 * v + zzahl(1,7)/2*u
                    g_v = [g_vx, g_vy, g_vz] = punkt_vektor(4)
                    ergebnis_r = zzahl(1, 6) / 2
                    punkt_e = [ex, ey, ez] = punkt_s - ergebnis_r * g_v
                    punkt_f = [fx, fy, fz] = punkt_e + g_v


                lsg = (gzahl(nx_gk * ex + ny_gk * ey + nz_gk * ez)
                       + vorz_str(nx_gk * g_vx + ny_gk * g_vy + nz_gk * g_vz) + r' \cdot r ~=~'
                       + gzahl(np.dot(punkt_a, n_gk)) + r' \quad \vert '
                       + vorz_str(-1 * (nx_gk * ex + ny_gk * ey + nz_gk * ez)) + r' \quad \vert \div '
                       + vorz_str_minus(nx_gk * g_vx + ny_gk * g_vy + nz_gk * g_vz) + r' \quad \to \quad r~=~'
                       + gzahl(ergebnis_r) + r' \quad (2P) \\'
                       + r' \mathrm{Die~Gerade~schneidet~die~Ebene~im~Punkt:} \\ \begin{pmatrix} '
                       + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                       r' \end{pmatrix}' + vorz_str(ergebnis_r) + r' \cdot \begin{pmatrix} '
                       + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                       r' \end{pmatrix} ~=~ \begin{pmatrix} '
                       + gzahl(ex + ergebnis_r*g_vx) + r' \\' + gzahl(ey + ergebnis_r*g_vy) + r' \\'
                       + gzahl(ez + ergebnis_r*g_vz) + r' \\ \end{pmatrix} \quad \to \quad S('
                       + gzahl(ex + ergebnis_r*g_vx) + r' \vert ' + gzahl(ey + ergebnis_r*g_vy) + r' \vert '
                       + gzahl(ez + ergebnis_r*g_vz) + r') \quad (3P) \\')


                punkte_aufg += 3

            aufgabe.extend(('und die Gerade g durch die Punkte:'
                            'A( ' + gzahl(ex) + ' | ' + gzahl(ey) + ' | ' + gzahl(ez) + ' ) und ' 
                            'B( ' + gzahl(fx) + ' | ' + gzahl(fy) + ' | ' + gzahl(fz) + ' ).  \n\n',
                            str(liste_teilaufg[i]) + f') Überprüfe die Lagebeziehung der Geraden g '
                                                     f'zur Ebene E und berechne ggf. den Schnittpunkt. \n\n'))
            loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{AB} ~=~ \begin{pmatrix} '
                           + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                           r' \end{pmatrix} \quad \to \quad g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                           r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                           + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                           r' \end{pmatrix} \quad (2P) \\ '
                           + gzahl(nx_gk) + r' \cdot (' + gzahl(ex) + vorz_str(g_vx) + 'r)'
                           + vorz_str(ny_gk) + r' \cdot (' + gzahl(ey) + vorz_str(g_vy) + 'r)'
                           + vorz_str(nz_gk) + r' \cdot (' + gzahl(ez) + vorz_str(g_vz) + 'r) ~=~'
                           + gzahl(np.dot(punkt_a,n_gk)) + r' \quad (1P) \\'
                           + lsg + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            liste_punkte.append(punkte_aufg)
            i += 1
        if auswahl_gerade_ebene == 'parallel':
            if 'b' in teilaufg:
                punkte_aufg = 4
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{('
                               + gzahl(nx_gk) + ')^2 + (' + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ '
                               + ergebnis_n0 + r' \quad \to \quad '
                               + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} ~=~0' + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1

            if 'c' in teilaufg:
                punkte_aufg = 3
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand der Geraden zur Ebene E. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad E: \vert \begin{bmatrix} \begin{pmatrix} '
                               + gzahl(ex) + r' \\' + gzahl(ex) + r' \\' + gzahl(ez) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \vert ~=~'
                               + latex(abs((np.dot((punkt_e - punkt_a),(1 / n_betrag * n_gk)), 3)))
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]

    def ebene_ebene(nr, teilaufg):
        i = 0
        n_gk = [nx_gk,ny_gk,nz_gk] = punkt_vektor(4)
        n_betrag = np.linalg.norm(n_gk)
        if n_betrag%1 == 0:
            ergebnis_n0 = gzahl(n_betrag)
        else:
            ergebnis_n0 = r' \sqrt{' + gzahl(nx_gk**2 + ny_gk**2 + nz_gk**2) + r'}'
        punkt_d = [dx, dy, dz] = punkt_vektor(3)
        v =  np.array([ny_gk, -1*nx_gk, 0])
        u = np.array([0, nz_gk, -1*ny_gk])
        print('n_gk: ' + str(n_gk))
        print('Punkt D: ' + str(punkt_d))
        print('Vektor v: ' + str(v))
        print('Vektor u: ' + str(u))

        # auswahl = 'schneiden'
        if auswahl_ebene_ebene == 'identisch':
            punkte_aufg = 4
            punkt_a = [ax, ay, az] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(v))
            punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(u))
            punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_b + zzahl(1, 3) * np.array(u))
            g_v = [g_vx, g_vy, g_vz] = np.array(punkt_b - punkt_a)
            k_v = [k_vx, k_vy, k_vz] = np.array(punkt_c - punkt_a)

            lsg = (gzahl(np.dot(punkt_a,n_gk)) + '~=~' + gzahl(np.dot(punkt_d,n_gk))
                   + r' \quad \mathrm{w.A. \quad Die~Ebene~F~liegt~in~der~Ebene~E. \quad (2P) } \\'
                   + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')

        elif auswahl_ebene_ebene == 'parallel':
            punkte_aufg = 6
            abstand = zzahl(1, 7) / 2
            punkt_a = [ax, ay, az] = vektor_ganzzahl(punkt_d + abstand * np.array(n_gk))
            punkt_b = [bx, by, bz] = vektor_ganzzahl(punkt_a + zzahl(1, 3) * np.array(v))
            punkt_c = [cx, cy, cz] = vektor_ganzzahl(punkt_a - zzahl(1, 3) * np.array(u))
            g_v = [g_vx, g_vy, g_vz] = np.array(punkt_b - punkt_a)
            k_v = [k_vx, k_vy, k_vz] = np.array(punkt_c - punkt_a)

            lsg = (gzahl(np.dot(punkt_a,n_gk)) + '~=~' + gzahl(np.dot(punkt_d,n_gk))
                   + r' \quad \mathrm{f.A. \quad Die~Ebene~F~ist~parallel~zur~Ebene~E. \quad (2P) } \\'
                   + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')

        else:
            punkte_aufg = 10
            n = [nx, ny, nz] = punkt_vektor(4)
            punkt_a = [ax, ay, az] = punkt_vektor(3)
            while vektor_kollinear(n, n_gk) == True:
                n = [nx, ny, nz] = punkt_vektor(4)

            g_v = [g_vx, g_vy, g_vz] = vektor_kürzen(zzahl(1,7)/2 * np.array([nz, 0, -1*nx]))
            k_v = [k_vx, k_vy, k_vz] = vektor_kürzen(zzahl(1,7)/2 * np.array([-1*ny, nx, 0]))
            while np.dot(n_gk,k_v) == 0 or np.dot(n_gk,g_v) == 0:
                g_v = [g_vx, g_vy, g_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([nz, 0, -1 * nx]))
                k_v = [k_vx, k_vy, k_vz] = vektor_kürzen(zzahl(1, 7) / 2 * np.array([-1 * ny, nx, 0]))

            print('Vektor n: ' + str(n))
            print('Vektor g_v: ' + str(g_v))
            print('Vektor k_v: ' + str(k_v))
            print(-1*np.dot(n_gk,k_v))
            print(np.dot(n_gk,g_v))
            g_stütz = [g_sx, g_sy, g_sz] = punkt_a + Rational(np.dot(punkt_d - punkt_a,n_gk),np.dot(n_gk,g_v))*g_v
            g_richtung = [g_rx, g_ry, g_rz] = Rational(-1*np.dot(n_gk,k_v), np.dot(n_gk,g_v))*g_v + k_v

            lsg = (gzahl(np.dot(punkt_a,n_gk)) + vorz_str(np.dot(n_gk,g_v)) + 'r'
                   + vorz_str(np.dot(n_gk,k_v)) + 's ~=~' + gzahl(np.dot(punkt_d,n_gk)) + r' \quad \vert '
                   + vorz_str(-1*np.dot(punkt_a,n_gk)) + r' \quad \vert '+ vorz_str(-1 * np.dot(n_gk,k_v))
                   + r's \quad \to \quad ' + gzahl(np.dot(n_gk,g_v)) + 'r ~=~'
                   + gzahl(np.dot(punkt_d - punkt_a,n_gk)) + vorz_str(np.dot(n_gk,k_v))
                   + r's \quad \vert \div' + vorz_str_minus(np.dot(n_gk,g_v)) + r' \quad (2P) \\ r ~=~'
                   + gzahl(Rational(np.dot(punkt_d - punkt_a,n_gk), np.dot(n_gk,g_v)))
                   + vorz_str(Rational(-1*np.dot(n_gk,k_v), np.dot(n_gk,g_v)))
                   + r's \quad \mathrm{Die~Ebene~F~liegt~in~der~Ebene~E. \quad (2P) } \\'
                   + r' \quad \mathrm{Schnittgerade~bestimmen,~indem~man~r~in~F~einsetzt} \\'
                   + r' \overrightarrow{x} ~=~ \begin{pmatrix} '
                   + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   r' \end{pmatrix} ~+~ (' + gzahl(Rational(np.dot(punkt_d - punkt_a,n_gk), np.dot(n_gk,g_v)))
                   + vorz_str(Rational(np.dot(n_gk,k_v), np.dot(n_gk,g_v)))
                   + r's) \cdot \begin{pmatrix} '
                   + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                   r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                   + gzahl(k_vx) + r' \\' + gzahl(k_vy) + r' \\' + gzahl(k_vz) + r' \\'
                   + r' \end{pmatrix} ~=~ \begin{pmatrix}'
                   + gzahl(g_sx) + r' \\' + gzahl(g_sy) + r' \\' + gzahl(g_sz) + r' \\'
                   r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                   + gzahl(g_rx) + r' \\' + gzahl(g_ry) + r' \\' + gzahl(g_rz) + r' \\'
                   + r' \end{pmatrix} \quad (2P) \\'
                   + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben sind die Ebenen E und F mit',
                   r' E: ~' + vorz_gzahl(nx_gk) + 'x' + vorz_str(ny_gk) + 'y' + vorz_str(nz_gk) + 'z ='
                   + gzahl(np.dot(punkt_d,n_gk))
                   + r' \quad \mathrm{und} \quad F: \overrightarrow{x} ~=~ \begin{pmatrix} '
                   + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\'
                   r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                   + gzahl(g_vx) + r' \\' + gzahl(g_vy) + r' \\' + gzahl(g_vz) + r' \\'
                   r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                   + gzahl(k_vx) + r' \\' + gzahl(k_vy) + r' \\' + gzahl(k_vz) + r' \\'
                   r' \end{pmatrix} ']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        grafiken_aufgaben = ['', '', '']
        grafiken_loesung = ['']


        if 'a' in teilaufg:
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
            grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')

            aufgabe.append(str(liste_teilaufg[i]) + f') Bestimmen Sie die Lagebeziehung der Ebenen E und F '
                                              f'und berechnen Sie ggf. die Schnittgerade. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + gzahl(nx_gk) + r' \cdot (' + gzahl(ax)
                           + vorz_str(g_vx) + 'r' + vorz_str(k_vx) + 's)' + vorz_str(ny_gk) + '(' + gzahl(ay)
                           + vorz_str(g_vy) + 'r' + vorz_str(k_vy) + 's)' + vorz_str(nz_gk) + '(' + gzahl(az)
                           + vorz_str(g_vz) + 'r' + vorz_str(k_vz) + 's) ~=~ ' + gzahl(np.dot(punkt_d,n_gk))
                           + r' \quad (1P) \\' + gzahl(nx_gk * ax) + vorz_str(nx_gk * g_vx) + 'r'
                           + vorz_str(nx_gk * k_vx) + 's' + vorz_str(ny_gk * ay) + vorz_str(ny_gk * g_vy) + 'r'
                           + vorz_str(ny_gk * k_vy) + 's' + vorz_str(nz_gk * az) + vorz_str(nz_gk * g_vz) + 'r'
                           + vorz_str(nz_gk * k_vz) + 's ~=~ ' + gzahl(np.dot(punkt_d,n_gk)) + r'\quad (1P) \\'
                           + lsg)

            liste_punkte.append(punkte_aufg)
            i += 1
        if auswahl_ebene_ebene == 'parallel':
            if 'b' in teilaufg:
                punkte_aufg = 4
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append(f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)
                punkt_aE = [ax_E, ay_E, az_E] = np.array([Rational(np.dot(punkt_d,n_gk),nx_gk),0,0])
                aufgabe.append(str(liste_teilaufg[i]) + f') Stellen Sie die hessische Normalform der Ebene E auf. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \sqrt{(' + gzahl(nx_gk) + ')^2 + ('
                               + gzahl(ny_gk) + ')^2 + (' + gzahl(nz_gk) + r')^2 } ~=~ ' + ergebnis_n0
                               + r' \quad \to \quad ' + r' E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} ~=~0' + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1

            if 'c' in teilaufg:
                punkte_aufg = 3
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                grafiken_aufgaben.append( f'Aufgabe_{nr}{liste_teilaufg[i]}')
                grafiken_loesung.append(f'Loesung_{nr}{liste_teilaufg[i]}')
                liste_punkte.append(punkte_aufg)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie den Abstand des Punktes P zur Ebene E. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad E: \vert \begin{bmatrix}'
                               + r' \begin{pmatrix}' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ '
                               + r' \end{pmatrix} ~-~ \begin{pmatrix} '
                               + gzahl(ax_E) + r' \\' + gzahl(ay_E) + r' \\' + gzahl(az_E) + r' \\'
                               + r' \end{pmatrix} \end{bmatrix} \cdot \frac{1}{' + ergebnis_n0 + r'} \begin{pmatrix} '
                               + gzahl(nx_gk) + r' \\' + gzahl(ny_gk) + r' \\' + gzahl(nz_gk) + r' \\'
                               + r' \end{pmatrix} \vert ~=~' + gzahl(abs(N(np.dot((punkt_a-punkt_aE),1/n_betrag*n_gk),3)))
                               + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
                i += 1

        return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung]


    aufgaben = [punkte_ebene(1, ['a', 'b', 'c', 'd', 'e']),
                gerade_ebene(2,['a', 'b', 'c']),
                ebene_ebene(3,['a', 'b', 'c'])]

    # erstellen der Tabelle zur Punkteübersicht
    Punkte = (sum(liste_punkte[1:]))
    liste_bez.append('Summe')
    liste_punkte.append(str(Punkte))
    anzahl_spalten = len(liste_punkte)
    liste_ergebnis_z1 = ['erhaltene']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z1.append('')
    liste_ergebnis_z2 = ['Punkte']
    for p in range(anzahl_spalten - 1):
        liste_ergebnis_z2.append('')

    spalten = '|'
    for p in liste_punkte:
        spalten += 'c|'

    table2 = Tabular(spalten, row_height=1.2)
    table2.add_hline()
    table2.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben'),))
    table2.add_hline()
    table2.add_row(liste_bez)
    table2.add_hline()
    table2.add_row(liste_punkte)
    table2.add_hline()
    table2.add_row(liste_ergebnis_z1)
    table2.add_row(liste_ergebnis_z2)
    table2.add_hline()

    # Angaben für den Test im pdf-Dokument
    Datum = datetime.date.today().strftime('%d.%m.%Y')
    Kurs = 'Grundkurs'
    Fach = 'Mathematik'
    Klasse = '13'
    Lehrer = 'Herr Herrys'
    Art = 'Test'
    Titel = 'Lagebeziehung und Abstände von Ebenen'

    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))  # fügt das Package 'amsfonts' hinzu, für das \mathbb{R} für reelle Zahlen
        # erste Seite
        table1 = Tabular('|c|c|c|c|c|c|', row_height=1.2)
        table1.add_row((MultiColumn(6, align='c', data=MediumText(bold('Torhorst - Gesamtschule'))),))
        table1.add_row((MultiColumn(6, align='c', data=SmallText(bold('mit gymnasialer Oberstufe'))),))
        table1.add_hline()
        table1.add_row('Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:', 'Art:')
        table1.add_hline()
        table1.add_row(Klasse, Fach, Kurs, Lehrer, Datum, Art)
        table1.add_hline()
        Aufgabe.append(table1)
        Aufgabe.append(' \n\n\n\n')
        Aufgabe.append(LargeText(bold(f' {Titel} \n\n')))
        for aufgabe in aufgaben:
            k = 0
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[2][k], width='200px')
                else:
                    Aufgabe.append(elements)
                k += 1

        Aufgabe.append('\n\n')
        Aufgabe.append(table2)

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mKontrolle erstellt\033[0m')

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            k = 0
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Loesung.append(elements)
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3][k], width='200px')
                else:
                    Loesung.append(elements)
                k += 1
        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)
        print('\033[38;2;0;220;120m\033[1mErwartungshorizont erstellt\033[0m')

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_Arbeiten = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
    print()  # Abstand zwischen den Arbeiten (im Terminal)
