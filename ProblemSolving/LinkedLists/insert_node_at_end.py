"""
Question:

You are given the pointer to the head node of a linked list and an integer to
add to the list. Create a new node with the given integer. Insert this node at
the tail of the linked list and return the head node of the linked list formed
after inserting this new node. The given head pointer may be null, meaning that
the initial list is empty.

Input Format
You have to complete the SinglyLinkedListNode
insert_at_tail(SinglyLinkedListNode head, int data) method. It takes two
arguments: the head of the linked list and the integer to insert at tail.
You should not read any input from the stdin/console.

The input is handled by code editor and is as follows:
    * The first line contains an integer n, denoting the elements of the linked
      list.
    * The next n lines contain an integer each, denoting the element that needs
      to be inserted at tail.

Constraints:
    * 1 <= n <= 1000
    * 1 <= ;isti <= 1000

Output Format:
    Insert the new node at the tail and just return the head of the updated
    linked list. Do not print anything to stdout/console.

The output is handled by code in the editor and is as follows:
    Print the elements of the linked list from head to tail, each in a new line.

Sample Input:
    5
    141
    302
    164
    530
    474
Sample Output:
    141
    302
    164
    530
    474
Explanation:
    First the linked list is NULL. After inserting 141, the list is 141 -> NULL.
    After inserting 302, the list is 141 -> 302 -> NULL.
    After inserting 164, the list is 141 -> 302 -> 164 -> NULL.
    After inserting 530, the list is 141 -> 302 -> 164 -> 530 -> NULL. After
     inserting 474, the list is 141 -> 302 -> 164 -> 530 -> 474 -> NULL, which
     is the final list.
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


def print_singly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next

        if node:
            print(sep)


# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insert_node_at_tail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
    else:
        temp = head
        while temp.next:
            temp = temp.next

        temp.next = node

    return head


# ------------------------------------------------------------------------ #
# Recursive method fails in Python with error: "Recursion depth exceeded"  #
# So, recursion is not really recommended in python.                       #
# ------------------------------------------------------------------------ #
def insert_node_at_tail_revursive(head, data):
    if not head:
        return SinglyLinkedListNode(data)
    else:
        if head.next:
            insert_node_at_tail(head.next, data)
        else:
            head.next = SinglyLinkedListNode(data)

        return head
# ------------------------------------------------------------------------ #


if __name__ == '__main__':

    llist_count = int(input("Enter the length of linked list: "))

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input("Enter the linked list node data: "))
        llist_head = insert_node_at_tail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
