# Chapter 10: Transactions & Concurrency Control

## Overview

Transactions ensure data integrity when multiple operations must succeed or fail
together. Understanding isolation levels and locking is essential for Data Engineers
who build ETL pipelines, handle concurrent writes, or work with financial data.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Transactions](01_transactions.ipynb) | ACID, START TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT, auto-commit |
| 2 | [Isolation Levels](02_isolation_levels.ipynb) | READ UNCOMMITTED through SERIALIZABLE, read phenomena, MySQL defaults |
| 3 | [Locking & Deadlocks](03_locking_and_deadlocks.ipynb) | Row locks, table locks, gap locks, deadlock detection, ETL patterns |

## Key Concepts

- **ACID**: Atomicity, Consistency, Isolation, Durability
- **Transaction**: A group of operations that succeed or fail as a unit
- **Isolation level**: How much one transaction can see of another's uncommitted changes
- **Deadlock**: Two transactions each waiting for the other's lock

## Prerequisites

- Chapters 1-9 (all SQL concepts, stored procedures)
- Basic understanding of concurrent access patterns
