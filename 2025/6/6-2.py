with open('input', 'r') as file:
    lines = file.read().splitlines()
    row_numbers = []
    for line in lines[:-1]:
        row_numbers.append(line.split())
    vert_numbers = []
    for col in range(len(row_numbers[0])):
        vert_number_group = []
        for row in range(len(row_numbers)):
            vert_number_group.append(row_numbers[row][col])
        vert_numbers.append(vert_number_group)

    operations = []
    for operation in lines[-1].split():
        operations.append(operation)

    total_sum = 0
    num_index = 0
    for op in range(len(operations)):
        problem_set = vert_numbers[op]
        digits = len(max(problem_set, key=len))

        arranged_nums = []
        for digit in range(digits):
            curr_num_list = []
            for row in range(0, len(problem_set)):
                col = num_index + digits - digit - 1
                if lines[row][col] != ' ':
                    curr_num_list.append(lines[row][col])
            arranged_nums.append(int(''.join(curr_num_list)))
        

        if operations[op]  == '*':
            multiplied = 1
            for arranged_num in arranged_nums:
                multiplied *= arranged_num
            total_sum += multiplied
        if operations[op] == '+':
            total_sum += sum(arranged_nums)

        num_index += digits + 1
    print(total_sum)