 ###
 # @Author: Robot.LI 
 # @Date: 2018-02-18 19:54:14 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-02-18 19:54:14 
 ### 

import itchat
itchat.auto_login()

@itchat.msg_register(lwl)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)

_(msg)