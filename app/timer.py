import time
from threading import Thread
from tkinter import messagebox

class Timer:
    def __init__(self, task, callback):
        self.task = task
        self.callback = callback
        self.running = False

    def start(self):
        self.running = True
        Thread(target=self._run_timer, daemon=True).start()

    def _run_timer(self):
        time_left = self.task.time_limit
        while time_left > 0 and self.running:
            time.sleep(1)
            time_left -= 1

        if self.running:
            self.task.mark_completed()
            self.callback(self.task)

    def stop(self):
        self.running = False

    @staticmethod
    def show_alarm(task):
        messagebox.showinfo("Time's up!", f"Time limit for '{task.name}' has expired!")