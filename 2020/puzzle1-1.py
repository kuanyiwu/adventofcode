# goal: find 2 input numbers that add to 2020

input = set()
f = open("puzzle1-input.txt", "r")
for line in f:
    num = int(line)
    if 2020-num in input:
        print('values= '+ str(num) + ', ' + str(2020-num))
        break
    input.add(num)