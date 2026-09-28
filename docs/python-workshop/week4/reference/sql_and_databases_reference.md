# Reference: SQL and Databases

This course has mainly used CSV files, pandas DataFrames, GeoDataFrames, and notebooks. Larger, frequently updated, or shared datasets are often stored in a **database**.

## What is a database?

A relational database stores information in tables with rows, columns, identifiers, and relationships between tables.

Examples include:

- SQLite
- PostgreSQL
- MySQL
- Microsoft SQL Server

**PostGIS** extends PostgreSQL with geographic data types and spatial operations.

## What is SQL?

SQL, or Structured Query Language, is used to query relational databases.

Common operations include:

- selecting columns;
- filtering rows;
- sorting;
- joining tables;
- grouping and aggregating records;
- inserting and updating data.

These ideas closely resemble pandas.

### SQL

```sql
SELECT city, population
FROM cities
WHERE province = 'Ontario'
ORDER BY population DESC;
```

### pandas

```python
ontario = cities.loc[
    cities["province"] == "Ontario",
    ["city", "population"]
].sort_values(
    "population",
    ascending=False
)
```

## When should you consider a database?

A database becomes useful when:

- files are becoming very large;
- many tables must be joined repeatedly;
- data changes frequently;
- multiple users or applications need the same data;
- access permissions or data integrity matter;
- you want the database to filter before loading data into Python;
- repeated spatial queries would benefit from a spatial database.

## What you need to know for now

You do not need to build a database in this course.

The important ideas are:

1. CSV files are not the only way to store tables.
2. SQL expresses many of the same operations as pandas.
3. Databases become increasingly useful as projects grow.
4. PostgreSQL + PostGIS is a common choice for larger spatial workflows.

Further reference:

[School of Cities: SQL fundamentals](https://schoolofcities.github.io/urban-data-storytelling/urban-data-analytics/sql-basics/sql-basics.html)
