# https://kth.kattis.com/problems/pointinpolygon?editsubmit=10115406

import itertools
import sys


def left(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) > 0

def on(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) == 0

def main():
    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break
        
        polygon = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            polygon.append((x, y))
        
        m = int(sys.stdin.readline())
        for _ in range(m):
            x, y = map(int, sys.stdin.readline().split())
            point = (x, y)
            far_right_point = (10000, point[1])
            
            is_on = False
            for i in range(n-1):
                if on(polygon[i], polygon[i+1], point) and min(polygon[i][0], polygon[i+1][0]) <= point[0] <= max(polygon[i][0], polygon[i+1][0]) and min(polygon[i][1], polygon[i+1][1]) <= point[1] <= max(polygon[i][1], polygon[i+1][1]):
                    is_on = True
                    break
            if is_on:
                print('on')
                continue

            intersections = 0
            for i, z in zip(range(n), itertools.chain(range(1, n), [0])):
                if left(point, far_right_point, polygon[i]) != left(point, far_right_point, polygon[z]) and left(polygon[i], polygon[z], point) != left(polygon[i], polygon[z], far_right_point):
                    if left(polygon[i], polygon[z], point) != left(polygon[i], polygon[z], far_right_point):
                        intersections += 1

            if intersections % 2 == 0:
                print('out')
            else:
                print('in')

if __name__ == '__main__':
    main()