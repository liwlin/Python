 ###
 # @Author: Robot.LI 
 # @Date: 2018-02-15 17:52:46 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-02-15 17:52:46 
 ### 


import itchat, time

SINCERE_WISH = u'亲爱的%s,您好,我是李伟林设计的机器人LI_webot,2017年马上就过去了，2018年马上到来！我仅代表李伟林祝你新年快乐，心想事成。！'
REAL_SINCERE_WISH = u'祝%s新年快乐！！'

def send_wishes():
    friendList = itchat.get_friends(update=True)[1:]
    for friend in friendList:
        # 如果不是演示目的，把下面的方法改为itchat.send即可
        print(SINCERE_WISH % (friend['DisplayName']
            or friend['NickName']), friend['UserName'])
        time.sleep(.5)