# Data: 20180128
# Author: 易_yi
# Subject: forcast your future

import random
questions_list = ['性别(F/M)','姓名','出生日期（8位数字）','职业','未来打算']       #询问项目
#global input_vars     = {'your_gender':'F','your_name':'N','born_data':19800101,'your_work':'F','future_plan':'F'}
input_vars     = ['','',1,'','']
prefix         = ['美貌仙子','魅力男神'] 
user_name      = ''                                           #名字之前的前缀
#引用全局变量，不需要global声明，修改全局变量，需要使用global声明，
#特别地，列表、字典等如果只是修改其中元素的值，可以直接使用全局变量，不需要global声明。

#信息输入
def personal_info():
	global user_name
	question_times = len(questions_list)                                            #问询次数
	#开始输入
	print('Magic House欢迎您！请按要求输入您的信息，预知您的未来。')
	print(question_times)
	i = 0
	for i in range(question_times):
		input_vars[i] = input('请输入您的%s：'%questions_list[i])
		if i == 0:
			if input_vars[i] == 'F' or input_vars[i] == 'f':
				print('您的美丽犹如繁星一样璀璨 :)')
				user_name = prefix[0]
			elif input_vars[i] == 'M' or input_vars[i] == 'm':
				print('您的帅气犹如明月一样光耀 :)')
				user_name = prefix[1]
			else:
				print('Oh! My God. Did you just come back from Tailand')
	i = i + 1

	print('''
		是否需要更正信息：
		    修改信息请按：y
		    输入正确，不用修改请按任意键
		''')
	rapeat_or_not = input()
	if rapeat_or_not == 'y' or rapeat_or_not == 'Y':
		personal_info()

	#取得称呼
	user_name = user_name + input_vars[1]

		
#预测未来
def forecast_future():
	global user_name
	your_input = input('亲爱的%s请输入您现在的想法：'%user_name)
	length = len(your_input)
	random.seed(length) 
	forecast_num = length * random.randint(10,100)
	if forecast_num == 0:
		print('你也太懒了，想不劳而获，白日做梦！')
	else:
		if forecast_num % 4 == 0:
			print('Good luck! 您集天地运气于一身，好好努力一定成就非凡。')
		elif forecast_num % 4 == 1:
			print('Good job! 辛勤的耕耘终将带来沉甸甸的收获。')
		elif forecast_num % 4 == 2:
			print('Enjoy your day. 生活需要调剂，请停下匆忙的脚步欣赏一下美好的现在，审视自己的人生。')
		elif forecast_num % 4 == 3:
			print('Freedom. 生命诚可贵，爱情价更高，若为自由故，二者皆可抛。')
		else:
			print('Attention. 你命犯小人，诸事不宜，请远离豆腐。')


def main():
	global user_name
	personal_info()      #调用个人信息输入子函数

	#调用预测未来子函数
	continue_play = True
	while continue_play:
		forecast_future()
		print('''
			亲爱的%s是否继续预测您的未来？
			    退出预测请输入：n
			    继续预测请按任意键继续。
			'''%user_name)
		mark1 = input()
		if mark1 == 'n'or mark1 == 'N':
			continue_play = False
		else:
			continue_play = True


#运行主程序
main()
