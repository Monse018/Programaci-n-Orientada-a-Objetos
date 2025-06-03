#La abstracción permite ocultar la complejidad interna y mostrar solo lo esencial al usuario.
#Ejemplo
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "¡Miauu!"

# Uso
mi_gato = Gato()
print(mi_gato.sonido()) 