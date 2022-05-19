# DESCOMPOSICIÓN 
#   Partir un problema en problemas mas pequeños
#   Las clases permiten crear mayores abstracciones en forma de componentes
#   Cada clase se encarga de una parte delproblema y del programa se vuelve mas facil de mantener.

# Ejemplo descomponer un automovil:

from curses import noecho


class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        # Despues de definir las clases de motor y sus funciones
        self._motor = None
    
    def acelerar(self, tipo='despacio'):
        

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
         pass


