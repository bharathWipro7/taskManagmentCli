import json
from datetime import datetime

class TaskManager:
    def __init__(self, db_file='tasks.json'):
        self.db_file = db_file
        self.tasks = self.load_tasks()

    # Load tasks from the JSON file
    def load_tasks(self):
        try:
            with open(self.db_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Save tasks to the JSON file
    def save_tasks(self):
        with open(self.db_file, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Validate date format (YYYY-MM-DD)
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")
            return False

    # Add a new task
    def add_task(self, task_name, due_date, category):
        # Ensure due date is valid
        while not self.validate_date(due_date):
            due_date = input("Enter due date (YYYY-MM-DD): ")

        new_id = max(task['id'] for task in self.tasks) + 1 if self.tasks else 1
        new_task = {"id": new_id, "task": task_name, "due_date": due_date, "category": category}
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    # Remove a task by ID
    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print("Task removed successfully!")

    # List tasks, sorted by due date in descending order
    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x['due_date'], reverse=True)
        return sorted_tasks
