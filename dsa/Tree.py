class Node:
    def __init__(self, data, left_child, right_child):
        self.data = data
        self.left = left_child
        self.right = right_child
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root

    def treeSum(self, root):
        if root is None:
            return 0
        else: 
            leftSum = self.treeSum(root.left)
            rightSum = self.treeSum(root.right)
        return root.data + leftSum + rightSum
    
    def treeMax(self, root):
        if root is None:
            return float("-inf")
        else:
            left_max = self.treeMax(root.left)
            right_max = self.treeMax(root.right)
        return max (root.data, left_max, right_max)
    
    def treeHeight(self, root):
        if root is None: 
            return 0 
        else:
            left_height = self.treeHeight(root.left)
            right_height = self.treeHeight(root.right)
        return 1 + max(left_height, right_height) 

    def exists(self, root, data):
        if root is None: 
            return 0 
        else:
            in_left = self.exists(root.left, data)
            in_right = self.exists(root.right, data)
        return root.data == data or in_left or in_right

    def reverse(self, root):
        if root is None:
            return None
        else:
            left = self.reverse(root.left)
            right = self.reverse(root.right)
        root.left = right
        root.right = left
        return root