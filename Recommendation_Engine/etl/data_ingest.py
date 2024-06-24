from sqlalchemy import text
import pandas as pd
from os.path import join

from database import engine, _add_tables
from models import (DEVICE_DIRECTORY, SUB_DEVICE_DIRECTORY)

def load_csv_to_table(table_name, csv_path):
    """
    Load data from a CSV file into a database table.

    Args:
    - table_name: Name of the database table.
    - csv_path: Path to the CSV file containing data.

    Returns:
    - None
    """
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

    
# Initiating Database Tables
_add_tables(engine)

# Define a list containing table names and their corresponding CSV file paths
tables_to_load = [
    "DEVICE_DIRECTORY",
    "SUB_DEVICE_DIRECTORY"
]

# Loop through the list of tables and CSV file paths, and load each CSV into its corresponding table
for table in tables_to_load:
    try:
        load_csv_to_table(table, join("data/", f"{table}.csv"))
    except Exception as e:
        print(f"Failed to ingest table {table}. Moving to the next!")

print("Tables are populated.")