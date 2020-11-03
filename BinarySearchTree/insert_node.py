"""
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
"""

class Node:
    def __int__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root == None:
        return Node(key)


    if (key ==  root.val):
        return root
    elif (key < root.val):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def inorder_traversal(root):
    if not root is None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

