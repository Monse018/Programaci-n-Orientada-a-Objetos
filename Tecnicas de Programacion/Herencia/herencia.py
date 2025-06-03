#Reutiliza el código de una clase padre.
#Ejemplo Clase Vehiculo y Subclase Coche 
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        return f"Vehículo de marca {self.marca}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def descripcion(self):
        return f"Auto: {self.marca} {self.modelo}"

# Uso
mi_auto = Auto("Toyota", "Hilux")
print(mi_auto.descripcion())  