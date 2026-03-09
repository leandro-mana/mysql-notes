# Chapter 11: Data Modeling & Normalization

## Overview

Good data modeling is the foundation of every reliable data pipeline. This chapter covers
normalization theory (1NF through BCNF), when to intentionally denormalize, and dimensional
modeling patterns (star/snowflake schemas) used in analytics warehouses — all critical
knowledge for Data Engineers designing or maintaining production systems.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Normalization](01_normalization.ipynb) | 1NF, 2NF, 3NF, BCNF, practical normalization examples, when to normalize vs denormalize |
| 2 | [Schema Design Patterns](02_schema_design_patterns.ipynb) | Star schema, snowflake schema, slowly changing dimensions (SCD Types 1-3), surrogate vs natural keys |
| 3 | [Data Modeling for Analytics](03_data_modeling_for_analytics.ipynb) | OLTP vs OLAP design, wide tables, pre-aggregation, materialized view patterns, partitioning strategies |

## Key Concepts

- **Normal Forms**: Progressive rules that eliminate data redundancy and update anomalies
- **Denormalization**: Intentionally adding redundancy for read performance
- **Star Schema**: Fact table at center surrounded by dimension tables — the analytics standard
- **Slowly Changing Dimensions**: Strategies for tracking historical changes in dimension data
- **Partitioning**: Splitting large tables into smaller physical segments for query performance

## Prerequisites

- Chapters 1-10 (JOINs, aggregation, window functions, DDL)
- The `mysql_notes` database running in Docker with sample data loaded
