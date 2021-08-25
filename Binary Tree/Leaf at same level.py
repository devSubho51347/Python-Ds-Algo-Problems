import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#Method to check whether all the leaf nodes are present at the same level

def leafAtSameLevel(root,height = 0,li = []):
    if root is None:
        return 1
    if root.left is None and root.right is None:
        if len(li) == 0:
            li.append(height)
            return 1
        else:
            if height == li[0]:
                return 1
            else:
                return 0
    left_tree = leafAtSameLevel(root.left,height = height + 1)
    if left_tree == 0:
        return 0
    right_tree = leafAtSameLevel(root.right, height = height + 1)
    if right_tree == 0:
        return 0
    if left_tree == 1 and right_tree == 1:
        return 1
    else:
        return 0


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

if leafAtSameLevel(root) == 1:
    print("All the leaf nodes are present at the same level")
else:
    print("All the leaf nodes are not present at the same level")
