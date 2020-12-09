valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check_entries(passport):
    if len(passport) != 7:
        return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if int(passport['iyr']) < 2010 or int(passport['byr']) > 2020:
        return False
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    measure = passport['hgt'][:2:-1]
    if (measure != 'mc' and measure != 'ni'):
        return False
    if (len(passport['hgt']) < 2):
        return False
    height = int(passport['hgt'][:-2])
    if passport['hgt'][-1] == 'm':
        if height < 150 or height > 193:
            return False
    else:
        if height < 59 or height > 76:
            return False
    if passport['hcl'][0] != '#':
        return False
    hcl = passport['hcl'][1:]
    try:
        int(hcl, 16)
    except ValueError:
        return False
    if passport['ecl'] not in valid_ecl:
        return False
    if len(passport['pid']) != 9:
        return False
    try:
        int(passport['pid'])
    except ValueError:
        return False
    return True

def main():
    f = open("puzzle4-input.txt", "r")
    valid = 0
    check = 0
    passport = {}
    valid_catg = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in f:
        if line == '\n':
            if check_entries(passport):
                valid += 1
            check = 0
        else:
            entries = line.split(" ")
            for entry in entries:
                data = entry.split(':')
                if data[0] in valid_catg:
                    passport[data[0]] = data[1]
                
    if check_entries(passport):
        valid += 1        
    print('valid: ' + str(valid))
main()