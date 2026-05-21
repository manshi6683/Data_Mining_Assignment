# Web Scraping + DataFrame Operations in Python

# Install required libraries first:
# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Open-source website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all book data
books = soup.find_all("article", class_="product_pod")

# Create empty lists
book_name = []
price = []
rating = []

# Extract data
for book in books:
    
    # Book title
    title = book.h3.a["title"]
    book_name.append(title)
    
    # Price
    price_text = book.find("p", class_="price_color").text
    price_value = float(price_text.replace("£", "").replace("Â", ""))
    price.append(price_value)
    
    # Rating
    rating_text = book.find("p")["class"][1]
    
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    
    rating.append(rating_map[rating_text])

# Convert into DataFrame
df = pd.DataFrame({
    "Book Name": book_name,
    "Price": price,
    "Rating": rating
})

# Display DataFrame
print("\nComplete DataFrame:\n")
print(df)

# ---------------------------------------------------
# HEAD FUNCTION
# ---------------------------------------------------
print("\nFirst 5 Rows using head():\n")
print(df.head())

# ---------------------------------------------------
# MEAN OF SPECIFIC COLUMN
# ---------------------------------------------------
mean_price = df["Price"].mean()

print("\nMean Price of Books:\n")
print(mean_price)

# ---------------------------------------------------
# SORTING DATA ASCENDING
# ---------------------------------------------------
ascending_sort = df.sort_values(by="Price")

print("\nBooks Sorted by Price (Ascending):\n")
print(ascending_sort)

# ---------------------------------------------------
# SORTING DATA DESCENDING
# ---------------------------------------------------
descending_sort = df.sort_values(by="Price", ascending=False)

print("\nBooks Sorted by Price (Descending):\n")
print(descending_sort)

# ---------------------------------------------------
# STANDARD DEVIATION
# ---------------------------------------------------
std_price = df["Price"].std()

print("\nStandard Deviation of Price:\n")
print(std_price)