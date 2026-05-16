import sqlite3
import pandas as pd

conn = sqlite3.connect("database/expenses.db")

query = "SELECT * FROM expenses"
df = pd.read_sql(query, conn)

print(df)
print("\nTotal amount:", df["amount"].sum())

conn.close()