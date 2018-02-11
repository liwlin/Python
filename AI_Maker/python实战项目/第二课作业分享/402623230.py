print('______________________________________算命机_______________________________________')
q=5
for x in range (5):
	print('算命点%s'%q)
	q-=1
	a = input('男（B） & 女（G）')
	b = input('凶（x）& (s) 善')
	c = input('打人（d） & (b)不打人')	
	if a=='B' :
		if b=='x' :
			if c=='d' :
				print('你女朋友被你打过')
			elif c=='b' :
				print('你爱骂人')
			else:
				print('不能输这个!!') 
		elif b=='s' :
			if c=='d' :
				print('你打过人次数<10')
			elif c=='b':
				print('你乐于助人')
			else:
				print('不能输这个!!')
			
		else:			
			print('不能输这个!!')	
				
	elif a=='G':
		if b=='x' :
			if c=='d' :
				print('你男朋友被你打过')
			elif c=='b' :
				print('你爱骂人')
			else:
				print('不能输这个!!')
		elif b=='s' :
			if c=='d' :
				print('你打过人次数<10')
			elif c=='b' :
				print ('你乐于助人')
			else:
				print('不能输这个!!')
	else:			
		 print('不能输这个!!')

