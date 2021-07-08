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


def sort_even_odds(head):
    first_odd_node = None
    prev_even_node = None
    head1 = head
    if head.next is None:
        return head
    if head1.data % 2 != 0:
        first_odd_node = head1
    prev = None
    current = None
    while head.next is not None:
        prev = head
        current = prev.next

        if (current.data % 2 != 0) and (prev.data % 2 == 0):
            prev_even_node = prev
            first_odd_node = current
            head = head.next
        elif (prev.data % 2 != 0) and (current.data % 2 == 0):
            if head1.data % 2 != 0:
                prev.next = current.next
                current.next = first_odd_node
                head1 = current
                prev_even_node = current

            else:
                prev.next = current.next
                current.next = first_odd_node
                prev_even_node.next = current
                prev_even_node = current

        else:
            head = head.next
    return head1

arr = [int(x) for x in input().split()]
head = create_linked_list(arr)
print_linked_list(head)
new_head = sort_even_odds(head)
print("Even and Odd Linked List")
print_linked_list(new_head)