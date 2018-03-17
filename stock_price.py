from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=ITD&ssoPageId=10&selectPage=2'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = bs(page_html, "html.parser")

price = page_soup.findAll("div",{"class":"col-xs-6 col-xs-offset-6 colorRed"})
date = page_soup.findAll("span",{"class":"stt-remark"})
#print(page_soup.h1)

text_price = price[0].text
date_text = date[0].text

# Print Result
print("Current Price of ITD: {} Bath".format(text_price))
print("Current Date, Time: {}".format(date_text))
