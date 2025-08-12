from producto import Producto

class Inventario:
    # Clase que gestiona una colección de productos
    
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
            raise ValueError(f"Ya existe un producto con ID {producto.id}")
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
        print(f"No se encontró producto con ID {id_producto}")
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
        """Muestra todos los productos en el inventario"""
        if not self._productos:
            print("El inventario está vacío.")
            return
        
        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self._productos:
            print(producto)
        print(f"Total de productos: {len(self._productos)}\n")
        
def main():
    """Función principal que maneja la interfaz de usuario"""
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