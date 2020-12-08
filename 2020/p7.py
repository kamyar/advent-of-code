from collections import defaultdict
from pprint import pprint

bag_contains = defaultdict(dict)
while True:
	l = input()
	if not l: break
	# raw.append(l.strip())
	target, inside_bags_raw = l.split("bags contain")
	target = target.strip()
	inside_bags = [b.strip() for b in inside_bags_raw.split(",")]

	print(target)
	for bag_desc in inside_bags:
		space_index = bag_desc.strip().find(" ")
		number = bag_desc[:space_index]
		bag_type = bag_desc[space_index:].split("bag")[0].strip()
		print(bag_type, number)
		if number.isnumeric():
			bag_contains[target][bag_type] = int(number)
		else:
			bag_contains[target] = {}


pprint(bag_contains)


def get_bag_total_bags_count(bag):
	r = 0
	for b, count in bag_contains[bag].items():
		r += count
		r += count * get_bag_total_bags_count(b)
	return r



yellow_containers = set()
ALL_THAT_CONTAINS = set()
YELLOW_SHINY = "shiny gold"
bags_to_check = [YELLOW_SHINY]
already_visited = set()
while bags_to_check:
	# print(bags_to_check)
	# from time import sleep
	# sleep(1)
	# get one
	current_bag = bags_to_check.pop()
	# add to visited set
	already_visited.add(current_bag)
	# Loop looking for this bag
	for bag, bag_contents in bag_contains.items():
		if current_bag in bag_contents.keys():
			if bag not in bags_to_check and bag not in already_visited:
				ALL_THAT_CONTAINS.add(bag)
				bags_to_check.append(bag)

	# # get bag content abgs
	# bag_content = bag_contains[current_bag]
	# # yellow ina ny of them?
	# if YELLOW_SHINY in bag_content.keys():
	# 	if current_bag not in bags_to_check and current_bag not in already_visited:
	# 		ALL_THAT_CONTAINS.add(current_bag)
	# 		bags_to_check.append(current_bag)

print(ALL_THAT_CONTAINS)
print(len(ALL_THAT_CONTAINS))

print("TOTAL:", get_bag_total_bags_count("mirrored chartreuse"))
print("TOTAL:", get_bag_total_bags_count(YELLOW_SHINY))
