# Chapter 14: ETL Patterns for Data Engineers

## Overview

ETL (Extract, Transform, Load) is the bread and butter of Data Engineering. This chapter
covers battle-tested patterns for staging data, bulk loading, upserting records, and
building idempotent pipelines — all implemented in pure SQL within MySQL.

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | [Staging & Bulk Load](01_staging_and_bulk_load.ipynb) | Staging tables, LOAD DATA INFILE, bulk INSERT optimization, CREATE TABLE...SELECT, INSERT INTO...SELECT |
| 2 | [UPSERT & Merge](02_upsert_and_merge.ipynb) | INSERT...ON DUPLICATE KEY UPDATE, REPLACE INTO, merge patterns, idempotent loads, late-arriving data |
| 3 | [CDC & Incremental Loads](03_cdc_and_incremental.ipynb) | Change Data Capture concepts, timestamp-based extraction, high-water mark, audit columns, incremental aggregation |

## Key Concepts

- **Staging table**: Temporary landing zone for raw data before transformation and merge
- **UPSERT**: INSERT or UPDATE in a single atomic statement (INSERT...ON DUPLICATE KEY UPDATE)
- **Idempotent load**: A pipeline that produces the same result whether run once or many times
- **High-water mark**: Tracking the last processed timestamp/ID for incremental extraction
- **Change Data Capture (CDC)**: Detecting and propagating data changes from source systems

## Prerequisites

- Chapters 1-11 (SQL fundamentals, DDL, data modeling)
- The `mysql_notes` database running in Docker with sample data loaded
