# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# non-recursive solution
class Solution(object):

    def isSymmetric(self, root):
        Queue = []
        Queue = self.BFSqueue(root)
        for levelarr in Queue:
            for j in range(len(levelarr)):
                if levelarr[j] is not None and levelarr[len(levelarr) - 1 - j] is not None:
                    if levelarr[j].val != levelarr[len(levelarr) - 1 - j].val:
                        return False
                elif levelarr[j] is None and levelarr[len(levelarr) - 1 - j] is None:
                    continue
                else:return False
        return True

    def BFSqueue(self, root):
        Queue = []
        Queue.append([root])
        while Queue[-1].count(None) != len(Queue[-1]):
            newLevelArr = []
            for node in Queue[-1]:
                if node:
                    newLevelArr.append(node.left)
                    newLevelArr.append(node.right)
            Queue.append(newLevelArr)
        Queue.pop()
        return Queue


# BFSsolution
class Solution(object):

    def isSymmetric(self, root):
        if root is None:
            return True
        if self.leftTraversal(root.left) == self.rightTraversal(root.right):return True
        else:return False


    def leftTraversal(self, root, res = []):
        if root is None:
            return res.append(None)
        self.leftTraversal(root.left)
        self.leftTraversal(root.right)
        res.append(root.val)
        return res

    def rightTraversal(self, root, res = []):
        if root is None:
            return res.append(None)
        self.rightTraversal(root.right)
        self.rightTraversal(root.left)
        res.append(root.val)
        return res
    
 #recursive solution,this is the best one!!!
class Solution(object):
    def isSymmetric(self, root):
        return root is None or self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetricHelper(left.left, right.right) & self.isSymmetricHelper(left.right, right.left)

