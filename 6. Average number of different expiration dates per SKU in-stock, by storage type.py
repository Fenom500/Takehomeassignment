import pandas as pd

# Load the data
transaction_log = pd.read_csv('wms_inventory_transaction_log.csv')
inventory_summary = pd.read_csv('wms_inventory_summary.csv')

# Count distinct expiration dates per SKU
expiration_dates_count = inventory_summary.groupby('item_number')['expiration_timestamp'].nunique().reset_index()

# Merge with item info to get storage type
expiration_dates_count = pd.merge(expiration_dates_count, item_info, on='item_number')

# Calculate average number of expiration dates per storage type
avg_expiration_dates = expiration_dates_count.groupby('storage_type')['expiration_timestamp'].mean()
print(avg_expiration_dates)
