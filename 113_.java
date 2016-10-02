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
        else if ((root.right == null)&&(root.left == null)){
            if (sum==root.val){
            List<Integer> new_one = new LinkedList(part_output);
            
            new_one.add(root.val);
            output.add(new_one);
            }
            return;
        }
        else{
            part_output.add(root.val);
            pathSum(root.left, sum-root.val,output,part_output);
            pathSum(root.right, sum-root.val,output,part_output);
            
        }
        part_output.remove(part_output.size() - 1);// this is help us to delete every added element after each iteration is finished.
        // every time we go to a deep iteration we will add a new element to the list, this will help us to delete that element we finish the iteration.
        // so out list is not polluted by the iteration and alway ready for the next iteration.
        // this is called backtrack
    }
}


        //       5
        //      / \
        //     4   8
        //    /   / \
        //   11  13  4
        //  /  \    / \
        // 7    2  5   1

// 5-4(5) iter 1 left
// 5-4-11 (5-4) iter 2 left 
// 5-4-11-7 (5-4-11) iter 3 left, done
// 5-4-11-2 (5-4-11) iter 3 right (new list 5-4-11-2), then iter 3 is done go back to iter 2 (5-4) right
// 5-4-null iter 2 left, then iter 2 is done, go back to iter 1 (5) right;
// 5-8(5) iter 1 right
// 5-8-13(5-8) iter 2 left, it is done
// 5-8-4(5-8) iter 2 right 
// 5-8-4-5(5-8-4) iter 3 left,
// 5-8-4-1(5-8-4) iter 3 right, iter 3 is done  go back to iter 2 (5-8), 
// then iter 2 is done go back to iter 1(5)
// iter 1 is done , become ()





