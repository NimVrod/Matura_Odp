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
with open("dane_6_1.txt","r") as f, open("wynik_6_1.txt","w") as o:
    for line in f:
        o.write(zaszyfruj(line.strip(), 107) + "\n")

#podpunkt2
with open("dane_6_2.txt","r") as f, open("wynik_6_2.txt","w") as o:
    for line in f:
        tab = line.strip().split(" ")
        try:
            if tab[1] == None:
                tab[1] = 0
        except IndexError:
            tab.append(0)
        o.write(odszyfruj(tab[0], int(tab[1])) + "\n")

#podpunkt3
with open("dane_6_3.txt","r") as f, open("wynik_6_3.txt", "w") as o, open("test.txt", 'w') as t:
    wyrazy = []
    for line in f:
        tab = line.strip().split(" ")
        if tab == []:
            break
        dobry = False
        for i in range(0, 27):
            if tab[0] == odszyfruj(tab[1], i):
                dobry = True
        
        if dobry == False:
            wyrazy.append(tab[0])
        

    for wyraz in wyrazy:
        o.write(f"{wyraz}\n")   
