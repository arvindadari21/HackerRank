"""
Question:

Starting with a 1-indexed array of zeros and a list of operations, for each
operation add a value to each of the array element between two given indices,
inclusive. Once all operations have been performed, return the maximum value in
your array.

For example, the length of your array of zeros n = 10. Your list of queries is
as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of k between the indices a and b inclusive:
    index-> 1 2 3 4 5 6 7 8 9 10
    [0,0,0, 0, 0,0,0,0,0, 0]
    [3,3,3, 3, 3,0,0,0,0, 0]
    [3,3,3,10,10,7,7,7,0, 0]
    [3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.

Function Description:
    Complete the function arrayManipulation in the editor below. It must return
    an integer, the maximum value in the resulting array.
    arrayManipulation has the following parameters:
        * n - the number of elements in your array
        * queries - a two dimensional array of queries where each queries[i]
                    contains three integers, a, b, and k.

Input Format:
    * The first line contains two space-separated integers n and m, the size of
      the array and the number of operations.
    * Each of the next m lines contains three space-separated integers a, b and
      k, the left index, right index and summand.

Constraints:
    * 3 <= n <= 10^7
    * 1 <= m <= 2*10^5
    * 1 <= a <= b <= n
    * 0 <= k <= 10^9

Output Format:
    Return the integer maximum value in the finished array.

Sample Input:
    5 3
    1 2 100
    2 5 100
    3 4 100

Sample Output:
    200

Explanation:
    After the first update list will be 100 100 0 0 0 .
    After the second update list will be 100 200 100 100 100 .
    After the third update list will be 100 200 200 200 100 .
    The required answer will be 200.
"""

# Solution:
import datetime


class Limits:
    def __init__(self, low, high, total=None):
        self.low = low
        self.high = high
        self.total = total

    def update_total(self, val):
        if self.total:
            self.total += val
        else:
            self.total = val

    def matches_lower_limit(self, low_limit):
        return self.low == low_limit

    def matches_upper_limit(self, upper_limit):
        return self.high == upper_limit


def yield_queries(queries):
    for query in queries:
        yield query


# Complete the arrayManipulation function below.
def array_manipulation(n, queries):
    limits = []
    for a, b, k in yield_queries(queries):
        pass


# Complete the arrayManipulation function below.
# def array_manipulation(n, queries):
#     counter = {}
#     for a, b, k in yield_queries(queries):
#         for i in range(a, b + 1):
#             try:
#                 counter[i] += k
#             except KeyError:
#                 counter[i] = k
#
#         print(counter)
#
#     max_val = 0
#     for val in counter.values():
#         if val > max_val:
#             max_val = val
#
#     return max_val


if __name__ == '__main__':

    # nm = input("Enter the value of n, m: ").split()

    n = 10000000  # int(nm[0])

    m = 100000  # int(nm[1])

    queries = []

    with open(r'C:\HackerRank\ProblemSolving\Arrays\test.txt', 'r') as f_:
        for data in f_.readlines():
            queries.append(list(map(int, data.rstrip().split())))
            # print("Added data: ", data)

    print("start time: ", datetime.datetime.now())
    result = array_manipulation(n, queries)

    print("Maximum value is: ", result)
    print("end time: ", datetime.datetime.now())
