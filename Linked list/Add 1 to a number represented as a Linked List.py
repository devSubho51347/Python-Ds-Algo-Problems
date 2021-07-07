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

# Method to add one to the end of linked list
def addOne(head):
    if head.next is None:
        head.data = head.data + 1
        if head.data == 10:
            head.data = 0
            carry = 1
        else:
            carry = 0
        return carry

    carry = addOne(head.next)
    head.data = head.data + carry
    if head.data == 10:
        head.data = 0
        carry = 1
    return carry


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
print("New linked List after adding 1 to tail")
addOne(head)
print_linked_list(head)