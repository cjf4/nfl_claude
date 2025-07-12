# NFL Analytics Project

A simple, maintainable project for NFL data analysis and visualization.

## Structure

- **`data/`** - NFL data pipeline using nflfastr, dbt for transformations
- **`analysis/`** - Python notebooks and custom analysis scripts  
- **`webapp/`** - Future web application for public insights
- **`nfl_env/`** - Python virtual environment

## Getting Started

### 1. Activate Virtual Environment
```bash
source nfl_env/bin/activate
```

### 2. Run Components
```bash
# Data pipeline
python data/download_nflfastr.py

# Analysis
cd analysis && jupyter lab

# Web app (future)
cd webapp
```

## Current Status

✅ **500 plays** across 5 seasons (2020-2024)  
✅ **112 comprehensive nflfastR columns** per play  
✅ **Virtual environment** with all dependencies  
✅ **Sample analysis notebook** ready to use

## Requirements

- Python 3.9+
- Virtual environment: `nfl_env/` (already created)