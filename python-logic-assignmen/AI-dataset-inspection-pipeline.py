import pandas as pd

csv_filename = "sample_dataset.csv"

df = pd.read_csv(csv_filename)

print("First 5 rows:")
print(df.head(), "\n")

print("Last 5 rows:")
print(df.tail(), "\n")

print("Dataset Info:")
print(df.info(), "\n")

print("Summary Statistics:")
print(df.describe(), "\n")

ages = df["Age"]
print("Selected Column (Age):")
print(ages, "\n")

subset_df = df[["Name", "Score"]]
print("Selected Multiple Columns (Name & Score):")
print(subset_df, "\n")

filtered_rows = df[df["Score"] > 80]
print("Filtered Rows (Score > 80):")
print(filtered_rows, "\n")
