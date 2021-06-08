import random
from os import remove
from os import path


def generar_aleatorios(limite): #genera aleatorios  nro arreglos, 
    array=[]
    for _ in range(limite):
        array.append(random.randint(-limite, limite))
        #write(array)
        #print(array)
        
        
    return array



if __name__ == '__main__':
    if path.exists("./numbers.dot"):
        remove("./numbers.dot")
    main_array=generar_aleatorios(2,10)
    for array in main_array:
        print(array)

    