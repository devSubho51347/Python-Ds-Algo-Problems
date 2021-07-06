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


def insert_node(head,newNode,i):
    if i == 1:
        tail = head.next
        head.next = newNode
        newNode.next = tail
        return

    else:
        insert_node(head.next,newNode,i-1)


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

## Let us create the node which we want to add and at what position
a = int(input())
index = int(input())
newNode = Node(a)
insert_node(head,newNode,index)
print_linked_list(head)
