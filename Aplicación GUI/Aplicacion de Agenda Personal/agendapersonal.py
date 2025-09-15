import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    desc = entry_desc.get()
    if fecha and hora and desc:
        tree.insert('', 'end', values=(fecha, hora, desc))
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos.")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):
            tree.delete(seleccionado)
    else:
        messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")

root = tk.Tk()
root.title("Agenda Personal")
root.configure(bg="#e6f2ff")  # Fondo ventana

# Estilo para Treeview
style = ttk.Style()
style.configure("Treeview", background="#f0f8ff", foreground="#003366", fieldbackground="#f0f8ff")
style.map("Treeview", background=[('selected', '#b3d9ff')])

# Frame para la lista de eventos
frame_lista = tk.Frame(root, bg="#e6f2ff")
frame_lista.pack(padx=10, pady=5)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para entrada de datos
frame_entrada = tk.Frame(root, bg="#e6f2ff")
frame_entrada.pack(padx=10, pady=5)

tk.Label(frame_entrada, text="Fecha:", bg="#e6f2ff", fg="#003366").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy', background="#b3d9ff", foreground="#003366")
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:", bg="#e6f2ff", fg="#003366").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada, bg="#f0f8ff", fg="#003366")
entry_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:", bg="#e6f2ff", fg="#003366").grid(row=2, column=0)
entry_desc = tk.Entry(frame_entrada, bg="#f0f8ff", fg="#003366")
entry_desc.grid(row=2, column=1)

# Frame para botones
frame_botones = tk.Frame(root, bg="#e6f2ff")
frame_botones.pack(padx=10, pady=5)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="#b3d9ff", fg="#003366")
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="#b3d9ff", fg="#003366")
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit, bg="#b3d9ff", fg="#003366")
btn_salir.grid(row=0, column=2, padx=5)

root.mainloop()
