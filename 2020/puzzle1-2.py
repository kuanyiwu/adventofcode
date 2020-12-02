# goal: find 3 input numbers that add to 2020

ans = set()
input = set()
def recurse(sum, times):
    if sum == 0 and times == 0:
        return True
    elif times == 0:
        return False
    else:
        res = False
        for i in input:
            if len(ans) == 3:
                break
            if recurse(sum-i, times-1):
                res = True
                ans.add(i)
        return res


f = open("puzzle1-input.txt", "r")
for line in f:
    input.add(int(line))

recurse(2020, 3)
print('values=' + str(ans))