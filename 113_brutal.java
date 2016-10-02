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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        
        List<List<Integer>> output = new LinkedList<>();
        List<Integer> part_output = new LinkedList<>();
        pathSum( root, sum,  output, part_output);
        return output;
    }
    
    private void pathSum(TreeNode root, int sum, List<List<Integer>> output, List<Integer> part_output){
        
        
        
        if (root == null)
        return ;
        else if ((root.right == null)&&(root.left == null)&&(sum==root.val)){
            List<Integer> new_one = new LinkedList(part_output);
            
            new_one.add(root.val);
            output.add(new_one);
            return;
        }
        else{
            List<Integer> new_left =new LinkedList(part_output);
            List<Integer> new_right = new LinkedList(part_output);
            new_left.add(root.val);
            new_right.add(root.val);
            pathSum(root.right, sum-root.val,output,new_right);
            pathSum(root.left, sum-root.val,output,new_left);
        }
    }
}