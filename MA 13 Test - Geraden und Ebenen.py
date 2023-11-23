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

    punkt_a = [a_x, a_y, a_z] = punkt_vektor(3)
    punkt_b = [b_x, b_y, b_z] = [a_x + zzahl(1, 3), a_y + zzahl(1, 3), a_z + zzahl(1, 3)]
    v_ab = [v_ab_x, v_ab_y, v_ab_z] =  np.array(punkt_b) - np.array(punkt_a)
    p = random.choice([0,1])
    if p == 0:
        punkt_t = [t_x, t_y, t_z] = np.array(punkt_a) + zzahl(1,30)/5*v_ab
    else:
        punkt_t = [t_x, t_y, t_z] = np.array(punkt_a) + (zzahl(1,30)/5)*v_ab + [1, 1, 1]

    lsg_x, lsg_y, lsg_z = [(t_x-a_x)/v_ab_x, (t_y-a_y)/v_ab_y, (t_z-a_z)/v_ab_z]

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
               'A( ' + latex(a_x)  + ' | ' + latex(a_y) + ' | ' + latex(a_z) + ' ), ' 
               'B( ' + latex(b_x)  + ' | ' + latex(b_y) + ' | ' + latex(b_z) + ' ) und '
               'T( ' + str(N(t_x,3))  + ' | ' + str(N(t_y,3)) + ' | ' + str(N(t_z,3)) + ' ).  \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        loesung_1 = (r' \overrightarrow{AB} ~=~'
                     r' \begin{pmatrix} '
                     + latex(v_ab[0]) + r' \\' + latex(v_ab[1]) + r' \\' + latex(v_ab[2]) + r' \\'
                     r' \end{pmatrix} \quad \to \quad '
                     r' g: \overrightarrow{x} \ ~=~'
                     r' \begin{pmatrix} '
                     + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v_ab[0]) + r' \\' + latex(v_ab[1]) + r' \\' + latex(v_ab[2]) + r' \\'
                     r' \end{pmatrix} \quad (4P) \\')

        aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                          f' welche die Punkte A und B enthält. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)
        i +=1
        Punkte += 4

    if b in teilaufg:
        if lsg_x == lsg_y == lsg_z:
            loesung_0 = r' \mathrm{Der~Punkt~liegt~auf~der~Geraden.} '
        else:
            loesung_0 = r' \mathrm{Der~Punkt~liegt~nicht~auf~der~Geraden.} '
        loesung_1 =  (r' \begin{pmatrix} '
                     + latex(N(t_x,3)) + r' \\' + latex(N(t_y,3)) + r' \\' + latex(N(t_z,3)) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} \to \begin{matrix} '
                     + latex(N(t_x,3)) + '~=~' + latex(a_x) + vorz_str(v_ab_x) + r' \cdot r' + r' \\'
                     + latex(N(t_y,3)) + '~=~' + latex(a_y) + vorz_str(v_ab_y) + r' \cdot r' + r' \\'
                     + latex(N(t_z,3)) + '~=~' + latex(a_z) + vorz_str(v_ab_z) + r' \cdot r' + r' \\'
                     r' \end{matrix} \quad \to \quad \begin{matrix} '
                     + 'r=' + latex(N(lsg_x,3)) + r' \\' + 'r=' + latex(N(lsg_y,3)) + r' \\'
                     + 'r=' + latex(N(lsg_z,3)) + r' \\'
                     r' \end{matrix} \\'
                     + loesung_0 + r'\quad (4P) \\')
        aufgabe.append(str(teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T auf g liegt. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)
        i +=1
        Punkte += 4

    return aufgabe, loesung, Punkte

def lagebeziehung(nr, teilaufg):
    i = 0
    Punkte = 0
    v_ab_teiler = zzahl(1, 3)
    punkt_a = [a_x, a_y, a_z] = punkt_vektor(3)
    v_ab = [v_ab_x, v_ab_y, v_ab_z] = [v_ab_teiler, v_ab_teiler * zzahl(1,6)/2, v_ab_teiler * zzahl(1,6)/2]
    v_o_ab_x, v_o_ab_y = zzahl(1, 3), zzahl(1,3)
    v_o_ab = [v_o_ab_x, v_o_ab_y, v_o_ab_z] =  [v_o_ab_x, v_o_ab_y, - 1 * (v_ab_x*v_o_ab_x + v_ab_y * v_o_ab_y)/v_ab_z]

    auswahl = random.choice(['identisch', 'parallel', 'windschief', 'schneiden'])
    # auswahl = 'parallel'
    if auswahl == 'identisch':
        punkt_c = [c_x,c_y,c_z] = np.array(punkt_a) + zzahl(1,30)/5*np.array(v_ab)
        v_cd = [v_cd_x, v_cd_y, v_cd_z] = zzahl(1,30)/10 * np.array(v_ab)
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(v_ab_x/v_cd_x,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_y/v_cd_y,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_z/v_cd_z,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~parallel} \quad (3P) \\\\'
                     r' \mathrm{Überprüfen~ob~Stützvektor~von~g_1~auf~g_1~liegt.} \hspace{15em} \\'
                     r' \begin{pmatrix} '
                     + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + latex(c_x) + r' \\' + latex(c_y) + r' \\' + latex(c_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     + latex(a_x) + '~=~' + latex(c_x) + vorz_str(v_cd_x) + r' \cdot r' + r' \\'
                     + latex(a_y) + '~=~' + latex(c_y) + vorz_str(v_cd_y) + r' \cdot r' + r' \\'
                     + latex(a_z) + '~=~' + latex(c_z) + vorz_str(v_cd_z) + r' \cdot r' + r' \\'
                     r' \end{matrix} \quad \to \quad \begin{matrix} '
                     + 'r=' + latex(N((a_x-c_x)/v_cd_x,3)) + r' \\' + 'r=' + latex(N((a_y-c_y)/v_cd_y,3)) + r' \\'
                     + 'r=' + latex(N((a_z-c_z)/v_cd_z,3)) + r' \\ \end{matrix} \\'
                     r' \mathrm{Die~Geraden~g_1~und~g_2~sind~identisch.} \quad (4P) \\')
        Punkte += 7
    elif auswahl == 'parallel':
        punkt_c =  [c_x,c_y,c_z] = np.array(punkt_a) + zzahl(1,30)/5*np.array(v_o_ab)
        v_cd = [v_cd_x, v_cd_y, v_cd_z] = zzahl(1,30)/10* np.array(v_ab)
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(v_ab_x/v_cd_x,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_y/v_cd_y,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_z/v_cd_z,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~parallel} \quad (3P) \\\\'
                     r' \mathrm{Überprüfen~ob~Stützvektor~von~g_1~auf~g_1~liegt.} \hspace{15em} \\'
                     r' \begin{pmatrix} '
                     + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + latex(c_x) + r' \\' + latex(c_y) + r' \\' + latex(c_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     + latex(a_x) + '~=~' + latex(c_x) + vorz_str(v_cd_x) + r' \cdot r' + r' \\'
                     + latex(a_y) + '~=~' + latex(c_y) + vorz_str(v_cd_y) + r' \cdot r' + r' \\'
                     + latex(a_z) + '~=~' + latex(c_z) + vorz_str(v_cd_z) + r' \cdot r' + r' \\'
                     r' \end{matrix} \quad \to \quad \begin{matrix} '
                     + 'r=' + latex(N((a_x-c_x)/v_cd_x,3)) + r' \\' + 'r=' + latex(N((a_y-c_y)/v_cd_y,3)) + r' \\'
                     + 'r=' + latex(N((a_z-c_z)/v_cd_z,3)) + r' \\ \end{matrix} \\'
                     r' \mathrm{Die~Geraden~g_1~und~g_2~sind~echt~parallel.} \quad (4P) \\')
        Punkte += 7
    elif auswahl == 'windschief':
        punkt_c =  [c_x,c_y,c_z] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(v_o_ab)
        punkt_d =  [d_x,d_y,d_z] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(v_o_ab)
        v_cd = [v_cd_x, v_cd_y, v_cd_z] = np.array(punkt_d) - np.array(punkt_c)
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(v_ab_x/v_cd_x,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_y/v_cd_y,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_z/v_cd_z,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~nicht~parallel} \quad (3P) \\\\'
                     r' \mathrm{Schnittpunkt~finden,~indem~man~die~Geraden~gleichsetzt:~g_1~=~g_2} \hspace{5em} \\'
                     r'\begin{pmatrix} ' + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + latex(c_x) + r' \\' + latex(c_y) + r' \\' + latex(c_z) + r' \\'
                     r' \end{pmatrix} ~+~s \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \beginn{matrix} '
                     'I: ~~' + latex(a_x) + vorz_str(v_ab_x) + r'~ \cdot ~r \\'
                     'II: ~' + latex(a_y) + vorz_str(v_ab_y) + r'~ \cdot ~r \\'
                     'III: ~' + latex(a_z) + vorz_str(v_ab_z) + r'~ \cdot ~r \\'
                     r' \end{pmatrix} \quad ~=~ \quad \beginn{matrix} '
                     + latex(c_x) + vorz_str(v_cd_x) + r'~ \cdot ~s \\'
                     + latex(c_y) + vorz_str(v_cd_y) + r'~ \cdot ~s \\'
                     + latex(c_z) + vorz_str(v_cd_z) + r'~ \cdot ~s \\'
                     r' \end{pmatrix} \\\\')
        if v_ab_x != 0 and v_cd_x != 0:
            loesung_2 = (r' \mathrm{I~nach~s~umstellen:} \quad ' + str(a_x) + vorz_str(v_ab_x) + r'~ \cdot ~r ~=~'
                         + latex(c_x) + vorz_str(v_cd_x) + r'~ \cdot ~s \vert ~' + vorz_str(-1*c_x)
                         + r' ~ \vert ~ \div ' + vorz_str_minus(v_cd_x) + r'~ \to ~ s ~=~ '
                         + latex(Rational((a_x-c_x)/v_cd_x)) + r'\quad (2P) \\')
            if v_ab_y != 0 and v_cd_y != 0:
                loesung_3 = ((r' \mathrm{s~in~II~einsetzen:} \quad ' + str(a_y) + vorz_str(v_ab_y) + r'~ \cdot ~r ~=~'
                             + latex(c_y) + vorz_str(v_cd_y) + r'~ \cdot ~ \big( ' + latex(Rational((a_x-c_x)/v_cd_x))
                             + r' \big) ~ \vert ' + vorz_str(-1*a_y) + r'~ \vert ~ \div ' + str(v_ab_y))
                             + r' \quad \to \quad ' +
        Punkte += 12
    else:
        punkt_c =  [c_x,c_y,c_z] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(v_ab)
        punkt_d = [d_x,d_y,d_z] = np.array(punkt_a) + zzahl(1, 30) / 5 * np.array(v_o_ab)
        v_cd = [v_cd_x, v_cd_y, v_cd_z] = np.array(punkt_d) - np.array(punkt_c)
        loesung_1 = (r' \mathrm{Überpüfen~der~Geraden~auf~Parallelität} \hspace{20em} \\'
                     r'\begin{pmatrix}' + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
                     r' \end{pmatrix} ~=~ r \cdot \begin{pmatrix} '
                     + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
                     r' \end{pmatrix} \quad \to \quad \begin{matrix} '
                     'r~=~' + latex(N(v_ab_x/v_cd_x,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_y/v_cd_y,3)) + r' \\'
                     'r~=~' + latex(N(v_ab_z/v_cd_z,3)) + r' \\'
                     r' \end{matrix} \quad \to \quad \mathrm{g_1~und~g_2~sind~nicht~parallel} \quad (3P) \\\\')
        Punkte += 12
    # print(v_ab), print(v_cd), print(punkt_c)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               r'Gegeben sind die beiden Geraden mit folgenden Gleichungen:',
               r'g_1: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + latex(a_x) + r' \\' + latex(a_y) + r' \\' + latex(a_z) + r' \\'
               r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + latex(v_ab_x) + r' \\' + latex(v_ab_y) + r' \\' + latex(v_ab_z) + r' \\'
               r' \end{pmatrix} \quad \mathrm{und} \quad g_2: \overrightarrow{x} \ ~=~ \begin{pmatrix} '
               + latex(c_x) + r' \\' + latex(c_y) + r' \\' + latex(c_z) + r' \\'
               r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
               + latex(v_cd_x) + r' \\' + latex(v_cd_y) + r' \\' + latex(v_cd_z) + r' \\'
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