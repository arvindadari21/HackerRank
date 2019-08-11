"""
Question:

You’re given the pointer to the head node of a doubly linked list. Reverse the
order of the nodes in the list. The head node might be NULL to indicate that the
list is empty. Change the next and prev pointers of all the nodes so that the
direction of the list is reversed. Return a reference to the head node of the
reversed list.

Function Description:
Complete the reverse function in the editor below. It should return a reference
to the head of your reversed list.

reverse has the following parameter(s):
    head: a reference to the head of a DoublyLinkedList

Input Format:
    * The first line contains an integer t, the number of test cases.
    Each test case is of the following format:
    * The first line contains an integer n, the number of elements in the
      linked list.
    * The next n lines contain an integer each denoting an element of the
      linked list.

Constraints:
    * 1 <= t <= 10
    * 0 <= n <= 1000
    * 0 <=  DoublyLinkedListNode.data <= 1000

Output Format:
    Return a reference to the head of your reversed list. The provided code will
    print the reverse array as a one line of space-separated integers for each
    test case.

Sample Input:
    1
    4
    1
    2
    3
    4

Sample Output:
    4 3 2 1

Explanation:
    The initial doubly linked list is: 1 <-> 2 <-> 3 <-> 4 <-> NULL
    The reversed doubly linked list is: 4 <-> 3 <-> 2 <-> 1 <-> NULL
"""


# Solution:


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next


def reverse(head):
    swap_node = head
    while head:
        swap_node = head
        nxt = swap_node.next
        swap_node.next = swap_node.prev
        swap_node.prev = nxt

        head = nxt

    return swap_node


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1)
