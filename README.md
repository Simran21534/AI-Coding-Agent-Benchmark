# AI Coding Agent Benchmark

## Project Overview

This project evaluates an AI coding agent's ability to generate and modify Python code correctly based on a defined programming task.

The benchmark uses automated tests to verify whether the generated solution handles normal inputs, edge cases, and invalid or missing data correctly.

## Task

The benchmark task implements a transaction summarization function.

The function:

- Calculates the total transaction amount
- Counts valid transactions
- Groups transaction amounts by category
- Handles missing categories using `Unknown`
- Handles empty input
- Ignores invalid transaction amounts

## Project Structure

```text
AI_Coding_Agent_Benchmark/
│
├── agents/
│   ├── candidate_001.py
│   ├── candidate_002.py
│   └── __init__.py
│
├── benchmark/
│   ├── reference_solutions/
│   └── tasks/
│
├── evaluator/
│   └── grader.py
│
├── tests/
│   └── test_task_001.py
│
├── results/
│   └── evaluation_results.csv
│
└── README.md