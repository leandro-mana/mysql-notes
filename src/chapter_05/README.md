# Chapter 05: JOINs — Deep Dive

This chapter provides a comprehensive look at all JOIN types in MySQL, including
visual explanations, self-joins, multi-table joins, anti-join patterns, and
performance considerations critical for Data Engineers.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | `01_inner_and_outer_joins.ipynb` | INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN (simulated), finding unmatched records |
| 2 | `02_cross_self_and_advanced_joins.ipynb` | CROSS JOIN, SELF JOIN, multi-table JOINs, NATURAL JOIN, USING clause vs ON |
| 3 | `03_anti_joins_and_patterns.ipynb` | Anti-join (LEFT JOIN + IS NULL), semi-join (EXISTS), NOT IN vs NOT EXISTS, join ordering tips |

## Key Concepts

- **INNER JOIN** — only matching rows from both tables
- **LEFT / RIGHT JOIN** — all rows from one side, matched rows from the other
- **FULL OUTER JOIN** — simulated in MySQL via UNION of LEFT and RIGHT joins
- **CROSS JOIN** — Cartesian product of two tables
- **SELF JOIN** — joining a table to itself (hierarchies, comparisons)
- **Anti-Join** — finding rows with no match using LEFT JOIN + IS NULL
- **Semi-Join** — checking existence without duplicating rows (EXISTS)
- **Performance** — NOT IN vs NOT EXISTS, join ordering, index considerations
