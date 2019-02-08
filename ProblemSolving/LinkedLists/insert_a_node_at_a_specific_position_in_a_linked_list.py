"""
Question:

You’re given the pointer to the head node of a linked list, an integer to add to
the list and the position at which the integer must be inserted. Create a new
node with the given integer, insert this node at the desired position and return
the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the
head and so on. The head pointer given may be null meaning that the initial list
is empty.

As an example, if your list starts as 1 -> 2 -> 3 and you want to insert a node
at position 2 with data = 4, your new list should be 1 -> 2 -> 4 -> 3

Function Description:
    Complete the function insertNodeAtPosition in the editor below. It must
    return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:
    * head: a SinglyLinkedListNode pointer to the head of the list
    * data: an integer value to insert as data in your new node
    * position: an integer position to insert the new node, zero based indexing

Input Format:
    * The first line contains an integer n, the number of elements in the linked
      list.
    * Each of the next n lines contains an integer SinglyLinkedListNode[i].data.
    * The last line contains an integer position.

Constraints:
    * 1 <= n <= 1000
    * 1 <= SingleLinkedListNode[i].data <= 1000; where SingleLinkedListNode[i]
      is the ith element of the linked list.
    * 0 <= position <= n.

Output Format:
    Return a reference to the list head. Locked code prints the list for you.

Sample Input:
    3
    16
    13
    7
    1
    2
Sample Output:
    16 13 1 7

Explanation:
    The initial linked list is 16 13 7. We have to insert 1 at the position 2
    which currently has 7 in it. The updated linked list will be 16 13 1 7
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
        print(node.data)

        node = node.next

        if node:
            print(sep)


# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insert_node_at_position(head, data, position):
    current_position = 0
    temp = head
    prev = temp
    while current_position != position:
        prev = temp
        temp = temp.next
        current_position += 1

    node = SinglyLinkedListNode(data)
    prev.next = node
    node.next = temp

    return head


if __name__ == '__main__':

    llist_count = int(input("Enter the legth of linked list: "))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter the element of linked list: "))
        llist.insert_node(llist_item)

    data = int(input("Enter the data to be added in linked list: "))

    position = int(input("Enter the position where is to be added: "))

    llist_head = insert_node_at_position(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')
