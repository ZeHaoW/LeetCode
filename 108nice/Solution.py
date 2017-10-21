# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def convert2BST(left, right):
        	if left > right:
        		return None
        	root = TreeNode(nums[(right+left)/2])
        	root.left = convert2BST(left, (right+left)/2-1)
        	root.right = convert2BST((right+left)/2+1, right)
        	return root
        root = convert2BST(0, len(nums)-1)
        return root