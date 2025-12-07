with open('input-2', 'r') as file:
    lines = file.read().splitlines()
    ranges = []
    fresh_count = 0
    for line in lines:
        split_res = line.split('-')
        if(len(split_res) > 1):
            ranges.append((int(split_res[0]), int(split_res[1])))
    ranges.sort()
    curr_range = ranges[0]
    for range in ranges[1:]:
        if range[0] > curr_range[1]:
            # set curr range to new range and add up numbers if no overlap.
            fresh_count += curr_range[1] - curr_range[0] + 1
            curr_range = range
        elif range[0] <= curr_range[1]:
            # merge range if overlap.
            curr_range = (min(curr_range[0], range[0]), max(curr_range[1], range[1]))
            if range == ranges[-1]:
                # add last range.
                fresh_count += curr_range[1] - curr_range[0] + 1
    print(fresh_count)
