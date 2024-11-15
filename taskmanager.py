# JOHN RICO CAGALITAN
# JANCEE ROD COLEGIO
# IRISH MAE TAGAYLO

"""
JANCEE 
    add task
    view task

RICO
    filter task
    edit task

IRISH
    mark as complete
    delete task
"""

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def edit(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"[{'✔' if self.completed else ' '}] {self.name}"


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def menu(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a Task")
            print("2. View All Tasks")
            print("3. Filter Tasks (Completed/Incomplete)")
            print("4. Edit a Task")
            print("5. Mark a Task as Complete")
            print("6. Delete a Task")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                task_name = input("Enter the task name: ")
                self.add_task(task_name)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                filter_choice = input("View (completed/incomplete) tasks: ").lower()
                if filter_choice in ["completed", "incomplete"]:
                    self.view_tasks(filter_choice)
                else:
                    print("Invalid filter option.")
            elif choice == "4":
                try:
                    index = int(input("Enter task number to edit: ")) - 1
                    new_name = input("Enter the new name for the task: ")
                    self.edit_task(index, new_name)
                except ValueError:
                    print("Invalid input.")
            elif choice == "5":
                try:
                    index = int(input("Enter task number to mark as complete: ")) - 1
                    self.mark_task_complete(index)
                except ValueError:
                    print("Invalid input.")
            elif choice == "6":
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("Invalid input.")
            elif choice == "7":
                print("Exiting To-Do List Manager.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ToDoListManager()
    manager.menu()
