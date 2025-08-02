"""
Example of optimized import usage in a temp file
"""
import os
from helpers import root_path

# Standard library imports
import random
import string

# Third-party imports (only what's needed)
from sympy import symbols, solve, Eq, diff
from pylatex import Document, MediumText, NewPage
from pylatex.utils import bold

# Custom imports (lazy loading)
from skripte.imports import get_numpy, get_matplotlib, cleanup_memory
from skripte.erstellen import seite, test_erzeugen

# Set working directory
os.chdir(root_path())

# Only import specific functions from Aufgaben
from Aufgaben import (
    rechtwinkliges_dreieck,
    verhaeltnisgleichgungen,
    kongruente_dreiecke
)

def create_test_with_memory_management():
    """Example function with proper memory management"""
    
    # Test configuration
    schule = 'Torhorst - Gesamtschule'
    schulart = 'mit gymnasialer Oberstufe'
    Kurs = 'Grundkurs'
    Fach = 'Mathematik'
    Klasse = '10c'
    Lehrer = 'Herr Herrys'
    Art = 'Test 01'
    Titel = 'Trigonometrie im rechtw. Dreieck'
    datum_delta = 1
    anzahl = 1
    probe = False

    liste_punkte = ['Punkte']
    liste_bez = ['Aufgabe']

    try:
        for i in range(anzahl):
            # Create tasks
            Aufgaben = [
                [
                    kongruente_dreiecke(1),
                    rechtwinkliges_dreieck(2),
                    verhaeltnisgleichgungen(3)
                ]
            ]
            
            # Process tasks
            liste_seiten = []
            for element in Aufgaben:
                for aufgabe in element:
                    liste_bez.extend(aufgabe[5])
                    liste_punkte.extend(aufgabe[4])
                liste_seiten.append(seite(element))

            angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]
            test_erzeugen(liste_seiten, angaben, i, probe)
            
    finally:
        # Always cleanup memory
        cleanup_memory()

if __name__ == "__main__":
    create_test_with_memory_management()