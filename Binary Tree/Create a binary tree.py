# import queue
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def buildLevelTree(levelorder):
#     index = 0
#     length = len(levelorder)
#     if length<=0 or levelorder[0]==-1:
#         return None
#     root = BinaryTreeNode(levelorder[index])
#     index += 1
#     q = queue.Queue()
#     q.put(root)
#     while not q.empty():
#         currentNode = q.get()
#         leftChild = levelorder[index]
#         index += 1
#         if leftChild != -1:
#             leftNode = BinaryTreeNode(leftChild)
#             currentNode.left =leftNode
#             q.put(leftNode)
#         rightChild = levelorder[index]
#         index += 1
#         if rightChild != -1:
#             rightNode = BinaryTreeNode(rightChild)
#             currentNode.right =rightNode
#             q.put(rightNode)
#     return root
#
#
#
# def print_binary_trees(root):
#     if root is None:
#         return
#     print(root.data, end= ":")
#     if root.left is not None:
#         print("L",root.left.data, end = ",")
#     if root.right is not None:
#         print("R", root.right.data)
#     print_binary_trees(root.left)
#     print_binary_trees(root.right)
#
#
#
#
#
#
# arr = [int(x) for x in input().split()]
# root = buildLevelTree(arr)
# print_binary_trees(root)


# Python implementation
# to print circle pattern

import math


# function to print circle pattern
def printPattern(radius):
    # dist represents distance to the center
    # for horizontal movement
    for i in range((2 * radius) + 1):

        # for vertical movement
        for j in range((2 * radius) + 1):

            dist = math.sqrt((i - radius) * (i - radius) +
                             (j - radius) * (j - radius))

            # dist should be in the
            # range (radius - 0.5)
            # and (radius + 0.5) to print stars(*)
            if (dist > radius - 0.5 and dist < radius + 0.5):
                print("*", end="")
            else:
                print(" ", end="")

        print()


# Driver code

radius = 5
printPattern(radius)

# This code is contributed
# by Anant Agarwal.