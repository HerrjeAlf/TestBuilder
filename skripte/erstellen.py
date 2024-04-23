import datetime
import os
import string
from pylatex import (Document, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Package, HugeText)
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
            else:
                Loesung.append(elements)



    return Aufgabe, Loesung

def erzeugen_test(Teil, liste_seiten, angaben):
    Kurs, Fach, Klasse, Lehrer, Art, Titel = angaben[0], angaben[1], angaben[2], angaben[3], angaben[4], angaben[5]
    in_tagen, liste_bez, liste_punkte = angaben[6], angaben[7], angaben[8]
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
        Aufgabe.packages.append(Package('amsfonts'))
        Aufgabe.packages.append(Package('bm'))

        # Kopf erste Seite
        table1 = Tabular('|p{1.2cm}|p{2.5cm}|p{2.5cm}|p{2.5cm}|p{2cm}|p{2cm}|', row_height=1.2)
        table1.add_row((MultiColumn(6, align='c', data=MediumText(bold('Torhorst - Gesamtschule'))),))
        table1.add_row((MultiColumn(6, align='c', data=SmallText(bold('mit gymnasialer Oberstufe'))),))
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
        Loesung.packages.append(Package('amsfonts'))
        Loesung.packages.append(Package('bm'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} - {Titel}')))

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


def pdf_erzeugen(liste_seiten, angaben, anzahl=1, probe=False):
    alphabet = string.ascii_uppercase
    if probe:
        erzeugen_test(f'Probe {anzahl + 1:02d}', liste_seiten, angaben)
    else:
        erzeugen_test(f'Gr. {alphabet[anzahl]}', liste_seiten, angaben)
    print()  # Abstand zwischen den Arbeiten (im Terminal)

def erzeugen_kl_teil_1(liste_seiten, angb_hmft):
    Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema = (angb_hmft[0],
    angb_hmft[1], angb_hmft[2], angb_hmft[3], angb_hmft[4], angb_hmft[5], angb_hmft[6], angb_hmft[7])
    in_tagen, liste_bez, liste_punkte = angb_hmft[8], angb_hmft[9], angb_hmft[10]
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
        Aufgabe.packages.append(Package('amsfonts'))
        Aufgabe.packages.append(Package('bm'))
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
        table1.add_row(MediumText('Hilfsmittel:'), MediumText('Tafelwerk und Taschenrechner'))
        table1.add_row(MediumText('Bearbeitungszeit:'), MediumText(str(Gesamtzeit) + ' min'))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='r', data=MediumText(bold('Teil I'))),))
        table1.add_hline(1, 2)
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenstellung 1'))),))
        table1.add_row(MediumText('Thema/Inhalt:'), MediumText('Hilfsmittelfreier Teil'))
        table1.add_row(MediumText('Hinweis:'), MediumText('Hier gibt es keine Wahlmöglichkeiten.'))
        table1.add_row('', MediumText(f'Die Aufgabenstellung und die Lösung zum hilfsmittelfreien Teil müssen'
                                      f' spätestens nach {Zeithmft} Minuten abgegeben werden. Eine frühere Abgabe ist'
                                      f' möglich. Nach Abgabe dieser Aufgabenstellung dürfen die Hilfsmittel'
                                      f' verwendet werden.'))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='r', data=MediumText(bold('Teil II'))),))
        table1.add_hline(1, 2)
        table1.add_row((MultiColumn(2, align='l', data='Im Teil 2 des Aufgabenvorschlages sind enthalten:'),))
        table1.add_empty_row()
        table1.add_row((MultiColumn(2, align='l', data=LargeText(bold('Aufgabenstellung 2'))),))
        table1.add_row(MediumText('Thema/Inhalt:'), MediumText(Thema))
        table1.add_row(MediumText('Hinweis:'), MediumText('Hier dürfen Sie alle Hilfsmittel verwenden.'))
        table1.add_empty_row()
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
        table2.add_row(MediumText(bold('Teil I')),MediumText(bold('Hilfsmittelfreier Teil')))
        table2.add_hline(1, 2)
        table2.add_empty_row()

        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 1
        for element in liste_seiten:
            Aufgabe.append(table2)
            Aufgabe.append(' \n\n')
            Aufgabe.extend(element[0])
            if k < len(liste_seiten):
                Aufgabe.append(NewPage())
            k += 1

        Aufgabe.append(' \n\n')
        Aufgabe.append(table3)

        Aufgabe.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - Teil I', clean_tex=true)

    # Erwartungshorizont
    @timer
    def EWH_Teil_1():
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.packages.append(Package('bm'))
        Loesung.append(LargeText(bold(f' Lösung für Teil I der Klausur im {Semester}. Semester \n\n'
                                      f'der {Phase} am {Datum}')))

        # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 0
        for element in liste_seiten:
            Loesung.extend(element[1])

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - EWH Teil I', clean_tex=true)

    # Druck der Seiten
    Teil_1()
    EWH_Teil_1()

def erzeugen_kl_teil_2(liste_seiten, angb):
    Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase, Gesamtpunktzahl, Thema = (angb[0], angb[1], angb[2], angb[3],
                                                                                   angb[4], angb[5], angb[6], angb[7])
    in_tagen, liste_bez, liste_punkte = angb[8], angb[9], angb[10]
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
        Aufgabe.packages.append(Package('amsfonts'))
        # Kopf erste Seite
        table2 = Tabular(' p{4cm} p{12cm}', row_height=1.5)
        table2.add_row(MediumText(bold('Teil II')),MediumText(bold('Aufgaben mit zugelassenen Hilfsmitteln')))
        table2.add_hline(1, 2)
        table2.add_empty_row()

        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 1
        for element in liste_seiten:
            Aufgabe.append(table2)
            Aufgabe.append(' \n\n')
            Aufgabe.extend(element[0])
            if k < len(liste_seiten):
                Aufgabe.append(NewPage())
            k += 1

        Aufgabe.append(' \n\n')
        Aufgabe.append(table3)

        Aufgabe.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester Teil II', clean_tex=true)

    # Erwartungshorizont
    @timer
    def EWH_Teil_2():
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f' Lösung für Teil I der Klausur im {Semester}. Semester \n\n'
                                      f'der {Phase} am {Datum}')))

        # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 0
        for element in liste_seiten:
            Loesung.extend(element[1])

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'pdf/Ma {Klasse} - Klausur im {Semester}. Semester - EWH Teil II', clean_tex=true)

    # Druck der Seiten
    Teil_2()
    EWH_Teil_2()


