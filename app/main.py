import tkinter as tk
from tkinter import messagebox, simpledialog
from .task import Task
from .timer import Timer

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        # GUI komponente
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=5)

    def add_task(self):
        name = simpledialog.askstring("Task Name", "Enter task name:")
        if name:
            time_limit = simpledialog.askinteger("Time Limit", "Enter time limit (in seconds):")
            if time_limit:
                task = Task(name, time_limit)
                self.tasks.append(task)
                self.task_listbox.insert(tk.END, str(task))

    def start_timer(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            timer = Timer(task, self.show_alarm)
            timer.start()
            messagebox.showinfo("Timer Started", f"Timer for '{task.name}' started!")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to start the timer.")

    def show_alarm(self, task):
        Timer.show_alarm(task)
        self.task_listbox.delete(0, tk.END)
        for t in self.tasks:
            self.task_listbox.insert(tk.END, str(t))