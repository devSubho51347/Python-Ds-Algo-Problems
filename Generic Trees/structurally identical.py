import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def isIdentical(tree1, tree2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(tree1)
    q2.put(tree2)
    while not (q1.empty()) and not (q2.empty()):
        new_node1 = q1.get()
        new_node2 = q2.get()
        if new_node1.data == new_node2.data:

            for children in new_node1.children:
                q1.put(children)

            if len(new_node2.children) == len(new_node1.children):
                for i in range(0, len(new_node2.children), 1):

                    if (new_node2.children[i]).data == (new_node1.children[i]).data:
                        q2.put(new_node2.children[i])
                    else:
                        return False
            else:
                return False

        else:
            return False
    return True


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')