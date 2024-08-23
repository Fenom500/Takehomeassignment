import pandas as pd

# Load the data
transaction_log = pd.read_csv('wms_inventory_transaction_log.csv')
item_info = pd.read_csv('wms_item_info.csv')

# Merge with item info to get storage type
receiving_data = pd.merge(transaction_log, item_info, on='item_number')

# Filter for dry SKUs and receiving operation
dry_receiving = receiving_data[(receiving_data['storage_type'] == 'dry') & (receiving_data['operation_type'] == 'Receiving')]

# Convert timestamp to date
dry_receiving['date'] = pd.to_datetime(dry_receiving['unixtimestamp'], unit='s').dt.date

# Count pallets received per day
pallets_received_per_day = dry_receiving.groupby('date')['quantity'].sum()
print(pallets_received_per_day)
