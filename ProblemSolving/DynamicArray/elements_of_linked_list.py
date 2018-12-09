"""
Question:

* Print the Elements of a Linked List

Given a pointer to the head node of a linked list, print its elements in order,
one element per line. If the head pointer is null (indicating
the list is empty), don’t print anything.

Input Format:
    The first line of input contains n, the number of elements in the linked
    list. The next n lines contain one element each, which are the elements of
    the linked list.

Note: Do not read any input from stdin/console. Complete the printLinkedList
      function in the editor below.

Constraints:
    * 1 <= n <= 1000
    * 1 <= listi <= 1000; where listi is the ith element of the linked list.

Output Format:
    Print the integer data for each element of the linked list to stdout/console
    (e.g.: using printf, cout, etc.). There should be one element per line.
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


# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def print_linked_list(head):
    while head is not None:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    llist_count = int(input("Enter the length of linked list: "))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter the elements of linked list: "))
        llist.insert_node(llist_item)

    print_linked_list(llist.head)
