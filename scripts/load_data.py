import pandas as pd

# Load data
df = pd.read_csv("data/United Nations Refugee Data.csv")

# Clean "-" and convert relevant columns to numeric
columns_to_clean = [
    'Other people in need of international protection',
    'Host Community'
]

for col in columns_to_clean:
    df[col] = df[col].replace("-", 0)
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Drop rows with "Unknown" country of origin (optional)
df = df[df["Country of origin"] != "Unknown"]

# Show cleaned data info
print("✅ Cleaned Data Info:")
print(df.info())

# Save cleaned version (optional for modeling)
df.to_csv("data/cleaned_refugee_data.csv", index=False)
print("\n🧼 Saved cleaned dataset to: data/cleaned_refugee_data.csv")
