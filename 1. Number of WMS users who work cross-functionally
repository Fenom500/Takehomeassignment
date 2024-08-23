import pandas as pd

# Load the data
transaction_log = pd.read_csv('wms_inventory_transaction_log.csv')

# Convert unix timestamp to datetime
transaction_log['date'] = pd.to_datetime(transaction_log['unixtimestamp'], unit='s').dt.date

# Group by user_name, date and count distinct operation types
user_operation_count = transaction_log.groupby(['user_name', 'date'])['operation_type'].nunique().reset_index()

# Identify cross-functional days
user_operation_count['is_cross_functional'] = user_operation_count['operation_type'] > 1

# Count the number of cross-functional days per user
cross_functional_days = user_operation_count.groupby('user_name')['is_cross_functional'].mean()

# Users with more than 50% cross-functional days
cross_functional_users = cross_functional_days[cross_functional_days > 0.5].index

# Number of cross-functional users
num_cross_functional_users = len(cross_functional_users)
print(num_cross_functional_users)
