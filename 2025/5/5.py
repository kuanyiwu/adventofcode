with open('input', 'r') as file:
    lines = file.read().splitlines()
    fresh_range = []
    fresh_count = 0
    for line in lines:
        split_res = line.split('-')
        if(len(split_res) > 1):
            for i in range(int(split_res[0]), int(split_res[1]) + 1):
                fresh.add(i)
        elif(len(split_res) == 1 and len(split_res[0]) > 0):
            if int(split_res[0]) in fresh:
                fresh_count += 1
    print(fresh_count)
