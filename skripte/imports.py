"""
Centralized import management for memory optimization
This module provides lazy loading functions for heavy libraries
"""

def get_sympy():
    """Lazy import for sympy - only load when needed"""
    import sympy
    return sympy

def get_matplotlib():
    """Lazy import for matplotlib with memory optimization"""
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend to save memory
    import matplotlib.pyplot as plt
    return plt

def get_numpy():
    """Lazy import for numpy"""
    import numpy as np
    return np

def get_scipy():
    """Lazy import for scipy"""
    import scipy
    return scipy

def get_pylatex():
    """Lazy import for pylatex components"""
    from pylatex import (
        Document, NoEscape, SmallText, LargeText, MediumText, 
        NewPage, Tabular, Alignat, Figure, MultiColumn, MultiRow
    )
    return {
        'Document': Document,
        'NoEscape': NoEscape,
        'SmallText': SmallText,
        'LargeText': LargeText,
        'MediumText': MediumText,
        'NewPage': NewPage,
        'Tabular': Tabular,
        'Alignat': Alignat,
        'Figure': Figure,
        'MultiColumn': MultiColumn,
        'MultiRow': MultiRow
    }

def cleanup_matplotlib():
    """Clean up matplotlib resources"""
    try:
        import matplotlib.pyplot as plt
        plt.close('all')
        plt.clf()
    except ImportError:
        pass

def cleanup_memory():
    """Force garbage collection"""
    import gc
    gc.collect()