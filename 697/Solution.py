class Solution(object):
    def findShortestSubArray(self, nums):
        first,last = {},{}
        c = collections.Counter(nums)
        degree = max(c.values())
        for i,v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        return min([last[v]-first[v]+1 for v in nums if c[v] == degree])