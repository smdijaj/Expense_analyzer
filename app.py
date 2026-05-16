from flask import Flask, request
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    category = request.args.get("category")

    conn = sqlite3.connect("database/expenses.db")

    if category:
        df = pd.read_sql(
            "SELECT * FROM expenses WHERE category = ?",
            conn,
            params=(category,)
        )
    else:
        df = pd.read_sql("SELECT * FROM expenses", conn)

    conn.close()

    total = df["amount"].sum()

    html = f"""
    <h1>Expense Analyzer Dashboard</h1>

    <form>
        <input name="category" placeholder="Food / Travel / Bills">
        <button type="submit">Filter</button>
    </form>

    <h3>Total: {total}</h3>

    <img src="/static/category_chart.png" width="600">

    {df.to_html(index=False)}
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)