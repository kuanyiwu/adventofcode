def rotate_left(index, left):
    hits_0 = 0
    print('L', left)
    for _ in range(0, left):
        index -= 1
        if index == 0:
            print('hits 0: L', left)
            hits_0 += 1
        if index == -1:
            index = 99
    print(index)
    return hits_0

def rotate_right(index, right):
    hits_0 = 0
    print('R', right)
    for _ in range(0, right):
        index += 1
        if index == 100:
            index = 0
        if index == 0:
            print('hits 0: R', right)
            hits_0 += 1
    print(index)
    return hits_0

with open('input.txt', 'r') as file:
    index = 50
    hits_0 = 0
    for line in file:
        if line[0] == 'R':
            hits_0 += rotate_right(index, int(line[1:-1]))
            index = (index + int(line[1:-1])) % 100
        elif line[0] == 'L':
            hits_0 += rotate_left(index, int(line[1:-1]))
            index = (index - int(line[1:-1])) % 100
    print(hits_0)