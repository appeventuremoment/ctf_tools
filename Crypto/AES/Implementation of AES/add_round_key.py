state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
	test = ""
	temp = 0
	for x in range(4):
		for y in range (4):
			temp = s[x][y] ^ k[x][y]
			test += str(temp) + " "
	return test


print(add_round_key(state, round_key))

