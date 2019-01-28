"""
Question:

You are given a string S.
S contains alphanumeric characters only.
GINORTS Your task is to sort the string S in the following manner:
    * All sorted lowercase letters are ahead of uppercase letters.
    * All sorted uppercase letters are ahead of digits.
    * All sorted odd digits are ahead of sorted even digits.

Input Format:
    A single line of input contains the string S.

Constraints:
    * 0 < len(S) < 1000

Output Format:
    Output the sorted string S.

Sample Input:
    Sorting1234

Sample Output:
    ginortS1324
"""

# Solution:

s = input().strip()

lower = ''.join(sorted([i for i in s if i.islower()]))
upper = ''.join(sorted([i for i in s if i.isupper()]))
digit = [i for i in s if i.isdigit()]

odd = ''.join(sorted([i for i in digit if int(i) % 2 != 0]))
even = ''.join(sorted([i for i in digit if int(i) % 2 == 0]))

print(lower + upper + odd + even)
