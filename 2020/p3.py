

grid = []
while True:
	l = input().rstrip()
	if l:
		grid.append(l)
	else:
		break


interesting_slopes = [
	(1, 1),
	(1, 3),
	(1, 5),
	(1, 7),
	(2, 1),
]
tree_multiplications = 1
for dx, dy in interesting_slopes:
	i = 0
	j = 0
	trees_count = 0
	print(dx, dy)
	while i < len(grid):
		# print(i, j % len(grid[i]), j, grid[i])
		if grid[i][j % len(grid[i])] == "#":
			trees_count += 1
		i += dx
		j += dy

	tree_multiplications *= trees_count
	print(dx, dy, trees_count)

print(tree_multiplications)
