def read_input():
    input = []
    f = open("puzzle3-input.txt", "r")
    for line in f:
        input.append(line)
    return input

def main():
    input = read_input()
    width = len(input[0])-1    
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = 1

    for slope in slopes:
        col_pos = 0
        row_pos = 0
        tree = 0
        while(row_pos < (len(input) - 1)):
            col_pos += slope[0]
            col_pos = col_pos % width
            row_pos += slope[1]

            if (input[row_pos][col_pos] == '#'):
                tree += 1
        trees *= tree
    print(trees)

main()
