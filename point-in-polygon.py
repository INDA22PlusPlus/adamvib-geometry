# https://kth.kattis.com/problems/pointinpolygon?editsubmit=10115406

import sys

import numpy as np


def left(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

def distance(a, b, p):
    a = np.array(a)
    b = np.array(b)
    p = np.array(p)
    return np.linalg.norm(np.cross(b-a, a-p))/np.linalg.norm(b-a)

def counter_clockwise(polygon):
    area = 0
    for i in range(len(polygon)):
        area += polygon[i][0] * polygon[(i + 1) % len(polygon)][1] - polygon[(i + 1) % len(polygon)][0] * polygon[i][1]
    return area > 0

def in_range(x, y, closest_line):
    return (closest_line[0][0] <= x <= closest_line[1][0] or closest_line[1][0] <= x <= closest_line[0][0]) and (closest_line[0][1] <= y <= closest_line[1][1] or closest_line[1][1] <= y <= closest_line[0][1])

def main():
    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break
        
        polygon = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            polygon.append((x, y))
        
        cc = counter_clockwise(polygon)
        m = int(sys.stdin.readline())

        for _ in range(m):
            x, y = map(float, sys.stdin.readline().split())
            closest_line = ()

            min_distance = float('inf')
            for i in range(n-1):
                distance = abs(left(polygon[i], polygon[i+1], (x, y)))
                if distance < min_distance:
                    min_distance = distance
                    closest_line = (polygon[i], polygon[i+1])

            left_d = left(closest_line[0], closest_line[1], (x, y))
            
            if cc and left_d > 0 and in_range(x, y, closest_line):
                print('in')
            elif not cc and left_d < 0 and in_range(x, y, closest_line):
                print('in')
            elif left_d == 0 and in_range(x, y, closest_line):
                print('on')
            else:
                print('out')

if __name__ == '__main__':
    main()