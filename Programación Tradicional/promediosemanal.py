#Programación Tradicional
def ingresar_temperaturas():
    """Solicitar al usuario que ingrese las temperaturas de la semana."""
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    print("Programa para calcular el promedio semanal del clima")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

#Programación Orientada a Objetos
class ClimaSemanal:
    """Clase para representar el clima de una semana."""
    
    def __init__(self):
        """Ingresar la lista de temperaturas."""
        self.temperaturas = []
    
    def ingresar_temperaturas(self):
        """Solicitar al usuario que ingrese las temperaturas de la semana."""
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temp)
    
    def calcular_promedio(self):
        """Calcula el promedio de temperaturas."""
        return sum(self.temperaturas) / len(self.temperaturas)
    
    def mostrar_promedio(self):
        """Mostrar el promedio semanal."""
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

def main():
    print("Programa para calcular el promedio semanal del clima (POO)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

if __name__ == "__main__":
    main()