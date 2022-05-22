# Algoritmos de Ordenación.
# ORDENAMIENTO BURBUJAor $ ( Bubble Sort):
    # Es un algoritmo que recorre repetidamiente una lista que necesita 
    # ordenarse. Compara elementos adyacentes y los intercambia si estan en
    # el orden incorrecto. Este procedimiento se repite hasta que nose
    # se requieren intercambios, lo que indica que la lista se encuentra 
    # ordenada.

# Es importante visualizar lo que pasará siempre antes de ejecutar un algoritmo.
# La primera ronda de este tipo de ordenamiento grantiza encontrar el may

import random

def ordenamiento_burbuja(lista):
    # Tamaño de la la lista.
    n = len(lista)
    print(f'El tamaño de la lista es de {n} caracteres')
    print(lista)

    # Se realizará un ciclo por cada caracter de la lista:
    for i in range(n):
        print(f'Recorriendo el elemento numero {i+1} de la lista ')
        print(f'El elemento numero {i+1} de la lista es: {lista[(i)]}\n')
        # Dentro del ciclo superior se hará un ciclo
        # en un rango que inicie en cero y que termina en:
        #   n(# tamaño total de la lista) 
        # - i(# elemento a recorrer de la lista)
        # - 1 (# elemento ya recorrido)
        # Basicamente es restarle al indice recorrido un 1 para eliminar el indice previamente recorrido y reducir el tamaño de la lista e recorrer
        for j in range(0 , n - i -1):
            # print(f'Comparando con el elemento {j} de la lista el cual es {lista[j]}')
            # Si el elemento lista es mayor al elemento que le procede:
            if lista[j] > lista[j + 1]:
                # Si se cumple se hace swaping para intercabiar values:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f'El elemento {lista[j+1]} es mayor que {lista[j]}\n por lo cual seran intercambiados')
    return lista                



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

# COMPLEJIDAD ALGORITNMICA: 
# Crecimiento cuadratico:  O(n**2)
# Entre mas crezca la lista es muy dificil su eficiencia.