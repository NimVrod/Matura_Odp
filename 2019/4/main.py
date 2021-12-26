import math
#odczyt z pliku
liczby = []
with open("liczby.txt", "r") as f:
    for line in f:
        liczby.append(int(line.strip()))

def potega_trzy(liczba):
    while liczba % 3 == 0:
        if liczba //3 == 1:
            return True
        else:
            liczba //= 3
    return False

#podpunkt1
suma = 0
for liczba in liczby:
    if potega_trzy(liczba):
        suma += 1

print(suma)

def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    else:
        return 1

#podpunkt2
suma2 = 0
for liczba in liczby:
    suma_silnia = 0
    for litera in str(liczba):
        suma_silnia += silnia(int(litera))

    #print(f"{liczba} : {suma_silnia}")
    if liczba == suma_silnia:
        suma2 +=1

print(suma2)

dlugosc = []
dzielniki = []
pierwszeliczby = []
for i in range(0, len(liczby)):
    for j in range(i+1, len(liczby)):
        dzielnik = math.gcd(*liczby[i:j])
        if dzielnik > 1:
            dlugosc.append(j-i); dzielniki.append(dzielnik); pierwszeliczby.append(i)


indeks = dlugosc.index(max(dlugosc))
print(f"Pierwsza liczba ciągu {liczby[pierwszeliczby[indeks]]}, długość {dlugosc[indeks]}, największy wspólny dzielnik {dzielniki[indeks]}")

#zapis do pliku
with open ("wynik4.txt", "w") as f:
    f.write(f"4.1 {suma}\n")
    f.write(f"4.2 {suma2}\n")
    f.write(f"4.3 Pierwsza liczba ciągu {liczby[pierwszeliczby[indeks]]}, długość {dlugosc[indeks]}, największy wspólny dzielnik {dzielniki[indeks]}\n")