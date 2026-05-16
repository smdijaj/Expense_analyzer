from flask import Flask, request
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    category = request.args.get("category")

    conn = sqlite3.connect("database/expenses.db")

    if category:
        query = "SELECT * FROM expenses WHERE LOWER(category)=LOWER(?)"
        df = pd.read_sql(query, conn, params=(category.strip(),))
    else:
        df = pd.read_sql("SELECT * FROM expenses", conn)

    conn.close()

    if not df.empty:
        summary = df.groupby("category")["amount"].sum()
        plt.figure()
        summary.plot(kind="bar")
        plt.tight_layout()
        plt.savefig("static/category_chart.png")
        plt.close()

    total = df["amount"].sum() if not df.empty else 0

    html = f"""
<h1>Expense Analyzer Dashboard</h1>

<form>
    <input name="category" placeholder="Food / Travel / Bills">
    <button type="submit">Filter</button>
</form>

<h3>Total: {total}</h3>

<div style="display:flex; gap:30px; align-items:flex-start;">

    <div>
        <h2>Chart</h2>
        <img src="/static/category_chart.png" width="500">
    </div>

    <div>
        <h2>Data</h2>
        {df.to_html(index=False)}
    </div>

</div>
"""

    return html

if __name__ == "__main__":
    app.run(debug=True)