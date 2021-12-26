def czy_pierwsza(n : int) -> bool:
    #if n == 2:
    #    return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def lista_pierwszych(n : int) -> list[int]:
    pierwsze = []
    for i in range(2, n):
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze


#wczytanie z pliku
liczby = []; slowa = []
with open("przyklad.txt", "r") as f:
    for line in f:
        linia = line.split(" ")
        liczby.append(int(linia[0].strip())); slowa.append(linia[1].strip())

#podpunkt1
sumy = []
for liczba in liczby:
    lista = lista_pierwszych(liczba)
    for pierwsza in lista:
        roznica = liczba - pierwsza
        if roznica in lista:
            sumy.append((pierwsza, roznica))
            break   

print(sumy)

#podpunkt2
text = ""
for slowo in slowa:
    dlugosci = []; pierwszeliczby = []
    for i in range(0, len(slowo)):
        for j in range(i+1, len(slowo)):
            if slowo[i] == slowo[j]:
                dlugosci.append(j-i+1); pierwszeliczby.append(i)
            else:
                break

    indeks = dlugosci.index(max(dlugosci))
    text += f"{slowo[pierwszeliczby[indeks]:pierwszeliczby[indeks]+dlugosci[indeks]]} {dlugosci[indeks]}\n"

print(text)


#podpunkt3
liczby_rowne = []; slowa_rowne = [];
for i in range(len(slowa)):
    if liczby[i] == len(slowa[i]):
        liczby_rowne.append(liczby[i]); slowa_rowne.append(slowa[i])

zdanie = ""
for i in range(0, len(liczby_rowne)):
    if liczby_rowne[i] == min(liczby_rowne) and min(slowa_rowne) == slowa_rowne[i]:
        zdanie = f"{liczby_rowne[i]} : {slowa_rowne[i]}"; break

print(zdanie)

#zapis do pliku
with open ("wynik4.txt", "w") as f:
    f.write("4.1\n")
    for i in range(0, len(liczby)):
        f.write(f"{liczby[i]} {sumy[i][0]} {sumy[i][1]}\n")

    f.write(f"4.2\n {text}")
    f.write(f"4.3\n {zdanie}")