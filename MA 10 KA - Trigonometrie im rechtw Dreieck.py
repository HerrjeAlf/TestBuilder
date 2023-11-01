import pylatex, math, random, sympy, numpy, matplotlib
from random import randrange, randint, choice
from sympy import *
from numpy.linalg import solve as slv
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from Dreiecke_konstruieren import dreieck_zeichen

# Definition der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()

def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k

def nzahl(p, q):
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

def Graph(a, b, xwert, f, n, name):
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    plt.annotate(n, xy=(xwert, f.subs(x,xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points', fontsize=12)
    plt.grid(True)
    plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
    plt.axis([-6, 6, -6, 6])
    plt.plot(a, b, linewidth=2)
    return plt.savefig(name, dpi = 200)


# Berechnung für die Aufgaben
def kongruente_Dreiecke(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1,5)
    m = n + random.randint(1,5)
    a_d = (m**2 - n**2)/10
    b_d = 2*m*n/10
    c_d = (m**2 + n**2)/10
    gamma = 90
    beta = int(math.degrees(math.asin(b_d/c_d)))
    alpha = gamma - beta

    auswahl = random.choice([['sss', 'a~=~' + str(a_d) + 'cm', 'b~=~' + str(b_d) + 'cm', 'c~=~' + str(c_d) + 'cm'],
                             ['sws', 'a~=~' + str(a_d) + 'cm', 'b~=~' + str(b_d) + 'cm', r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['sws', 'b~=~' + str(b_d) + 'cm', 'c~=~' + str(c_d) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}'],
                             ['sws', 'c~=~' + str(c_d) + 'cm', 'a~=~' + str(a_d) + 'cm', r' \beta ~=~' + str(beta) + r' ^{  \circ}'],
                             ['wsw', 'a~=~' + str(a_d) + 'cm', r' \beta ~=~' + str(beta) + r' ^{  \circ}', r' \gamma ~=~' + str(gamma) + r' ^{  \circ}'],
                             ['wsw', 'b~=~' + str(b_d) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}', r' \gamma ~=~ ' + str(gamma) + r' ^{  \circ}'],
                             ['wsw', 'c~=~' + str(c_d) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}', r' \beta ~=~ ' + str(beta) + r' ^{  \circ}'],
                             ['sww', 'b~=~' + str(b_d) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}', r' \beta ~=~' + str(beta) + r' ^{  \circ}'],
                             ['sww', 'c~=~' + str(c_d) + 'cm', r' \beta ~=~' + str(beta) + r' ^{  \circ}', r' \gamma ~=~' + str(gamma)+ r' ^{  \circ}'],
                             ['sww', 'a~=~' + str(a_d) + 'cm', r' \alpha ~=~' + str(alpha) + r' ^{  \circ}', r' \gamma ~=~' + str(gamma)+ r' ^{  \circ}'],
                             ['Ssw', 'b~=~' + str(b_d) + 'cm', ' c ~=~' + str(c_d) + 'cm', r' \gamma ~=~' + str(gamma)+ r' ^{  \circ}'],
                             ['Ssw', 'a~=~' + str(a_d) + 'cm', ' c ~=~' + str(c_d) + 'cm', r' \gamma ~=~' + str(gamma)+ r' ^{  \circ}']])

    # print('a = ' + str(a))
    # print('a = ' + str(a))
    # print('b = ' + str(b))
    # print('c = ' + str(c))
    # print('gamma = ' + str(gamma))
    # print('beta = ' + str(beta))
    # print('alpha = ' + str(alpha))
    print(auswahl)

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n', 'Von einem kongruenten Dreieck sind folgende Daten gegeben:']
    aufgabe.append(str(auswahl[1]) + ',~' + str(auswahl[2]) + r'~ \mathrm{und} ~' + str(auswahl[3]) + r'.')
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(teilaufg[i]) + ') Nenne den Kongruenzsatz, nach dem das Dreieck kongruent ist. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad ' + str(auswahl[0]) + r' \quad (1P) ~')
        Punkte += 1
        i += 1
    if b in teilaufg:
        aufgabe.append(str(teilaufg[i]) + ') Konstruiere das Dreieck mithilfe der gegebenen Daten. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad \mathrm{Planskizze} ~(2P), \quad ' + str(auswahl[1]) + '~(1P),~' + str(auswahl[2]) + '~(1P),~' +
                                                str(auswahl[3]) + r'~(1P),~ \mathrm{restl.~Seite(n)~und~Beschrift.} '
                                                                  r' ~(2P)')
        Punkte += 7
        i += 1
    return aufgabe, loesung, Punkte
def rechtwinkliges_dreieck(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1,5)
    m = n + random.randint(1,5)
    s_1 = (m**2 - n**2)/10
    s_2 = 2*m*n/10
    s_3 = (m**2 + n**2)/10
    print(s_1)
    print(s_2)
    print(s_3)
    w_3 = 90
    w_2 = int(math.degrees(math.asin(s_2 / s_3)))
    w_1 = w_3 - w_2

    auswahl = random.choice([['a', 'b', 'c', r' \alpha ', r' \beta ', r' \gamma '],
                             ['a', 'c', 'b', r' \alpha ', r' \gamma ', r' \beta '],
                             ['b', 'a', 'c', r' \beta ', r' \alpha ', r' \gamma '],
                             ['b', 'c', 'a', r' \beta ', r' \gamma ', r' \alpha '],
                             ['c', 'a', 'b', r' \gamma ', r' \alpha ', r' \beta '],
                             ['c', 'b', 'a', r' \gamma ', r' \beta ', r' \alpha ']])
    print(auswahl)
    if random.random() < 0.33:
        aufgabe_1 = (str(auswahl[0]) + '~=~' + str(s_1) + r'cm,~' + str(auswahl[1]) + '~=~' + str(s_2) + r'cm, ~ \mathrm{und} ~'
                    + str(auswahl[5]) + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + str(auswahl[2])
                     + r'~=~ \sqrt{ (' + str(s_1) + r'cm)^2 ~+~ (' + str(s_2) + r'cm)^2 } ~=~'
                     + str(s_3) + r'cm \quad (3P) \\' + r' \mathrm{Planskizze} \quad (2P)')
    elif random.random() < 0.66:
        aufgabe_1 = (str(auswahl[1]) + '~=~' + str(s_2) + r'cm,~' + str(auswahl[2]) + '~=~' + str(s_3) + r'cm, ~ \mathrm{und} ~'
                    + str(auswahl[5]) + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert -' + str(auswahl[1]) + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + str(auswahl[0])
                     + r'~=~ \sqrt{ (' + str(s_3) + r'cm)^2 ~-~ (' + str(s_2) + r'cm)^2 } ~=~' + str(s_1)
                     + r'cm \quad (3P) \\' + r' \mathrm{Planskizze} \quad (2P)')
    else:
        aufgabe_1 = (str(auswahl[0]) + '~=~' + str(s_1) + r'cm,~' + str(auswahl[2]) + '~=~' + str(s_3) + r'cm, ~ \mathrm{und} ~'
                    + str(auswahl[5]) + '~=~' + str(w_3) + r' ^{  \circ} .')
        loesung_1 = (str(auswahl[2]) + '^2 ~=~' + str(auswahl[0]) + '^2 ~+~' + str(auswahl[1])
                     + r'^2 \quad \vert -' + str(auswahl[0]) + r'^2 \quad \vert \sqrt{...} \quad \to \quad ' + str(auswahl[1])
                     + r'~=~ \sqrt{ (' + str(s_3) + r'cm)^2 ~-~ (' + str(s_1) + r'cm)^2 } ~=~' + str(s_2)
                     + r'cm \quad (3P) \\' + r' \mathrm{Planskizze} \quad (2P)')

    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n','Von einem rechtwinkligen Dreieck sind folgende Daten gegeben:']
    aufgabe.append(aufgabe_1)
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        aufgabe.append(str(teilaufg[i]) + ') Berechne die fehlende Seitenlänge im Dreieck ABC. Fertige dazu eine Planskizze an. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad ' + loesung_1)
        Punkte += 5
        i += 1

    return aufgabe, loesung, Punkte

def verhaeltnisgleichgungen(nr, teilaufg):
    i = 0
    Punkte = 0

    n = random.randint(1, 5)
    m = n + random.randint(1, 5)
    l_a = (m ** 2 - n ** 2) / 10
    l_b= 2 * m * n / 10
    l_c = (m ** 2 + n ** 2) / 10
    pkt = [[0,0], [l_c,0], [(l_b**2)/l_c,l_a*l_b/l_c]]
    st = random.choice([['a','b','c'], ['d','e','f'], ['g','k','l'],
                        ['m','n','p'], ['r','s','t'], ['u','v','w'], ['x','y','z']])

    name = 'Aufgabe_' + str(nr)
    grafik = 'Aufgabe_' + str(nr) + '.png'
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr))) + ' \n\n', 'Die folgende Abbildung stellt ein rechtwinkliges Dreieck dar.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

    if a in teilaufg:
        dreieck_zeichen(pkt, st, [r'\alpha',r'\beta',r'90^{ \circ}'], name)
        auswahl_winkel = random.choice(['Alpha', 'Beta'])
        if auswahl_winkel == 'Alpha':
            loesungen = (r' \mathrm{sin \alpha ~=~ \frac{' + st[0] + '}{' + st[2] + '},'
                               r'\quad cos \alpha ~=~ \frac{' + st[1] + '}{' + st[2] + '},'
                               r'\quad tan \alpha ~=~ \frac{' + st[0] + '}{' + st[1] + '}}')
        else:
            loesungen = (r' \mathrm{sin \beta ~=~ \frac{' + st[1] + '}{' + st[2] + '}, '
                               r'\quad cos \beta ~=~ \frac{' + st[0] + '}{' + st[2] + '},'
                               r'\quad tan \beta ~=~ \frac{' + st[1] + '}{' + st[0] + '}}')

        aufgabe.append(str(teilaufg[i]) + f') Gib den Sinus, Kosinus und Tangens von {auswahl_winkel} als Seitenverhältnis an. \n\n')
        loesung.append(str(teilaufg[i]) + r') \quad ' + loesungen + r' \quad (3P) \\')

        i += 1
        Punkte += 3

    return aufgabe, loesung, Punkte, grafik

aufgaben = [kongruente_Dreiecke(1, [a, b]),
            rechtwinkliges_dreieck(2, [a]),
            verhaeltnisgleichgungen(3, [a])]

Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '10'
Lehrer = 'Herr Herrys'
Art = 'HAK 04 - Verhältnisgleichungen im rechtw. Dreieck'
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
            elif 'Abbildung' in elements:
                Aufgabe.append(elements)
                with Aufgabe.create(Figure(position='h!')) as graph:
                    graph.add_image(aufgabe[3], width='200px')
            else:
                Aufgabe.append(elements)

    Aufgabe.append('\n\n')
    Aufgabe.append(MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

    Aufgabe.append(NewPage())
    Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
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
    Loesung.append(NewPage())

    Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
# Druck der Seiten
Hausaufgabenkontrolle()
Erwartungshorizont()