import pandas as pd
df=pd.read_csv(r"C:\Users\mijaj\expense-analyzer\data\Expenses.csv")
print(df)
print("rows:",len(df))
print("columns:",list(df.columns))