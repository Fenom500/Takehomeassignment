import pandas as pd

# Load the data
transaction_log = pd.read_csv('wms_inventory_transaction_log.csv')

# Filter for picking operation type
picking_data = transaction_log[transaction_log['operation_type'] == 'Picking']

# Group by order_id and sum quantities
order_sizes = picking_data.groupby('order_id')['quantity'].sum()

# Generate distribution
order_size_distribution = order_sizes.describe()
print(order_size_distribution)
