
import copy

lines = []
with open('input', 'r') as file:
    lines = file.read().splitlines()

def bfs(buttons, target):
    search_states = [[False] * len(target)]
    depth = 0
    while True:
        for state in search_states:
            if state == target:
                return depth
        depth += 1
        future_search_states = []
        for state in search_states:
            for button in buttons:
                curr_state = copy.deepcopy(state)
                for index in button:
                    button_num = int(index)
                    curr_state[button_num] = not curr_state[button_num]
                future_search_states.append(curr_state)
        search_states = future_search_states

def parse_target(line):
    target = []
    for l in line:
        if l == '.':
            target.append(False)
        else:
            target.append(True)
    return target

sum = 0
for line in lines:
    # Parse input into target, buttons, and joltage.
    # Sample: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    target = parse_target(line.split(' ')[0][1:-1])
    joltage = line.split(' ')[-1][1:-1]
    buttons = line[len(target) + 3: -(len(joltage) + 3)].split(' ')
    for index in range(len(buttons)):
        buttons[index] = buttons[index][1:-1].split(',')

    # Do a BFS search of state that is equivalent to target.
    sum += bfs(buttons, target)
print(sum)
    

