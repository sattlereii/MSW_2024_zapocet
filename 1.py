from sympy import symbols, diff
import scipy.integrate as integrate
import numpy as np
from math import factorial
from time import process_time
import sys

# Zvýšení limiWtu pro počet číslic při převodu na řetězec
sys.set_int_max_str_digits(1000000)

# Derivace s knihovnou SymPy
def derivace_sym(funkce, promenna, hodnota):
    promenna = symbols("x")
    derivace = diff(funkce, promenna)
    return (derivace.subs(x, hodnota)).doit()

start = process_time()
x = symbols('x')
funkce = (6*x**3)*(4+2*x**-2)
vysledek = derivace_sym(funkce, x, 7)
konec = process_time()

print("Knihovna Sympy:")
print(f"Derivace je {vysledek} a Doba trvání výpočtu: {(konec - start)}")

# Derivace vlastní funkce
def f(x):
    return (6*x**3)*(4+2*x**-2)

def derivace(funkce, hodnota, h=0.001):
    return (funkce(hodnota+h) - funkce(hodnota))/h

start = process_time()
vysledek = derivace(f, 7)
konec = process_time()

print("Vlastní funkce:")
print(f"Derivace funkce je {vysledek} a Doba trvání výpočtu: {(konec - start)}")
print("\n")

# Integrace s knihovnou SciPy
start = process_time()
vysledek = integrate.quad(lambda x: (2*x**2-4*x+4)/4, 0, 2)
konec = process_time()

print("Knihovna Scipy:")
print(f"Výpočet integrace je: {vysledek[0]} a Doba trvání výpočtu: {(konec - start)}")

# Integrace vlastní funkcí (lichoběžníkové pravidlo)
def f(x):
    return (2*x**2-4*x+4)/4

start = process_time()
vysledek = 0
x = 0
b = 2
dx = 0.0001
while x < b:
    vysledek += dx * (f(x) + f((x+dx)))/2
    x += dx
konec = process_time()

print("Vlastní funkce:")
print(f"Výpočet integrace je: {vysledek} a Doba trvání výpočtu: {(konec - start)}")
print("\n")

# Skalární součin s knihovnou NumPy
start = process_time()
a = np.array([2, 6, 10])
b = np.array([3, 9, 15])
vysledek = sum(a*b)
konec = process_time()

print("Knihovna Numpy:")
print(f"Skalární součin je: {vysledek} a Doba trvání výpočtu: {(konec - start)}")

# Skalární součin vlastní funkcí
start = process_time()
vysledek = 0
a = (2, 6, 10)
b = (3, 9, 15)
for i in range(len(a)):
    vysledek += a[i]*b[i]
konec = process_time()

print("Vlastní cyklus:")
print(f"Skalární součin je {vysledek} a Doba trvání výpočtu: {(konec - start)}")
print("\n")

# Výpočet faktoriálu s knihovnou Math
start = process_time()
x = 55200
vysledek = factorial(x)
konec = process_time()
vysledek = str(vysledek)

print("Knihovna Math:")
print(f"Faktoriál z čísla {x} je {vysledek[:10]} a Doba trvání výpočtu: {(konec - start)}")

# Výpočet faktoriálu vlastní funkcí
start = process_time()
x = 55200
vysledek = 1
for i in range(1, x+1):
    vysledek = vysledek * i 
konec = process_time()
vysledek = str(vysledek)

print("Vlastní cyklus:")
print(f"Faktoriál z čísla {x} je {vysledek[:10]} a Doba trvání výpočtu: {(konec - start)}")
print("\n")

# Násobení matice s knihovnou NumPy
start = process_time()
matice = [[55, 1492, 2001], [606, 1526, 1944], [0, 1939, 2022]]
vysledek = np.array(matice)*15
konec = process_time()

print("Knihovna Numpy:")
print(f"Matice je {vysledek} a Doba trvání výpočtu: {(konec - start)}")

# Násobení matice vlastní funkcí
start = process_time()
matice = [[55, 1492, 2001], [606, 1526, 1944], [0, 1939, 2022]]
for i in range(len(matice)):
    for j in range(len(matice[0])):
        matice[i][j] = matice[i][j]*15
konec = process_time()

print("Vlastní cyklus:")
print(f"Matice je {matice} a Doba trvání výpočtu: {(konec - start)}")
