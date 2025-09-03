#SISTEMA PARA GESTIONAR UNA BIBLIOTECA DIGITAL 
# Clase para representar un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tuplas para los atributos inmutables
        self.titulo_autor = (titulo, autor)  
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True
    
    def __str__(self):
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]} - {self.categoria} (ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para libros prestados actualmente
        self.libros_prestados = []
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        # Diccionario para libros disponibles (clave: ISBN, valor: objeto Libro)
        self.libros_disponibles = {}
        # Conjunto para IDs de usuario únicos
        self.ids_usuarios = set()
        # Diccionario para usuarios registrados (clave: ID usuario, valor: objeto Usuario)
        self.usuarios_registrados = {}
        # Lista para historial de préstamos
        self.historial_prestamos = []
    
    def añadir_libro(self, libro):
        # Añadir un libro a la biblioteca
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
            return False
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")
        return True
    
    def quitar_libro(self, isbn):
        # Eliminar un libro de la biblioteca
        if isbn not in self.libros_disponibles:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False
        
        libro = self.libros_disponibles[isbn]
        if not libro.disponible:
            print(f"No se puede eliminar el libro '{libro.titulo_autor[0]}' porque está prestado.")
            return False
            
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo_autor[0]}' eliminado correctamente.")
        return True
    
    def registrar_usuario(self, nombre, id_usuario):
        # Registrar un nuevo usuario en la biblioteca
        if id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {id_usuario} ya está registrado.")
            return False
        
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios_registrados[id_usuario] = nuevo_usuario
        self.ids_usuarios.add(id_usuario)
        print(f"Usuario '{nombre}' registrado correctamente con ID {id_usuario}.")
        return True
    
    def dar_baja_usuario(self, id_usuario):
        # Dar de baja a un usuario de la biblioteca
        if id_usuario not in self.ids_usuarios:
            print(f"Usuario encontrado correctamente: {id_usuario}.")
            return False
        
        usuario = self.usuarios_registrados[id_usuario]
        if usuario.libros_prestados:
            print(f"No se puede dar de baja al usuario '{usuario.nombre}' porque tiene libros prestados.")
            return False
            
        del self.usuarios_registrados[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario '{usuario.nombre}' dado de baja correctamente.")
        return True
    
    def prestar_libro(self, isbn, id_usuario):
        # Prestar un libro a un usuario
        if isbn not in self.libros_disponibles:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False
        
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False
        
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        
        if not libro.disponible:
            print(f"El libro '{libro.titulo_autor[0]}' no está disponible.")
            return False
        
        # Realizar el préstamo
        libro.disponible = False
        usuario.libros_prestados.append(libro)
        
        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'préstamo',
            'libro': libro.titulo_autor[0],
            'usuario': usuario.nombre,
            'fecha': '2025-08-28'  
        })
        
        print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre} correctamente.")
        return True
    
    def devolver_libro(self, isbn, id_usuario):
        # Devolver un libro prestado por un usuario
        if isbn not in self.libros_disponibles:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False
        
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False
        
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        
        if libro not in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene prestado el libro '{libro.titulo_autor[0]}'.")
            return False
        
        # Realizar la devolución
        libro.disponible = True
        usuario.libros_prestados.remove(libro)
        
        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'devolución',
            'libro': libro.titulo_autor[0],
            'usuario': usuario.nombre,
            'fecha': '2025-09-01'  
        })
        
        print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre} correctamente.")
        return True
    
    def buscar_libros(self, criterio, valor):
        # Buscar libros por título, autor o categoría
        resultados = []
        
        for isbn, libro in self.libros_disponibles.items():
            if criterio.lower() == 'titulo' and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio.lower() == 'autor' and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio.lower() == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        
        return resultados
    
    def listar_libros_prestados(self, id_usuario):
        # Lista todos los libros prestados a un usuario específico
        if id_usuario not in self.ids_usuarios:
            print(f"Usuario encontrado: {id_usuario}.")
            return None
        
        usuario = self.usuarios_registrados[id_usuario]
        return usuario.libros_prestados

# Uso del sistema con operaciones automáticas
def main():
    print("\n---Sistema de Biblioteca Digital---")
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "111")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "222")
    libro3 = Libro("Python para todos", "Raúl González", "Tecnología", "333")
    libro4 = Libro("Don Quijote", "Miguel de Cervantes", "Novela", "444")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)
    biblioteca.añadir_libro(libro4)

    # Registrar usuarios
    biblioteca.registrar_usuario("Ana Martinez", "A01")
    biblioteca.registrar_usuario("Luis Pérez", "L02")
    biblioteca.registrar_usuario("Carlos Gómez", "C03")

    # Prestar libros
    biblioteca.prestar_libro("111", "A01")  # Ana toma "Cien años de soledad"
    biblioteca.prestar_libro("222", "L02")  # Luis toma "El Principito"
    biblioteca.prestar_libro("333", "A01")  # Ana toma "Python para todos"

    # Buscar libros por categoría
    print("\nLibros en la categoría 'Novela':")
    novelas = biblioteca.buscar_libros("categoria", "Novela")
    for libro in novelas:
        print(f" - {libro}")

    # Listar libros prestados a usuarios
    print("\nLibros prestados a Ana Martinez:")
    libros_ana = biblioteca.listar_libros_prestados("A01")
    for libro in libros_ana:
        print(f" - {libro}")

    # Devolver libro
    print("\nAna devuelve 'Cien años de soledad':")
    biblioteca.devolver_libro("111", "A01")

    # Intentar dar de baja a un usuario 
    print("\n No se puede dar de baja al usuario por que tiene libros prestados:")
    biblioteca.dar_baja_usuario("A01")

    # Devolver libro
    print("\nAna devuelve 'Python para todos':")
    biblioteca.devolver_libro("333", "A01")

    # Dar de baja al usuario
    print("\nUsuario Ana dado de baja correctamente:")
    biblioteca.dar_baja_usuario("A01")

def menu_principal():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Sistema de Gestión de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados a un usuario")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)
        elif opcion == "4":
            id_usuario = input("ID de usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor de búsqueda: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            if resultados:
                print("Resultados encontrados:")
                for libro in resultados:
                    print(f" - {libro}")
            else:
                print("No se encontraron libros.")
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                for libro in libros_prestados:
                    print(f" - {libro}")
            else:
                print(f"El usuario {id_usuario} no tiene libros prestados.")
        elif opcion == "9":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()