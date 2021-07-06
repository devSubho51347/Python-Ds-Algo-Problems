## Creation of a node of linked list

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

# Method to reverse the linked list
def reverse_linked_list(head):
    if head.next is None:
        return head,head
    head1,tail1 = reverse_linked_list(head.next)
    tail1.next = head
    head.next = None
    return head1,head

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
head = create_linked_list(arr)
print_linked_list(head)
new_head, new_tail = reverse_linked_list(head)
print("Head of reversed Linked list is {}".format(new_head.data))
print("Tail of reversed Linked list is {}".format(new_tail.data))
print("Reversed Linked List")
print_linked_list(new_head)