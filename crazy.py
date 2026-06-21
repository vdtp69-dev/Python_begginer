def load_contacts():
    numb={}
    try:
        file =open("contacts.txt","r")
        for line in file:
            name,number=line.strip().split(",")
            numb[name]=number
        file.close()
        return numb
        
        
    except FileNotFoundError:
        print("File doesnt exist!")
        return numb
    
def save_contacts(contacts):
    file = open("contacts.txt","w")
    for name,number in contacts.items():
        file.write(f"{name},{number}\n")
    file.close()
        
contacts=load_contacts()   
    
def add_contacts(contacts):
       name= input("Enter your name:")
       number=input("Enter your number: ")
       contacts[name]=number
       save_contacts(contacts)
       print("Contact added!")
       
       
def view_contacts(contacts):
    if len(contacts)>0:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("Currently you dont have any contacts in your mini contact book")
        
        
def search_contacts(contacts):
    search=input("\nEnter the contact name you want to search: ")
    if search in contacts:
        print(f"{search}'s phone number is {contacts[search]}")
    else:
        print("Contact not found!")
        
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")
    
    save_contacts(contacts)
            
def update_contact(contacts):    
    name=input("Enter the contact name you want to update: ")
    if name in contacts:
        contacts[name]=input("Enter the new contact number: ")
        save_contacts(contacts)
    else:
        a=input(("Do you want to create a new contact ? y or n?"))
        if(a=='y'):
            add_contacts(contacts)
        else:
            print("Okay")
    
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
       add_contacts(contacts)
       
    elif choice == "2":
        search_contacts(contacts)
            
    elif choice == "3":
       view_contacts(contacts)
            
    elif choice == "4":
        print("Goodbye!")
        break
    
    elif choice == "5":
        delete_contact(contacts)
            
    elif choice == "6":
        print(f"There are {len(contacts)} contacts present in your Mini Contact Book")
    
    elif choice == "7":
        update_contact(contacts)
        
    else:
        print("Invalid Choice")