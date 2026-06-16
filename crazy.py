contacts={}
count=0
while True:
    print("\n1.Add contact: ")
    print("2.Search contact: ")
    print("3.View contact: ")
    print("4.Exit")
    print("5.Delete contact")
    print("6.Count number of contacts you have")
    print("7.Update contact")

    choice=input("Enter your choice: ")

    if choice == "1" :
       name= input("Enter your name:")
       contacts[name]=input("Enter your number: ")
       print("Contact added!")
       
    elif choice == "2":
        search=input("\nEnter the contact name you want to search: ")
        if search in contacts:
            print(f"{search}'s phone number is {contacts[search]}")
        else:
            print("Contact not found!")
            
    elif choice == "3":
       for name, number in contacts.items():
            print(f"{name}: {number}")
            
    elif choice == "4":
        print("Goodbye!")
        break
    
    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")
            
    elif choice == "6":
        print(f"There are {len(contacts)} contacts present in your Mini Contact Book")
    
    elif choice == "7":
        name=input("Enter the contact name you want to update: ")
        contacts[name]=input("Enter the new contact number: ")
    
    else:
        print("Invalid Choice")
        
        