
import csv
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

random.seed(42)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "transactions.csv"

CATEGORIES = ["groceries", "rent", "shopping", "transport", "utilities"]
STATUSES = ["completed", "pending", "failed"]

with OUTPUT_FILE.open("w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "user_id",
        "amount",
        "category",
        "status",
        "timestamp"
    ])

    for i in range(1, 1201):
        timestamp = datetime(2026, 1, 1, tzinfo=timezone.utc)
        timestamp += timedelta(hours=random.randint(0, 2000))

        writer.writerow([
            f"TXN{i:05d}",
            random.randint(1, 100),
            round(random.uniform(5, 1000), 2),
            random.choice(CATEGORIES),
            random.choice(STATUSES),
            timestamp.isoformat()
        ])

print(f"Generated 1,200 transactions in {OUTPUT_FILE}")
