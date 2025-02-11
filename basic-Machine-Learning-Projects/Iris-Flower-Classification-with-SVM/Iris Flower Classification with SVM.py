#Building Simple Machine Learning Model(Iris dataset)

import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC # type: ignore
from sklearn.metrics import accuracy_score
import seaborn as sns   # type: ignore
import matplotlib.pyplot as plt     # type: ignore

from sklearn.datasets import load_iris # type: ignore

# Load Iris dataset
iris = load_iris()
X = iris.data  # Features (measurements)
y = iris.target  # Labels (species)

# Convert to DataFrame for better readability
df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = iris.target_names[y]

# Display first few rows
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()

# Fit and transform the training data, then transform the test data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel='linear')  # Using linear kernel for simplicity
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

sns.pairplot(df, hue='species', height=2.5) 
plt.show()

from sklearn.model_selection import GridSearchCV    # type: ignore

# Define the parameter grid
param_grid = {
    'kernel': ['linear', 'poly', 'rbf'],  # Different kernels
    'C': [0.1, 1, 10]  # Regularization parameter
}

# Create GridSearchCV object
grid_search = GridSearchCV(SVC(), param_grid, cv=5)  # 5-fold cross-validation
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters and model
print("Best parameters found:", grid_search.best_params_)
best_model = grid_search.best_estimator_

import joblib

# Save the model
joblib.dump(best_model, 'iris_svm_model.pkl')

# Load the model later
loaded_model = joblib.load('iris_svm_model.pkl')

# Test the loaded model
loaded_y_pred = loaded_model.predict(X_test_scaled)
loaded_accuracy = accuracy_score(y_test, loaded_y_pred)
print(f"Accuracy of loaded model: {loaded_accuracy * 100:.2f}%")

from sklearn.metrics import confusion_matrix, classification_report

# Generate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Generate classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

import seaborn as sns
import matplotlib.pyplot as plt

# Visualize confusion matrix as a heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

from sklearn.decomposition import PCA

# Apply PCA to reduce dimensions to 2 for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Train the model on PCA-reduced data
X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.3, random_state=42)
best_model.fit(X_train_pca, y_train)

# Plot decision boundaries
xx, yy = np.meshgrid(np.linspace(X_pca[:, 0].min(), X_pca[:, 0].max(), 100),
                     np.linspace(X_pca[:, 1].min(), X_pca[:, 1].max(), 100))

Z = best_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.75)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, edgecolors='k', marker='o', cmap='coolwarm')
plt.title('SVM Decision Boundaries (PCA-reduced data)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
