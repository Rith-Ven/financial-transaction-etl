
# Financial Transaction ETL Pipeline

A Python and SQL ETL pipeline that processes 1,200 synthetic
financial transactions, validates data quality, and loads
records into SQLite for analysis.

## Technologies
Python, SQL, SQLite, pytest, GitHub Actions

## Pipeline Architecture
CSV → Extract → Validate & Transform → SQLite → SQL Analytics → CSV Reports

## Features
- Generates 1,200 reproducible synthetic financial transactions
- Validates transaction amounts, user IDs, and UTC timestamps
- Removes duplicate transaction IDs
- Uses SQLite primary keys for duplicate-safe incremental loading
- Generates daily spending summaries using SQL aggregation
- Flags completed transactions exceeding $900 for review
- Includes four automated pytest tests
- Runs tests automatically through GitHub Actions

## Run Locally

Requires Python 3.9+.

```bash
python3 generate_data.py
python3 pipeline.py
python3 analytics.py
```

## Run Tests

```bash
python3 -m pip install pytest
python3 -m pytest -q
```

## Data

All transactions are synthetic. No real financial information
is used.

The $900 suspicious-transaction threshold is illustrative
and is not a production fraud-detection system.
