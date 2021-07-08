# Description
'''
You have been given a singly linked list of integer
 along with an integer 'N'. Write a function to append the last 'N'
 nodes towards the front of the singly linked list and returns
 the new head to the list.
'''
# Solved question using two pointer approach
def AppendLastToFirst(head,n):
    ptr1 = head
    ptr2 = head
    head1 = head
    head2 = head
    while head.next is not None:
        if n > 0:
            ptr1 = head.next
            head = head.next
            n = n - 1
        elif n == 0:
               ptr1 = head.next
               ptr2 = head1.next
               head = head.next
               head1 = head1.next
    if n > 0:
        return head2

    ptr1.next = head2
    head = ptr2.next
    ptr2.next = None
    return head

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Method to create the linked list
def create_linked_list(arr):
    head = None
    tail = None

    for ele in arr:
        newNode = Node(ele)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

    return head




# Method to print the linked list
def print_linked_list(head):
    while head is not None:
        if head.next is None:
            print(head.data)
            break
        else:
           print(head.data, end = " ->")
           head = head.next




arr = [int(x) for x in input().split()]
n = int(input())
head = create_linked_list(arr)
print_linked_list(head)
print("New Linked List")
new_head = AppendLastToFirst(head,n)
print_linked_list(new_head)
