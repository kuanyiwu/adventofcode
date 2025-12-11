
import copy

lines = []
with open('input', 'r') as file:
    lines = file.read().splitlines()


sum = 0
for line in lines:
    # Parse input into target, buttons, and joltage.
    # Sample: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    target = line.split(' ')[0][1:-1]
    joltage = line.split(' ')[-1][1:-1]
    buttons = line[len(target) + 3: -(len(joltage) + 3)].split(' ')
    for index in range(len(buttons)):
        buttons[index] = buttons[index][1:-1].split(',')

print(sum)
    

