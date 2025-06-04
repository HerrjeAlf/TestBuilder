import numpy as np
import string
import random, math
from math import degrees
from sympy import *
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)

from scipy.stats import norm, binom
from skripte.funktionen import *
from skripte.plotten import *
from sympy.stats import Binomial, P

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
# b = list(range(1,4))
# print(b)

def geraden_lagebeziehung(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], lagebeziehung=[None, 'identisch', 'parallel', 'windschief', 'schneiden'][0], gerade_k=[False,True][0], i=0, BE=[]):
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
    punkt_a = [ax, ay, az] = vektor.punkt(3) # Punkt A liegt auf Gerade g_1
    # Vektor v ist der Richtungsvektor von Geraden g_1
    v = [vx, vy, vz] = vektor.kuerzen([zzahl(1, 6) / 2 * v_teiler, zzahl(1, 6) / 2 * v_teiler, v_teiler])
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    uz = (vx*ux + vy * uy)/ (-1 * vz)
    u = vektor.kuerzen([ux, uy, uz])

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    if 'a' in teilaufg:
        # lagebeziehungen zweier Geraden und die dafür nötigen Eigenschaften erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 8

        aufgabe.append(beschriftung(teilaufg,i) + 'Erläutern Sie die möglichen Lagebeziehungen zweier Geraden und '
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
        liste_punkte.append(punkte)
        i += 1

    if 'b' in teilaufg:
        # mathematisches Vorgehen zur Bestimmung der Lagebeziehung zweier Geraden erläutern
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        punkte = 6
        aufgabe.append(beschriftung(teilaufg,i) + 'Erläutern Sie, wie man die Lagebeziehung zweier '
                                          'Geraden mathematisch überprüfen kann. \n\n')
        # Tabelle mit dem Text
        table2 = Tabular('p{0.2cm} p{0.2cm} p{12cm} p{2cm}')
        table2.add_row(beschriftung(teilaufg, i),
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
        liste_punkte.append(punkte)
        i += 1

    if 'c' in teilaufg:
        # Lagebeziehung zweier gegebener Geraden bestimmen
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if lagebeziehung == 'identisch':
            punkte_aufg = 7
            liste_punkte.append(punkte_aufg)
            punkt_c = [cx,cy,cz] = vektor.ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(v)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor.kuerzen(zzahl(1,30)/10 * np.array(v)) # Vektor w ist der Richtungsvektor von h

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
            punkt_c = [cx,cy,cz] = vektor.ganzzahl((punkt_a) + zzahl(1,30)/5*np.array(u)) # Punkt C liegt auf h
            w = [wx, wy, wz] = vektor.kuerzen(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
            while (cx-ax)/vx == (cy-ay)/vy == (cz-az)/vz:
                punkt_c = [cx, cy, cz] = vektor.ganzzahl((punkt_a) + zzahl(1, 30) / 5 * np.array(u))  # Punkt C liegt auf h
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
            [dx, dy, dz] = vektor.ganzzahl(punkt_a + fakt_r * np.array(v))
            punkt_d = [dx, dy, dz + zzahl(1,3)]
            fakt_s = zzahl(1, 7) / 2
            punkt_c = [cx,cy,cz] = vektor.ganzzahl(punkt_d + fakt_s * np.array(u))
            w = [wx, wy, wz]= vektor.kuerzen(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            # while (vx * wy - vy * wx) == 0 or (vx * wy - vy * wx) == 0:
            #     fakt_r = zzahl(1, 7) / 2
            #     [dx, dy, dz] = vektor.ganzzahl(punkt_a + fakt_r * np.array(v))
            #     punkt_d = [dx, dy, dz + zzahl(1, 3)]
            #     fakt_s = zzahl(1, 7) / 2
            #     punkt_c = [cx, cy, cz] = vektor.ganzzahl(punkt_d + fakt_s * np.array(u))
            #     w = [wx, wy, wz] = vektor.kuerzen(punkt_d - punkt_c)  # Vektor w ist der Richtungsvektor von h
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
            punkt_d = [dx,dy,dz] = vektor.ganzzahl(punkt_a + fakt_r * np.array(v)) # Punkte C und D liegen auf h
            punkt_c = [cx,cy,cz] = vektor.ganzzahl(punkt_a + fakt_s * np.array(u))
            [wx, wy, wz] = w = vektor.kuerzen(punkt_d - punkt_c) # Vektor w ist der Richtungsvektor von h
            while (vx * wy - vy * wx) == 0 or (vx * wy - vy * wx) == 0:
                fakt_r = zzahl(1, 7) / 2
                fakt_s = zzahl(1, 7) / 2
                punkt_d = [dx, dy, dz] = vektor.ganzzahl(punkt_a + fakt_r * np.array(v))  # Punkte C und D liegen auf h
                punkt_c = [cx, cy, cz] = vektor.ganzzahl(punkt_a + fakt_s * np.array(u))
                [wx, wy, wz] = w = vektor.kuerzen(punkt_d - punkt_c)  # Vektor w ist der Richtungsvektor von h
            lsgs = (dx-cx)/wx
            lsgr = fakt_r
            # lsgr = -1 * (ax * wy - ay * wx - cx * wy + cy * wx) / (vx * wy - vy * wx)
            # lsgs_alt = (-1*(ax*vy)+(ay*vx)+(cx*vy)-(cy*vx))/(vx*wy-vy*wx)
            # print('vektor d-c: ' + str(np.array(punkt_d-punkt_c)))
            # print('Vektor w ist: ' + str(w))
            # print('Punkt D: ' + str(punkt_d))
            # print('faktor r ist:' + str(fakt_r) + ' und r ist:' + str(lsgr))
            # print('faktor p ist:' + str(fakt_p) + ' und s ist:' + str(lsgs_alt))
            schnittpunkt_s = [sx, sy, sz] = (vektor.ganzzahl(punkt_c + lsgs*w))

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
        aufgabe.append(beschriftung(teilaufg,i) + 'Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(beschriftung(teilaufg,i, True) + r' \mathit{Die~Auswahl~war~'
                       + lagebeziehung + r'} \hspace{25em} \\' + loesung_1)
        i += 1

    if 'd' in teilaufg and lagebeziehung in ['parallel', 'windschief']:
        # Bestimmung des Abstandes zweier paralleler bzw. windschiefer Geraden
        liste_bez.append(f'{str(nr)}.{str(liste_teilaufg[i])})')
        if lagebeziehung == 'parallel':
            if 'c' not in teilaufg:
                punkt_c = [cx,cy,cz] = vektor.ganzzahl(punkt_a * zzahl(1,7)/2 + vektor.kuerzen(u)) # Punkt C liegt auf h
                w = [wx, wy, wz] = vektor.ganzzahl(zzahl(1,30)/10* np.array(v)) # Vektor w ist der Richtungsvektor von h
                while (cx-ax)/vx == (cy-ay)/vy == (cz-az)/vz:
                    punkt_c = [cx, cy, cz] = vektor.ganzzahl(punkt_a * zzahl(1,7)/2 + vektor.kuerzen(u))  # Punkt C liegt auf h
            fakt_r = Rational(vektor.skalarprodukt(punkt_c - punkt_a, v), vektor.skalarprodukt(v, v))
            erg = N(sqrt((cx - ax - fakt_r * vx) ** 2 + (cy - ay - fakt_r * vy) ** 2 + (cz - az - fakt_r * vz) ** 2), 3)
            erg_cross = [crx, cry, crz] = vektor.ganzzahl(np.cross(punkt_c - punkt_a, v))
            erg_alt_disk = Rational(crx ** 2 + cry ** 2 + crz ** 2, vx ** 2 + vy ** 2 + vz ** 2)
            erg_alt = N(sqrt(erg_alt_disk), 3)
        elif lagebeziehung == 'windschief':
            if 'c' not in teilaufg:
                fakt_r = zzahl(1, 7) / 2
                [dx, dy, dz] = vektor.ganzzahl(punkt_a + fakt_r * np.array(v))
                punkt_d = [dx, dy, dz + zzahl(1, 3)]
                fakt_s = zzahl(1, 7) / 2
                punkt_c = [cx, cy, cz] = vektor.ganzzahl(punkt_d + fakt_s * np.array(u))
                w = [wx, wy, wz] = vektor.kuerzen(punkt_d - punkt_c)
            vec_n, fakt_n = [nx, ny, nz], fakt_n = vektor.kuerzen(np.cross(v,w), qout=True)
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
        aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Abstand der Geraden g und h. \n\n')


        if lagebeziehung == 'parallel':
            punkte = 7
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' \mathrm{Hilfsebene~aufstellen: } \hspace{25em} \\'
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
                           + gzahl(vektor.skalarprodukt(punkt_a,v)) + vorz_v_innen(vektor.skalarprodukt(v,v),'r')
                           + r' \quad \vert ' + vorz_str(-1*vektor.skalarprodukt(punkt_a,v)) + r' \quad \vert \div '
                           + gzahl_klammer(vektor.skalarprodukt(v,v)) + r' \quad (1BE) \\\\' + r' r~=~ ' + gzahl(fakt_r)
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
                           + gzahl(crz) + r' \\' + r' \end{pmatrix} \right| }{ \sqrt{'
                           + summe.exponenten([vx,vy,vz],2) + r'}} ~=~ \frac{ \sqrt{ '
                           + summe.exponenten([crx, cry, crz],2) + r' }}{ \sqrt{ '
                           + gzahl(vx**2 + vy**2 + vz**2) + r'}} ~=~' + gzahl(erg_alt) + r' \quad (3BE)')
        elif lagebeziehung == 'windschief':
            punkte = 7
            loesung.append(beschriftung(teilaufg,i, True)
                           + r' \mathrm{Berechnung~mithilfe~der~hessischen~Normalform'
                           + r'~der~Hilfsebene~H~deren~Normalenvektor}, \\'
                           + r' \mathrm{~das~Kreuzprodukt~der~Richtungsvektoren~von~g~und~h~ist:} \\'
                           + r' \overrightarrow{n} ~=~ \overrightarrow{v} \times \overrightarrow{u} ~=~'
                           + r' \begin{pmatrix} ' + gzahl(vx) + r' \\' + gzahl(vy) + r' \\' + gzahl(vz)
                           + r' \\' + r' \end{pmatrix} \times \begin{pmatrix} ' + gzahl(wx) + r' \\' + gzahl(wy)
                           + r' \\' + gzahl(wz) + r' \\' + r' \end{pmatrix} ~=~ ' + fakt_n_str
                           + r' \begin{pmatrix} ' + gzahl(nx) + r' \\' + gzahl(ny) + r' \\' + gzahl(nz) + r' \\'
                           + r' \end{pmatrix} \quad \to \quad \left| \overrightarrow{n} \right| ~=~ \sqrt{'
                           + summe.exponenten([nx,ny,nz],2)+ r'} ~=~ \sqrt{' + gzahl(nx**2+ny**2+nz**2)
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
        punkt_f = [fx,fy,fz] = vektor.ganzzahl(np.array(punkt_a) + fakt_r * np.array(v)) # Punkte C und D liegen auf h
        punkt_e = [ex,ey,ez] = vektor.ganzzahl(np.array(punkt_a) + fakt_s * np.array(u))
        [px, py, pz] = p = vektor.kuerzen(np.array(punkt_f) - np.array(punkt_e)) # Vektor w ist der Richtungsvektor von h


        if 'c' in teilaufg and lagebeziehung == 'schneiden' and gerade_k == False:
            [ex, ey, ez] = [cx,cy,cz]
            [px, py, pz] = [wx, wy, wz]
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Schnittwinkel der Geraden g und h. \n\n')
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
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')

        else:
            aufgabe.append('Gegeben ist eine weitere Gerade k, die g schneidet, mit der folgenden Gleichung.')
            aufgabe.append(r'k: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
                           + gzahl(ex) + r' \\' + gzahl(ey) + r' \\' + gzahl(ez) + r' \\'
                           r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                           + gzahl(px) + r' \\' + gzahl(py) + r' \\' + gzahl(pz) + r' \\'
                           r' \end{pmatrix} ')
            aufgabe.append(beschriftung(teilaufg,i) + 'Berechnen Sie den Schnittwinkel der Geraden g und k. \n\n')

        sp_vp = abs(vektor.skalarprodukt([px, py, pz],[vx, vy, vz]))
        l_v = sqrt(vx ** 2 + vy ** 2 + vz ** 2)
        l_p = sqrt(px ** 2 + py ** 2 + pz ** 2)
        erg = N(acos(sp_vp / (l_p * l_v)) * 180 / pi, 3)
        if erg >= 90:
            text = '~=~ 180 - ' + gzahl(erg) + '~=~' + gzahl(180-erg)
            punkte_aufg += 1
        else:
            text = ''

        loesung.append(beschriftung(teilaufg,i, True) + r' cos( \gamma ) = \frac{ \vert \overrightarrow{v}'
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
                       + r' \gamma ~=~ cos^{-1} \left( \frac{' + gzahl(N(sp_vp,3)) + '}{'
                       + gzahl(N(l_v,3)) + r' \cdot ' + gzahl(N(l_p,3))
                       + r'} \right) ~=~' + gzahl(erg) + text
                       + r' \quad (2BE) \\ \mathrm{insgesamt~' + str(punkte_aufg) + r'~BE} \\')
        liste_punkte.append(punkte_aufg)
        i += 1

    if BE != []:
        if len(BE) != len(teilaufg):
            print(f'Die Anzahl der gegebenen BE ({len(BE)}) stimmt nicht mit der Anzahl der Teilaufgaben '
                  f'({len(teilaufg)}) überein. Es wird die ursprüngliche Punkteverteilung übernommen.')
        else:
            liste_punkte = BE


    print('liste Punkte: ' + str(liste_punkte))

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
