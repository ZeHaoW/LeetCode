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
	TreeNode tmp;
    public TreeNode invertTree(TreeNode root) {
    	if(root != null){
  		    tmp = root.left;
	        root.left = root.right;
	        root.right = tmp;
	        root.left = invertTree(root.left);
	        root.right = invertTree(root.right);
	        return root;
    	}
    	else return root;
    }
}