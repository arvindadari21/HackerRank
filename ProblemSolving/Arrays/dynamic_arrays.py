"""
Question:

* Create a list, seq_list, of n empty sequences, where each sequence is indexed
  from 0 to n-1. The elements within each of the n sequences also use 0-indexing.

* Create an integer, last_answer, and initialize it to .

* The types of queries that can be performed on your list of sequences
  (seq_list) are described below:
    1. Query: 1 x y
        1. Find the sequence, seq, at index ((x ^ last_answer)%n) in seq_list.
        2. Append integer y to sequence seq.
    2. Query: 2 x y
        1. Find the sequence, seq, at index ((x ^ last_answer)%n) in seq_list.
        2. Find the value of element (y % size) in seq (where is the size of seq)
           and assign it to last_answer.
        3. Print the new value of last_answer on a new line.
Task:
    Given N, Q, and Q queries, execute each query.

Note: bitwise XOR operation, which corresponds to the ^ operator in most
      languages.

Input Format:
    The first line contains two space-separated integers, N
    (the number of sequences) and Q(the number of queries), respectively.
    Each of the Q subsequent lines contains a query in the format defined above.

Constraints:
    * 1 <= N, Q <= 10^5
    * 0 <= x <= 10^9
    * 0 <= y <= 10^9
    * It is guaranteed that query type 2 will never query an empty sequence
      or index.

Output Format:
    For each type 2 query, print the updated value of last_answer on a new line.

Sample Input:
    2 5
    1 0 5
    1 1 7
    1 0 3
    2 1 0
    2 1 1
Sample Output:
    7
    3
Explanation:
    Initial Values:
    N = 2
    last_answer = 0
    S0 = [ ]
    S1 = [ ]
    Query 0: Append to sequence ((0^0)%2) = 0.
    last_answer = 0
    S0 = [5]
    S1 = [ ]
    Query 1: Append to sequence ((1^0)%2) = 1.
    last_answer = 0
    S0 = [5]
    S1 = [7]
    Query 2: Append to sequence ((0^0)%2) = 0.
    last_answer = 0
    S0 = [5, 3]
    S1 = [7]
    Query 3: Assign the value at index of sequence ((1^0)%2) = 1 to last_answer,
             print last_answer.
    last_answer = 7
    S0 = [5, 3]
    S1 = [7]
    7   (print)
    Query 4: Assign the value at index of sequence ((1^7)%2) = 0 to last_answer,
             print last_answer.
    S0 = [5, 3]
    S1 = [7]
    3   (print)
"""


# Solution:

# Complete the dynamicArray function below.
def dynamic_array(n, queries):
    seqList = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for query, x, y in queries:
        index = (x ^ last_answer) % n
        seq = seqList[index]
        if query == 1:
            seq.append(y)
        else:
            ls_index = y % len(seq)
            last_answer = seq[ls_index]
            result.append(last_answer)

    return result


if __name__ == '__main__':
    nq = input("Enter the values for N, Q: ").rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input("Enter the query: ").rstrip().split())))

    result = dynamic_array(n, queries)

    print(result)
