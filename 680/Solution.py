class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # def ispalindrome(s):
        #     return s == s[::-1]
                
        # flag = 0
        # for i in range(len(s)):
        #     if s[i] != s[len(s)-1-i]:
        #         flag = 1
        #         break
        # if flag == 1:
        #     return ispalindrome(s.replace(s[i], '')) or ispalindrome(s.replace(s[len(s)-1-i], ''))
        # return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

