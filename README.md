The CNN Money’s Market Movers website (https://money.cnn.com/data/hotstocks/ )
tracks the most active stocks on a real time basis. You will first write Python scripts that collect the
list of Most Actives tickers only from the above website. Next, your programs should take the ticker
symbols and names of these companies (and categories) and build a csv file (called stocks.csv) with
data about each stock from the website:
https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch-v1 which gives the quote for
ticker symbol AMD as an example. The data to be collected from the Yahoo Finance site should
include:
OPEN price
PREV CLOSE price
VOLUME
In addition to the stocks.csv file, the data should also be stored in a SQLite database called
StocksDatabase in the directory that your Jupyter Notebook code will be executed from. The
StocksDatabase should have a table called StocksTable that contains the following columns and
types:
Ticker TEXT
OpenPrice REAL
PrevClose REAL
Volume INTEGER
Every execution of your program should create a stocks.csv and StocksDatabase.db file in the
directory (delete any existing files that you will create) that your Python script is located and run.
We will be testing your output by verifying the following:
1. The program gets the list of Most Actives ticker symbols from the
https://money.cnn.com/data/hotstocks/ website and uses it to create the stocks.csv and SQLite
database
2. Verify that the stocks.csv file is created with the Most Active ticker symbols and the data
obtained from https://finance.yahoo.com/quote website in the csv format.
3. Verify that the StocksDatabase.db file is created and that the SQLite database contains the
StocksTable with the appropriate columns and is populated with the data. SQLite Browser may
be used to verify database content.
