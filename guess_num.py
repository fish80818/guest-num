import random
start = input('請決定隨機數字範圍起始值: ')
end = input('請決定隨機數字範圍終止值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 
	num = input('請輸入數字: ')
	num = int(num)
	if num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	else:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	print('這是你猜的第', count, '次')