'''
Crecimiento asintónico (conforme crece al infinito)
# los terminos cuadraticos de vuelven los inportantes

* No importan variaciones pequeñas
* El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
* Mejor de los casos, promedio, peor delos casos
* Big O (Notación Solo importa el termino dde mayor tamaño)
* Nada más importa el termino de mayor tamaño
'''

# Ley de la suma:

def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        prin(i)

# Bigs 'O'
# O(n) + O(n) = O(n + n) <- Ley de la suma  = O(2n) = O(n)
# Crecimiento lineal acorde a el valor de n o el O(n)

# Segundo ejemplo ley de la suma:

def f(n):

    for i in range(n):
        print(i)

    for i in range(n * n):
        # Crece al cuadrado 
        prin(i)

# Ecuación:
#           O(n) + O(n * n) = O(n + n2) = O(n2)
# Para llegar al la expresión final se considera solamente el valor mas grande.

# Ley de la multiplicación:

def f(n):

    for i in range(n):
        
        for j in range(n):
            prin(i, j)

# Cuando se tiene un loop dentro de otro loop los valores de multiplican, ambos crecen igual 
# pero multiplicados:

# 0(n) * 0(n) = O(n * n) = 0(n2)


# Recursivida multiple:

def fibonacci(n):

    if n == 0 or n == 1:
        return 1
    return fibonacci(n -1) + fibonacci(n - 2)
# Cada ves que se ejecuta la función realmente se aplica dos veces por cada n
# 0(2**n)

# Crecimiento exponencial.