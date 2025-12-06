def is_paper(char):
    return char == '@'

def is_valid_row_col(lines, row, col):
    if row < 0 or row >= len(lines):
        return False
    if col < 0 or col >= len(lines[0]):
        return False
    return True

def paper_access(lines, row, col):
    adj_paper_count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue
            if is_valid_row_col(lines, r, c) and is_paper(lines[r][c]):
                adj_paper_count += 1
            # print('row:' + str(r) +', col: ' +  str(c) + ', adj_paper_count: '+ str(adj_paper_count))
    return adj_paper_count < 4


with open('input', 'r') as file:
    lines = file.read().splitlines()
    count = 0
    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            if is_paper(lines[row][col]) and paper_access(lines, row, col):
                count += 1
    print(count)
    
                    
