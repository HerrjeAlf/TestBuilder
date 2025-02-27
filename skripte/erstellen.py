import datetime
import os
import string
from pylatex import (Document, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Package, HugeText, MultiRow, NoEscape, Center)
from pylatex.utils import bold, italic
from skripte.funktionen import *
from skripte.plotten import *

# # Sorgt dafür, dass mögliche benötigte Ordner erstellt werden
dirs = ['img/temp', 'pdf']
for directory in dirs:
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass

# Löscht alle PDFs in pdf außer die in pdf_behalten
pdf_behalten = ['Übersicht der Aufgaben.pdf']
for name in os.listdir('pdf'):
   if name not in pdf_behalten:
        os.remove(f'pdf/{name}')

geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.5in", "rmargin": "0.7in"}

def seite(aufgaben):
    Aufgabe = Document(geometry_options=geometry_options)
    Loesung = Document(geometry_options=geometry_options)

    for aufgabe in aufgaben:
        i = 0
        for elements in aufgabe[0]:
            if '~' in elements:
                with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Figure' in elements:
                with Aufgabe.create(Figure(position='ht!')) as graph:
                    graph.add_image(f'../img/temp/{aufgabe[2][i]}', width='250px', placement=None)
                Aufgabe.append(SmallText('Abbildung ' + str(i+1) + ' \n\n'))
                i += 1
            elif 'Grafik' in elements:
                if isinstance(elements, list) and len(elements) == 2:
                    with Aufgabe.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/temp/{aufgabe[2][i]}', width=elements[1])
                    i += 1
                elif isinstance(elements, str):
                    with Aufgabe.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/temp/{aufgabe[2][i]}', width='250px')
                    i += 1
            elif 'Bild' in elements:
                if isinstance(elements, list) and len(elements) == 2:
                    with Aufgabe.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/aufgaben/{aufgabe[2][i]}', width=elements[1])
                    i += 1
                elif isinstance(elements, str):
                    with Aufgabe.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/aufgaben/{aufgabe[2][i]}', width='300px')
                    i += 1
            elif 'NewPage' in elements:
                Aufgabe.append(NewPage())
            else:
                Aufgabe.append(elements)

    for loesung in aufgaben:
        i = 0
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Figure' in elements:
                with Loesung.create(Figure(position='ht!')) as graph:
                    graph.add_image(f'../img/temp/{loesung[3][i]}', width='200px')
                i += 1
            elif 'Grafik' in elements:
                if isinstance(elements, list) and len(elements) == 2:
                    with Loesung.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/temp/{loesung[3][i]}', width=elements[1])
                    i += 1
                elif isinstance(elements, str):
                    with Loesung.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/temp/{loesung[3][i]}', width='250px')
                    i += 1
            elif 'Bild' in elements:
                if isinstance(elements, list) and len(elements) == 2:
                    with Loesung.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/aufgaben/{loesung[2][i]}', width=elements[1])
                    i += 1
                elif isinstance(elements, str):
                    with Loesung.create(Figure(position='ht!')) as graph:
                        graph.add_image(f'../img/aufgaben/{loesung[2][i]}', width='300px')
                    i += 1
            elif 'NewPage' in elements:
                Aufgabe.append(NewPage())
            else:
                Loesung.append(elements)

    return Aufgabe, Loesung

# hier wird ein Arbeitsblatt erzeugt
def arbeitsblatt_erzeugen(liste_seiten, angaben, anzahl=1, clean_tex=True):
    def arbeitsblatt(Teil, liste_seiten, ang):
        schule, schulart, Klasse, Thema, in_tagen= ang[0], ang[1], ang[2], ang[3], ang[4]
        print(f'\033[38;2;100;141;229m\033[1m Gr. {Teil}\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d.%m.%Y')

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Aufgaben():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            table1 = Tabular('|c|c|c|c|p{7cm}|', row_height=1.2)
            table1.add_row((MultiColumn(5, align='c', data=MediumText(bold('Arbeitsblatt - ' + Thema))),))
            table1.add_hline(1,5)
            table1.add_row(MediumText(bold(schule)), 'Kl.', 'Gr.', ' Datum ',
                           MultiRow(2, data=MediumText(bold('Name:'))))
            table1.add_hline(2,4)
            table1.add_row(SmallText(bold(schulart)), Klasse, Teil, Datum, '')
            table1.add_hline(1,5)
            Aufgabe.append(table1)
            Aufgabe.append(' \n\n\n\n')

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            k = 0
            for element in liste_seiten:
                Aufgabe.extend(element[0])
                Aufgabe.append(NewPage())

            Aufgabe.generate_pdf(f'pdf/Kl. {Klasse} - Arbeitsblatt {Thema} Gr. {Teil}', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def Erwartungshorizont():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f'Loesung vom Arbeitsblatt über {Thema} - Gr. {Teil}')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
            k = 0
            for element in liste_seiten:
                Loesung.extend(element[1])

            Loesung.generate_pdf(f'pdf/Kl. {Klasse} - Arbeitsblatt {Thema} - Lsg Gr. {Teil}', clean_tex=clean_tex)

        # Druck der Seiten
        Aufgaben()
        Erwartungshorizont()


    alphabet = string.ascii_uppercase
    arbeitsblatt(f'{alphabet[anzahl]}', liste_seiten, angaben)
    print()  # Abstand zwischen den Arbeiten (im Terminal)

# hier wird ein Test erzeugt
def test_erzeugen(liste_seiten, angaben, anzahl=1, probe=False, clean_tex=True):
    def erzeugen_test(Teil, liste_seiten, angaben):
        schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel =\
            (angaben[0], angaben[1], angaben[2], angaben[3], angaben[4], angaben[5], angaben[6], angaben[7])
        in_tagen, liste_bez, liste_punkte = angaben[8], angaben[9], angaben[10]
        print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d.%m.%Y')

        # erstellen der Tabelle zur Punkteübersicht
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        spalten = '|c|'
        for step in range(len(liste_punkte) - 1):
            spalten += 'p{0.5 cm}|'
        spalten += 'c|'
        liste_punkte.append(Punkte)
        anzahl_spalten = len(liste_punkte)
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z2.append('')

        table2 = Tabular(spalten, row_height=1.2)
        table2.add_hline()
        table2.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben'),))
        table2.add_hline()
        table2.add_row(liste_bez)
        table2.add_hline()
        table2.add_row(liste_punkte)
        table2.add_hline()
        table2.add_row(liste_ergebnis_z1)
        table2.add_row(liste_ergebnis_z2)
        table2.add_hline()

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Aufgaben():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            table1 = Tabular('|c|p{2.5cm}|p{2.5cm}|p{2.5cm}|p{2cm}|p{3cm}|', row_height=1.2)
            table1.add_row((MultiColumn(6, align='c', data=MediumText(bold(schule))),))
            table1.add_row((MultiColumn(6, align='c', data=SmallText(bold(schulart))),))
            table1.add_hline()
            table1.add_row('Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:', 'Art:')
            table1.add_hline()
            table1.add_row(Klasse, Fach, Kurs, Lehrer, Datum, Art)
            table1.add_hline()
            Aufgabe.append(table1)
            Aufgabe.append(' \n\n\n\n')
            Aufgabe.append(LargeText(bold(f' {Titel} \n\n')))

            # Kopf nach der ersten Seite
            def tabelle_kopf(Text):
                table3 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
                table3.add_row(MediumText(bold(f'{Teil}')), MediumText(bold(f'{Text}')))
                table3.add_hline()
                table3.add_empty_row()
                return table3

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            k = 0
            for element in liste_seiten:
                if k > 0:
                    Aufgabe.append(tabelle_kopf(Titel))
                    Aufgabe.append('\n\n')
                Aufgabe.extend(element[0])
                Aufgabe.append(NewPage())
                k += 1


            if len(liste_seiten) % 2 == 0:
                Aufgabe.append(tabelle_kopf('für Notizen und Rechnungen'))
                Aufgabe.append(NewPage())

            Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

            Aufgabe.append('\n\n')
            Aufgabe.append('\n\n')
            Aufgabe.append(table2)

            Aufgabe.generate_pdf(f'pdf/Kl. {Klasse} - {Art} {Teil}', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def Erwartungshorizont():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n {Titel}')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
            k = 0
            for element in liste_seiten:
                Loesung.extend(element[1])

            Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

            Loesung.generate_pdf(f'pdf/Kl. {Klasse} - {Art} {Teil} - Lsg', clean_tex=clean_tex)

        # Druck der Seiten
        Aufgaben()
        Erwartungshorizont()
        del liste_bez[1:]
        del liste_punkte[1:]

    alphabet = string.ascii_uppercase
    if probe:
        erzeugen_test(f'Probe {anzahl + 1:02d}', liste_seiten, angaben)
    else:
        erzeugen_test(f'Gr. {alphabet[anzahl]}', liste_seiten, angaben)
    print()  # Abstand zwischen den Arbeiten (im Terminal)

# Hier wird eine Vorprüfung für den Abschluss der 10. Klasse erzeugt
def vorpruefung_kl10(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex=True):
    def erzeugen_vorpr_teil_1(liste_seiten_teil1, angb_teil1):
        in_tagen, liste_bez, liste_punkte = angb_teil1[0], angb_teil1[1], angb_teil1[2]
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')

        # Ergänzen der Listen für table4
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        liste_punkte.append(str(Punkte))
        liste_punkte = angb_teil1[-1]
        liste_bez = angb_teil1[-2]
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(len(liste_punkte) - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(len(liste_punkte) - 1):
            liste_ergebnis_z2.append('')


        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_1():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            with Aufgabe.create(Figure(position='h')) as kopf:
                kopf.add_image('../img/kopfzeile.png', width='480px')
            # erste Seite


            table1 = Tabular('l c', row_height=1.2)
            table1.add_row((MultiColumn(2, align='c',
                                        data=LargeText(bold(f'Einheitliche Klassenarbeit der Klasse 10'))),))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='c', data=HugeText(bold('Mathematik'))),))
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Allgemeine Arbeitshinweise')), '')
            table1.add_row(NoEscape(r'Die $ \mathbf{Arbeitszeit} $ beträgt $ \mathbf{90} $ Minuten.'), '')
            table1.add_row('Jede Aufgabe und alle Teilaufgaben sind mit der entsprechenden Punktzahl versehen. '
                           'Das soll Ihnen','')
            table1.add_row('bei der Reihenfolge der Bearbeitung von Teilaufgaben helfen.', '')
            table1.add_row(NoEscape('Die Schülerinnen und Schüler der ' + r'$ \mathbf{Erweiterungskurse} $'
                                    + ' müssen alle Aufgaben lösen.'), '')
            table1.add_row(NoEscape('Die Schülerinnen und Schüler der ' + r'$ \mathbf{Grundkurse} $ lösen nur '
                                    + r'$ \underline{die~ohne~Symbol~ * } $  (Sternchen)'), '')
            table1.add_row(' gekennzeichneten Aufgaben. Zusatzpunkte werden nicht vergeben.', '')
            table1.add_empty_row()
            table1.add_hline()
            table1.add_row((MultiColumn(2, align='|l|',
                                        data=italic('Bitte bearbeiten Sie alle Aufgaben auf den vorgegebenen Blättern. '
                                                    'Sollte der zur Verfügung stehende')),))
            table1.add_row((MultiColumn(2, align='|l|',
                                        data=italic('Platz nicht ausreichen, fügen Sie Ihre Ergänzungen auf einem '
                                                    'gesonderten Blatt ein.')),))
            table1.add_row((MultiColumn(2, align='|l|',
                                        data=italic('Alle Lösungswege müssen nachvollziehbar '
                                                    'dokumentiert sein.')),))
            table1.add_row((MultiColumn(2, align='|l|',
                                        data=italic('Denken Sie an Begründungen und vergessen Sie bei '
                                                    'Textaufgaben nicht den Antwortsatz.')),))
            table1.add_hline()
            table1.add_empty_row()
            table1.add_row('Falls Sie eine Lösung durch Probieren finden, müssen Sie Ihre Überlegungen ausreichend '
                           'kommentieren.', '')
            table1.add_row('Während der Arbeitszeit können Sie den nicht programmierbaren, nicht grafikfähigen '
                           'Taschenrechner,', '')
            table1.add_row('die Formelsammlung, das beiliegende Formelblatt (Doppelseite), Kurvenschablonen, '
                           'Zeichengräte', '')
            table1.add_row('sowie den Duden als Hilfsmittel benutzen. Viel Erfolg bei der Arbeit', '')
            table1.add_empty_row()
            table1.add_hline()
            table1.add_empty_row()
            table1.add_row('Vorname, Name:   ____________________', '')
            table1.add_empty_row()
            table1.add_row('Klasse, Kurs:   ____________________', '')
            table1.add_empty_row()
            table1.add_row('Fachlehrer*in:   ____________________', '')
            table1.add_empty_row()
            table1.add_hline()


            # Auswertung
            table3 = Tabular('|c|c| p{1cm} r p{7cm} ', row_height=1.5)
            table3.add_row((MultiColumn(5, align='c', data='Dieser Teil wird nur von der Lehrkraft ausgefüllt.'),))
            table3.add_row(MultiColumn(2, align='l', data=MediumText(bold('Punktewertung:'))),'', '', '')
            table3.add_hline(1, 2)
            table3.add_row(bold('Aufgabe'),bold('Summe'),'', MediumText('Note'), '____')
            table3.add_hline(1, 2)
            table3.add_row('1', '', '', '', '')
            table3.add_hline(1, 2)
            table3.add_row('2','','',MediumText('Punktewert'),'____')
            table3.add_hline(1, 2)
            table3.add_row('3','','', '', '')
            table3.add_hline(1, 2)
            table3.add_row('4','','',MediumText('Datum'),'_______________')
            table3.add_hline(1, 2)
            table3.add_row('5','','','','')
            table3.add_hline(1, 2)
            table3.add_row('Summe','','',MediumText('Unterschrift'),'_______________')
            table3.add_hline(1, 2)

            Aufgabe.append(table1)
            Aufgabe.append(' \n\n')
            Aufgabe.append(table3)

            Aufgabe.append(' \n\n')
            Aufgabe.append(NewPage())

            table5 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
            table5.add_row(MediumText(bold(f'Thema:')),MediumText(bold(f'Basisaufgaben')))
            table5.add_hline(1, 2)
            table5.add_empty_row()

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            for element in liste_seiten_teil1:
                Aufgabe.append(table5)
                Aufgabe.append(' \n\n')
                Aufgabe.extend(element[0])
                if element != liste_seiten_teil1[-1]:
                    Aufgabe.append(NewPage())

            # erstellen der Tabelle zur Punkteübersicht aller Aufgaben
            with Aufgabe.create(Center()) as centered:
                spalten = '|'
                for element in liste_punkte:
                    spalten += 'c|'
                with centered.create(Tabular(spalten, row_height=1.2)) as table4:
                    table4.add_hline(1)
                    table4.add_row((MultiColumn(len(liste_punkte), align='|c|',
                                                data='Punkteverteilung aller Basisaufgaben'),))
                    table4.add_hline(1)
                    table4.add_row(liste_bez)
                    table4.add_hline(1)
                    table4.add_row(liste_punkte)
                    table4.add_hline(1)
                    table4.add_row(liste_ergebnis_z1)
                    table4.add_row(liste_ergebnis_z2)
                    table4.add_hline(1)



            Aufgabe.generate_pdf(f'pdf/Vorpruefung Kl. 10 - Basisaufgaben', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_1():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f'Lösung Vorpruefung Kl. 10 - Basisaufgaben')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt

            for element in liste_seiten_teil1:
                Loesung.extend(element[1])


            Loesung.generate_pdf(f'pdf/Vorpruefung Kl. 10 - Basisaufgaben Lsg', clean_tex=clean_tex)

        # Druck der Seiten
        Teil_1()
        EWH_Teil_1()

    def erzeugen_vorpr_teil_2(liste_seiten_teil2, angb_teil2):
        in_tagen, liste_bez, liste_punkte = angb_teil2[0], angb_teil2[1], angb_teil2[2]
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')
        themen = ['Aufgabe zur Trigonometrie', 'Aufgabe zu Funktionen', 'Aufgaben zu Wahrscheinlichkeit',
                  'Aufgabe zur Flächenberechnung']

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_2():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)
            i = 0
            for element in themen:
                # Tabelle für Kopfzeile
                table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
                table2.add_row(MediumText(bold(f'Thema')),
                               MediumText(bold(element)))
                table2.add_hline(1, 2)
                table2.add_empty_row()

                # erstellen der Tabelle zur Punkteübersicht
                Punkte = (sum(liste_punkte[i][1:]))
                liste_bez[i].append('Summe')
                liste_punkte[i].append(str(Punkte))
                anzahl_spalten = len(liste_punkte[i])
                liste_ergebnis_z1 = ['erhaltene']
                for p in range(anzahl_spalten - 1):
                    liste_ergebnis_z1.append('')
                liste_ergebnis_z2 = ['Punkte']
                for p in range(anzahl_spalten - 1):
                    liste_ergebnis_z2.append('')

                # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
                for aufgaben in liste_seiten_teil2[i]:
                    Aufgabe.append(table2)
                    Aufgabe.append(' \n\n')
                    Aufgabe.extend(aufgaben[0])

                    # erstellen der Tabelle zur Punkteübersicht aller Aufgaben
                    with Aufgabe.create(Center()) as centered:
                        spalten = '|'
                        for element in liste_punkte[i]:
                            spalten += 'c|'
                        with centered.create(Tabular(spalten, row_height=1.2)) as table3:
                            table3.add_hline()
                            table3.add_row((MultiColumn(anzahl_spalten, align='|c|',
                                                        data='Punkteverteilung der Aufgabe'),))
                            table3.add_hline()
                            table3.add_row(liste_bez[i])
                            table3.add_hline()
                            table3.add_row(liste_punkte[i])
                            table3.add_hline()
                            table3.add_row(liste_ergebnis_z1)
                            table3.add_row(liste_ergebnis_z2)
                            table3.add_hline()

                    if element != liste_seiten_teil2[i][-1]:
                        Aufgabe.append(NewPage())
                i += 1

            Aufgabe.generate_pdf(f'pdf/Vorpruefung Kl. 10 - verschiedene Themen', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_2():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
            i = 0
            for thema in themen:
                Loesung.append(LargeText(bold(f'Lösung Vorpruefung Kl. 10 - verschiedene Themen')))
                for element in liste_seiten_teil2[i]:
                    Loesung.extend(element[1])
                Loesung.append(NewPage())
                i += 1

            Loesung.generate_pdf(f'pdf/Vorpruefung Kl. 10 - verschiedene Themen Lsg', clean_tex=clean_tex)

        # Druck der Seiten
        Teil_2()
        EWH_Teil_2()

    erzeugen_vorpr_teil_1(liste_seiten_teil1, angb_teil1)
    erzeugen_vorpr_teil_2(liste_seiten_teil2, angb_teil2)

# Hier werden Aufgabenstellung für die mündliche Prüfung erzeugt
def muendliche_pruefung(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb, clean_tex=True):

    # Aufgabenblatt
    def Aufgaben(liste_aufg_lsg_teil1, angb):
        Aufgabe = Document(geometry_options=geometry_options)
        packages(Aufgabe)
        schuljahr, pruefungsfach, lehrkraft, vorschlag, thema_1, thema_2 = \
            (angb[0], angb[1], angb[2], angb[3], angb[4], angb[5])
        # Kopf erste Seite
        with Aufgabe.create(Figure(position='h')) as kopf:
            kopf.add_image('../img/kopfzeile.png', width='480px')

        # Tabelle erste Seite
        table1 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
        table1.add_row((MultiColumn(2, align='c',
                                    data=MediumText(bold(f'Mündliche Abiturprüfung im Fach '
                                                    f'Mathematik des Schuljahres {schuljahr}'))),))
        table1.add_row((MultiColumn(2, align='c', data=MediumText(bold(str(pruefungsfach)))),))
        table1.add_empty_row()
        table1.add_row(MediumText('Prüfung:'), MediumText(f'Vorschlag {vorschlag}'))
        table1.add_row(MediumText('Lehrkraft:'), MediumText(str(lehrkraft)))
        table1.add_row(MediumText('Hilfsmittel:'), MediumText('Tafelwerk und Taschenrechner'))
        table1.add_row(MediumText('Bearbeitungszeit:'), MediumText('30 min'))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='l', data=MediumText(bold(f'Thema: {thema_1}'))),))
        table1.add_hline(1, 2)

        Aufgabe.append(table1)
        Aufgabe.append(' \n\n\n')

        for element in liste_aufg_lsg_teil1:
            Aufgabe.extend(element[0])

        Aufgabe.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - Aufgaben {vorschlag}', clean_tex=clean_tex)

    # Fragen für das Prüfungsgespräch der mündlichen Prüfung
    def pruefungsfragen(liste_aufg_lsg_teil2, angb):
        Aufgabe = Document(geometry_options=geometry_options)
        packages(Aufgabe)
        schuljahr, pruefungsfach, lehrkraft, vorschlag, thema_1, thema_2 =\
            (angb[0], angb[1], angb[2], angb[3], angb[4], angb[5])
        # Kopf erste Seite
        with Aufgabe.create(Figure(position='h')) as kopf:
            kopf.add_image('../img/kopfzeile.png', width='480px')

        # Tabelle erste Seite
        table1 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
        table1.add_row((MultiColumn(2, align='c',
                                    data=MediumText(bold(f'Mündliche Abiturprüfung im Fach '
                                                         f'Mathematik des Schuljahres {schuljahr}'))),))
        table1.add_row((MultiColumn(2, align='c', data=MediumText(bold(str(pruefungsfach)))),))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='c',
                                    data=LargeText(bold(f'Fragen zum Prüfungsgespräch - Vorschlag {vorschlag}'))),))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='l', data=MediumText(bold(f'Thema: {thema_2}'))),))
        table1.add_hline(1, 2)

        Aufgabe.append(table1)
        Aufgabe.append(' \n\n')
        Aufgabe.append(' \n\n')

        for element in liste_aufg_lsg_teil2:
            Aufgabe.extend(element[0])
            Aufgabe.append(NewPage())

        Aufgabe.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - Fragen {vorschlag}', clean_tex=clean_tex)

    def Erwartungshorizont(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb):
        schuljahr, pruefungsfach, lehrkraft, vorschlag, thema_1, thema_2 =\
            (angb[0], angb[1], angb[2], angb[3], angb[4], angb[5])

        # Erwartungshorizont
        Loesung = Document(geometry_options=geometry_options)
        packages(Loesung)

        # Lösung Teil 1
        table2 = Tabular(' p{1.5cm} p{15cm}', row_height=1.5)
        table2.add_row(MediumText(bold(f'Teil I')), MediumText(bold(f'EWH zum Thema {thema_1} - {vorschlag}')))
        table2.add_hline(1, 2)
        table2.add_empty_row()

        Loesung.append(table2)

        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        for element in liste_aufg_lsg_teil1:
            Loesung.extend(element[1])

        Loesung.append(NewPage())

        # Lösung Teil 2
        table3 = Tabular(' p{1.5cm} p{15cm}', row_height=1.5)
        table3.add_row(MediumText(bold(f'Teil II')), MediumText(bold(f'EWH zum Thema {thema_2} - {vorschlag}')))
        table3.add_hline(1, 2)
        table3.add_empty_row()

        Loesung.append(table3)

        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        for element in liste_aufg_lsg_teil2:
            Loesung.extend(element[1])

        Loesung.append(NewPage())

        # Lösung Teil 2
        table4 = Tabular(' p{16.5cm}', row_height=1.5)
        table4.add_row(MediumText(bold(f'Auswertung der mündlichen Prüfung {vorschlag}')))
        table4.add_hline()
        table4.add_empty_row()
        Loesung.append(table4)
        Loesung.append(' \n\n')
        Loesung.append(MediumText('erzielte Leistungen in der Präsentation: \n\n'))

        # Auswertungsseite
        # erstellen der Tabelle zur Punkteübersicht
        liste_punkte = angb[-1]
        liste_bez = angb[-2]
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        liste_punkte.append(str(Punkte))
        anzahl_spalten = len(liste_punkte)
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z2.append('')

        spalten = '|'
        for p in liste_punkte:
            spalten += 'c|'

        table5 = Tabular(spalten, row_height=1.2)
        table5.add_hline()
        table5.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben in Teil I'),))
        table5.add_hline()
        table5.add_row(liste_bez)
        table5.add_hline()
        table5.add_row(liste_punkte)
        table5.add_hline()
        table5.add_row(liste_ergebnis_z1)
        table5.add_row(liste_ergebnis_z2)
        table5.add_hline()

        Loesung.append(table5)
        Loesung.append(' \n\n')
        Loesung.append(' \n\n')
        Loesung.append(MediumText('Im Prüfungsvortrag wurden ____% der Leistung erreicht \n\n'))

        Loesung.append(' \n\n')
        Loesung.append(' \n\n')
        Loesung.append(MediumText('erzielte Leistungen im Prüfungsgespräch: \n\n'))

        # erstellen der Tabelle zur Punkteübersicht
        liste_punkte = angb[-1]
        liste_bez = angb[-2]
        liste_bez.append('')
        liste_punkte.append('')
        anzahl_spalten = len(liste_punkte)
        liste_gewaehlt = ['gewählt']
        for p in range(anzahl_spalten - 2):
            liste_gewaehlt.append(NoEscape(r'$  \square $'))
        liste_gewaehlt.append('Summe')
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z2.append('')

        spalten = '|'
        for p in liste_punkte:
            spalten += 'c|'

        table6 = Tabular(spalten, row_height=1.2)
        table6.add_hline()
        table6.add_row((MultiColumn(anzahl_spalten, align='|c|',
                                    data='Punkteverteilung aller Aufgaben des Prüfungsgespräches'),))
        table6.add_hline()
        table6.add_row(liste_bez)
        table6.add_row(liste_gewaehlt)
        table6.add_hline()
        table6.add_row(liste_punkte)
        table6.add_hline()
        table6.add_row(liste_ergebnis_z1)
        table6.add_row(liste_ergebnis_z2)
        table6.add_hline()

        Loesung.append(table6)
        Loesung.append(' \n\n')
        Loesung.append(' \n\n')
        Loesung.append(MediumText('Im Prüfungsgespräch wurden ____% der Leistung erreicht \n\n'))

        Loesung.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - EWH {vorschlag}', clean_tex=clean_tex)


    Aufgaben(liste_aufg_lsg_teil1, angb)
    pruefungsfragen(liste_aufg_lsg_teil2, angb)
    Erwartungshorizont(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb)

# Hier wird eine Klausur erzeugt
def klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex=True):
    def erzeugen_kl_teil_1(liste_seiten_teil1, angb_teil1):
        Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema =\
            (angb_teil1[0], angb_teil1[1], angb_teil1[2], angb_teil1[3], angb_teil1[4], angb_teil1[5],
             angb_teil1[6], angb_teil1[7], angb_teil1[8])
        in_tagen, liste_bez, liste_punkte = angb_teil1[9], angb_teil1[10], angb_teil1[11]
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')

        # erstellen der Tabelle zur Punkteübersicht
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        liste_punkte.append(str(Punkte))
        anzahl_spalten = len(liste_punkte)
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z2.append('')

        spalten = '|c|'
        for step in range(len(liste_punkte) - 2):
            spalten += 'p{0.5 cm}|'
        spalten += 'c|'

        table3 = Tabular(spalten, row_height=1.2)
        table3.add_hline()
        table3.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben in Teil I'),))
        table3.add_hline()
        table3.add_row(liste_bez)
        table3.add_hline()
        table3.add_row(liste_punkte)
        table3.add_hline()
        table3.add_row(liste_ergebnis_z1)
        table3.add_row(liste_ergebnis_z2)
        table3.add_hline()

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_1():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            with Aufgabe.create(Figure(position='h')) as kopf:
                kopf.add_image('../img/kopfzeile.png', width='480px')
            # Tabelle erste Seite
            table1 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
            table1.add_row((MultiColumn(2, align='l',
                                        data=MediumText(bold(f'Klausur im {Semester}. Semester der {Phase} am {Datum}'))),))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='c', data=HugeText(bold('Mathematik'))),))
            table1.add_row((MultiColumn(2, align='c', data=MediumText(bold(Kurs))),))
            table1.add_empty_row()
            table1.add_row(MediumText('Vorname, Name:'), '')
            table1.add_hline(2, 2, color='gray')
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgaben'))),))
            table1.add_hline(1, 2)
            table1.add_row(MediumText('Hilfsmittel:'),
                           MediumText('Formelübersicht (nach IQB) und zugelassener Taschenrechner'))
            table1.add_row(MediumText('Bearbeitungszeit:'), MediumText(str(Gesamtzeit) + ' min'))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='r', data=MediumText(bold('Teil I'))),))
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenstellung 1'))),))
            table1.add_row(MediumText('Thema/Inhalt:'), MediumText('Hilfsmittelfreier Teil'))
            table1.add_row(MediumText('Hinweis:'),
                           MediumText(f'Die Aufgabenstellung und die Lösung zum hilfsmittelfreien Teil müssen '
                                      f'spätestens nach {Zeithmft} Minuten abgegeben werden. Eine frühere Abgabe '
                                      f'ist möglich. Nach Abgabe dieser Aufgabenstellung dürfen '
                                      f'die Hilfsmittel verwendet werden.'))
            table1.add_empty_row()
            table1.add_row('', MediumText(f'Anzahl der abgegebenen Blätter: ____'))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='r', data=MediumText(bold('Teil II'))),))
            table1.add_hline(1, 2)
            table1.add_row((MultiColumn(2, align='l', data='Im Teil 2 des Aufgabenvorschlages sind enthalten:'),))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenstellung 2'))),))
            table1.add_row(MediumText('Thema/Inhalt:'), MediumText(Thema))
            table1.add_row(MediumText('Hinweis:'), MediumText('Hier dürfen Sie alle Hilfsmittel verwenden.'))
            table1.add_empty_row()
            table1.add_row('', MediumText(f'Anzahl der abgegebenen Blätter: ____'))
            table1.add_empty_row()
            table1.add_empty_row()
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l',
                                        data=MediumText(bold(f'Insgesamt __ von {Gesamtpunktzahl} Punkten'
                                        f' und damit __ Notenpunkte bzw. Note __'))),))

            Aufgabe.append(table1)

            Aufgabe.append(' \n\n')
            Aufgabe.append(NewPage())

            table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
            table2.add_row(MediumText(bold(f'Teil I')),MediumText(bold(f'Hilfsmittelfreier Teil {Gruppe}')))
            table2.add_hline(1, 2)
            table2.add_empty_row()

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            for element in liste_seiten_teil1:
                Aufgabe.append(table2)
                Aufgabe.append(' \n\n')
                Aufgabe.extend(element[0])
                if element != liste_seiten_teil1[-1]:
                    Aufgabe.append(NewPage())


            Aufgabe.append(' \n\n')
            Aufgabe.append(table3)

            Aufgabe.generate_pdf(f'pdf/Kl. {Klasse} - Klausur im {Semester}. Semester - Teil I {Gruppe}',
                                 clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_1():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f' Lösung für Teil I {Gruppe} der Klausur im {Semester}. Semester \n\n'
                                          f'der {Phase} am {Datum}')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt

            for element in liste_seiten_teil1:
                Loesung.extend(element[1])

            Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

            Loesung.generate_pdf(f'pdf/Kl. {Klasse} - Klausur im {Semester}. Semester - EWH Teil I {Gruppe}',
                                 clean_tex=clean_tex)

        # Druck der Seiten
        Teil_1()
        EWH_Teil_1()

    def erzeugen_kl_teil_2(liste_seiten_teil2, angb_teil2):
        Kurs, Klasse, Gruppe, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema =\
            (angb_teil2[0], angb_teil2[1], angb_teil2[2], angb_teil2[3],
             angb_teil2[4], angb_teil2[5], angb_teil2[6], angb_teil2[7], angb_teil2[8])
        in_tagen, liste_bez, liste_punkte = angb_teil2[9], angb_teil2[10], angb_teil2[11]
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')

        # erstellen der Tabelle zur Punkteübersicht
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        liste_punkte.append(str(Punkte))
        anzahl_spalten = len(liste_punkte)
        liste_ergebnis_z1 = ['erhaltene']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['Punkte']
        for p in range(anzahl_spalten - 1):
            liste_ergebnis_z2.append('')
        spalten = '|c|'
        for step in range(len(liste_punkte) - 2):
            spalten += 'p{0.5 cm}|'
        spalten += 'c|'

        table3 = Tabular(spalten, row_height=1.2)
        table3.add_hline()
        table3.add_row((MultiColumn(anzahl_spalten, align='|c|', data='Punkteverteilung aller Aufgaben in Teil II'),))
        table3.add_hline()
        table3.add_row(liste_bez)
        table3.add_hline()
        table3.add_row(liste_punkte)
        table3.add_hline()
        table3.add_row(liste_ergebnis_z1)
        table3.add_row(liste_ergebnis_z2)
        table3.add_hline()

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_2():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
            table2.add_row(MediumText(bold(f'Teil II')),
                           MediumText(bold(f'Aufgaben mit zugelassenen Hilfsmitteln {Gruppe}')))
            table2.add_hline(1, 2)
            table2.add_empty_row()

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            for element in liste_seiten_teil2:
                Aufgabe.append(table2)
                Aufgabe.append(' \n\n')
                Aufgabe.extend(element[0])
                if element != liste_seiten_teil2[-1]:
                    Aufgabe.append(NewPage())

            Aufgabe.append(' \n\n')
            Aufgabe.append(table3)

            Aufgabe.generate_pdf(f'pdf/Kl. {Klasse} - Klausur im {Semester}. Semester - Teil II {Gruppe}',
                                 clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_2():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f' Lösung für Teil II {Gruppe} der Klausur im {Semester}. Semester \n\n'
                                          f'der {Phase} am {Datum}')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
            for element in liste_seiten_teil2:
                Loesung.extend(element[1])


            Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

            Loesung.generate_pdf(f'pdf/Kl. {Klasse} - Klausur im {Semester}. Semester - EWH Teil II {Gruppe}',
                                 clean_tex=clean_tex)

        # Druck der Seiten
        Teil_2()
        EWH_Teil_2()

    erzeugen_kl_teil_1(liste_seiten_teil1, angb_teil1)
    erzeugen_kl_teil_2(liste_seiten_teil2, angb_teil2)

# Hier wird eine Vorbiturklausur erzeugt
def vorabiturklausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2, clean_tex=True):
    def erzeugen_kl_teil_1(liste_seiten_teil1, angb_teil1):
        Kurs, in_tagen, liste_bez, liste_punkte = angb_teil1[0], angb_teil1[1], angb_teil1[2], angb_teil1[3]
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')

        # erstellen der Tabelle zur Punkteübersicht
        liste_punkte = angb_teil1[-1]
        liste_bez = angb_teil1[-2]
        liste_bez.append('')
        liste_bez.insert(0,'')
        liste_punkte.append('')
        liste_punkte.insert(0,MediumText(bold('Auswertung für Teil I ')))
        liste_gewaehlt = ['','gewählt']
        for p in range(len(liste_punkte) - 3):
            if Kurs == 'Grundkurs':
                if p < 3:
                    liste_gewaehlt.append(NoEscape(r'$ \surd $'))
                else:
                    liste_gewaehlt.append(NoEscape(r'$ \square $'))
            else:
                if p < 4:
                    liste_gewaehlt.append(NoEscape(r'$ \surd $'))
                else:
                    liste_gewaehlt.append(NoEscape(r'$ \square $'))
        liste_gewaehlt.append('Summe')
        liste_ergebnis_z1 = ['','erhaltene']
        for p in range(len(liste_punkte) - 2):
            liste_ergebnis_z1.append('')
        liste_ergebnis_z2 = ['','Punkte']
        for p in range(len(liste_punkte) - 2):
            liste_ergebnis_z2.append('')

        spalten = ''
        for element in liste_punkte:
            spalten += 'c|'
        table3 = Tabular(spalten, row_height=1.2)
        table3.add_hline(2)
        table3.add_row('',(MultiColumn(len(liste_punkte) - 1, align='|c|',
                                    data='Punkteverteilung aller Aufgaben')))
        table3.add_hline(2)
        table3.add_row(liste_bez)
        table3.add_row(liste_gewaehlt)
        table3.add_hline(2)
        table3.add_row(liste_punkte)
        table3.add_hline(2)
        table3.add_row(liste_ergebnis_z1)
        table3.add_row(liste_ergebnis_z2)
        table3.add_hline(2)


        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_1():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            with Aufgabe.create(Figure(position='h')) as kopf:
                kopf.add_image('../img/kopfzeile.png', width='480px')
            # Tabelle erste Seite
            table1 = Tabular(' p{5cm} p{11cm}', row_height=1.5)
            table1.add_row((MultiColumn(2, align='l',
                                        data=MediumText(bold(f'Klausur im 3. Semester der Qualifikationsphase am {Datum}'))),))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='c', data=HugeText(bold('Mathematik'))),))
            table1.add_row((MultiColumn(2, align='c', data=MediumText(bold(Kurs))),))
            table1.add_empty_row()
            table1.add_row(MediumText('Vorname, Name:'), '')
            table1.add_hline(2, color='gray')
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenvorschlag Teil I'))),))
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Thema/Inhalt:')),
                           MediumText('hilfsmittelfreie Aufgaben'))
            table1.add_row(MediumText(bold('Hilfsmittel:')),
                           MediumText('Nachschlagewerk zur Rechtschreibung der deutschen Sprache, Zeichenwerkzeuge'))
            table1.add_row(MediumText(''),MediumText(bold('keine weiteren Hilfsmittel')))
            table1.add_empty_row()
            if Kurs == 'Grundkurs':
                table1.add_row(MediumText(bold('Bearbeitungszeit:')),
                        MediumText('Für die Bearbeitung stehen maximal 90 Minuten zur Verfügung. '
                                   'Sobald die Aufgabenstellungen und die Bearbeitungen zum Teil I abgegeben '
                                   'wurden, werden die Hilfsmittel für Teil II ausgegeben, auch wenn dies bereits '
                                   'vor Ablauf der 90 Minuten erfolgt.'))
            else:
                table1.add_row(MediumText(bold('Bearbeitungszeit:')),
                               MediumText('Für die Bearbeitung stehen maximal 100 Minuten zur Verfügung. '
                                          'Sobald die Aufgabenstellungen und die Bearbeitungen zum Teil I abgegeben '
                                          'wurden, werden die Hilfsmittel für Teil II ausgegeben, auch wenn dies bereits '
                                          'vor Ablauf der 100 Minuten erfolgt.'))

            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenwahl'))),))
            table1.add_hline(1, 2)
            table1.add_empty_row()
            if Kurs == 'Grundkurs':
                table1.add_row(MediumText(bold('Pflichtaufgaben')),
                               MediumText('Die Aufgaben 1, 2 und 3 müssen bearbeitet werden.'))
                table1.add_row(MediumText(bold('Wahlaufgaben:')),
                               MediumText('Von den Aufgaben 4, 5 und 6 muss genau eine bearbeitet werden.'))
                table1.add_row('', MediumText(bold(NoEscape(r'$ \square $' + ' Aufgabe 4  '
                                                            + r'$ \square $' + ' Aufgabe 5 ' + r'$ \square $'
                                                            + ' Aufgabe 6'))))

                table1.add_empty_row()
                table1.add_row(MediumText(bold('Wahlaufgaben:')),
                               MediumText('Von den Aufgaben 7, 8 und 9 muss genau eine bearbeitet werden.'))
                table1.add_row('', MediumText(bold(NoEscape(r'$ \square $' + ' Aufgabe 7 '
                                                            + r'$ \square $' + ' Aufgabe 8 ' + r'$ \square $'
                                                            + ' Aufgabe 9'))))

            else:
                table1.add_row(MediumText(bold('Pflichtaufgaben')),
                               MediumText('Die Aufgaben 1, 2, 3 und 4 müssen bearbeitet werden.'))
                table1.add_empty_row()
                table1.add_row(MediumText(bold('Wahlaufgaben:')),
                               MediumText('Von den Aufgaben 5 bis 10 müssen genau zwei Aufgaben bearbeitet werden.'))
                table1.add_row(MediumText(bold('')),
                               MediumText(bold(NoEscape(r'$ \square $' + ' Aufgabe 5 ' + r'$ \square $'
                                                        + ' Aufgabe 6 ' + r'$ \square $' + ' Aufgabe 7'))))
                table1.add_row(MediumText(bold('')),
                               MediumText(bold(NoEscape(r'$ \square $' + ' Aufgabe 8 ' + r'$ \square $'
                                                        + ' Aufgabe 9 ' + r'$ \square $' + ' Aufgabe 10'))))

            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row(MediumText('Anzahl abgegebene Blätter:'),'____________')

            Aufgabe.append(table1)
            Aufgabe.append(' \n\n \n\n')
            Aufgabe.append(table3)
            Aufgabe.append(' \n\n')
            Aufgabe.append(NewPage())

            table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
            table2.add_row(MediumText(bold(f'Teil I')),MediumText(bold(f'hilfsmittelfreie Aufgaben')))
            table2.add_hline(1, 2)
            table2.add_empty_row()

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            for element in liste_seiten_teil1:
                Aufgabe.append(table2)
                Aufgabe.append(' \n\n')
                Aufgabe.extend(element[0])
                if element != liste_seiten_teil1[-1]:
                    Aufgabe.append(NewPage())


            Aufgabe.append(' \n\n')

            Aufgabe.generate_pdf(f'pdf/Kl. 13 - Klausur im 3. Semester - Teil I', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_1():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            Loesung.append(LargeText(bold(f' Lsg für Teil I der Kl. im 3. Semester am {Datum}')))

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt

            for element in liste_seiten_teil1:
                Loesung.extend(element[1])


            Loesung.generate_pdf(f'pdf/Kl. 13 - Klausur im 3. Semester - EWH Teil I', clean_tex=clean_tex)

        # Druck der Seiten
        Teil_1()
        EWH_Teil_1()

    def erzeugen_kl_teil_2(liste_seiten_teil2, angb_teil2):
        Kurs, in_tagen, liste_bez, liste_punkte = angb_teil2[0], angb_teil2[1], angb_teil2[2], angb_teil2[3]
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d. %B %Y')
        print(f'\033[38;2;100;141;229m\033[1m\033[0m')
        themen = ['1. Wahlaufgabe zur Analysis', '2. Wahlaufgabe zur Analysis', 'Aufgaben zur analytischen Geometrie',
                  'Aufgaben zur Stochastik']

        # der Teil in dem die PDF-Datei erzeugt wird
        @timer
        def Teil_2():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            with Aufgabe.create(Figure(position='h')) as kopf:
                kopf.add_image('../img/kopfzeile.png', width='480px')
            # Tabelle erste Seite
            table1 = Tabular(' p{5cm} p{11cm}', row_height=1.5)
            table1.add_row((MultiColumn(2, align='l',
                                        data=MediumText(
                                            bold(f'Klausur im 3. Semester der Qualifikationsphase am {Datum}'))),))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='c', data=HugeText(bold('Mathematik'))),))
            table1.add_row((MultiColumn(2, align='c', data=MediumText(bold(Kurs))),))
            table1.add_empty_row()
            table1.add_row(MediumText('Vorname, Name:'), '')
            table1.add_hline(2, 2, color='gray')
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenvorschlag Teil II'))),))
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Hilfsmittel:')),
                           MediumText('Nachschlagewerk zur Rechtschreibung der deutschen Sprache, '
                                      'Standard-Zeichenwerkzeuge, Mathematische Formelsammlung (IQB), Taschenrechner, '
                                      'die nicht programmierbar und nicht grafikfähig sind und nicht über '
                                      'Möglichkeiten der numerischen Differenziation oder Integration oder des '
                                      'automatisierten Lösens von Gleichungen verfügen'))
            table1.add_empty_row()
            if Kurs == 'Grundkurs':
                table1.add_row(MediumText(bold('Gesamtbearbeitungszeit:')),
                               MediumText('285 Minuten (davon maximal 90 Minuten für Teil I)'))
            else:
                table1.add_row(MediumText(bold('Gesamtbearbeitungszeit:')),
                               MediumText('330 Minuten (davon maximal 100 Minuten für Teil I)'))
            table1.add_empty_row()
            table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenwahl'))),))
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Analysis:')),
                           MediumText('Von den beiden Aufgaben zur Analysis muss eine bearbeitet werden'))
            table1.add_row('',MediumText(bold(NoEscape('gewählt wurde: ' + r'$ \square $' + ' Aufgabe 1  bzw.  '
                                                                 + r'$ \square $' + ' Aufgabe 2'))))
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Analytische Geometrie:')),
                           MediumText('Hier müssen alle Aufgaben bearbeitet werden.'))
            table1.add_empty_row()
            table1.add_row(MediumText(bold('Stochastik:')),
                           MediumText('Hier müssen alle Aufgaben bearbeitet werden.'))
            table1.add_empty_row()
            table1.add_hline(1, 2)
            table1.add_empty_row()
            table1.add_row(MediumText('Anzahl abgegebene Blätter:'),'____________')

            table4 = Tabular('c|c|c|c|c|c|c|')
            table4.add_hline(2)
            table4.add_row('',(MultiColumn(6, align='|c|', data=MediumText(bold(f'Punkteverteilung aller Aufgaben')))))
            table4.add_hline(2)
            table4.add_row('','Aufgaben','Teil I', 'Analysis', 'Geometrie', 'Stochastik','Summe')
            table4.add_hline(2)
            table4.add_row(MediumText(bold('Auswertung der Klausur ')),'Punkte','', '', '', '','')
            table4.add_hline(2)
            table4.add_row('','erhalten','','','','','')
            table4.add_hline(2)
            table4.add_row((MultiColumn(7, align='l', data=MediumText(bold(f''))),))
            table4.add_row((MultiColumn(7, align='c', data=MediumText(bold(f'Note bzw. Notenpunkte: '))),))

            Aufgabe.append(table1)
            Aufgabe.append(' \n\n')
            Aufgabe.append(' \n\n')
            Aufgabe.append(table4)

            Aufgabe.append(NewPage())
            i = 0

            for element in themen:

                # Tabelle für Kopfzeile
                table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
                table2.add_row(MediumText(bold(f'Teil II')),
                               MediumText(bold(element)))
                table2.add_hline(1, 2)
                table2.add_empty_row()

                # erstellen der Tabelle zur Punkteübersicht
                Punkte = (sum(liste_punkte[i][1:]))
                liste_bez[i].append('Summe')
                liste_punkte[i].append(str(Punkte))
                anzahl_spalten = len(liste_punkte[i])
                spalten = '|'
                for p in liste_punkte[i]:
                    spalten += 'c|'
                liste_ergebnis_z1 = ['erhaltene']
                for p in range(anzahl_spalten - 1):
                    liste_ergebnis_z1.append('')
                liste_ergebnis_z2 = ['Punkte']
                for p in range(anzahl_spalten - 1):
                    liste_ergebnis_z2.append('')

                table3 = Tabular(spalten, row_height=1.2)
                table3.add_hline()
                table3.add_row((MultiColumn(anzahl_spalten, align='|c|',
                                            data='Punkteverteilung der Aufgabe'),))
                table3.add_hline()
                table3.add_row(liste_bez[i])
                table3.add_hline()
                table3.add_row(liste_punkte[i])
                table3.add_hline()
                table3.add_row(liste_ergebnis_z1)
                table3.add_row(liste_ergebnis_z2)
                table3.add_hline()

                # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
                for aufgaben in liste_seiten_teil2[i]:
                    Aufgabe.append(table2)
                    Aufgabe.append(' \n\n')
                    Aufgabe.extend(aufgaben[0])
                    Aufgabe.append(' \n\n')
                    Aufgabe.append(' \n\n')
                    Aufgabe.append(table3)
                    if element != liste_seiten_teil2[i][-1]:
                        Aufgabe.append(NewPage())
                i += 1

            Aufgabe.generate_pdf(f'pdf/Kl. 13 - Klausur im 3. Semester - Teil II', clean_tex=clean_tex)

        # Erwartungshorizont
        @timer
        def EWH_Teil_2():
            Loesung = Document(geometry_options=geometry_options)
            packages(Loesung)

            # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
            i = 0
            for thema in themen:
                Loesung.append(LargeText(bold(f' Lsg für Teil II der Kl. im 3. Semester am {Datum} \n\n'
                                              f'{thema}')))
                for element in liste_seiten_teil2[i]:
                    Loesung.extend(element[1])
                Loesung.append(NewPage())
                i += 1

            Loesung.generate_pdf(f'pdf/Kl. 13 - Klausur im 3. Semester - EWH Teil II', clean_tex=clean_tex)

        # Druck der Seiten
        Teil_2()
        EWH_Teil_2()

    erzeugen_kl_teil_1(liste_seiten_teil1, angb_teil1)
    erzeugen_kl_teil_2(liste_seiten_teil2, angb_teil2)

