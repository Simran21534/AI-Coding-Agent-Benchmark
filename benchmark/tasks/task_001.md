# Task 001 — Robust Transaction Summary

## Difficulty
Easy

## Task

Implement a Python function:

    summarize_transactions(transactions)

The function receives a list of dictionaries representing financial transactions.

Each transaction may contain:

- `amount`: numeric transaction amount
- `category`: transaction category

Return a dictionary containing:

- `total_amount`: sum of all valid transaction amounts
- `transaction_count`: number of valid transactions
- `category_totals`: total amount grouped by category

## Requirements

1. Ignore transactions where `amount` is missing.
2. Ignore transactions where `amount` is not numeric.
3. Treat a missing `category` as `"Unknown"`.
4. The function must not modify the original input list.
5. Return `0` for `total_amount` and `transaction_count` when there are no valid transactions.
6. `category_totals` must contain only categories belonging to valid transactions.

## Example

Input:

[
    {"amount": 100, "category": "Food"},
    {"amount": 50, "category": "Transport"},
    {"amount": 25, "category": "Food"}
]

Expected output:

{
    "total_amount": 175,
    "transaction_count": 3,
    "category_totals": {
        "Food": 125,
        "Transport": 50
    }
}