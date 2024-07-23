import numpy as np
from scipy import integrate

# Definice funkcí
def polynomial_function(x):
    return x**2 - 2*x + 6

def harmonic_function(x):
    return 2*np.sin(2*x) 

def logarithm_function(x):
    return np.log(4*x) + 0.5

# Metody výpočtu
def riemann_ctverec(funkce, a, b):
    return integrate.quadrature(funkce, a, b)[0]

def simpson(funkce, a, b, h=0.01):
    return integrate.simpson(funkce(np.arange(a, b+h, h)), np.arange(a, b+h, h))

def romberg(funkce, a, b):
    return integrate.romberg(funkce, a, b)

# Analytické řešení pro porovnání
def analytical_polynomial(a, b):
    return (b**3/3 - b**2 + 6*b) - (a**3/3 - a**2 + 6*a)

def analytical_harmonic(a, b):
    return -np.cos(2*b) + np.cos(2*a)

def analytical_logarithm(a, b):
    return (b * (np.log(4*b) - 1) + 0.5*b) - (a * (np.log(4*a) - 1) + 0.5*a)

# Intervaly
a, b = 1, 2

# Výsledky
print("Polynomická funkce")
print(f"Riemann {riemann_ctverec(polynomial_function, a, b)}")
print(f"Simpson {simpson(polynomial_function, a, b)}")
print(f"Romberg {romberg(polynomial_function, a, b)}")
print(f"Analytické řešení {analytical_polynomial(a, b)}")

print("\nHarmonická funkce")
print(f"Riemann {riemann_ctverec(harmonic_function, a, b)}")
print(f"Simpson {simpson(harmonic_function, a, b)}")
print(f"Romberg {romberg(harmonic_function, a, b)}")
print(f"Analytické řešení {analytical_harmonic(a, b)}")

print("\nLogaritmická funkce")
print(f"Riemann {riemann_ctverec(logarithm_function, a, b)}")
print(f"Simpson {simpson(logarithm_function, a, b)}")
print(f"Romberg {romberg(logarithm_function, a, b)}")
print(f"Analytické řešení {analytical_logarithm(a, b)}")
