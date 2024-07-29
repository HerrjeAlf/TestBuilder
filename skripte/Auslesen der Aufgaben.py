from Aufgaben import *

for titel in liste_Aufgaben:
    file = open('../Aufgaben/' + titel + '.py', 'r')
    liste_file = []
    for line in file:
        liste_file.append(line.strip())
    file.close()
    i = 0
    Aufgabenstellung = []
    for element in liste_file:
        if '# in Entwicklung' in element:
            del liste_file[i:]
        if 'del' and 'nr,' in element:
            p = 1
            Aufgabenstellung.append(element[4:])
            while '#' in liste_file[i+p]:
                Aufgabenstellung.append('Erläuterungen: ' + liste_file[i+p][2:])
                p += 1
        if 'in teilaufg:' in element and '#' in liste_file[i+1]:
            Aufgabenstellung.append('Teilaufgabe ' + liste_file[i][4] + '): ' + liste_file[i+1][2:])
        i += 1
    print(Aufgabenstellung)





