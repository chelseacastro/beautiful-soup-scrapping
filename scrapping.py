import pandas as pd

# crawling html page
import requests

# scrapping and parsing from obtained html page
from bs4 import BeautifulSoup

# crawling
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
page = requests.get(url)
# print("Crawling Result")
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

# scrapping
# result = soup.find("title")
# print("Scrapping Result")
# print(result.text)

# scrapping table
table = soup.find("table",class_="wikitable")
tbody = table.find("tbody")
trows = tbody.find_all('tr')

# print("Scrapping Table Result")
# print(trow)

country = []
region = []
estimate = []
year = []

for trow in range(3, len(trows)):
    country.append(trows[trow].find_all("td")[0].text.replace("\xa0",""))
    region.append(trows[trow].find_all("td")[1].text)
    estimate.append(trows[trow].find_all("td")[2].text)
    year.append(trows[trow].find_all("td")[3].text)

df = pd.DataFrame()

df['Country'] = country
df['Region'] = region
df['Estimate'] = estimate
df['Year'] = year

print(df)