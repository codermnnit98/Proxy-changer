import bs4
import requests
from bs4 import BeautifulSoup
import re
import subprocess
from subprocess import Popen,PIPE


inp = "http://172.31.9.69/dc/proxy"




page = requests.get(inp)
soup = BeautifulSoup(page.content,'html.parser')

flag=-1

proxy_max=""
port_max=""
speed_max=-1
occupied=-1

for link in soup.find_all('tr',class_="text-success")[1:]:

 pp=link.find_all('td')
 proxy=pp[0]
 proxy_str=''.join(proxy.findAll(text=True))

 port=pp[1]
 port_str=''.join(port.findAll(text=True))

 status=pp[2].b
 status_str=''.join(status.findAll(text=True))
 status_str=status_str.lstrip()
 
 per=pp[3]
 per_str=''.join(per.findAll(text=True))

 speed=pp[4].b
 speed_str=''.join(speed.findAll(text=True))

 

 j=(int)(speed_str.find(' '))
 speed_digits=speed_str[0:j]
 kbmb=speed_str[j+1]
 speed_float=float(speed_digits)
 if kbmb == "K":
 	speed_float=speed_float/1024.0
 per_int=per_str[0:per_str.find(' ')]

 if status_str =="Working":
     flag=1

     if speed_float > speed_max:
        proxy_max=proxy_str
        port_max=port_str
        speed_max=speed_float
        occupied=per_int
     elif speed_float == speed_max and occupied > per_int:
        proxy_max=proxy_str
        port_max=port_str
        occupied=per_int

if flag==1:
	print(proxy_max)
	print(port_max)
	print(speed_max)
	print(occupied)

else:
	print("No working proxy right now, please open the script again!!")

Process=Popen(['./proxy-changer.sh',str(proxy_max),str(port_max)],shell=True,stdin=PIPE,stderr=PIPE)
