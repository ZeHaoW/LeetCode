class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return ''.join(re.findall('[a-zA-Z0-9]+', s)).upper()[::-1] == ''.join(re.findall('[a-zA-Z0-9]+', s)).upper()
