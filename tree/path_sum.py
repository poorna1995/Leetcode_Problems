class TreeNode:
    def __int__( self,value=0,left=None,right=None):
        self.value =value
        self.left = left
        self.right = right


def pathSum(root,target):
    def max_sum(node,target):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.value
        else:
            max1= max_sum(node.left, target-node.value)
            max2 = max_sum(node.right,target - node.value)
            return max(max1,max2)
        
        
    