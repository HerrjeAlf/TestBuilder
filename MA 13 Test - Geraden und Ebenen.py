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
        return latex(k)
    else:
        return f'+{latex(k)}'

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

    def zf_vorz(q):
        return random.choice([-1, 1]) * q

    punkt_a = [a_x, a_y, a_z] = punkt_vektor(3)
    punkt_b = [b_x, b_y, b_z] = [a_x + zzahl(1, 3), a_y + zzahl(1, 3), a_z + zzahl(1, 3)]
    v_ab = [v_ab_x, v_ab_y, v_ab_z] =  np.array(punkt_a) + np.array(punkt_b)
    p = random.choice([0,1])
    if p == 0:
        punkt_t = [t_x, t_y, t_z] = np.array(punkt_a) + (zzahl(1,30)/10)*v_ab
    else:
        punkt_t = [t_x, t_y, t_z] = np.array(punkt_b) + (zzahl(1,30)/10)*[v_ab_y,0,-1*v_ab_z]


    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),'Gegeben sind die Punkte '
               'A( ' + str(a_x)  + ' | ' + str(a_y) + ' | ' + str(a_z) + ' ), ' 
               'B( ' + str(b_x)  + ' | ' + str(b_y) + ' | ' + str(b_z) + ' ) und '
               'T( ' + str(t_x)  + ' | ' + str(t_y) + ' | ' + str(t_z) + ' ).  \n\n']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        loesung_1 = (r' \overrightarrow{AB} ~=~'
                     r' \begin{pmatrix} '
                     + str(v_ab[0]) + r' \\' + str(v_ab[1]) + r' \\' + str(v_ab[2]) + r' \\'
                     r' \end{pmatrix} \quad \to \quad '
                     r' g: \overrightarrow{x} \ ~=~'
                     r' \begin{pmatrix} '
                     + str(a_x) + r' \\' + str(a_y) + r' \\' + str(a_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + str(v_ab[0]) + r' \\' + str(v_ab[1]) + r' \\' + str(v_ab[2]) + r' \\'
                     r' \end{pmatrix} \quad (4P) \\')

        aufgabe.append(str(teilaufg[i]) + f') Stellen Sie die Gleichung der Geraden g auf,'
                                          f' welche die Punkte A und B enthält. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)
        i +=1
        Punkte += 4

    if b in teilaufg:
        loesung_1 =  (r' \begin{pmatrix} '
                     + str(t_x) + r' \\' + str(t_y) + r' \\' + str(t_z) + r' \\'
                     r' \end{pmatrix} ~=~ \begin{pmatrix} '
                     + str(a_x) + r' \\' + str(a_y) + r' \\' + str(a_z) + r' \\'
                     r' \end{pmatrix} ~+~r \cdot \begin{pmatrix} '
                     + str(v_ab[0]) + r' \\' + str(v_ab[1]) + r' \\' + str(v_ab[2]) + r' \\'
                     r' \end{pmatrix} \quad (4P) \\')
        aufgabe.append(str(teilaufg[i]) + f') Überprüfen Sie, ob der Punkt T auf g liegt. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)
        i +=1
        Punkte += 8

    return aufgabe, loesung, Punkte

aufgaben = [gerade(1, [a, b])]
Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '13'
Lehrer = 'Herr Herrys'
Art = 'HAK 05 - mit Geraden rechnen'
Teil = 'Gr. A'
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