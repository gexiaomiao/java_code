/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 

public class Solution {
    public boolean isValidBST(TreeNode root) {
        // return isValidBST(root, (long)(Integer.MIN_VALUE)-1, (long)(Integer.MAX_VALUE)+1); // this is also good
        return isValidBST(root, Long.MIN_VALUE , Long.MAX_VALUE);
        // defalut : set the min and max is the edge of integer range.
    }

    private boolean isValidBST(TreeNode node, long min, long max){ // make sure the input parameters are using same type
    	if (node==null){
    		return true;
    	}
    	if (((long)node.val<=min)|| ((long)node.val>=max)){

			return false;
		}

		return (isValidBST (node.left,  min, node.val)&&isValidBST (node.right, node.val, max));
    	
    }
}