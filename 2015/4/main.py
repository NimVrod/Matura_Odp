def wczytaj():
        """
        Wczytanie danych z pliku do tabeli
        returns list of strings
        """
        tab = []
        with open("liczby.txt", "r") as f:
            for line in f:
                #print(line.strip())
                tab.append(line.strip())
                
        #print(tab)
        return tab

def podpunkt1(tab):
    suma = 0
    for liczba in tab:
        #print(f"{liczba.count('0')} ? {liczba.count('1')}")
        if liczba.count('0') > liczba.count('1'):
            suma +=1

    return suma

def podpunkt2(tab):
    suma1, suma2 = 0, 0
    for liczba in tab:
        a = int(liczba, 2)
        if a % 2 == 0:
            suma1 +=1
        if a % 8 == 0:
            suma2 +=1
    
    return suma1, suma2


def podpunkt3(tab : list[str]) :
    liczby = [int(i, 2) for i in tab] # list comprehension zamiana stringów binarnych na int
    print(liczby)
    return liczby.index(max(liczby)) + 1, liczby.index(min(liczby)) +1


def main():
    liczby = wczytaj()
    #suma1 = podpunkt1(liczby)
    with open("wynik4.txt", 'w') as f:
        f.write(f"4.1 {podpunkt1(liczby)}\n4.2 {podpunkt2(liczby)}\n4.3 {podpunkt3(liczby)}")
        print(f"{podpunkt1(liczby)}\n{podpunkt2(liczby)}\n{podpunkt3(liczby)}")


if __name__ == '__main__':
    main()