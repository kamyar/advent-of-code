

lines = []
valid_count = 0
valid_count_2 = 0
while True:
	l = input().rstrip()
	if l:
		rule, pwd = l.split(":")
		minmax, char = rule.split(" ")
		charmin, charmax = map(int, minmax.split("-"))
		pwd = pwd.strip()
		if charmin <= pwd.count(char) <= charmax:
			valid_count += 1

		first_pos_is_char = pwd[charmin + -1] == char
		second_pos_is_char = pwd[charmax + -1] == char
		# print(pwd[charmin + -1], pwd[charmax + -1])
		if first_pos_is_char ^ second_pos_is_char:
			valid_count_2 += 1
		lines.append(l)
	else:
		break
print(valid_count)
print(valid_count_2)
