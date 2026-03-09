# Chapter 01: Database Fundamentals & DDL

This chapter covers the foundational building blocks of MySQL databases: data types,
database and table creation, constraints, and schema management.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | `01_data_types_and_databases.ipynb` | MySQL data types (INT, VARCHAR, DECIMAL, DATE, TIMESTAMP, ENUM, JSON, BLOB), CREATE/DROP DATABASE, character sets |
| 2 | `02_create_tables_and_constraints.ipynb` | CREATE TABLE, PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, DEFAULT, CHECK constraints, AUTO_INCREMENT |
| 3 | `03_alter_and_manage_schema.ipynb` | ALTER TABLE (ADD, MODIFY, DROP COLUMN, RENAME), DROP TABLE, TRUNCATE, SHOW TABLES, DESCRIBE, information_schema |

## Key Concepts

- **CREATE DATABASE / DROP DATABASE** — provisioning and removing databases
- **Data Types** — choosing the right type for storage efficiency and correctness
- **CREATE TABLE** — defining tables with columns and inline constraints
- **Constraints** — PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, DEFAULT, CHECK
- **ALTER TABLE** — evolving schemas without data loss
- **Schema Inspection** — SHOW, DESCRIBE, and information_schema queries
