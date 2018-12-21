"""
Question:

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
    * Both players are given the same string, S.
    * Both players have to make substrings using the letters of the string S.
    * Stuart has to make words starting with consonants.
    * Kevin has to make words starting with vowels.
    * The game ends when both players have made all possible substrings.

Scoring:
    A player gets +1 point for each occurrence of the substring in the string S.

For Example:
    String  = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
                        B A N A N A
                STUART                  KEVIN
            Words   Score           Words   Score
              B       1               A       3
              N       2              AN       2
             BA       1              ANA      2
             NA       2              ANAN     1
            BAN       1             ANANA     1
            NAN       1
            BANA      1
            NANA      1
           BANAN      1
           BANANA     1

        Total         12                      9

Your task is to determine the winner of the game and their score.

Input Format:
    A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
    0 < len(S) <= 10^6

Output Format:
    Print one line: the name of the winner and their score separated by a space.
    If the game is a draw, print Draw.

Sample Input:
    BANANA

Sample Output:
    Stuart 12

Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""

# Solution:

# -------------------------- Broad solution ------------------------------------
# This fails if string size is very large (Eg: 10^6)
import re

VOVELS = list('AEIOU')
CONSONENTS = list(set(chr(i) for i in range(65, 91)) - set(VOVELS))


def find_sub_str_count(sub, string):
    return len(re.findall(f'(?={sub})', string))


def sub_strings(condition, s):
    sub_strs = []
    s_len = len(s)
    for i in range(s_len):
        for j in range(s_len - i):
            t = s[j: j + i + 1]
            if (t[0] in condition) and (not t in sub_strs):
                sub_strs.append(t)
                yield t


def get_count(condition, s):
    count = 0
    for sub in sub_strings(condition, s):
        count += find_sub_str_count(sub, s)

    return count


def minion_game_1(string):
    stuart = get_count(CONSONENTS, string)

    kevin = get_count(VOVELS, string)

    print(f'Stuart {stuart}' if stuart > kevin else f'Kevin {kevin}')


# ------------------------------------ End -------------------------------------


# Working solution without constraint failure:

def minion_game(string):
    n = len(string)
    kevin = 0
    stuart = 0
    for i in range(n):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)


if __name__ == '__main__':
    s = input("Enter the string: ")
    minion_game(s)
