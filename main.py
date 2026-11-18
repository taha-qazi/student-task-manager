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
            # delete-task hook — implemented on the feature/delete-task branch
            print("Delete task is not available yet.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
