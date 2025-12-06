with open('input', 'r') as file:
    lines = file.read().splitlines()
    sum = 0
    for line in lines:
        last_index = -1
        joltage = 0
        for digit in range(1, 13):
            max_battery = 0
            start = last_index + 1
            for battery_index in range(start, len(line) - (12 - digit)):
                if int(line[battery_index]) > max_battery:
                    max_battery = int(line[battery_index])
                    last_index = battery_index
            joltage += max_battery * pow(10, 12 - digit)
        sum += joltage
    print(sum)
