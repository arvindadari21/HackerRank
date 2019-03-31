"""
Question:

You’re given the pointer to the head nodes of two linked lists. Compare the data
in the nodes of the linked lists to check if they are equal. The lists are equal
only if they have the same number of nodes and corresponding nodes contain the
same data. Either head pointer given may be null meaning that the corresponding
list is empty.

Input Format:
    You have to complete the int CompareLists(Node* headA, Node* headB) method
    which takes two arguments - the heads of the two linked lists to compare.
    You should NOT read any input from stdin/console.

    The input is handled by the code in the editor and the format is as follows:
        The first line contains t, the number of test cases. The format for
        each test case is as follows:
            * The first line contains an integer n, denoting the number of
              elements in the first linked list.
            * The next n lines contain an integer each, denoting the elements of
              the first linked list.
            * The next line contains an integer m, denoting the number of
              elements in the second linked list.
            * The next m lines contain an integer each, denoting the elements
              of the second linked list.

Constraints:
    * 1 <= t <= 10
    * 1 <= n <= 1000
    * 1 <= Listi <= 1000, where Listi is the ith element in the list.

Output Format:
    Compare the two linked lists and return 1 if the lists are equal. Otherwise,
    return 0. Do NOT print anything to stdout/console.

    The output is handled by the code in the editor and it is as follows:
        For each test case, in a new line, print 1 if the two lists are equal,
        else print 0.

Sample Input:
    2
    2
    1
    2
    1
    1
    2
    1
    2
    2
    1
    2

Sample Output:
    0
    1

Explanation:
    In the first case, linked lists are: 1 -> 2 -> NULL and 1 -> NULL
    In the second case, linked lists are: 1 -> 2 -> NULL and 1 -> 2 -> NULL
"""


# Solution:


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=' ')

        node = node.next

        if node:
            print(sep)


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    equal = 0
    try:
        if llist1.next is not None or llist2.next is not None:
            equal = compare_lists(llist1.next, llist2.next)
        else:
            equal = 1 if llist1.data == llist2.data else 0
    except AttributeError:
        equal = 0

    return equal


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        print(result)
