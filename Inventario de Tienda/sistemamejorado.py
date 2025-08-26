import json
import os
from typing import Dict, List, Optional

class Producto:
    """Clase que representa un producto en el inventario"""
    
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nuevo_nombre
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int) -> None:
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio = nuevo_precio
    
    def to_dict(self) -> Dict:
        """Convierte el producto a un diccionario para serialización"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Producto':
        """Crea un producto a partir de un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])
    
    def __str__(self) -> str:
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    """Clase que gestiona el inventario de productos utilizando un diccionario"""
    
    def __init__(self):
        # Usamos un diccionario para almacenar productos por ID
        self._productos: Dict[int, Producto] = {}

    def añadir_producto(self, producto: Producto) -> bool:
        """Añade un nuevo producto al inventario"""
        if producto.id in self._productos:
            return False  # El ID ya existe
        self._productos[producto.id] = producto
        return True
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto por ID"""
        if id_producto not in self._productos:
            return False
        del self._productos[id_producto]
        return True
    
    def actualizar_producto(self, id_producto: int, cantidad: Optional[int] = None, 
                           precio: Optional[float] = None) -> bool:
        """Actualiza la cantidad y/o precio de un producto"""
        if id_producto not in self._productos:
            return False
        
        producto = self._productos[id_producto]
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio
        
        return True
    
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """Busca productos por nombre (búsqueda parcial case-insensitive)"""
        nombre_lower = nombre.lower()
        # Usamos una lista comprehension para filtrar productos
        return [producto for producto in self._productos.values() 
                if nombre_lower in producto.nombre.lower()]
    
    def mostrar_todos(self) -> List[Producto]:
        """Devuelve todos los productos del inventario"""
        return list(self._productos.values())
    
    def guardar_en_archivo(self, nombre_archivo: str = "inventario.json") -> bool:
        """Guarda el inventario en un archivo JSON"""
        try:
            datos = [producto.to_dict() for producto in self._productos.values()]
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False
    
    def cargar_desde_archivo(self, nombre_archivo: str = "inventario.json") -> bool:
        """Carga el inventario desde un archivo JSON"""
        try:
            if not os.path.exists(nombre_archivo):
                return False
            
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
            self._productos.clear()
            for item in datos:
                producto = Producto.from_dict(item)
                self._productos[producto.id] = producto
            
            return True
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            return False

class SistemaInventario:
    """Clase principal del sistema con interfaz de usuario"""
    
    def __init__(self):
        self.inventario = Inventario()
        productos_iniciales = [
            Producto(1, "Laptop HP", 10, 820.60),
            Producto(2, "Mouse Logitech", 25, 19.99),
            Producto(3, "Teclado Mecánico", 15, 99.99),
            Producto(4, "Monitor Samsung", 5, 300.00),
            Producto(5, "Impresora Canon", 7, 150.00),
            Producto(6, "Webcam Logitech", 12, 75.00),
            Producto(7, "Auriculares Sony", 20, 120.00)
        ]
        for producto in productos_iniciales:
            self.inventario.añadir_producto(producto)
        self.cargar_inventario()
    
    def cargar_inventario(self) -> None:
        """Intenta cargar el inventario al iniciar el sistema"""
        if self.inventario.cargar_desde_archivo():
            print("Inventario cargado exitosamente.")
        else:
            print("No se encontró un archivo de inventario existente. Se creará uno nuevo.")
    
    def guardar_inventario(self) -> None:
        """Guarda el inventario antes de salir"""
        if self.inventario.guardar_en_archivo():
            print("Inventario guardado exitosamente.")
        else:
            print("Error al guardar el inventario.")
    
    def mostrar_menu(self) -> None:
        """Muestra el menú principal"""
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
    
    def ejecutar(self) -> None:
        """Ejecuta el sistema principal"""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.añadir_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.actualizar_producto()
            elif opcion == "4":
                self.buscar_producto()
            elif opcion == "5":
                self.mostrar_productos()
            elif opcion == "6":
                self.guardar_inventario()
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def añadir_producto(self) -> None:
        """Interfaz para añadir un nuevo producto"""
        try:
            print("\n--- Añadir Nuevo Producto ---")
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre: ").strip()
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            
            producto = Producto(id_producto, nombre, cantidad, precio)
            
            if self.inventario.añadir_producto(producto):
                print("Producto añadido exitosamente.")
            else:
                print("Error: Ya existe un producto con ese ID.")
        
        except ValueError as e:
            print(f"Error en los datos ingresados: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def eliminar_producto(self) -> None:
        """Interfaz para eliminar un producto"""
        try:
            print("\n--- Eliminar Producto ---")
            id_producto = int(input("ID del producto a eliminar: "))
            
            if self.inventario.eliminar_producto(id_producto):
                print("Producto eliminado exitosamente.")
            else:
                print("Error: No se encontró un producto con ese ID.")
        
        except ValueError:
            print("Error: El ID debe ser un número entero.")
    
    def actualizar_producto(self) -> None:
        """Interfaz para actualizar un producto"""
        try:
            print("\n--- Actualizar Producto ---")
            id_producto = int(input("ID del producto a actualizar: "))
            
            print("Deje en blanco los campos que no desea actualizar:")
            cantidad_str = input("Nueva cantidad: ").strip()
            precio_str = input("Nuevo precio: ").strip()
            
            cantidad = int(cantidad_str) if cantidad_str else None
            precio = float(precio_str) if precio_str else None
            
            if cantidad is None and precio is None:
                print("No se proporcionaron datos para actualizar.")
                return
            
            if self.inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado exitosamente.")
            else:
                print("Error: No se encontró un producto con ese ID.")
        
        except ValueError:
            print("Error: La cantidad debe ser un número entero y el precio un número decimal.")
    
    def buscar_producto(self) -> None:
        """Interfaz para buscar productos por nombre"""
        print("\n--- Buscar Producto por Nombre ---")
        nombre = input("Nombre a buscar: ").strip()
        
        if not nombre:
            print("Error: Debe ingresar un nombre para buscar.")
            return
        
        resultados = self.inventario.buscar_por_nombre(nombre)
        
        if resultados:
            print(f"\nSe encontraron {len(resultados)} producto(s):")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")
    
    def mostrar_productos(self) -> None:
        """Interfaz para mostrar todos los productos"""
        print("\n--- Todos los Productos ---")
        productos = self.inventario.mostrar_todos()
        
        if productos:
            for producto in productos:
                print(producto)
            print(f"\nTotal: {len(productos)} producto(s) en inventario.")
        else:
            print("-----------------")


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.ejecutar()