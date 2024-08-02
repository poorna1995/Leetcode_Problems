
class TreeNode:
    def __int__( self,value=0,left=None,right=None):
        self.value =value
        self.left = left
        self.right = right
    
def inorder_traversal(root):
    return inorder_traversal(root.left)+[root.value]+inorder_traversal(root.right) if root else []

print(TreeNode())

def height(root):
    if root == None:
        return 0
    
    return 1+max(height(root.left),height(root.right))


def treeBalance(root):
    def check_height(node):
        if node ==None:
            retun 0
            left_height = check_height(node.left)
            right_height = check_height(node.left)
            if left_height == -1 or right_height == -1:
                return -1
            else:
                return max(left_height,right_height)


def maxPath(root):
    def helper(node):
        if node == None:
            return float('-inf')

        left_sum,