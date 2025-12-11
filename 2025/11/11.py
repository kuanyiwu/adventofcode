lines = []
with open('input', 'r') as file:
    lines = file.read().splitlines()

input_to_output = {}
for line in lines:
    input, all_output = line.split(': ', 2)
    input_to_output[input] = all_output.split(' ')
    
def dfs(curr, input_to_output):
    if curr == 'out':
        return 1
    paths = 0
    for output in input_to_output[curr]:
        paths += dfs(output, input_to_output)
    return paths

print(dfs('you', input_to_output))