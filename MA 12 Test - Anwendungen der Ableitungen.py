import string
import numpy as np
import random, math
import matplotlib.pyplot as plt
from numpy.linalg import solve as slv
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure
from pylatex.utils import bold
from sympy import *

# Definition der Funktionen

a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()

def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

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

def erstellen(Teil):
    print(f'\n\033[1;35mHAK {Teil}\033[0m')

    def Graph(a, b, xwert, f, titel, n, name):
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_xlabel('Ost', size=10, labelpad=-24, x=1.03)
        ax.set_ylabel('Höhe', size=10, labelpad=-21, y=1.02, rotation=0)
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(np.linspace(0, 8, 9, endpoint=True))
        plt.yticks(np.linspace(1, 5, 5, endpoint=True))
        plt.axis([-1, 9, 0, 6])
        plt.plot(a, b, linewidth=2)
        plt.suptitle(titel, usetex=True)
        return plt.savefig(name, dpi=200)

    def anwendungen(nr, teilaufg):
        i = 0
        Punkte = 0
        y_wert_s = 0
        while y_wert_s > 5 or y_wert_s < 1:
            x_wert_x1 = nzahl(4, 8) / 2
            x_wert_x2 = x_wert_x1 + nzahl(4, 8) / 2
            x_wert_s = 0.5 * (x_wert_x2 + x_wert_x1)
            faktor = -1 * nzahl(2, 8) / 2
            fkt = expand(faktor* (x - x_wert_x1) * (x - x_wert_x2))
            y_wert_s = fkt.subs(x, x_wert_s)

        fkt_str = (str(faktor) + 'x^2~' + vorz_str(-1 * faktor * (x_wert_x1 + x_wert_x2)) + 'x~'
                   + vorz_str(faktor * x_wert_x1 * x_wert_x2))
        p_fkt = -1 * (x_wert_x1 + x_wert_x2)
        q_fkt = x_wert_x1 * x_wert_x2
        fkt_str_pq = 'x^2~' + vorz_str(p_fkt) + 'x~' + vorz_str(q_fkt)
        fkt_abl = diff(fkt, x, 1)
        fkt_abl_str = str(2 * faktor) + 'x~' + vorz_str(-1 * faktor * (x_wert_x1 + x_wert_x2))
        m_tangente_str = Rational(y_wert_s,(x_wert_s - 1))
        m_tangente = y_wert_s/(x_wert_s - 1)
        fkt_tangente = N(m_tangente,3) * x - N(m_tangente,3)
        #print(fkt_tangente)
        x_wert_schnittpunkt = solve(Eq(fkt, fkt_tangente), x)
        y_wert_schnittpunkt = fkt_tangente.subs(x, x_wert_schnittpunkt[0])
        xwerte = [-1 + n / 5 for n in range(60)]
        ywerte_huegel = [fkt.subs(x, xwerte[i]) for i in range(60)]
        xwerte_gerade = [1, x_wert_schnittpunkt[0]]
        ywerte_gerade = [0, y_wert_schnittpunkt]
        plt.plot(xwerte_gerade, ywerte_gerade)
        Graph(xwerte, ywerte_huegel, x_wert_s, fkt, '$f(x) =' + latex(fkt) + '$', 'Hügel', 'Aufgabe_3')

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
                   'Im Koordinatensystem auf der Rückseite ist die Profilkurve eines Hügels aufgetragen.',
                   r' f(x)~=~' + latex(fkt)]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        if a in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Fußpunkte des Hügels. \n\n')
            loesung.append(str(teilaufg[i]) + r') \quad f(x)~=~0 \quad \to \quad 0~=~' + fkt_str
                           + r' \quad \vert ~ \div ~' + vorz_str_minus(faktor) + r' \\ 0~=~'
                           + fkt_str_pq + r' \quad (2P) \\ x_{^1/_2} ~=~ - ~ \frac{' + vorz_str_minus(N(p_fkt, 4))
                           + r'}{2} \pm' + r' \sqrt{ \Big( \frac{' + str(N(p_fkt, 4)) + r'}{2} \Big) ^2'
                           + vorz_str(N(-1 * q_fkt, 4)) + r'} ~=~' + str(N(-0.5 * p_fkt, 4)) + r' \pm '
                           + vorz_str_minus(N(sqrt((p_fkt * 0.5) ** 2 - q_fkt), 4)) + r' \quad (2P) \\'
                           + r' x_1 ~=~\mathbf{' + str(x_wert_x1) + r'} \quad \mathrm{und} \quad x_2 ~=~\mathbf{'
                           + str(x_wert_x2) + r'} \quad (1P) \quad \mathbf{P_1(' + str(x_wert_x1)
                           + r' \vert 0)} \quad \mathrm{und} \quad \mathbf{P_2(' + str(x_wert_x2)
                           + r' \vert 0)} \quad (1P) \\\\')
            Punkte += 6
            i += 1

        if b in teilaufg:
            m_x1 = fkt_abl.subs(x, x_wert_x1)
            #print('m_x1 = ' + str(m_x1))
            winkel_x1 = math.degrees(N(atan(m_x1),2))
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Steigung und den Steigungswinkel am westlichen Fußpunkt. \n\n')
            loesung.append(str(teilaufg[i]) + r') f^{ \prime } (x) ~=~ ' + fkt_abl_str + r' \quad \to \quad f^{ \prime } ('
                           + str(x_wert_x1) + r') ~=~ \mathbf{' + str(N(m_x1,3)) + r'} \quad (2P) \\'
                           + r' \alpha ~=~ arctan(' + str(N(m_x1,3)) + r') ~=~ \mathbf{' + str(N(winkel_x1,3))
                           + r'^\circ} \quad (2P) \\\\')

            Punkte += 4
            i += 1

        if c in teilaufg:
            fkt_tp = fkt - fkt_tangente
            fkt_tp_str = (str(faktor) + 'x^2~' + vorz_str(N(-1 * faktor * (x_wert_x1 + x_wert_x2) - m_tangente,3)) + 'x~'
                          + vorz_str(N(faktor * x_wert_x1 * x_wert_x2 + m_tangente,3)))
            p_fkt_tp = -1 * (x_wert_x1 + x_wert_x2) - m_tangente/faktor
            q_fkt_tp = x_wert_x1 * x_wert_x2 + m_tangente/faktor
            fkt_tp_pq = ('x^2~' + vorz_str(N(-1 * (x_wert_x1 + x_wert_x2) - m_tangente/faktor,3)) + 'x~'
                          + vorz_str(N(x_wert_x1 * x_wert_x2 + m_tangente/faktor,3)))
            x_werte_tp = solve(fkt_tp,x)
            y_wert_tp = fkt.subs(x, x_werte_tp[0])
            #print(x_werte_tp[0], x_werte_tp[1])
            aufgabe.append(str(teilaufg[i]) + ') Die Seilbahn startet bei B(1|0). Berechne den Treffpunkt mit dem Hügel, wenn die Steigung')
            aufgabe.append(r' \mathrm{m~=~}' + latex(m_tangente_str) + r' \mathrm{~beträgt}. \hspace{38em}')
            loesung.append(str(teilaufg[i]) + r') \quad \mathrm{B~und~m~einsetzen~in~}  t(x)~=~m~x~+~n \to \quad '
                           + r' 0 ~=~' + latex(N(m_tangente,3)) + r' \cdot 1 ~+~n \quad \vert '
                           + vorz_str(N(-1 * m_tangente,3)) + r' \quad (1P) \\ n ~=~' + vorz_str(N(-1 * m_tangente,3))
                           + r' \quad t(x)~=~' + str(N(m_tangente,3)) + r' \cdot x ' + vorz_str(N(-1 * m_tangente,3))
                           + r' \quad (2P) \\' + fkt_str + '~=~' + latex(fkt_tangente) + r'~ \vert -('
                           + latex(fkt_tangente) + r') \quad (1P) \\' + ' 0 ~=~ ' + fkt_tp_str + r'~ \vert \div '
                           + vorz_str_minus(faktor) + r' \quad \to \quad 0~=~'
                           + fkt_tp_pq + r' \quad (1P) \\ x_{^1/_2} ~=~ - ~ \frac{' + vorz_str_minus(N(p_fkt_tp, 3))
                           + r'}{2} \pm' + r' \sqrt{ \Big( \frac{' + str(N(p_fkt_tp, 3)) + r'}{2} \Big) ^2'
                           + vorz_str(N(-1 * q_fkt_tp, 3)) + r'} ~=~' + str(N(-0.5 * p_fkt_tp, 3)) + r' \pm '
                           + vorz_str_minus(N(sqrt((p_fkt_tp * 0.5) ** 2 - q_fkt_tp), 3)) + r' \quad (2P) \\'
                           + r' x_1 ~=~\mathbf{' + str(N(x_werte_tp[0],3)) + r'} \quad \mathrm{und} \quad x_2 ~=~\mathbf{'
                           + str(N(x_werte_tp[1],3)) + r'} \quad (1P) \quad \mathbf{P_1(' + str(N(x_werte_tp[0],3))
                           + r' \vert' + str(N(y_wert_tp,3)) + r')} \quad (1P) \\\\')

            Punkte += 9
            i += 1

        if d in teilaufg:
            m_fkt_x_tp = fkt_abl.subs(x, x_werte_tp[0])
            winkel_alpha = N(math.degrees(atan(m_fkt_x_tp)),3)
            winkel_beta = N(math.degrees(atan(m_tangente)),3)
            loesung_1 = (r' \gamma ~=~ \vert ' + str(winkel_beta) + r'^\circ~-~' + vorz_str_minus(winkel_alpha)
                       + r'^\circ \vert ~=~\mathbf{' + str(abs(winkel_beta-winkel_alpha)) + r'^\circ} \quad (2P) \\')
            if abs(winkel_beta-winkel_alpha) > 90:
                loesung_1 = (r' \gamma ~=~ \vert ' + str(winkel_beta) + r'^\circ~-~' + vorz_str_minus(winkel_alpha)
                           + r'^\circ \vert ~=~' + str(abs(winkel_beta - winkel_alpha)) + r'^\circ \quad \to \quad \gamma ~=~ 180^\circ ~-~'
                           + str(abs(winkel_beta - winkel_alpha)) + r'^\circ~=~\mathbf{' + str(180 - abs(winkel_beta - winkel_alpha))
                           + r'^\circ} \quad (2P) \\')
                Punkte += 1

            print(m_fkt_x_tp)

            aufgabe.append(str(teilaufg[i]) + ') Berechne den Schnittwinkel der Seilbahn mit dem Hügel. \n\n')
            loesung.append(str(teilaufg[i]) + r') f^{ \prime } (x) ~=~ ' + fkt_abl_str + r' \quad \to \quad f^{ \prime } ('
                           + str(N(x_werte_tp[0],3)) + r') ~=~ ' + str(N(m_fkt_x_tp,3))
                           + r' \quad (1P) \quad \to \quad' + r' \alpha ~=~ arctan(' + str(N(m_fkt_x_tp,3))+ ') ~=~'
                           + latex(winkel_alpha) + r'^\circ \quad (2P) \\'
                           + r' t^{ \prime}(x) ~=~' + str(N(m_tangente,3)) + r' \quad \to \quad'
                           r'\beta ~=~ arctan(' + str(N(m_tangente,3))+ ') ~=~' + latex(winkel_beta) + r'^\circ \quad (2P) \\'
                           + loesung_1)

            Punkte += 6
            i += 1

        if e in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Berechne den  Startpunkt der Seilbahn, damit sie am Schnittpunkt die'
                                              ' Steigung des Hügels besitzt. \n\n')
            loesung.append(str(teilaufg[i]) + r') ')

            Punkte += 4
            i += 1

        if f in teilaufg:
            aufgabe.append(str(teilaufg[i]) + ') Berechne die Höhe des Hügels. \n\n')
            loesung.append(str(teilaufg[i]) + r') ')

            Punkte += 4
            i += 1

        return [aufgabe, loesung, Punkte]

    def steigungen(nr, teilaufg):
        i = 0
        Punkte = 0

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        def faktorliste(p, q, n):
            return [zzahl(p, q) for _ in range(n)]

        def exponenten(n):
            menge = set()
            while len(menge) < n:
                menge.add(nzahl(2, 6 + n))
            return menge

        if a in teilaufg:
            a1, a2, a3 = faktorliste(2, 10, 3)
            e1, e2 = (nzahl(2,5)*2)-1, (nzahl(2,5)*2)-1
            funktionen_liste = ([[a1*x**2 + a2*x + a3, str(a1) + 'x^2' + vorz_str(a2) + 'x' + vorz_str(a3), 2*a1*x + a2],
                                 [a1/(x**e1),r' \frac{' + str(a1) + '}{x^{' + str(e1) + '}}',
                                  str(-1 * a1 * e1) + r' \cdot x^{' + str(-1 * e1 - 1) + '}'],
                                 [a1 * x ** (e1 / e2), str(a1) + r' \sqrt[' + str(e1) + ']{x^{' + str(e2) + '}}',
                                  latex(Rational(a1 * e2, e1)) + r' \cdot x^{' + latex(Rational(e2,e1) - 1) + '}']])
            Aufgabe = random.randint(0,1)
            Aufgabe = 1

            funktion_liste = funktionen_liste[Aufgabe]
            fkt, fkt_str, fkt_abl_str = funktion_liste[0], funktion_liste[1], funktion_liste[2]
            fkt_abl = diff(fkt, x)
            stelle = zzahl(3,10)/2
            steigung = int(fkt_abl.subs(x,stelle))
            while steigung == 0:
                stelle = zzahl(3,10)/2
                steigung = int(fkt_abl.subs(x, stelle))
            print('stelle =' + str(stelle))
            print('steigung = ' + str(steigung))
            print('faktor = ' +str(a1))
            print('exponent = ' + str(e1))
            print(steigung/(-1*a1*e1))
            loesung_liste = [r' \quad f ^ { \prime} (x) ~ = ~' + str(fkt_abl_str) + '~ = ~' + str(steigung) + r'~ \vert ~-~'
                             + vorz_str_minus(a2) + r'~ \vert \div ' + vorz_str_minus(2 * a1) + r' \quad \to \quad x~=~\mathbf{'
                             + latex(N((steigung-a2)/(2*a1),3)) + r'} \quad (3P) \\',
                             r' \quad f ^ { \prime} (x) ~ = ~' + str(fkt_abl_str) + '~ = ~' + str(steigung) + r'~ \vert \div'
                             + vorz_str_minus(-1*a1*e1) + r'~ \vert ~(~)^{' + str(Rational(1,-1*e1-1)) + r'} \quad \to \quad x~=~ \big('
                             + latex(Rational(steigung,-1*a1*e1)) + r' \big) ^{' + latex(Rational(1,-1*e1-1)) + r'} ~=~\mathbf{'
                             + latex(N((sqrt((steigung/(-1*a1*e1)),1-e1)),3)) + r'} \quad (3P) \\']
            loesung_1 = loesung_liste[Aufgabe]

            aufgabe.append(str(teilaufg[i]) + r') Berechne die Stelle, an der die Funktion f die Steigung m hat. ')
            aufgabe.append(r' f(x)~=~' + fkt_str + r' \quad \mathrm{und} \quad m~=~' + str(steigung) + r' \hspace{20em} \\')
            loesung.append(str(teilaufg[i]) + r') \quad' + loesung_1)

            Punkte += 3
            i += 1
        return [aufgabe, loesung, Punkte]

    aufgaben = [anwendungen(1, [a,b,c,d,e,f]), steigungen(2,[a])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'HAK 05 - Anwendungen der Ableitung'

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
        Aufgabe.append(LargeText(bold(f'\n {Art} \n\n')))

        for aufgabe in aufgaben:
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                else:
                    Aufgabe.append(elements)

        Aufgabe.append('\n\n')
        Aufgabe.append(
            MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))
        Aufgabe.append(' \n\n')
        with Aufgabe.create(Figure(position='h!')) as graph:
            graph.add_image(r'Aufgabe_3.png', width='400px')
            # falls es nicht funktioniert wieder zu 'C:\Users\aherr\Documents\GitHub\Aufgabe_1.png' wechseln

        Aufgabe.generate_pdf(f'{Art} {Teil}', clean_tex=true)

    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n')))

        for loesung in aufgaben:
            with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                for elements in loesung[1]:
                    agn.append(elements)

        Loesung.append('\n\n')
        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))


        Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
        plt.cla()

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_HAKs = 1
probe = True
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
