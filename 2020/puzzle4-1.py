def main():
    f = open("puzzle4-input.txt", "r")
    valid = 0
    check = 0
    valid_catg = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in f:
        if line == '\n':
            if check == 7:
                valid += 1
            check = 0
        else:
            entries = line.split(" ")
            for entry in entries:
                catg = entry[:3]
                if catg in valid_catg:
                    check += 1
    if check == 7:
        valid += 1        
    print('valid: ' + str(valid))
main()