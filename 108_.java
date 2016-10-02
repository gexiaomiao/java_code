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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length <1) return null;
        else {
        TreeNode node = new TreeNode(nums[nums.length/2]);
        if (nums.length >1){
        node.left = sortedArrayToBST(Arrays.copyOfRange(nums,0,nums.length/2));
        }
        else node.left =null;
        
        if (nums.length >2){
        node.right = sortedArrayToBST(Arrays.copyOfRange(nums,nums.length/2+1,nums.length));
        }
        else node.right =null;
        
        return node;
        }
    }
}