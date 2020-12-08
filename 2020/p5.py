



from utils import fetch_input
seats = fetch_input(
	transform=lambda l: int(l.replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0"), 2)
)

print(sorted(seats)[-1])
print(set(seats) ^ set(range(min(seats), max(seats)+1)))
