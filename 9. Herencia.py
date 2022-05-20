'''HERENCIA
* Permite modelar una jerarquia de clases
* Permite compartir comportamiento entre clase
* Al padre se le conoce como superclase y al hijo como subclase y puede 
    heredar sus atributos  o métodos.

'''

'''Ejemplo:'''

class Rectangulo:
    # Constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Metodos:
    def area(self):
        return self.base * self.altura

#Generando herencia: La clase cuadraso extiende al rectangulo convirtiendola en su superclass.
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        #Hacemos referencia a la clase padre o superclase.
        #Permite obtener un a referncia directa de la superclase, lo que nos permite
        # llamar al constructor de la clase padre.
        # utilizando el constructor de la clase padre.
        # En lugar de pasar una base y una altura como parametro ahora estamos pasando lado a las dos entradas
        #       de parametros del constructor.
        super().__init__(lado, lado)

if __name__=='__main__':
    # Generamos rectagulo
    rectangulo = Rectangulo(base=3,altura=4)
    print(rectagulo.area())

    # con esta herencia podemos usar el metodo de la superclase(padre):
    cuadrado = cuadrado(lado=3)
    print(cuadrado.area())