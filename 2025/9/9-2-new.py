from shapely.geometry import Polygon, box
from heapq import heappush, heappop

# Create a polygon from a list of coordinate tuples
coords = []
with open('input', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        coord = line.split(',')
        coords.append((int(coord[0]), int(coord[1])))
polygon = Polygon(coords)

area_heap = []
for point in coords:
    for other_point in coords:
        area = (abs(point[0] - other_point[0]) + 1) * (abs(point[1] - other_point[1]) + 1)
        heappush(area_heap, (area * -1, (point, other_point)))
    
while(len(area_heap) > 0):
    area, points = heappop(area_heap)
    point, other_point = points
    if polygon.contains(box(point[0], point[1], other_point[0], other_point[1])):
        print(area)
        break