import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("database/expenses.db")

query = """
SELECT category, SUM(amount) as total
FROM expenses
GROUP BY category
"""

df = pd.read_sql(query, conn)

plt.bar(df["category"], df["total"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/category_chart.png")
plt.show()

conn.close()