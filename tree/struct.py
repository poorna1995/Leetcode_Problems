class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node):
    if node:
        print("Node Value:", node.value)
        if node.left is None:
            print("Left Child:", None)
        if node.left:
            print("Left Child:", node.left.value)
        if node.right:
            print("Right Child:", node.right.value)
        dfs(node.left)
        dfs(node.right)

root= TreeNode(1)
# root.left = TreeNode(4)
root.right = TreeNode(5)

dfs(root)