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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root ==null || root ==q || root == p) return root;
        TreeNode leftnode = lowestCommonAncestor(root.left,  p,  q);
        TreeNode rightnode = lowestCommonAncestor(root.right,  p,  q);
        // if we find the node :
        if (leftnode != null && rightnode != null ) return root;
        // if we did not find, means at least one branch is null
        return leftnode != null ? leftnode: rightnode;
    }
}

// the good answer is the node that have p(q) linked at right, q(p) linked at left; excpet the one that root =q(p);

// so this iteration keep iteration, if one branch is linked to p or q then we keep it .
// if two branch is linked then it is the answer.
