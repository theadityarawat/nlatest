import requests
from bs4 import BeautifulSoup
import pandas as pd
url ="https://uktenders.gov.in/nicgep/app"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")

huee=soup.find(id="activeTenders")

web_links = huee.select('a') 
actual_web_links = [web_link['href'] for web_link in web_links]
for i in range(len(actual_web_links)):
    j=actual_web_links[i]
    actual_web_links[i]="https://uktenders.gov.in"
    actual_web_links[i]+=j
final=[]
temp=[]
p=0
for i in range(len(actual_web_links)):
    if(i%4==0 and i!=0):
        res={
            'NAME':temp[i-4],
            'REF NO':temp[i-3],
            'CLOSING DATE':temp[i-2],
            'BID OPENING DATE':temp[i-1],
            'LINK':actual_web_links[p]
        }
        p+=1
        final.append(res)
    j=huee.find_all('td')[i].text
    temp.append(j)
res={
            'NAME':temp[i-3],
            'REF NO':temp[i-2],
            'CLOSING DATE':temp[i-4],
            'BID OPENING DATE':temp[i-1],
            'LINK':actual_web_links[p]
        }

final.append(res)
print(final)
df=pd.DataFrame(final)
print(df.tail)
df.to_csv('C:/Users/adity/Desktop/Data/nlatest/Uttarakhand.csv')