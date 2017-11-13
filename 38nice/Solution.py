class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(s):
            i, res = 0, ''
            start, cnt = s[0], 0
            while i < len(s):
                if s[i] == start:
                    cnt += 1
                else:
                    res += (str(cnt) + s[i - 1])
                    start, cnt = s[i], 0
                    continue
                i += 1
            
            res += (str(cnt) + s[i - 1])  # attaching last count
            return res
        
        if n == 1:
		    return '1'
        else:
		    return say(self.countAndSay(n - 1))
if __name__ == '__main__':
    print Solution(). countAndSay(4)