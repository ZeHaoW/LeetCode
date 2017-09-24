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
	List<Double> list = new ArrayList<>();
    public List<Double> averageOfLevels(TreeNode root) {
    	int tmp = 0, num = 0, nextnum = 0, sum = 0;
        Queue<TreeNode> que = new LinkedList<>();
        if(root != null){
        	que.offer(root);
        	tmp++;
        	num++;
        } 
        else return null;
        while(!que.isEmpty()){
        	TreeNode t = que.poll();
        	System.out.println(t.left, t.right);
        	sum += t.val;
        	tmp--;
        	if(tmp == 0) {
        		list.add((double)sum/num);
        		num=tmp=nextnum;
        		nextnum = 0;
        		sum = 0;
        	}
        	if(t.left != null) {
        		que.offer(t.left);
        		nextnum++;
        	}
        	if(t.right != null){
        		que.offer(t.right);
        		nextnum++；
        	} 
        }
        return list;
    }
}