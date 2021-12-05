from bs4 import BeautifulSoup
import requests
import urllib

arg_url = r"file:///C:/Users/suman.pandey/Desktop/work_2021/LLTC_review/TesikoHtml.htm"
client = urllib.request.urlopen(arg_url)

res = requests.get('https://www.w3schools.com/w3css/w3css_web.asp')
soup = BeautifulSoup(res, 'html.parser')
print('----------------------------------------------------------------------------------------')
link = soup.find('div')
print(link)