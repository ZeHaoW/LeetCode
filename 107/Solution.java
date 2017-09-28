class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<TreeNode>();
    	List<Integer> tmpList = new LinkedList<Integer>();
        List<List<Integer>> list = new LinkedList<List<Integer>>();
        if(root == null) return list;
        que.add(root);
        int tmp = 1;
        int nextnum = 0;
        while(!que.isEmpty()){
        	TreeNode t = que.poll();
        	tmpList.add(t.val);
        	tmp--;
        	if(t.left != null){
        		que.add(t.left);
        		nextnum++;
        	}
        	if(t.right != null){
        		que.add(t.right);
        		nextnum++;
        	}
        	if(tmp == 0){
                List<Integer> tmpList1 = new LinkedList<Integer>(tmpList);
        		tmp = nextnum;
                nextnum = 0;
        		list.add(0, tmpList1);
                tmpList.clear();
        	}
        }
        return list;
    }
}