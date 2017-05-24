import random

answer = random.randint(1,11)

while True:
	guess = int(input("숫자를 입력해주세요"))
	if answer>guess:
		print("크다")
	elif answer<guess:
		print("작다")
	else:
		print("정답")
		break
		