# Chapter 13: Query Optimization & EXPLAIN

## Overview

Understanding how MySQL executes your queries is the difference between a pipeline that runs
in seconds and one that takes hours. This chapter teaches you to read EXPLAIN output, design
effective indexes, and rewrite queries for performance — the most impactful skills a Data
Engineer can develop.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [EXPLAIN Deep Dive](01_explain_deep_dive.ipynb) | EXPLAIN columns, EXPLAIN ANALYZE, FORMAT=JSON/TREE, access types (ALL through const), reading execution plans |
| 2 | [Index Optimization](02_index_optimization.ipynb) | Composite indexes, covering indexes, index condition pushdown, index merge, FORCE INDEX, when indexes are ignored |
| 3 | [Query Rewriting](03_query_rewriting.ipynb) | Subqueries to JOINs, pagination optimization, batching, EXISTS vs IN, UNION vs UNION ALL, slow query log |

## Key Concepts

- **EXPLAIN**: Shows the query execution plan without running the query
- **Access types**: From worst (ALL = full table scan) to best (const = single row lookup)
- **Covering index**: An index that contains all columns needed by the query — no table access required
- **Leftmost prefix rule**: Composite indexes are used left-to-right; skipping columns breaks the index
- **Keyset pagination**: Using WHERE id > last_seen_id instead of OFFSET for scalable pagination

## Prerequisites

- Chapters 1-10 (all SQL fundamentals)
- The `mysql_notes` database running in Docker with sample data loaded
