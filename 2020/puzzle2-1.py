# goal: parse password policy and check if password contains (lower < number < upper) chars
# input format: lower-upper char: password

f = open("puzzle2-input.txt", "r")
valid = 0
for line in f:
    line_list = line.split(" ")

    bounds = line_list[0].split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])
    char = line_list[1][0]
    password = line_list[2]

    count = password.count(char)
    if lower <= count and count <= upper:
        valid += 1
print(valid)
