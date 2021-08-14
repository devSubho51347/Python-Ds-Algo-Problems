#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Converted sorted array to Binary tree
def arrToBst(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        root = BinaryTreeNode(list[0])
        return root
    mid = len(list)//2
    root = BinaryTreeNode(list[mid])
    left_node = arrToBst(list[0:mid:1])
    right_node = arrToBst(list[mid + 1::])
    root.left = left_node
    root.right = right_node
    return root










# Method to print a tree level wise

def printLevelWise(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, ":", end = " ")
        if current_node.left is not None:
            q.put(current_node.left)
            print("L", current_node.left.data, end = " ")
        elif current_node.left is None:
            print("L", -1, end = " ")
        if current_node.right is not None:
            q.put(current_node.right)
            print("R", current_node.right.data, end=" ")
        elif current_node.right is None:
            print("R",-1, end = " ")

        print()






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
root = arrToBst(levelOrder)

printLevelWise(root)
