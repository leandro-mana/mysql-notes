# MySQL Notes

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![Notebooks](https://img.shields.io/badge/Notebooks-45-green)
![Chapters](https://img.shields.io/badge/Chapters-15-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Interactive MySQL notes and SQL notebooks for Data Engineers — from fundamentals to real-world ETL patterns. All content is delivered through executable Jupyter notebooks using [JupySQL](https://jupysql.ploomber.io/) `%%sql` magic against a local MySQL 8.0 Docker container.

## Requirements

- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)

## Quick Start

```bash
# 1. Install dependencies
make install

# 2. Start MySQL container
make up

# 3. Open notebooks for a chapter
make jupyter CH=01
```

## Project Structure

```text
mysql-notes/
├── src/
│   ├── common/              # Connection utilities
│   ├── chapter_01/          # Database Fundamentals & DDL
│   ├── chapter_02/          # DML — INSERT, UPDATE, DELETE
│   ├── ...
│   └── chapter_15/          # Real-World Data Engineering Recipes
├── tests/                   # Pytest test suite
├── scripts/
│   └── init.sql             # Database seed data
├── docker-compose.yml       # MySQL 8.0 container
├── Makefile                 # Automation commands
└── pyproject.toml           # Poetry configuration
```

## Chapters

| Chapter | Notebooks | Topics |
| --- | --- | --- |
| **01 - Database Fundamentals & DDL** | 3 | Data types, CREATE/ALTER/DROP, constraints, schema management |
| **02 - DML — INSERT, UPDATE, DELETE** | 3 | CRUD operations, UPSERT patterns, idempotent loads |
| **03 - SELECT, Filtering & Sorting** | 3 | WHERE, LIKE, REGEXP, ORDER BY, pagination patterns |
| **04 - Aggregations & GROUP BY** | 3 | COUNT/SUM/AVG, GROUP BY, HAVING, ROLLUP, analytics |
| **05 - JOINs — Deep Dive** | 3 | INNER/LEFT/RIGHT/CROSS/SELF JOIN, anti-joins, data quality |
| **06 - Subqueries & CTEs** | 3 | Scalar/correlated subqueries, CTEs, recursive CTEs |
| **07 - Window Functions** | 3 | ROW_NUMBER, RANK, LAG/LEAD, running totals, frames |
| **08 - Views, Indexes & Performance** | 3 | Views, B-Tree/composite indexes, EXPLAIN basics |
| **09 - Stored Procedures & Functions** | 3 | Procedures, functions, cursors, triggers, events |
| **10 - Transactions & Concurrency** | 3 | ACID, isolation levels, locking, deadlock handling |
| **11 - Data Modeling & Normalization** | 3 | 1NF-BCNF, star/snowflake schemas, SCD patterns |
| **12 - JSON, Text & Advanced Types** | 3 | JSON functions, FULLTEXT search, date/time, spatial |
| **13 - Query Optimization & EXPLAIN** | 3 | EXPLAIN deep dive, index strategies, query rewriting |
| **14 - ETL Patterns for Data Engineers** | 3 | Staging tables, bulk loads, UPSERT, CDC, incremental |
| **15 - Real-World DE Recipes** | 3 | Deduplication, pivot/unpivot, gaps, hierarchies |

## Running Notebooks

```bash
# Open a specific chapter in Jupyter Lab
make jupyter CH=07

# List all chapters
make list-chapters

# List notebooks in a chapter
make list-notebooks CH=05
```

## Docker (MySQL)

```bash
# Start MySQL container (localhost:3306)
make up

# Stop and remove volumes
make down

# Rebuild from scratch
make reset
```

Connection details:

- **Host**: `localhost:3306`
- **User**: `root`
- **Password**: `root_password`
- **Database**: `mysql_notes`

## Code Quality

```bash
make lint           # Ruff linter
make format         # Auto-format
make type-check     # mypy
make check          # All checks
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for workflow, commit conventions, and code style guidelines.

## References

- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [JupySQL Documentation](https://jupysql.ploomber.io/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- Analytics Engineering with SQL and dbt (O'Reilly)

## License

MIT
