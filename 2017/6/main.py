#odczyt z pliku
piksele = []
with open("dane.txt", "r") as f:
    for line in f:
        tab = line.strip().split(" ")
        piksele.append([int(x) for x in tab])

#podpunkt 1
tab = []
for tablica in piksele:
    for liczba in tablica:
        tab.append(liczba)

najasniejszy = max(tab)
najciemnieszy = min(tab)

#podpunkt2
suma2 = 0
for tablica in piksele:
    for i in range(1, len(tablica)//2):
        if tablica[i] == tablica[-i-1]:
            pass
        else:
            suma2 +=1; break

print(suma2)

#podpunkt 3
suma3 = 0
#środek
for i in range(1, len(piksele[0])-1):
    for j in range(1, len(piksele)-1):
        #print(f"{piksele[j][i]} : {piksele[j][i+1]} : {(piksele[j+1][i])}")
        if abs(piksele[j][i]-piksele[j][i+1]) > 128:
            suma3+=1
        elif abs(piksele[j][i]-piksele[j+1][i]) > 128:
            suma3+=1
        elif abs(piksele[j][i]-piksele[j-1][i]) > 128:
            suma3+=1
        elif abs(piksele[j][i]-piksele[j][i-1]) > 128:
            suma3+=1


#brzegowe srodki
for i in range(1, len(piksele[-1])-1):
    if abs(piksele[-1][i]-piksele[-1][i+1]) >  128:
        suma3 +=1
    elif abs(piksele[-1][i]-piksele[-2][i]) > 128:
        suma3 +=1
    elif abs(piksele[-1][i]-piksele[-1][i-1]) > 128:
        suma3+=1
        

for i in range(1, len(piksele[0])-1):
    if abs(piksele[0][i]-piksele[0][i+1]) >  128:
        suma3 +=1
    elif abs(piksele[0][i]-piksele[1][i]) > 128:
        suma3 +=1
    elif abs(piksele[0][i]-piksele[0][i-1]) > 128:
        suma3+=1

for i in range(1, len(piksele)-1):
    if abs(piksele[i][-1] - piksele[i+1][-1]) > 128:
        suma3 +=1
    elif abs(piksele[i][-1] - piksele[i][-2]) > 128:
        suma3+=1
    elif abs(piksele[i][-1] - piksele[i-1][-1]) > 128:
        suma3+=1

for i in range(1, len(piksele)-1):
    if abs(piksele[i][0] - piksele[i+1][0]) > 128:
        suma3 +=1
    elif abs(piksele[i][0] - piksele[i][1]) > 128:
        suma3+=1
    elif abs(piksele[i][0] - piksele[i-1][0]) > 128:
        suma3+=1


#brzegi
if abs(piksele[-1][-1]- piksele[-2][-1]) > 128:
    suma3+=1
elif abs(piksele[-1][-1]- piksele[-1][-2]) > 128:
    suma3+=1

if abs(piksele[0][0] - piksele[0][1]) > 128:
    suma3+=1
elif abs(piksele[0][0] - piksele[1][0]) > 128:
    suma3+=1

if abs(piksele[0][-1] - piksele[0][-2]) > 128:
    suma3+=1
elif abs(piksele[0][-1] - piksele[1][-1]) > 128:
    suma3+=1

if abs(piksele[-1][0] - piksele[-1][1]) > 128:
    suma3+=1
elif abs(piksele[-1][0] - piksele[-2][0]) > 128:
    suma3+=1


print(suma3) #zły wynik


#podpunkt 4
dlugosci = []
for n in range(0, len(piksele[0])):
    for i in range(0, len(piksele)):
        for j in range(i+1, len(piksele)):
            if piksele[i][n] == piksele[j][n]:
                dlugosci.append(j-i+1)
            else:
                break

print(max(dlugosci))


#zapis do pliku
with open("wynik6.txt", "w") as f:
    f.write(f"6.1 Najasniejszy: {najasniejszy}, Najciemniejszy: {najciemnieszy}\n")
    f.write(f"6.2 {suma2}\n")
    f.write(f"6.3 {suma3}\n")
    f.write(f"6.4 {max(dlugosci)}\n")