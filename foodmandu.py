import requests
from bs4 import BeautifulSoup


class FoodmandScrapper:
    def __init__(self):
        self.url = "https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId={restaurant_id}&show=" 

    def scrape_menu(self,restaurant_id):
        url = self.url.format(restaurant_id=restaurant_id)
        r = requests.get(url)
        all_menus=r.json()
        all_menus = all_menus[0] ['items']
        for menu in all_menus:
            print(["name:", menu['name'], menu['price']])
        return all_menus
    
s = FoodmandScrapper()
s.scrape_menu(1027)


