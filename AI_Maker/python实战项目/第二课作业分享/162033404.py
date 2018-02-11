'''下为显示格式,不为最终版本,很多功能没有完善.
____________________________________________________________
下面是您的基本信息:
您的姓名是:jin hai
您的生日是:1983年1月1日
您的星座是:摩羯座
您的生肖是:猪
您的年龄是:35岁
您的性别是:male
____________________________________________________________
下面是对您的一些鼓励:
您现在正处于人生的黄金阶段,抛开一切努力工作,实现自己的梦想
____________________________________________________________

	所计算出的生肖不准确,
	尽请见谅,因为这是按照西方历法计算出来的,
	按照中国农历历法计算的话有区别,区别不大,
	可能相差1-2个月,敬请见谅,谢谢!'''


import platform
import time
import os


# 为了界面清洁定义了下面两个函数,根据系统的不同,进行清屏
def TestPlatform():
    print("----------Operation System--------------------------")
    #Windows will be : (32bit, WindowsPE)
    #Linux will be : (32bit, ELF)
    print(platform.architecture())

    #Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    #Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
    print(platform.platform())

    #Windows will be : Windows
    #Linux will be : Linux
    print(platform.system())

    print("--------------Python Version-------------------------")
    #Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        os.system('cls')
    elif (sysstr == "Linux"):
        os.system('clear')
    else:
        os.system('clear')


# 定义一个chinese_zodiac的生肖函数,通过传递的形参年计算用户生肖
def chinese_zodiac(year):
    zodiac_map = {
        u'鼠': 1900,
        u'牛': 1901,
        u'虎': 1902,
        u'兔': 1903,
        u'龙': 1904,
        u'蛇': 1905,
        u'马': 1906,
        u'羊': 1907,
        u'猴': 1908,
        u'鸡': 1909,
        u'狗': 1910,
        u'猪': 1911
    }

    for k, v in zodiac_map.items():
        if (year % v % 12) == 0:
            return k


# 定义一个zodiac的星座函数,通过传递形参月日计算用户星座
def zodiac(month, day):
    zodiac_map = {
        u'白羊座': [(3, 21), (4, 20)],
        u'金牛座': [(4, 21), (5, 20)],
        u'双子座': [(5, 21), (6, 21)],
        u'巨蟹座': [(6, 22), (7, 22)],
        u'狮子座': [(7, 23), (8, 22)],
        u'处女座': [(8, 23), (9, 22)],
        u'天秤座': [(9, 23), (10, 22)],
        u'天蝎座': [(10, 23), (11, 21)],
        u'射手座': [(11, 23), (12, 22)],
        u'水瓶座': [(1, 20), (2, 18)],
        u'双鱼座': [(2, 19), (3, 20)]
    }
    for k, v in zodiac_map.items():
        if v[0] <= (month, day) <= v[1]:
            return k
    if (month, day) >= (12, 22) or (month, day) <= (1, 19):
        return u'摩羯座'

# 判断用户输入的userDate的有效性和切片
def user_date():
    global userDate, userMonth, userDay
    user_answer_correct = False
    while not user_answer_correct:
        # 下面进行分辨生日的年月日,进行计算星座
        # 把用户输入数据得到的userDate数据进行len操作,输出长度存入临时变量temp,用于后面的判断
        temp = len(userDate)
        # 进行生日的日月长度判断最大4位数
        if temp == 4:
            # 进行数据切片操作,对用户输入的得到的日期userDate进行前两位切片并且转换成int类型,以备候用
            userMonth = int(userDate[0:2])
            # 进行数据切片操作,对用户输入的得到的日期userDate进行后两位切片并且转换成int类型,以备候用
            userDay = int(userDate[2:4])
            print('您输入的生日有效')
            user_answer_correct = True
        else:
            userDate = input('输入错误,请重新输入:')


# 判断用户的性别
def user_gender():
    global userGender
    user_answer_correct = False
    while not user_answer_correct:
        temp2 = userGender
        if temp2 == 'nan' or temp2 == 'male' or temp2 == '男':
            print('您输入的性别有效' + temp2)
            user_answer_correct = True
        elif temp2 == 'nv' or temp2 == 'female' or temp2 == '女':
            print('您输入的性别有效' + temp2)
            user_answer_correct = True
        else:
            userGender = input('输入错误,请重新输入:')


# 根据年龄的大小,判断一些东西
def user_age():
    if userAge > 25 and userAge < 45:
        print('您现在正处于人生的黄金阶段,抛开一切努力工作,实现自己的梦想')
    elif userAge > 5 and userAge < 25:
        print('您现在正处于人生的成长阶段,抛开一切努力学习,积累自己的知识')
    elif userAge > 0 and userAge < 6:
        print('您现在正处于人生的认知阶段,快快乐乐的成长吧,享受这个世界给你带来的新鲜')
    else:
        print('您现在正处于人生的享受阶段,享受一切,享受生活,享受家庭,您以前的付出,值得您现在这个阶段的享受')


# 先让用户输入自己的部分信息
user_answer_correct = False
userName = input('您的姓名是:')
userYear = int(input('您的生日年份是(1999):'))
userDate = input('您的生日日期是(0101):')
user_date()
userGender = input('您的性别是(男/女):')
user_gender()

# 间隔时间为2秒,优化显示,提高体验
time.sleep(2)

# 计算年龄
userAge = int(time.strftime('%Y', time.localtime(time.time()))) - userYear

# 清屏
UsePlatform()

# 打印分隔符及基本信息
print('_'*60)
print('下面是您的基本信息:')
print('您的姓名是:' + userName)
print('您的生日是:' + str(userYear) + '年' + str(userMonth) + '月' + str(userDay) + '日')
print('您的星座是:' + zodiac(userMonth, userDay))
print('您的生肖是:' + chinese_zodiac(userYear))
print('您的年龄是:' + str(userAge) + '岁')
print('您的性别是:' + userGender)

# 打印分隔符及提示语言
print('_' * 60)
print('下面是对您的一些鼓励:')
user_age()
print('_' * 60)

print('''\n\t所计算出的生肖不准确,
\t尽请见谅,因为这是按照西方历法计算出来的,
\t按照中国农历历法计算的话有区别,区别不大,
\t可能相差1-2个月,敬请见谅,谢谢!''')