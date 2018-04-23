 ###
 # @Author: Robot.LI 
 # @Date: 2018-04-11 16:51:08 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-04-11 16:51:08 
 ### 

import requests
baidu_url='https://www.baidu.com'
req=requests.get(baidu_url)
coo=req.cookies
print(coo)

for key in coo.keys():
    print(key)
    print(coo[key])