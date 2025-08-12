class Producto:
    # Clase que representa un producto en el inventario

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto
            id_producto (int): Identificador único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad en stock
            precio (float): Precio unitario
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Getters
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def precio(self):
        return self._precio
    
    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")
    
    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    # Clase que gestiona una lista de productos
    
    def __init__(self):
        # Constructor que inicializa una lista vacía de productos
        self._productos = []
    
    def agregar_producto(self, producto: Producto):
        """
        Añade un nuevo producto al inventario
            producto (Producto): Producto a añadir
            ValueError: Si el ID del producto ya existe
        """
        if any(p.id == producto.id for p in self._productos):
            raise ValueError(f"Ya existe un producto con ese ID {producto.id}")
        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido correctamente.")
    
    def eliminar_producto(self, id_producto: int):
        """
        Elimina un producto por su ID
            id_producto (int): ID del producto a eliminar
            bool: True si se eliminó, False si no se encontró
        """
        for i, producto in enumerate(self._productos):
            if producto.id == id_producto:
                nombre = producto.nombre
                del self._productos[i]
                print(f"Producto '{nombre}' eliminado correctamente.")
                return True
        print(f"No se encontró producto con ID {id_producto}")
        return False
    
    def actualizar_producto(self, id_producto: int, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto
            id_producto (int): ID del producto a actualizar
            cantidad (int, optional): Nueva cantidad
            precio (float, optional): Nuevo precio
            bool: True si se actualizó, False si no se encontró
        """
        for producto in self._productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto ID {id_producto} actualizado correctamente.")
                return True
        print(f"No se encontró producto con ese ID {id_producto}")
        return False
    
    def buscar_por_nombre(self, nombre: str):
        """
        Busca productos por nombre (coincidencias parciales)
            nombre (str): Nombre o parte del nombre a buscar
            list: Lista de productos que coinciden
        """
        nombre = nombre.lower()
        return [p for p in self._productos if nombre in p.nombre.lower()]
    
    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if not self._productos:
            print("El inventario está vacío.")
            return
        
        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self._productos:
            print(producto)
        print(f"Total de productos: {len(self._productos)}\n")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    # Función principal que maneja la interfaz de usuario
    inventario = Inventario()
    
    # Lista de productos iniciales para probar
    productos_iniciales = [
        Producto(1, "Laptop HP", 10, 820.60),
        Producto(2, "Mouse inalámbrico", 25, 20.00),
        Producto(3, "Teclado mecánico", 15, 60.25),
        Producto(4, "Monitor 24 pulgadas", 6, 220.10),
        Producto(5, "Auriculares Bluetooth", 18, 65.75),
        Producto(6, "Webcam HD", 10, 30.50),
        Producto(7, "Cables USB", 8, 5.00)
    ]
    
    # Añadir productos iniciales al inventario
    for producto in productos_iniciales:
        inventario.agregar_producto(producto)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                # Añadir nuevo producto
                print("\n--- AÑADIR NUEVO PRODUCTO ---")
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
                
            elif opcion == "2":
                # Eliminar producto
                print("\n--- ELIMINAR PRODUCTO ---")
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
                
            elif opcion == "3":
                # Actualizar producto
                print("\n--- ACTUALIZAR PRODUCTO ---")
                id_producto = int(input("ID del producto a actualizar: "))
                
                print("Deje en blanco los campos que no desea actualizar")
                cantidad = input("Nueva cantidad: ")
                precio = input("Nuevo precio: ")
                
                # Convertir inputs vacíos a None
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                
                inventario.actualizar_producto(id_producto, cantidad, precio)
                
            elif opcion == "4":
                # Buscar producto por nombre
                print("\n--- BUSCAR PRODUCTO ---")
                nombre = input("Nombre o parte del nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                
                if resultados:
                    print("\nResultados de la búsqueda:")
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre.")
                    
            elif opcion == "5":
                # Mostrar inventario completo
                inventario.mostrar_inventario()
                
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
                
            else:
                print("Opción no válida. Por favor seleccione 1-6.")
                
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese datos válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()