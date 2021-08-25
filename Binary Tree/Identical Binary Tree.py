import queue
class binaryTree:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

# Method to check whether the two given binary trees are identical or not

def checkIdentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data == root2.data:
        bool_left = checkIdentical(root1.left,root2.left)
        if bool_left is False:
            return False
        bool_right = checkIdentical(root1.right,root2.right)
        if bool_right is False:
            return False
        else:
            return True
    else:
        return False


# Method to create a binary tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = binaryTree(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = binaryTree(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = binaryTree(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]
root1 = buildLevelTree(li1)
root2 = buildLevelTree(li2)
if checkIdentical(root1,root2):
    print("Both the trees are identical")
else:
    print("Trees are not identical")