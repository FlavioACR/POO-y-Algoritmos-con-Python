'''Complejidad Algoritmica:

* ¿ Por qué compararmos la eficiencia de un algoritmo ?
* Complejidad temporal vs complejidad espacial(memoria)
* Podemos definirla como T(n)

Implementaciónde T(n)
Aproximaciones:
* Cronometrar el tiempo en el que corre un algoritmo
* Contar los pasos con una medida abstracta de operación
* Contar los pasos conforme nos aproximamos al infinito (Estandar)

'''

# Para medir el tiempo em python usaremos este modulo:
import time 

# Generar dos implementaciones factorial:

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

# Factorial recursivo
def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

if __name__=='__main__':
    n = 200000

    comienzo = time.time()
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    final = time.time()
    print(final - comienzo)