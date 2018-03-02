 ###
 # @Author: Robot.LI 
 # @Date: 2018-02-15 17:52:46 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-02-15 17:52:46 
 ### 


import itchat, time
itchat.auto_login()

SINCERE_WISH = u'亲爱的 %s 在这新春到来之际，祝您新年快乐，阖家幸福，万事如意！'


def send_wishes():
    friendList = itchat.get_friends(update=True)[1:]
    for friend in friendList:
        # 如果不是演示目的，把下面的方法改为itchat.send即可
        print(SINCERE_WISH % (friend['DisplayName']
            or friend['NickName']), friend['UserName'])
        time.sleep(3)

send_wishes()