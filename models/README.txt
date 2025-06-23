📦 Customer Segmentation Model – KMeans

This folder contains the trained clustering model for customer segmentation.

- Filename: customer_segmentation.pkl
- Model Type: KMeans (4 clusters)
- Input Features: age, gender_encoded, income, avg_spent, total_txn, region_encoded
- Preprocessing: StandardScaler + PCA (2D projection)
- Tool: Scikit-learn 1.4

Use joblib to load this model:
>>> import joblib
>>> model = joblib.load("models/customer_segmentation.pkl")

# Azure SQL Connection
AZURE_SQL_SERVER=yourserver.database.windows.net
AZURE_SQL_DB=your_database_name
AZURE_SQL_USER=your_username
AZURE_SQL_PWD=your_password

# Optional: Azure Blob Storage if used
AZURE_BLOB_ACCOUNT_NAME=yourblobaccount
AZURE_BLOB_ACCOUNT_KEY=yourkey
AZURE_BLOB_CONTAINER_NAME=yourcontainer
