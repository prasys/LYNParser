#Lowyat.net Parser to gather the information more about Manglish
from bs4 import BeautifulSoup
import requests
import json
import datetime
import urllib3
import re


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')


## This will parse the bloody LYN
def parseLYN(url):
    
    result = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    #find paging page 
    divs = soup.find_all("div",{'style':'float:left'})
   # print(divs)
    for div in divs:
        print div.find('a').contents[0] ## Print's the Topic 
        ##print(div.text)
        ###break
        ##result = re.match(".*?(?=\s{2})",div.text)
        ##if result:
        ##    print result.group(0)
        #print(div.find('a')['href'])
        #print(div.find('a').contents[0])
        #print(div)
        #print(div.get_(text))
       

        


 

url = 'https://forum.lowyat.net/Kopitiam'
crawl  = parseLYN(url)
#with open("kompas.json","w") as f:
#    json.dump(crawl,f)