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
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null)
        return false;
        else if ((root.right == null)&&(root.left == null)){
           return sum==root.val;
        }
        else
        return (hasPathSum(root.right, sum-root.val)||hasPathSum(root.left, sum-root.val));
    }
}