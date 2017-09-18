public class Solution{
    int sum = 0;
    public TreeNode convertBST(TreeNode root){
        inorder(root);
        return root;
    }

    private void inorder(TreeNode t){
        if(t){
            inorder(t.right);
            t.val += sum;
            sum = t.val;
            inorder(t.left);
        }
        else return;
    }
}