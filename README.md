# Task Managment CLI

This is a command-line task manager application that allows users to add, remove, and list tasks. It uses a simple file-based database (tasks.json) for storing tasks and leverages the tabulate library for clean tabular display.

Features
Add Task: Allows users to add new tasks with a name, due date, and category.
Remove Task: Allows users to remove tasks by their ID.
List Tasks: Displays all tasks in a neatly formatted table, sorted by due date (in descending order).
Persistent Storage: Task data is stored in a tasks.json file, ensuring that tasks are preserved between program runs.
