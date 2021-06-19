import requests
import pandas as pd

# page = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India")
# # print(page.content)
r = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
# print(r)
print(r.columns.values)
# p=pd.print(r.columns.values)(r'C:\Users\Win_10\Desktop\python projects\country_vaccinations.csv')
# print(p)