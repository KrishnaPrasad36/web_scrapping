import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)


#soup= BeautifulSoup(r.text,'lxml') #getting html tag
#tag=soup.header
#attr=tag.attrs
#print(attr['role'])
#tag=soup.header.div.a.button.span
#print(tag.string)# to get string from the tag
#print(soup.find('div'))#(to find the tag using find() function)
#price=soup.find(('h4',{'class':'pull-right price'}))
#print(price.string)
#find function only find first tag
#descr=soup.find('p',class_='description')  #finding tag with class name
#prices=soup.find_all('h4',class_="pull-right price")
#print(prices[2].text)
#for i in prices:
 #   print(i.string)
 #using regular expression
import re
#data= soup.find_all(string='Galaxy Tab 3')
#data= soup.find_all(string=re.compile('Galaxy'))#getting data with the help of regular expression
#print(data)
#working with pandas
'''import pandas as pd
soup=BeautifulSoup(r.text,'lxml')
names=soup.find_all('a', class_='title')
#print(names)
product_name=[]
for i in names:
    name=i.text
    product_name.append(name)
print(product_name)  

prices=soup.find_all('h4', class_='pull-right price')
product_prices=[]
for i in prices:
    price=i.text
    product_prices.append(price)
print(product_prices)

description=soup.find_all('p', class_='description')
product_desc=[]
for i in description:
    descs=i.text
    product_desc.append(descs)
print(product_desc)

reviews=soup.find_all('p', class_="pull-right")
reviews_list=[]
for i in reviews:
    review=i.text
    reviews_list.append(review)
print(reviews_list)    

#creating dataframe
df=pd.DataFrame({'product_name':product_name,'price':product_prices,'Description':product_desc,'review':reviews_list})
print(df)

df.to_csv('product_detail.csv')'''

soup=BeautifulSoup(r.text,'lxml')
boxes=soup.find_all('div',class_="col-sm-4 col-lg-4 col-md-4")

#print(len(boxes))
#getting the value of any boxes
box=soup.find('div',class_="col-sm-4 col-lg-4 col-md-4")[3]
print(box)
