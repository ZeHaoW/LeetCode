# 这道题的关键在于，要从下往上走。
class Solution(object):
    def __init__(self):
        self.maxCount = 0
        self.currCount = 0
        self.currVal = 0
        self.res = []

    def findMode(self, root):
        if root == None:return self.res
        self.findMode(root.left)
        self.manage(root.val)
        self.findMode(root.right)
        return self.res

    def manage(self, value):
        if value != self.currVal:
            self.currCount = 0
            self.currVal = value
        self.currCount += 1
        if self.currCount > self.maxCount:
            del self.res[:]
            self.res.append(self.currVal)
            self.maxCount = self.currCount
        elif self.currCount == self.maxCount:
            self.res.append(self.currVal)
        else: return
