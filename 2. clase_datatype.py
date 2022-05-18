# Ejemplo de estructura de una clase:

# Ejemplo:

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso:
# Instanciamo la clase, definiendo la y llamandola en una variable:
david = Persona('David', 35)
erika = Persona('Erika', 32)

# Instanciamos los metodos:
david.saluda(erika)

def información_instancias():
    '''Imprime la información relevante sobre las Instancias:
    
    * Mientras que una clase es un molde, a los objetos creados se les 
      conoce como instancias.
    * Cuando se crea una instancia, se ejecuta el método __init__
    * Todos los elementos de una clase reciben implicitamente como primer 
      parametro self.
    '''
    
    return help(información_instancias())