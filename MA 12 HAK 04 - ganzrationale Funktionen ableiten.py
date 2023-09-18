import string
import numpy
import random
import matplotlib.pyplot as plt
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

    def Graph(a, b, xwert, f, f_str, n, name):
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
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.axis([-6, 6, -6, 6])
        plt.plot(a, b, linewidth=2)
        plt.suptitle(r'Dargestellt ist der Graph von: \ $f(x) =' + f_str + '$', usetex=True)
        return plt.savefig(name, dpi=200)

    def aenderungsrate(nr, teilaufg):
        i = 0
        Punkte = 0

        faktor = zzahl(1, 20) / 10
        s_xwert = zzahl(1, 3)
        s_ywert = zzahl(1, 3)
        abstand = random.choice([[-1, 2], [-2, 1]])

        x_wert_1 = s_xwert + abstand[0]
        x_wert_2 = s_xwert + abstand[1]
        y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
        y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
        werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

        while not all(abs(wert) < 6 for wert in werte):
            s_xwert = zzahl(1, 3)
            s_ywert = zzahl(1, 3)
            abstand = random.choice([[-1, 2], [-2, 1]])

            x_wert_1 = s_xwert + abstand[0]
            x_wert_2 = s_xwert + abstand[1]
            y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
            y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
            werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

        print(f'\033[0;36mIntervall: [X: {x_wert_1} Y: {round(y_wert_1, 2)} | '
              f'X: {x_wert_2} Y: {round(y_wert_2, 2)}]\033[0m')

        fkt = expand(faktor * (x - s_xwert) ** 2 + s_ywert)
        fkt_abl = diff(fkt, x)
        fkt_str = (latex(faktor) + 'x^2' + vorz_str(-2 * faktor * s_xwert)
                   + 'x' + vorz_str((faktor * (s_xwert ** 2)) + s_ywert))
        fkt_abl = diff(fkt, x)
        fkt_abl_x0 = fkt_abl.subs(x, x_wert_2)

        print("f(x)=" + str(fkt))
        print("f'(x)=" + str(fkt_abl))
        print("f'(x_0)=" + str(fkt_abl_x0))

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Funktion:',
                   r'f(x)~=~' + fkt_str]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        xwerte_geraden = [-6, 6]
        if a in teilaufg:
            aufgabe.append(str(teilaufg[i]) + f') Bestimme zeichnerisch die mittlere Änderungsrate im '
                                              f'Interval [ {x_wert_1} | {x_wert_2} ] vom Graphen f. \n\n')

            dy = y_wert_2 - y_wert_1
            dx = x_wert_2 - x_wert_1
            fkt_sekante = dy / dx * (x - x_wert_2) + y_wert_2
            xwerte = [-6 + n / 5 for n in range(60)]
            ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
            Graph(xwerte, ywerte, s_xwert, fkt, fkt_str, 'f', 'Aufgabe_1')

            xwerte_dy = [x_wert_2, x_wert_2]
            ywerte_dy = [y_wert_1, y_wert_2]
            xwerte_dx = [x_wert_1, x_wert_2]
            ywerte_dx = [y_wert_1, y_wert_1]

            steigung_dreieck = N((y_wert_2-y_wert_1)/(x_wert_2-x_wert_1), 2)

            ywerte_sekante = [fkt_sekante.subs(x, -6), fkt_sekante.subs(x, 6)]

            plt.plot(xwerte_dy, ywerte_dy)
            plt.plot(xwerte_dx, ywerte_dx)
            plt.plot(xwerte_geraden, ywerte_sekante)

            loesung.append(str(teilaufg[i])
                           + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~~Steigungsdreieck~(1P),~Steigung~m='
                           + str(steigung_dreieck) + r'~bestimmt~(1P)} \\\\')

            if c not in teilaufg:
                plt.savefig('loesung_Aufgabe_1', dpi=150)

            Punkte += 3
            i += 1

        if b in teilaufg:
            aufgabe.append(str(teilaufg[i]) +
                           f') Überprüfe die mittlere Änderungsrate im Interval [ {x_wert_1} | {x_wert_2} ] '
                           f'durch Rechnung. \n\n')
            loesung.append(
                str(teilaufg[i]) + r') \quad \frac{ \Delta y}{ \Delta x} ~=~ \frac{f(' + str(x_wert_2)
                + ') - f(' + str(x_wert_1) + ')}{' + str(x_wert_2) + str(vorz_str(-1 * x_wert_1)) + r'} ~=~ \frac{'
                + latex(N(y_wert_2, 3)) + vorz_str(-1 * N(y_wert_1, 3)) + '}{' + str(x_wert_2)
                + vorz_str(-1 * x_wert_1) + '} ~=~'
                + latex(N(Rational(y_wert_2 - y_wert_1, x_wert_2 - x_wert_1), 3))
                + r'\quad \to \quad \mathrm{'r'Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (4P) \\\\')
            Punkte += 4
            i += 1

        if c in teilaufg:
            aufgabe.append(str(teilaufg[i])
                           + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')

            if a not in teilaufg:
                xwerte = [-6 + n / 5 for n in range(60)]
                ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
                Graph(xwerte, ywerte, s_xwert, fkt, fkt_str, 'f', 'Aufgabe_1')

            steigung_tangente = fkt_abl.subs(x, x_wert_2)
            fkt_tangente = steigung_tangente * (x - x_wert_2) + y_wert_2

            x_wert_3 = x_wert_2 - 1
            y_wert_3 = fkt_tangente.subs(x, x_wert_3)
            steigung_dreieck = N((y_wert_2 - y_wert_3)/(x_wert_2-x_wert_3), 2)
            xwerte_dy = [x_wert_2, x_wert_2]
            ywerte_dy = [y_wert_2, y_wert_3]
            xwerte_dx = [x_wert_2, x_wert_3]
            ywerte_dx = [y_wert_3, y_wert_3]
            ywerte_tangente = [fkt_tangente.subs(x, -6), fkt_tangente.subs(x, 6)]

            plt.plot(xwerte_dy, ywerte_dy)
            plt.plot(xwerte_dx, ywerte_dx)
            plt.plot(xwerte_geraden, ywerte_tangente)
            plt.savefig('loesung_Aufgabe_1', dpi=150)
            loesung.append(str(teilaufg[i])
                           + r') \quad \mathrm{Tangente~an~Punkt~(1P),~~Steigungsdreieck~(1P),~Steigung~m~=~'
                           + str(steigung_dreieck) + r'~bestimmt~(1P)} \\\\')
            Punkte += 3
            i += 1

        if d in teilaufg:
            aufgabe.append(str(teilaufg[i])
                           + f') Überprüfe die lokale Änderungsrate an der Stelle x = {x_wert_2} '
                             f'mit einer Rechnung. \n\n')
            a_3_re = faktor
            b_1_re = -2 * faktor * s_xwert
            b_2_re = faktor * x_wert_2
            b_3_re = b_1_re + b_2_re
            c_1_re = faktor * (s_xwert ** 2) + s_ywert - (faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert)
            c_2_re = b_3_re * x_wert_2

            a_1 = latex(N(faktor, 3))
            a_3 = latex(N(a_3_re, 3))
            b_1 = latex(N(b_1_re, 3))
            b_2 = latex(N(b_2_re, 3))
            b_3 = latex(N(b_3_re, 3))
            c_1 = latex(N(c_1_re, 3))
            c_2 = latex(N(c_2_re, 3))

            table = Tabular('c|c|c', row_height=1.2)
            table.add_row(a_1, b_1, c_1)
            table.add_hline(1, 3)
            table.add_row('', b_2, c_2)
            table.add_hline(1, 3)
            table.add_row(a_3, b_3, 0)

            division_fkt_linear = (fkt - fkt.subs(x, x_wert_2)) / (x - x_wert_2)
            partialbruch = latex(faktor) + 'x' + vorz_str(b_3_re)

            print(division_fkt_linear)
            print(partialbruch)

            # loesung.append(str(teilaufg[i]) + r') \quad \lim \limits_{x \to ' + str(x_wert_2)
            #               + r'} ~ \frac{f(x)-f(' + str(x_wert_2) + r')}{x' + vorz_str(-1 * x_wert_2)
            #               + r'} ~=~ \lim \limits_{x \to ' + str(x_wert_2) + r'} ~ \frac{' + fkt_str + '-('
            #               + latex(N(fkt.subs(x, x_wert_2), 3)) + ')}{x' + vorz_str(-1 * x_wert_2)
            #               + '} ~=~' + r' \lim \limits_{x \to ' + str(x_wert_2) + '}~' + partialbruch + '~=~'
            #               + latex(N(fkt_abl_x0, 3)) + r' \quad (3P) \\'
            #               + r'\to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} \quad (1P) \\\\')
            # loesung.append(r' \mathrm{Lösung~mit~Hornerschema~(2P):}  \hspace{3em} ')
            # loesung.append(table)
            # loesung.append(r' \hspace{5em}')

            loesung.append(str(teilaufg[i]) + r') \quad f^{ \prime} (x)~=~' + latex(fkt_abl) + r' \to f^{ \prime} ('
                           + str(x_wert_2) + ')~=~' + latex(fkt_abl.subs(x, x_wert_2)) +
                           r' \quad (2P) \quad \to \quad \mathrm{Zeichnung~stimmt~mit~berechneter~Steigung~überein} '
                           r'\quad (1P) \\\\')
            Punkte += 3

        # plt.show()
        return [aufgabe, loesung, Punkte]

    def ableitungen(nr, teilaufg):
        i = 0
        Punkte = 0

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em} \\']

        def faktorliste(p, q, n):
            return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

        def exponenten(n):
            menge = set()  # ich habe hier eine Menge verwendet, weil diese keine gleichen Elemente enthält
            while len(menge) < n:
                menge.add(nzahl(2, 6 + n))
            return menge

        if a in teilaufg:
            a1, a2 = faktorliste(2, 10, 2)  # funktioniert auch so :)
            b1, b2, b3 = faktorliste(2, 12, 3)
            fkt_str_a = str(a1) + 'x' + vorz_str(a2)
            fkt_str_b = str(b1) + 'x^2' + vorz_str(b2) + 'x' + vorz_str(b3)

            aufgabe.append(str(teilaufg[i]) 
                           + r') Berechne die Ableitung der folgenden Funktionen mithilfe des Differentialquotienten.')
            aufgabe.append(r'i) \quad f_1 (x)~=~' + fkt_str_a + r' \hspace{10em} ' + r'ii) \quad f_2 (x)~=~'
                           + fkt_str_b + r' \hspace{5em} \\')
            loesung.append(str(teilaufg[i])
                           + r') \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe~des~'
                             r'Differentialquotienten}. \\\\')
            loesung.append(r' i) \quad f_1 ^{ \prime} (x) ~=~ \lim \limits_{ h \to 0} \frac{f(x+h) ~-~ f(x)}{h}'
                           + r'= ~ \lim \limits_{ h \to 0}\frac{' + str(a1) + r'(x + h)~' + vorz_str(a2) + r'~-('
                           + str(a1) + r'x' + vorz_str(a2) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{'
                           + str(a1) + 'x~' + vorz_str(a1) + 'h~' + vorz_str(a2) + '~' + vorz_str(-1*a1) + r'x~'
                           + vorz_str(-1*a2) + r'}{h} =~ \lim \limits_{ h \to 0} \frac{~' + str(a1) + r'h~}{h} ~=~'
                           + str(a1) + r' \quad (3P) \\\\')  # \\\\ für Übersichtlichkeit
            loesung.append(r' ii) \quad f_2 ^{ \prime} (x) ~=~ \lim \limits_{ h \to 0}'
                           + r' \frac{f(x+h) - f(x)}{h} ~=~ \lim \limits_{ h \to 0} \frac{' + str(b1) + r'(x + h)^2 ~'
                           + vorz_str(b2) + r'(x+h) ~' + vorz_str(b3) + r' ~-~ (' + str(b1) + r'x^2' + vorz_str(b2)
                           + r'x~' + vorz_str(b3) + r')}{h}' + r' \\ =~ \lim \limits_{ h \to 0} \frac{~' + str(b1)
                           + r'x^2 ~' + vorz_str(2*b1) + 'xh ~' + vorz_str(b1) + 'h^2 ~' + vorz_str(b2) + 'x~'
                           + vorz_str(b2) + 'h~' + vorz_str(b3) + '~' + vorz_str(-1 * b1) + 'x^2~'
                           + vorz_str(-1 * b2) + 'x ~' + vorz_str(-1 * b3) + r'}{h} ~=~ \lim \limits_{ h \to 0} \frac{~'
                           + str(2*b1) + r'xh ~' + vorz_str(b1) + r'h^2~' + vorz_str(b2) + r' h~}{h} \\'
                           + r' ~=~ \lim \limits_{ h \to 0} \frac{~ h(~' + str(2*b1) + r'x~' + vorz_str(b1)
                           + 'h ~' + vorz_str(b2) + r'~)}{h} =~ \lim \limits_{ h \to 0} ' + str(2*b1) + r'x~'
                           + vorz_str(b1) + 'h ~' + vorz_str(b2) + r'~=~' + str(2*b1) + 'x~' + vorz_str(b2)
                           + r' \quad (5P) \\\\')
            Punkte += 8
            i += 1

        if b in teilaufg:
            def funktion(p):  # erzeugt eine Funktion und deren Ableitungen mit p Summanden und maximal p-Grades
                fkt = random.choice([zzahl(1, 10), 0])
                koeffizienten = faktorliste(1, 15, p)
                potenzen = exponenten(p)

                for koeffizient in koeffizienten:
                    fkt = koeffizient*(x**potenzen.pop()) + fkt
                fkt_abl_1 = expand(diff(fkt, x))
                fkt_abl_2 = expand(diff(fkt, x, 2))

                return fkt, fkt_abl_1, fkt_abl_2

            fkt_i, fkt_abl_1_i, fkt_abl_2_i = funktion(2)
            fkt_ii, fkt_abl_1_ii, fkt_abl_2_ii = funktion(3)

            aufgabe.append(str(teilaufg[i])
                           + r') Berechne die Ableitung der folgenden Funktionen mithilfe der '
                             r'elementaren Ableitungsregeln.')
            aufgabe.append(r'i) \quad f_1 (x)~=~' + latex(fkt_i) + r' \hspace{10em} ' + r'ii) \quad f_2 (x)~=~'
                           + latex(fkt_ii) + r' \hspace{5em} \\')
            loesung.append(str(teilaufg[i])
                           + r') \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~mithilfe~der~'
                             r'elementaren~Ableitungsregeln.} \\\\')
            loesung.append(r'i) \quad f_1^{ \prime} (x) ~=~' + latex(fkt_abl_1_i) + r' \quad (2P) \hspace{5em}'
                           r'ii) \quad f_2^{ \prime} (x) ~=~' + latex(fkt_abl_1_ii) + r' \quad (3P) \\\\')
            Punkte += 5
            i += 1

        if c in teilaufg:
            # Teilaufgabe i:
            faktor_i_a = zzahl(3, 15)
            exponent = nzahl(2, 6)
            fkt_i = faktor_i_a / (x**exponent)
            fkt_i_str = r' \frac{' + str(faktor_i_a) + '}{x^{' + str(exponent) + '}}'
            fkt_i_str_einf = str(faktor_i_a) + r'\cdot x^{' + str(-1*exponent) + '}'
            fkt_i_str_abl = str(-1 * faktor_i_a * exponent) + r' \cdot x^{' + str(-1*exponent - 1) + '}'

            # Teilaufgabe ii
            faktor_ii_a = zzahl(2, 15)
            exp_ii_a, exp_ii_b = exponenten(2)
            fkt_ii = faktor_ii_a * x**(exp_ii_a/exp_ii_b)
            fkt_ii_str = str(faktor_ii_a) + r' \sqrt[' + str(exp_ii_a) + ']{x^{' + str(exp_ii_b) + '}}'
            fkt_ii_str_einf = str(faktor_ii_a) + r' \cdot x^{ \frac{' + str(exp_ii_b) + '}{' + str(exp_ii_a) + '}}'
            fkt_ii_str_abl = (latex(Rational(faktor_ii_a * exp_ii_b, exp_ii_a)) + r' \cdot x^{'
                              + latex(Rational(exp_ii_b, exp_ii_a)-1) + '}')

            # print('2c) fkt_ii = ' + str(fkt_ii) + ' und fkt_ii_str = ' + str(fkt_ii_str) + ' und fkt_ii_abl = ' + str(fkt_iii_str_abl))

            # Teilaufgabe iii
            faktor_iii_a, faktor_iii_b, faktor_iii_c = faktorliste(2, 12, 3)
            exp_iii_a, exp_iii_b, exp_iii_c = exponenten(3)
            print(exp_iii_a, exp_iii_b, exp_iii_c)

            if faktor_iii_a/faktor_iii_b < 0:
                fkt_iii_str = (r'-~ \frac{' + str(abs(faktor_iii_a)) + '}{' + str(abs(faktor_iii_b)) + r'x^{' +
                               str(exp_iii_a) + '}}')
                fkt_iii_str_einf = ('-~' + latex(Rational(abs(faktor_iii_a), abs(faktor_iii_b))) + r' \cdot x^{' +
                                    str(-1*exp_iii_a) + '}')
                fkt_iii_str_abl = (latex(Rational(abs(faktor_iii_a*exp_iii_a), abs(faktor_iii_b))) + r' \cdot x^{'
                                   + str(-1*exp_iii_a - 1) + '}')
            else:
                fkt_iii_str = (r' \frac{' + str(abs(faktor_iii_a)) + '}{' + str(abs(faktor_iii_b)) + r'x^{' +
                               str(exp_iii_a) + '}}')
                fkt_iii_str_einf = (latex(Rational(abs(faktor_iii_a), abs(faktor_iii_b))) + r' \cdot x^{' +
                                    str(-1 * exp_iii_a) + '}')
                fkt_iii_str_abl = ('-~' + latex(Rational(abs(faktor_iii_a * exp_iii_a), abs(faktor_iii_b)))
                                   + r' \cdot x^{' + str(-1 * exp_iii_a - 1) + '}')

            if faktor_iii_c < 0:
                fkt_iii_str = (fkt_iii_str + r'~-~ \frac{' + str(abs(faktor_iii_c)) + r'}{ \sqrt[' +
                               str(exp_iii_b) + ']{x^{' + str(exp_iii_c) + '}}}')
                exp_iii_c *= -1
                fkt_iii_str_einf = (fkt_iii_str_einf + '~-~' + str(abs(faktor_iii_c)) + r' \cdot x^{'
                                    + latex(Rational(exp_iii_c, exp_iii_b)) + '}')
                fkt_iii_str_abl = (fkt_iii_str_abl + '~+~'
                                   + latex(Rational(abs(faktor_iii_c * exp_iii_c), abs(exp_iii_b)))
                                   + r' \cdot x^{' + latex(Rational(exp_iii_c - exp_iii_b, exp_iii_b)) + '}')
            else:
                fkt_iii_str = (fkt_iii_str + r'~+~ \frac{' + str(abs(faktor_iii_c)) + r'}{ \sqrt[' +
                               str(exp_iii_b) + ']{x^{' + str(exp_iii_c) + '}}}')
                exp_iii_c *= -1
                fkt_iii_str_einf = (fkt_iii_str_einf + '~+~' + str(abs(faktor_iii_c)) + r' \cdot x^{'
                                    + latex(Rational(exp_iii_c, exp_iii_b)) + '}')
                fkt_iii_str_abl = (fkt_iii_str_abl + '~-~'
                                   + latex(Rational(abs(faktor_iii_c * exp_iii_c), abs(exp_iii_b)))
                                   + r' \cdot x^{' + latex(Rational(exp_iii_c - exp_iii_b, exp_iii_b)) + '}')

            print(faktor_iii_a)
            print(faktor_iii_b)
            print(faktor_iii_c)
            print(r'2c) fkt_iii_str = ' + str(fkt_iii_str))
            print(r'2c) fkt_iii_einf = ' + str(fkt_iii_str_einf))
            print(r'2c) fkt_iii_abl = ' + str(fkt_iii_str_abl))

            aufgabe.append(str(teilaufg[i]) + r') Berechne die Ableitung der folgenden Funktionen mithilfe der '
                                              r'elementaren Ableitungsregeln.')
            aufgabe.append(r'i) \quad f_1 (x)~=~' + fkt_i_str + r' \hspace{5em} ' + r'ii) \quad f_2 (x)~=~'
                           + fkt_ii_str + r' \hspace{5em} iii) \quad f_3(x)~=~' + fkt_iii_str + r' \\')
            loesung.append(str(teilaufg[i]) + r') \mathrm{~Berechne~die~erste~Ableitung~der~folgenden~Funktionen~'
                                              r'mithilfe~der~elementaren~Ableitungsregeln.} \\\\')
            loesung.append(r'i) \quad f_1(x) ~=~' + fkt_i_str + '~=~' + fkt_i_str_einf +
                           r' \quad f_1^{ \prime} (x) ~=~' + fkt_i_str_abl + r' \quad (1P) \\')
            loesung.append(r'ii) \quad f_2(x) ~=~' + fkt_ii_str + '~=~' + fkt_ii_str_einf +
                           r' \quad f_2^{ \prime} (x) ~=~' + fkt_ii_str_abl + r' \quad (1P) \\')
            loesung.append(r'iii) \quad f_3(x) ~=~' + fkt_iii_str + '~=~' + fkt_iii_str_einf +
                           r' \quad f_3^{ \prime} (x) ~=~' + fkt_iii_str_abl + r' \quad (1P) \\')
            Punkte += 7
            i += 1

        return [aufgabe, loesung, Punkte]

    aufgaben = [aenderungsrate(1, [a, b, c, d]), ableitungen(2, [a, b, c])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))

    # Angaben für den Test im pdf-Dokument
    Datum = NoEscape(r' \today')
    Kurs = 'Leistungskurs'
    Fach = 'Mathematik'
    Klasse = '12'
    Lehrer = 'Herr Herrys'
    Art = 'HAK 04 - ganzrationale Funktionen ableiten'

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
            graph.add_image(r'Aufgabe_1.png', width='400px')
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

        Loesung.append(NewPage())
        with Loesung.create(Figure(position='h!')) as graph:
            graph.add_image(r'loesung_Aufgabe_1.png', width='400px')
            # falls es nicht funktioniert wieder zu 'C:\Users\aherr\Documents\GitHub\loesung_Aufgabe_1.png' wechseln

        Loesung.generate_pdf(f'{Art} {Teil} - Lsg', clean_tex=true)
        plt.cla()

    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


anzahl_HAKs = 1
probe = False
alphabet = string.ascii_uppercase
for teil_id in range(anzahl_HAKs):
    if probe:
        erstellen('Probe {:02d}'.format(teil_id + 1))
    else:
        erstellen(f'Gr. {alphabet[teil_id]}')
