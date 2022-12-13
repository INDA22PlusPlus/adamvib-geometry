# https://kth.kattis.com/problems/convexhull

import math
import sys


def graham_scan(points):
    if len(points) < 3:
        if len(points) == 2 and points[0] == points[1]:
            return [points[0]]
        return points

    # remove duplicates
    points = [t for t in (set(tuple(p) for p in points))]
    points.sort(key=lambda p: [p[1], p[0]])
    stack = [points[0]]
    points.pop(0)
    points.sort(key=lambda p: math.atan2(p[1] - stack[0][1], p[0] - stack[0][0]))

    for i in range(len(points)):
        while len(stack) >= 2 and not is_counter_clockwise(stack[-2], stack[-1], points[i]):
            stack.pop()

        stack.append(points[i])

    return stack

def is_counter_clockwise(p1, p2, p3):
    cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return cross_product > 0

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    points = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    
    polygon = graham_scan(points)
    print(len(polygon))

    for i in range(len(polygon)):
        print(polygon[i][0], polygon[i][1], sep=' ')