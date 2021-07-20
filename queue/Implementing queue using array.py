class Queue:
    def __init__(self):
        self.list = []
        self.start = -1
        self.end = -1
    def enqueue(self,data):
        if self.start == -1:
            self.start += 1
            self.end +=1
            self.list.append(data)
        else:
            self.end += 1
            self.list.append(data)
    def dequeue(self):
        if self.start == -1 or self.start > self.end:
            return -1
        else:
            self.start += 1



    def isEmpty(self):
        if self.start == -1 or self.start >self.end:
            return True
        return False

    def size(self):
        if self.start == -1 or self.start > self.end:
            return 0
        else:
            return (self.end - self.start + 1)
    def print_queue(self):
        print(self.list[self.start:self.end + 1:1])


# q = Queue()
# q.enqueue(5)
# q.enqueue(4)
# print(q.start,q.end)
# q.enqueue(5)
# print(q.start,q.end)
# q.enqueue(6)
# print(q.size())
# print(q.start,q.end)
# q.print_queue()
# q.dequeue()
# print(q.size())
# q.print_queue()
# q.dequeue()
# print(q.isEmpty())
# q.print_queue()
# q.dequeue()
# q.print_queue()
# print(q.isEmpty())
# q.dequeue()
# q.print_queue()
# print(q.isEmpty())

