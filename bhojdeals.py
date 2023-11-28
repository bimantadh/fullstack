import requests
from bs4 import BeautifulSoup

# class FantechScrapper:
#     def __init__(self):
#         self.url = "https://www.bhojdeals.com/deal/361"

#     def scrape_bhoj(self):
        
url = "https://merolagani.com/StockQuote.aspx"
r =requests.get(url)
source_code=r.text

soup= BeautifulSoup(source_code)

listing_div = soup.find_all("div",{
                            "class": "table-responsive"})

for listing in listing_div:
    print(listing.text.strip())