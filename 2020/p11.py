from copy import deepcopy
from pprint import pprint
from functools import reduce
seat_mtrx = []

while True:
	l = input()
	if not l:
		break
	seat_mtrx.append(list(l.strip()))


def count_seated(mtrx, i, j):
	count_seated = 0
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if 0 <= i + dx < len(mtrx) and 0 <= j + dy < len(mtrx[0]) and mtrx[i+dx][j+dy] == "#":
				count_seated += 1
	return count_seated

first_part_seats = deepcopy(seat_mtrx)
next_seating = deepcopy(seat_mtrx)
while True:
	i = 0
	while i < len(first_part_seats):
		j = 0
		while j < len(first_part_seats[i]):
			cseated = count_seated(first_part_seats, i, j)

			if first_part_seats[i][j] == "L" and cseated == 0:
				next_seating[i][j] = "#"
			elif first_part_seats[i][j] == "#" and cseated >= 5:
				next_seating[i][j] = "L"
			j += 1
		i += 1
	if next_seating == first_part_seats:
		break
	# Swap
	first_part_seats = deepcopy(next_seating)


print((reduce(lambda x, y: x+y, next_seating).count("#")))


def diagonal_count_seated(mtrx, i, j):
	directions = [
		(-1, -1), (-1, 0), (-1, 1),
		(0, -1), (0, 1),
		(1, -1), (1, 0), (1, 1),
	]
	result = 0
	for direction in directions:
		dx, dy = direction
		x = i + dx
		y = j + dy
		while 0 <= x < len(mtrx) and 0 <= y < len(mtrx[0]):
			if mtrx[x][y] == "L":
				break
			elif mtrx[x][y] == "#":
				result += 1
				break
			x += dx
			y += dy
	return result

next_seating = deepcopy(seat_mtrx)
while True:
	i = 0
	while i < len(seat_mtrx):
		j = 0
		while j < len(seat_mtrx[i]):
			cseated = diagonal_count_seated(seat_mtrx, i, j)

			if seat_mtrx[i][j] == "L" and cseated == 0:
				next_seating[i][j] = "#"
			elif seat_mtrx[i][j] == "#" and cseated >= 5:
				next_seating[i][j] = "L"
			j += 1
		i += 1
	if next_seating == seat_mtrx:
		break
	# Swap
	seat_mtrx = deepcopy(next_seating)

print((reduce(lambda x, y: x+y, next_seating).count("#")))
