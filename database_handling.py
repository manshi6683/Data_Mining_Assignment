# DATABASE HANDLING USING PANDAS
# Create two databases and perform merging

# Install required libraries first:
# pip install pandas numpy

import pandas as pd
import numpy as np

# ---------------------------------------------------
# CREATE FIRST DATABASE
# 100 Rows and 15 Columns
# ---------------------------------------------------

np.random.seed(10)

db1 = pd.DataFrame({
    "Emp_ID": range(1, 101),
    "Name": [f"Employee_{i}" for i in range(1, 101)],
    "Age": np.random.randint(21, 60, 100),
    "Salary": np.random.randint(25000, 90000, 100),
    "Department_ID": np.random.randint(1, 11, 100),
    "Project_ID": np.random.randint(100, 120, 100),
    "Experience": np.random.randint(1, 20, 100),
    "City": np.random.choice(["Delhi", "Mumbai", "Jaipur", "Pune"], 100),
    "Bonus": np.random.randint(2000, 10000, 100),
    "Performance_Score": np.random.randint(1, 6, 100),
    "Manager_ID": np.random.randint(1, 20, 100),
    "Attendance": np.random.randint(70, 100, 100),
    "Gender": np.random.choice(["Male", "Female"], 100),
    "Shift": np.random.choice(["Day", "Night"], 100),
    "Tax": np.random.randint(1000, 5000, 100)
})

print("\nFIRST DATABASE (15 Columns):\n")
print(db1.head())

# ---------------------------------------------------
# CREATE SECOND DATABASE
# 100 Rows and 12 Columns
# ---------------------------------------------------

db2 = pd.DataFrame({
    "Department_ID": np.random.randint(1, 11, 100),
    "Project_ID": np.random.randint(100, 120, 100),
    "Department_Name": np.random.choice(
        ["HR", "IT", "Finance", "Sales", "Marketing"], 100),
    "Project_Name": np.random.choice(
        ["Project_A", "Project_B", "Project_C"], 100),
    "Client_Name": np.random.choice(
        ["Client_X", "Client_Y", "Client_Z"], 100),
    "Budget": np.random.randint(100000, 500000, 100),
    "Deadline_Months": np.random.randint(1, 24, 100),
    "Team_Size": np.random.randint(5, 30, 100),
    "Location": np.random.choice(
        ["Delhi", "Mumbai", "Bangalore"], 100),
    "Project_Status": np.random.choice(
        ["Running", "Completed", "Pending"], 100),
    "Technology": np.random.choice(
        ["Python", "Java", "AI", "Cloud"], 100),
    "Rating": np.random.randint(1, 6, 100)
})

print("\nSECOND DATABASE (12 Columns):\n")
print(db2.head())

# ---------------------------------------------------
# FOREIGN KEY IDENTIFICATION
# ---------------------------------------------------

print("\nFOREIGN KEY:")
print("Department_ID")

print("\nSECONDARY FOREIGN KEY:")
print("Project_ID")

# Explanation:
# Department_ID and Project_ID are common columns
# between both databases and can be used for merging.

# ---------------------------------------------------
# DATABASE MERGING USING PANDAS
# ---------------------------------------------------

merged_db = pd.merge(
    db1,
    db2,
    on=["Department_ID", "Project_ID"],
    how="inner"
)

print("\nMERGED DATABASE:\n")
print(merged_db.head())

# ---------------------------------------------------
# INFORMATION ABOUT MERGED DATABASE
# ---------------------------------------------------

print("\nMerged Database Shape:")
print(merged_db.shape)

print("\nMerged Database Columns:")
print(merged_db.columns)

# ---------------------------------------------------
# SAMPLE OPERATIONS
# ---------------------------------------------------

# Mean Salary
print("\nAverage Salary:")
print(merged_db["Salary"].mean())

# Standard Deviation of Salary
print("\nSalary Standard Deviation:")
print(merged_db["Salary"].std())

# Sort by Salary Descending
print("\nSorted by Salary (Descending):")
print(merged_db.sort_values(by="Salary", ascending=False).head())

# Top 5 Employees
print("\nTop 5 Rows:")
print(merged_db.head())