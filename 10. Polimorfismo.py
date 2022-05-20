'''Poliformismo

* La habilidad de tomar varias formas 
* En Python, nos permite cambiar el comportamiento de una superclase
  para adaptarlo a la subclase

'''

# Ejemplo:

class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Estoy caminando')

# Extiende persona:
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')


# Ejecución:
# Punto de entrada
def main():
    persona = Persona('Davida')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__=='__main__':
    main()