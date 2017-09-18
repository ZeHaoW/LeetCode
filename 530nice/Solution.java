/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int min = 0;
    TreeNode prev;
    public int getMinimumDifference(TreeNode root) {
        return inorder(root);
    }
    private void inorder(TreeNode t){
        if(t != null){
            inorder(t.left);
            if(prev != null)
            min = (min > t.val - prev.val) ? (t.val - prev.val) : min;
            else prev = t;
            inorder(t.right);
        }
        else return;
    }
}