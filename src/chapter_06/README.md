# Chapter 6: Subqueries & Common Table Expressions (CTEs)

## Overview

Subqueries and CTEs are essential tools for breaking down complex data problems into
manageable pieces. This chapter covers how to nest queries, use CTEs for readability,
and leverage recursive CTEs for hierarchical data — all critical skills for Data Engineers.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Subqueries](01_subqueries.ipynb) | Scalar subqueries, WHERE subqueries (IN, ANY, ALL), derived tables, correlated subqueries, EXISTS vs IN |
| 2 | [Common Table Expressions](02_common_table_expressions.ipynb) | WITH clause, multiple CTEs, CTE vs subquery readability, step-by-step transformations |
| 3 | [Recursive CTEs](03_recursive_ctes.ipynb) | Recursive syntax, hierarchy traversal, date series generation, depth limiting |

## Key Concepts

- **Scalar subquery**: Returns a single value; usable anywhere an expression is valid
- **Correlated subquery**: References the outer query — executes once per outer row
- **CTE (Common Table Expression)**: Named temporary result set defined with `WITH`
- **Recursive CTE**: A CTE that references itself to traverse hierarchical data

## Prerequisites

- Chapters 1-5 (basic SELECT, JOINs, aggregation)
- The `mysql_notes` database running in Docker with sample data loaded
