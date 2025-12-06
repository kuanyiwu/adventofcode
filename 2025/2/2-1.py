# Part 1
with open('input-2.txt', 'r') as file:
    for line in file:
        ids = line.split(',')
        invalid_sum = 0
        for id in ids:
            pair = id.split('-')
            first = pair[0]
            second = pair[1]
            for r in range(int(first), int(second)+1):
                str_r = str(r)
                mid = len(str_r) // 2
                if len(str_r) % 2 != 0:
                    continue
                if str_r[0:mid] == str_r[mid:]:
                    invalid_sum += r
        print(invalid_sum)