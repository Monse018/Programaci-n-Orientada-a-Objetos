#Ejemplo 3:Tienda de Celulares
class Producto:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def descripcion(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio}"

class Celular(Producto):  
    def __init__(self, nombre, precio, marca, sistema_operativo):
        super().__init__(nombre, precio, marca)
        self.sistema_operativo = sistema_operativo

    def descripcion(self):  
        return f"Celular {super().descripcion()}, SO: {self.sistema_operativo}"

# Uso
iphone = Celular("iPhone 14", 600, "Apple", "iOS")
print(iphone.descripcion())  