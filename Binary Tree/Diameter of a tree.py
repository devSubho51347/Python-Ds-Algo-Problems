#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Method to find diametre(max distance between two leafs in a tree) of a tree
def diametre(root, height = 0):
    if root is None:
        return 0,height - 1
    if root.left is None and root.right is None:
        return 1, height
    dia_left, height_left = diametre(root.left,height = height + 1)
    dia_right, height_right = diametre(root.right,height = height + 1)
    new_dia = (height_left - height) + (height_right - height)
    return max(new_dia,dia_left,dia_right), max(height_left,height_right)


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
dia, height = diametre(root)
print(dia)

