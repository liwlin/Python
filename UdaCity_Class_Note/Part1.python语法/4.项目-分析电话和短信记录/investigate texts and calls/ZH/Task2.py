"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

call_times ={}
for i in calls:
    if i[0] in call_times:      #i[0] 判断clls列表中第一个元素（主叫号码）是否字典内的键
        call_times[i[0]] += int((i[3]))  #如果是重复号码，则把号码的通话时长累加 ***需要注意由于字典的值为int型，需要进行数据转换***
    else:
        call_times[i[0]] =int(i[3])   #如果没有不是重复号码，则直接赋值对应号码的通话时间。
for i in calls:
    if i[1] in call_times:    #j[1] 判断calls列表中第二个元素（被叫号码）是否字典内的键
        call_times[i[1]] += int((i[3]))    #如果是重复号码，则把号码的通话时长累加
    else:
        call_times[i[1]] = int((i[3]))   #如果没有不是重复号码，则直接赋值对应号码的通话时间   
#print(call_times)  #打印call_times 字典

'''#方法一：使用 max与zip的使用
num = max(zip(call_times.values(),call_times.keys())) 
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(num[1],num[0]))
'''
#方法二：直接使用max函数
num = max(call_times.values())
time = max(call_times,key =call_times.get)
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(num,time))