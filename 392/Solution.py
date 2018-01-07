class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) > len(t) or s[0] not in t:
            return False
        else:
            index = t.index(s[0])
            return self.isSubsequence(s[1:], t[index+1:])

if __name__ == '__main__':
    print Solution().isSubsequence('abc', 'adfeweb')