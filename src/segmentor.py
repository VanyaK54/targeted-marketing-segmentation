import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import joblib
import matplotlib.pyplot as plt

def run_segmentation(n_clusters=4):
    df = pd.read_csv("data/processed/customer_features.csv")

    X = df[['age', 'gender_encoded', 'income', 'avg_spent', 'total_txn', 'region_encoded']]
    X_scaled = StandardScaler().fit_transform(X)

    # Dimensionality reduction
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_pca)

    df['cluster'] = clusters

    # Save model
    joblib.dump(kmeans, "models/customer_segmentation.pkl")

    # Save cluster assignment
    df.to_csv("data/processed/segmented_customers.csv", index=False)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
    plt.title("Customer Segments (PCA + KMeans)")
    plt.savefig("outputs/plots/clusters_plot.png")

    print("✅ Segmentation complete. Outputs saved.")
    return df
