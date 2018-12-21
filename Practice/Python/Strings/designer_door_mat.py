"""
Question:

Mr. Vincent works in a door mat manufacturing company. One day, he designed a
new door mat with the following specifications:

* Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

Sample Designs:

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format:
    A single line containing the space separated values of N and M.

Constraints:
    * 5 < N < 101
    * 15 < M < 303

Output Format:
    Output the design pattern.

Sample Input:
    9 27

Sample Output:

    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------
"""


# Solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

def design(n, m):
    pattern = '.|.'
    welcome = 'WELCOME'
    center = n // 2

    for i in range(n):
        # Top design
        if i < center:
            temp = (2*i + 1) * pattern
            print(temp.center(m, '-'))
        # Welcome message
        elif i == center:
            print(welcome.center(m, '-'))
        # Bottom design
        else:
            temp = (2 * (2*center - i) + 1) * pattern
            print(temp.center(m, '-'))


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    design(N, M)
