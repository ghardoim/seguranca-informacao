from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
soup = BeautifulSoup(site, "html.parser")
# print(soup.prettify())
link = soup.find("a", class_="link actTriggerGA")

print(link.string)
print(soup.title.string)
print(soup.p.string)
