with open('input', 'r') as file:
    sum = 0
    for line in file:
        max_first = 0
        first_index = 0
        for battery_index in range(0, len(line)-2):
            if int(line[battery_index]) > max_first:
                max_first = int(line[battery_index])
                first_index = battery_index
        max_second = 0
        for battery in line[first_index+1:-1]:
            if int(battery) > max_second:
                max_second = int(battery)
        print(max_first * 10 + max_second)
        sum += max_first * 10 + max_second
    print(sum)

