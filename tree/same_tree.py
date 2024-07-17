def sameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p and q and p.val==q.val:
        return sameTree(p.left,q.left) and 
               sameTree(p.right,q.right)
    else:
        return False