"""
Question:

You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate
system. You are required to print the angle between the plane made by the
points A, B, C and B, C, D in degrees(not radians). Let the angle be PHI.

Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD.

Here, X, Y means the dot product of X and Y, and AB x BC means the cross
product of vectors AB and BC. Also, AB = B - A.

Input Format:
    One line of input containing the space separated floating number values of
    the X, Y and Z coordinates of a point.

Output Format:
    Output the angle correct up to two decimal places.

Sample Input:
    0 4 5
    1 7 6
    0 5 9
    1 7 2

Sample Output:
    8.19
"""

# Solution:

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        i = self.x - no.x
        j = self.y - no.y
        k = self.z - no.z

        return Points(i, j, k)

    def dot(self, no):
        i = self.x * no.x
        j = self.y * no.y
        k = self.z * no.z

        return i + j + k

    def cross(self, no):
        i = (self.y * no.z) - (self.z * no.y)
        j = (self.x * no.z) - (self.z * no.x)
        k = (self.x * no.y) - (self.y * no.x)

        return Points(i, -j, k)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(
        *points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f".format(math.degrees(angle)))
