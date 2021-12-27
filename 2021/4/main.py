tekst = []
funkcje = []
dane = []

#funkcje
def dopisz(litera):
    global tekst
    tekst.append(litera)

def zmien(litera):
    global tekst
    tekst[-1] = litera

def usun():
    global tekst
    tekst.pop(-1)

def przesun(litera):
    global tekst
    indeks = tekst.index(litera)
    nowa = ord(litera) + 1
    if nowa > 90:
        nowa = 65
    tekst[indeks] = chr(nowa)

#odczyt z pliku
with open('instrukcje.txt', 'r') as f:
    for line in f:
        tab = line.strip().split(" ")
        funkcje.append(tab[0]); dane.append(tab[1]);
    print(funkcje)
    print(dane)

#podpunkt 2
rodzaje = []; dlugosci = []
for i in range(0, len(funkcje)):
    for j in range(i+1, len(funkcje)):
        if funkcje[i] == funkcje[j]:
            rodzaje.append(funkcje[i]); dlugosci.append(j-i+1)
        else:
            break

indeks = dlugosci.index(max(dlugosci))
print(f"Rodzaj instrukcji: {rodzaje[indeks]}, długość ciągu: {dlugosci[indeks]}")

#podpunkt 3
sumy_liter = {}
for i in range(0, len(funkcje)):
    if funkcje[i] == "DOPISZ":
        if dane[i] in sumy_liter:
            sumy_liter[dane[i]] += 1
        else:
            sumy_liter[dane[i]] = 1
    
print(max(sumy_liter, key=sumy_liter.get))


#podpunkt 4 i 1
for i in range(0, len(funkcje)):
    if funkcje[i] == "DOPISZ":
        dopisz(dane[i])
    elif funkcje[i] == "USUN":
        usun()
    elif funkcje[i] == "PRZESUN":
        przesun(dane[i])
    elif funkcje[i] == "ZMIEN":
        zmien(dane[i])

txt = "".join(tekst)
print(f"Napis to: {txt}, długość to {len(txt)}")

#zapis do pliku
with open("wynik4.txt", "w") as f:
    f.write(f"4.1 {len(txt)}\n")
    f.write(f"4.2 Rodzaj instrukcji: {rodzaje[indeks]}, długość ciągu: {dlugosci[indeks]}\n")
    f.write(f"4.3 {max(sumy_liter, key=sumy_liter.get)}\n")
    f.write(f"4.4 {txt}\n")