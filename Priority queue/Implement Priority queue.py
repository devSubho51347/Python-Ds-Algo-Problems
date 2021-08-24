class priorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class priorityQueue:
    def __init__(self):
        self.pq = []


    def isEmpty(self):
        if self.getSize() == 0:
            return True
        return False

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele

# Method to insert values in the priority queue
    def insert(self,value,priority):
        Node = priorityQueueNode(value,priority)
        self.pq.append(Node)
        length = self.getSize()
        index = length - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.pq[parent_index].priority > self.pq[index].priority:
                if index % 2 == 0:
                    if self.pq[index].priority < self.pq[index - 1].priority:
                        self.pq[index],self.pq[parent_index] = self.pq[parent_index],self.pq[index]
                    else:
                        self.pq[index - 1], self.pq[parent_index] = self.pq[parent_index], self.pq[index - 1]
                else:
                    self.pq[index], self.pq[parent_index] = self.pq[parent_index], self.pq[index]
            else:
                break
            index = parent_index

#Method to remove minimum element from priority queue
    def removeMinHelper(self):
        self.pq[0],self.pq[self.getSize() - 1] = self.pq[self.getSize() - 1],self.pq[0]
        self.pq.pop()

    def removeMin(self):
        i = 0
        self.removeMinHelper()
        length = self.getSize() - 1
        while i < self.getSize()  - 1:
            if 2*i + 2 <= length:
                if self.pq[i].priority > min(self.pq[2*i + 1].priority,self.pq[2*i + 2].priority):
                    if self.pq[2*i + 1].priority < self.pq[2*i + 2].priority:
                        self.pq[2 * i + 1],self.pq[i] = self.pq[i],self.pq[2*i + 1]
                        i = 2*i + 1
                    else:
                        self.pq[2 * i + 2], self.pq[i] = self.pq[i], self.pq[2 * i + 2]
                        i = 2*i + 2
                else:
                    break


            elif 2*i + 1 <= length:
                if self.pq[i].priority > self.pq[2*i + 1].priority:
                    self.pq[2 * i + 1], self.pq[i] = self.pq[i], self.pq[2 * i + 1]
                    i = 2*i + 1
                else:
                    break

            else:
                break



    def print(self):
        for ele in self.pq:
            print(ele.priority, end = ",")
    def clean(self):
        self.pq = []


# p1 = priorityQueueNode(3,3)
# p2 = priorityQueueNode(3,3)
# p3 = priorityQueueNode(3,3)
# p4 = priorityQueueNode(3,3)
# p5 = priorityQueueNode(3,3)

q = priorityQueue()
# q.insert(3,3)
# q.insert(2,2)
# q.insert(5,5)
#
# q.insert(1,1)
# q.insert(4,4)
# q.insert(9,9)
# q.insert(15,15)
# q.insert(3,3)
# q.insert(2,2)
# q.insert(6,6)
# q.insert(3,3)
q.insert(3,3)
q.insert(6,6)
q.insert(9,9)
q.insert(4,4)
q.insert(2,2)
# q.insert(4,4)
# q.insert(2,2)
q.print()
q.removeMin()
print()
q.print()
# q.print()