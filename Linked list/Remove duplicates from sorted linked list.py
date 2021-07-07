class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



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

def print_linked_list(head):
    while head is not None:
        if head.next is None:
            print(head.data)
            break
        else:
           print(head.data, end = " ->")
           head = head.next

def remove_duplicates(head):
    head1 = head
    if head.next is None:
        return head1
    while head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next


arr = [int(x) for x in input().split()]
head = create_linked_list(arr)
print("Initial sorted linked list")
print_linked_list(head)
remove_duplicates(head)
print("Final distinct sorted linked list")
print_linked_list(head)