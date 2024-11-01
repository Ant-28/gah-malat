import requests
from bs4 import BeautifulSoup as bs


# dt#text
url = "https://en.uesp.net/wiki/Lore:Dark_Elvish"

r = requests.get(url)

soup = bs(r.content, 'html.parser')


for sup in soup.find_all("sup"):
    sup.decompose()
for dd in soup.find_all("dd"):
    dd.decompose()

words = soup.select("tr td dl dt")

with open("data.txt", "w", encoding="utf-8") as outfile:
    for word in words:
        outfile.write(bs.get_text(word) + "\n")

