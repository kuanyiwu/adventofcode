import functools

lines = []
with open('input', 'r') as file:
    lines = file.read().splitlines()

input_to_output = {}
for line in lines:
    input, all_output = line.split(': ', 2)
    input_to_output[input] = all_output.split(' ')

@functools.cache
def dfs(curr, hit_fft, hit_dac):
    if curr == 'out':
        if hit_fft and hit_dac:
            return 1
        return 0
    paths = 0
    for output in input_to_output[curr]:
        paths += dfs(output, hit_fft or curr == 'fft', hit_dac or curr == 'dac')
    return paths

print(dfs('svr', False, False))