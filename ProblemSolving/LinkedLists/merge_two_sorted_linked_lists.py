"""
Question:

You’re given the pointer to the head nodes of two sorted linked lists. The data
in both lists will be sorted in ascending order. Change the next pointers to
obtain a single, merged linked list which also has data in ascending order.
Either head pointer given may be null meaning that the corresponding list is
empty.

Input Format:
    You have to complete the
    SinglyLinkedListNode MergeLists(SinglyLinkedListNode headA,
                                    SinglyLinkedListNode headB)
    method which takes two arguments - the heads of the two sorted linked lists
    to merge. You should NOT read any input from stdin/console.

    The input is handled by the code in the editor and the format is as follows:
        * The first line contains an integer t, denoting the number of test
          cases.
        * The format for each test case is as follows:
            * The first line contains an integer n, denoting the length of the
              first linked list.
            * The next n lines contain an integer each, denoting the elements of
              the linked list.
            * The next line contains an integer m, denoting the length of the
              second linked list.
            * The next m lines contain an integer each, denoting the elements of
              the second linked list.

Constraints:
    * 1 <= t <= 10
    * 1 <= n <= 1000
    * 1 <= Listi <= 1000, where Listi is the ith element of the list.

Output Format:
    Change the next pointer of individual nodes so that nodes from both lists
    are merged into a single list. Then return the head of this merged list. Do
    NOT print anything to stdout/console.

    The output is handled by the editor and the format is as follows:
        For each test case, print in a new line, the linked list after merging
        them separated by spaces.

Sample Input:
    1
    3
    1
    2
    3
    2
    3
    4

Sample Output:
    1 2 3 3 4

Explanation:
    The first linked list is: 1 -> 2 -> 3 -> NULL
    The second linked list is: 3 -> 4 -> NULL
    Hence, the merged linked list is: 1 -> 2 -> 3 -> 3 -> 4 -> NULL
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


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def merge_lists(head1, head2):
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    temp = head
    while head1 or head2:
        try:
            if head1.data <= head2.data:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
        except TypeError:
            if head1 is not None:
                temp.next = head1
                head1 = head1.next
            elif head2 is not None:
                temp.next = head2
                head2 = head2.next

        temp = temp.next

    return head


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

        llist3 = merge_lists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
