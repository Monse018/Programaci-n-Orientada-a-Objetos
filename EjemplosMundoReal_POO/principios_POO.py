#Ejemplo 1: Sistema de Reserva de un Hotel 
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero         
        self.tipo = tipo              
        self.precio = precio
        self.disponible = True       

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return "Reserva exitosa"
        return "Habitación ocupada"

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        return self.habitacion.precio * self.dias

# Uso
cliente1 = Cliente("Juan Carlos Enriquez", "0450295863")
habitacion54 = Habitacion(54, "Doble", 120)
print(habitacion54.reservar())  
reserva1 = Reserva(cliente1, habitacion54, 4)
print(f"Total a pagar: ${reserva1.calcular_total()}")  