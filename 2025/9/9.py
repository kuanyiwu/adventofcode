from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

points = []
with open('input', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        coord = line.split(',')
        points.append(Point(x=int(coord[0]), y=int(coord[1])))

max_area = 0

for point in points:
    for other_point in points:
        area = (point.x - other_point.x + 1) * (point.y - other_point.y + 1)
        if area > max_area:
            max_area = area
print(max_area)

