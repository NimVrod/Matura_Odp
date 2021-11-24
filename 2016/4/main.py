import random
import numpy as np
import math

def podpunkt1(tab):
    suma1 = 0 # na okręgu
    suma2 = 0 # wewnątrz okręgu
    for liczba in tab:
        #print(liczba)
        if ((liczba[0]-200)**2) + ((liczba[1]-200)**2) == 200**2:
            suma1 += 1
        if ((liczba[0]-200)**2) + ((liczba[1]-200)**2) < 200**2:
            suma2 +=1
    return suma1, suma2

def podpunkt2(tab, nk, a=400, r=200) -> int:
    """
    nk/n≈Pk/P
    """

    pi = (nk[1]*(a**2))/(len(tab)*(r**2))
    return pi


def podpunkt3(tab, nk, a=400, r=200) -> list[int]:
    liczby = []
    for i in range(1, len(tab)):
        pi = (nk[1]*(a**2))/(i*(r**2))
        roznica = abs(np.pi - pi)
        liczby.append(roznica)


    for i in range(1, len(liczby)):
        txt = ""
        for j in range(0, math.floor(liczby[i])):
            txt+="#"
            j+=9
            if j > 100:
                break
        print(f"{i}: {txt} {liczby[i]}")




tab = []
for i in range(0, 10000):
    tab.append([random.randint(0, 400), random.randint(0, 400)])
tab[0] = [400, 200]
#print("\n\n\n\n")
n =(podpunkt1(tab))
print(n)
print(podpunkt2(tab, n))
podpunkt3(tab, n)