import requests
from bs4 import BeautifulSoup
import re
url = "https://www.ptt.cc/bbs/Notebook/index.html"
resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)
tag = soup.find_all('div', re.compile('title'))
# print(tag)
for t in tag:
    print(t.text.strip())
