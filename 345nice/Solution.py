import re
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sarr = list(s)
        start, end = 0, len(s)-1
        while True:
            while start < len(s) and s[start] not in 'aeiouAEIOU':
                start += 1
            while end > -1 and s[end] not in 'aeiouAEIOU':
                end -= 1 
            if start > len(s) or end < 0 or start > end:
                break
            sarr[start], sarr[end] = sarr[end], sarr[start]
            start += 1
            end -= 1
        return ''.join(sarr)

    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s) 
