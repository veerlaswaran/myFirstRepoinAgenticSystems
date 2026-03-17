import pandas as pd
import numpy as np

#  Step 1: Create sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, None, 700000,
        520000, None, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print(" Original DataFrame:\n", df)

#  Step 2: Detect missing values
print("\n Missing Values:\n", df.isnull().sum())

#  Step 3: Fill missing Salary values with mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

#  Step 4: Drop Temporary_Notes column
df.drop(columns=["Temporary_Notes"], inplace=True)

#  Step 5: Rename Salary to Annual_Salary
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\n Cleaned DataFrame:\n", df)

#  Step 6: Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
).reset_index()

print("\n Final Summary Table:\n", summary)
