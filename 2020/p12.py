

inps = []

while True:
    l = input()
    if not l: break
    clean_l = l.strip()
    inps.append((clean_l[0], int(clean_l[1:])))


EAST = (1, 0)
WEST = (-1, 0)
SOUTH = (0, -1)
NORTH = (0, 1)

match = {
    "E": EAST,
    "W": WEST,
    "S": SOUTH,
    "N": NORTH,
}


TURNS = {
    EAST: {
        "R": SOUTH,
        "L": NORTH,
    },
    WEST: {
        "R": NORTH,
        "L": SOUTH,
    },
    SOUTH: {
        "R": WEST,
        "L": EAST,
    },
    NORTH: {
        "R": EAST,
        "L": WEST,
    },
}

current_dir = EAST
x = 0
y = 0
for cmd, value in inps:
    dx = 0
    dy = 0
    if cmd == "F":
        dx, dy = current_dir
    elif cmd in ["R", "L"]:
        k = value // 90
        for _ in range(k):
            current_dir = TURNS[current_dir][cmd]
    else:
        dx, dy = match[cmd]
    x += dx * value
    y += dy * value

print("ANS1:", abs(x) + abs(y))


current_dir = EAST
waypoint = (10, 1)
x = 0
y = 0
for cmd, value in inps:
    dx = 0
    dy = 0
    wx, wy = waypoint
    if cmd == "F":
        dx, dy = current_dir
        x += value * wx
        y += value * wy
    elif cmd in ["R", "L"]:
        k = value // 90
        for _ in range(k):
            wx, wy = waypoint
            if cmd == "R":
                waypoint = (wy, -1 * wx)
            else:
                waypoint = (-1 * wy, wx)
    else:
        dx, dy = match[cmd]
        waypoint = (dx * value + wx, dy * value + wy)

print("ANS2:", abs(x) + abs(y))


