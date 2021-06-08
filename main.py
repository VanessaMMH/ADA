from generador_random import generar_aleatorios
from quicksort import *
from insercion import insercion
from mergesort import *
import time
from os import remove
from os import path


#escribe los tiempos generados en un archivo times.dot
def write_time(tam, tiempo,opcion):
    ss=""
    if opcion==1:  
        ss="quicksort.dot"
        
    elif opcion==2:
        ss="insercion.dot"
    elif opcion==3:
        ss="mergesort.dot"
    else:
        quit()

    with open("./times{}".format(ss), "a" ) as f:
        f.write(str(tam)+','+str(tiempo))
        f.write('\n')
    


#Genera el tiempo que tarda y lo hace guardar 
def tiempo(minimo , maximo , incremento):
    # opcion=1   
    for i in range(minimo , maximo+1 , incremento):
        main_array=generar_aleatorios(i)
        array_insercion=main_array
        array_quicksort=main_array
        array_mergesort=main_array
        # print('_'*100)
        # print(main_array)
        # print('_'*100)
    
        empiezo=time.time()
        quicksort(array_quicksort,0,len(array_quicksort)-1)
        termino=time.time()
        print(i,'quicksort '+'tardaste: ',termino-empiezo)
        write_time(i,termino-empiezo,1)
        print('_'*50)
        empiezo=time.time()
        insercion(array_insercion)
        termino=time.time()
        print(i,'insertionsort '+'tardaste: ',termino-empiezo)
        write_time(i,termino-empiezo,2)
        print('_'*50)
        empiezo=time.time()
        mergesort(array_mergesort)
        termino=time.time()
        print(i,'mergesort '+'tardaste: ',termino-empiezo)
        write_time(i,termino-empiezo,3)
        print('_'*50)


if __name__ == '__main__':
   
   
    if path.exists("./timesinsercion.dot"):
        remove("./timesinsercion.dot")
    if path.exists("./timesquicksort.dot"):
        remove("./timesquicksort.dot")
    if path.exists("./timesmergesort.dot"):
        remove("./timesmergesort.dot")
    
   #tiempo(minimo_array, maximo_array , incremento_array )
    # tiempo(100, 1000, 100)
    tiempo(1000, 10000, 500)
    


