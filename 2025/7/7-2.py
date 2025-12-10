import functools

lines = []
beam = 0
with open('input', 'r') as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines[0])):
        if lines[0][i] == 'S':
            beam = i
    lines = lines[1:]

@functools.cache
def traverse(row_num, beam):
    if row_num == len(lines):
        return 1
    if lines[row_num][beam] == '^':
        return traverse(row_num + 1, beam - 1) +  traverse(row_num + 1, beam + 1)
    else:
        return traverse(row_num + 1, beam)

print(traverse(0, beam))