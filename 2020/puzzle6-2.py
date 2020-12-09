def main():
    f = open("puzzle6-input.txt", "r")
    sum = 0
    first_set = set()
    start_group = True
    for line in f:
        if line == '\n':
            sum += len(first_set)
            first_set = set()
            start_group = True
        else:
            if not start_group:
                curr_set = first_set.copy()
                for first in first_set:
                    if first not in line:
                        curr_set.remove(first)
                first_set = curr_set
            else:
                for i in line:
                    if i != '\n':
                        first_set.add(i)
                start_group = False
    
    sum += len(first_set)
    print(sum)


main()