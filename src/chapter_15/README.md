# Chapter 15: Real-World Data Engineering Recipes

## Overview

This chapter is a cookbook of practical SQL recipes that solve problems Data Engineers
encounter regularly: deduplicating messy data, pivoting reports, detecting gaps in
sequences, and querying hierarchical structures. Each recipe is self-contained and
ready to adapt to your own pipelines.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Deduplication & Data Quality](01_deduplication_and_data_quality.ipynb) | Finding duplicates, dedup strategies, data profiling queries, validation checks |
| 2 | [Pivot, Unpivot & Reshape](02_pivot_unpivot_and_reshape.ipynb) | CASE WHEN pivoting, conditional aggregation, UNION ALL unpivoting, JSON_OBJECTAGG |
| 3 | [Gaps, Sequences & Hierarchies](03_gaps_sequences_and_hierarchies.ipynb) | Gap detection, island detection, recursive CTEs for hierarchies, adjacency list vs nested set |

## Key Concepts

- **Deduplication**: Identifying and removing duplicate rows while preserving the "winner"
- **Pivoting**: Transforming rows into columns for cross-tabulation reports
- **Gap detection**: Finding missing values in sequences (IDs, dates, timestamps)
- **Island detection**: Identifying consecutive ranges within a dataset
- **Adjacency list**: Storing hierarchical data with a parent_id foreign key

## Prerequisites

- Chapters 1-14 (all previous material)
- The `mysql_notes` database running in Docker with sample data loaded
