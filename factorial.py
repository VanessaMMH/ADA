import time
import sys
sys.setrecursionlimit(10000)
def factorial(n):
    respuesta=1
    while n>1:
        respuesta*=n
        n-=1
    return respuesta

def factorial_r(n):
    if n==1:
        return n
    return n * factorial_r(n-1)

if __name__=='__main__':

    comienzo=time.time()
    factorial(1000)
    final=time.time()
    print('factorial', final-comienzo)
    comienzo=time.time()
    factorial_r(1000)
    final=time.time()
    print('f.recursivo', final-comienzo)
