import sqlite3
import pandas as pd

CSV_PATH = "data/sales_data.csv"
DB_PATH = "data/sales.db"

df = pd.read_csv(CSV_PATH)

# Remove the CSV index column
df = df.drop(columns=["Unnamed: 0"])

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Store the dataset in SQLite
connection = sqlite3.connect(DB_PATH)

df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print(f"Database created successfully: {DB_PATH}")
print(f"Rows inserted: {len(df)}")