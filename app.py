from flask import Flask
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("database/expenses.db")
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    return df.to_html()

if __name__ == "__main__":
    app.run(debug=True)