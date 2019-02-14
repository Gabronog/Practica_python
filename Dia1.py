'''
    Tenemos un conjunto de numeros en un array.
    Dado un numero cualquiera devolver un booleano cuyo valor dependa de si el numero se puede obtener
    como combinacion de dos numeros de nuestro array

    Por ejemplo
    [1,2,5,6]

    (3)

    Devolveria true porque 2+1 = 3;

    [1,5,6]

    (3)

    Devolveria false porque no hay ninguna combinacion entre los numeros del array que de 3
'''


def comprobarArray(list, numero):
    # Primera forma de resolverlo (Complejidad O(X(N))
    for i in range(len(list)):
        if numero - list[i] in list:
            return True
        elif numero - list[i] not in list:
            return False



def comprobarArray2(list, numero):
    list.sort()
    i = (len(list) - 1)
    j = 0
    encontrado = False
    while (i > 0 and j < len(list)):
        sum = list[i] + list[j]
        if sum < numero:
            j = j + 1
        elif sum > numero:
            i = i - 1
        elif sum == numero:
            return True
    return False
    # Forma mas optimizada (complejidad logaritmica)


encontrado = False
l = [1, 4, 9, 5, 6, 2]
n = 3
encontrado = comprobarArray2(l, n)
print(encontrado)

# Complejidad O(x(n)) -> En el peor de los casos == fuerza bruta
