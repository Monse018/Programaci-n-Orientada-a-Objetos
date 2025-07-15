#Utilizamos el mismo método pero con comportamientos diferentes.
# Metodo Hablar 
class Gato:
    def hablar(self):
        return "¡Miauu!"

class Pato:
    def hablar(self):
        return "¡Cuack!"

def hacer_hablar(animal):
    print(animal.hablar())

# Uso
hacer_hablar(Gato())  
hacer_hablar(Pato())  