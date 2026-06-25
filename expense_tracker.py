def load_expenses():
    dummy=[]
    try:
        file=open("expenses.txt","r")
        for line in file:
            task,amt=line.strip().split(",")
            amount=(int)(amt)
            dummy.append([task,amount])
        file.close()
        return dummy
    except FileNotFoundError:
        print("File does not exist.")
        a=input("Would you like to create a file to store expenses(y/n): ")
        if a.lower() == "y":
            file=open("expenses.txt","w")
            file.close()
        return dummy
expenses=load_expenses()
def save_expenses(expenses):
    file = open("expenses.txt","w")
    for expense in expenses:
        file.write(f"{expense[0]},{expense[1]}\n")
    file.close()
    
def get_valid_amount():
    while True:
        try:
            amt=int(input("Enter the amount you spent: "))
            if amt>0:
                return amt
            else:
                print("Enter appropriate amount value.")
        except ValueError:
            print("Please enter a valid number")
def add_expense(expenses):
    category=input("Enter the category: ")
    amount=get_valid_amount()
    expenses.append([category,amount])
    save_expenses(expenses)
        

def view_expenses(expenses):
    if len(expenses)>0:
        for i,a in enumerate(expenses,start=1):
            print(f"{i}.{a[0]} {a[1]}")
    else:
        print("No expenses recorded yet.")

def show_category_spending(expenses):
    if len(expenses) > 0:
        total=0
        flag=0
        cat_name=input("Enter the category whose total spending you want to know: ")
        for expense in expenses:
            if cat_name.lower() == expense[0].lower():
                total+=expense[1]
                flag=1
        if flag == 1:
            print(f"The total amount you spend in {cat_name} is : {total}")
        else:
            print("The category doesn't exist in your expense tracker yet.")
    else:
        print("No expenses recorded yet.")
           
def show_total_spending(expenses):
    if len(expenses) > 0:
        total=0
        for expense in expenses:
            total+=expense[1]
        print(f"The total spending across all category is : {total}")  
    else:
        print("No expenses recorded yet.")
def highest_single_expense(expenses):
    if len(expenses) > 0:
        amt=expenses[0][1]
        cat=expenses[0][0]
        for expense in expenses:
            if expense[1] > amt:
                amt=expense[1]
                cat=expense[0]
        print(f"Highest single expense is :\n{cat} {amt}")
    else:
        print("No expenses recorded yet.")
def highest_spending_category(expenses):
    category_total={}
    if len(expenses) > 0:
        for expense in expenses:
            category=expense[0].lower()
            if category in category_total:
                category_total[category]+=expense[1]
            else:
                category_total[category]=expense[1]
        largest=category_total[expenses[0][0].lower()]
        name=expenses[0][0].lower()
        for cat,amt in category_total.items():
            if largest < amt:
                largest=amt
                name=cat
        print(f"The largest spending category is {name} : {largest}")
    else:
        print("No expenses recorded yet.")  
        
def delete_expense(expenses):
    if len(expenses)>0:
        while True:
            try:
                a=int(input("Which expense you want to delete(Tell us the expense number): "))
                if 1<=a<=len(expenses):
                    expenses.pop(a-1)
                    save_expenses(expenses)
                    print("Expense Deleted Successfully!")
                    break
                else:
                    print("Doesn't exist.")
            except ValueError:
                print("Enter a proper value.")
while True:
    print("\n1.Add Expense")
    print("2.View Expense")
    print("3.Show Category spending")
    print("4.Show Total spending")
    print("5. Highest Single Expense")
    print("6. Highest Spending Category")
    print("7.Delete Expense")
    print("8.Exit")
    
    choice=input("Enter your choice:")
    
    if choice == '1':
        add_expense(expenses)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        show_category_spending(expenses)
    elif choice == '4':
        show_total_spending(expenses)
    elif choice == '5':
        highest_single_expense(expenses)
    elif choice == '6':
        highest_spending_category(expenses)
    elif choice == '7':
        delete_expense(expenses)
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")