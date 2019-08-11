"""
Question:

A linked list is said to contain a cycle if any node is visited more than once
while traversing the list.

Complete the function provided for you in your editor. It has one parameter: a
pointer to a Node object named  that points to the head of a linked list. Your
function must return a boolean denoting whether or not there is a cycle in the
list. If there is a cycle, return true; otherwise, return false.

Note: If the list is empty,  will be null.

Input Format:
    Our hidden code checker passes the appropriate argument to your function.
    You are not responsible for reading any input from stdin.

Constraints:
    * 0 <= List size <= 1000

Output Format:
    If the list contains a cycle, your function must return true. If the list
    does not contain a cycle, it must return false. The binary integer
    corresponding to the boolean value returned by your function is printed to
    stdout by our hidden code checker.

Sample Input:
    The following linked lists are passed as arguments to your function:
                 _______
                |   1   |
                |_______|------> Null

                 _______      _______      _______
                |   1   |    |   2   |    |   3   |
                |_______|--->|_______|--->|_______|-----
                                       ^                |
                                       |                |
                                       |________________|

Sample Output:
    0
    1

Explanation:
    * The first list has no cycle, so we return false and the hidden code
      checker prints 0 to stdout.
    * The second list has a cycle, so we return true and the hidden code
      checker prints 1 to stdout.
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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def has_cycle(head):
    visited_nodes = []
    while head:
        if not id(head) in visited_nodes:
            visited_nodes.append(id(head))
        else:
            return 1
        head = head.next

    return 0


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        print(result)
