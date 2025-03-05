import sys
from tabulate import tabulate
from task_manager import TaskManager


def display_tasks(tasks):
    # Prepare the table headers and data
    headers = ["ID", "Task", "Due Date", "Category"]
    task_data = [(task['id'], task['task'], task['due_date'], task['category']) for task in tasks]

    # Use tabulate to format the table
    table = tabulate(task_data, headers, tablefmt="grid")

    # Print the formatted table
    print(table)


def main():
    task_manager = TaskManager()

    while True:
        tasks = task_manager.list_tasks()
        display_tasks(tasks)

        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            task_manager.add_task(task_name, due_date, category)
        elif choice == '2':
            try:
                task_id = int(input("Enter task id to remove: "))
                task_manager.remove_task(task_id)
            except ValueError:
                print("Invalid task ID entered.")
        elif choice == '3':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
