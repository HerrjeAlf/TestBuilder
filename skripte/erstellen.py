import datetime
import os
import string
from pylatex import (Document, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Package, HugeText, MultiRow, NoEscape)
from pylatex.utils import bold
from skripte.funktionen import *
from skripte.plotten import *

# Sorgt dafür, dass mögliche benötigte Ordner erstellt werden
try:
    os.mkdir('pdf')
    os.mkdir('img/temp')
except FileExistsError:
    pass

geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}

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
                with Aufgabe.create(Figure(position='h!')) as graph:
                    graph.add_image(f'../img/temp/{aufgabe[2][i]}', width='250px', placement=None)
                Aufgabe.append(SmallText('Abbildung ' + str(i+1) + ' \n\n'))
                i += 1
            elif 'neueSeite' in elements:
                Aufgabe.append(NewPage())
            elif '3dim_Koordinatensystem' in elements:
                with Aufgabe.create(Figure(position='h!')) as graph:
                    graph.add_image(f'../img/{elements}.png', width='300px')
            else:
                Aufgabe.append(elements)

    for loesung in aufgaben:
        i = 0
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Figure' in elements:
                with Loesung.create(Figure(position='h!')) as graph:
                    graph.add_image(f'../img/temp/{loesung[3][i]}', width='250px')
                i += 1
            elif 'neueSeite' in elements:
                Loesung.append(NewPage())
            elif '3dim_Koordinatensystem' in elements:
                with Loesung.create(Figure(position='h!')) as graph:
                    graph.add_image(f'../img/{elements}.png', width='300px')
            else:
                Loesung.append(elements)

    return Aufgabe, Loesung

# hier wird ein Test erzeugt
def test_erzeugen(liste_seiten, angaben, anzahl=1, probe=False):
    def erzeugen_test(Teil, liste_seiten, angaben):
        schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel =\
            (angaben[0], angaben[1], angaben[2], angaben[3], angaben[4], angaben[5], angaben[6], angaben[7])
        in_tagen, liste_bez, liste_punkte = angaben[8], angaben[9], angaben[10]
        print(f'\033[38;2;100;141;229m\033[1m{Teil}\033[0m')
        Datum = (datetime.date.today() + datetime.timedelta(days=in_tagen)).strftime('%d.%m.%Y')

        # erstellen der Tabelle zur Punkteübersicht
        print(liste_punkte)
        Punkte = (sum(liste_punkte[1:]))
        liste_bez.append('Summe')
        liste_punkte.append(Punkte)
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
        def Hausaufgabenkontrolle():
            Aufgabe = Document(geometry_options=geometry_options)
            packages(Aufgabe)

            # Kopf erste Seite
            table1 = Tabular('|p{1.2cm}|p{2.5cm}|p{2.5cm}|p{2.5cm}|p{2cm}|p{3cm}|', row_height=1.2)
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

            # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
            k = 0
            for element in liste_seiten:
                Aufgabe.extend(element[0])
                Aufgabe.append(NewPage())

            if len(liste_seiten) % 2 == 0:
                Aufgabe.append('für Notizen und Rechnungen:')
                Aufgabe.append(NewPage())

            Aufgabe.append(LargeText(bold(Teil + ' - bearbeitet von:')))

            Aufgabe.append('\n\n')
            Aufgabe.append('\n\n')
            Aufgabe.append(table2)

            Aufgabe.generate_pdf(f'pdf/Ma {Klasse} - {Art} {Teil}', clean_tex=true)

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

            Loesung.generate_pdf(f'pdf/Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)

        # Druck der Seiten
        Hausaufgabenkontrolle()
        Erwartungshorizont()
        del liste_bez[1:]
        del liste_punkte[1:]

    alphabet = string.ascii_uppercase
    if probe:
        erzeugen_test(f'Probe {anzahl + 1:02d}', liste_seiten, angaben)
    else:
        erzeugen_test(f'Gr. {alphabet[anzahl]}', liste_seiten, angaben)
    print()  # Abstand zwischen den Arbeiten (im Terminal)


# Hier wird eine Klausur erzeugt
def klausur(liste_seiten_teil1, angb_teil1, liste_seiten_teil2, angb_teil2):
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

        spalten = '|'
        for p in liste_punkte:
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

            Aufgabe.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - Teil I {Gruppe}', clean_tex=true)

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

            Loesung.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - EWH Teil I {Gruppe}', clean_tex=true)

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
        spalten = '|'
        for p in liste_punkte:
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

            Aufgabe.append(table3)

            Aufgabe.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - Teil II {Gruppe}', clean_tex=true)

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

            Loesung.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - EWH Teil II {Gruppe}', clean_tex=true)

        # Druck der Seiten
        Teil_2()
        EWH_Teil_2()

    erzeugen_kl_teil_1(liste_seiten_teil1, angb_teil1)
    erzeugen_kl_teil_2(liste_seiten_teil2, angb_teil2)

# Hier werden Aufgabenstellung für die mündliche Prüfung erzeugt

def muendliche_pruefung(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb):

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

        Aufgabe.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - Aufgaben {vorschlag}', clean_tex=true)

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

        Aufgabe.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - Fragen {vorschlag}', clean_tex=true)

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
        liste_punkte = angb[-3]
        liste_bez = angb[-4]
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

        Loesung.generate_pdf(f'pdf/mündliche Prüfung {schuljahr} - EWH {vorschlag}', clean_tex=true)


    Aufgaben(liste_aufg_lsg_teil1, angb)
    pruefungsfragen(liste_aufg_lsg_teil2, angb)
    Erwartungshorizont(liste_aufg_lsg_teil1, liste_aufg_lsg_teil2, angb)
