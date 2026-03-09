import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [95, 92, 76, 88, 67],
    "Passed": [True, True, False, True, False],
    "Category": ["A", "A", "B", "B", "A"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df, "\n")

print("Single column - Name:")
print(df["Name"], "\n")

print("Multiple columns - Name and Score:")
df_subset = df[["Name", "Score"]]
print(df_subset, "\n")

print("First three rows using iloc:")
print(df.iloc[:3], "\n")

df_indexed = df.set_index("Name")
print("DataFrame with Name as index:")
print(df_indexed.loc[["Alice", "David"]], "\n")

print("Rows where Score > 85:")
print(df[df["Score"] > 85], "\n")

print("Rows where Score > 85 and Passed is True:")
print(df[(df["Score"] > 85) & (df["Passed"] == True)], "\n")

filtered_sorted = df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False)
print("Filtered and sorted (Score > 85 and Passed=True):")
print(filtered_sorted, "\n")

print("Chained operation: High-performing students (Score > 85 and Passed=True, sorted):")
print(df.query("Score > 85 and Passed == True").sort_values("Score", ascending=False)[["Name", "Score"]])
