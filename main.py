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

def create_strip(points, d):
    strip = []
    middle = middle_x_value(points)
    for point in points:
        if (point[0] > middle - d) and (point[0] < middle + d):
            strip.append(point)
    return strip


def middle_x_value(points):
    return (points[(len(points) // 2) - 1][0] + points[(len(points) // 2)][0]) / 2

def brute_force(points):
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

def closest_point(points):
    if len(points) <= 3:
        return brute_force(points)
    pointsx = sort_by_x(points)
    d1 = closest_point(pointsx[:len(pointsx) // 2])
    d2 = closest_point(pointsx[len(pointsx) // 2:])
    min_dist = min(d1,d2)
    midpoint = middle_x_value(pointsx)
    strip = create_strip(pointsx, min_dist)
    strip = sort_by_y(strip)
    for j in range(len(strip) - 1):
        for i in range(len(strip[j:]) - 1):
            if strip[j][1] - strip[i + j + 1][1] > min_dist:
                break
            if find_distance(strip[j], strip[i + j + 1]) < min_dist:
                min_dist = find_distance(strip[j], strip[i + j + 1])
    return min_dist
    
def main():
    points_base = create_points_list(txtfile)
    print(closest_point(points_base))

if __name__ == "__main__":
    main()
