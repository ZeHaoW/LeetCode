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
    Queue<Integer> que = new LinkedList();
    public boolean findTarget(TreeNode root, int k) {
        traversal(root);
        while(!que.isEmpty()){
            if(que.contains(k-que.poll()))
                return true;
            else continue;
        }
        return false;        
    }

    private void traversal(TreeNode t){
        if(t != null){
            que.add(t.val);
            traversal(t.left);
            traversal(t.right);
        }
        else return null;
    }
}