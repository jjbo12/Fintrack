import numpy as np
import random  # For "AI" tips
import pandas as pd
import os



def login():
    username = input("Username: ")
    password = input("Password: ")

    a = "admin"
    b = "1234"

    if username == a  and password == b:
        print("Login successful!")
        return main()
    else:
        print("❌Invalid credentials!")
        return None
    
def main():
    try:
        current_user = None
        while True:
            print("\nFINTRACK PRO")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Spending Report")
            print("4. Get Savings Tip")
            print("5. Exit")

            choice = input("Enter choice (1-5): ").strip()

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                spending_report()
            elif choice == "4":
                get_savings_tip()
            elif choice == "5":
                print("\n Goodbye!")
                break
            else:
                print("Invalid choice!")
    except Exeption as e:
        print(e)
    finally:
        print("\n thankyou for using Fintrack Pro")


def add_expense():
    """Add expense to the list of dictionaries"""
    try:
        category = input("Category (e.g., Food, Travel): ").strip()
        amount = float(input("Amount (PKR): "))
        date = input("Date (YYYY-MM-DD): ").strip()

        expenses.append({
            "category": category,
            "amount": amount,
            "date": date
        })
        print("Expense added!")
    except ValueError as e:
        print("Error ⚠️  try again")
    save()



def view_expenses():
    """Reads and prints all expenses directly from CSV"""
    filename = "expenses.csv"

    if not os.path.exists(filename):
        print("No expenses found! Add some first.")
        return

    try:
        df = pd.read_csv(filename)
        if df.empty:
            print("No expenses recorded yet!")
        else:
            print("\n=== ALL EXPENSES ===")
            print(df.to_string(index=False))  #  table format

    except Exception as e:
        print(e)


def save():
    """Appends new expenses to CSV, creates file if missing"""
    filename = "expenses.csv"

    # Convert current expenses to DataFrame
    new_data = pd.DataFrame(expenses)

    if os.path.exists(filename):
        # Append without headers
        new_data.to_csv(filename, mode='a', header=False, index=False)
    else:
        # Create new file with headers
        new_data.to_csv(filename, index=False)

    print( "Data Saved !")


def spending_report():
    # Read expenses from CSV instead of list
    if not os.path.exists("expenses.csv"):
        return print("No expenses!")

    df = pd.read_csv("expenses.csv")
    if df.empty:
        return print("No expenses!")

    # Convert DataFrame to list of dictionaries (to keep your existing logic working)
    expenses = df.to_dict('records')

    # Convert amounts to NumPy array for calculations
    amounts = np.array([expense['amount'] for expense in expenses])
    categories = [expense['category'] for expense in expenses]

    # Basic calculations
    total = np.sum(amounts)
    average = np.mean(amounts)
    max_expense = np.max(amounts)
    min_expense = np.min(amounts)

    # Category-wise spending
    unique_categories = set(categories)
    category_totals = {}

    for category in unique_categories:
        # Get all amounts for this category using list comprehension
        cat_amounts = [e['amount'] for e in expenses if e['category'] == category]
        category_totals[category] = np.sum(cat_amounts)

    # Find top spending category
    top_category = max(category_totals.items(), key=lambda x: x[1]) if category_totals else ("None", 0)

    # Print report
    print("\n=== SPENDING REPORT ===")
    print(f"Total spending: PKR {total:.2f}")
    print(f"Average expense: PKR {average:.2f}")
    print(f"Most expensive single purchase: PKR {max_expense:.2f}")
    print(f"Least expensive purchase: PKR {min_expense:.2f}")

    print("\nSpending by category:")
    for category, total in category_totals.items():
        print(f"- {category}: PKR {total:.2f}")

    print(f"\nTop spending category: {top_category[0]} (PKR {top_category[1]:.2f})")


def get_savings_tip():
    # Read expenses from CSV instead of list
    if not os.path.exists("expenses.csv"):
        return print("No expenses to analyze! Start tracking to get tips.")

    df = pd.read_csv("expenses.csv")
    if df.empty:
        return print("No expenses to analyze! Start tracking to get tips.")

    # Convert DataFrame to list of dictionaries (to keep your existing logic working)
    expenses = df.to_dict('records')

    # Analyze spending patterns
    category_spending = {}
    for expense in expenses:
        cat = expense['category']
        category_spending[cat] = category_spending.get(cat, 0) + expense['amount']

    # Find problem areas
    top_category = max(category_spending.items(), key=lambda x: x[1]) if category_spending else ("None", 0)
    total_spent = sum(category_spending.values())

    # Creative "AI" responses
    tips = {
        'Food': [
            "🍔 Burger lover? Try meal prepping Sundays to save 30%!",
            "Your food spending is sizzling! Try local markets for fresher, cheaper ingredients.",
            "Pro tip: Eating out 1 less time per week could save you PKR {} monthly!".format(
                int(top_category[1] * 0.25))
        ],
        'Travel': [
            "🚗 Car burning your wallet? Try carpooling with colleagues!",
            "Fuel prices got you down? Walking short distances improves health AND savings!",
            "Alert: You could save PKR {} monthly using public transport 2 days/week!".format(
                int(top_category[1] * 0.4))
        ],
        'Entertainment': [
            "🎬 Streaming subscriptions piling up? Try rotating services monthly.",
            "Gaming budget high? Look for free indie games between big purchases!",
            "Did you know? Library cards give free access to movies, games and books!"
        ]
    }

    # Special conditions
    if total_spent > 10000:
        emergency_tip = "\n💥 EMERGENCY ALERT! You've spent PKR {} this month. Consider a spending freeze!".format(
            total_spent)
    else:
        emergency_tip = ""

    # Generate random personalized tip
    print("\n=== 🤖 AI SAVINGS WIZARD ===")
    print(random.choice([
        "💡 Your personalized savings insight:",
        "🔍 My analysis reveals:",
        "✨ Here's a money magic trick for you:"
    ]))

    if top_category[0] in tips:
        print(random.choice(tips[top_category[0]]))
    else:
        print(f"Your biggest spending is on {top_category[0]}. Track this category carefully!")

    print(emergency_tip)

    # Fun final touch
    print("\n" + random.choice([
        "Remember: Small savings grow into big fortunes!",
        "Financial freedom starts with one good decision!",
        "You're smarter than your spending habits!"
    ]))




login()


