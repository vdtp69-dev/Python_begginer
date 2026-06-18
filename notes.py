# Notes app

while True:
    print("\n1.Create/Add notes")
    print("2.View notes")
    print("3.Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        note = input("Enter your note: ")
        file = open("note.txt","a")
        file.write(f"{note}\n")
        file.close()
    elif choice == "2":
        file = open("note.txt","r")
        content = file.read()
        print(content)
        file.close()
    elif choice == "3":
        print("Goodbye!")
        break
    else: 
        print("Invalid choice!")