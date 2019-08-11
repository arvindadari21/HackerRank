"""
Question:

You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height. You can change the height of a stack by removing
and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are
exactly the same height. This means you must remove zero or more cylinders from
the top of zero or more of the three stacks until they're all the same height,
then print the height. The removals must be performed in such a way as to
maximize the height.

Note: An empty stack is still a stack.

Input Format:
The first line contains three space-separated integers, n1, n2, and n3,
describing the respective number of cylinders in stacks 1, 2, and 3. The
subsequent lines describe the respective heights of each cylinder in a
stack from top to bottom:
    * The second line contains n1 space-separated integers describing the
      cylinder heights in stack 1. The first element is the top of the stack.
    * The third line contains n2 space-separated integers describing the
      cylinder heights in stack 2. The first element is the top of the stack.
    * The fourth line contains n3 space-separated integers describing the
      cylinder heights in stack 3. The first element is the top of the stack.

Constraints:
    * 0 < n1, n2, n3 <= 10^5
    * 0 < height of any cylinder <= 100

Output Format:
    Print a single integer denoting the maximum height at which all stacks will
    be of equal height.

Sample Input:
    5 3 4
    3 2 1 1 1
    4 3 2
    1 1 4 1

Sample Output:
    5

Explanation:
    Initially, the stacks look like this:

    initial stacks:     _____
             ____      |     |
            | 3  |     |  4  |
            |____|     |     |       _____
            | 2  |     |_____|      |__1__|
            |____|     |  3  |      |__1__|
            |_1__|     |_____|      |     |
            |_1__|     |  2  |      |__4__|
            |_1__|     |_____|      |__1__|

Observe that the three stacks are not all the same height. To make all stacks of
equal height, we remove the first cylinder from stacks 1 and 2, and then remove
the top two cylinders from stack 3 (shown below).

    modified stacks
                                 _____
     ____                       |     |
    | 3  | <---|          |---->|  4  |
    |____|   __|_         |     |     |              _____
            | 2  |      __|___  |_____| |---------->|__1__|
            |____|     |  3  |          |           |__1__|
            |_1__|     |_____|       ___|_          |_____|
            |_1__|     |  2  |      |__4__|
            |_1__|     |_____|      |__1__|


As a result, the stacks undergo the following change in height:
    1) 8 - 3 = 5
    2) 9 - 4 = 5
    3) 7 - 1 - 1 = 5
    All three stacks now have height = 5. Thus, we print 5 as our answer.
"""


# Solution:

def equal_stacks(h1, h2, h3):
    sum_list = []
    sum_list.extend([sum(h1), sum(h2), sum(h3)])

    while len(set(sum_list)) != 1:
        min_val = min(sum_list)
        # h1
        while sum_list[0] > min_val:
            sum_list[0] -= h1.pop(0)

        # h2
        while sum_list[1] > min_val:
            sum_list[1] -= h2.pop(0)

        # h3
        while sum_list[2] > min_val:
            sum_list[2] -= h3.pop(0)

    return sum_list[0]


if __name__ == '__main__':
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equal_stacks(h1, h2, h3)

    print(result)
