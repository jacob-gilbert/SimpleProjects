class Task:
    def __init__(self, name, priority, notes):
        self.name = name
        self.priority = priority
        self.notes = notes
        self.completed = False
        
    def get_name(self):
        return self.name
    
    def get_priority(self):
        return self.priority
    
    def get_notes(self):
        return self.notes
    
    def get_completion_status(self):
        return self.completed
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_priority(self, new_priority):
        self.priority = new_priority
    
    def set_notes(self, new_notes):
        self.notes = new_notes
    
    def set_completion_status(self, new_completed):
        self.completed = new_completed

task_list = []
completed_list = []
keep_going = True
print("Welcome to your to-do list!\nYou can add, delete, view, and mark tasks as complete, and you can see your completed tasks")
while keep_going:
    answer = input("What would you like to do:\na) Add Task\nb) View Tasks\nc) Delete Task\nd) Mark Task Complete\ne) View Completed Tasks\nf) Exit\n")
    if answer == "a":
        name = input("Enter the name of your task\n")
        priority = input("Enter the priority of your task where 1 is most important and 100 is least important\n")
        notes = input("Enter any notes you would like to include about the task\n")
        print("Adding task...")
        temp_task = Task(name, priority, notes)
        task_list.append(temp_task)
        
    elif answer == "b":
        # check the number of tasks in the list, if its zero tell the user there are not tasks, otherwise print the list of tasks
        num_tasks = len(task_list)
        if num_tasks == 0:
            print("No tasks found")
            
        for i in range(num_tasks):
            print(f"{i + 1}: {task_list[i].get_name()}")
    
    elif answer == "c":
        # get the name of the task to be deleted
        name = input("Enter the name of the task you would like to delete\n")
        task_deleted = False
        print("Finding task...")
        
        # iterate through task list to find tasks with the given name
        for i in range(len(task_list)):
            temp_task = task_list[i]
            if temp_task.get_name() == name:
                print(f"Identified Task {name} with priority {temp_task.get_priority()} and notes {temp_task.get_notes()}")
                delete_task = input("Should this task be deleted? (y/n)\n")
                
                # task is set to be deleted so delete task and stop searching
                if delete_task == "y":
                    task_list.pop(i)
                    task_deleted = True
                    break
                
                # do not delete the found task
                elif delete_task == "n":
                    continue
                else:
                    print("Incorrect input, task will not be deleted, restarting...")
                    break
        
        # inform user whether or not their task was deleted            
        if not task_deleted:
            print("Could not find specified task")
        else:
            print("Task Successfully Deleted")
            
    elif answer == "d":
        # get the name of the task to be deleted
        name = input("Enter the name of the task you would like to mark as complete\n")
        task_completed = False
        print("Finding task...")
        
        # iterate through task list to find tasks with the given name
        for i in range(len(task_list)):
            temp_task = task_list[i]
            if temp_task.get_name() == name:
                print(f"Identified Task {name} with priority {temp_task.get_priority()} and notes {temp_task.get_notes()}")
                complete_task = input("Should this task be marked as complete? (y/n)\n")
                
                # task is set to be deleted so delete task and stop searching
                if complete_task == "y":
                    temp_task.set_completion_status(True)
                    task_deleted = True
                    
                    # add task to completed task list
                    completed_list.append(temp_task)
                    
                    # remove task from task list
                    task_list.pop(i)
                    
                    break
                
                # do not delete the found task
                elif complete_task == "n":
                    continue
                else:
                    print("Incorrect input, task will not be marked as complete, restarting...")
                    break
        
        # inform user whether or not their task was deleted            
        if not task_completed:
            print("Could not find specified task")
        else:
            print("Task Successfully Marked as Complete")
            
    elif answer == "e":
        # check the number of tasks in the list, if its zero tell the user there are not tasks, otherwise print the list of completed tasks
        num_tasks = len(completed_list)
        if num_tasks == 0:
            print("No tasks found")
            
        for i in range(num_tasks):
            print(f"{i + 1}: {completed_list[i].get_name()}")
        
    elif answer == "f":
        keep_going = False
        print("Exitting To-Do List...")
    else:
        print("Invalid input, try again")