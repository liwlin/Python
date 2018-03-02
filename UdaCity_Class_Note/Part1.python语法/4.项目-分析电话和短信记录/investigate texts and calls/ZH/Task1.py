"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
'''
使用set内置函数解决的方法
records = texts + calls 
def remove_duplicates(records):
    mix_records= []
    for i in records:
        mix_records += [i[0], i[1]]
    new_records = set(mix_records)
    return new_records
'''

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


'''
1.calls列表和texts列表合并为为一个列表 records
2.创建一个新的列表new_records,把records列表中所有元素的前两个元素（电话号码）提取出来并存储。
3.删除new_records中的重复电话号码，再统计new_records中的长度即可算出答案
'''
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
 """
 
records = texts + calls 
def remove_duplicates(records):
    mix_records= []
    for i in records:
        mix_records += [i[0], i[1]]
    new_records = []
    for j in mix_records:
        if j not in new_records:
            new_records.append(j)
    return new_records

print("There are {} different telephone numbers in the records.".format(len(remove_duplicates(records))))

