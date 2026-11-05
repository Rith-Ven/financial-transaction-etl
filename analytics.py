
import csv
import sqlite3
from pathlib import Path

DATABASE_FILE = Path("transactions.db")
REPORT_DIR = Path("reports")


def export_query(conn, query, output_file):
    """Run a SQL query and export its results to CSV."""
    cursor = conn.execute(query)

    with output_file.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(cursor.fetchall())


def main():
    REPORT_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DATABASE_FILE) as conn:

        # Aggregate completed transactions by date.
        export_query(
            conn,
            """
            SELECT
                DATE(timestamp) AS transaction_date,
                COUNT(*) AS transaction_count,
                ROUND(SUM(amount), 2) AS total_amount,
                ROUND(AVG(amount), 2) AS average_amount
            FROM transactions
            WHERE status = 'completed'
            GROUP BY DATE(timestamp)
            ORDER BY transaction_date
            """,
            REPORT_DIR / "daily_summary.csv"
        )

        # Flag unusually large completed transactions.
        export_query(
            conn,
            """
            SELECT
                transaction_id,
                user_id,
                amount,
                category,
                timestamp
            FROM transactions
            WHERE status = 'completed'
              AND amount > 900
            ORDER BY amount DESC
            """,
            REPORT_DIR / "suspicious_transactions.csv"
        )

    print("Generated daily_summary.csv")
    print("Generated suspicious_transactions.csv")


if __name__ == "__main__":
    main()
