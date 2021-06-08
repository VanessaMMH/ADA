import random
import time
import sys
from os import remove
from os import path

# minimo , maximo , incremento , nroArray
# python3 generador.py 10 100 10 2

def generar_aleatorios(nro_arreglos,limite): #genera aleatorios  nro arreglos, 
    for _ in range(nro_arreglos):
        array=[]
        for _ in range(limite):
            array.append(random.randint(-limite, limite))
        #write(array)
        print(array)


#escribe los numeros generados en un archivo numbers.dot
def write(numbers):
    with open("./numbers.dot", "a" ) as f:
        for number in numbers:
            f.write(str(number))
            f.write('\n')


#escribe los tiempos generados en un archivo times.dot
def write_time(tam, tiempo):
    
    with open("./times.dot", "a" ) as f:
            f.write(str(tam)+','+str(tiempo))
            f.write('\n')



#Genera el tiempo que tarda y lo hace guardar 
def tiempo(minimo , maximo , incremento,nroArray):   
    for i in range(minimo , maximo+1 , incremento):
        empiezo=time.time()
        generar_aleatorios(nroArray,i)
        termino=time.time()
        print(i,'tardaste: ',termino-empiezo)
        write_time(i,termino-empiezo)

if __name__ == '__main__':
    # if path.exists("./numbers.dot"):
    #     remove("./numbers.dot")
    # if path.exists("./times.dot"):
    #     remove("./times.dot")
    
    # # minimo , maximo , incremento , nroArray
    # # python3 generador.py 10 100 10 2
    # tiempo(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
    generar_aleatorios(2,10)

 




   
    
    