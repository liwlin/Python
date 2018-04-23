 ###
 # @Author: Robot.LI 
 # @Date: 2018-04-12 16:44:14 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-04-12 16:44:14 
 ### 

import requests
req=requests.get('http://www.youku.com/')
#print(req.text) #输出网页的html文本
print(req.json)