import random

#Necesitamos dividir el array
#Necesitamos un punto pivotal
#Recursivamente ordenar cada mitad del array

def quicksort(array, izquierda, derecha):
    if izquierda < derecha:
        indice_particion = particion(array, izquierda, derecha)       
        quicksort(array, izquierda, indice_particion-1)
        quicksort(array, indice_particion + 1, derecha)
    


def particion(array, i_bajo, i_alto):
    pivot = array[i_alto]
    i = i_bajo
    for j in range(i_bajo,len(array)):
        valorActual=array[j]
        if (valorActual < pivot) :
            swap(array, i, j)
            i+=1                
    swap(array, i, i_alto)
    return i


def swap(array, n1, n2):
    aux = array[n1]
    array[n1] = array[n2]
    array[n2] = aux



# if __name__=='__main__':
#     tamanho_de_array = int(input('Tamanho del array? '))
#     array = [random.randint(0, 100) for i in range(tamanho_de_array)]
#     print(array)
#     print('-' * 50)
#     quicksort(array,0 ,len(array)-1)
#     print(array)
