import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/processed_data/processed_water_data.csv")

# pH Distribution
plt.figure()
sns.histplot(df['ph'], kde=True)
plt.title("pH Distribution")
plt.savefig("outputs/graphs/ph_distribution.png")

# Turbidity vs Potability
plt.figure()
sns.boxplot(x='Potability', y='Turbidity', data=df)
plt.title("Turbidity vs Water Quality")
plt.savefig("outputs/graphs/turbidity_boxplot.png")

# Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("outputs/graphs/heatmap.png")

# Countplot
plt.figure()
sns.countplot(x='Potability', data=df)
plt.title("Water Quality Count")
plt.savefig("outputs/graphs/countplot.png")

print("Graphs saved successfully")
