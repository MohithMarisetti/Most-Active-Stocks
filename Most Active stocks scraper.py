import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
import os


if os.path.exists("stocks.csv"):
    os.remove("stocks.csv")
if os.path.exists("StocksDatabase.db"):
    os.remove("StocksDatabase.db")

activeStocksURL = "https://money.cnn.com/data/hotstocks/"

page = requests.get(activeStocksURL)

soup = BeautifulSoup(page.content, 'html.parser')

conn = sqlite3.connect("StocksDatabase.db")

c = conn.cursor()

c.execute('CREATE TABLE StocksTable (Ticker TEXT, OpenPrice REAL, PrevClose REAL,Volume INTEGER)');

MOST_ACTIVES = soup.find('table')


quotesURL = "https://finance.yahoo.com/quote/"

table_class = "W(100%)"

collectibles = ['Previous Close','Open','Volume']


with open('stocks.csv', mode='w', newline='') as stocks_file:
    stocks_writer = csv.writer(stocks_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    stocks_writer.writerow(["Company", "Symbol", "Previous close", "Open", "Volume"])

    for each_td in MOST_ACTIVES.find_all('td'):
        symbol = each_td.find('a')
        if (symbol):
            span = each_td.find('span')
            counter = 0
            page = requests.get(quotesURL + symbol.get_text())
            soup_obj = BeautifulSoup(page.content , 'html.parser')
            
            prev_close = 0
            open_val = 0
            volume = 0
            prev_val = ''
            table = soup_obj.find('table', class_ = table_class)
            
            for val in table.find_all('td'):
                
                if(prev_val in collectibles):
                    if prev_val == 'Previous Close':
                        prev_close = val.get_text()
                        
                    elif prev_val == 'Open':
                        open_val = val.get_text()
                        
                    elif prev_val == 'Volume':
                        volume = val.get_text()
                        
                prev_val = val.get_text()
                
                        
                

            stocks_writer.writerow([span.get_text(), symbol.get_text(), prev_close, open_val, volume])
            c.execute('INSERT INTO StocksTable (Ticker, PrevClose, OpenPrice, Volume) VALUES(?,?,?,?)', 
                      (symbol.get_text(), prev_close, open_val, volume))
            conn.commit()

c.close()
conn.close()
            
        
        