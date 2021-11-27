import math
#podpunkt 1
with open("przyklad.txt", "r") as f:
    piksele = []
    for line in f:
        tab = line.split(" ")
        for px in tab:
            piksele.append(int(px))   

    print(f"Najciemniejszy piskel: {min(piksele)}\nNajciemniejszy piksel: {max(piksele)}")

#podpunkt 2
with open("przyklad.txt", "r") as f:
    suma = 0
    for line in f:
        tab= line.split(" ")
        for i in range(0, math.floor(len(tab)/2)):
            if tab[i] != tab[-i]:
                suma +=1
                break

    print(f"Należy usunąć {suma} linii")


#podpunkt 3
with open("przyklad.txt", "r") as f:
    piksele = []
    for line in f:
        tab= line.split(" ")
        piksele.append(tab)

    suma = 0
    for i in range(0, len(piksele[0])-1):
        for j in range(0, len(piksele)-1):
            if abs(piksele[i+1][j]-piksele[i][j]) > 128:
                suma +=1
            if abs(piksele[i][j+1]-piksele[i][j]) > 128:
                suma +=1
    for i in range(0, len(piksele)-1):
        if abs(piksele[i][-1] - piksele[i+1][-1]) > 128:
            suma+=1

    for i in range(0, len(piksele[0])-1):
        if abs(piksele[-1][i] - piksele[-1][i+1]) > 128:
            suma+=1
        

    print(suma) 





def find_max_in_one(piksele,j : int = 0, start : int = 0):
    for i in range(start, len(piksele)):
        if piksele[j][i] != piksele[j][i+1]:
            return start, i



def find_max(piksele, j):
    start = 0
    maxy = []
    while start < len(piksele):
        e = find_max_in_one(piksele, j, start)
        start = e[0]
        maxy.append(e[1])

    return max(maxy)
    





#podpunkt 4
with open("przyklad.txt", "r") as f:
    piksele = []
    for line in f:
        tab= line.split(" ")
        piksele.append(tab)

    dlugosc = []
    for i in range(0, len(piksele[0])):
        dlugosc.append(find_max(piksele, i))

    