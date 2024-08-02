# how dowe know that wehave reached the leaf
# how depth we have to go till the leaf doesn't have any left or rught child
# the base case will be when there is no node in the tree and it returns false as a result of this function call

class TreeNode:
    def __init__ ( self,val=None,left = None,right = None):
        self.val =val
        self.left=left
        self.right = right
def similar_leaf(root1):
    def dfs(root,seq):
        if root == none:
            return
        if root.left ==None and root.right == None:
            seq.append(root)
        dfs(root.left,seq)
        dfs(root.right,seq)
    seq1=[]
    seq2=[]
    dfs(root1,seq1)
    dfs(root2,seq2)
    return seq1==seq2
    
        
    

