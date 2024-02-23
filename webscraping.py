import requests

url='https://www.wscubetech.com/'
r=requests.get(url)
print(r.status_code)#give status code
print(r.text) #give all the html tag
