import pandas as pd
import matplotlib.pyplot as plt
from predict import predict_expense

expenses = []

while True:
    user_input = input("Enter expense (or type 'done'): ")

    if user_input.lower() == "done":
        break

    try:
        amount = int([word for word in user_input.split() if word.isdigit()][-1])
    except:
        print("Please include amount (e.g., 'pizza 250')")
        continue

    category = predict_expense(user_input)

    expenses.append({
        "text": user_input,
        "category": category,
        "amount": amount
    })

    print("\n--- Result ---")
    print(f"Category: {category}")
    print(f"Amount: ₹{amount}\n")

df = pd.DataFrame(expenses)

if len(df) == 0:
    print("No data entered.")
    exit()

total = df["amount"].sum()

category_sum = df.groupby("category")["amount"].sum()

top_category = category_sum.idxmax()

print("\n===== SUMMARY =====")
print(f"Total Spending: ₹{total}")
print(f"Top Category: {top_category}\n")

print("Breakdown:")
print(category_sum)

plt.figure()
category_sum.plot(kind='pie', autopct='%1.1f%%')
plt.title("Spending Distribution")
plt.ylabel("")
plt.show()

print("\n===== SUGGESTION =====")

if top_category == "Shopping":
    print("You spend the most on Shopping. Try reducing unnecessary purchases.")
elif top_category == "Food":
    print("Food expenses are high. Consider budgeting meals.")
elif top_category == "Travel":
    print("Travel costs are high. Try optimizing your routes.")
else:
    print("Keep tracking your expenses for better insights!")