#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Method to check whether Binary tree is balanced or not
def checkBalancedBinaryTree(root,height = 0):
    if root is None:
        return True, height - 1
    if root.left is None and root.right is None:
        return True, height
    is_balanced_left, height_left = checkBalancedBinaryTree(root.left,height = height + 1)
    is_balanced_right, height_right = checkBalancedBinaryTree(root.right, height = height + 1)
    if is_balanced_left is True and is_balanced_right is True:
        if (height_left - height_right) <= 1 and (height_left - height_right) >= -1:
            return True, max(height_left,height_right)
        else:
            return False,0
    else:
        return False,0


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
is_balanced , unwanted = checkBalancedBinaryTree(root)
if is_balanced is True:
    print("The given Binary tree is balanced")
else:
    print("The Binary Tree is not Balanced")
