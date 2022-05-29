
def morral(tamano, pesos, valores, n):
    '''Esta función resive 4 paramentros:

    tamano = Tamaño del morral
    pesos = Peso de los elementos
    valores = Valor de los elementos
    n = Indice actual que representa el elemento.
    '''
# Caso base 1:
# Si no quedad mas elementos o si el tamaño del morral es cero, es decir no queda mas espacio, retornar 0:
    if n == 0 or tamano == 0:
        return 0
# Caso base 2:
# Si el elemento es mas grande que el tamaño del morral disponible
# hacer un retorno de manera recursiva, utilizando la propia función pero 
# haciendo referencia al siguiente valor de los indices:        
    if pesos[n - 1] > tamano:
        # f recursiva
        return morral(tamano, pesos, valores, n -1)

# Caso final:
# Comparar si lo no o no el valor que se obtendria mximo:
    return max(valores[n -1] + morral(tamano - pesos[n -1], pesos, valores, n -1),
                morral(tamano, pesos, valores, n - 1)
    )






if __name__ == '__main_':
    valores = [60,100,120]
    pesos = [10,20,30]
    tamano = 50
    n = len(valores)

    resultado = morral(tamano, pesos, valores, n)
    print(resultado)