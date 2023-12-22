import random, sys
import numpy as np
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure, Math
from pylatex.utils import bold
from threading import Thread

# Definition der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k

def nzahl(p, q):
    k = random.randint(p, q)
    return k

def vorz_str(k):
    if k < 0:
        return f'~-~{latex(abs(k))}'
    else:
        return f'~+~{latex(k)}'

def vorz_str_minus(k):
    if k < 0:
        return f'({latex(k)})'
    else:
        return latex(k)

def punkt_vektor(p):
    return [zzahl(1,p), zzahl(1,p), zzahl(1,p)]

def faktorliste(n, p=1,q=10):
    return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

def vektor_runden(vec,p):
    return [N(elements,p) for elements in vec]
# Berechnung für die Aufgaben
def gerade(nr, teilaufg):
    i = 0
    Punkte = 0

    punkt_a = [ax, ay, az] = punkt_vektor(3)
    punkt_b = [bx, by, bz] = [ax + zzahl(1, 3), ay + zzahl(1, 3), az + zzahl(1, 3)]
    v = [vx, vy, vz] =  np.array(punkt_b) - np.array(punkt_a)
    p = random.choice([0,1])
    if p == 0:
        punkt_t = [tx, ty, tz] = np.array(punkt_a) + zzahl(1,30)/5*v
    else:
        punkt_t = [tx, ty, tz] = np.array(punkt_a) + (zzahl(1,30)/5)*v + [1, 1, 1]

    lx, ly, lz = [(tx-ax)/vx, (ty-ay)/vy, (tz-az)/vz]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
               'A( ' + latex(ax)  + ' | ' + latex(ay) + ' | ' + latex(az) + ' ), ' 
               'B( ' + latex(bx)  + ' | ' + latex(by) + ' | ' + latex(bz) + ' ) und '
               'T( ' + str(N(tx,3))  + ' | ' + str(N(ty,3)) + ' | ' + str(N(tz,3)) + ' ).  \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        loesung_1 = (r' \overrightarrow{AB} ~=~'
                     r' \begin{pmatrix} '
                     + latex(v[0]) + r' \\' + latex(v[1]) + r' \\' + latex(v[2]) + r' \\'
                     r' \end{pmatrix} \quad \to \quad '
                     r' g: \overrightarrow{x} \ ~=~'
                     r' \begin{pmatrix} '
                     + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v[0]) + r' \\' + latex(v[1]) + r' \\' + latex(v[2]) + r' \\'
                     r' \end{pmatrix} \quad (4P) \\')

        aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                          f' welche die Punkte A und B enthält. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)
        i +=1
        Punkte += 4

    if b in teilaufg:
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
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1 + loesung_2)
        i +=1
        Punkte += 4

    return aufgabe, loesung, Punkte

def lagebeziehung(nr, teilaufg):
    i = 0
    Punkte = 0
    v_teiler = zzahl(1, 3)
    punkt_a = [ax, ay, az] = punkt_vektor(3) # Punkt A liegt auf Gerade g_1
    v = [vx, vy, vz] = punkt_vektor(4) # Vektor v ist der Richtungsvektor von Geraden g_1
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    uz = - 1 * (vx*ux + vy * uy)/vz
    u = np.array([ux, uy, uz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Gegeben sind die beiden Geraden mit folgenden Gleichungen:']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        auswahl = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
        auswahl = 'windschief'
        if auswahl == 'identisch':
            punkt_c = [cx,cy,cz] = np.array(punkt_a) + zzahl(1,30)/5*np.array(v) # Punkt C liegt auf h
            w = [wx, wy, wz] = zzahl(1,30)/10 * np.array(v) # Vektor w ist der Richtungsvektor von h
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
                         r' \mathrm{Die~Geraden~g~und~h~sind~identisch.} \quad (4P) \\')
            Punkte += 7
        elif auswahl == 'parallel':
            punkt_c =  [cx,cy,cz] = np.array(punkt_a) + zzahl(1,30)/5*np.array(u) # Punkt C liegt auf h
            w = [wx, wy, wz] = zzahl(1,30)/10* np.array(v) # Vektor w ist der Richtungsvektor von h
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
                         r' \mathrm{Die~Geraden~g~und~h~sind~echt~parallel.} \quad (4P) \\')
            Punkte += 7
        elif auswahl == 'windschief':
            punkt_c =  [cx,cy,cz] = np.array(punkt_a) + nzahl(1,6)/2 * np.array(u) # Punkte C und D liegen auf h
            punkt_d =  [dx,dy,dz] = np.array(punkt_c) - nzahl(1,6)/2 * np.cross(np.array(u),np.array(v))
            w = [wx, wy, wz] = punkt_d - punkt_c # Vektor w ist der Richtungsvektor von h
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
                         r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4)
            Punkte += 15

        else:
            punkt_d =  [dx,dy,dz] = np.array(punkt_a) + zzahl(1, 7) / 2 * np.array(v) # Punkte C und D liegen auf h
            punkt_c = [cx,cy,cz] = np.array(punkt_d) + zzahl(1, 7) / 2 * np.array(u)
            w = punkt_d - punkt_c # Vektor w ist der Richtungsvektor von h
            [wx, wy, wz] = vektor_runden(w,3)
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
                         r' \end{matrix} \quad (2P) \\\\'  + loesung_2 + loesung_3 + loesung_4)

            Punkte += 17
            # print(v), print(w), print(punkt_c)

        aufgabe.append(r'g: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                       r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                       r' \end{pmatrix} \quad \mathrm{und} \quad h: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                       + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                       r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                       + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                       r' \end{pmatrix}\\')
        aufgabe.append(str(teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \mathit{Die~Auswahl~war~'
                       + auswahl + r'} \hspace{25em} \\' + loesung_1)
        i += 1


    if b in teilaufg:
        punkt_f =  [fx,fy,fz] = np.array(punkt_a) + zzahl(1, 7) / 2 * np.array(v) # Punkte C und D liegen auf h
        punkt_e =  [ex,ey,ez] = np.array(punkt_f) - nzahl(1,7) / 2 * np.array(punkt_vektor(4))
        p = np.array(punkt_f) - np.array(punkt_e) # Vektor w ist der Richtungsvektor von h
        [px, py, pz] = vektor_runden(p, 3)
        sp_vp = np.vdot(v,p)
        l_v = np.linalg.norm(v)
        l_p = np.linalg.norm(p)

        aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
        aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + latex(ex) + r' \\' + latex(ey) + r' \\' + latex(ez) + r' \\'
               r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + latex(px) + r' \\' + latex(py) + r' \\' + latex(pz) + r' \\'
               r' \end{pmatrix} \quad ')
        aufgabe.append(str(teilaufg[i]) + ') Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')
        loesung.append(str(teilaufg[i]) + (r') \quad cos( \gamma ) = \frac{ \vert \overrightarrow{v}'
                                           r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                                           r' \vert \overrightarrow{u} \vert } \quad \vert ~ cos^{-1} \quad \to \quad '
                                           r' \gamma ~=~ cos^{-1} \Big( \frac{ \vert \overrightarrow{v}'
                                           r' \cdot  \overrightarrow{u} \vert }{ \vert \overrightarrow{v} \vert \cdot '
                                           r' \vert \overrightarrow{u} \vert } \Big] \quad (1P) \\'
                                           r' \vert \overrightarrow{v} \vert \cdot \vert \overrightarrow{u} \vert'
                                           r'~=~ \vert ' + vorz_str_minus(vx) + r' \cdot ' + vorz_str_minus(px)
                                           + '+' + vorz_str_minus(vy) + r' \cdot ' + vorz_str_minus(py)
                                           + '+' + vorz_str_minus(vz) + r' \cdot ' + vorz_str_minus(pz) + r' \vert ~=~'
                                           + latex(abs(N(sp_vp,3))) + r' \quad (2P) \\'
                                           r' \vert \overrightarrow{v} \vert ~=~ \sqrt{ (' + str(vx) + ')^2 ~+~('
                                           + str(vy) + ')^2 ~=~(' + str(vz) + ')} ~=~ ' + latex(N(l_v,3))
                                           + r' \quad \mathrm{und} \quad \vert \overrightarrow{v} \vert ~=~ \sqrt{ ('
                                           + str(px) + ')^2 ~+~(' + str(py) + ')^2 ~=~(' + str(pz)
                                           + ')} ~=~ ' + latex(N(l_p,3)) + r' \quad (2P) \\'
                                           + r' \gamma ~=~ cos^{-1} \Big( \frac{' + latex(abs(N(sp_vp,3))) + '}{'
                                           + latex(N(l_v,3)) + r' \cdot ' + latex(N(l_p,3))
                                           + r'} \Big) ~=~' + latex(N(np.degrees(np.arccos(abs(sp_vp)/(l_v*l_p))),3)) + r' \quad (2P) \\'))
        Punkte += 7

    return aufgabe, loesung, Punkte


aufgaben = [gerade(1, [a, b]),
            lagebeziehung(2, [a,b])]
Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'HAK 05 - Schnittwinkel von Geraden berechnen'
Teil = 'Gr. A'
# der Teil in dem die PDF-Datei erzeugt wird
def Hausaufgabenkontrolle():
    geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
    Aufgabe = Document(geometry_options=geometry_options)
    # erste Seite
    table1 = Tabular('c|c|c|c|c|c|', row_height=1.2)
    table1.add_hline(2, 6)
    table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:',
                   'Datum:')
    table1.add_row(SmallText('mit gymnasialer Oberstufe'), Klasse, Fach, Kurs, Lehrer, Datum)
    table1.add_hline(2, 6)
    Aufgabe.append(table1)
    Aufgabe.append(' \n\n')
    Aufgabe.append(LargeText(bold(f'\n {Art} {Titel} \n\n')))
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

    Aufgabe.append('\n\n')
    Aufgabe.append(
        MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

    Aufgabe.append(NewPage())
    Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

    Aufgabe.generate_pdf(f'Ma {Klasse} - {Art} {Titel} {Teil}', clean_tex=true)

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


    Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Titel} {Teil} - Lsg', clean_tex=true)

# Druck der Seiten
Hausaufgabenkontrolle()
Erwartungshorizont()