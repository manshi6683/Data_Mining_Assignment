# API Handling in Python
# Create object of specific columns and make DataFrame

# Install required libraries first:
# pip install requests pandas

import requests
import pandas as pd

# API URL (Open Source API)
url = "https://jsonplaceholder.typicode.com/users"

# Get API response
response = requests.get(url)

# Convert JSON data into Python object
data = response.json()

# Display complete data
print("\nComplete API Data:\n")
print(data)

# ---------------------------------------------------
# CREATE OBJECT OF SPECIFIC COLUMNS
# ---------------------------------------------------

# Create empty list
user_list = []

# Extract only required columns
for user in data:
    
    obj = {
        "ID": user["id"],
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"]
    }
    
    user_list.append(obj)

# ---------------------------------------------------
# CONVERT OBJECT INTO DATAFRAME
# ---------------------------------------------------

df = pd.DataFrame(user_list)

# Display DataFrame
print("\nDataFrame with Specific Columns:\n")
print(df)

# ---------------------------------------------------
# DATAFRAME OPERATIONS
# ---------------------------------------------------

# Head Function
print("\nFirst 5 Rows:\n")
print(df.head())

# Print Column Names
print("\nColumn Names:\n")
print(df.columns)

# Sorting by Name
print("\nSorted by Name:\n")
print(df.sort_values(by="Name"))

# Total number of records
print("\nTotal Records:")
print(len(df))