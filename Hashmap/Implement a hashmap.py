class mapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketsize = 10
        self.buckets = [None for i in range(self.bucketsize)]
        self.count = 0

    def size(self):
        return self.count
    # Method to generate index of bucket array
    def hashFunction(self,key):
        self.index = hash(key)
        self.index = ((abs(self.index)) % self.bucketsize)
        return int(self.index)

    #Method to insert a node
    def insertMapNode(self,key,value):

        index = self.hashFunction(key)
        # print(index)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value

                return
            head = head.next
        Node = mapNode(key,value)
        Node.next = head
        self.buckets[index] = Node
        self.count += 1

    #Method to delete a node
    def deleteMapNode(self,key):
        index = self.hashFunction(key)
        head = self.buckets[index]
        head1 = head
        while head1 is not None:
            if head.key == key:
                head = head.next
                self.buckets[index] = head
                self.count -= 1
                return
            else:
                head = head1
                head1 = head1.next
                if head1.key == key:
                    head.next = head1.next
                    self.count -= 1
                    return

    #Method to search a map node
    def searchMapNode(self,key):
        index = self.hashFunction(key)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                print(head.value)
                return
            head = head.next
        print("The node which you are searching is not present in the list")






m = Map()
m.insertMapNode("sunny",3)
print(m.size())
m.insertMapNode("babi",3)
print(m.size())
m.insertMapNode("babi",5)
print(m.size())
m.deleteMapNode("sunny")
print(m.size())
m.insertMapNode("sunny",4)
m.insertMapNode("subho",7)
print(m.size())
m.deleteMapNode("sunny")
print(m.size())
m.searchMapNode("subho")
m.searchMapNode("monty")