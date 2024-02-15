import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Review = []

for i in range(2,12):

    url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" + str(i)

    r = requests.get(url)
    

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    for i in names:
        name = i.text 
        Product_name.append(name)
        
    prices = box.find_all("div",class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)

    desc = box.find_all("ul",class_ = "_1xgFaf")  

    for i in desc:
        name = i.text
        Description.append(name)
        

df = pd.DataFrame({"Product_name":Product_name,"Prices":Prices,"Description":Description})
#print(df)
 
 
df.to_csv("C:/Users/Aditya/New folder/FlipkartWebscr.csv")
 
 
 
    # print(len(reviews))


    #while True:
    # np = soup.find("a", class_ = "_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print (cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")
#print (soup)

#names = soup.find_all("a", class_="title")


#for i in np:
    #print(i.text)

#prices = soup.find_all("h4", class_="pull right price")

#for i in prices:
    #print(i.text)