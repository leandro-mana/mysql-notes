# Chapter 12: JSON, Text & Advanced Data Types

## Overview

Modern data pipelines frequently handle semi-structured data (JSON from APIs), full-text
search requirements, and complex date/time logic. This chapter covers MySQL 8's powerful
JSON functions, full-text search capabilities, and advanced data type handling — skills
you will use daily as a Data Engineer.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [JSON Functions](01_json_functions.ipynb) | JSON data type, JSON_OBJECT, JSON_ARRAY, JSON_EXTRACT, ->/->>, JSON_SET/REPLACE/REMOVE, JSON_CONTAINS, indexing JSON |
| 2 | [Text Search](02_text_search.ipynb) | FULLTEXT indexes, MATCH...AGAINST, natural language & boolean mode, relevance scoring, LIKE vs REGEXP vs FULLTEXT |
| 3 | [Dates & Advanced Types](03_dates_and_advanced_types.ipynb) | DATE/TIME functions, ENUM/SET, spatial basics, BIT operations, generated columns |

## Key Concepts

- **JSON column type**: Native binary JSON storage with validation and indexing support
- **FULLTEXT index**: Specialized index for natural-language text search
- **Generated columns**: Virtual or stored columns computed from expressions — great for indexing JSON
- **ENUM/SET**: Constrained string types useful for categorical data

## Prerequisites

- Chapters 1-10 (basic SQL, DDL, indexes)
- The `mysql_notes` database running in Docker with sample data loaded
