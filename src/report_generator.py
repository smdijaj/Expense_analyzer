import sqlite3
import pandas as pd

conn = sqlite3.connect("database/expenses.db")
df = pd.read_sql("SELECT * FROM expenses", conn)

total = df["amount"].sum()
average = df["amount"].mean()
highest = df.loc[df["amount"].idxmax()]

with open("reports/summary.txt", "w") as f:
    f.write(f"Total Spending: {total}\n")
    f.write(f"Average Spending: {average:.2f}\n")
    f.write(f"Highest Expense: {highest['category']} - {highest['amount']}\n")

print("Report created")

conn.close()