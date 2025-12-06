# Part 2
def is_invalid(num):
    for chunk_size in range(1, len(num) // 2 + 1):
        compare = num[0:chunk_size]
        same = True
        for i in range(0, len(num), chunk_size):
            if compare != num[i:i+chunk_size]:
                same = False
        if same:
            print(num)
            return True
    return False
        
with open('input-2.txt', 'r') as file:
    for line in file:
        ids = line.split(',')
        invalid_sum = 0
        for id in ids:
            pair = id.split('-')
            first = pair[0]
            second = pair[1]
            for r in range(int(first), int(second)+1):
                if is_invalid(str(r)):
                    invalid_sum += r
        print(invalid_sum)