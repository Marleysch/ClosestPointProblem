import math

txtfile = '1.txt'

def create_points_list(txtfile):
    with open(txtfile, 'r') as file:
        content = file.read()
        content = content.replace(" ", "")
    
    points = []
    mode = 0
    point = []
    for char in content[1:]:
        if mode == 1:
            if char == ',':
                point.append(float(x))
                mode = 2
            else:
                x += char
        elif mode == 2:
            if char == '}':
                mode = 0
                point.append(float(y))
                points.append(point)
                point = []
            else:
                y += char
        else:
            if char == "{":
                mode = 1
                x = ''
                y = ''
    return points


def find_distance(point1, point2):
    return math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) 

def monkey(points):
    numofpoints = len(points)
    smallest_distance = find_distance(points[0],points[1])
    curr_distance = smallest_distance + 1
    for i in range(numofpoints - 1):
        for point in points[i + 1:]:
            curr_distance = find_distance(points[i], point)
            if curr_distance < smallest_distance:
                smallest_distance = curr_distance
    return smallest_distance

def sort_by_x(points):
    return sorted(points, key=lambda point:point[0])

def sort_by_y(points):
    return sorted(points, key=lambda point:point[1])


points = create_points_list(txtfile)
print(sort_by_y(points))
print() 
print()
print()
print(monkey(points))