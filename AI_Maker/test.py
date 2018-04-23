import time #调用time
print("*"*32)
print("*"," "*28,"*")
print(" *|欢迎使用个人信息报告生成程序|*")
print("*"," "*28,"*")
print("*"*32)
time.sleep(0.5)
for i in range(10):
    print("-",end='')
    print("->",end='')
    time.sleep(0.3)  #休眠0.5秒
print("开始！")


print("|","*"*25,"|")
print("请输入您的姓名：？")
name = input()
print("请输入您的性别：？")
gender = input()
print("你的身高是：？")
height = input()
print("你的体重是：？")
weight = input()
print("|","*"*25,"|")

print("|","*"*25,"|")
print("|","个人信息报告生成","|")
print("名字{}".format(name))
print("性别：{}".format(gender))
print("身高{}".format(height))
print("体重{}".format(weight)),
print("|","*"*16,"|")
