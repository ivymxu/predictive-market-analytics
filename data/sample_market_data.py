# sample dataset and visualization for testing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# sample dataset
np.random.seed(50)
n_samples = 200
data = {
    'feature1': np.random.normal(50, 10, n_samples),
    'feature2': np.random.normal(30, 5, n_samples),
    'feature3': np.random.normal(100, 20, n_samples),
    'target': np.random.choice([0, 1], size=n_samples),
}

df = pd.DataFrame(data)
df.to_csv("predictive-market-analytics/data/market_data.csv", index=False)

# sample visualization
plt.figure(figsize=(8, 6))
plt.scatter(df['feature1'], df['feature2'], c=df['target'], cmap='bwr', alpha=0.7)
plt.title("Feature1 vs Feature2 Colored by Target")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.grid(True)
plt.savefig("predictive-market-analytics/visualizations/feature_scatter.png")
plt.close()
