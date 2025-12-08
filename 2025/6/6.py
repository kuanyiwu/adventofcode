with open('input', 'r') as file:
    lines = file.read().splitlines()
    numbers = []
    for line in lines[:-1]:
        numbers.append(line.split())

    operations = []
    for operation in lines[-1].split():
        operations.append(operation)

    total_sum = 0 
    for op in range(len(operations)):
        curr_num = 0 # '+'
        if operations[op]  == '*':
            curr_num = 1
        for num in range(len(numbers)):
            if operations[op]  == '*':
                curr_num *= int(numbers[op][num])
            elif operations[op]  == '+':
                curr_num += int(numbers[op][num])
        print(curr_num)
        total_sum += curr_num
    print(total_sum)