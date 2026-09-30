# AI Coding Agent Benchmark

A Python-based benchmark for evaluating AI coding agents using automated tests and objective scoring.

## Project Overview

This project evaluates coding-agent solutions against a predefined task specification. It runs automated tests, identifies passed and failed cases, and calculates an overall performance score.

## Project Structure

```text
AI-Coding-Agent-Benchmark/
│
├── agents/
│   ├── candidate_001.py
│   └── candidate_002.py
│
├── benchmark/
│   └── task_001.md
│
├── evaluator/
│   └── grader.py
│
├── results/
│   └── evaluation_results.csv
│
├── tests/
│   └── test_task_001.py
│
├── README.md
└── task_001_solution.py
