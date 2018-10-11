# lesson 2 exercice
# lesson 2 test

from bs4 import BeautifulSoup
import numpy as np
import urllib
data = []
#ticker =['LVMH.PA','AIR.PA','DANO.PA']
#for i in range (len(ticker)):
    #link = 'https://www.reuters.com/finance/stocks/financial-highlights/'+ticker[i]
link = 'https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA'
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
    
    #name_box1 = soup.find(class_= )
    #name_box2 = soup.find(class_='valueContent')
    #print(soup.h1.prettify)
#name_box = soup.find('h1', class_='name')
    #price_box = soup.find('div', class_='price')
 # strip() is used to remove starting and trailing
price =[]
sales_est = []
Dividend_yield_ind = []
Dividend_yield_corp = []
shareholder_ownership = []
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='dataTable')
right_table


