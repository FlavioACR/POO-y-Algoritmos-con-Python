'''DESCOMPOSICIÓN 
* Partir un problema en problemas mas pequeños
* Las clases permiten crear mayores abstracciones en forma de componentes
* Cada clase se encarga de una parte delproblema y del programa se vuelve mas facil de mantener.
'''
# Ejemplo para comprender la descomposición:

# 1 Creamos una clase llamada automovil.
class Automovil:
    # La inicializamos y agregamos atributos de la clase
    def __init__(self, modelo, marca, color):
        # Atributos propios:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        # Metodos privados:
        self._estado = 'en_reposo'
        # Despues de definir las clases de motor y sus funciones
        # Instanciamos una de las clases hijas.
        self._motor = Motor(cilindros=4)

    # Metodos:
    def acelerar(self, tipo='despacio'):
        if tipo = 'rapida':
            # Llamamos a otra clase para regular la inyeccion clase ajena:
            self._motor.inyecta_gasolina(10)
        else:
            # Repetimos el paso if pero con una menor inyección de combustible:
            self._motor.inyecta_gasolina(3)
        # Modifica el estado del automovil.
        self._estado = 'en_movimiento'

class Motor:
    # Parametro por defecto tipo='gasolina', cuando es asi se especifica o no:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        # Metodos privados:
        self._temperatura = 0

    # Metodos:
    # Cantidad = Recibe la cantidad de gasolina.
    def inyecta_gasolina(self, cantidad):
         pass


