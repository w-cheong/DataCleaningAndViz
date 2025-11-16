# DataCleaningAndViz

This is my submission for the Data Cleaning & Viz assignment.

## Tasks

- [x] csv loaded
- [x] inspect shape
- [x] quick schema/null summary
- [x] row preview
- [x] snake case
- [x] trim whitespace
- [X] standardize text case
- [X] map items
- [X] define schema
- [X] parse dates
- [X] deduplicate row if needed
- [X] store cleaned.parquet
- [X] aggregations of cleaned.parquet
- [ ] Streamlit screenshots

---

For `validated` column, use "Yes", "No", or "". 
Convert all values to one of these three.

```
{'-', 'N', 'NO', 'No', 'Y', 'YES', 'Yes', 'n', 'na', nan, 'y'}
```

## Instructions

Raw Data:  Load the CSV into Pandas or Polars, inspect shape, preview rows, and capture a quick schema/null summary.

Normalize schema: Convert headers to snake_case, trim whitespace, standardize text case, and map obvious items ("", "NA", "N/A", "null", "-") to one standard value of your choice. Fix the date format to yyyy-MM-dd, trim the unwanted spaces

Define a target schema (dates, strings, ints, floats, bools), parse dates, deduplicate row if any, and store the file as cleaned.parquet.

Load the cleaned.parquet and create 2–3 small aggregations (e.g., daily avg close by ticker, avg volume by sector, simple daily return by ticker) and save to an agg1.parquet, agg2.parquet and so on.

Finally Load the aggregates parquet, add filters (date range, ticker), show various charts using StreamLit library. 
https://streamlit.io/

Deliverables: Minimal GitHub repo with your Python code, data files, README.md and 3 to 5 screen shots of your Streamlit output.

Submit your Repo.

Note: Use UV and VSCode for your development.

## Points breakdown (out of 50)

* Data Cleaning – 10 
* Aggregations Process – 10
* Using Streamlit – 20
* Coding hygiene (comments, structure, README clarity) – 10