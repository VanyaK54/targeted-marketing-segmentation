import pandas as pd

def clean_customer_data(customers_fp, transactions_fp, campaign_fp):
    customers = pd.read_csv(customers_fp)
    transactions = pd.read_csv(transactions_fp)
    campaigns = pd.read_csv(campaign_fp)

    # Drop nulls
    customers.dropna(inplace=True)

    # Encode categorical variables
    gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
    region_map = {name: idx for idx, name in enumerate(customers['region'].unique(), 1)}

    customers['gender_encoded'] = customers['gender'].map(gender_map)
    customers['region_encoded'] = customers['region'].map(region_map)

    # Transaction features
    txn_summary = transactions.groupby('customer_id')['amount_spent'].agg(['mean', 'count']).reset_index()
    txn_summary.columns = ['customer_id', 'avg_spent', 'total_txn']

    # Merge
    final_df = customers.merge(txn_summary, on='customer_id', how='left').fillna(0)

    # Save cleaned data
    final_df.to_csv("data/proc
