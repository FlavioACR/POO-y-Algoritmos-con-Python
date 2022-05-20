'''Encapsulación
* Permite agrupar datos y su comportamiento.
* Controla el acceso a dichos datos
* Previene modificacioens no autorizadas
* Programación defenciba
'''
# Ejemplo: Casilla de votación:

class CasillaDeVotacion:

    # Inicializamos:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    # Definimos un decorador, llamado property
    # definida con el docnotation, redefiniendola como 
    # una propiedad:

    # Se accede a la variable privada ._region mediante
    # el uso de un getters, con docnotations property
    # y usando la sintaxis de un decorador @ (@property):
    @property
    def region(self):
        return self._region
    
    # Este proceso permite modificar o evaluar la condición
    # una variable privada.
    @region.setter
    def region(self, region):
        # Evalua si la región es permitida dentro del pais
        # o cualquir otro hecho para acceder a las variables:
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es validad
            en un {self._pais}')
            
    


