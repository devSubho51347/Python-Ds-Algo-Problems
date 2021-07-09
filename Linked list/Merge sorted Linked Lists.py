def merge_linked_list(head1,head2):
    a = None
    b = None
    c = None
    d = None
    if head1.data > head2.data:
        a = head1
        b = head2
        head = head1
        c = head2
        d = head2
    else:
        a = head2
        b = head1
        head = head2
        c = head1
        d = head1

    while c is not None and  a.data > c.data:
        d = c.next
        c.next = a.next
        head.next = c
        c = d
    a = b.next
    while (a is not None) and (c is not None):
        if a.data < c.data:
            b.next = a.next
            a.next = head
            head = a
            a = b.next
        else:
            d = c.next
            c.next = head
            head = c
            c = d

    while a is not None:
        b.next = a.next
        a.next = head
        head = a
        a = b.next

    while d is not None:
        d = c.next
        c.next = head
        head = c
        c = d
    return head


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



# Method to print the linked list
def print_linked_list(head):
    while head is not None:
        if head.next is None:
            print(head.data)
            break
        else:
           print(head.data, end = " ->")
           head = head.next

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
head1 = create_linked_list(arr1)
head2 = create_linked_list(arr2)
print_linked_list(head1)
print_linked_list(head2)
head3 = merge_linked_list(head1,head2)
print_linked_list(head3)





