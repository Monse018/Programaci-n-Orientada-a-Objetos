import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        tasks_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea.")

def complete_task():
    selected = tasks_list.curselection()
    if selected:
        idx = selected[0]
        tasks_list.itemconfig(idx, {'fg': 'gray'})
    else:
        messagebox.showinfo("Info", "Selecciona una tarea.")

def delete_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
    else:
        messagebox.showinfo("Info", "Selecciona una tarea.")

def clear_completed():
    for i in reversed(range(tasks_list.size())):
        if tasks_list.itemcget(i, 'fg') == 'gray':
            tasks_list.delete(i)

def show_shortcuts():
    info = (
        "ATAJOS:\n"
        "Enter: Añadir\n"
        "C: Completar\n"
        "E: Eliminar\n"
        "Esc: Salir"
    )
    messagebox.showinfo("Atajos", info)

root = tk.Tk()
root.title("Gestor de Tareas con Atajos")
root.geometry("400x350")
root.configure(bg="#e0f7fa")

entry = tk.Entry(root, font=('Arial', 12), bg="#fffde7")
entry.pack(pady=10, padx=10, fill=tk.X)
entry.focus()

btn_frame = tk.Frame(root, bg="#e0f7fa")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Añadir", bg="#aed581", command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Completar", bg="#12a9f0", command=complete_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Eliminar", bg="#ff8a65", command=delete_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Limpiar Completadas", bg="#ce93d8", command=clear_completed).pack(side=tk.LEFT, padx=5)

tasks_list = tk.Listbox(root, font=('Arial', 12), height=10, selectbackground="#1ba599")
tasks_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(root, text="Enter: Añadir | C: Completar | E: Eliminar | Esc: Salir", 
         bg="#d7d9e7", fg="#D67575", font=('Arial', 9)).pack(pady=5)

root.bind('<Return>', lambda e: add_task())
root.bind('<c>', lambda e: complete_task())
root.bind('<C>', lambda e: complete_task())
root.bind('<e>', lambda e: delete_task())
root.bind('<E>', lambda e: delete_task())
root.bind('<Escape>', lambda e: root.quit())

root.mainloop()
