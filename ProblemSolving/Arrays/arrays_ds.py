"""
Question:

An array is a type of data structure that stores elements of the same type in
a contiguous block of memory. In an array, A, of size N, each memory location
has some unique index, i(where 0 <= i <= N), that can be referenced as
A[i] (you may also see it written as Ai).

Given an array, A, of N integers, print each element in reverse order as a
single line of space-separated integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge,
you may want to skip this.

Input Format:
    The first line contains an integer, (the number of integers in ).
    The second line contains space-separated integers describing .
Constraints:
    * 1 <= N <= 10^3
    * 1 <= Ai <= 10^4, where Ai is the ith integer in A.
Output Format:
    Print all integers in in reverse order as a single line of space-separated
    integers.
Sample Input:
    4
    1 4 3 2
Sample Output:
    2 3 4 1
"""


# Solution:

# Reversing using recursion
def reverse_array_recursion(a):
    try:
        char = a[0]
        reverse_array_recursion(a[1:])
        print(char, end=' ')
    except IndexError:
        return


# Complete the reverseArray function below.
def reverse_array(a):
    return a[::-1]


if __name__ == '__main__':
    arr_count = int(input("Enter the array count: "))

    arr = list(map(int, input("Enter the array elements: ").rstrip().split()))

    res = reverse_array(arr)

    # Reversing using recursion
    reverse_array_recursion(arr)

    print("Reverse order of array is: ", res)
