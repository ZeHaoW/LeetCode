# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        box = [root]
        res = []
        tmp = []
        while len(box) != 0:
            num = len(box)
            while num != 0:
                if box[0].left:
                    box.append(box[0].left)
                if box[0].right:
                    box.append(box[0].right)
                if box[0]:
                    tmp.append(box[0].val)
                del box[0]
                num -= 1
            res.append(tmp)
            tmp = []
        return res


