import pandas as pd

# Load the data
transaction_log = pd.read_csv('wms_inventory_transaction_log.csv')

# Extract aisle from location_no
inventory_summary['aisle'] = inventory_summary['location_no'].str[:1]

# Merge with item info to get storage type
merged_inventory = pd.merge(inventory_summary, item_info, on='item_number')

# Group by warehouse, storage type, and aisle, then sum quantities
units_picked_distribution = merged_inventory.groupby(['warehouse_id', 'storage_type', 'aisle'])['quantity'].sum()

print(units_picked_distribution.describe())
