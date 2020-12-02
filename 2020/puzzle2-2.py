# goal: parse password policy and check if password contains exactly one char at specified positions
# input format: pos1-pos2 char: password
# password indexing starts at 1

f = open("puzzle2-input.txt", "r")
valid = 0
for line in f:
    line_list = line.split(" ")

    bounds = line_list[0].split("-")
    pos1 = int(bounds[0]) - 1
    pos2 = int(bounds[1]) - 1
    char = line_list[1][0]
    password = line_list[2]
    occur = 0
    if pos1 < len(password) and password[pos1] == char:
        occur += 1
    if pos2 < len(password) and password[pos2] == char:
        occur += 1
    if occur == 1:
        valid += 1
print(valid)
