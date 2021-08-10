#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Method to remove leaf nodes
def removeLeafNodes(root, l = 1):
    if root is None:
        return None

    if root.left is None and root.right is None:
        if l == 1:
            root = None
            return root
        return None

    left_node = removeLeafNodes(root.left, l = l + 1)
    right_node = removeLeafNodes(root.right,l = l + 1)
    if left_node is None:
        root.left = None
    if right_node is None:
        root.right = None
    return root

# Method to print the binary tree

def printBinaryTree(root):
    if root is None:
        return
    print(root.data,":", end = " ")
    if root.left is not None:
        print("L",root.left.data, end = " ")
    if root.right is not None:
        print("R", root.right.data, end = " ")
    print()
    printBinaryTree(root.left)
    printBinaryTree(root.right)


# Method to create the Binary Tree
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


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(printBinaryTree(root))
root = removeLeafNodes(root)
print()
print(printBinaryTree(root))

