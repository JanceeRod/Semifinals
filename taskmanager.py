# JOHN RICO CAGALITAN
# JANCEE ROD COLEGIO
# IRISH MAE TAGAYLO

"""
JANCEE 
    task class
    menu page
    
RICO
    add
    view/filter task
    edit task

IRISH
    mark as complete
    delete task
"""


class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False


class ToDoListManager:
    def __init__(self):
        self.tasks = []
        
        
    def add_task(self, task_name):
        self.tasks.append(Task(task_name))
        print(f"Task '{task_name}' added.")

        
    def view_tasks(self, filter_type=None):
        if filter_type == "completed":
            tasks = [task for task in self.tasks if task.completed]
            print("\nCompleted Tasks:")
        elif filter_type == "incomplete":
            tasks = [task for task in self.tasks if not task.completed]
            print("\nIncomplete Tasks:")
        else:
            tasks = self.tasks
            print("\nAll Tasks:")

        if tasks:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks found.")

            
    def edit_task(self, index, new_name):
        if 0 <= index < len(self.tasks):
            old_name = self.tasks[index].name
            self.tasks[index].edit(new_name)
            print(f"Task '{old_name}' updated to '{new_name}'.")
        else:
            print("Invalid task number.")

        def mark_complete(self):
            self.completed = True

        def edit(self, new_name):
            self.name = new_name

        def __str__(self):
            return f"[{'✔' if self.completed else ' '}] {self.name}"

          
    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].name}' marked as complete.")
        else:
            print("Invalid task number.")

            
    def delete_task(self, index):
            if 0 <= index < len(self.tasks):
                task_name = self.tasks.pop(index).name
                print(f"Task '{task_name}' deleted.")
            else:
                print("Invalid task number.")
    
    
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