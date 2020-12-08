

numbers = []

while True:
	l = input().rstrip()
	if l:
		numbers.append(int(l))
	else:
		break

# print(numbers)
# for i in numbers:
# 	for j in numbers:
# 		for k in numbers:
# 			if i + j + k == 2020:
# 				print(i)
# 				print(j)
# 				print(k)
# 				print("done")
# 				print(i*j*k)
# 				exit()

s = 0
for i in numbers:
	s += i//3 - 2

print(s)
