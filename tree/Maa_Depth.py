class solution:
    def __init__(self,root):
        self.root=value
        self.left=None
        self.right=None
    
    # recursion 
    def MaxDepth(self,root):
        if root is None:
            return 0
        
        return 1+  max(MaxDepth(root.left),maxDepth(root.right))


#iterative Breadth First Search ( level order of the tree is the same as breadth first search)


class solution:
    def __init__(self,root):
        self.root=value
        self.left=None
        self.right=None
    
    def MaxDepth(self,root):
        if root is None:
            return 0
        level=1
        q= deque([root])
        while q:
            for i in range(len(q)):
                node =q.popleft()
                if node.left !=None:
                    q.append(node.left)
                if node.right !=None:
                    q.append(node.right)
            level+=1
        return level



class solution:
    def __init__(self,root):
        self.root=value
        self.left=None
        self.right=None
    
    def MaxDepthStack(self,root):
        if root is None:
            return 0
        
        depth =1
        stack=[[root,1]]
        res=1
        while stack:
            node,depth=stack.pop()

            if node!=None:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
            
        


        
     

      

    


