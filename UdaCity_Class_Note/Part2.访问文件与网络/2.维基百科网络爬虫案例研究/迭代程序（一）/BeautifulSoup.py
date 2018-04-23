 ###
 # @Author: Robot.LI 
 # @Date: 2018-04-12 15:16:41 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-04-12 15:16:41 
 ### 

import requests
from bs4 import BeautifulSoup

req=requests.get('http://www.youku.com')
html =req.text
#print(html)
soup = BeautifulSoup(html,"html.parser")
#print(soup)
#soup.find(id='mw-content-text')
print(soup.find(id='AWSC_uabModule'))
