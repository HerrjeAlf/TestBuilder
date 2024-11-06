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
            aufg = aufg + vorz_v_innen(fakt[k + 1]/10, bas[0])
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
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
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

def terme_ausmultiplizieren(nr, teilaufg=['a', 'b', 'c', 'd', 'e', 'f'], anzahl=False, BE=[]):
    # Hier sollen die SuS verschiedene Produkte von Terme mit Klammern ausmultiplizieren
    # Mithilfe von "teilaufg=[]" können folgende Aufgaben (auch mehrfach z.B. der Form ['a', 'a', ...]) ausgewählt werden:
    # a)
    #
    # Mit 'anzahl=' kann eine Anzahl von zufällig ausgewählten Teilaufgaben aus den in 'teilaufg=[]' festgelegten Arten Bruchtermen erstellt werden.
    # Mit dem Parameter "BE=[]" kann die Anzahl der Bewertungseinheiten festgelegt werden. Wird hier nichts eingetragen, werden die Standardbewertungseinheiten verwendet.

    liste_bez = [f'{str(nr)}']
    i = 0
    aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')),
               'Löse die Klammern auf und fasse zusammen.']
    loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
    grafiken_aufgaben = []
    grafiken_loesung = []

    def terme_in_klammer(anz_terme, anz_var, fakt=True, exp=False, p=1, q=10):
        anz_var = anz_terme if anz_var > anz_terme else anz_var
        liste_exp = [1 for _ in range(anz_var)]
        liste_exp = exponenten(anz_var, wdh=True) if exp != False else liste_exp
        if fakt == False:
            liste_fakt = [1 for _ in range(anz_terme)]
        else:
            fakt = random.choice(['nat', 'ganz', 'rat', 'dez']) if fakt not in ['nat', 'ganz', 'rat', 'dez'] else fakt
            if fakt == 'nat':
                liste_fakt = [nzahl(p, q) for _ in range(anz_terme)]
            elif fakt == 'ganz':
                liste_fakt = [nzahl(p, q) for _ in range(anz_terme)]
            elif fakt == 'rat':
                liste_fakt = [Rational(zzahl(p, q), nzahl(p, q)) for _ in range(anz_terme)]
            else:
                liste_fakt = [zzahl(p, 10 * q) / 10 for _ in range(anz_terme)]

        liste_var = random_selection([1, a, b, c, d, e, f, g, h, x, y, z], anzahl=anz_var, wdh=False)
        terme = [[liste_fakt[k], liste_var[k % anz_var] ** liste_exp[k % anz_var]] for k in range(anz_terme)]
        return terme

    def einf(anz_terme, anz_var, var_aus=False, fakt_aus='vorz', fakt_in=True, exp_aus=False, exp_in=False, p=1, q=10):
        terme = terme_in_klammer(anz_terme, anz_var, fakt_in, exp_in)
        print(terme)
        fakt_aus = random.choice(['vorz', 'nat', 'ganz', 'rat', 'dez']) if fakt_aus not in ['vorz', 'nat', 'ganz',
                                                                                            'rat',
                                                                                            'dez'] else fakt_aus
        faktoren = {'vorz': random.choice([-1, 1]), 'nat': nzahl(1, 9), 'ganz': zzahl(1, 9),
                    'rat': Rational(zzahl(p, q), nzahl(p, q)), 'dez': zzahl(1, 100) / 10}
        fakt = faktoren[fakt_aus]
        if var_aus == True:
            var_aus = random.choice([1, a, b, c, d, e, f, g, h, x, y, z])
        else:
            var_aus = 1
        if exp_aus == True:
            exp_aus = nzahl(p, q)
        else:
            exp_aus = 1
        print(fakt)
        print(var_aus)
        print(exp_aus)
        print(anz_terme)
        ausmulti_terme = [[fakt * terme[k][0], (var_aus ** exp_aus) * terme[k][1]] for k in range(anz_terme)]
        print(ausmulti_terme)
        kopie_terme = ausmulti_terme.copy()
        print(kopie_terme)
        gleiche_terme = []
        while len(kopie_terme) != 0:
            gleichartiger_term = []
            for element in kopie_terme:
                var = element[1]
                for element1 in kopie_terme:
                    if element1[1] == var:
                        gleichartiger_term.append(element1)
                        kopie_terme.remove(element1)
                        print(element1)
            gleiche_terme.append(gleichartiger_term)
        terme_erg = []
        print(gleiche_terme)
        for element in gleiche_terme:
            zahl = 0
            for k in range(len(element)):
                zahl += element[k][0]
            terme_erg.append([zahl, element[0][1]])
        print(terme_erg)
        klammer_terme = vorz_v_aussen(terme[0][0], fakt_var(terme[0][1]))
        for k in range(anz_terme-1):
            klammer_terme += vorz_v_innen(terme[k+1][0], fakt_var(terme[k+1][1]))
        if var_aus ==1:
            aufg = vorz_v_aussen(fakt,r' \left( ' + klammer_terme + r' \right) ~')
        else:
            aufg = vorz_v_aussen(fakt,latex(var_aus**exp_aus) + r' \left( ' + klammer_terme + r' \right) ')

        lsg_zw = vorz_v_aussen(ausmulti_terme[0][0],fakt_var(ausmulti_terme[0][1]))
        for k in range(anz_terme-1):
            lsg_zw += vorz_v_innen(ausmulti_terme[k+1][0], fakt_var(ausmulti_terme[k+1][1]))
        print(lsg_zw)
        lsg_erg = vorz_v_aussen(terme_erg[0][0], fakt_var(terme_erg[0][1]))
        for k in range(len(terme_erg) - 1):
            lsg_erg += vorz_v_innen(terme_erg[k + 1][0], fakt_var(terme_erg[k + 1][1]))
        if lsg_zw == lsg_erg:
            lsg = aufg + '~=~' + lsg_zw
        else:
            lsg = aufg + '~=~' + lsg_zw + '~=~' + lsg_erg
        return aufg, lsg



    if anzahl != False:
        exit("Der Parameter 'anzahl=' muss eine natürliche Zahl kleiner 27 sein.") if type(anzahl) != int or anzahl > 26 else anzahl
        teilaufg = random_selection(teilaufg, anzahl, True)
    aufgaben = {'a': einf(2, 2, fakt_aus='vorz', fakt_in='ganz'),
                'b': einf(2, 2, fakt_aus='ganz', fakt_in='ganz'),
                'c': einf(3, 2, var_aus=True, fakt_aus=True, fakt_in=True),
                'd': einf(3, 2, exp_in=True, fakt_in=True),
                'e': einf(2, 2, var_aus=True, fakt_in='ganz'),
                'f': einf(2, 2, var_aus=True, fakt_in=None)}

    aufg = ''
    lsg = ''
    punkte = 0
    for element in teilaufg:
        teilaufg_aufg, teilaufg_lsg = aufgaben[element]
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