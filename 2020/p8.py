


insts = []

while True:
	l = input()
	if not l:
		break
	ins, num = l.strip().split()
	insts.append((ins, int(num)))


acc = 0
next_inst_i = 0
visited_insts_i = set()
while next_inst_i < len(insts):
	if next_inst_i in visited_insts_i:
		break
	visited_insts_i.add(next_inst_i)
	curr_inst, curr_num = insts[next_inst_i]
	if curr_inst == "nop":
		next_inst_i += 1
	elif curr_inst == "jmp":
		next_inst_i += curr_num
	elif curr_inst == "acc":
		acc += curr_num
		next_inst_i += 1
print("ANS_1", acc)


# Bruteforce FTW!
i = 0
while i < len(insts):
	this_inst, this_num = insts[i]
	if this_inst == "nop":
		insts[i] = ("jmp", this_num)
	elif this_inst =="jmp":
		insts[i] = ("nop", this_num)
	else:
		i += 1
		continue

	acc = 0
	next_inst_i = 0
	visited_insts_i = set()
	while next_inst_i < len(insts):
		if next_inst_i in visited_insts_i:
			break
		visited_insts_i.add(next_inst_i)
		curr_inst, curr_num = insts[next_inst_i]
		if curr_inst == "nop":
			next_inst_i += 1
		elif curr_inst == "jmp":
			next_inst_i += curr_num
		elif curr_inst == "acc":
			acc += curr_num
			next_inst_i += 1
	if next_inst_i >= len(insts):
		print("ANS_2", acc)
		break
	insts[i] = (this_inst, this_num)
	i += 1
