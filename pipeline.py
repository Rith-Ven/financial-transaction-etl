
import csv
from datetime import datetime, timezone
from pathlib import Path

INPUT_FILE = Path("data/transactions.csv")


def extract():
    """Read transactions from the source CSV."""
    with INPUT_FILE.open("r", newline="") as file:
        reader = csv.DictReader(file)
        transactions = list(reader)

    print(f"Extracted {len(transactions)} transactions")
    return transactions


def transform(transactions):
    """Validate and normalize transaction records."""
    cleaned = []
    seen_ids = set()

    for row in transactions:
        transaction_id = row["transaction_id"].strip()

        # Skip duplicate or missing transaction IDs.
        if not transaction_id or transaction_id in seen_ids:
            continue

        try:
            amount = float(row["amount"])
            if not 0 < amount < float("inf"):
                continue

            user_id = int(row["user_id"])
            if user_id <= 0:
                continue

            # Parse timestamp and normalize to UTC.
            timestamp = datetime.fromisoformat(row["timestamp"])
            if timestamp.tzinfo is None:
                continue

            timestamp = timestamp.astimezone(
                timezone.utc
            ).isoformat()

        except (ValueError, TypeError, KeyError):
            continue

        cleaned.append({
            "transaction_id": transaction_id,
            "user_id": user_id,
            "amount": round(amount, 2),
            "category": row["category"].strip(),
            "status": row["status"].strip(),
            "timestamp": timestamp
        })

        seen_ids.add(transaction_id)

    print(f"Validated {len(cleaned)} transactions")
    return cleaned


def main():
    raw_transactions = extract()
    cleaned_transactions = transform(raw_transactions)

    print("Sample cleaned transaction:")
    print(cleaned_transactions[0] if cleaned_transactions else "None")


if __name__ == "__main__":
    main()
