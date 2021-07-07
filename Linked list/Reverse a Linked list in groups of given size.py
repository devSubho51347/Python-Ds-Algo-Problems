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

def reversed_group(head,k,length):
    i = 1
    li = []
    li.append(head)
    head2 = None
    head1 = None
    tail2 = None
    tail1 = None
    while i <= length:
        head = head.next
        i = i + 1
        if i % k == 1:
            li.append(head)

    for ele in li[::-1]:
        if ele == li[-1]:
            if length % k == 0:
                head2,tail2 = reversed_linked_list(ele,k)

            else:
                head2,tail2 = reversed_linked_list(ele, length % k)

        else:
            head1,tail1 = reversed_linked_list(ele,k)

        if tail1 is not None:
            tail1.next = head2
            head2 = head1

    return head1






def reversed_linked_list(head,counter):
    if counter ==  1:
        return head, head
    head2,tail2 = reversed_linked_list(head.next, counter - 1)
    tail2.next = head
    head.next = None
    return head2,head


arr = [int(x) for x in input().split()]
print("Enter size of group")
k = int(input())
head = create_linked_list(arr)
print_linked_list(head)
length = len(arr)

new_head = reversed_group(head,k,length)
print_linked_list(new_head)