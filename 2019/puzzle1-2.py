f = open("puzzle1-input.txt", "r")
def get_fuel(num):
    fuel = int(num/3)-2
    if fuel <= 0:
        return 0
    return fuel + get_fuel(fuel)

total_fuel = 0
for line in f:
    mass = int(line)
    total_fuel += get_fuel(mass)
print(total_fuel)