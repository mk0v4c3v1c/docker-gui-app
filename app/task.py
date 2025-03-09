class Task:
    def __init__(self, name, time_limit):
        self.name = name
        self.time_limit = time_limit  # Time limit per seconds
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name} | Time Limit: {self.time_limit}s | Status: {status}"