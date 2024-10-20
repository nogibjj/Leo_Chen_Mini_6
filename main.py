from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


# Extract
print("Extracting data...")
extract()

# Load
print("Loading data...")
load()

# Query
print("Querying data...")
query()