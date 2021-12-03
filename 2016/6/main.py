def zaszyfruj(haslo :str, klucz):
    new = ''
    k = klucz % 26
    for litera in haslo.strip():
        if ord(litera) + k > 90:
            new += chr(ord(litera) + k - 26)
        else:
            new += chr(ord(litera) + k)

    return new

def odszyfruj(haslo :str, klucz):
    new = ''
    k = klucz % 26
    for litera in haslo.strip():
        if ord(litera) - k < 65:
            new += chr(ord(litera) - k + 26)
        else:
            new += chr(ord(litera) - k)

    return new

#podpunkt1
with open("dane6_1.txt","r") as f, open("wynik6_1.txt","w") as o:
    for line in f:
        o.write(zaszyfruj(line.strip(), 107) + "\n")

#podpunkt2
with open("dane6_2.txt","r") as f, open("wynik6_2.txt","w") as o:
    for line in f:
        tab = line.split(" ")
        o.write(odszyfruj(tab[0], int(tab[1])) + "\n")

#podpunkt3
with open("dane6_3.txt","r") as f, open("wynik6_3.txt", "w") as o:
    wyrazy = []
    for line in f:
        tab = line.split(" ")
        for i in range(1, 26):
            if tab[0] == odszyfruj(tab[1], i):
                break
        wyrazy.append(tab[0] + "\n")

    o.writelines(wyrazy)   
