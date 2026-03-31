import requests
from bs4 import BeautifulSoup

#step 1 - Visit the website
url = "https://books.toscrape.com"
response = requests.get(url)

#step 2 - Read the page
soup = BeautifulSoup(response.text, "html.parser")

#step 3 - Find all books titles
books = soup.find_all("article", class_="product_pod")

print("Books found:", len(books))
print("---")

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(title, "->", price)

import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Book Title"
sheet["B1"] = "Price"

row = 2
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    sheet["A" +str(row)] = title
    sheet["B" +str(row)] = price
    row = row + 1

workbook.save("c:/Users/SK MUJEEB/Desktop/books.xlsx")
print("Saved to Excel!")


 