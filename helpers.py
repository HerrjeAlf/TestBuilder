import pathlib

# Gibt den root-Pfad des Projekts zurück
def root_path():
    return pathlib.Path(__file__).parent.absolute()
