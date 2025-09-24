import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x350")
        self.tasks = []

        self.root.configure(bg="#e0f7fa")

        self.entry = tk.Entry(root, font=("Arial", 12), bg="#fffde7")
        self.entry.pack(pady=10, padx=10, fill="x")

        self.add_btn = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#81c784", fg="white")
        self.add_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, font=("Arial", 11), selectbackground="#ffb74d", bg="#ffffff")
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.complete_btn = tk.Button(root, text="Marcar Completada", command=self.mark_completed, bg="#64b5f6", fg="white")
        self.complete_btn.pack(side="left", padx=10, pady=5)

        self.delete_btn = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#e57373", fg="white")
        self.delete_btn.pack(side="right", padx=10, pady=5)

        # Botón de salida añadido por un principiante
        self.exit_btn = tk.Button(root, text="Salir", command=self.root.quit, bg="#bdbdbd", fg="black")
        self.exit_btn.pack(pady=5)

        self.listbox.bind("<Double-Button-1>", self.toggle_task_status)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_list()
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea.")

    def mark_completed(self):
        idx = self.listbox.curselection()
        if idx:
            self.tasks[idx[0]]["completed"] = True
            self.update_list()

    def delete_task(self):
        idx = self.listbox.curselection()
        if idx:
            del self.tasks[idx[0]]
            self.update_list()

    def toggle_task_status(self, event):
        idx = self.listbox.curselection()
        if idx:
            self.tasks[idx[0]]["completed"] = not self.tasks[idx[0]]["completed"]
            self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            color = "#bdbdbd" if task["completed"] else "#212121"
            self.listbox.insert(tk.END, task["text"])
            self.listbox.itemconfig(tk.END, fg=color)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
