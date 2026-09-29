import csv
from pathlib import Path

import subprocess
import sys
import re


def run_tests():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "tests"],
        capture_output=True,
        text=True,
    )

    output = result.stdout

    passed = 0
    failed = 0

    match = re.search(r"(\d+) passed", output)
    if match:
        passed = int(match.group(1))

    match = re.search(r"(\d+) failed", output)
    if match:
        failed = int(match.group(1))

    total = passed + failed

    score = (passed / total * 100) if total > 0 else 0

    return {
        "passed": passed,
        "failed": failed,
        "total": total,
        "score": score,
        "output": output,
    }
def save_result(result):
    output_file = Path("results/evaluation_results.csv")

    output_file.parent.mkdir(exist_ok=True)

    file_exists = output_file.exists()

    with open(output_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "candidate",
                "task",
                "passed",
                "failed",
                "total",
                "score",
            ],
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {
                "candidate": "candidate_001",
                "task": "task_001",
                "passed": result["passed"],
                "failed": result["failed"],
                "total": result["total"],
                "score": round(result["score"], 1),
            }
        )

if __name__ == "__main__":
    result = run_tests()
    save_result(result)

    print("=" * 45)
    print("AI CODING AGENT BENCHMARK")
    print("=" * 45)

    print(f"Tests:  {result['total']}")
    print(f"Passed: {result['passed']}")
    print(f"Failed: {result['failed']}")
    print(f"Score:  {result['score']:.1f}%")

    print("\nTest Output:")
    print(result["output"])

    if result["failed"] == 0:
        print("STATUS: PASS")
    else:
        print("STATUS: PARTIAL / FAILED")