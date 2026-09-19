import os

from dotenv import load_dotenv
from crewai import Agent, LLM

from tools import execute_sql

# Workaround for CrewAI/Groq cache breakpoint issue
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

load_dotenv()


llm = LLM(
    model="openai/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    temperature=0
)


data_analyst = Agent(
    role="Sales Data Analyst",
    goal=(
        "Answer sales-data questions accurately using SQL. "
        "For each question, formulate the SQL query needed to obtain the answer "
        "and execute it using the execute_sql tool. "
        "After receiving the first SQL result that directly answers the question, "
        "immediately provide the final answer. Never perform a second query to "
        "verify, reinterpret, or repeat an already answered question."
    ),
    backstory=(
        "You are an expert sales data analyst working with a SQLite database "
        "containing a sales table with these columns: "
        "Order ID, Product, Quantity Ordered, Price Each, Order Date, "
        "Purchase Address, Month, Sales, City, and Hour. "
        "Use the execute_sql tool directly to answer questions. "
        "The SQL result is authoritative. "
        "If a query returns 0, NULL, an empty result, or no matching rows, "
        "treat that result as the answer and do not run another query. "
        "Do not inspect the database schema using PRAGMA or sqlite_master. "
        "Do not run exploratory queries, DISTINCT queries, verification queries, "
        "or repeated queries unless the original query itself failed with an SQL error. "
        "Normally, answer each question with exactly one SQL query. "
        "Once the SQL query returns a valid result, stop using tools and provide "
        "the final answer."
    ),
    llm=llm,
    tools=[execute_sql],
    verbose=True,
    max_iter=3,
)


if __name__ == "__main__":

    print("\nSales Data Analysis Agent")
    print("Ask questions about the sales dataset.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            continue

        response = data_analyst.kickoff(question)

        print(f"\nAgent: {response}\n")