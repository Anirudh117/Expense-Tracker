import datetime

def record_expense(expenses, date, amount, category, description):
    expenses.append({
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    })

def display_spending_pattern(expenses):
    print("\nSpending Pattern:")
    print("=================")
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']} - Rs.{expense['amount']:.2f}")

def main():
    expenses = []
    
    while True:
        print("\nExpense Tracking System")
        print("1. Record Expense")
        print("2. Display Spending Pattern")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = float(input("Enter the amount spent: "))
            category = input("Enter the category: ")
            description = input("Enter a description (optional): ")

            record_expense(expenses, date, amount, category, description)
            print("Expense recorded successfully!")

        elif choice == '2':
            display_spending_pattern(expenses)

        elif choice == '3':
            print("Exiting Expense Tracking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
