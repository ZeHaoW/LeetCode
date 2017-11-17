class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':return 0
        if haystack == '':return -1
        if needle in haystack:
            firstIndex = haystack.index(needle[0])
            while True:
                if haystack[firstIndex:firstIndex+len(needle)] == needle:
                    return firstIndex
                else:
                    firstIndex = haystack[firstIndex+1:].index(needle[0])
        else:return -1
