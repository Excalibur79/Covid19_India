import requests
import pandas
from bs4 import BeautifulSoup
r=requests.get("https://www.mygov.in/covid-19")
c=r.content
soup=BeautifulSoup(c,'html.parser')
all=soup.find_all("div",{"class":"marquee_data view-content"})
l=[]
for i in range(37):
    d={}
    d["State"]=all[0].find_all("span",{"class":"st_name"})[i].text
    d["Confirmed_cases"]=all[0].find_all("div",{"class":"tick-confirmed"})[i].find("small").text
    d["Active_cases"]=all[0].find_all("div",{"class":"tick-active"})[i].find("small").text
    d["Recovered_cases"]=all[0].find_all("div",{"class":"tick-discharged"})[i].find("small").text
    d["Deaths"]=all[0].find_all("div",{"class":"tick-death"})[i].find("small").text
    l.append(d)
df=pandas.DataFrame(l)
print(df.set_index("State"))