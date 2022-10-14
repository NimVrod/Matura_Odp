

def load_file(filename:str):
    tablice = []
    with open(filename, 'r') as f:
        tablica = []
        for line in f:
            if line.strip() == "":
                if tablica:
                    tablice.append(tablica)
                    tablica = []

            else:
                tablica.append(line.strip())
        if tablica:
            tablice.append(tablica)
    return tablice

def podpunkt_1(tablice):
    suma, ilosc = 0, 0
    for tablica in tablice:
        ilosc2 = 0
        for i in range(len(tablica[0])):
            dodaj = 1
            for j in range(len(tablica)):
                #print(tablica[j][i])
                if tablica[j][i] != '.':
                    dodaj = 0
                    break
            ilosc2 += dodaj

        if ilosc2 > 0:
            #print(tablica)
            suma += 1
            if ilosc2 > ilosc:
                ilosc = ilosc2

    return suma, ilosc

def podpunkt_2(tablice):
    suma, ilosc = 0, 999
    pionki = ['k', 'h', 'w', 'g', 's', 'p']
    bialeilosc = {}
    czarneilosc = {}
    for tablica in tablice:
        dodaj = 1
        for line in tablica:
            for pionek in pionki:
                bialeilosc[pionek] = bialeilosc.get(pionek, 0) + line.count(pionek.upper())
                czarneilosc[pionek] = czarneilosc.get(pionek, 0) + line.count(pionek)

        for pionek in pionki:
            if bialeilosc[pionek] != czarneilosc[pionek]:
                dodaj = 0
                break

        if dodaj > 0:
            suma += 1
            i = 0
            for pionek in pionki:
                i += czarneilosc[pionek]+bialeilosc[pionek]
            if i < ilosc:
                #print(tablica)
                ilosc = i

        czarneilosc = {}
        bialeilosc = {}

    return suma, ilosc



def czy_szachuje(tablica, x, y, biale:bool):
    sk, sw = "", ""
    #kolumana
    for i in range(len(tablica)):
        if tablica[i][x] != '.':
            sk += tablica[i][x]
    #wiersz
    for i in range(len(tablica[0])):
        if tablica[y][i] != '.':
            sw += tablica[y][i]

    #print(sk, sw)

    if biale:
        if sk == "Wk" or sk == "kW":
            return True

        if sw == "Wk" or sw == "kW":
            return True
    else:
        if sk == "wK" or sk == "Kw":
            return True

        if sw == "wK" or sw == "Kw":
            return True




def podpunkt_3(tablice):
    czarne, biale = 0, 0

    for tablica in tablice:
        for line in tablica:
            if 'w' in line:
                if czy_szachuje(tablica, line.index('w'), tablica.index(line), False):
                    czarne += 1
            elif 'W' in line:
                if czy_szachuje(tablica, line.index('W'), tablica.index(line), True):
                    biale += 1


    return biale, czarne

def main():
    tablice = load_file("szachy.txt")

    a1 = podpunkt_1(tablice)
    print("a1:", a1[0], a1[1])
    with open("zadanie1_1.txt", 'w') as f:
        f.write(str(a1[0]) + " " + str(a1[1]))

    a2 = podpunkt_2(tablice)
    print("a2:", a2[0], a2[1])
    with open("zadanie1_2.txt", 'w') as f:
        f.write(str(a2[0])+" "+str(a2[1]))


    a3 = podpunkt_3(tablice)
    print("a3:", a3[0], a3[1])
    with open("zadanie1_3.txt", 'w') as f:
        f.write(str(a3[0])+" "+str(a3[1]))

if __name__ == "__main__":
    main()