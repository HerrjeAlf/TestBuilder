from Aufgaben import *
from pylatex import (Document, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Package, HugeText, MultiRow, NoEscape)
from pylatex.utils import bold

# Auslesen der Aufgabenstellungen bzw. Erläuterungen und der Teilaufgaben
alle_Aufgaben = []
for titel in liste_Aufgaben:
    file = open('../Aufgaben/' + titel + '.py', 'r', encoding='utf-8')
    Titel = titel.replace('_', ' ')
    liste_file = []
    for line in file:
        liste_file.append(line.strip())
    file.close()
    i = 0
    Aufgabenstellung = [LargeText(bold('Aufgaben zum Thema ' + Titel + ' \n'))]
    for element in liste_file:
        if '# in Entwicklung' in element:
            del liste_file[i:]
        if ('def' in element) and ('(nr' in element) and ('#' in liste_file[i+1]):
            Aufgabenstellung.append(MediumText(bold(' \n' + element[4:] + ' \n')))
            if '#' in liste_file[i+1]:
                Aufgabenstellung.append('Erläuterungen: \n')
            p = 1
            while '#' in liste_file[i+p]:
                Aufgabenstellung.append(liste_file[i+p][2:] + ' \n')
                p += 1
            Aufgabenstellung.append(' \n')
        if 'in teilaufg' in element and '#' in liste_file[i+1] and 'if len([element for' not in element:
            Aufgabenstellung.append('Teilaufgabe ' + liste_file[i][4] + '): ' + liste_file[i+1][2:] + ' \n')
        if 'if len([element for element in' in element and '#' in liste_file[i+1]:
            Aufgabenstellung.append('Teilaufgabe ' + liste_file[i][33] + '): ' + liste_file[i+1][2:] + ' \n')
        i += 1
    alle_Aufgaben.append(Aufgabenstellung)
# print(alle_Aufgaben)

# Erstellen des PDF-Dokuments aus der Liste mit den Aufgabenstellungen
geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
text = Document(geometry_options=geometry_options)

for themen in alle_Aufgaben:
    for element in themen:
        text.append(element)
    text.append(NewPage())

text.generate_pdf(f'../pdf/Übersicht der Aufgaben', clean_tex=true)



