# Copyright (C) 2024 Yako
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from ansiscraper.shemas.ScraperProviderShema import ScraperProviderShema
import requests as rq
import json
from bs4 import BeautifulSoup as bs
import re
from ansiscraper.utils.utils import formatNumbersToMoney
class JetstereoProvider(ScraperProviderShema):
    __urlNormal = "https://www.jetstereo.com"
    __urlApi = "https://api.jetstereo.com"
    __urlNormalConfigProductListByCategory = "viewMode=list&perPage=20&currentPage=1"
    __urlApiConfigProductListByCategory = "viewMode=list&expand=description%2Cgifts"

    #categories/26/products?viewMode=list&per-page=10&page=1&expand=description%2Cgifts
    #https://www.jetstereo.com/category/smartphones?viewMode=list&perPage=20&currentPage=1

    def getProductListByCategory(self, productCategory, page = 1, perPage = 20):
        full_url = f"{self.__urlApi}/categories/{productCategory}/products?{self.__urlApiConfigProductListByCategory}&page={page}&per-page={perPage}"
        
        nearestNumber = self.__nearestNumber(self.__getCategoryList(), productCategory)
        
        if productCategory not in self.__getCategoryList():
            print(f"Category {productCategory} not available. Try with {nearestNumber}")

        try:
            r = rq.get(full_url)
            json_object = json.loads(r.text)
            lastPage = self.__getLastPage(json_object.get('_links').get('last').get('href'))

            if(page > lastPage):
                print(f"Page {page} not available \nLast page is {lastPage}")
                return None                 
            
            #formatted = json.dumps(json_object["content"], indent = 2)
            data = []

            for item in json_object["content"]:
                id = item.get("id")
                model = item.get("model")
                name = item.get("name")
                price = {
                    "sale": formatNumbersToMoney(item.get("price").get("sale")),
                    "regular": formatNumbersToMoney(item.get("price").get("sale"))
                }
                url = item.get('url')
                data.append({
                    "id": id,
                    "model": model,
                    "name": name,
                    "price": price,
                    "url": url
                })
        except Exception as e:
            print(f"Failed to resolve {full_url}, name or service not available.")
            print(e)
            return None

        return data
    
    def __getCategoryList(self):
        jsonFile = open('./ansiscraper/providers/jetstereo/data.json')

        data = json.load(jsonFile)
        categoriesId = [i.get("id") for i in data["categories"]]

        return categoriesId
        jsonFile.close()

    def __getLastPage(self, url):
        patternPage = r'page=(\d+)'
        lastPage = re.findall(patternPage, url)

        return int(lastPage[0])

    def __nearestNumber(self, arrayNumbers, number):
        return min(arrayNumbers, key=lambda x: abs(x - number))





        
        
        

    

