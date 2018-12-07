"""
Question:

There is a collection of input strings and a collection of query strings. For
each query string, determine how many times it occurs in the list of input
strings.

For example, given input strings=[ab, ab, abc] and queries=[ab, abc, bc], we
find 2 instances of ab, 1 of abc and 0 of bc. For each query, we add an element
to our return array, results=[2, 1, 0].

Function Description:
    Complete the function matchingStrings in the editor below. The function must
    return an array of integers representing the frequency of occurrence of each
    query string in strings.

    matchingStrings has the following parameters:
        * strings - an array of strings to search
        * queries - an array of query strings

Input Format:
    The first line contains and integer n, the size of strings.
    Each of the next n lines contains a string strings[i].
    The next line contains q, the size of queries.
    Each of the next q lines contains a string queries[i].

Constraints:
    * 1 <= n, q <= 1000
    * 1 <= |strings[i]|, |queries[i]| <= 20.

Output Format:
    Return an integer array of the results of all queries in order.

Sample Input:
    4
    aba
    baba
    aba
    xzxb
    3
    aba
    xzxb
    ab

Sample Output:
    2
    1
    0

Explanation:
    Here, "aba" occurs twice, in the first and third string. The string "xzxb"
    occurs once in the fourth string, and "ab" does not occur at all.
"""

# Solution:

import os


# Complete the matchingStrings function below.
def matching_strings(strings, queries):
    result = []
    for query in queries:
        result.append(sum([1 for string in strings if string == query]))

    return result


if __name__ == '__main__':
    strings_count = int(input("Enter the strings count: "))

    strings = []

    for _ in range(strings_count):
        strings_item = input("Enter the string: ")
        strings.append(strings_item)

    queries_count = int(input("Enter the queries count: "))

    queries = []

    for _ in range(queries_count):
        queries_item = input("Enter the query: ")
        queries.append(queries_item)

    res = matching_strings(strings, queries)

    print("Result: ", res)
