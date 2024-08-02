class TreeNode:
    def __int__( self,value=0,left=None,right=None):
        self.value =value
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = float('-inf')
        def dfs(node,max_val):
            if node.value >= max_val:
                good =1
            else:
                good =0
    
        max_val=max(max_val,node.value)
        good=good+dfs(node.left,max_val)
        good=good+dfs(node.right,max_val)

        return good

        
 
