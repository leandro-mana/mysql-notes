# Chapter 7: Window Functions

## Overview

Window functions perform calculations across a set of rows related to the current row,
without collapsing the result set like GROUP BY. They are arguably the most important
SQL feature for Data Engineers — enabling ranking, running totals, period-over-period
comparisons, and moving averages.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Ranking Functions](01_ranking_functions.ipynb) | ROW_NUMBER, RANK, DENSE_RANK, NTILE, top-N per group |
| 2 | [Analytic Functions](02_analytic_functions.ipynb) | LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE, period-over-period |
| 3 | [Aggregate Windows & Frames](03_aggregate_windows_and_frames.ipynb) | SUM/AVG/COUNT OVER, running totals, moving averages, frame specs |

## Key Concepts

- **OVER()**: Defines the window — which rows to include in the calculation
- **PARTITION BY**: Divides rows into groups (like GROUP BY, but without collapsing)
- **ORDER BY** (in OVER): Determines the order of rows within each partition
- **Frame specification**: Controls exactly which rows within the partition to include (ROWS BETWEEN, RANGE BETWEEN)

## Prerequisites

- Chapters 1-6 (SELECT, JOINs, aggregation, subqueries)
- Understanding of GROUP BY vs non-grouped queries
