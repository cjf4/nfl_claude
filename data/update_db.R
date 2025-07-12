#!/usr/bin/env Rscript

# Simple R script to update NFL database using nflfastR and DuckDB
# Usage: Rscript update_db.R

library(nflfastR)
library(duckdb)
library(DBI)
library(dplyr)
library(dbplyr)

# Configuration
DB_PATH <- "nfl.duckdb"

# Update database with nflfastR data
# This will download/update play-by-play data for all available seasons
update_db(
  dbdir = ".",
  dbname = "nfl.duckdb",
  tblname = "pbp",
  force_rebuild = FALSE
)

cat("NFL database updated successfully at:", DB_PATH, "\n")