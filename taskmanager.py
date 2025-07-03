import os 

task_list = []
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.strip())

while True:
    print("\nMenu:")
    print("Add Task (A)")
    print("View Task (V)")
    print("Delete Task (D)")
    print("Complete Task (C)")
    print("Quit (Q)")
    
    user_choice = input("Choose an option: ").lower()
    
    if user_choice == "a":
        task = input("Enter a task: ")
        task_list.append(task)
        print(f"Task added: {task}")
    
    
    elif user_choice == "v":
        if task_list:
            print("\nTask List:")
            for index, task in enumerate(task_list, 1):
                print(f"{index}. {task}")
        else:
            print("Task list is empty.")
        
    
    elif user_choice == "d":
        if task_list:
            print("\nTask List:")
            for index, task in enumerate(task_list, 1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the number of the task to delete: "))
            if 1 <= task_index <= len(task_list):
                deleted_task = task_list.pop(task_index - 1)
                print(f"Task deleted: {deleted_task}")
            else:
                print("Invalid task number.")
        else:
            print("Task list is empty.")
        
    
    elif user_choice == "c":
        if not task_list:
            print("Task list is empty.")
        else:
            print("\nTask List:")
            for index, task in enumerate(task_list, 1):
                print(f"{index}. {task}")
        task_index = int(input("Enter the number of the task to complete: "))
        if 1 <= task_index <= len(task_list):
            completed_task = task_list.pop(task_index - 1)
            print(f"Task completed: {completed_task}")
        else:
            print("Invalid task number.")
        
        
    elif user_choice == "q":
        with open("tasks.txt", "w") as file:
            for task in task_list:
                file.write(f"{task}\n")
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
    
    
    



        
