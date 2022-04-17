import tkinter as tk
from tkinter import ttk  # themed widgets
from tkinter.messagebox import showwarning


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Λίστα εργασιών")
        self.frame_tasks = ttk.Frame(self)
        self.frame_tasks.pack()

        self.tasks = tk.Variable(value=[])
        self.listbox_tasks = tk.Listbox(
            self.frame_tasks, height=10, width=50, listvariable=self.tasks
        )
        self.listbox_tasks.pack(side=tk.LEFT)

        self.scrollbar_tasks = ttk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        # σύνδεση listbox με scrollbar
        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = ttk.Entry(self, width=50)
        self.entry_task.pack(fill="x", expand=True)

        self.button_add_task = ttk.Button(
            self, text="Νέα εργασία", width=45, command=self.add_task
        )
        self.button_add_task.pack(fill="x", expand=True)

        self.button_delete_task = ttk.Button(
            self, text="Διαγραφή εργασίας", width=45, command=self.delete_task
        )
        self.button_delete_task.pack(fill="x", expand=True)

    def add_task(self):
        task = self.entry_task.get()
        if task == "":
            showwarning(title="Σφάλμα!", message="Θα πρέπει να εισάγετε μια εργασία")
        elif task in self.tasks.get():
            showwarning(title="Σφάλμα!", message="H εργασία ήδη υπάρχει στη λίστα")
        else:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(task_index)
        except:
            showwarning(title="Σφάλμα!", message="Θα πρέπει να επιλέξετε μια εργασία")


if __name__ == "__main__":
    app = App()
    app.mainloop()
