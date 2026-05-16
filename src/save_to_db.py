import pandas as pd
import sqlite3

df = pd.read_csv("data/expenses.csv")

conn = sqlite3.connect("database/expenses.db")
df.to_sql("expenses", conn, if_exists="replace", index=False)

print("Saved to database")
conn.close()