import pylatex, math, random, sympy, numpy
from random import randrange, randint, choice
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold

# Defintion der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')

pi = numpy.pi

liste_variable = [a, b, c, d, x, y, z]

def variable():
    k = random.choice(liste_variable)
    return k

def zzahl(p,q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k

def nzahl(p,q):
    k = random.randint(p, q)
    return k

def vorz_str(k):
    if k < 0:
        k = latex(k)
    else:
        k = '+' + latex(k)
    return k

def vorz_str_minus(k):
    if k < 0:
        k = '(' + latex(k) + ')'
    else:
        k = latex(k)
    return k

def Bild_1(a, b, f, n):
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.annotate(n,xy=(-4,f.subs(x, -4)), xycoords='data', xytext=(+5,+5), textcoords='offset points',fontsize=12)
    plt.grid(True)
    plt.xticks(numpy.linspace(-5 , 5, 11, endpoint=True))
    plt.yticks(numpy.linspace(-5 , 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    return plt.plot(a, b, linewidth = 2)

def Bild_2(a, b, f, n, d):
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.annotate(n, xy=(d, f.subs(x, -d)), xycoords='data', xytext=(-2,-2), textcoords='offset points', fontsize=12)
    plt.grid(True)
    plt.xticks(numpy.linspace(-pi,5*pi,13), ['-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π', '9π/2', '5π'])
    plt.yticks(numpy.linspace(-5 , 5, 11, endpoint=True))
    plt.axis([-3/2*pi,11/2*pi, -6, 6])
    return plt.plot(a, b, linewidth = 2)

# Berechnung für die Aufgaben

def sinus_kosinussatz(nr):

    seite_b = nzahl(3,12)
    seite_a = seite_b + nzahl(2,8)
    gamma = nzahl(30,59)
    seite_c = round(math.sqrt(seite_a**2+seite_b**2-2*seite_a*seite_b*cos(math.radians(gamma))),1)
    alpha = round(math.degrees(math.acos(((seite_a)**2 - (seite_b)**2 - (seite_c)**2)/(-2*seite_b*seite_c))),1)
    beta = round(180-gamma-alpha,1)

    liste = [seite_a, alpha, seite_b, beta, seite_c, gamma]
    bezeichnung = ['a', r' \alpha ', 'b', r' \beta ', 'c', r' \gamma ']
    einheit = ['~cm', r' ^{ \circ } ', '~cm', r' ^{ \circ } ', '~cm', r' ^{ \circ } ']
    auswahl_liste = random.choice([[0,1,2],[0,1,3],[0,1,4],[0,1,5],[0,2,5],[1,2,4],[0,3,4],[0,2,4]])

    aufgabe = []
    aufgabe.append(MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')))
    aufgabe.append('Berechne die fehlenden Größen in einem Dreieck, wenn folgendes gegeben ist:')
    aufgabe.append(bezeichnung[auswahl_liste[0]] + '~=~' + str(liste[auswahl_liste[0]]) + einheit[auswahl_liste[0]] + r' \quad \mathrm{und} \quad ' +
                   bezeichnung[auswahl_liste[1]] + '~=~' + str(liste[auswahl_liste[1]]) + einheit[auswahl_liste[1]] + r' \quad \mathrm{und} \quad ' +
                   bezeichnung[auswahl_liste[2]] + '~=~' + str(liste[auswahl_liste[2]]) + einheit[auswahl_liste[2]])

    loesung = []
    loesung.append(r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\')
    if all(elements in auswahl_liste for elements in [0,1]):
        if 2 in auswahl_liste:
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{b}{ \sin ( \beta ) } \quad \vert \cdot \sin ( \beta ) ' +
                           r' ~ \cdot \sin ( \alpha ) \quad \vert \div a \quad \vert \arcsin () \quad (1P) \\' +
                           r' \beta ~=~ \arcsin \Big( \frac{b \cdot \sin ( \alpha )}{a} \Big) ~=~ \arcsin \Big( \frac{' +
                           str(seite_b) + r'cm \cdot \sin (' + str(alpha) + '^{ \circ } )}{' + str(seite_a) +
                           'cm} \Big) ~=~' + str(beta) + r' ^{ \circ } \quad (3P) \\')
            loesung.append(r' \gamma ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(gamma) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r'c~=~ \frac{a \cdot \sin ( \gamma )}{ \sin ( \alpha )} ~=~ \frac{' + str(seite_a) +
                           r'cm \cdot \sin (' + str(gamma) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_c) + r'cm \quad (3P) \\')
        elif 3 in auswahl_liste:
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{b}{ \sin ( \beta ) } \quad \vert \cdot \sin ( \beta )' +
                           r' \quad \to \quad b~=~ \frac{a \cdot \sin ( \beta )}{ \sin ( \alpha )} ~=~ \frac{' +
                           str(seite_a) + r'cm \cdot \sin (' + str(beta) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_b) + r'cm \quad (4P) \\')
            loesung.append(r' \gamma ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(gamma) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r'c~=~ \frac{a \cdot \sin ( \gamma )}{ \sin ( \alpha )} ~=~ \frac{' + str(seite_a) +
                           r'cm \cdot \sin (' + str(gamma) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_c) + r'cm \quad (3P) \\')
        elif 4 in auswahl_liste:
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{c}{ \sin ( \gamma ) } \quad \vert \cdot \sin ( \gamma ) ' +
                           r' ~ \cdot \sin ( \alpha ) \quad \vert \div a \quad \vert \arcsin () \quad (1P) \\' +
                           r' \gamma ~=~ \arcsin \Big( \frac{c \cdot \sin ( \alpha )}{a} \Big) ~=~ \arcsin \Big( \frac{' +
                           str(seite_c) + r'cm \cdot \sin (' + str(alpha) + '^{ \circ } )}{' + str(seite_a) +
                           'cm} \Big) ~=~' + str(gamma) + r' ^{ \circ } \quad (3P) \\')
            loesung.append(r' \beta ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(beta) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r'b~=~ \frac{a \cdot \sin ( \beta )}{ \sin ( \alpha )} ~=~ \frac{' + str(seite_a) +
                           r'cm \cdot \sin (' + str(beta) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_b) + r'cm \quad (3P) \\')
        else:
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{c}{ \sin ( \gamma ) } \quad \vert \cdot \sin ( \gamma )' +
                           r' \quad \to \quad c~=~ \frac{a \cdot \sin ( \gamma )}{ \sin ( \alpha )} ~=~ \frac{' +
                           str(seite_a) + r'cm \cdot \sin (' + str(gamma) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_c) + r'cm \quad (4P) \\')
            loesung.append(r' \beta ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(gamma) + r'^{ \circ }' +
                           '~=~' + str(beta) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r'b~=~ \frac{a \cdot \sin ( \beta )}{ \sin ( \alpha )} ~=~ \frac{' + str(seite_a) +
                           r'cm \cdot \sin (' + str(beta) + r'^{ \circ } )}{ \sin (' + str(alpha) +
                           r'^{ \circ } )} ~=~' + str(seite_b) + r'cm \quad (3P) \\')
    else:
        if all(elements in auswahl_liste for elements in [0,2,5]):
            loesung.append(r' c^2~=~a^2~+~b^2~-~2 \cdot ab~ \cos ( \gamma ) \quad \to \quad c~=~' +
                           r' \sqrt{~a^2~+~b^2~-~2 \cdot ab~ \cos ( \gamma )} \quad (1P) \\' +
                           r' c~=~ \sqrt{~(' + str(seite_a) + 'cm)^2~+~(' + str(seite_b) + r'cm)^2~-~2 \cdot ' + 
                           str(seite_a) + r'cm \cdot ' + str(seite_b) + r'cm ~ \cos (' + str(gamma) +
                           r')^{ \circ }} ~=~ ' + str(seite_c) + r'cm \quad (2P) \\')
            loesung.append(r' a^2~=~b^2~+~c^2~-~2 \cdot bc~ \cos ( \alpha ) \quad \vert -(b^2~+~c^2) \quad \vert \div (~-2bc~) \quad \vert ~ arccos()' +
                           r' \to \quad \alpha ~=~ arccos \Big( \frac{~a^2~-~b^2~-~c^2~}{~-2bc~} \Big) \quad (1P) \\' +
                           r' \alpha ~=~ arccos \Big( \frac{~(' + str(seite_a) + 'cm)^2~-~(' + str(seite_b) + r'cm)^2~-~(' +
                           str(seite_c) + r'cm)^2}{~-2 \cdot ' + str(seite_b) + r'cm \cdot ' + str(seite_c) + r'cm} \Big) ~=~'  +
                           str(alpha) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r' \beta ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(beta) + r'^{ \circ } \quad (2P) \\')

        elif all(elements in auswahl_liste for elements in [1,2,4]):
            loesung.append(r' a^2~=~b^2~+~c^2~-~2 \cdot bc~ \cos ( \alpha ) \quad \to \quad a~=~' +
                           r' \sqrt{~b^2~+~c^2~-~2 \cdot bc~ \cos ( \alpha )} \quad (1P) \\' +
                           r' a~=~ \sqrt{~(' + str(seite_b) + 'cm)^2~+~(' + str(seite_c) + r'cm)^2~-~2 \cdot ' +
                           str(seite_b) + r'cm \cdot ' + str(seite_c) + r'cm ~ \cos (' + str(alpha) +
                           r')^{ \circ }} ~=~ ' + str(seite_a) + r'cm \quad (2P) \\')
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{b}{ \sin ( \beta ) } \quad \vert \cdot \sin ( \beta ) ' +
                           r' ~ \cdot \sin ( \alpha ) \quad \vert \div a \quad \vert \arcsin () \quad (1P) \\' +
                           r' \beta ~=~ \arcsin \Big( \frac{b \cdot \sin ( \alpha )}{a} \Big) ~=~ \arcsin \Big( \frac{' +
                           str(seite_b) + r'cm \cdot \sin (' + str(alpha) + '^{ \circ } )}{' + str(seite_a) +
                           'cm} \Big) ~=~' + str(beta) + r' ^{ \circ } \quad (3P) \\')
            loesung.append(r' \gamma ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(gamma) + r'^{ \circ } \quad (2P) \\')
        elif all(elements in auswahl_liste for elements in [0, 3, 4]):
            loesung.append(r' b^2~=~a^2~+~c^2~-~2 \cdot ac~ \cos ( \beta ) \quad \to \quad b~=~' +
                           r' \sqrt{~a^2~+~c^2~-~2 \cdot ac~ \cos ( \beta )} \quad (1P) \\' +
                           r' b~=~ \sqrt{~(' + str(seite_a) + 'cm)^2~+~(' + str(seite_c) + r'cm)^2~-~2 \cdot ' +
                           str(seite_a) + r'cm \cdot ' + str(seite_c) + r'cm ~ \cos (' + str(beta) +
                           r')^{ \circ }} ~=~ ' + str(seite_b) + r'cm \quad (2P) \\')
            loesung.append(r' a^2~=~b^2~+~c^2~-~2 \cdot bc~ \cos ( \alpha ) \quad \vert -(b^2~+~c^2) \quad \vert \div (~-2bc~) \quad \vert ~ arccos()' +
                           r' \to \quad \alpha ~=~ arccos \Big( \frac{~a^2~-~b^2~-~c^2~}{~-2bc~} \Big) \quad (1P) \\' +
                           r' \alpha ~=~ arccos \Big( \frac{~(' + str(seite_a) + 'cm)^2~-~(' + str(seite_b) + r'cm)^2~-~(' +
                           str(seite_c) + r'cm)^2}{~-2 \cdot ' + str(seite_b) + r'cm \cdot ' + str(seite_c) + r'cm} \Big) ~=~'  +
                           str(alpha) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r' \gamma ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(gamma) + r'^{ \circ } \quad (2P) \\')
        else:
            loesung.append(r' a^2~=~b^2~+~c^2~-~2 \cdot bc~ \cos ( \alpha ) \quad \vert -(b^2~+~c^2) \quad \vert \div (~-2bc~) \quad \vert ~ arccos()' +
                           r' \to \quad \alpha ~=~ arccos \Big( \frac{~a^2~-~b^2~-~c^2~}{~-2bc~} \Big) \quad (1P) \\' +
                           r' \alpha ~=~ arccos \Big( \frac{~(' + str(seite_a) + 'cm)^2~-~(' + str(seite_b) + r'cm)^2~-~(' +
                           str(seite_c) + r'cm)^2}{~-2 \cdot ' + str(seite_b) + r'cm \cdot ' + str(seite_c) + r'cm} \Big) ~=~'  +
                           str(alpha) + r'^{ \circ } \quad (2P) \\')
            loesung.append(r' \frac{a}{ \sin ( \alpha ) } = \frac{b}{ \sin ( \beta ) } \quad \vert \cdot \sin ( \beta ) ' +
                           r' ~ \cdot \sin ( \alpha ) \quad \vert \div a \quad \vert \arcsin () \quad (1P) \\' +
                           r' \beta ~=~ \arcsin \Big( \frac{b \cdot \sin ( \alpha )}{a} \Big) ~=~ \arcsin \Big( \frac{' +
                           str(seite_b) + r'cm \cdot \sin (' + str(alpha) + '^{ \circ } )}{' + str(seite_a) +
                           'cm} \Big) ~=~' + str(beta) + r' ^{ \circ } \quad (3P) \\')
            loesung.append(r' \gamma ~=~ 180^{ \circ } - ' + str(alpha) + r'^{ \circ } -' + str(beta) + r'^{ \circ }' +
                           '~=~' + str(gamma) + r'^{ \circ } \quad (2P) \\')


    print(f'Seite a: {seite_a}')
    print(f'Seite b {seite_b}')
    print(f'Seite c: {seite_c}')
    print(f'Winkel gamma: {gamma}')
    print(f'Winkel alpha: {alpha}')
    print(f'Winkel beta: {beta}')
    print(f'Auswahl: {auswahl_liste}')

    return aufgabe, loesung

def trigonometrische_fkt(nr, teilaufg):
    liste_teilaufg = [a, b, c, d]
    i = 0

    def trigonometrische_fkt():
        faktr = zzahl(2,6)/2
        k_1 = nzahl(1,4)
        periode = k_1*pi
        streckung = 2*pi/periode
        k_2 = random.choice([-1,-1/2,1/2, 1, 3/2, 2, 5/2 ])
        versch_x = k_2*pi
        versch_y = zzahl(1,3)
        fkt = faktr * sin(streckung*(x-versch_x))+versch_y
        fkt_str = latex(faktr) + r' \cdot sin \Big( ~' + latex(Rational(2,k_1)) + '(x' + vorz_str(-1*k_2) + r' \pi ) \Big) ' + vorz_str(versch_y)
        return fkt, fkt_str, faktr, k_1, periode, versch_x, k_2, versch_y

    fkt_1, fkt_str_1, faktr_1, k_1_1, periode_1, versch_x_1, k_2_1, versch_y_1 = trigonometrische_fkt()
    fkt_2, fkt_str_2, faktr_2, k_1_2, periode_2, versch_x_2, k_2_2, versch_y_2 = trigonometrische_fkt()

    P_1 = fkt_1.subs(x,1)
    xwerte = numpy.linspace(versch_x_1,versch_x_1+periode_1, 200)
    ywerte = [fkt_1.subs(x, xwerte[i]) for i in range(200)]
    plot_1 = Bild_2(xwerte, ywerte, P_1, 'f', versch_x_1)

    y_wert_gl = round(1/zzahl(1,10)*faktr_2+versch_y_2,1)
    loesung_goniom_gl = solve(Eq(fkt_2,y_wert_gl))

    print(loesung_goniom_gl)

    aufgabe = []
    aufgabe.append(MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')))

    loesung = []
    loesung.append(r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}')

    if a in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Lies die Parameter a, b, c und d aus dem Graphen ab und notiere die Funktionsgleichung von f. \n\n')
        loesung.append(str(liste_teilaufg[i]) + r') \quad f(x)~=~' + fkt_str_1 + r' \quad (5P)')
        i = i + 1

    if b in teilaufg:
        aufgabe.append(str(liste_teilaufg[i]) + ') Löse die Gleichung.')
        aufgabe.append(fkt_str_2 + r'~=~' + latex(y_wert_gl))
        loesung.append(str(liste_teilaufg[i]) + r') \quad ' + fkt_str_2 + r'~=~' + latex(y_wert_gl) + r' \vert ~' +
                       vorz_str(-1*versch_y_2) + r' \quad \vert ~ \div ' + vorz_str_minus(faktr_2) + r' \quad \vert ~ arcsin() \\' +
                       latex(Rational(2,k_1_2)) + r'\cdot ~(x' + vorz_str(-1*k_2_2) + r' \pi ) ~=~ arcsin (' +
                       latex(round((y_wert_gl-versch_y_2)/faktr_2,1)) + r') \quad \vert \div ' + vorz_str_minus(Rational(2,k_1_2)) +
                       r' \quad \vert ~' + vorz_str(k_2_2) + r' \pi \quad \to \quad x_0~=~' + latex(round(loesung_goniom_gl[0],1)) +
                       r' \quad (2P) \\' + r' x_1 ~=~ x_0 + k \cdot \frac{2 \pi }{b} ~=~' + latex(round(loesung_goniom_gl[0],1)) +
                       r'~+~ k \cdot \frac{2 \pi }{' + latex(Rational(2,k_1_2)) + r'} \quad (1P) \\' +
                       r' x_2 ~=~ \frac{ \pi }{b} - x_0 + k \cdot \frac{2 \pi }{b} ~=~ \frac{ \pi }{' + latex(Rational(2,k_1_2)) +
                       '} ~-~' + latex(round(loesung_goniom_gl[0],1)) + r'+ ~ k \cdot \frac{2 \pi }{' + latex(Rational(2,k_1_2)) +
                       r'} \quad (1P) \\')
        i = i + 1

    print(f'die Funktion lautet: {fkt_str_1}')

    return aufgabe, loesung

Aufgabe_1, Loesung_1 = sinus_kosinussatz(1)
Aufgabe_2, Loesung_2 = trigonometrische_fkt(2, [a,b])

# plt.show()

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '11'
Lehrer = 'Herr Herrys'

Art = 'Test - trigonometrische Funktionen'
Teil = 'Nachschreiber'

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

    for elements in Aufgabe_1:
        if '~' in elements:
            with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                agn.append(elements)
        else:
            Aufgabe.append(elements)

    for elements in Aufgabe_2:
        if '~' in elements:
            with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                agn.append(elements)
        else:
            Aufgabe.append(elements)
    with Aufgabe.create(Figure(position='htbp')) as plot:
        plot.add_plot()

    Aufgabe.append(NewPage())
    Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

    Aufgabe.generate_pdf('Test - trigonometrische Funktionen Nachschreiber', clean_tex=true)


# Erwartungshorizont

def Erwartungshorizont():
    geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
    Loesung = Document(geometry_options=geometry_options)

    Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
        for elements in Loesung_1:
            agn.append(elements)
    for elements in Loesung_2:
        if '~' in elements:
            with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                agn.append(elements)
        else:
            Loesung.append(elements)

    Loesung.generate_pdf('Test - trigonometrische Funktionen Nachschreiber - Lsg', clean_tex=true)


# Druck der Seiten


Hausaufgabenkontrolle()
Erwartungshorizont()
