# Cada numero de Lucas se define como la suma de sus dos inmediatos
# anteriores, formando ası una secuencia de enteros. Los dos primeros numeros de Lucas son a y b.
# Dada la siguiente ley:

#               a                               si n = 0,
# L(a, b, n) =  b                               si n = 1,
#               L(a, b, n − 1) + L(a, b, n − 2) si n > 1

# Definir en python la funcion lucas(...) que permita calcular el n-esimo numero de forma recursiva.

def lucas(a:int, b:int, n:int) -> int:
    if a == 0:
        return a
    elif b == 1:
        return b
    elif n > 1:
        return lucas(a, b, n-1) + lucas(a, b, n-2)
    
lucas(10, 5, 3)