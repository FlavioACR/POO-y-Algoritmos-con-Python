'''Adstracción:

* Enfocarnos en la información relevante, iteractuando con otros objetos.
* Separar la información central de los detalles secundarios.
* Podemos utilizar variables y métodos (privados o públicos).

Ejemplo:
Cuando manejas no te preocupas por el funcionamiento del motor o cuando usas un elevador solo te preocupas en usar el 
elevador pero no en su funcionamiento de el sistema y poleas.

Para hacer esto se genera una interfaz para interactuar con las clases.


'''

# Ejemplificación:

class Lavadora:

    def __init__(self):
        pass
    
    # Metodo publico:
    def lavar(self, temperatura='caliente'):
        # Al usuario no le interesa el funcionamiento,
        # por lo cual se usaran variables privadas.
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._sentrifugar()

