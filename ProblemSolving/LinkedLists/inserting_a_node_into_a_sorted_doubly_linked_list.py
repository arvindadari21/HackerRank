"""
Question:

Given a reference to the head of a doubly-linked list and an integer, data,
create a new DoublyLinkedListNode object having data value data and insert it
into a sorted linked list while maintaining the sort.

Function Description:
    Complete the sortedInsert function in the editor below. It must return a
    reference to the head of your modified DoublyLinkedList.

    sortedInsert has two parameters:
    head: A reference to the head of a doubly-linked list of
          DoublyLinkedListNode objects.
    data: An integer denoting the value of the data field for the
          DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where head = null) and a list with one
element are sorted lists.

Input Format:
    * The first line contains an integer t, the number of test cases.
    Each of the test case is in the following format:
    * The first line contains an integer n, the number of elements in the
      linked list.
    * Each of the next n lines contains an integer, the data for each node of
      the linked list.
    * The last line contains an integer data which needs to be inserted into
      the sorted doubly-linked list.

Constraints:
    * 1 <= t <= 10
    * 1 <= n <= 1000
    * 1 <= DoublyLinkedListNode.data <= 1000

Output Format:
    Do not print anything to stdout. Your method must return a reference to the
    head of the same list that was passed to it as a parameter.

    The ouput is handled by the code in the editor and is as follows:
    For each test case, print the elements of the sorted doubly-linked list
    separated by spaces on a new line.

Sample Input:
    1
    4
    1
    3
    4
    10
    5

Sample Output:
    1 3 4 5 10

Explanation:
    The initial doubly linked list is: 1 <-> 3 <-> 4 <-> 10 <-> NULL.
    The doubly linked list after insertion is: 1 <-> 3 <-> 4 <-> 5 <-> 10 <-> NULL.
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


def sorted_insert(head, data):
    temp_head = head
    new_node = DoublyLinkedListNode(data)

    while temp_head:
        if temp_head is None:
            head = new_node
            return head
        elif data >= temp_head.data and (
                (temp_head.next is None) or (data <= temp_head.next.data)):
            new_node.next = temp_head.next
            temp_head.next = new_node
            new_node.prev = temp_head
            return head
        elif data < temp_head.data:
            new_node.next = temp_head
            head = new_node
            return head
        else:
            temp_head = temp_head.next


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sorted_insert(llist.head, data)

        print_doubly_linked_list(llist1)
