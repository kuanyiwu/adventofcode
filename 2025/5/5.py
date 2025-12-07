with open('input', 'r') as file:
    lines = file.read().splitlines()
    fresh_ranges = []
    fresh_count = 0
    for line in lines:
        split_res = line.split('-')
        if(len(split_res) > 1):
            fresh_ranges.append((int(split_res[0]), int(split_res[1]) + 1))
        elif(len(split_res) == 1 and len(line) > 0):
            id = int(split_res[0])
            for fresh_range in fresh_ranges:
                if id >= fresh_range[0] and id <= fresh_range[1]:
                    fresh_count += 1
                    break
    print(fresh_count)
