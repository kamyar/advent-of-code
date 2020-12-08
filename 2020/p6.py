from functools import reduce

inp = []
while True:
	this_group = []
	while True:
		l = input()
		if not l:
			break
		this_group.append(l)

	if not this_group:
		break
	else:
		inp.append(this_group)


print(sum([len(reduce(lambda x, y: set(y) & set(x), group_list)) for group_list in inp]))

