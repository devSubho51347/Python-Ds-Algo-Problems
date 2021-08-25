class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Method to create a new linked list by deleting nodes having greater value on right

def newLinkedList(head, li = []):
    if head is None:
        return
    temp = head
    li.append(head)
    temp = temp.next
    while temp is not None:
        print(temp.data)
        while len(li) > 0 and temp.data > li[-1].data:
            li.pop()
        if len(li) == 0:
            li.append(temp)
            head = temp
        else:
            li[-1].next = temp
            li.append(temp)
        temp = temp.next
    return head


# Method to create a linked list
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

# Method to print a linked list
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
new_head = newLinkedList(head,li = [])
print()
print_linked_list(new_head)
