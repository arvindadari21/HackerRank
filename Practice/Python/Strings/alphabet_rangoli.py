"""
Question:

You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----

#size 5
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------

#size 10
    ------------------j------------------
    ----------------j-i-j----------------
    --------------j-i-h-i-j--------------
    ------------j-i-h-g-h-i-j------------
    ----------j-i-h-g-f-g-h-i-j----------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ----------j-i-h-g-f-g-h-i-j----------
    ------------j-i-h-g-h-i-j------------
    --------------j-i-h-i-j--------------
    ----------------j-i-j----------------
    ------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has
the Nth alphabet letter (in alphabetical order).

Input Format:
    Only one line of input containing N, the size of the rangoli.

Constraints:
    * 0 < N < 27

Output Format:
    Print the alphabet rangoli in the format explained above.

Sample Input:
    5

Sample Output:
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
"""


# Solution:

def print_rangoli(size):
    # your code goes here
    sep = '-'
    total_len = (size * 4) - 3
    center = (2 * size)//2

    k = 1
    for i in range(1, 2 * size):
        s_ascii = ord('a') + size
        t_center = k // 2
        text = []
        # Top design
        if i < center:
            for j in range(k):
                s_ascii += -1 if j <= t_center else 1
                text.append(chr(s_ascii))
            k += 2
        # Center design
        elif i == center:
            for j in range(k):
                s_ascii += -1 if j <= t_center else 1
                text.append(chr(s_ascii))
            k -= 2
        # Bottom design
        else:
            for j in range(k):
                s_ascii += -1 if j <= t_center else 1
                text.append(chr(s_ascii))
            k -= 2
        design = '-'.join(text)
        print(design.center(total_len, sep))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
