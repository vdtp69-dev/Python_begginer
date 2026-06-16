# # name=input("Enter your name:")
# # print(f"Welcome,{name}")
# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# print(f"Sum of the number is :{a+b}")
# print(f"Product of the number is :{a*b}")
# print(f"Subtraction of the number is :{a-b}")

# # for i in range(1,11):
# #     print(f"{a} X {i} = {a*i}")

# def greet(name):
#     print(f"Hello God {name}")
    
# greet("Vihaan")

# fruits=["apple","banana","guava"]

# for fruit in fruits:
#     print(fruit)

# a=[]
# for i in range(1,6):
#     b=int(input(f"Enter number {i}: "))
#     a.append(b)
# maxi=a[0]
# for i in a:
#     if(maxi<i):
#         maxi=i
# print(f"Maximum number in the list is: {maxi}")
# ev=0
# od=0
# for i in a:
#     if i%2==0:
#         ev+=1
#     else:
#         od+=1
        
# print(f"Even numbers: {ev}")
# print(f"Odd numbers: {od}")

# def largest(numbers):
#     maxi=numbers[0]
#     for i in numbers:
#         if maxi < i:
#             maxi=i
#     return maxi
# nums=[34,31,86,54,86]
# print(largest(nums))

# students={}
# for i in range(1,4):
#     name=input("Enter you name: ")
#     age=int(input("Enter your age: "))
#     students[name]=age
#     print("\n")

# for name,age in students.items():
#     print(f"{name}'s age is {age}")
# # print(students)

# search=input("Enter the name you want to search")

# print(f"{search}'s age is {students[search]}")


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
        
        