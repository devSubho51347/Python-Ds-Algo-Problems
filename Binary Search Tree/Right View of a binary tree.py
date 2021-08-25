#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Print Right View of a Binary Tree
def RightView(root,arr, height = 0):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if arr[height] == False:
            print(root.data)
            arr[height] = True
            return
    if arr[height] == False:
        print(root.data)
        arr[height] = True
    RightView(root.right,arr,height = height + 1)
    RightView(root.left,arr,height = height + 1)






# Method to find height of a binary tree
def heightOfBinaryTree(root, height = 0):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return height
    left_height = heightOfBinaryTree(root.left, height = height + 1)
    right_height = heightOfBinaryTree(root.right, height = height + 1)
    return max(left_height,right_height)












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





#Git token is good authentication
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
root =buildLevelTree(levelOrder)
printLevelWise(root)
print()
height = heightOfBinaryTree(root)
arr = []
i = 0
while i <= height:
    arr.append(False)
    i = i + 1
RightView(root,arr)



