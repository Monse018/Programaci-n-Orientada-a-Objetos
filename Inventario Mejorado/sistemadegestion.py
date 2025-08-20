import os
import json
from datetime import datetime

class Producto:
    """Clase que representa un producto en el inventario"""
    
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
    
    def to_dict(self):
        """Convierte el producto a un diccionario para serialización"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un producto a partir de un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])


class Inventario:
    """Clase que gestiona el inventario de productos con persistencia en archivos"""

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {1: Producto("001", "Laptop HP", 10, 820.60), 2: Producto("002", "Mouse Logitech", 25, 19.99), 3: Producto("003", "Teclado Mecánico", 15, 99.99), 4: Producto("004", "Monitor Samsung", 5, 300.00), 5: Producto("005", "Impresora Canon", 7, 150.00), 6: Producto("006", "Webcam Logitech", 12, 75.00), 7: Producto("007", "Auriculares Sony", 20, 120.00)}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo, manejando posibles excepciones"""
        try:
              # Verificar si el archivo existe
            if not os.path.exists(self.archivo):
                print(f"El archivo {self.archivo} no existe. Se creará uno nuevo al guardar.")
                self.guardar_inventario()
                return

            # Intentar abrir y leer el archivo
            with open(self.archivo, 'r') as f:
                contenido = f.read().strip()

             # Si el archivo está vacío
                if not contenido:
                    print("El archivo de inventario está vacío.")
                    return

                print(f"Inventario cargado exitosamente desde {self.archivo}")
                
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no fue encontrado.")
        except PermissionError:
            print(f"Error: No tiene permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {str(e)}")
    
    def guardar_inventario(self):
        """Guarda el inventario en el archivo, manejando posibles excepciones"""
        try:
            # Convertir los productos a una lista de diccionarios
            datos = [producto.to_dict() for producto in self.productos.values()]
            
            # Guardar en el archivo
            with open(self.archivo, 'w') as f:
                json.dump(datos, f, indent=4)
            
            print(f"Inventario guardado exitosamente en {self.archivo}")
            return True
            
        except PermissionError:
            print(f"Error: No tiene permisos para escribir en el archivo {self.archivo}.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {str(e)}")
            return False
    
    def añadir_producto(self, id, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario y guarda en el archivo"""
        if id in self.productos:
            print("Error: Ya existe un producto con ese ID.")
            return False
        
        try:
            cantidad = int(cantidad)
            precio = float(precio)
            
            if cantidad < 0 or precio < 0:
                print("Error: La cantidad y el precio deben ser valores positivos.")
                return False
            
            self.productos[id] = Producto(id, nombre, cantidad, precio)
            
            if self.guardar_inventario():
                print("Producto añadido exitosamente.")
                return True
            else:
                # Si no se pudo guardar, revertir la operación
                del self.productos[id]
                print("Error: No se pudo guardar el producto en el archivo.")
                return False
                
        except ValueError:
            print("Error: La cantidad debe ser un número entero y el precio un número válido.")
            return False
    
    def eliminar_producto(self, id):
        """Elimina un producto del inventario y guarda en el archivo"""
        if id not in self.productos:
            print("Error: No existe un producto con ese ID.")
            return False
        
        producto = self.productos[id]
        del self.productos[id]
        
        if self.guardar_inventario():
            print(f"Producto '{producto.nombre}' eliminado exitosamente.")
            return True
        else:
            # Si no se pudo guardar, revertir la operación
            self.productos[id] = producto
            print("Error: No se pudo eliminar el producto del archivo.")
            return False
    
    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza un producto del inventario y guarda en el archivo"""
        if id not in self.productos:
            print("Error: No existe un producto con ese ID.")
            return False
        
        producto = self.productos[id]
        
        try:
            if cantidad is not None:
                cantidad = int(cantidad)
                if cantidad < 0:
                    print("Error: La cantidad debe ser un valor positivo.")
                    return False
                producto.cantidad = cantidad
            
            if precio is not None:
                precio = float(precio)
                if precio < 0:
                    print("Error: El precio debe ser un valor positivo.")
                    return False
                producto.precio = precio
            
            if self.guardar_inventario():
                print("Producto actualizado exitosamente.")
                return True
            else:
                print("Error: No se pudo actualizar el producto en el archivo.")
                return False
                
        except ValueError:
            print("Error: La cantidad debe ser un número entero y el precio un número válido.")
            return False
    
    def buscar_por_nombre(self, nombre: str):
        """
        Busca productos por nombre (coincidencias parciales)
            nombre (str): Nombre o parte del nombre a buscar
            list: Lista de productos que coinciden
        """
        nombre = nombre.lower()
        return [p for p in self.productos.values() if nombre in p.nombre.lower()]

    def listar_productos(self):
        """Lista todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        print("\n--- Inventario Actual ---")
        for producto in self.productos.values():
            print(producto)
        print("-------------------------\n")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== Sistema de Gestión de Inventarios ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar todos los productos")
    print("6. Guardar inventario")
    print("7. Salir")
    print("=========================================")


def main():
    """Función principal del programa"""
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\n--- Añadir nuevo producto ---")
            try:
                id = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = input("Cantidad: ")
                precio = input("Precio: ")
                inventario.añadir_producto(id, nombre, cantidad, precio)
            except Exception as e:
                print(f"Error inesperado: {str(e)}")
        
        elif opcion == '2':
            print("\n--- Eliminar producto ---")
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        
        elif opcion == '3':
            print("\n--- Actualizar producto ---")
            id = input("ID del producto a actualizar: ")
            
            # Verificar si el producto existe
            producto = inventario.buscar_producto(id)
            if producto:
                print("Deje en blanco los campos que no desea modificar:")
                cantidad = input(f"Nueva cantidad (actual: {producto.cantidad}): ")
                precio = input(f"Nuevo precio (actual: {producto.precio:.2f}): ")
                
                # Convertir campos vacíos a None
                cantidad = cantidad if cantidad.strip() else None
                precio = precio if precio.strip() else None
                
                inventario.actualizar_producto(id, cantidad, precio)
        
        elif opcion == "4":
                # Buscar producto por nombre
                print("\n--- BUSCAR PRODUCTO ---")
                nombre = input("Nombre o parte del nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
        
        elif opcion == '5':
            inventario.listar_productos()
        
        elif opcion == '6':
            inventario.guardar_inventario()
        
        elif opcion == '7':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()