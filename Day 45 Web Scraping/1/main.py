
from bs4 import BeautifulSoup
#import lxml

with open("Day 55 Web Scraping\\1\\website.html",encoding='cp437') as file:
    contents=file.read()
soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor_tag=soup.find_all("a")
print(all_anchor_tag)

for tag in all_anchor_tag:
    #print(tag.getText())
    print(tag.get("href"))
    
heading=soup.find_all(name="h1",id="name")
print(heading)

for tag in heading:
    print(tag.getText())


section_heading=soup.find_all(name="h3",class_="heading")
print(section_heading)

company_url=soup.select_one(selector="p a")
print(company_url)

name=soup.select_one(selector="#name")
print(name)

heading=soup.select(selector=".heading")
print(heading)