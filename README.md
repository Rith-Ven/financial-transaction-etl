# Financial Transaction ETL Pipeline

A Python and SQL-based ETL pipeline that processes **1,200 synthetic financial transactions**, performs data validation and transformation, and loads clean records into SQLite for analytics.

## Tech Stack

**Python | SQL | SQLite | pytest | GitHub Actions**

## Pipeline Architecture

```text
Synthetic Transaction Data (CSV)
              |
              v
      Extract (Python CSV)
              |
              v
    Transform & Validate
    - Validate amounts and user IDs
    - Normalize timestamps to UTC
    - Remove duplicate transactions
              |
              v
       Load into SQLite
    - Primary key constraints
    - Duplicate-safe ingestion
              |
              v
        SQL Analytics
    - Daily transaction summaries
    - High-value transaction flags
              |
              v
        CSV Reports
```

## Key Features

- **Data ingestion:** Extracts 1,200 reproducible synthetic financial transactions from CSV
- **Data quality:** Validates transaction amounts, user IDs, and timestamps while removing duplicate records
- **Incremental loading:** Uses SQLite primary keys and `INSERT OR IGNORE` to prevent duplicate ingestion across repeated runs
- **SQL analytics:** Calculates daily transaction counts, total amounts, and average transaction values
- **Transaction monitoring:** Flags completed transactions exceeding $900 for review
- **Automated testing:** Includes four pytest tests covering validation, deduplication, and repeat loading
- **Continuous integration:** Uses GitHub Actions to run tests automatically on pushes and pull requests

## Getting Started

**Requirements:** Python 3.9+

Clone the repository:

```bash
git clone https://github.com/Rith-Ven/financial-transaction-etl.git
cd financial-transaction-etl
```

Generate the dataset and run the pipeline:

```bash
python3 generate_data.py
python3 pipeline.py
python3 analytics.py
```

Run the automated tests:

```bash
python3 -m pip install pytest
python3 -m pytest -q
```

## Project Structure

```text
financial-transaction-etl/
├── .github/workflows/tests.yml
├── data/
│   └── transactions.csv
├── reports/
│   ├── daily_summary.csv
│   └── suspicious_transactions.csv
├── tests/
│   └── test_pipeline.py
├── generate_data.py
├── pipeline.py
├── analytics.py
├── README.md
└── .gitignore
```

## Data Privacy and Limitations

All transaction data is synthetically generated and does not contain real customer information.

The $900 high-value transaction threshold is an illustrative monitoring rule, not a trained fraud-detection model. SQLite is used for a lightweight local implementation rather than a distributed production data system.
