import math
import random, sys, string, datetime
import numpy as np
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Math)
from pylatex.utils import bold
from threading import Thread

# Definition der Funktionen

a, b, c, d, e, f, g, r, s, x, y, z = symbols('a b c d e f g r s x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]


def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k

def nzahl(p, q):
    k = random.randint(p, q)
    return k

def vorz(k):
    if k == -1:
        return '-'
    elif k == 1:
        return '+'
    else:
        pass

def vorz_str(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'

def gzahl(k):
    if k%1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def vorz_str_minus(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def erstellen(Teil):
    print(f'\n\033[1;35m{Teil}\033[0m')
    liste_bez = ['Aufgabe']
    liste_punkte = ['Punkte']

    def punkt_vektor(p):
        return np.array([zzahl(1,p), zzahl(1,p), zzahl(1,p)])

    def faktorliste(n, p=1,q=10):
        return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

    def vektor_runden(vec,p):
        return [N(elements,p) for elements in vec]
    # Berechnung für die Aufgaben
    def vektor_ganzzahl(vec):
        return np.array([int(element) if element % 1 == 0 else element for element in vec])

    def vektor_kürzen(vec):
        faktor = [x + 1 for x in range(50)]
        list = np.array(vec)
        i = 0
        for element in vec:
            k = 0
            if list[i] % 1 == 0:
                i += 1
            else:
                while (list[i] * faktor[k]) % 1 != 0 and k < 49:
                    k += 1
                list = list * faktor[k]
                i += 1
        # print('erweitert: ' + str(list))
        teiler = [x + 1 for x in range(int(max(list)/2))]
        for zahl in teiler:
            treffer = [1 for x in list if x % zahl == 0]
            if sum(treffer) == len(vec):
                list = list / zahl
        # print('gekürzt: ' + str(list))
        list = np.array([int(element) if element % 1 == 0 else element for element in list])
        return np.array(list)

    def gerade(nr, teilaufg):
        i = 0
        punkt_a = [ax, ay, az] = punkt_vektor(3)
        punkt_b = [bx, by, bz] = punkt_a + punkt_vektor(3)
        v = [vx, vy, vz] = vektor_ganzzahl((punkt_b) - (punkt_a))
        p = random.choice([0,1])
        if p == 0:
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,30)/5)*v)
        else:
            punkt_t = [tx, ty, tz] = vektor_ganzzahl(punkt_a + (zzahl(1,30)/5)*v + [1, 1, 1])

        lx, ly, lz = vektor_ganzzahl([(tx-ax)/vx, (ty-ay)/vy, (tz-az)/vz])

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + str(ax)  + ' | ' + str(ay) + ' | ' + str(az) + ' ), ' 
                   'B( ' + str(bx)  + ' | ' + str(by) + ' | ' + str(bz) + ' ) und '
                   'T( ' + str(N(tx,3))  + ' | ' + str(N(ty,3)) + ' | ' + str(N(tz,3)) + ' ).  \n\n']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            loesung_1 = (r' \overrightarrow{AB} ~=~'
                         r' \begin{pmatrix} '
                         + latex(v[0]) + r' \\' + latex(v[1]) + r' \\' + latex(v[2]) + r' \\'
                         r' \end{pmatrix} \quad \to \quad '
                         r' g: \overrightarrow{x} \ ~=~'
                         r' \begin{pmatrix} '
                         + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + latex(v[0]) + r' \\' + latex(v[1]) + r' \\' + latex(v[2]) + r' \\'
                         r' \end{pmatrix} \quad (3P) \\')

            aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                              f' welche die Punkte A und B enthält. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i +=1

        if b in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            loesung_1 =  (r' \begin{pmatrix} '
                         + latex(N(tx,3)) + r' \\' + latex(N(ty,3)) + r' \\' + latex(N(tz,3)) + r' \\'
                         r' \end{pmatrix} ~=~ \begin{pmatrix} '
                         + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                         r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                         + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                         r' \end{pmatrix} \to \begin{matrix} '
                         + latex(N(tx,3)) + '~=~' + latex(ax) + vorz_str(vx) + r' \cdot r' + r' \\'
                         + latex(N(ty,3)) + '~=~' + latex(ay) + vorz_str(vy) + r' \cdot r' + r' \\'
                         + latex(N(tz,3)) + '~=~' + latex(az) + vorz_str(vz) + r' \cdot r' + r' \\'
                         r' \end{matrix} \quad \to \quad \begin{matrix} '
                         + 'r=' + latex(N(lx,3)) + r' \\' + 'r=' + latex(N(ly,3)) + r' \\'
                         + 'r=' + latex(N(lz,3)) + r' \\'
                         r' \end{matrix} \\')
            if lx == ly == lz:
                loesung_2 = r' \mathrm{Der~Punkt~liegt~auf~der~Geraden.} \quad (4P) \\'
            else:
                loesung_2 = r' \mathrm{Der~Punkt~liegt~nicht~auf~der~Geraden.} \quad (4P) \\'

            aufgabe.append(str(teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T auf g liegt. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1 + loesung_2
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i +=1

        return aufgabe, loesung

    def lagebeziehung(nr, teilaufg):
        i = 0
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

        if a in teilaufg:
            auswahl = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
            # auswahl = 'schneiden'
            if auswahl == 'identisch':
                punkte_aufg = 7
                liste_punkte.append(punkte_aufg)
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                punkt_c = [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(v)) # Punkt C liegt auf h
                w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10 * np.array(v)) # Vektor w ist der Richtungsvektor von h
                loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                             r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             'r~=~' + latex(N(vx/wx,3)) + r' \\'
                             'r~=~' + latex(N(vy/wy,3)) + r' \\'
                             'r~=~' + latex(N(vz/wz,3)) + r' \\'
                             r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3P) \\\\'
                             r' \mathrm{Überprüfen~ob~Stützvektor~von~g~auf~h~liegt.} \hspace{15em} \\'
                             r' \begin{pmatrix} '
                             + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                             r' \end{pmatrix} ~=~ \begin{pmatrix} '
                             + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                             r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             + latex(ax) + '~=~' + latex(cx) + vorz_str(wx) + r' \cdot r' + r' \\'
                             + latex(ay) + '~=~' + latex(cy) + vorz_str(wy) + r' \cdot r' + r' \\'
                             + latex(az) + '~=~' + latex(cz) + vorz_str(wz) + r' \cdot r' + r' \\'
                             r' \end{matrix} \quad \to \quad \begin{matrix} '
                             + 'r=' + latex(N((ax-cx)/wx,3)) + r' \\' + 'r=' + latex(N((ay-cy)/wy,3)) + r' \\'
                             + 'r=' + latex(N((az-cz)/wz,3)) + r' \\ \end{matrix} \\'
                             r' \mathrm{Die~Geraden~g~und~h~sind~identisch.} \quad (4P) \\'
                             + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            elif auswahl == 'parallel':
                punkte_aufg = 7
                liste_punkte.append(punkte_aufg)
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                punkt_c =  [cx,cy,cz] = vektor_ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(u)) # Punkt C liegt auf h
                w = [wx, wy, wz] = vektor_ganzzahl(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
                loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                             r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             'r~=~' + latex(N(vx/wx,3)) + r' \\'
                             'r~=~' + latex(N(vy/wy,3)) + r' \\'
                             'r~=~' + latex(N(vz/wz,3)) + r' \\'
                             r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~parallel} \quad (3P) \\\\'
                             r' \mathrm{Überprüfen~ob~Stützvektor~von~g~auf~h~liegt.} \hspace{15em} \\'
                             r' \begin{pmatrix} '
                             + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                             r' \end{pmatrix} ~=~ \begin{pmatrix} '
                             + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                             r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             + latex(ax) + '~=~' + latex(cx) + vorz_str(wx) + r' \cdot r' + r' \\'
                             + latex(ay) + '~=~' + latex(cy) + vorz_str(wy) + r' \cdot r' + r' \\'
                             + latex(az) + '~=~' + latex(cz) + vorz_str(wz) + r' \cdot r' + r' \\'
                             r' \end{matrix} \quad \to \quad \begin{matrix} '
                             + 'r=' + latex(N((ax-cx)/wx,3)) + r' \\' + 'r=' + latex(N((ay-cy)/wy,3)) + r' \\'
                             + 'r=' + latex(N((az-cz)/wz,3)) + r' \\ \end{matrix} \\'
                             r' \mathrm{Die~Geraden~g~und~h~sind~echt~parallel.} \quad (4P) \\'
                             + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            elif auswahl == 'windschief':
                punkte_aufg = 15
                liste_punkte.append(punkte_aufg)
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                punkt_c =  [cx,cy,cz] = vektor_ganzzahl((punkt_a) + nzahl(1,6)/2 * np.array(u)) # Punkte C und D liegen auf h
                punkt_d =  [dx,dy,dz] = vektor_ganzzahl((punkt_c) - nzahl(1,6)/2
                                                        * np.cross(np.array(u),np.array(v)))
                w = [wx, wy, wz] = vektor_ganzzahl(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
                lsgr = -1*(ax*wy-ay*wx-cx*wy+cy*wx)/(vx*wy-vy*wx)
                lsgs = (-1*(ax*vy)/(vx*wy-vy*wx))+((ay*vx)/(vx*wy-vy*wx))+((cx*vy)/(vx*wy-vy*wx))-((cy*vx)/(vx*wy-vy*wx))
                if vx != 0 and wx != 0:
                    loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                                 + latex(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1*cx)
                                 + r' ~ \vert \div ' + vorz_str_minus(wx) + r' \quad \to \quad s ~=~ '
                                 + latex(N((ax-cx)/wx,3)) + vorz_str(N(vx/wx,3)) + r' \cdot r \quad (2P) \\')
                    if vy != 0 and wy != 0:
                        loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                     + latex(cy) + vorz_str(wy) + r' \cdot \big( ' + latex(N((ax-cx)/wx,3))
                                     + vorz_str(N(vx/wx,3)) + r' \cdot r \big) \\'
                                     + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + latex(N((wx*cy + wy*(ax - cx))/wx,3))
                                     + vorz_str(N(wy*vx/wx,3)) + r' \cdot r \quad \vert ~'
                                     + vorz_str(-1*vy) + r' \cdot r \quad \vert ~'
                                     + vorz_str(-1*N((wx*cy + wy*(ax - cx))/wx,3)) + r' \quad (2P) \\'
                                     + latex(N(ay-(wx*cy+wy*(ax-cx))/wx,3)) + '~=~' + latex(N((vx*wy-vy*wx)/wx,3))
                                     + r' \cdot r \quad \vert \div ' + vorz_str_minus(N((vx*wy-vy*wx)/wx,3))
                                     + r' \quad \to \quad r~=~' + latex(N(lsgr,3))
                                     + r' \quad \mathrm{und} \quad s ~=~'
                                     + latex(N(lsgs,3)) + r' \quad (3P) \\')
                        if vz != 0 and wz != 0:
                            loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + latex(az) + vorz_str(vz)
                                         + r' \cdot (' + latex(N(lsgr,3)) + r') ~=~ ' + latex(cz) + vorz_str(wz)
                                         + r' \cdot (' + latex(N(lsgs,3)) + r') \quad \to \quad ' + latex(N(az+vz*lsgr,3))
                                         + '~=~' + latex(N(cz+wz*lsgs,3))
                                         + r' \quad (2P) \\ \to \mathrm{Widerspruch} ~ \to ~ '
                                           r'\mathrm{Die~Geraden~sind~Windschief.} \quad (1P)')
                        else:
                            sys.exit('vz oder wz ist null.')
                    else:
                        sys.exit('vy oder wy ist null.')
                else:
                    sys.exit('va oder wa ist null.')


                loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                             r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             'r~=~' + latex(N(vx/wx,3)) + r' \\'
                             'r~=~' + latex(N(vy/wy,3)) + r' \\'
                             'r~=~' + latex(N(vz/wz,3)) + r' \\'
                             r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3P) \\\\'
                             r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g~=~h} \hspace{5em} \\'
                             r' \begin{pmatrix} ' + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                             r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                             + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ \begin{pmatrix} '
                             + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                             r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                             'I: ~~' + latex(ax) + vorz_str(vx) + r' \cdot r ~=~' + r' \\'
                             'II: ~' + latex(ay) + vorz_str(vy) + r' \cdot r ~=~' + r' \\'
                             'III: ~' + latex(az) + vorz_str(vz) + r' \cdot r~=~' + r' \\'
                             r' \end{matrix} \begin{matrix} '
                             + latex(cx) + vorz_str(wx) + r' \cdot s' + r' \\'
                             + latex(cy) + vorz_str(wy) + r' \cdot s' + r' \\'
                             + latex(cz) + vorz_str(wz) + r' \cdot s' + r' \\'
                             r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4 + r' \\'
                             + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')


            else:
                punkte_aufg = 17
                liste_punkte.append(punkte_aufg)
                liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
                punkt_d =  [dx,dy,dz] = vektor_ganzzahl(punkt_a + zzahl(1, 7) / 2 * np.array(v)) # Punkte C und D liegen auf h
                punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_d + zzahl(1, 7) / 2 * np.array(u))
                w = vektor_ganzzahl(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
                [wx, wy, wz] = vektor_ganzzahl(vektor_runden(w,3))
                lsgr = -1 * (ax * wy - ay * wx - cx * wy + cy * wx) / (vx * wy - vy * wx)
                lsgs = (-1*(ax*vy)/(vx*wy-vy*wx))+((ay*vx)/(vx*wy-vy*wx))+((cx*vy)/(vx*wy-vy*wx))-((cy*vx)/(vx*wy-vy*wx))
                schnittpunkt_s = punkt_c + lsgr*w
                [sx, sy, sz] = vektor_runden(schnittpunkt_s,3)
                if vx != 0 and wx != 0:
                    loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(ax) + vorz_str(vx) + r' \cdot r ~=~'
                                 + latex(cx) + vorz_str(wx) + r' \cdot s \quad \vert ' + vorz_str(-1 * cx)
                                 + r' ~ \vert \div ' + vorz_str_minus(wx) + r' \quad \to \quad s ~=~ '
                                 + latex(N((ax - cx) / wx, 3)) + vorz_str(N(vx / wx, 3)) + r' \cdot r \quad (2P) \\')
                    if vy != 0 and wy != 0:
                        loesung_3 = (r' \mathrm{s~in~II~einsetzen:} \quad ' + str(ay) + vorz_str(vy) + r' \cdot r ~=~'
                                     + latex(cy) + vorz_str(wy) + r' \cdot \big( ' + latex(N((ax - cx) / wx, 3))
                                     + vorz_str(N(vx / wx, 3)) + r' \cdot r \big) \\'
                                     + str(ay) + vorz_str(vy) + r' \cdot r ~=~' + latex(N((wx * cy + wy * (ax - cx)) / wx, 3))
                                     + vorz_str(N(wy * vx / wx, 3)) + r' \cdot r \quad \vert ~'
                                     + vorz_str(-1 * vy) + r' \cdot r \quad \vert ~'
                                     + vorz_str(-1 * N((wx * cy + wy * (ax - cx)) / wx, 3)) + r' \quad (2P) \\'
                                     + latex(N(ay - (wx * cy + wy * (ax - cx)) / wx, 3)) + '~=~'
                                     + latex(N((vx * wy - vy * wx) / wx, 3)) + r' \cdot r \quad \vert \div '
                                     + vorz_str_minus(N((vx * wy - vy * wx) / wx, 3))
                                     + r' \quad \to \quad r~=~' + latex(N(lsgr, 3))
                                     + r' \quad \mathrm{und} \quad s ~=~'
                                     + latex(N(lsgs, 3)) + r' \quad (3P) \\')
                        if vz != 0 and wz != 0:
                            loesung_4 = (r' \mathrm{r~und~s~in~III~einsetzen:~} \quad ' + latex(az) + vorz_str(vz)
                                         + r' \cdot (' + latex(N(lsgr, 3)) + r') ~=~ ' + latex(cz) + vorz_str(wz)
                                         + r' \cdot (' + latex(N(lsgs, 3)) + r') \quad \to \quad ' + latex(N(az + vz * lsgr, 3))
                                         + '~=~' + latex(N(cz + wz * lsgs, 3))
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
                             r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                             'r~=~' + latex(N(vx/wx,3)) + r' \\'
                             'r~=~' + latex(N(vy/wy,3)) + r' \\'
                             'r~=~' + latex(N(vz/wz,3)) + r' \\'
                             r' \end{matrix} \quad \to \quad \mathrm{g~und~h~sind~nicht~parallel} \quad (3P) \\\\'
                             r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g~=~h} \hspace{5em} \\'
                             r' \begin{pmatrix} ' + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                             r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                             + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                             r' \end{pmatrix} ~=~ \begin{pmatrix} '
                             + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                             r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                             + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                             r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                             'I: ~~' + latex(ax) + vorz_str(vx) + r' \cdot r ~=~' + r' \\'
                             'II: ~' + latex(ay) + vorz_str(vy) + r' \cdot r ~=~' + r' \\'
                             'III: ~' + latex(az) + vorz_str(vz) + r' \cdot r~=~' + r' \\'
                             r' \end{matrix} \begin{matrix} '
                             + latex(cx) + vorz_str(wx) + r' \cdot s' + r' \\'
                             + latex(cy) + vorz_str(wy) + r' \cdot s' + r' \\'
                             + latex(cz) + vorz_str(wz) + r' \cdot s' + r' \\'
                             r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4 + r' \\'
                             + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')

                # print(v), print(w), print(punkt_c)

            aufgabe.append(r'g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                           r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                           + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                           r' \end{pmatrix} \quad \mathrm{und} \quad h: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                           r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                           + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                           r' \end{pmatrix}\\')
            aufgabe.append(str(teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad \mathit{Die~Auswahl~war~'
                           + auswahl + r'} \hspace{25em} \\' + loesung_1)
            i += 1


        if b in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            punkt_f =  [fx,fy,fz] = vektor_ganzzahl(np.array(punkt_a) + zzahl(1, 7) / 2 * np.array(v)) # Punkte C und D liegen auf h
            punkt_e =  [ex,ey,ez] = vektor_ganzzahl(np.array(punkt_f) - nzahl(1,7) / 2 * np.array(punkt_vektor(4)))
            p = vektor_ganzzahl(np.array(punkt_f) - np.array(punkt_e)) # Vektor w ist der Richtungsvektor von h
            [px, py, pz] = vektor_ganzzahl(vektor_runden(p, 3))
            sp_vp = np.vdot(v,p)
            l_v = np.linalg.norm(v)
            l_p = np.linalg.norm(p)

            aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
            aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                   + latex(ex) + r' \\' + latex(ey) + r' \\' + latex(ez) + r' \\'
                   r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                   + latex(px) + r' \\' + latex(py) + r' \\' + latex(pz) + r' \\'
                   r' \end{pmatrix} \quad ')
            aufgabe.append(str(teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad cos( \gamma ) = \frac{ \vert \overrightarrow{v}'
                           r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                           r' \vert \overrightarrow{u} \vert } \quad \vert ~ cos^{-1} \quad \to \quad '
                           r' \gamma ~=~ cos^{-1} \Big( \frac{ \vert \overrightarrow{v}'
                           r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                           r' \vert \overrightarrow{u} \vert } \Big) \quad (1P) \\'
                           r' \vert \overrightarrow{v} \cdot \overrightarrow{u} \vert'
                           r'~=~ \vert ' + vorz_str_minus(vx) + r' \cdot ' + vorz_str_minus(px)
                           + '+' + vorz_str_minus(vy) + r' \cdot ' + vorz_str_minus(py)
                           + '+' + vorz_str_minus(vz) + r' \cdot ' + vorz_str_minus(pz) + r' \vert ~=~'
                           + latex(abs(N(sp_vp,3))) + r' \quad (2P) \\'
                           r' \vert \overrightarrow{u} \vert ~=~ \sqrt{ (' + str(vx) + ')^2 ~+~('
                           + str(vy) + ')^2 ~+~(' + str(vz) + ')^2} ~=~ ' + latex(N(l_v,3))
                           + r' \quad \mathrm{und} \quad \vert \overrightarrow{v} \vert ~=~ \sqrt{ ('
                           + str(px) + ')^2 ~+~(' + str(py) + ')^2 ~+~(' + str(pz)
                           + ')^2} ~=~ ' + latex(N(l_p,3)) + r' \quad (2P) \\'
                           + r' \gamma ~=~ cos^{-1} \Big( \frac{' + latex(abs(N(sp_vp,3))) + '}{'
                           + latex(N(l_v,3)) + r' \cdot ' + latex(N(l_p,3))
                           + r'} \Big) ~=~' + latex(N(np.degrees(np.arccos(abs(sp_vp)/(l_v*l_p))),3))
                           + r' \quad (2P) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        return aufgabe, loesung

    def ebenen(nr, teilaufg):
        i = 0
        v_teiler = zzahl(1, 3)
        punkt_a = [ax, ay, az] = punkt_vektor(3) # Punkt A liegt auf Gerade g_1
        v = [vx, vy, vz] = vektor_ganzzahl(np.array([zzahl(1, 6) / 2 * v_teiler,
                                                     zzahl(1, 6) / 2 * v_teiler, v_teiler]))
        # Vektor v ist der Richtungsvektor von Geraden g_1
        # Vektor u steht orthogonal auf v
        ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
        uz = - 1 * (vx*ux + vy * uy)/vz
        u = vektor_ganzzahl([ux, uy, uz])
        punkt_b = [bx,by,bz] = vektor_ganzzahl(punkt_a + v) # Punkte C und D liegen auf h
        punkt_c = [cx,cy,cz] = vektor_ganzzahl(punkt_b + zzahl(1, 7) / 2 * np.array(u))
        w = vektor_ganzzahl(punkt_c - punkt_a) # Vektor w ist der Richtungsvektor von h
        [wx, wy, wz] = vektor_runden(w,3)
        n = [nx, ny, nz] = vektor_ganzzahl(np.cross(v,w))
        n_gk = [nx_gk, ny_gk, nz_gk] = vektor_kürzen(n)

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
                   'A( ' + str(ax) + ' | ' + str(ay) + ' | ' + str(az) + ' ), ' 
                   'B( ' + str(bx) + ' | ' + str(by) + ' | ' + str(bz) + ' ) und '
                   'C( ' + str(cx) + ' | ' + str(cy) + ' | ' + str(cz) + ' ).  \n\n']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            punkte_aufg = 4
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Parametergleichung der Ebene E auf, '
                                              f'welche die Punkte A, B und C enthält. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{AB} ~=~ \begin{pmatrix} '
                           + latex(bx-ax) + r' \\' + latex(by-ay) + r' \\' + latex(bz-az) + r' \\'
                           r' \end{pmatrix} \quad \mathrm{und} \quad \overrightarrow{AC} ~=~ \begin{pmatrix} '
                           + latex(cx-ax) + r' \\' + latex(cy-ay) + r' \\' + latex(cz-az) + r' \\'
                           r' \end{pmatrix} \quad \to \quad E: \overrightarrow{x} ~=~ \begin{pmatrix} '
                           + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                           r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                           + latex(bx - ax) + r' \\' + latex(by - ay) + r' \\' + latex(bz - az) + r' \\'
                           r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix}'
                           + latex(cx - ax) + r' \\' + latex(cy - ay) + r' \\' + latex(cz - az) + r' \\'
                           r' \end{pmatrix} \quad (2P) \\'
                           r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if a and b in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(teilaufg[i]) + f') Formen Sie die Gleichung für Ebene E in '
                                              f'Normalen- und Koordinatenform um. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad \overrightarrow{n} ~=~ \begin{pmatrix} '
                           + latex(vy*wz) + '-' + vorz_str_minus(vz*wy) + r' \\'
                           + latex(vz*wx) + '-' + vorz_str_minus(vx*wz) + r' \\'
                           + latex(vx*wy) + '-' + vorz_str_minus(vy*wx) + r' \\ \end{pmatrix} ~=~ \begin{pmatrix} '
                           + latex(nx) + r' \\' + latex(ny) + r' \\' + latex(nz) + r' \\'
                           r' \end{pmatrix} \quad (2P) \quad \mathrm{und}'
                           r'\quad E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                           + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                           r' \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                           + latex(nx_gk) + r' \\' + latex(ny_gk) + r' \\' + latex(nz_gk) + r' \\'
                           r' \end{pmatrix} ~=~0 \quad (2P) \\'
                           r'E:~' + latex(nx_gk) + r' \cdot x' + vorz_str(ny_gk) + r' \cdot y' + vorz_str(nz_gk) + r' \cdot z'
                           + '~=~' + latex(np.dot(punkt_a,n_gk)) + r' \quad (2P) \\'
                           + r' \mathrm{insgesamt~' + str(punkte_aufg) + r'~Punkte} \\')
            i += 1

        if a and b and c in teilaufg:
            punkte_aufg = 3
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            parameter_r = zzahl(1,6)/2
            parameter_s = zzahl(1,6)/2
            zufallszahl = random.randint(1,2)
            if zufallszahl == 1:
                punkt_d = [dx,dy,dz] = vektor_ganzzahl(punkt_a + parameter_r*v + parameter_s*w)
            else:
                punkt_d = [dx,dy,dz] = vektor_ganzzahl(punkt_a + punkt_vektor(1) + parameter_r * v + parameter_s * w)
            if np.array_equal(punkt_d, punkt_a + parameter_r * v + parameter_s * w):
                lsg = r' \quad \mathrm{w.A.} \\ \mathrm{Der~Punkt~D~liegt~auf~der~Geraden.} \quad (3P) \\'
            else:
                lsg = r' \quad \mathrm{f.A.} \\ \mathrm{Der~Punkt~D~liegt~nicht~auf~der~Geraden.} \quad (3P) \\'
            aufgabe.append('Gegeben ist ein weiterer Punkt D( ' + str(dx) + ' | ' + str(dy) + ' | '
                           + str(dz) + ' ), \n\n')
            aufgabe.append(str(teilaufg[i]) + f') Überprüfen Sie, ob der Punkt D in der Ebene E liegt. \n\n')
            loesung.append(str(teilaufg[i]) + (r') \quad E:~' + latex(nx_gk) + r' \cdot (' + latex(dx) + ')'
                                               + vorz_str(ny_gk) + r' \cdot (' + latex(dy) + ')'
                                               + vorz_str(nz_gk) + r' \cdot (' + latex(dz) + ') ~=~'
                                               + latex(np.dot(punkt_a,n_gk)) + r' \quad \to \quad '
                                               + latex(np.dot(n_gk,punkt_d)) + '~=~' + latex(np.dot(punkt_a,n_gk)) + lsg))
            i += 1

        return aufgabe, loesung

    def ebenen_umformen(nr, teilaufg):
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

        auswahl = random.choice([1,2])
        if auswahl == 1:
            ebenengleichung = normalenform
            andere_darstellungsform = koordinatenform
            lsg = (r' \begin{pmatrix} ' + gzahl(ax) + r' \\' + gzahl(ay) + r' \\' + gzahl(az) + r' \\ \end{pmatrix}')
        else:
            ebenengleichung = koordinatenform
            andere_darstellungsform = (r'E: \begin{bmatrix} \overrightarrow{x} ~-~ \begin{pmatrix} '
                                       + latex(Rational(np.dot(punkt_a,n),nx)) + r' \\' + gzahl(0)
                                       + r' \\' + gzahl(0) + r' \\  \end{pmatrix} \end{bmatrix} \cdot \begin{pmatrix} '
                                       + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                                       r' \end{pmatrix} ~=~ 0')
            lsg = (r' \begin{pmatrix} ' + latex(Rational(np.dot(punkt_a,n),nx)) + r' \\' + gzahl(0)
                   + r' \\' + gzahl(0) + r' \\ \end{pmatrix}')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Gegeben ist die Ebene E mit der folgenden Gleichung:']
        aufgabe.append(ebenengleichung)
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
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

        if b in teilaufg:
            punkte_aufg = 6
            liste_punkte.append(punkte_aufg)
            liste_bez.append(str(nr) + '. ' + str(liste_teilaufg[i]) + ')')
            aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Achsenabschnittsform der Ebenengleichung'
                                              f' auf und zeichnen Sie ein Schrägbild der Ebene. \n\n ')
            loesung.append(str(teilaufg[i]) + (r') \quad ' + koordinatenform + r' \quad \vert \div '
                                               + gzahl(np.dot(punkt_a,n)) + r' \quad \to \quad '
                                               + r'E:~ \frac{x}{' + vorz_str_minus(sx) + r'} + '
                                               r' \frac{y}{' + vorz_str_minus(sy) + r'} + '
                                               r' \frac{z}{' + vorz_str_minus(sz) + r'} ~=~' + str(1)
                                               + r' \quad (4P) \\ \mathrm{Zeichnung: \quad (2P)} \\'))
            i += 1

        return aufgabe, loesung

    aufgaben = [gerade(1, [a, b]),
                lagebeziehung(2, [a,b]),
                ebenen(3,[a,b,c]),
                ebenen_umformen(4, [a,b])]

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
    Art = 'Test II'
    Titel = 'Achsenabschnittsform'

    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        # erste Seite
        table1 = Tabular('|c|c|c|c|c|c|', row_height=1.2)
        table1.add_row((MultiColumn(6, align='c', data=LargeText(bold('Torhorst - Gesamtschule'))),))
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
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    Aufgabe.append(elements)
                    with Aufgabe.create(Figure(position='h!')) as graph:
                        graph.add_image(aufgabe[3], width='200px')
                else:
                    Aufgabe.append(elements)


        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
        Aufgabe.append('\n\n')
        Aufgabe.append('\n\n')

        Aufgabe.append(table2)

        Aufgabe.append('\n\n')
        Aufgabe.append('\n\n')
        with Aufgabe.create(Figure(position='h!')) as koordinatensystem:
            koordinatensystem.add_image('3dim_Koordinatensystem.png', width='400px')

        Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Teil}', clean_tex=true)

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        for loesung in aufgaben:
            for elements in loesung[1]:
                if '~' in elements:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                elif 'Abbildung' in elements:
                    with Loesung.create(Figure(position='h!')) as graph:
                        graph.add_image(loesung[3], width='200px')
                else:
                    Loesung.append(elements)

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()

anzahl_Arbeiten = 3
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_Arbeiten):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')