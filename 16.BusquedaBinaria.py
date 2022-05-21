#
# Divid y conquista
# El problema se divide en dos en cada iteración
# el algoritmo asume que la lista esta en orde
# Cual es el pero caso?
# se requier eun alista ordenaa

import random

def  buesqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    if comienzo > final:
        return False

    # división de entreos:
    # Medio es igual a la suma de el indice inicial al indice final entre 2 absoluto
    medio = (comienzo + final) // 2

    # Si la lisa es igual a medio retornamos verdadero
    if lista[medio] == objetivo:
        return True
    # O si el indice medio de la lista  es menor al objetivo de busqueda:
    elif lista[medio] < objetivo:
        # Retorna la aplicación de la misma función con una modificaciónde las
        # el comienzo a hora se convierte en el medio mas 1 ´pr:::: 
        return buesqueda_binaria(lista, medio + 1, final, objetivo)
    # elif lista[medio] > objetivo:
    #     # Retorna la aplicación de la misma función con una modificaciónde las
    #     # explicar esto
    #     return buesqueda_binaria(lista, comienzo, final - 1, objetivo)
    else:
        return buesqueda_binaria(lista, comienzo, final - 1, objetivo)
    



if __name__ == '__main__':
    tamaño_lista = int(input('Tamaño de lista'))
    objetivo = int(input('Numero a encontrar'))

    lista = sorted([random.randint(0,100) for i in range(tamaño_lista)])
    encontrado = buesqueda_binaria(lista, 0, len(lista), objetivo)
    
    print(lista)
    # Operadores Tenarios:
    # Permite hacer un if en una linea
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

