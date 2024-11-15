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