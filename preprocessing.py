import pandas as pd

# Load dataset
df = pd.read_csv("dataset/raw_data/water_potability.csv")

print(df.info())
print(df.isnull().sum())

# Fill missing values
df.fillna(df.mean(), inplace=True)

# Save processed file
df.to_csv("dataset/processed_data/processed_water_data.csv", index=False)

print("Preprocessing Done")