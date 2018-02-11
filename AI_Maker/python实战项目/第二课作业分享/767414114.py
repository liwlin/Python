#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 19:57:18
# @Author  : Ben (767414114@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import datetime

def get_constellation(month, day):
    days = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
    if day < days[month-1]:
    	return constellations[month-1]
    else:
    	return constellations[month]

sex = input("请输入您的性别（F/M）：")
while (True):
	if sex == 'F' or sex == 'M':
		break
	else :
		print("Wrong Input!\n")
		sex = input("请重新输入您的性别（F/M）：")

age = input("请输入您的年龄：")
while (True):
	if age.lstrip('-').isdigit() == True :
		a = int(age)
	else :
		a = ord(age)

	if a <= 0 or age.isdigit() == False:
		print("Wrong Input!\n")
		age = input("请重新输入您的年龄：")
	else :
		break

year = input("请输入您的出生年：")
month = input("请输入您的出生月：")
day = input("请输入您的出生日：")
days = [31,28,31,30,31,30,31,31,30,31,30,31]
y = int(year)
if (y%4 == 0 and y%100 != 0) or (y%400 == 0) :
	days[1] = 29;
while (True):
	if month.lstrip('-').isdigit() == True :
		m = int(month)
	else :
		m = ord(month)

	if day.lstrip('-').isdigit() == True :
		d = int(day)
	else :
		d = ord(day)

	if m < 1 or m > 12 or month.isdigit() == False :
		print("Wrong Input!\n")
		month = input("请重新输入您的出生月份：")
	elif d < 1 or d > days[m-1] or day.isdigit() == False :
		print("Wrong Input!\n")
		day = input("请重新输入您的出生日：")
	else :
		break

constellation = get_constellation(m, d)

now = datetime.datetime.now().year
print("\n")
print("*"*3,"你%d年的运势" %now,"*"*3)
print("你的星座是：%s座" %constellation)
print("%s座%d年的运势是：\n" %(constellation,now))
if a < 30 :
	if constellation == '摩羯' :
		print("突破困境，柳暗花明")
		if sex == 'M' :
			print("你是一个可爱、温柔的梦想家。")
		elif sex == 'F' :
			print("典型的便利贴女孩，你们善良，你们心软，你们是全世界最好的女孩。你给人的感觉永远那么乖巧勤快，在工作上无怨无悔的样子让人心疼。")
	elif constellation == '水瓶' :
		print("承受压力，谨慎行事")
		if sex == 'M' :
			print("你可能显得猥琐")
		elif sex == 'F' :
			print("你可能显得邪魅")
	elif constellation == '双鱼' :
		print("压力解除，创意缤纷")
		if sex == 'M' :
			print("你很善良")
		elif sex == 'F' :
			print("你很善良")
	elif constellation == '白羊' :
		print("蛰伏隐忍，厚积薄发")
		if sex == 'M' :
			print("你勇敢直接")
		elif sex == 'F' :
			print("你如爷们一样MAN，如狮子座一样霸气，如射手座一样风风火火，如摩羯座一样对工作尽责，是一个上得厅堂下得厨房的职场女强人。")
	elif constellation == '金牛' :
		print("意气风发，直面挑战")
		if sex == 'M' :
			print("你比较慢热，对工作、生活、环境都需要比较长的适应期。")
		elif sex == 'F' :
			print("你是个单纯、活泼、温柔、拥有智慧、有责任感的女生。")
	elif constellation == '双子' :
		print("安静避世，情感挂心")
		if sex == 'M' :
			print("你喜好新鲜事物，他们有着小聪明，但做事常常不太专一")
		elif sex == 'F' :
			print("你古灵精怪的脾气，时而大惊小怪让人可气又可笑，时而发出银铃般的笑容深深吸引你的注意力，时而板着脸装深沉。")
	elif constellation == '巨蟹' :
		print("风水轮转，苦尽甘来")
		if sex == 'M' :
			print("你少言而寡语，讲话比较含蓄。")
		elif sex == 'F' :
			print("你有一副乖巧模样，看到她仿佛就看到了安宁。")
	elif constellation == '狮子' :
		print("沉迷虚幻，难辨真心")
		if sex == 'M' :
			print("你是一枚定时炸弹呀。")
		elif sex == 'F' :
			print("你总是高昂着头，仿佛不把全天下放在眼里的样子。")
	elif constellation == '处女' :
		print("自信满满，激情迸发")
		if sex == 'M' :
			print("你眼光挑剔，却又充满着罗曼蒂克的幻想。")
		elif sex == 'F' :
			print("你的外表犹如天使一般甜美纯洁，可是只要近距离接近，别人会发现你不是天使，你是魔鬼。")
	elif constellation == '天秤' :
		print("努力奋发，一展宏图")
		if sex == 'M' :
			print("你可以做良好的顾问，你能给别人提出参考的意见，解答别人提出的问题。")
		elif sex == 'F' :
			print("你善于交谈，沟通能力极强，但却犹豫不决。")
	elif constellation == '天蝎' :
		print("目标重现，迷茫退却")
		if sex == 'M' :
			print("你坚韧不拔，你有无限的热量。")
		elif sex == 'F' :
			print("你永远看起来那么神秘，让人有一探究竟的冲动。")
	elif constellation == '射手' :
		print("戒骄戒躁，平稳心态")
		if sex == 'M' :
			print("你极端乐观，你的周围总有一群人围着你。你是那个能给人带来美好的人，快乐的像个开心果")
		elif sex == 'F' :
			print("你一个活碰乱跳，比双子座还疯狂的女人。你像男人一样大声开口笑，像男人一样玩蹦极，不屑于木马摩天轮那种弱智的娱乐设施。")
elif a >= 30 :
	print("这么大了还测什么！")