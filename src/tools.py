import sqlite3

from crewai.tools import tool


DB_PATH = "data/sales.db"


@tool("execute_sql")
def execute_sql(query: str) -> str:
    """
    Execute a read-only SQL SELECT query on the sales database.

    Database schema:
    sales(
        "Order ID" INTEGER,
        "Product" TEXT,
        "Quantity Ordered" INTEGER,
        "Price Each" REAL,
        "Order Date" TIMESTAMP,
        "Purchase Address" TEXT,
        "Month" INTEGER,
        "Sales" REAL,
        "City" TEXT,
        "Hour" INTEGER
    )

    Use this tool directly to answer sales questions.
    Do not use PRAGMA or sqlite_master queries.
    Only SELECT queries are allowed.
    """

    query = query.strip()

    if not query.lower().startswith("select"):
        return "Error: Only SELECT queries are allowed."

    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            return "Query returned no matching rows. Treat this as a valid empty result."

        # Handle aggregate queries such as SUM() when no matching rows exist.
        if all(value is None for value in rows[0]):
            return "Query returned no matching rows. Aggregate result is 0."

        columns = [description[0] for description in cursor.description]

        result = [", ".join(columns)]

        for row in rows:
            result.append(", ".join(str(value) for value in row))

        return "\n".join(result)

    except Exception as e:
        return f"SQL execution error: {str(e)}"

    finally:
        connection.close()