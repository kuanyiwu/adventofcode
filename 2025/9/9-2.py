# Took too long.

from collections import namedtuple
from heapq import heappush, heappop

Point = namedtuple('Point', ['x', 'y'])

points = []
left_most = 10000000
right_most = 0
up_most = 10000000
down_most = 0

with open('input', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        coord = line.split(',')
        point = Point(x=int(coord[0]), y=int(coord[1]))
        points.append(point)
        if point.x < left_most:
            left_most = point.x
        if point.x > right_most:
            right_most = point.x
        if point.y < up_most:
            up_most = point.y
        if point.y > down_most:
            down_most = point.y

# Transform the matrix start point to 0 indexed at x and y.
for i in range(0, len(points)):
    points[i] = Point(x=points[i].x-left_most, y=points[i].y - up_most)
right_most -= left_most
down_most -= up_most

# Stora a max heap of area.
area_heap = []
for point in points:
    for other_point in points:
        area = (abs(point.x - other_point.x) + 1) * (abs(point.y - other_point.y) + 1)
        heappush(area_heap, (area * -1, (point, other_point)))

# initialize the matrix.
matrix = [[0 for _ in range(down_most + 1)] for _ in range(right_most + 1)]

# Trace the outline.
for i in range(0, len(points)-1):
    curr = points[i]
    next = points[i+1]
    if curr.x == next.x:
        for j in range(min(curr.y, next.y), max(curr.y, next.y) + 1):
            matrix[curr.x][j] = 1
    else:
        for j in range(min(curr.x, next.x), max(curr.x, next.x) + 1):
            matrix[j][curr.y] = 1
points.remove(points[-1])

# BFS to fill in the innards.
starting_point = Point(x=0, y=0)
for i in range(0, right_most + 1):
    if matrix[i][0] == 1 and matrix[i][1] == 0:
        starting_point = Point(x=i, y=1)
        break

queue = [starting_point]
while len(queue) > 0:
    curr = queue[0]
    if matrix[curr.x][curr.y] == 0:
        queue.append(Point(x=curr.x-1, y=curr.y))
        queue.append(Point(x=curr.x+1, y=curr.y))
        queue.append(Point(x=curr.x, y=curr.y-1))
        queue.append(Point(x=curr.x, y=curr.y+1))
    matrix[curr.x][curr.y] = 1
    del queue[0]

def is_vertical_valid(x, y1, y2):
    for y in range(y1, y2 + 1):
        if matrix[x][y] == 0:
            return False
    return True
        
def is_horizontal_valid(x1, x2, y):
    for x in range(x1, x2 + 1):
        if matrix[x][y] == 0:
            return False
    return True

while len(area_heap) > 0:
    area, points = heappop(area_heap)
    point1, point2 = points
    xs = sorted([point1.x, point2.x])
    ys = sorted([point1.y, point2.y])
    if (is_horizontal_valid(xs[0], xs[1], ys[0]) 
        and is_horizontal_valid(xs[0], xs[1], ys[1])
        and is_vertical_valid(xs[0], ys[0], ys[1])
        and is_vertical_valid(xs[1], ys[0], ys[1])
        ):
        print(area * -1)
        break