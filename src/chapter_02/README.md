# Chapter 02: DML — INSERT, UPDATE, DELETE

This chapter covers data manipulation language (DML) operations: inserting rows,
updating existing data, deleting records safely, and MySQL-specific UPSERT patterns
that are essential for Data Engineers building idempotent pipelines.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | `01_insert_operations.ipynb` | INSERT INTO (single row, multi-row), INSERT...SELECT, INSERT IGNORE, REPLACE INTO |
| 2 | `02_update_and_delete.ipynb` | UPDATE with WHERE, UPDATE with JOIN, multi-table UPDATE, DELETE with WHERE, DELETE with JOIN, TRUNCATE vs DELETE |
| 3 | `03_upsert_patterns.ipynb` | INSERT...ON DUPLICATE KEY UPDATE, REPLACE INTO, practical UPSERT patterns for idempotent loads |

## Key Concepts

- **INSERT** — single-row, multi-row, and INSERT...SELECT for bulk loading
- **INSERT IGNORE** — skip rows that violate constraints instead of failing
- **UPDATE** — conditional updates, joined updates, multi-table updates
- **DELETE** — safe deletion with WHERE, joined deletes, cascading effects
- **TRUNCATE vs DELETE** — performance and transactional differences
- **UPSERT** — INSERT...ON DUPLICATE KEY UPDATE for idempotent data loads
