#Lowyat.net Parser to gather the information more about Manglish
from bs4 import BeautifulSoup
import requests
import json
import datetime
import urllib3
import re

url = 'https://forum.lowyat.net/Kopitiam'
LYNTOPICURL = 'https://forum.lowyat.net'
def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')


## This will parse the LYN Topic Parser
## It should extract the topic
def parseLYN(url):
    
    result = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    #find paging page 
    divs = soup.find_all("div",{'style':'float:left'})
   # print(divs)
    for div in divs:
        print div.find('a').contents[0] ## Print's the Topic
        print div.find('a')['href']
        parseThread(div.find('a')['href'])
        break;
        ##print(div.text)
        ###break
        ##result = re.match(".*?(?=\s{2})",div.text)
        ##if result:
        ##    print result.group(0)
        #print(div.find('a')['href'])
        #print(div.find('a').contents[0])
        #print(div)
        #print(div.get_(text))
       

        

def parseThread(topicID):

    result = []
    req = requests.get(LYNTOPICURL + topicID)
    soup = BeautifulSoup(req.text, "lxml")
    # postcolor post_text - LYN uses it to tell if it is a post or not. We will take a look at it 
    thread = soup.find_all("div",{'class':'postcolor post_text'})
    for post in thread:
        print post.text


 

url = 'https://forum.lowyat.net/Kopitiam'
crawl  = parseLYN(url)
#with open("kompas.json","w") as f:
#    json.dump(crawl,f)