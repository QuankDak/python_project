import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://danggn.com/hot_articles.com")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup)