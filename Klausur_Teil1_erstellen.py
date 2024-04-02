import datetime
import string

from pylatex import (Document, SmallText, HugeText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure,
                     MultiColumn, Package)
from pylatex.utils import bold

from funktionen import *
from plotten import *

geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}

def seite(aufgaben):
    Aufgabe = Document(geometry_options=geometry_options)
    Loesung = Document(geometry_options=geometry_options)

    for aufgabe in aufgaben:
        k = 0
        for elements in aufgabe[0]:
            if '~' in elements:
                with Aufgabe.create(Alignat(aligns=1, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Abbildung' in elements:
                Aufgabe.append(elements)
                with Aufgabe.create(Figure(position='h!')) as graph:
                    graph.add_image(aufgabe[2][k], width='200px')
            else:
                Aufgabe.append(elements)
            k += 1

    for loesung in aufgaben:
        k = 0
        for elements in loesung[1]:
            if '~' in elements:
                with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                    agn.append(elements)
            elif 'Abbildung' in elements:
                with Loesung.create(Figure(position='h!')) as graph:
                    graph.add_image(loesung[3][k], width='300px')
            else:
                Loesung.append(elements)
            k += 1


    return Aufgabe, Loesung

def erzeugen_kl_hmft(liste_seiten, angaben):
    Kurs, Klasse, Semester, Gesamtzeit, Zeithmft, Phase = (angaben[0], angaben[1], angaben[2], angaben[3],
                                                           angaben[4], angaben[5])
    in_tagen, liste_bez, liste_punkte = angaben[6], angaben[7], angaben[8]
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
    def klausur():
        Aufgabe = Document(geometry_options=geometry_options)
        Aufgabe.packages.append(Package('amsfonts'))
        # Kopf erste Seite
        with Aufgabe.create(Figure(position='h')) as kopf:
            kopf.add_image('img/kopfzeile.png', width='480px')
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
        table1.add_row((MultiColumn(2, align='l', data=MediumText(bold('Aufgaben'))),))
        table1.add_hline(1, 2)
        table1.add_row(MediumText('Hilfsmittel:'), 'Tafelwerk und Taschenrechner')
        table1.add_row(MediumText('Bearbeitungszeit:'), Gesamtzeit)

        Aufgabe.append(table1)
        Aufgabe.append(' \n\n')
        Aufgabe.append(NewPage())


        # hier werden die Aufgaben der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 1
        for element in liste_seiten:
            Aufgabe.extend(element[0])
            if k < len(liste_seiten):
                Aufgabe.append(NewPage())
            k += 1
        Aufgabe.append(' \n\n')
        Aufgabe.append(table2)

        Aufgabe.generate_pdf(f'Ma {Klasse} - Klausur Teil I', clean_tex=true)

    # Erwartungshorizont
    @timer
    def Erwartungshorizont():
        Loesung = Document(geometry_options=geometry_options)
        Loesung.packages.append(Package('amsfonts'))
        Loesung.append(LargeText(bold(f'Loesung für {Art} {Teil} \n\n {Titel} \n\n')))

        # hier werden die Lösungen der einzelnen Seiten an die Liste Aufgabe angehängt
        k = 0
        for element in liste_seiten:
            Loesung.extend(element[1])

        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.generate_pdf(f'Ma {Klasse} - {Art} {Teil} - Lsg', clean_tex=true)

    # Druck der Seiten
    klausur()
    # Erwartungshorizont()

