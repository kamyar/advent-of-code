


numbers = []
while True:
	l = input()
	if not l: break
	numbers.append(int(l.strip()))

current_i = 25
unfound_sum_number = None
while current_i < len(numbers):
	current = numbers[current_i]
	rng = numbers[current_i-25:current_i]
	l_rng = len(rng)
	i = 0
	found = False
	while i < l_rng and not found:
		j = i + 1
		while j < l_rng:
			if rng[i] + rng[j] == current:
				print(f"{rng[i]} + {rng[j]} = {current}")
				found = True
				break
			else:
				print(f"{rng[i]} + {rng[j]} != {current}")
			j += 1
		i += 1
		# exit()
	if not found:
		unfound_sum_number = current
		break
	current_i += 1

print(f"{unfound_sum_number} not found")

i = 0
while i < len(numbers):
	extra = 1
	while True:
		this_sum = sum(numbers[i:i+extra])
		if this_sum == unfound_sum_number:
			# TODO solution found
			weakness = min(numbers[i:i+extra]) + max(numbers[i:i+extra])
			print(f"Weakness: {weakness}")
			exit()
		elif this_sum > unfound_sum_number:
			break
		else:
			extra += 1
			continue

	i += 1
