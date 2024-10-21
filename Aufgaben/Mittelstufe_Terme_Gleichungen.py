import string
import numpy as np
import random, math
from numpy.linalg import solve as slv
from pylatex import (Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, MultiRow)
from pylatex.utils import bold
from random import *
from sympy import *
from sympy.plotting import plot
from skripte.funktionen import *
from skripte.plotten import *


a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')
liste_teilaufg = list(string.ascii_lowercase)

def terme_addieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], anzahl=False, BE=[]):
    # Hier sollen SuS Terme addieren bzw. subtrahieren
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) Terme mit einer Basis und ganzzahligen Faktoren (zwei Summanden)
    # b) Terme mit einer Basis und ganzzahligen Faktoren (drei Summanden)
    # c) Terme mit einer Basis und rationalen Faktoren (zwei Summanden)
    # d) Terme mit einer Basis und rationalen Faktoren (drei Summanden)
    # e) Bruchterme mit einer Basis (zwei Summanden)
    # f) Bruchterme mit einer Basis (drei Summanden)
    # g) gemischte Terme mit einer Basis und ganzzahligen Faktoren und Zahlen (3 Summanden)
    # h) gemischte Terme mit einer Basis und ganzzahligen Faktoren und Zahlen (5 Summanden)
    # i) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (4 Summanden)
    # j) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (6 Summanden)
    # k) gemischte Terme mit vers. gleichwertigen Termen und ganzzahligen Faktoren (8 Summanden)
    # l) gemischte Bruchterme mit vers. gleichwertigen Termen (4 Summanden)
    # d) gemischte Bruchterme mit vers. gleichwertigen Termen (6 Summanden)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    i = 0
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Fasse die Terme zusammen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def einf_ganzz_terme(anz_sum):
        fakt = faktorliste(anz_sum, 1,12)
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg = '~' + vorz_v_aussen(fakt[0],bas[0])
        for k in range(len(fakt)-1):
            aufg = aufg + vorz_v_innen(fakt[k + 1],bas[0])
        lsg = aufg + '~=~' + str(sum(fakt)) + bas[0]
        return aufg, lsg

    def einf_ratio_terme(anz_sum):
        fakt = [zzahl(1,20) for step in range(anz_sum)]
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg =  '~' + vorz_v_aussen(fakt[0]/10,bas[0])
        for k in range(len(fakt) - 1):
            aufg = aufg + vorz_v_innen(fakt[k + 1], bas[0])
        lsg = aufg + '~=~' + latex(sum(fakt)/10) + bas[0]
        return aufg, lsg

    def einf_bruch_terme(anz_sum):
        fakt = [random.choice([-1,1])* Rational(nzahl(1,12), random.choice([2, 3, 5, 7, 11])) for step in range(anz_sum)]
        bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'])
        aufg =  '~' + vorz_v_aussen(fakt[0], bas[0])
        for k in range(len(fakt) - 1):
            aufg = aufg + vorz_v_innen(fakt[k + 1], bas[0])
        lsg = aufg + '~=~' + latex(sum(fakt)/10) + bas[0]
        return aufg, lsg

    def einf_gem_ganzz_terme(anz_sum):
        fakt = faktorliste(anz_sum, 2,12)
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z])
        liste_bas = [['', str(bas[0])][step%2] for step in range(anz_sum)]
        liste_bas_zahl = [1 if element == '' else bas[0] for element in liste_bas]
        summe = 0
        for k in range(len(liste_bas_zahl)):
            summe += fakt[k]*liste_bas_zahl[k]
        aufg =  '~' + vorz_v_aussen(fakt[0],liste_bas[0])
        for k in range(len(liste_bas)-1):
            aufg = aufg + vorz_v_innen(fakt[k+1],liste_bas[k+1])
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg

    def gem_glw_ganzz_terme(anz_sum):
        if anz_sum == 1:
            anz_sum = anz_sum + 1
            anz_glw = 1
        elif anz_sum < 5:
            anz_glw = 2
        else:
            anz_glw = 3
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z], 2,False)
        liste_glw_terme = []
        for step in range(anz_glw):
            glw_term = 1
            for element in bas:
                exp = nzahl(0,5)
                glw_term = glw_term*(element**exp)
            liste_glw_terme.append(glw_term)
        print(liste_glw_terme)
        liste_terme = []
        for step in range(anz_sum):
            liste_terme.append([zzahl(1,12), liste_glw_terme[step % anz_glw]])
        random.shuffle(liste_terme)
        print(liste_terme)
        summe = 0
        for element in liste_terme:
            summe += element[0] * element[1]
        aufg =  '~' + vorz_v_aussen(liste_terme[0][0],latex(liste_terme[0][1]))
        del liste_terme[0]
        for element in liste_terme:
            aufg = aufg + vorz_v_innen(element[0],latex(element[1]))
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg

    def gem_glw_rat_terme(anz_sum):
        if anz_sum == 1:
            anz_sum = anz_sum + 1
            anz_glw = 1
        elif anz_sum < 5:
            anz_glw = 2
        else:
            anz_glw = 3
        bas = random_selection([a, b, c, d, e, f, g, h, x, y, z], 2,False)
        liste_glw_terme = []
        for step in range(anz_glw):
            glw_term = 1
            for element in bas:
                exp = nzahl(0,5)
                glw_term = glw_term*(element**exp)
            liste_glw_terme.append(glw_term)
        print(liste_glw_terme)
        liste_terme = []
        for step in range(anz_sum):
            liste_terme.append([Rational(zzahl(1,12), zzahl(1,12)), liste_glw_terme[step % anz_glw]])
        random.shuffle(liste_terme)
        print(liste_terme)
        summe = 0
        for element in liste_terme:
            summe += element[0] * element[1]
        aufg =  '~' + vorz_v_aussen(liste_terme[0][0],latex(liste_terme[0][1]))
        del liste_terme[0]
        for element in liste_terme:
            aufg = aufg + vorz_v_innen(element[0],latex(element[1]))
        lsg = aufg + '~=~' + latex(summe)
        return aufg, lsg
    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    aufgaben = {'a': [einf_ganzz_terme, 2], 'b': [einf_ganzz_terme, 3],
                'c': [einf_ratio_terme, 2], 'd': [einf_ratio_terme, 3],
                'e': [einf_bruch_terme, 2], 'f': [einf_bruch_terme, 3],
                'g': [einf_gem_ganzz_terme, 3], 'h': [einf_gem_ganzz_terme, 5],
                'i': [gem_glw_ganzz_terme, 4], 'j': [gem_glw_ganzz_terme, 6],
                'k': [gem_glw_ganzz_terme, 8], 'l': [gem_glw_rat_terme, 4],
                'm': [gem_glw_rat_terme, 6]}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element][0](aufgaben[element][1])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg
        if element not in ['i', 'j', 'k']:
            if (i+1) % 3 != 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \hspace{5em} '
            elif (i + 1) % 3 == 0 and i+1 < len(teilaufg):
                aufg = aufg + r' \\\\'
        if element not in ['i', 'j', 'k']:
            if (i+1) % 2 != 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \hspace{5em} '
            elif (i + 1) % 2 == 0 and i+1 < len(teilaufg):
                lsg = lsg + r' \\\\'
        else:
            aufg = aufg + r' \\\\'
            lsg = lsg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]

def terme_multiplizieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f', 'g'], anzahl=False, BE=[]):
    # Hier sollen die SuS mehrere Potenzen, mit verschiedenen Exponenten, multiplizieren.
    # Mithilfe von "teilaufg=[]" können folgende Bruchterme (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a) vier Faktoren aus zwei Basen und ganzzahligen Exponenten
    # b) sechs Faktoren aus zwei Basen und ganzzahligen Exponenten
    # c) sechs Faktoren aus drei Basen und ganzzahligen Exponenten
    # d) vier Faktoren aus zwei Basen und rationalen Exponenten
    # e) sechs Faktoren aus drei Basen und rationalen Exponenten
    # f) vier Faktoren aus zwei Basen und rationalen Exponenten (als Dezimalbruch)
    # g) sechs Faktoren aus drei Basen und rationalen Exponenten (als Dezimalbruch)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    i = 0
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Vereinfache.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def aufg_lsg(exponenten, anz_bas):
        ar_ausw_bas = random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z'], anz_bas, False)
        ausw_bas = [element for element in ar_ausw_bas]
        list_basen = ausw_bas.copy()
        for step in range(len(exponenten)-len(ausw_bas)):
            random.shuffle(ausw_bas)
            list_basen.append(random.choice(ausw_bas))
        bas_exp = [[list_basen[k], exponenten[k]] for k in range(len(exponenten))]
        random.shuffle(bas_exp)
        ausw_bas.sort()
        aufg = ''
        m = 1
        for element in bas_exp:
            if m != len(bas_exp):
                aufg = aufg + element[0] + '^{' + gzahl(element[1]) + r'}~ \cdot ~'
            else:
                aufg = aufg + element[0] + '^{' + gzahl(element[1]) + '}'
            m += 1
        lsg = aufg + '~=~'
        exp_sort = []
        for basis in ausw_bas:
            exp_der_basis = []
            for element in bas_exp:
                if basis == element[0]:
                    exp_der_basis.append(element[1])
            lsg = lsg + basis + '^{' + gzahl(exp_der_basis[0])
            k = 1
            for zahl in range(len(exp_der_basis) - 1):
                lsg = lsg + vorz_str(exp_der_basis[k])
                k += 1
            lsg = lsg + '}'
            if basis != ausw_bas[-1]:
                lsg = lsg + r'~ \cdot ~'
            exp_sort.append(exp_der_basis)
        lsg = lsg + '~=~'
        k = 0
        for basis in ausw_bas:
            if basis != ausw_bas[-1]:
                if sum(exp_sort[k]) == 0:
                    pass
                else:
                    lsg = lsg + basis + '^{' + gzahl(sum(exp_sort[k])) + r'} \cdot '
            else:
                if sum(exp_sort[k]) == 0:
                    pass
                else:
                    lsg = lsg + basis + '^{' + gzahl(sum(exp_sort[k])) + '}'
            k += 1

        return aufg, lsg


    if anzahl != False:
        if type(anzahl) != int or anzahl > 26:
            exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.")
        teilaufg = random_selection(teilaufg, anzahl, True)
    aufgaben = {'a': [aufg_lsg, [zzahl(2,9) for zahl in range(4)], 2],
                'b': [aufg_lsg, [zzahl(2,9) for zahl in range(6)], 2],
                'c': [aufg_lsg, [zzahl(2,9) for zahl in range(6)], 3],
                'd': [aufg_lsg, [Rational(nzahl(1,9), nzahl(2,9)) for zahl in range(4)], 2],
                'e': [aufg_lsg, [Rational(nzahl(1,9), nzahl(2,9)) for zahl in range(6)], 3],
                'f': [aufg_lsg, [zzahl(2,9)/10 for zahl in range(4)], 2],
                'g': [aufg_lsg, [zzahl(2,9)/10 for zahl in range(6)], 3]}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element][0](aufgaben[element][1], aufgaben[element][2])
        aufg = aufg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_aufg
        lsg = lsg + str(liste_teilaufg[i]) + r') \quad ' + teilaufg_lsg + r' \\\\'
        if (i+1) % 2 != 0 and i+1 < len(teilaufg):
            aufg = aufg + r' \hspace{5em} '
        else:
            aufg = aufg + r' \\\\'
        punkte += 1
        i += 1

    if BE != []:
        if len(BE) > 1:
            print('Der Parameter BE darf nur ein Element haben, zum Beispiel BE=[2]. '
                  'Deswegen wird die standardmäßige Punkteverteilung übernommen.')
            liste_punkte = [punkte]
        liste_punkte = BE
    else:
        liste_punkte = [punkte]
    aufgabe.append(aufg)
    loesung.append(lsg)

    return [aufgabe, loesung, grafiken_aufgaben, grafiken_loesung, liste_punkte, liste_bez]
