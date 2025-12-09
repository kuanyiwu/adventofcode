from collections import namedtuple
from heapq import heappush, heappop
import math

Point = namedtuple('Point', ['x', 'y', 'z'])

def distance(p1, p2):
    return math.sqrt(abs(p1.x - p2.x) ** 2 
                     + abs(p1.y - p2.y) ** 2 
                     + abs(p1.z - p2.z) ** 2)
points = []
with open('input', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        coord = line.split(',')
        points.append(Point(x=int(coord[0]), y=int(coord[1]), z=int(coord[2])))

dist_heap = []

# Create a heap of distance pairs.
for point in points:
    for other_point in points:
        if point == other_point:
            continue
        heappush(dist_heap, (distance(point, other_point), (point, other_point)))

point_groups = []
connections = set()
connected = set()
last_connection = None

while len(connected) < len(points) or len(point_groups) > 1:
    _, point_tuple = heappop(dist_heap)
    point, other_point = point_tuple
    added = []
    already_connected = False
    for index, point_group in enumerate(point_groups):
        if (other_point, point) in connections:
            already_connected = True
        if point in point_group or other_point in point_group:
            point_groups[index].add(point)
            point_groups[index].add(other_point)
            added.append(index)
    if already_connected:
        continue
    connections.add((point, other_point))
    last_connection = (point, other_point)
    connected.add(point)
    connected.add(other_point)
    if len(added) == 0:
        # create a new set when points do not exist yet.
        new_set = set()
        new_set.add(point)
        new_set.add(other_point)
        point_groups.append(new_set)
    elif len(added) == 2:
        # merge a set if points exist in two sets.
        first = added[0]
        second = added[1]
        point_groups[first] = point_groups[first] | point_groups[second]
        del point_groups[second]

print(last_connection[0].x * last_connection[1].x)

    
