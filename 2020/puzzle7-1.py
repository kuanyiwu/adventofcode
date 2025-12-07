def main():
    f = open("puzzle6-input.txt", "r")
    sum = 0
    ans_set = set()
    for line in f:
        if line == '\n':
            sum += len(ans_set)
            ans_set = set()
        else:
            for i in line:
                if i != '\n':
                    ans_set.add(i)
    
    sum += len(ans_set)
    print(sum)


main()