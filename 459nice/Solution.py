import re
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str:return False
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

    def repeatedSubstringPattern(self, s):
        return str in (2 * str)[1:-1]



