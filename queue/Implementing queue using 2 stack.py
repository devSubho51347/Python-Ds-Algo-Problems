class Queue:
    def __init__(self):
        self.li1 = []
        self.li2 = []

    def enqueue(self,data):
        self.li1.append(data)

    def dequeue(self):
        if len(self.li1) == 0:
            return -1
        i = len(self.li1) - 1
        while i > 0:
            self.li2.append(self.li1.pop())
            i = i - 1
        self.li1.pop()
        i = len(self.li2) - 1
        while i >=0:
            self.li1.append(self.li2.pop())
            i = i - 1
    def start(self):
        if len(self.li1) == 0:
            return -1
        return self.li1[0]

    def print_queue(self):
        print(* self.li1)

    def isEmpty(self):
        if len(self.li1) == 0:
            return True
        return False

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
q.dequeue()
q.dequeue()
q.print_queue()
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.print_queue()

