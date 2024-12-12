import matplotlib.pyplot as plt

# Creating a dictionary wih basic categories
categories = {
    0: "Add a new category",
    1: "Groceries",
    2: "Transportation",
    3: "Utilities",
    4: "Entertainment",
    5: "Medical",
    6: "Housing",
    7: "Clothing"}

# Empty dictionary to get the expenses
expenses = {}

# funtion to get user input and categorise the expenses
def expense_track():
    global categories, expenses
    expense = float(input("Enter your expense (in Rs.): "))
    des = input("Give a small description about the expense:\n")
    print("\nCategories:")
    for key, value in categories.items():                          #This will print the keys-serial numbers and values-categories
        print(f"{key}: {value}")

    # Thsi will get the category they want the expenses to be categorized as. With the help of the keys
    cat = int(input("\nEnter the number of the category: ")) 
    
    # Adding a new category - If 0 is entered
    if cat == 0:
        user_cat = input("\nEnter the name of the new category: ")
        new_key = max(categories.keys()) + 1                       # This will allot the succeding serial number to the new category
        categories[new_key] = user_cat                             # Add the new category to the 'categories' dictionary with the new key
        cat = new_key
        print(f"New category '{user_cat}' successfully added!")

    user_cat = categories.get(cat)                                 # Retrieve the category name from the 'categories' dictionary using the key 'cat'
    if user_cat:
        if user_cat not in expenses:                               # If the category doesn't exist in the 'expenses' dictionary, keep it as an empty list
            expenses[user_cat] = []
        # Append a new expense entry with the amount and description to the appropriate category
        expenses[user_cat].append({"Amount": expense, "Description": des})
        print(f"Expense added to '{user_cat}'")
    else:
        print("Invalid category.")


# funtion to display user the summary and graph of the expenses
def display_results():
    if not expenses:                                               # Check if there are any recorded expenses
        print("No expenses recorded!")
    else:
        # Print table headers for displaying expense details and align it properly
        print(f"{'Category':<20}{'Amount (Rs.)':<20}{'Description':<30}")
        print("-" * 55)
        for category, records in expenses.items():                  # Print each expense with its category, amount, and description uisng loops
            for record in records:
                print(f"{category:<20}{record['Amount']:<20}{record['Description']:<30}")

    # Display total amount spent and category breakdown
    total_spent = 0
    category_summary = {category: 0 for category in categories.values() if category != "Add a new category"}
    # sum up amounts for each category
    for category, records in expenses.items():
        for record in records:
            total_spent += record['Amount']                          # Increment total spent by the expense amount
            category_summary[category] += record['Amount']           # Add the expense amount to the respective category in the summary

    print(f"\n{'Total Amount Spent:':<25} Rs. {total_spent:.2f}")
    # Print a breakdown of expenses by category
    print("\n\tCategory Breakdown:")
    print(f"{'Category':<20}{'Amount (Rs.)':<20}")
    print("-" * 35)
    for category, amount in category_summary.items():               # Display each category and the corresponding total expense amount
        print(f"{category:<20}{amount:<20.2f}")
    print("")
    # Plotting the graph
    classification = list(category_summary.keys())
    amounts = list(category_summary.values())
    
    plt.figure(figsize=(5, 6))                                     # Set the figure size
    plt.bar(classification, amounts, color='#488bc4')              # Create a bar chart with a specific color
    plt.title("Expenses")                                          # Add a title to the chart
    plt.xlabel("Category")                                         # Label the x-axis
    plt.ylabel("Amount (Rs.)")                                     # Label the y-axis
    plt.xticks(rotation=45)                                        # Rotate x-axis labels for better visibility
    plt.tight_layout()                                             # Adjust layout to prevent label overlap
    plt.show()                                                     # Display the chart
    

def main():
    while True:                                                    # starting the funtion if the condition or the main() is called - infinite loop
        expense_track()
        # Ask the user if they want to add another entry
        user = input("\nDo you want to add another entry (yes/no): ").lower()
        if user != "yes":
            print("\n\tSummary of the expenses:")
            display_results()                                     # if they dont want to enter another entry, end the loop with the summary displayed
            break                                                 # Come out of the loop

# Call the main funtion to start the problem
main()
