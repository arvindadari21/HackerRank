"""
Question:

ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of
its employees.
The company has assigned you the task of validating all the randomly generated
UIDs.

A valid UID must follow the rules below:
    * It must contain at least 2 uppercase English alphabet characters.
    * It must contain at least 3 digits (0 - 9).
    * It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
    * No character should repeat.
    * There must be exactly 10 characters in a valid UID.

Input Format
    The first line contains an integer T, the number of test cases.
    The next T lines contains an employee's UID.

Output Format:
    For each test case, print 'Valid' if the UID is valid. Otherwise, print
    'Invalid', on separate lines. Do not print the quotation marks.

Sample Input:
    2
    B1CD102354
    B1CDEF2354

Sample Output:
    Invalid
    Valid

Explanation:
    B1CD102354:  is repeating → Invalid
    B1CDEF2354: Valid
"""


# Solution:

class Validate:
    def __init__(self, uid):
        self.uid = uid

    def has_upper(self):
        # Checks for atleast 2 upper case letters in UID
        count = sum([1 if i.isupper() else 0 for i in self.uid])

        return count >= 2

    def is_valid_length(self):
        # Check if length is 10 characters
        return len(self.uid) == 10

    def is_alpha_numeric(self):
        # Check if alpha-numeric
        return self.uid.isalnum()

    def has_digits(self):
        # Checks for atleast 2 digits in UID
        count = sum([1 if i.isdigit() else 0 for i in self.uid])

        return count >= 3

    def no_repeat(self):
        # Check if no string is repeated
        return len(list(set(self.uid))) == 10

    def is_valid(self):
        # Performs UID validation
        return all([self.has_upper(), self.no_repeat(), self.has_digits(),
                    self.is_alpha_numeric(), self.is_valid_length()])


if __name__ == '__main__':

    for _ in range(int(input())):
        uid = input().strip()
        if Validate(uid).is_valid():
            print('Valid')
        else:
            print('Invalid')
