from flask import Flask
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("database/expenses.db")
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    total = df["amount"].sum()
    average = df["amount"].mean()

    html = f"""
    <h1>Expense Analyzer Dashboard</h1>
    <h3>Total Spending: {total}</h3>
    <h3>Average Spending: {average:.2f}</h3>
    {df.to_html(index=False)}
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)