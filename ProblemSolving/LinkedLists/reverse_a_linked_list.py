"""
Question:

You’re given the pointer to the head node of a linked list. Change the next
pointers of the nodes so that their order is reversed. The head pointer given
may be null meaning that the initial list is empty.

Input Format:
    You have to complete the SinglyLinkedListNode reverse(SinglyLinkedListNode
    head) method which takes one argument - the head of the linked list. You
    should NOT read any input from stdin/console.

    The input is handled by the code in the editor and the format is as follows:

    * The first line contains an integer t, denoting the number of test cases.
    * Each test case is of the following format:
        * The first line contains an integer n, denoting the number of elements
          in the linked list.
        * The next n lines contain an integer each, denoting the elements of
          the linked list.

Constraints:
    * 1 <= t <= 10
    * 1 <= n <= 1000
    * 1 <= Listi <= 1000, where Listi is the ith element in the list.

Output Format:
    Change the next pointers of the nodes that their order is reversed and
    return the head of the reversed linked list. Do NOT print anything to
    stdout/console.

    The output is handled by the code in the editor. The output format is as
    follows:
        For each test case, print in a new line the elements of the linked list
        after reversing it, separated by spaces.

Sample Input:
    1
    5
    1
    2
    3
    4
    5

Sample Output:
    5 4 3 2 1

Explanation:
    The initial linked list is: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

    The reversed linked list is: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
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
            print(sep, end=' ')


# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    prev = head
    curr = head.next

    if curr.next is not None:
        head = reverse(curr)
    else:
        head = curr

    curr.next = prev
    prev.next = None
    return head


if __name__ == '__main__':

    tests = int(input("No of test cases: "))

    for tests_itr in range(tests):
        llist_count = int(input("No of elements in list: "))

        llist = SinglyLinkedList()

        print("Enter list elements: ")
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        print("Reverse order of linked list is: ")
        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ')
