import os
from nbformat import v4 as nbf

os.makedirs("analysis/", exist_ok=True)

nb = nbf.new_notebook()

nb.cells = [
    nbf.new_markdown_cell("# Exploratory Data Analysis\nThis notebook provides an overview of the dataset and initial insights."),
    nbf.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../data/market_data.csv')
df.head()"""),
    nbf.new_markdown_cell("## Summary Statistics"),
    nbf.new_code_cell("df.describe()"),
    nbf.new_markdown_cell("## Correlation Matrix"),
    nbf.new_code_cell("""plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()"""),
    nbf.new_markdown_cell("## Distribution of Features"),
    nbf.new_code_cell("""df.hist(figsize=(10, 8), bins=20)
plt.tight_layout()
plt.show()""")
]