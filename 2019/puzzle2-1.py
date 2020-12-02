f = open("puzzle2-input.txt", "r")

raw_input = f.readline()
str_code = raw_input.split(',')
code = [int(i) for i in str_code] 

pointer = 0

while pointer != len(code):
    optcode = code[pointer]

    if optcode == 1 or optcode == 2:
        input1 = code[code[pointer + 1]]
        input2 = code[code[pointer + 2]]

        if optcode == 1:
            code[code[pointer + 3]] = input1 + input2
        else:
            code[code[pointer + 3]] = input1 * input2
        pointer += 4
    elif optcode == 99:
        break
print(code[0])