import requests
from bs4 import BeautifulSoup
import openpyxl

class Shopping_Crawling():
    def __init__(self,pages:int):
        self.res =  requests.get("https://brand.naver.com/doctorbio/category/391baf8101bc4c6fb13f612381359250?st=POPULAR&free=false&subscr=false&dt=BIG_IMAGE&page=" + str(pages) + "&size=40")
        self.soup = BeautifulSoup(self.res.content,"html.parser")
        
    def get_main_name(self):
        self.items = self.soup.select('#CategoryProducts > ul > li > a >strong')
        
        return self.items
    
    def get_explain(self):
        self.items = self.soup.select('#CategoryProducts > ul > li > a >p')
        
        return self.items
    
    def get_price(self):
        self.items = self.soup.select('#CategoryProducts > ul > li > a > div.ZAfIG5c7RT > strong > span._1mMufyjSsw')
        
        return self.items
    def get_soup(self):
        
        return self.soup
    
class excel():
    def __init__(self,file_name:str):
        self.excel_file = openpyxl.Workbook()
        self.excel_sheet = self.excel_file.active
        self.file_name = file_name
        
        self.excel_sheet.column_dimensions['A'].width = 168
        self.excel_sheet.column_dimensions['B'].width = 10
        
        self.title = ["제품명","가격","설명"]
        
    def save(self):
        self.excel_sheet.append(self.title)
        self.excel_sheet.title = self.file_name
        #for x in range(1,3):
        self.product_lists = list()
        self.shop = Shopping_Crawling(1)
        
        self.main_name = self.shop.get_main_name()
        self.explain = self.shop.get_explain()
        self.price = self.shop.get_price()
            
        for idx,item in enumerate(self.main_name):
            self.product_lists.append([item.get_text(),self.price[idx].get_text()+"원",self.explain[idx].get_text()])
            
        for item in self.product_lists:
            self.excel_sheet.append(item)
            
        self.excel_file.save(self.file_name)
        self.excel_file.close()
            
            
if __name__ == '__main__':
    #출력 테스트 
    # Shop_page1 = Shopping_Crawling(1)
    
    # main_name = Shop_page1.get_main_name()
    # explain = Shop_page1.get_explain()
    # price = Shop_page1.get_price()
    # for item in main_name:
    #     print(item.get_text())
    # for item in explain:
    #     print(item.get_text())
    # for item in price:
    #     print(item.get_text())
    
    excel = excel("Shop.xlsx")
    excel.save()
    