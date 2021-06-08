import random

#recorremos nuestro set de datos posición por posición y
#  comparamos el número con los valores anteriores, en caso de ser menor, 
# lo colocamos en su posición indicada para ordenar de menor a mayor.

def insercion(array):

    for i in range(1, len(array)):
        valorActual = array[i] #obtenemos el valor actual a comparar
        posicionActual = i


        # mueve los elementos del arreglo array[0..i-1],que son mayores
        # que el valor de la posición actual del recorrido,
        #  a una posición adelante de su posición actual 
        while posicionActual > 0 and array[posicionActual - 1] > valorActual:
            array[posicionActual] = array[posicionActual - 1]
            posicionActual -= 1

        array[posicionActual] = valorActual


   # return array
           

# if __name__=='__main__':
#     tamanho_de_array = int(input('Tamanho del array? '))
#     array = [random.randint(0, 100) for i in range(tamanho_de_array)]
#     print(array)
#     insercion(array)
#     print(array)