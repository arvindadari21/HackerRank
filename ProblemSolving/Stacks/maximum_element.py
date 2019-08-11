"""
Question:

You have an empty sequence, and you will be given N queries. Each query is one
of these three types:
    1 x  -Push the element x into the stack.
    2    -Delete the element present at the top of the stack.
    3    -Print the maximum element in the stack.

Input Format
    The first line of input contains an integer, N. The next N lines each
    contain an above mentioned query. (It is guaranteed that each query is
    valid.)

Constraints:
    * 1 <= N <= 10^5
    * 1 <= x <= 10^9
    * 1 <= type <= 3

Output Format:
    For each type 3 query, print the maximum element in the stack on a new line.

Sample Input:
    10
    1 97
    2
    1 20
    2
    1 26
    1 20
    2
    3
    1 91
    3

Sample Output:
    26
    91
"""


# Solution:

class Stack:
    def __init__(self):
        self._stack = list()
        self.max = 0

    def set_max(self):
        self.max = max(self._stack) if self._stack else 0

    def push(self, data):
        self._stack.append(data)
        if data > self.max:
            self.max = data

    def pop(self):
        self._stack.pop()
        self.set_max()

    def max_ele(self):
        return self.max


if __name__ == '__main__':
    _stack = Stack()

    no_of_tests = int(input())
    for _ in range(no_of_tests):
        options = input()
        try:
            choice, value = options.split()
        except ValueError:
            choice = options
            value = None

        if int(choice) == 1:
            _stack.push(int(value))
        elif int(choice) == 2:
            _stack.pop()
        elif int(choice) == 3:
            print(_stack.max_ele())
