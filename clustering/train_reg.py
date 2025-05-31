import json
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    median_absolute_error,
    explained_variance_score,
)
import joblib
import time
import os
import sys

with open("./labelled/chunk_clusters_labeled_tedex.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Data loaded, preparing for embeddings and labels...")
X = np.array([d["embedding"] for d in data])
y = np.array([d["progress"] for d in data])

print(f"Total samples: {len(X)}")

print("Splitting dataset into train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")

# param_grid = {
#     "n_estimators": [100, 200],
#     "max_depth": [None, 20, 40],
#     "min_samples_split": [2, 5],
#     # "max_features": [None, "sqrt", "log2"],
#     "max_features": [None, "log2"],
# }
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 20, 40],
    "min_samples_split": [2, 5],
    # "max_features": [None, "sqrt", "log2"],
    "max_features": ["log2"],
}

# param_grid = {
#     "n_estimators": [100],
#     "max_depth": [None],
#     "min_samples_split": [2],
#     "max_features": ["sqrt"],
# }


print("Setting up GridSearchCV...")
grid = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    scoring="neg_mean_absolute_error",
    cv=3,
    verbose=2,
    n_jobs=-1,
    error_score="raise",
)

print("Starting grid search...")
start_time = time.time()
try:
    grid.fit(X_train, y_train)
except Exception as e:
    print(f"❌ GridSearchCV failed: {e}")
    sys.exit

print(f"GridSearchCV completed in {time.time() - start_time:.2f} seconds")
# reg = RandomForestRegressor(n_estimators=100, random_state=42)
# reg.fit(X_train, y_train)

print("Best Params found:")
print("Best Params:", grid.best_params_)
reg = grid.best_estimator_

print("Prediction on test set...")
y_pred = reg.predict(X_test)

print("Evaluating model...")
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
medae = median_absolute_error(y_test, y_pred)
evs = explained_variance_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R^2 Score: {r2}")
print(f"Median Absolute Error: {medae}")
print(f"Explained Variance Score: {evs}")

print("Saving model...")
joblib.dump(reg, "./models/speech_progress_regressor_tedex.pkl")
print("Model saved to ./models/speech_progress_regressor_tedex.pkl")
