def execute(code):
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
    return code[0]

def main():
    f = open("puzzle2-input.txt", "r")
    raw_input = f.readline()
    str_code = raw_input.split(',')
    for noun in range(100):
        for verb in range(100):
            int_code = [int(i) for i in str_code] 
            int_code[1] = noun
            int_code[2] = verb
            if execute(int_code) == 19690720:
                print(100*noun + verb)
                return

main()