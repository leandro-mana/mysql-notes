# Chapter 9: Stored Procedures & Functions

## Overview

Stored procedures and functions let you encapsulate SQL logic on the database server.
While modern Data Engineering often favors application-level logic (Python, dbt),
understanding server-side programming is essential for working with legacy systems,
building database-level validations, and writing performant ETL routines.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Stored Procedures](01_stored_procedures.ipynb) | CREATE PROCEDURE, parameters, variables, control flow (IF, CASE, LOOP) |
| 2 | [Functions & Cursors](02_functions_and_cursors.ipynb) | CREATE FUNCTION, determinism, cursors, error handlers, ETL procedures |
| 3 | [Triggers & Events](03_triggers_and_events.ipynb) | BEFORE/AFTER triggers, audit trails, scheduled events |

## Key Concepts

- **Stored Procedure**: A named block of SQL statements callable with `CALL`
- **User-Defined Function**: Returns a single value, usable in SELECT/WHERE
- **Cursor**: Iterates over a result set row by row (use sparingly)
- **Trigger**: Automatically fires on INSERT/UPDATE/DELETE
- **Event**: Scheduled task that runs on a timer

## Important Note for JupySQL Users

The `%%sql` magic does not support `DELIMITER` changes. For multi-statement
procedures, you need to either:
1. Use single-statement procedures (shown in these notebooks)
2. Create procedures via a Python connection with `pymysql` directly
3. Use MySQL Workbench or the `mysql` CLI for complex procedure definitions

## Prerequisites

- Chapters 1-8 (all query types, views, indexes)
