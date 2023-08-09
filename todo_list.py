from datetime import date

class UserTask:
    def __init__(self, title, priority, state = "Doing", date = date.today()):
        self.title = title
        self.priority = priority
        self.state = state
        self.date = date
    
    def markedCompleted(self):
        self.state = "Completed"
    
    def edit_title(self, title):
        self.title = title

    def edit_priority(self, priority):
        self.priority = priority

class TodoList:

    def __init__(self):
        self.tasks = []

    def addTask(self, title, priority):
        self.tasks.append(UserTask(title, priority))
    
    def showTasks(self):
        index = 1
        print("\nID | TITLE | PRIORITY | STATE | DATE")
        for task in self.tasks:
            print(index, task.title, task.priority, task.state, task.date)
            index += 1

    def markedTaskCompleted(self, title):
        for task in self.tasks:
            if task.title == title:
                task.markedCompleted()
                return
        print("Not found task: " + title)
    
    def clearTasks(self):
        self.tasks = []

    def deleteTask(self, idTask):
        del self.tasks[idTask - 1]

    def clearTasks(self):
        self.tasks = []

if __name__ == "__main__":
    todolist = TodoList()
    while True:
        print(f"1. Add task\n2. List all tasks\n3. Mark task as completed\n4. Delete Task\n5. Clear all tasks\n6. Exit app")

        userOption = int(input("Enter a option: "))

        if userOption == 1:
            taskTitle = input("Enter task name: ")
            taskPriority = input("Enter task priority: ")
            todolist.addTask(taskTitle, taskPriority)

        elif userOption == 2:
            todolist.showTasks()

        elif userOption == 3:
            todolist.showTasks()
            taskTitle = input("Enter task name: ")
            todolist.markedTaskCompleted(taskTitle)

        elif userOption == 4:
            todolist.showTasks()
            taskId = int(input("Enter id task: "))
            todolist.deleteTask(taskId)

        elif userOption == 5:
            todolist.clearTasks()

        elif userOption == 6:
            break
        else:
            print("Invalid option")
    print("Thanks for using this software.")