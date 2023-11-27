import random
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
            loesung_2 = r' \mathrm{Der~Punkt~liegt~nicht~auf~der~Geraden.} '

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
    v = [vx, vy, vz] = [v_teiler, v_teiler * zzahl(1,6)/2, v_teiler * zzahl(1,6)/2] # Vektor v ist der Richtungsvektor von Geraden g_1
    # Vektor u steht orthogonal auf v
    ux, uy = zzahl(1, 3), zzahl(1,3) # x und y Koordinate von u kann frei gewählt werden
    u = [ux, uy, uz] =  [ux, uy, - 1 * (vx*ux + vy * uy)/vz] 

    auswahl = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
    auswahl = 'windschief'
    if auswahl == 'identisch':
        punkt_c = [cx,cy,cz] = np.array(punkt_a) + zzahl(1,30)/5*np.array(v) # Punkt C liegt auf g_2
        w = [wx, wy, wz] = zzahl(1,30)/10 * np.array(v) # Vektor w ist der Richtungsvektor von g_2
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(vx/wx,3)) + r' \\'
                     'r~=~' + latex(N(vy/wy,3)) + r' \\'
                     'r~=~' + latex(N(vz/wz,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~parallel} \quad (3P) \\\\'
                     r' \mathrm{Überprüfen~ob~Stützvektor~von~g_1~auf~g_1~liegt.} \hspace{15em} \\'
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
                     r' \mathrm{Die~Geraden~g_1~und~g_2~sind~identisch.} \quad (4P) \\')
        Punkte += 7
    elif auswahl == 'parallel':
        punkt_c =  [cx,cy,cz] = np.array(punkt_a) + zzahl(1,30)/5*np.array(u) # Punkt C liegt auf g_2
        w = [wx, wy, wz] = zzahl(1,30)/10* np.array(v) # Vektor w ist der Richtungsvektor von g_2
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(vx/wx,3)) + r' \\'
                     'r~=~' + latex(N(vy/wy,3)) + r' \\'
                     'r~=~' + latex(N(vz/wz,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~parallel} \quad (3P) \\\\'
                     r' \mathrm{Überprüfen~ob~Stützvektor~von~g_1~auf~g_1~liegt.} \hspace{15em} \\'
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
                     r' \mathrm{Die~Geraden~g_1~und~g_2~sind~echt~parallel.} \quad (4P) \\')
        Punkte += 7
    elif auswahl == 'windschief':
        punkt_c =  [cx,cy,cz] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(u) # Punkte C und D liegen auf g_2
        punkt_d =  [dx,dy,dz] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(u)
        w = [wx, wy, wz] = np.array(punkt_d) - np.array(punkt_c) # Vektor w ist der Richtungsvektor von g_2
        lsg_r = latex(N((wx*(ay-cy)-wy*(ax-cx))/(vx*wy-vy*wx),3))
        lsg_s = latex(N((ax-cx)/wx + (vx/wx)*(wx*(ay-cy)-wy*(ax-cx))/(vy*wy-vy*wx),3))
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
                             + latex(N((wx*(ay-cy)+wx*(ax-cx))/wx,3)) + '~=~' + latex(N((vx*wy-vy*wx)/wx,3))
                             + r' \cdot r \quad \vert \div ' + vorz_str_minus(N((vx*wy-vy*wx)/wx,3))
                             + r' \quad \to \quad r~=~' + lsg_r + r' \quad \mathrm{und} \quad s ~=~'
                             + lsg_s + r' \quad (3P) \\')
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(vx/wx,3)) + r' \\'
                     'r~=~' + latex(N(vy/wy,3)) + r' \\'
                     'r~=~' + latex(N(vz/wz,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~nicht~parallel} \quad (3P) \\\\'
                     r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g_1~=~g_2} \hspace{5em} \\'
                     r' \begin{pmatrix} ' + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
                     r' \end{pmatrix} ~+~ s \cdot \begin{pmatrix} '
                     + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix}'
                     'I: ~~' + latex(ax) + vorz_str(vx) + r' \cdot r' + r' \\'
                     'II: ~' + latex(ay) + vorz_str(vy) + r' \cdot r' + r' \\'
                     'III: ~' + latex(az) + vorz_str(vz) + r' \cdot r' + r' \\'
                     r' \end{matrix} ~=~ \begin{matrix} '
                     + latex(cx) + vorz_str(wx) + r' \cdot s' + r' \\'
                     + latex(cy) + vorz_str(wy) + r' \cdot s' + r' \\'
                     + latex(cz) + vorz_str(wz) + r' \cdot s' + r' \\'
                     r' \end{matrix} \\\\'  + loesung_2 + loesung_3)
        Punkte += 12
    else:
        punkt_c =  [cx,cy,cz] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(v) # Punkte C und D liegen auf g_2
        punkt_d = [dx,dy,dz] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(u)
        w = [wx, wy, wz] = np.array(punkt_d) - np.array(punkt_c) # Vektor w ist der Richtungsvektor von g_2

        Punkte += 12
    # print(v), print(w), print(punkt_c)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               r'Gegeben sind die beiden Geraden mit folgenden Gleichungen:',
               r'g_1: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + latex(ax) + r' \\' + latex(ay) + r' \\' + latex(az) + r' \\'
               r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + latex(vx) + r' \\' + latex(vy) + r' \\' + latex(vz) + r' \\'
               r' \end{pmatrix} \quad \mathrm{und} \quad g_2: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + latex(cx) + r' \\' + latex(cy) + r' \\' + latex(cz) + r' \\'
               r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + latex(wx) + r' \\' + latex(wy) + r' \\' + latex(wz) + r' \\'
               r' \end{pmatrix}\\']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(teilaufg[i]) + ') Überprüfen Sie die Lagebeziehung der Geraden. \n\n')
        loesung.append(str(teilaufg[i]) + ') \quad' + loesung_1)
        i += 1

    return aufgabe, loesung, Punkte


aufgaben = [gerade(1, [a, b]),
            lagebeziehung(2, [a])]
Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'HAK 05 - mit Geraden rechnen'
Teil = 'Gr. C'
# der Teil in dem die PDF-Datei erzeugt wird
def Hausaufgabenkontrolle():
    geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
    Aufgabe = Document(geometry_options=geometry_options)
    # erste Seite
    table1 = Tabular('c|c|c|c|c|c|', row_height=1.2)
    table1.add_hline(2, 6)
    table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:')
    table1.add_row(SmallText('mit gymnasialer Oberstufe'), Klasse, Fach, Kurs, Lehrer, Datum)
    table1.add_hline(2, 6)
    Aufgabe.append(table1)
    Aufgabe.append(' \n\n')

    Aufgabe.append(LargeText(bold(f'\n {Art} \n\n')))
    for aufgabe in aufgaben:
        for elements in aufgabe[0]:
            if '~' in elements:
                with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            else:
                Aufgabe.append(elements)

    Aufgabe.append('\n\n')
    Aufgabe.append(MediumText(bold(f'Du hast .......... von {Punkte} möglichen Punkten erhalten. \n\n')))

    Aufgabe.append(NewPage())

    Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
    Aufgabe.append(' \n\n')

#     aufgabe = aufgaben[0]
#     elemente = aufgabe[0]
#     punkte = elemente[1]
#     Aufgabe.append(punkte)

#     with Aufgabe.create(Figure(position='h!')) as koordinasystem:
#         koordinasystem.add_image(r'3dim_Koordinatensystem.png', width='400px')

    Aufgabe.generate_pdf(f'{Art} {Teil}', clean_tex=true)

# Erwartungshorizont
def Erwartungshorizont():
    geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
    Loesung = Document(geometry_options=geometry_options)
    Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

    for loesung in aufgaben:
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            else:
                Loesung.append(elements)

    Loesung.append('\n\n')
    Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

#     Loesung.append(NewPage())
#     with Loesung.create(Figure(position='h!')) as koordinasystem:
#         koordinasystem.add_image(r'3dim_Koordinatensystem.png', width='400px')

    Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
# Druck der Seiten
Hausaufgabenkontrolle()
Erwartungshorizont()