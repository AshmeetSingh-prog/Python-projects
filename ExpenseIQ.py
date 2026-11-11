import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. SETUP: Create our expense database

columns = ['Date', 'Category', 'Amount', 'Description']

expenses = pd.DataFrame(columns=columns)

FILE_NAME = "expenses.csv"


# 2. LOAD EXISTING EXPENSES

def load_expenses():
    global expenses

    try:
        expenses = pd.read_csv(FILE_NAME)
        print("Previous expenses loaded successfully!")

    except FileNotFoundError:
        print("No previous expense records found.")
        expenses = pd.DataFrame(columns=columns)


# 3. ADD A NEW EXPENSE

def add_expense(date, category, amount, description):

    global expenses

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    new_item = {
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }

    new_df = pd.DataFrame([new_item])

    expenses = pd.concat(
        [expenses, new_df],
        ignore_index=True
    )

    # Save data permanently
    expenses.to_csv(FILE_NAME, index=False)

    print(f"Successfully added Rs.{amount:.2f} for {category}!")


# 4. SHOW EXPENSE SUMMARY

def show_summary():

    if expenses.empty:
        print("\nNo expenses recorded yet!")
        return

    print("\n========== ALL EXPENSES ==========")

    print(expenses.to_string(index=False))

    # NumPy calculations
    amounts = expenses['Amount'].to_numpy()

    total = np.sum(amounts)
    average = np.mean(amounts)
    highest = np.max(amounts)
    lowest = np.min(amounts)

    print("\n========== EXPENSE SUMMARY ==========")

    print(f"Total Spending: Rs.{total:.2f}")
    print(f"Average Expense: Rs.{average:.2f}")
    print(f"Highest Expense: Rs.{highest:.2f}")
    print(f"Lowest Expense: Rs.{lowest:.2f}")

    # Calculate category-wise spending
    category_totals = expenses.groupby('Category')['Amount'].sum()

    print("\n========== CATEGORY-WISE SPENDING ==========")

    print(category_totals)


# 5. VISUALIZE EXPENSES
def plot_expenses():

    if expenses.empty:
        print("No expenses available to visualize!")
        return

    category_totals = expenses.groupby('Category')['Amount'].sum()

    # Create two charts
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Bar chart
    category_totals.plot(
        kind='bar',
        color='coral',
        ax=axes[0]
    )

    axes[0].set_title("Expenses by Category")
    axes[0].set_xlabel("Category")
    axes[0].set_ylabel("Amount (Rs.)")
    axes[0].tick_params(axis='x', rotation=45)

    # Pie chart
    category_totals.plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=axes[1]
    )

    axes[1].set_title("Expense Distribution")
    axes[1].set_ylabel("")

    plt.tight_layout()
    plt.show()


# 6. INTERACTIVE MENU

def main():

    load_expenses()

    while True:

        print("\n========== EXPENSEIQ ==========")

        print("1. Add New Expense")
        print("2. View Expense Summary")
        print("3. View Expense Charts")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")

            try:
                amount = float(input("Enter amount (Rs.): "))

                description = input("Enter description: ")

                add_expense(date, category, amount, description)

            except ValueError:
                print("Please enter a valid numerical amount!")

        elif choice == '2':

            show_summary()

        elif choice == '3':

            plot_expenses()

        elif choice == '4':

            print("Thank you for using ExpenseIQ!")
            break

        else:

            print("Invalid choice! Please try again.")


# 7. RUN THE APPLICATION

if __name__ == "__main__":
    main()
