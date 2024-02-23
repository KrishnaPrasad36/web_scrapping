import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
import pandas as pd
soup=BeautifulSoup(r.text,'lxml')
names=soup.find_all('a', class_='title')
#print(names)
product_name=[]
for i in names:
    name=i.text
    product_name.append(name)
#print(product_name)  

prices=soup.find_all('h4', class_='pull-right price')
product_prices=[]
for i in prices:
    price=i.text
    product_prices.append(price)
#print(product_prices)

description=soup.find_all('p', class_='description')
product_desc=[]
for i in description:
    descs=i.text
    product_desc.append(descs)
#print(product_desc)

reviews=soup.find_all('p', class_="pull-right")
reviews_list=[]
for i in reviews:
    review=i.text
    reviews_list.append(review)
#print(reviews_list)    

#creating dataframe
df=pd.DataFrame({'product_name':product_name,'price':product_prices,'Description':product_desc,'review':reviews_list})
print(df)
#storing dataframe in tbhe form of excel
df.to_excel('product_detail.xlsx')
