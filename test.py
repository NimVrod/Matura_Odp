tablica = [1,1,1,1,1,1,1,2,4,5,6,7,8]

suma = 0
for i in range(0, len(tablica)//2):
    print(f"{tablica[i]} - {tablica[-i-1]}")
    if tablica[i] == tablica[-i-1]:
        suma+=1
print(suma)