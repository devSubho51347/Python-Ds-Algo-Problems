class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Queue:

    def __init__(self):
        self.start = None

        self.head = None
        self.next_node = None

    # Operation to insert an element
    def enqueue(self, data):
        node = Node(data)

        if self.start is None:
            self.head = node
            self.next_node = node
            self.head.next = None
            self.start = self.head
            return

        self.next_node.next = node
        self.next_node = node


    # Operation to remove element from start, just move the pointer by one step
    def dequeue(self):
        if self.head is None:
            return -1
        self.head = self.head.next

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def size(self):
        if self.head is None:
            print(0)
        head2 = self.head
        count = 0
        while head2 is not None:
            count = count + 1
            head2 = head2.next
        print(count)


    def print_queue(self):
        head2 = self.head
        while head2 is not None:
            print(head2.data, end = " ")
            head2 = head2.next
        print()



q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.print_queue()
q.dequeue()
q.print_queue()
q.dequeue()
q.print_queue()





