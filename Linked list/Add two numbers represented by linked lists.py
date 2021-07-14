class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def add_nodes(head1,head2,n,m):
    while n > m:
        newNode = Node(0)
        newNode.next = head2
        head2 = newNode
        m = m + 1
    while m > n:
        newNode = Node(0)
        newNode.next = head1
        head1 = newNode
        n = n + 1
    return head1,head2




def add_two_linked_lists(head1,head2,n,m):
    if n != m:
        head1,head2 = add_nodes(head1,head2,n,m)
        n = m
    if head1.next is None and head2.next is None:
        sum = head1.data + head2.data
        if sum > 9:
            head1.data = sum % 10
            carry = 1
        else:
            head1.data = sum
            carry = 0
        return head1,carry
    data,carry = add_two_linked_lists(head1.next,head2.next,n,m)
    sum = head1.data + head2.data + carry
    if sum > 9:
        head1.data = sum % 10
        carry = 1
    else:
        head1.data = sum
        carry = 0
    return head1,carry



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

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]
head1 = create_linked_list(arr1)
print_linked_list(head1)
head2 = create_linked_list(arr2)
print_linked_list(head2)
final_head = add_two_linked_lists(head1,head2,n,m)[0]
print_linked_list(final_head)




