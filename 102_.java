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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        int i =0;
        levelOrder(root,output,  i);
        return output;
        
    }
    
    private void levelOrder(TreeNode root, List<List<Integer>> output, Integer i){
        if (root == null) return;
        if (output.size()<=i){
            output.add(i,new ArrayList<Integer>());
        }
        output.get(i).add(root.val);
        levelOrder(root.left, output, i+1);
        levelOrder(root.right, output, i+1);
    }
}