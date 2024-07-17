class solution:
    def __init__ (self,root):
        self.root=value
        self.left=None
        self.right=None
    
    def invert(self,root):
        if root is None:
            return root

        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)

        return root


