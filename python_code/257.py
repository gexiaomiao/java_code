# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        def onePath(Whole_list,List, root):
            List.append(root.val)
            if root.right==None and root.left==None :
                s="->"
                Whole_list.append(s.join(map(str,List)))
            else:
                if root.left!=None:
                    onePath(Whole_list,List,root.left)
                    List.pop()
                
                if root.right!=None:
                    onePath(Whole_list,List,root.right)
                    List.pop()

        
        Whole_list=[]
        List =[]
        if root==None: return []
        onePath(Whole_list,List, root)
        
        return Whole_list