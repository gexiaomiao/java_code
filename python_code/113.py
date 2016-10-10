# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def onePath(Whole_list,List, root,target):

            # List.append(root.val)

            if root.right==None and root.left==None :
                if root.val==target:

                    Whole_list.append(List+[root.val])
                    # print Whole_list

            else:
                if root.left!=None:
                    onePath(Whole_list,List+[root.val],root.left,target-root.val)

                
                if root.right!=None:
                    onePath(Whole_list,List+[root.val],root.right,target-root.val)

                
            # print List.pop()

        if root==None: return []
        Whole_list=[]
        List =[]
        
        # print Whole_list   
        onePath(Whole_list,List, root,sum)
        return Whole_list 
        
        
                