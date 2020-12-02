f = open("puzzle1-input.txt", "r")

total_fuel = 0
for line in f:
    mass = int(line)
    fuel = int(mass/3)-2
    total_fuel += fuel
print(total_fuel)