def read_input():
    input = []
    f = open("puzzle3-input.txt", "r")
    for line in f:
        input.append(line)
    return input

def main():
    input = read_input()
    width = len(input[0])-1
    tree = 0
    col_pos = 0
    row_pos = 0

    while(row_pos < (len(input) - 1)):
        col_pos += 3
        col_pos = col_pos % width
        row_pos += 1

        if (input[row_pos][col_pos] == '#'):
            tree += 1
    print(tree)

main()
