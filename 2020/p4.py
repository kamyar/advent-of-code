import re


required_fields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
passports = []

while True:
	this_pass = set()
	try:
		l = input()
	except:
		break

	print("====")
	while l:
		l = l.strip()
		line_info = l.split(" ")
		print(line_info)
		for info in line_info:
			k, v = info.split(":")
			if k == "byr" and not (1920 <= int(v) <= 2002):
				break
			elif k == "iyr" and not(2010 <= int(v) <= 2020):
				break
			elif k == "eyr" and not(2020 <= int(v) <= 2030):
				break
			elif k == "hgt":
				if v.endswith("cm"):
					if not(150 <= int(v[:-2]) <= 193):
						break
				elif v.endswith("in"):
					if not(59 <= int(v[:-2]) <= 76):
						break
				else: break
			elif k == "hcl" and not re.match(r"^#[0-9a-f]{6}$", v):
				break
			elif k == "ecl" and v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				break
			elif k == "pid" and not re.match(r"^[0-9]{9}$", v):
				break
			print("adding ", k)
			this_pass.add(k)
		print("------")
		# this_pass |= {[0] for info in line_info}
		l = input()
	if this_pass:
		passports.append(this_pass)

print(len(list(filter(lambda p: p & required_fields == required_fields, passports))))

