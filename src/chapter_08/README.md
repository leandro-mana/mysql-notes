# Chapter 8: Views, Indexes & Performance Basics

## Overview

Understanding views, indexes, and query performance is what separates a Data Engineer
who writes SQL from one who writes *efficient* SQL. This chapter covers the tools
MySQL provides for organizing queries (views), speeding them up (indexes), and
diagnosing bottlenecks (EXPLAIN).

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Views](01_views.ipynb) | CREATE VIEW, updatable views, views with JOINs/aggregations, practical patterns |
| 2 | [Indexes](02_indexes.ipynb) | B-Tree, Hash, Full-text, composite indexes, covering indexes, index on expressions |
| 3 | [Performance Basics](03_performance_basics.ipynb) | EXPLAIN, EXPLAIN ANALYZE, reading query plans, anti-patterns, query hints |

## Key Concepts

- **View**: A stored SELECT query that acts like a virtual table
- **Index**: A data structure that speeds up row lookups at the cost of write overhead
- **EXPLAIN**: MySQL's tool for showing how it plans to execute a query
- **Covering index**: An index that contains all columns needed by a query

## Prerequisites

- Chapters 1-7 (all query types, window functions)
- Basic understanding of how databases store data
