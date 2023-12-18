import requests
from bs4 import BeautifulSoup
import pandas as pd
url ="https://etender.up.nic.in/nicgep/app?page=FrontEndTendersByOrganisation&service=page"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")
# print(htmlContent)
# print(soup)
# title=soup.title
# print(type(soup))
# print(type(title))
# print(type(title.string))

# anchors=soup.find_all('a')
# print(anchors)

# paras=soup.find_all('p')
# print(paras)

# print(soup.find('p')) #get first element using find
# print(soup.find('p')['class']) #get class(s) of any element

#find all elements with class lead
# print(soup.find_all("p", class_="text-sm"))

#get text from the tags/soup
# print(soup.find('p').get_text)

# anchors=soup.find_all('a')
# all_links=set()
# # get all links on page:
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkt= "https://codewithharry.com" + link.get('href')
#         all_links.add(linkt)
#         print(linkt)

#comment
# markup = "<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(type((soup2.p.string)))

# table_list=[]
# tender_title=[]
# ref_no=[]
# closing_date=[]
# bid_opening_date=[]
# link=[]
# huee=soup.find(id='activeTenders')
# # print(huee)
# for item in huee.strings:
#     tender=item.find('td', class_='link2').text 
#     refff=item.find(width_="20%").text

#     active ={
#         'Tender_Title':tender,
#         'Ref_No':refff
#         # 'Closing_date'
#         # 'Bid_Opening_Date'
#         # 'Link'
#     }
#     table_list.append(active)
#     # print(item)
# print(table_list)
# listt=[]
huee=soup.find(id="table")
# for item in huee.strings:
#     n=huee.find_all(class_="link2")[0].text
#     print(n)
#     listt.append(item)
#     # print(item)
# temp=[]
# for i in range(0,10):
#     n=huee.find_all(class_="link2")[i].text
#     a={
#         'name':n
#     }
#     temp.append(a)
# rows=huee.find_all(class_="even")




# print(actual_web_links)








web_links = huee.select('a') 
actual_web_links = [web_link['href'] for web_link in web_links]
for i in range(0,108):
    j=actual_web_links[i]
    actual_web_links[i]="https://etender.up.nic.in"
    actual_web_links[i]+=j
# print(actual_web_links[0])
final=[]
temp=[]
p=0
for i in range(0,327):
    if(i%3==0 and i>=6):
        res={
            'Sr.No.':temp[i-3],
            'ORGANIZATION NAME':temp[i-2],
            'LINK':actual_web_links[p]
        }
        p+=1
        final.append(res)
    j=huee.find_all('td')[i].text
    temp.append(j)
# res={
#             'Sr.No.':temp[i-3],
#             'Organization_Name':temp[i-2],
#             'link':actual_web_links[p]
#         }
# print(final)
# res={
#     'Sr.No.':3,
#     'Organization_Name':"Motor Vehicle Division",
#     'link':"https://sikkimtender.gov.in/nicgep/app?component=%24DirectLink&page=FrontEndTendersByOrganisation&service=direct&session=T&sp=Sah2zYAQ5M9H4B0r42Ywf6w%3D%3D"    
# }
# final.append(res)
# print(final)
df=pd.DataFrame(final)
# print(df)
df.to_csv('./torg/up.csv')
# df.to_excel('Jharkhand_data.xlsx')