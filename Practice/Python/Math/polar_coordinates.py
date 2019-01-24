"""
Question:

Polar coordinates are an alternative way of representing Cartesian coordinates
or Complex Numbers.

A complex number z = x + yi

is completely determined by its real part x and imaginary part y.
Here, j is the imaginary unit.

A polar coordinate (r, @)

is completely determined by modulus r and phase angle @.

If we convert complex number r to its polar coordinate, we find:
r: Distance from  to origin, i.e.,
@: Counter clockwise angle measured from the positive -axis to the line segment
   that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex
numbers.

cmath.phase

    This tool returns the phase of complex number z(also known as the argument
    of z).

    >>> phase(complex(-1.0, 0.0))
    3.1415926535897931

abs

    This tool returns the modulus (absolute value) of complex number .

    >>> abs(complex(-1.0, 0.0))
    1.0

Task
    You are given a complex z. Your task is to convert it to polar coordinates.

Input Format:
    A single line containing the complex number z. Note: complex() function can
    be used in python to convert the input as a complex number.

Constraints:
    Given number is a valid complex number

Output Format:
    Output two lines:
        The first line should contain the value of r.
        The second line should contain the value of @.

Sample Input:
    1+2j

Sample Output:
    2.23606797749979
    1.1071487177940904
    Note: The output should be correct up to 3 decimal places.
"""

# Solution:

from cmath import phase

comp = input().strip()

print('{:.03f}'.format(abs(complex(comp))))
print('{:.03f}'.format(phase(complex(comp))))
