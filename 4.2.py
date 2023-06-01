def silnia(n):
    if(n == 1):
        return 1
    else:
        return n*silnia(n-1)
    
def sumac_cyfr(liczba):
    liczba = str(liczba)
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma

print(sumac_cyfr(123))