import numpy as np
from numpy import *
import time
import matplotlib.pyplot as plt

#Jacobiho metoda 
def jacobi(A, b, niteraci, x0):
    x = x0
    D = np.diag(A)
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U),x))/D
        #print("iterace:",i, "x=",x)
        #print(f"{vysledek_gaus[0]:.15f}")
        #print(f"{x[0]:.15f}")
        if (np.allclose(x, vysledek_gaus, rtol=1e-8, atol=1e-9,)) == True: # if (np.allclose(x, vysledek_gaus)) == True:
            break
    return x

#Gausova metoda 
def gaus(A,b):
    x = np.linalg.solve(A, b)
    return x

casyG = [ ]
casyJ = [ ]
CASYG = [ ]
CASYJ = [ ]

#Tvorba řady matic
m = input ("Zadej velikost čtvercové matice = " ) 
print("Zvolená velikost čtvercové matice je :", m)
m = int(m)
print("Čekej ...... probíhá výpočet")

for M in range (m-1):
    M = M + 2
    a = np.ones(M) #řada 1
    array
    #Tvorba matice - levá str.
    #Diagonální matice z 1
    A1 = np.diagflat([a])
    diag
    #Jednotková matice
    A2 = np.ones((M, M), dtype=int)
    array
    #Jednotková + Diagonální s 1 => tedy v diagonále jsou max(čísla) z řady aby  JACOBI dobře fungoval
    A = A1 + A2
    #Tvorba matice - pravá str.
    b1 = np.ones(M)
    array
    b = b1*(M+1)
    #opakování výpočtu
    for v in range (100):
        x0 = np.ones(len(A))
        #Výpočty + čas pro GAUSS
        g_start = time.perf_counter()
        vysledek_gaus = gaus(A,b)
        g_end = time.perf_counter()
        g = g_end - g_start
        g = round(1000000*g)
        #Výpočty + čas pro JACOBI
        j_start = time.perf_counter()
        vysledek_jacobi = jacobi(A,b,100,x0)
        j_end = time.perf_counter()
        j= j_end - j_start
        j = round(1000000*j)
    
        casyG.append(g)
        casyJ.append(j)

    PG = mean(casyG)
    PJ = mean(casyJ)
    casyG = [ ]
    casyJ = [ ]
    CASYG.append(PG)   
    CASYJ.append(PJ)   

#Tisk výsledného grafu
fig, ax = plt.subplots ()
line = plt.plot(CASYG, label = "Gausova eliminační metoda")
line = plt.plot(CASYJ, label = "Jacobiho iterační metoda")
plt.title(r'Čas potřebný k vyřešení soustavy lineárních rovnic v závislosti na velikosti soustavy a použité metodě výpočtu')
plt.xlabel('Velikost čtvercové matice')
plt.ylabel('Čas výpočtu [10^-6 s]')

ax.legend(loc=2)

plt.show() 

