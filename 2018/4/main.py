tab = []

#odczyt z pliku
with open("przyklad.txt", "r") as f:
    for line in f:
        tab.append(line.strip())


#podpunkt1
i = 39; slowo=""
while i <= len(tab):
    slowo += tab[i][9]; i+=40
print(slowo)

#podpunkt2
rozne_litery = []
for s in tab:
    suma = 0
    litery = {}
    for litera in s:
        if litera not in litery:
            suma += 1; litery[litera] = s.index(litera)
    rozne_litery.append(suma)  # zoptymalizowac kiedys

print(f"{tab[rozne_litery.index(max(rozne_litery))]} {max(rozne_litery)}")


wiecej_10 = []
#podpunkt3
for s in tab:
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if abs(ord(s[i]) - ord(s[j])) > 10:
                wiecej_10.append(s)

#zoptymalizować 2 

mniej_10 = [x for x in tab if x not in wiecej_10]
print(mniej_10)

#zapis do pliku
with open("wynik4.txt", "w") as f:
    f.write(f"4.1 {slowo}\n")
    f.write(f"4.2 {tab[rozne_litery.index(max(rozne_litery))]} {max(rozne_litery)}\n")
    f.write("4.3\n")
    for x in mniej_10:
        f.write(x + "\n")