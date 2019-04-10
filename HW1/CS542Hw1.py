##repeat some fixed strategies

import random

print("R is Rock, S is Scissor, P is paper.\nNow input the number of games:")

N = input("number of games:")

print('R')

N = N - 1

flag = 1

i = 0

while (i < N):
	if flag == 1:
		print("S")
	elif flag == 2:
		print("R")
	elif flag == 3:
		print("R")
	elif flag == 4:
		print("S")
	elif flag == 5:
		print("R")
	elif flag == 6:
		print("S")
	elif flag == 7:
		print("R")
	elif flag == 8:
		print("R")
	elif flag == 9:
		print("S")
	elif flag == 10:
		print("R")
	elif flag == 11:
		print("S")
	elif flag == 12:
		print("S")
	elif flag == 13:
		print("R")
	elif flag == 14:
		print("S")
	elif flag == 15:
		print("R")
	elif flag == 16:
		flag = 0
		for x in range(1):
			b = random.randint(1,3)
		if b == 1:
			print("R")
		elif b == 2:
			print("S")
		elif b == 3:
			print("P")
	i += 1
	flag += 1
	#print(flag)