import numpy as np
import time
from scipy.optimize import bisect, newton

def poly_func(x):
    return x**3 - 6*x**2 + 11*x - 6

def exp_func(x):
    return np.exp(x) - 5

def harm_func(x):
    return np.sin(x) - 0.5

# Derivace funkcí pro NM
def poly_func_deriv(x):
    return 3*x**2 - 12*x + 11

def exp_func_deriv(x):
    return np.exp(x)

def harm_func_deriv(x):
    return np.cos(x)

# uzavřená metoda
def find_root_bisection(func, a, b):
    return bisect(func, a, b)

# otevřená metoda
def find_root_newton(func, func_deriv, x0):
    return newton(func, x0, fprime=func_deriv)

intervals = [(-1, 4), (0, 3), (0, 2*np.pi)]
initial_guesses = [2, 1, 1]

functions = [(poly_func, poly_func_deriv), (exp_func, exp_func_deriv), (harm_func, harm_func_deriv)]

for i, (func, func_deriv) in enumerate(functions):
    a, b = intervals[i]
    x0 = initial_guesses[i]
    
    start_time = time.time()
    root_bisection = find_root_bisection(func, a, b)
    bisection_time = time.time() - start_time
    
    start_time = time.time()
    root_newton = find_root_newton(func, func_deriv, x0)
    newton_time = time.time() - start_time
    
    print(f"Funkce {i+1}:")
    print(f"Bisection Method: Kořen = {root_bisection}, Čas = {bisection_time:.6f} s")
    print(f"Newton-Raphson Method: Kořen = {root_newton}, Čas = {newton_time:.6f} s")
    print()
