import sqlite3
import pandas as pd

category_name = input("Enter category: ")

conn = sqlite3.connect("database/expenses.db")

query = "SELECT * FROM expenses WHERE category = ?"
df = pd.read_sql(query, conn, params=(category_name,))

print(df)

conn.close()