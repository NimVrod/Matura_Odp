#odczyt z pliku
liczby = []
with open("przyklad.txt", "r") as f:
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


