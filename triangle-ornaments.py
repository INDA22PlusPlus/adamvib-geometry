# https://kth.kattis.com/problems/triangleornaments

import math
import sys


def main():
    number_of_triangles = int(sys.stdin.readline())

    length = 0.0

    for _ in range(number_of_triangles):
        a, b, c = map(int, sys.stdin.readline().split())
 
        bc = math.acos((a**2 - b**2 - c**2) / -(2 * b * c))
        h = math.sqrt(b**2 + (c/2)**2 - 2 * b * (c/2) * math.cos(bc))

        left_angle = math.acos((h**2 + a**2 - (c/2)**2) / (2 * h * a))
        right_angle = math.acos((h**2 + b**2 - (c/2)**2) / (2 * h * b))

        length += b * math.cos(math.pi / 2 - right_angle)
        length += a * math.cos(math.pi / 2 - left_angle)
    
    print(length)

if __name__ == '__main__':
    main()