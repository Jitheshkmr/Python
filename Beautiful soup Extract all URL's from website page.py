import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =input('Enter URL : ')
count =input('Enter count : ')
position =input('Enter position : ')
i=0
n=0
count=int(count)
position=int(position)
while i<count:
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    
    tags=soup('a')
    for tag in tags:
        n=n+1
        if n==position:
            url=tag.get('href',None)
            print(url)
            n=0
            i=i+1
            break