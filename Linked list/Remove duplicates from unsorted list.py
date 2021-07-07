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

#   Method 1 to remove duplicates
def removeDuplicates1(head):
    # code here
    # return head after editing list
    head1 = head
    if head.next is None:
        return head
    dict = {}
    dict[head.data] = dict.get(head.data, 0) + 1
    while head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next

        elif head.data != head.next.data:

            dict[head.next.data] = dict.get(head.next.data, 0) + 1

            if dict[head.next.data] > 1:
                head.next = head.next.next
            else:
                head = head.next

# Method no 2 to remove duplicates
def removeDuplicates2(self, head):
        # code here
        # return head after editing list
        uniq = set()

        node = head

        while node.next is not None:
            uniq.add(node.data)
            if node.next.data in uniq:
                node.next = node.next.next
            else:
                node = node.next
        return head


arr = [int(x) for x in input().split()]
head = create_linked_list(arr)
print("Initial unsorted linked list")
print_linked_list(head)
removeDuplicates1(head)
print("Final distinct unsorted linked list")
print_linked_list(head)