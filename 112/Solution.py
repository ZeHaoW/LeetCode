# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
    	if root is None:
    		return False
    	sum-=root.val
    	if sum == 0 and root.left == None and root.right == None:
    		return True
    	return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

