"""Console interface for the Student Task Manager.

Run with:  python main.py
"""

from task_manager import TaskManager

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
"""


def main():
    manager = TaskManager()

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            # add-task hook — implemented on the feature/add-task branch
            print("Add task is not available yet.")

        elif choice == "2":
            print(manager.display_tasks())

        elif choice == "3":
            # complete-task hook — implemented on the feature/complete-task branch
            print("Complete task is not available yet.")

        elif choice == "4":
            raw_id = input("Enter the ID of the task to delete: ").strip()
            try:
                task_id = int(raw_id)
            except ValueError:
                print("Error: task ID must be a number.")
            else:
                if manager.delete_task(task_id):
                    print(f"Task {task_id} deleted.")
                else:
                    print(f"No task found with ID {task_id}.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
