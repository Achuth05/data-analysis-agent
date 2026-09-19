# Sales Data Analysis Agent

A natural-language sales data analysis agent built with **CrewAI**, **Groq**, and **SQLite**. The agent understands sales-related questions, generates the required SQL query, executes it against the sales database, and returns the result in a human-readable format.

## Features

* Ask questions about sales data using natural language
* Automatically generate SQL queries
* Execute read-only SQL queries against a SQLite database
* Analyse sales by:

  * Product
  * City
  * Month
  * Hour
  * Order
* Calculate totals, averages, counts, quantities, rankings, and comparisons
* Handle multiple filtering conditions
* Handle queries with no matching records
* Uses a real-world sales dataset containing 185,950 records

## Tech Stack

* **Python 3.13**
* **CrewAI** – Agent framework
* **Groq** – LLM provider
* **GPT-OSS 120B** – Language model
* **SQLite** – Database
* **Pandas** – Data processing
* **python-dotenv** – Environment variable management

## Dataset

The project uses the [Sales Data Analysis dataset](https://www.kaggle.com/datasets/beekiran/sales-data-analysis) from Kaggle.

The dataset contains information including:

* Order ID
* Product
* Quantity Ordered
* Price Each
* Order Date
* Purchase Address
* Month
* Sales
* City
* Hour

The original CSV file is stored in:

```text
data/sales_data.csv
```

The dataset is converted into a SQLite database for querying:

```text
data/sales.db
```

## Project Structure

```text
data-analysis-agent/
├── data/
│   ├── sales_data.csv
│   └── sales.db
├── src/
│   ├── agent.py
│   ├── tools.py
│   ├── config.py
│   └── create_database.py
├── tests/
│   ├── test_cases.json
│   └── run_tests.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd data-analysis-agent
```

### 2. Create a virtual environment

Python 3.13 is recommended.

```bash
py -3.13 -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

## Database Setup

The SQLite database can be generated from the CSV dataset using:

```bash
python src/create_database.py
```

This creates:

```text
data/sales.db
```

with the sales data stored in the `sales` table.

## Usage

Run the agent with:

```bash
python src/agent.py
```

The agent starts an interactive terminal session where you can ask questions about the sales dataset.

Example:

```text
Sales Data Analysis Agent
Ask questions about the sales dataset.
Type 'exit' to quit.

You: What was the total sales revenue in January?

Agent: The total sales revenue in January was $1,822,256.73.

You: Which city had the highest total sales revenue?

Agent: San Francisco had the highest total sales revenue.

You: How many Macbook Pro Laptops were sold?

Agent: 4,728 Macbook Pro Laptops were sold.

You: exit
Goodbye!
```

The agent generates the required SQL query, executes it against the SQLite database, and returns the result in a human-readable format.

Type `exit` to end the session.

## SQL Tool

The agent uses a read-only `execute_sql` tool to interact with the database.

Only `SELECT` queries are allowed. Database modification operations are not permitted.

The database schema is:

```text
sales(
    "Order ID",
    "Product",
    "Quantity Ordered",
    "Price Each",
    "Order Date",
    "Purchase Address",
    "Month",
    "Sales",
    "City",
    "Hour"
)
```

## Running Tests

The project includes a set of sample queries in:

```text
tests/test_cases.json
```

Run them using:

```bash
python tests/run_tests.py
```

