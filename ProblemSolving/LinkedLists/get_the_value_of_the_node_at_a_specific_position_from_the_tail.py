"""
Question:

You’re given the pointer to the head node of a linked list and a specific
position. Counting backwards from the tail node of the linked list, get the
value of the node at the given position. A position of 0 corresponds to the
tail, 1 corresponds to the node before the tail and so on.

Input Format:
You have to complete the
int getNode(SinglyLinkedListNode* head, int positionFromTail)
method which takes two arguments - the head of the linked list and the position
of the node from the tail. positionFromTail will be at least 0 and less than the
number of nodes in the list. You should NOT read any input from stdin/console.

The first line will contain an integer t, the number of test cases.
Each test case has the following format:
    * The first line contains an integer n, the number of elements in the
      linked list.
    * The next n lines contains, an element each denoting the element of the
      linked list.
    * The last line contains an integer `position_from_tail` denoting the
      position from the tail, whose value needs to be found out and returned.

Constraints:
    * 1 <= t <= 10
    * 1 <= n <= 1000
    * 1 <= listi <= 1000, where listi is the ith element of the linked list.

Output Format:
    Find the node at the given position counting backwards from the tail. Then
    return the data contained in this node. Do NOT print anything to
    stdout/console.

    The code in the editor handles output.
    For each test case, print the value of the node, each in a new line.

Sample Input:
    2
    1
    1
    0
    3
    3
    2
    1
    2

Sample Output:
    1
    3

Explanation:
    In first case, there is one element in linked list with value 1. Hence, last
    element is 1.

    In second case, there are 3 elements with values 3, 2 and 1 (3 -> 2 -> 1).
    Hence, element with position of 2 from tail is 3.
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
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def linked_list_head_pos(head):
    pos = 0
    while head:
        pos += 1
        head = head.next

    return pos - 1


def get_node(head, position_from_tail):
    head_pos = linked_list_head_pos(head)

    while head_pos != position_from_tail:
        head = head.next
        head_pos -= 1

    return head.data


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = get_node(llist.head, position)
