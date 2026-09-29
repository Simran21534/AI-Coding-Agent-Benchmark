import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0,str(PROJECT_ROOT))

from agents.candidate_002 import summarize_transactions


def test_basic_transactions():
    transactions = [
        {"amount": 100, "category": "Food"},
        {"amount": 50, "category": "Transport"},
        {"amount": 25, "category": "Food"},
    ]

    result = summarize_transactions(transactions)

    assert result["total_amount"] == 175
    assert result["transaction_count"] == 3
    assert result["category_totals"] == {
        "Food": 125,
        "Transport": 50,
    }


def test_invalid_amounts_are_ignored():
    transactions = [
        {"amount": 100, "category": "Food"},
        {"amount": "invalid", "category": "Food"},
        {"category": "Transport"},
        {"amount": None, "category": "Other"},
    ]

    result = summarize_transactions(transactions)

    assert result["total_amount"] == 100
    assert result["transaction_count"] == 1
    assert result["category_totals"] == {
        "Food": 100
    }


def test_missing_category():
    transactions = [
        {"amount": 100},
        {"amount": 50, "category": None},
    ]

    result = summarize_transactions(transactions)

    assert result["category_totals"] == {
        "Unknown": 150
    }


def test_empty_input():
    result = summarize_transactions([])

    assert result == {
        "total_amount": 0,
        "transaction_count": 0,
        "category_totals": {},
    }


def test_original_input_is_not_modified():
    transactions = [
        {"amount": 100, "category": "Food"}
    ]

    original = [transaction.copy() for transaction in transactions]

    summarize_transactions(transactions)

    assert transactions == original