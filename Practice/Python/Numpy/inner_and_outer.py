"""
Question:

inner:
    The inner tool returns the inner product of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.inner(A, B)     #Output : 4

outer:
    The outer tool returns the outer product of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.outer(A, B)     #Output : [[0 0]
                                #          [3 4]]

Task:
    You are given two arrays: A and B.
    Your task is to compute their inner and outer product.

Input Format:
    * The first line contains the space separated elements of array A.
    * The second line contains the space separated elements of array B.

Output Format:
    First, print the inner product.
    Second, print the outer product.

Sample Input:
    0 1
    2 3

Sample Output:
    3
    [[0 0]
     [2 3]]
"""

# Solution:

import numpy

nparr_a = numpy.array(list(map(int, input().strip().split())))

nparr_b = numpy.array(list(map(int, input().strip().split())))

print(numpy.inner(nparr_a, nparr_b))

print(numpy.outer(nparr_a, nparr_b))
