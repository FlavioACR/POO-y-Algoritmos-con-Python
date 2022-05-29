''' * El concepto de optimización permite resolver muchos problemas de manera computacional
* Una función objetivo que debemos de maximizar o minimizar (entrada o salida)
* Una serie de limitantes que debemos de respetar '''

'''
El problema del morral:

'''
def morral(tamano, pesos, valores, n):
    
    # Si no hay elementos y si no hay espacio retornar 0
    if n == 0 or tamano == 0:
        return 0

    # Si el peso del elemento n, es mayor al tamaño del morral:
    if pesos[n - 1] > tamano:
        # Retornar la función pero aplicando un menos uno al elemento n,
        return morral(tamano, pesos, valores, n -1)

    return max(valores[n - 1] + morral(tamano - pesos[n -1], pesos, valores, n - 1),
                morral(tamano, pesos, valores, n -1))  


 
# agregar print statmrn 



if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos= [10, 20, 30]
    # Constraings:
    tamano = 50
    n = len(valores)

    # Valor maximo.
    resultado = morral(tamano, pesos, valores, n)
    print(resultado)