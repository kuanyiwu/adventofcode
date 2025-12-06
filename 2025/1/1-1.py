def wrap(cur):
    while cur > 99:
        cur -= 100
    while cur < 0:
        cur += 100
    return cur

with open('input.txt', 'r') as file:
    index = 50
    hits_0 = 0
    for line in file:
        if line[0] == 'R':
            index += int(line[1:-1])
            index = index % 100
        elif line[0] == 'L':
            index -= int(line[1:-1])
            index = index % 100
        if index == 0:
            hits_0 += 1
    print(hits_0)