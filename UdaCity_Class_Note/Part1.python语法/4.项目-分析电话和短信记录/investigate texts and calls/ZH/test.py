import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

bangalore_calls_answers = 0
bangalore_calls = 0

for i in calls:
    #print(i[0][:5])
    if i[0][0:5] == "(080)":
        bangalore_calls +=1
        if i[1][0:5] =="(080)":
            bangalore_calls_answers +=1 
            
print(bangalore_calls_answers)
print(bangalore_calls)
percentage =round(bangalore_calls_answers / bangalore_calls,4) *100
print(type(percentage))

print("{} percent of calls from fixed lines in Bangalore are calls,to other fixed lines in Bangalore.".format(
    percentage
    
    ))