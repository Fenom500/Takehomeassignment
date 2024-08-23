import pandas as pd
import datetime

# Merge inventory summary with item info to get storage type
inventory_summary = pd.read_csv('wms_inventory_summary.csv')
item_info = pd.read_csv('wms_item_info.csv')

# Merge data
merged_data = pd.merge(inventory_summary, item_info, on='item_number')

# Filter for frozen items
frozen_inventory = merged_data[merged_data['storage_type'] == 'frozen']

# Calculate DOI
current_date = datetime.datetime.now().timestamp()
frozen_inventory['DOI'] = (frozen_inventory['expiration_timestamp'] - current_date) / (60 * 60 * 24)

# Group by warehouse and calculate average DOI
average_doi = frozen_inventory.groupby('warehouse_id')['DOI'].mean()
print(average_doi)
