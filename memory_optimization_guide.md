# Memory Optimization Guide for TestBuilder

## 1. PyCharm-Specific Settings

### Increase PyCharm Memory Allocation
1. Go to `Help` → `Change Memory Settings`
2. Increase heap size to at least 4GB (4096 MB)
3. Restart PyCharm

### Disable Heavy Indexing Features
1. `File` → `Settings` → `Editor` → `General` → `Code Completion`
   - Uncheck "Show suggestions as you type"
2. `File` → `Settings` → `Tools` → `Python Integrated Tools`
   - Disable unnecessary inspections

### Configure Garbage Collection
Add to PyCharm's custom VM options (`Help` → `Edit Custom VM Options`):
```
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:+UnlockExperimentalVMOptions
-XX:+UseStringDeduplication
```

## 2. Code-Level Optimizations

### A. Lazy Import Strategy
Replace global imports with function-level imports for heavy libraries:

```python
# Instead of global imports at module level
def create_plot():
    import matplotlib.pyplot as plt  # Import only when needed
    # ... plotting code
    plt.close('all')  # Always close figures
```

### B. Memory Management for Mathematical Objects
```python
import gc
from sympy import symbols, diff, solve

def process_function(func_params):
    # Create symbols locally
    x, y, z = symbols('x y z')
    
    try:
        # Your mathematical operations
        result = diff(func_params, x)
        return result
    finally:
        # Explicit cleanup
        del x, y, z
        gc.collect()
```

### C. Optimize Matplotlib Usage
```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

def create_graph():
    fig, ax = plt.subplots()
    try:
        # Your plotting code
        plt.savefig('output.png')
        return 'output.png'
    finally:
        plt.close(fig)  # Always close figures
        plt.clf()       # Clear current figure
```

## 3. Refactor Import Structure

### Create a new imports.py file:
```python
# imports.py - Centralized import management
def get_sympy():
    """Lazy import for sympy"""
    import sympy
    return sympy

def get_matplotlib():
    """Lazy import for matplotlib"""
    import matplotlib.pyplot as plt
    return plt

def get_numpy():
    """Lazy import for numpy"""
    import numpy as np
    return np
```

### Update module imports:
```python
# Instead of: from sympy import *
# Use:
from .imports import get_sympy

def some_function():
    sympy = get_sympy()
    x = sympy.symbols('x')
    # ... rest of function
```

## 4. Memory Monitoring

### Add memory tracking to your functions:
```python
import psutil
import os

def monitor_memory(func):
    """Decorator to monitor memory usage"""
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024 / 1024  # MB
        
        result = func(*args, **kwargs)
        
        mem_after = process.memory_info().rss / 1024 / 1024  # MB
        print(f"{func.__name__}: Memory used: {mem_after - mem_before:.2f} MB")
        
        return result
    return wrapper

@monitor_memory
def your_heavy_function():
    # Your code here
    pass
```

## 5. Optimize Large Data Structures

### Use generators instead of lists where possible:
```python
# Instead of:
def create_all_problems():
    problems = []
    for i in range(1000):
        problems.append(generate_problem(i))
    return problems

# Use:
def create_problems_generator():
    for i in range(1000):
        yield generate_problem(i)
```

## 6. File-Specific Optimizations

### For temp/ files:
- Move heavy imports inside functions
- Add explicit cleanup after PDF generation
- Use context managers for file operations

### For Aufgaben/ modules:
- Split large modules into smaller, focused modules
- Use lazy loading for mathematical functions
- Implement caching for frequently used calculations

## 7. PyCharm Project Settings

### Exclude unnecessary directories:
1. Right-click on `pdf/` folder → `Mark Directory as` → `Excluded`
2. Right-click on `img/temp/` folder → `Mark Directory as` → `Excluded`
3. Exclude `__pycache__` directories

### Configure Python interpreter:
1. Use a virtual environment to isolate dependencies
2. Consider using a lighter Python distribution if possible

## 8. System-Level Optimizations

### Virtual Environment with Memory Limits:
```bash
# Create a new virtual environment
python -m venv testbuilder_env

# Activate it
source testbuilder_env/bin/activate  # Linux/Mac
# or
testbuilder_env\Scripts\activate  # Windows

# Install only necessary packages
pip install -r requirements_minimal.txt
```

### Create requirements_minimal.txt:
```
numpy==1.24.0
sympy==1.12
matplotlib==3.7.0
pylatex==1.4.2
# Remove unnecessary packages
```

## Implementation Priority

1. **Immediate**: Increase PyCharm memory, disable heavy indexing
2. **Short-term**: Add plt.close() calls, implement lazy imports for heavy modules
3. **Medium-term**: Refactor import structure, add memory monitoring
4. **Long-term**: Split large modules, implement caching strategies

## Testing Memory Improvements

Run this script to monitor memory usage:
```python
import psutil
import time

def monitor_system():
    process = psutil.Process()
    while True:
        mem_info = process.memory_info()
        print(f"Memory: {mem_info.rss / 1024 / 1024:.2f} MB")
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()
```