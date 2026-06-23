expenses=[]
def add_expense(expenses):
    category=input("Enter the category: ")
    amount=int(input("Enter the amount you spent: "))
    expenses.append([category,amount])

def view_expenses(expenses):
    if len(expenses)>0:
        for i in expenses:
            print(f"{i[0]} {i[1]}")
    else:
        print("No expenses recorded yet.")

def show_category_spending(expenses):
    if len(expenses) > 0:
        total=0
        flag=0
        cat_name=input("Enter the category whose total spending you want to know: ")
        for expense in expenses:
            if cat_name == expense[0]:
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
    total={}
    if len(expenses) > 0:
        for expense in expenses:
            if expense[0] in total:
                total[expense[0]]+=expense[1]
            else:
                total[expense[0]]=expense[1]
        largest=total[expenses[0][0]]
        name=expenses[0][0]
        for cat,amt in total.items():
            if largest < amt:
                largest=amt
                name=cat
        print(f"The largest spending category is {name} : {largest}")
    else:
        print("No expenses recorded yet.")  
while True:
    print("\n1.Add Expense")
    print("2.View Expense")
    print("3.Show Category spending")
    print("4.Show Total spending")
    print("5. Highest Single Expense")
    print("6. Highest Spending Category")
    print("7.Exit")
    
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")