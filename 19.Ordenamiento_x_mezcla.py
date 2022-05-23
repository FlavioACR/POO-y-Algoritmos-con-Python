# MERGE SORT.
'''
* Primero divide las listas en partes iguales hasta que quedan sublistas
  de 1 a 0 elementos. Luego las recombina en forma ordenada.

'''

import random
# Ordenamiento recursivo:
def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        # Dividimos a la mitad:
        medio = len(lista) // 2
        # Creamos lista izq y lista der ahora tenemos dos:
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Haremos una llamada recursiva en cada una de las dos listas:
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Inicializamos variables (Iteradores para recorrer las sublistas):
        i = 0
        j = 0
        # Iterar en la lista principal
        k = 0

        # Primeras comparaciones entre las dos listas:
        while 


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)