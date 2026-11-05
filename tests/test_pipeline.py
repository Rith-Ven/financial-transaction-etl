
import sqlite3
import sys
from pathlib import Path

# Allow tests to import pipeline.py from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pipeline import transform, load


def sample_transaction(transaction_id="TXN001", amount="100.50"):
    return {
        "transaction_id": transaction_id,
        "user_id": "1",
        "amount": amount,
        "category": "groceries",
        "status": "completed",
        "timestamp": "2026-01-01T12:00:00+00:00",
    }


def test_valid_transaction():
    result = transform([sample_transaction()])

    assert len(result) == 1
    assert result[0]["amount"] == 100.50


def test_invalid_amount():
    result = transform([
        sample_transaction("TXN001", "-20"),
        sample_transaction("TXN002", "abc"),
    ])

    assert len(result) == 0


def test_duplicate_transactions():
    result = transform([
        sample_transaction("TXN001"),
        sample_transaction("TXN001"),
    ])

    assert len(result) == 1


def test_incremental_loading(tmp_path, monkeypatch):
    import pipeline

    test_db = tmp_path / "test_transactions.db"
    monkeypatch.setattr(pipeline, "DATABASE_FILE", test_db)

    transactions = transform([sample_transaction()])

    load(transactions)
    load(transactions)

    with sqlite3.connect(test_db) as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM transactions"
        ).fetchone()[0]

    assert count == 1
