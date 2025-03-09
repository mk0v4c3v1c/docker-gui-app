import tkinter as tk
from app.main import TaskManagerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()