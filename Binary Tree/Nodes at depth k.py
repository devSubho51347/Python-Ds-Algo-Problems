#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root,count = 0):
    if root is None:
        return -1
    elif root.left is None and root.right is None:
        count = count + 1
        return count

    else:
        count = count + 1
    left_side = height(root.left,count)
    right_side = height(root.right,count)
    return max(left_side,right_side)

def nodesAtDepth(root,k,cur_d = 1):
    if root is None:
        return
    elif cur_d == k:
        print(root.data, end = " ")
        cur_d += 1
    else:
        cur_d = cur_d + 1
    nodesAtDepth(root.left,k,cur_d)
    nodesAtDepth(root.right,k,cur_d)

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
depth = int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
nodesAtDepth(root,depth,cur_d=1)
