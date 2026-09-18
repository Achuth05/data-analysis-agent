import json
import sys
from pathlib import Path

# Allow imports from src/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from agent import data_analyst


TEST_CASES_PATH = PROJECT_ROOT / "tests" / "test_cases.json"


def load_test_cases():
    with open(TEST_CASES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def run_test(test_case):
    print("\n" + "=" * 70)
    print(f"Test Case: {test_case['id']}")
    print(f"Category: {test_case['category']}")
    print(f"Question: {test_case['question']}")
    print("=" * 70)

    result = data_analyst.kickoff(test_case["question"])

    print("\nAgent Answer:")
    print(result)

    return result


if __name__ == "__main__":
    test_cases = load_test_cases()

    print(f"Loaded {len(test_cases)} test cases.")

    for test_case in test_cases:
        run_test(test_case)