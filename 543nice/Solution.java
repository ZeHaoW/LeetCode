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
	int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
    	layerNum(root);
    	return max;
 	}

 	private int layerNum(TreeNode t){
 		if(t == null) return 0;
 		int left = layerNum(t.left);
 		int right = layerNum(t.right);
 		max = Math.max(left + right, max);
 		return Math.max(left, right) + 1;
 	}
}