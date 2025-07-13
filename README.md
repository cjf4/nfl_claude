# NFL Analytics Project

This is my (Chris Fenton's) NFL data analysis project. The goal is to make it easy
to create and share my analysis on NFL trends.

Software used:
- nflfastr for data
- dbt for analytics schema building
- claude code 
- pandas for data analysis


## Structure

- **`data/`** - NFL data pipeline using nflfastr, dbt for transformations
- **`analysis/`** - Python notebooks and custom analysis scripts  
- **`webapp/`** - Web app (currently empty)
- **`nfl_env/`** - Python virtual environment

## Getting Started

### 1. Activate Virtual Environment
```bash
source nfl_env/bin/activate
```

### 2. Update data
```bash
Rscript data/update_db.R
```

## Features

- ETL flow to download nflastR data set to DuckDB
- DBT transformations to build analytics schema derived from nflfastR play by play (pbp) data

