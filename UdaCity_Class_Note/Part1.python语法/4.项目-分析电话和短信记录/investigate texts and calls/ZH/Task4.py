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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
'''电话号码满足2个条件，一：只有拨出电话，没有接听电话；二：没有短信记录（收、发）'''

def sales_calls(list1,list2):
    call_tels = [] #拨出电话的集合
    answer_tels = [] #接听电话的集合
    message_tels = [] #收发短信的集合
    a_tels = []  #疑似推销电话号码集合
    b_tels = [] #确认为短小电话的集合
    for call in calls:   
        call_tels.append(call[0])
        answer_tels.append(call[1])  
    for message in texts: 
        message_tels.append(message[0])
        message_tels.append(message[1])
    for call_tel in call_tels: #第一个条件
        if call_tel not in answer_tels:
            a_tels.append(call_tel)
    for a_tel in a_tels: #第二个条件
        if a_tel not in message_tels:
            b_tels.append(a_tel)

    print("These numbers could be telemarketers: ")

    for b_tel in sorted(set(b_tels)):  #排set转化为集合（把重复项去除），循环输出
        print(b_tel)

sales_calls(calls,texts)
        