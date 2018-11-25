"""
Question:

Lilah has a string, s, of lowercase English letters that she repeated infinitely
many times.
Given an integer, n, find and print the number of letter a's in the first n
letters of Lilah's infinite string.

For example, if the string s = 'abcac' and n = 10, the substring we consider is
'abcacabcac', the first 10 characters of her infinite string. There are 4
occurrences of a in the substring.

Function Description:
    Complete the repeatedString function in the editor below. It should return
    an integer representing the number of occurrences of a in the prefix of
    length n in the infinitely repeating string.

repeatedString has the following parameter(s):
    s: a string to repeat
    n: the number of characters to consider

Input Format:
    The first line contains a single string, s.
    The second line contains an integer, n.

Constraints:
    * 1 <= |s| <= 100
    * 1 <= n <= 10^12
    * For 25% of the test cases, n <= 10^6

Output Format:
    Print a single integer denoting the number of letter a's in the first n
    letters of the infinite string created by repeating  infinitely many times.

Sample Input:
    aba
    10
Sample Output:
    7
Explanation:
    The first n = 10 letters of the infinite string are abaabaabaa.
    Because there are 7 a's, we print 7 on a new line.
"""

# Solution:

import re


# Complete the repeatedString function below.
def repeated_string(s, n):
    len_of_str = len(s)
    no_of_a_occ = len(re.findall('a', s))
    repeated_len, remaining_len = ((n // len_of_str), (n % len_of_str))

    return (no_of_a_occ * repeated_len) + (
        len(re.findall('a', s[:remaining_len])))


if __name__ == '__main__':
    s = input("Enter the string s: ")

    n = int(input("Enter the number of characters: "))

    result = repeated_string(s, n)

    print("No of a's: ", result)
