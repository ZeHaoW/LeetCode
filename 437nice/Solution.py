# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
    	if root is None:
    		return 0
    	return self.sumUp(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def sumUp(self, root, current, sum):
    	if root is None:
    		return 0
    	current += root.val
    	if current == sum :
    		return 1 + self.sumUp(root.left, current, sum) + self.sumUp(root.right, current, sum)
    	else:
    		return self.sumUp(root.left, current, sum) + self.sumUp(root.right, current, sum)

  # 思想在于，计算以一固定节点开始的总数，再将树的每个节点遍历，将返回值加在一起

    	