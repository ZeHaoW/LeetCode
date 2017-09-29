class Solution {
    public int findTilt(TreeNode root) {
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 0;
        else return Math.abs(sumSubTree(root.left) - sumSubTree(root.right)) + findTilt(root.left) + findTilt(root.right);
    } 
    private int sumSubTree(TreeNode t){
        if(t == null) return 0;
        else return t.val + sumSubTree(t.left) + sumSubTree(t.right);
    }
}