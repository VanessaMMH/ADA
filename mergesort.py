import random

def mergesort(array):
    if len(array) > 1:
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]
        # print(izquierda, '*' * 3, derecha)

        #Se llamara recursivamente  en cada mitad hasta 
        # que nos queden lista de un solo tamanho
        mergesort(izquierda)
        mergesort(derecha)
        #Funcion para comparar las sublistas generadas
        intercala(array,izquierda,derecha,len(array))
        return array

def intercala(array,izquierda,derecha,r):
        # Iteradores para recorrer las dos subarrays
        i = 0
        j = 0
        # Iterador para la array principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                array[k] = izquierda[i]
                i += 1
            else:
                array[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            array[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            array[k] = derecha[j]
            j += 1
            k += 1
        
        # print(f'izquierda {izquierda}, derecha {derecha}')
        # print(array)
        # print('_' * 50)


# if __name__ == '__main__':
#     tamanho_de_array = int(input('Tamanho del array? '))
#     array= [random.randint(0, 100) for i in range(tamanho_de_array)]
#     print(array)
#     print('-' * 50)
#     array_ordenado = mergesort(array)
#     print(array_ordenado)