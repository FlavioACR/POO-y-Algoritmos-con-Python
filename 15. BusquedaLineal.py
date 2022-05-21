# Desarrollar los conceptos de complejidad algoritmica:
# Los problemas se trasladan a algoritmos
'''
* Busqueda en todos los elementos de manera secuencial
* ¿Cual es el peor caso?

'''

import random

# Recibe lista de busqueda y el objetivo de busqueda:
def busqueda_lineal(lista, objetivo):
    # Variable que expres si se ha encontrado o no el objetivo:
    match = False

    for elemento in lista: #  O(n)
        if elemento == objetivo:
            match = True
            break
            
    return match

if __name__ == '__main__':
    tamaño_lista = int(input('Tamaño de lista'))
    objetivo = int(input('Numero a encontrar'))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    
    print(lista)
    # Operadores Tenarios:
    # Permite hacer un if en una linea
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


# Complejidad algoritmica:

# 