tasks=[]
def load_tasks():
    tp=[]
    try:
        file=open("tasks.txt","r")
        for line in file:
            task=line.strip()
            tp.append(task)
        file.close()
        return tp
    except FileNotFoundError:
        print("There doesn't exist file")
        a=input("Do you want to create a file: y/n?")
        if a == 'y':
            file=open("tasks.txt","w")
            file.close()
            print("File created")
        return tp
        
            

tasks=load_tasks()

def add_tasks(tasks):
    task=input("Enter your task: ")
    tasks.append(task)
    save_tasks(tasks)
    
def view_tasks(tasks):
    if len(tasks)!=0:
        i=1
        for task in tasks:
            print(f"{i}.{task}\n")
            i+=1
    else:
        print("Currently you dont have any tasks.")
        
def delete_tasks(tasks):
    if len(tasks) != 0:
        no=input("1.Do you want to delete all tasks?\n2.Do you want to delete some specific task? 1 or 2?")
        if no == '1':
            tasks.clear()
            save_tasks(tasks)
            
        elif no == '2':
            name=input("Enter the task you want to delete:")
            if name in tasks:
                tasks.remove(name)
                save_tasks(tasks)
            else:
                print("That task doesn't exist in your to-do-list")
    else:
        print("There is no tasks saved in your to-do-list")
        
def save_tasks(tasks):
    file=open("tasks.txt","w")
    for task in tasks:
        file.write(f"{task}\n")
    file.close()

while True:
    print("\n1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit from the program")
    
    choice=input("Enter your choice: ")
    
    if choice == '1':
        add_tasks(tasks)
    
    elif choice == '2':
        view_tasks(tasks)
        
    elif choice == '3':
        delete_tasks(tasks)
        
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")