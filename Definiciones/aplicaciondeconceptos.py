#Ejemplo sobre Sistema de gestión de vehículos que muestran los conceptos de:
#Definición de Clase 
#Definición de Objeto
#Herencia
#Encapsulación
#Polimorfismo

class Vehiculo:
    
    def __init__(self, marca, modelo, año):
        self._marca = marca  
        self.__modelo = modelo  
        self.__año = año  
        self.__kilometraje = 0  
    
    # Métodos getter para atributos privados (encapsulación)
    def get_modelo(self):
        return self.__modelo
    
    def get_año(self):
        return self.__año
    
    def get_kilometraje(self):
        return self.__kilometraje
    
    # Método setter con validación (encapsulación)
    def set_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje >= self.__kilometraje:
            self.__kilometraje = nuevo_kilometraje
        else:
            print("Error: El kilometraje no puede disminuir")
    
    def mostrar_info(self):
        return f"{self._marca} {self.__modelo} ({self.__año})"
    
    def avanzar(self, kilometros):
        """Método que incrementa el kilometraje"""
        self.__kilometraje += kilometros
        print(f"El vehículo ha avanzado {kilometros} km. Kilometraje total: {self.__kilometraje} km")

#Muestra método herencia de la clase Vehiculo

class Coche(Vehiculo):
   
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)  
        self.num_puertas = num_puertas
        self.__tipo_combustible = "Gasolina"  
    
    # Sobrescritura del método mostrar_info (polimorfismo)
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, {self.num_puertas} puertas, combustible: {self.__tipo_combustible}"

#Muestra método de herencia y polimorfismo clase derivada que representa una moto
class Moto(Vehiculo):

    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  
    
    # Sobrescritura del método mostrar_info (polimorfismo)
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Tipo: {self.tipo}"

# Función que demuestra polimorfismo al aceptar diferentes tipos de vehículos
def mostrar_vehiculo(vehiculo):
   
    print("Información del vehículo:", vehiculo.mostrar_info())


# Uso 
if __name__ == "__main__":
    # Creación de objetos
    mi_coche = Coche("Toyota", "Hilux", 2020, 4)
    mi_moto = Moto("Tuko Tk", "Cr300",2026,"Deportiva")
    
    # Mostrar método de encapsulación
    mi_coche.set_kilometraje(15000)
    mi_coche.avanzar(500)  
    
    # Intentar establecer un kilometraje inválido
    mi_coche.set_kilometraje(14000)  
    
    # Acceso a atributos privados a través de métodos getter
    print(f"Modelo del coche: {mi_coche.get_modelo()}")
    print(f"Año de la moto: {mi_moto.get_año()}")
    
    # Mostrar método de polimorfismo
    mostrar_vehiculo(mi_coche)
    mostrar_vehiculo(mi_moto)
    
  