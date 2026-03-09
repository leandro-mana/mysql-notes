# Chapter 04: Aggregations & GROUP BY

This chapter covers aggregate functions, grouping data with GROUP BY, filtering
groups with HAVING, and advanced reporting patterns like ROLLUP for subtotals.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | `01_aggregate_functions.ipynb` | COUNT, SUM, AVG, MIN, MAX, COUNT(DISTINCT), GROUP_CONCAT |
| 2 | `02_group_by_and_having.ipynb` | GROUP BY (single/multiple columns), HAVING, WHERE vs HAVING, GROUP BY with expressions |
| 3 | `03_rollup_and_analytics.ipynb` | GROUP BY WITH ROLLUP, subtotals, grand totals, practical reporting queries |

## Key Concepts

- **Aggregate Functions** — COUNT, SUM, AVG, MIN, MAX for summarizing data
- **COUNT(DISTINCT)** — counting unique values within groups
- **GROUP_CONCAT** — concatenating values within a group into a single string
- **GROUP BY** — partitioning rows into groups for aggregation
- **HAVING** — filtering groups after aggregation (vs WHERE which filters before)
- **ROLLUP** — automatic subtotals and grand totals for hierarchical reporting
- **Analytics Patterns** — revenue by period, top-N per group, running comparisons
