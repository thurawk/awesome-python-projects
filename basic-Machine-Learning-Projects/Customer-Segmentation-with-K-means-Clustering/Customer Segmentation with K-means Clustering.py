# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import joblib

# Generate Synthetic Data for Customer Segmentation
np.random.seed(42)

# Generate synthetic data
n_samples = 1000  # Number of customers

# Randomly generate data
age = np.random.randint(18, 70, size=n_samples)
income = np.random.randint(15, 150, size=n_samples)  # In thousands of dollars
spending_score = np.random.randint(1, 101, size=n_samples)  # Score from 1 to 100

# Create DataFrame
df = pd.DataFrame({
    'Age': age,
    'Annual Income (k$)': income,
    'Spending Score (1-100)': spending_score
})

# Display first few rows of the generated data
print(df.head())

# Step 3: Data Preprocessing
# Select relevant features
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Elbow Method to Determine Optimal Clusters
inertia = []  # List to store the sum of squared distances

for k in range(1, 11):  # Try k from 1 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the inertia values
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Step 5: Silhouette Scores to Validate Clusters
silhouette_scores = []  # List to store Silhouette Scores

for k in range(2, 11):  # Try k from 2 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot the Silhouette Scores
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Scores for Different k')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Step 6: Apply K-means Clustering (Assuming k = 5 from the Elbow Method)
k = 5  # Assuming 5 clusters from the elbow method
kmeans = KMeans(n_clusters=k, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# Add cluster labels to the dataset
df['Cluster'] = y_kmeans

# Display first few rows with cluster labels
print(df.head())

# Step 7: Visualize the Clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='viridis', s=100)
plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# Step 8: Analyze the Results
cluster_summary = df.groupby('Cluster').mean()
print(cluster_summary)

# Step 9: Save the Trained K-means Model and Scaler
joblib.dump(kmeans, 'kmeans_customer_segmentation_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load the saved model and scaler
loaded_model = joblib.load('kmeans_customer_segmentation_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# Step 10: Predict New Customer Data
new_data = np.array([[25, 80, 30]])  # Example: new customer data [Age, Income, Spending Score]
new_data_scaled = loaded_scaler.transform(new_data)  # Don't forget to scale new data
predicted_cluster = loaded_model.predict(new_data_scaled)
print(f"Predicted cluster for new customer: {predicted_cluster}")
