# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        A= p
        B= q
        if (A==None)&(B==None):
            return True
            
        
        if A!=None and B!=None :
            return (A.val==B.val)&self.isSameTree(A.left,B.left)&self.isSameTree(A.right,B.right)
        else:       
            return False