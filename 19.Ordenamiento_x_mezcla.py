# MERGE SORT.
'''
* Primero divide las listas en partes iguales hasta que quedan sublistas
  de 1 a 0 elementos. Luego las recombina en forma ordenada.

'''

import random
# Ordenamiento recursivo:
def ordenamiento_por_mezcla(lista):
    ''' Este algoritmo consta de dos partes'''
    if len(lista) > 1:
        '''Inici Parte 1:
        Esta parte pemite subdividir la listas en listas cada ves mas pequeñas
        hasta el punto de no tener mas listas y al ser listas de un solo elemento
        ya se encuentran ordenadas.
        '''
        # Dividimos a la mitad:
        medio = len(lista) // 2
        # Creamos lista izq y lista der ahora tenemos dos:
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Haremos una llamada recursiva en cada una de las dos listas:
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        #'''Final Parte 1:
        #Este codigo cuenta con un crecimiento logaritmico, reduciendo su tamañano cada vez mas
        #'''

        # Inicializamos variables (Iteradores para recorrer las sublistas izq y der):
        i = 0
        j = 0
        # Iterar en la lista principal
        k = 0

        # Primeras comparaciones entre las dos listas:
        while i < len(izquierda) and j < len(derecha):
            # Condicional de los indices i & j de las sublistas:
            if izquierda[i] > derecha[j]:
                # Se cambia el valor de la lista principal:
                lista[k] = izquierda[i]
                i += 1
            else:
                # De ser contrario:
                # Cambiamos el valor del siguiente modo.
                lista[k] = derecha[j]
                j += 1
            # Evitar que se tienda al infinito:
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while i < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1    
    return lista                 



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    #objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)