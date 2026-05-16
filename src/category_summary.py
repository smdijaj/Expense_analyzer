import sqlite3
import pandas as pd

conn = sqlite3.connect("database/expenses.db")

query = """
SELECT category, SUM(amount) as total
FROM expenses
GROUP BY category
ORDER BY total DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()