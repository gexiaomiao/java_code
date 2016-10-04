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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        int i =0;
        levelOrder(root,output,  i);
        return output;
        
    }
    
    private void levelOrder(TreeNode root, List<List<Integer>> output, Integer i){
        if (root == null) return;
        if (output.size()<=i){
            output.add(i,new LinkedList<Integer>());
        }
        if (i%2==0)
        output.get(i).add(root.val);
        else 
        output.get(i).add(0,root.val);//output.get(i).push(root.val); push did not work
        levelOrder(root.left, output, i+1);
        levelOrder(root.right, output, i+1);
    }
}