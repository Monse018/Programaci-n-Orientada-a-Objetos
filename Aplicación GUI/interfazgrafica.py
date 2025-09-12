import tkinter as tk
from tkinter import ttk, messagebox

def agregar():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    ciudad = ciudad_entry.get()
    if not nombre or not edad or not ciudad:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número")
        return
    tabla.insert('', tk.END, values=(nombre, edad, ciudad))
    limpiar()

def limpiar():
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    ciudad_entry.delete(0, tk.END)
    nombre_entry.focus()

def eliminar():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar")
        return
    tabla.delete(seleccionado)

root = tk.Tk()
root.title("Información Personal")
root.geometry("600x400")
root.configure(bg="lightblue")  # Fondo de la ventana

tk.Label(root, text="Nombre:", bg="lightblue", fg="darkblue").grid(row=0, column=0, pady=5, sticky=tk.W)
nombre_entry = tk.Entry(root, bg="white", fg="black")
nombre_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Edad:", bg="lightblue", fg="darkblue").grid(row=1, column=0, pady=5, sticky=tk.W)
edad_entry = tk.Entry(root, bg="white", fg="black")
edad_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Ciudad:", bg="lightblue", fg="darkblue").grid(row=2, column=0, pady=5, sticky=tk.W)
ciudad_entry = tk.Entry(root, bg="white", fg="black")
ciudad_entry.grid(row=2, column=1, pady=5)

tk.Button(root, text="Agregar", command=agregar, bg="lightgreen", fg="black").grid(row=3, column=0, pady=10)
tk.Button(root, text="Limpiar", command=limpiar, bg="purple", fg="black").grid(row=3, column=1, pady=10)
tk.Button(root, text="Eliminar Seleccionado", command=eliminar, bg="red", fg="white").grid(row=3, column=2, pady=10)

tabla = ttk.Treeview(root, columns=("nombre", "edad", "ciudad"), show="headings", height=8)
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.heading("ciudad", text="Ciudad")
tabla.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
