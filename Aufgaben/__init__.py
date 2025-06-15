# Optimized imports - only import what's actually needed
# Instead of importing everything with *, we'll use targeted imports

# Import specific functions that are commonly used across modules
from Aufgaben.Oberstufe_Analysis import (
    kurvendiskussion_polynome, 
    aenderungsrate, 
    rekonstruktion,
    extremalproblem_einfach,
    polynome_untersuchen,
    exponentialgleichungen,
    wachstumsfunktion
)

from Aufgaben.Oberstufe_Algebra import (
    geraden_lagebeziehung,
    geraden_aufstellen,
    punkte_und_vektoren,
    rechnen_mit_vektoren,
    ebene_und_punkt,
    ebenen_umformen
)

from Aufgaben.Oberstufe_Wahrscheinlichkeitsrechnung import (
    baumdiagramm,
    vierfeldertafel_studie,
    binomialverteilung,
    normalverteilung
)

from Aufgaben.Mittelstufe_Funktionen import (
    lineare_funktionen,
    parabel_und_gerade,
    einf_parabeln
)

from Aufgaben.Mittelstufe_Geometrie import (
    rechtwinkliges_dreieck,
    berechnungen_allg_dreieck,
    verhaeltnisgleichgungen,
    kongruente_Dreiecke
)

from Aufgaben.Mittelstufe_Terme_Gleichungen import (
    terme_addieren,
    terme_multiplizieren,
    terme_ausmultiplizieren,
    terme_ausklammern,
    gleichungen,
    potenzgesetze
)

from Aufgaben.Primarstufe_rationale_Zahlen import (
    brueche_erweitern,
    brueche_kuerzen,
    brueche_add_subr,
    brueche_mul_div,
    schreibweise_prozent_dezimal
)

# Physics modules - import only when needed
from Aufgaben.Mittelstufe_Ph_Elektrizität import physikalische_groessen as ph_groessen_mittel
from Aufgaben.Oberstufe_Ph_Felder import physikalische_groessen as ph_groessen_ober

# Keep the list for overview generation
liste_Aufgaben = [
    'Oberstufe_Analysis', 
    'Oberstufe_Algebra', 
    'Oberstufe_Wahrscheinlichkeitsrechnung',
    'Mittelstufe_Funktionen', 
    'Mittelstufe_Geometrie', 
    'Mittelstufe_Terme_Gleichungen',
    'Primarstufe_rationale_Zahlen', 
    'Mittelstufe_Ph_Elektrizität',
    'Oberstufe_Ph_Felder'
]