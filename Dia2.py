'''
Dado un array devolver el array resultante de multiplicar todos los indices del array menos el de la posicion en la que lo escribimos
Por ejemplo
Dado [1, 2, 3, 4, 5] deberia devolver [120, 60, 40, 30, 24]
Dado [3, 2, 1], deberia devolver [2, 3, 6]
'''


def devolverArray(list):
    total = 1
    nuevaLista = []
    # Calculo la multiplicacion de todos los indices
    for i in range(len(list)):
        total = total * list[i]
    #Divido entre el indice
    for i in range(len(list)):
        nuevaLista.insert(i,total/list[i])
    return nuevaLista
lista = [3, 2, 1]
print(devolverArray(lista))