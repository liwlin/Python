 ###
 # @Author: Robot.LI 
 # @Date: 2018-04-10 19:43:24 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-04-10 19:43:24 
 ### 

#status_code:编码状态  200(请求成功)
# 资源（网页）被永久转移到其他网站（301），网站不存在（404），内部服务器错误（500）
#encoding:编码类型
#cookies:缓存
#params :用于填充URL参数

import requests
payload ={'key1':'value1','key2':'value2' }
#req =requests.get('http://www.youku.com/',params=payload)
req =requests.post('http://www.youku.com/',data=payload)

print(req.text)
#print(req.url)
#print(type(req))
#print(req.status_code)
#print(req.encoding)
#print(req.cookies)


