# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




# from top to bottom
class Solution(object):
    def isBalanced(self, root):
        if root == None:return True
        return abs(self.depth(root.left)-self.depth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def depth(self, root):
    	if root == None:return 0
    	return max(self.depth(root.left), self.depth(root.right))+1

# from bottom to top
class Solution(object):
    def isBalanced(self, root):
        return self.depth(root) != -1


    def depth(self, root):
    	if root == None:return 0

    	leftheight = self.depth(root.left)
    	if leftheight == -1: return -1
    	rightheight = self.depth(root.right)
    	if rightheight == -1: return -1

    	if abs(leftheight - rightheight) > 1:return-1
    	return max(leftheight, rightheight)+1

    	