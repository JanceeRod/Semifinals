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