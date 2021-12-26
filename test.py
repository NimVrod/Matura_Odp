string = "bnnnnnnnnnnnnnoooooooooooooooooooooooooooooo"

def lis(string : str = None):
    dlugosci = []; pierwszeliczby = []
    if string is None:
        return None
    else:
        for i in range(0, len(string)):
            for j in range(i+1, len(string)):
                if string[i] == string[j]:
                    dlugosci.append(j-i+1); pierwszeliczby.append(i)
                else:
                    break

    indeks = dlugosci.index(max(dlugosci))
    return(dlugosci[indeks], (pierwszeliczby[indeks]))

l = lis(string)
print(f"{l} : {string[l[1]]}")