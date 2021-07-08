# Method to check Circular Linked list

def isCircular(head):
    # Code here
    if head is None:
        return True
    head1 = head
    li = []
    while head.next is not None:
        li.append(head)
        if head.next in li:

            if head.next == head1:
                return True
            else:
                return False

        head = head.next

# Method to create Node of a linked LIST
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Method to create the linked list
def create_circular_linked_list(arr):
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
    tail.next = head
    return head

# Method to create a singly linked list
def create_linked_list(head):
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
           print(head.data, end = "->")
           head = head.next

# Method to print the circular linked list
def print_circular_linked_lsit(head):
    if head is None:
        return
    li = []
    while head is not None:
        li.append(head)
        if head.next not in li:
            print(head.data, end = " ->")
            head = head.next
        elif head.next in li:
            print(head.data, "->")
            for i in range(0,len(li),1):
                if i == 0:
                    print("|", end = "")
                elif i == len(li) - 1:
                    print("|")
                else:
                    print("->->", end = "")
            break


arr = [int(x) for x in input().split()]
print("Press 1 for linked_list and 2 for Circular linked list")
n = int(input())
if n == 1:
    head = create_linked_list(arr)
elif n == 2:
    head = create_circular_linked_list(arr)
if isCircular(head):
    print("Linked list is circular")
    print_circular_linked_lsit(head)
else:
    print("Linked list is not circular")
    print_linked_list(head)