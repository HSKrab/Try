# https://www.learncodewithmike.com/2020/08/python-scraper-integrate-with-mysql.html
from bs4 import BeautifulSoup
import requests


class Stock:
    # 建構式
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers

    # 爬取
    def scrape(self):

        result = list()  # 最終結果

        for stock_number in self.stock_numbers:

            response = requests.get(
                "https://tw.stock.yahoo.com/q/q?s=" + stock_number)
            soup = BeautifulSoup(response.text.replace("加到投資組合", ""), "lxml")

            stock_date = soup.find(
                "font", {"class": "tt"}).getText().strip()[-9:]  # 資料日期

            tables = soup.find_all("table")[2]  # 取得網頁中第三個表格(索引從0開始計算)
            tds = tables.find_all("td")[0:11]  # 取得表格中1到10格

            result.append((stock_date,) +
                          tuple(td.getText().strip() for td in tds))

        return result


stock = Stock('2451', '2454')  # 建立Stock物件
print(stock.scrape())  # 印出爬取結果
