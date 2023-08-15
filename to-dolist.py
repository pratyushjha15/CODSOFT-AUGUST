class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print("Task removed:", removed_task)
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
