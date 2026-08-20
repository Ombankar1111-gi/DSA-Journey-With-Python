class Solution:
    def isSameTree(self, p, q):
        
        if p is None and q is None:
            return True

        
        if p is None or q is None:
            return False

        # Values different
        if p.val != q.val:
            return False

        # Left ani Right subtree check
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)