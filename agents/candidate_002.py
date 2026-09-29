def summarize_transactions(transactions):
    total_amount = 0
    transaction_count = 0
    category_totals = {}

    for transaction in transactions:
        amount = transaction.get("amount")

        if not isinstance(amount, (int, float)):
            continue

        category = transaction.get("category") or "Unknown"

        total_amount += amount
        transaction_count += 1

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    return {
        "total_amount": total_amount,
        "transaction_count": transaction_count,
        "category_totals": category_totals,
    }