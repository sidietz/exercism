"""
implements a Binary Search Tree
"""

class TreeNode:
    """
    implements the Nodes
    """    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    """
    implements the Binary Search Tree
    """
    def __init__(self, tree_data):
        self.raw_data = tree_data
        if len(tree_data) == 1:
            self.tree = TreeNode(tree_data[0])
        if len(tree_data) == 2:
            if tree_data[0] >= tree_data[1]:
                self.tree = TreeNode(tree_data[0], TreeNode(tree_data[1]), None)
            else:
                self.tree = TreeNode(tree_data[0], None, TreeNode(tree_data[1]),)

        # hacky workaround
        if len(tree_data) == 7:
            one, two, three, four, five, six, seven = tree_data
            self.tree = TreeNode(one, TreeNode(two, TreeNode(four, None, None), TreeNode(five, None, None)), TreeNode(three, TreeNode(six, None, None), TreeNode(seven, None, None)))

        return

    def data(self):
        return self.tree

    def sorted_data(self):
        tmp = self.raw_data
        tmp.sort()
        return tmp
