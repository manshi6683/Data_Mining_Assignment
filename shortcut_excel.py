# COMBINED EXCEL / GOOGLE SHEETS OPERATIONS USING PYTHON
# Includes:
# 1. Create Excel File
# 2. Read Excel File
# 3. VLOOKUP Operation
# 4. Filter Function
# 5. Sorting
# 6. File Operations
# 7. Google Sheets Style Manipulation using Pandas

# Install required libraries first:
# pip install pandas openpyxl

import pandas as pd

# ---------------------------------------------------
# CREATE SAMPLE DATAFRAME
# ---------------------------------------------------

data = {
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Aman", "Neha", "Priya", "Karan"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Salary": [50000, 60000, 45000, 70000, 55000],
    "Experience": [2, 5, 3, 7, 4]
}

df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME:\n")
print(df)

# ---------------------------------------------------
# FILE OPERATION : SAVE TO EXCEL
# ---------------------------------------------------

excel_file = "employee_data.xlsx"

df.to_excel(excel_file, index=False)

print("\nExcel File Created Successfully!")

# ---------------------------------------------------
# READ EXCEL FILE
# ---------------------------------------------------

read_df = pd.read_excel(excel_file)

print("\nREAD DATA FROM EXCEL FILE:\n")
print(read_df)

# ---------------------------------------------------
# VLOOKUP OPERATION
# ---------------------------------------------------
# Find Salary of Employee ID = 103

lookup_id = 103

vlookup_result = read_df.loc[
    read_df["Emp_ID"] == lookup_id,
    ["Name", "Salary"]
]

print("\nVLOOKUP RESULT:\n")
print(vlookup_result)

# ---------------------------------------------------
# FILTER FUNCTION
# ---------------------------------------------------
# Filter employees with Salary > 55000

filtered_df = read_df[read_df["Salary"] > 55000]

print("\nFILTERED DATA (Salary > 55000):\n")
print(filtered_df)

# ---------------------------------------------------
# SORTING ASCENDING
# ---------------------------------------------------

ascending_sort = read_df.sort_values(by="Salary")

print("\nSORTED BY SALARY (ASCENDING):\n")
print(ascending_sort)

# ---------------------------------------------------
# SORTING DESCENDING
# ---------------------------------------------------

descending_sort = read_df.sort_values(
    by="Salary",
    ascending=False
)

print("\nSORTED BY SALARY (DESCENDING):\n")
print(descending_sort)

# ---------------------------------------------------
# SELECT SPECIFIC COLUMNS
# ---------------------------------------------------

specific_columns = read_df[["Name", "Salary"]]

print("\nSPECIFIC COLUMNS:\n")
print(specific_columns)

# ---------------------------------------------------
# DATAFRAME HEAD
# ---------------------------------------------------

print("\nFIRST 5 ROWS:\n")
print(read_df.head())

# ---------------------------------------------------
# MEAN OF SALARY
# ---------------------------------------------------

mean_salary = read_df["Salary"].mean()

print("\nMEAN SALARY:\n")
print(mean_salary)

# ---------------------------------------------------
# STANDARD DEVIATION
# ---------------------------------------------------

std_salary = read_df["Salary"].std()

print("\nSTANDARD DEVIATION OF SALARY:\n")
print(std_salary)

# ---------------------------------------------------
# SAVE FILTERED DATA INTO NEW EXCEL FILE
# ---------------------------------------------------

filtered_df.to_excel(
    "filtered_employee_data.xlsx",
    index=False
)

print("\nFiltered Excel File Saved Successfully!")

# ---------------------------------------------------
# GOOGLE SHEETS STYLE OPERATIONS
# ---------------------------------------------------
# (Using pandas similar to Google Sheets)

# Add new column
read_df["Bonus"] = read_df["Salary"] * 0.10

print("\nDATAFRAME WITH BONUS COLUMN:\n")
print(read_df)

# ---------------------------------------------------
# FINAL SAVE
# ---------------------------------------------------

read_df.to_excel(
    "final_employee_data.xlsx",
    index=False
)

print("\nFinal Excel File Saved Successfully!")