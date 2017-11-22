class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.strip()
        flag = 0
        count = 0
        for i in range(len(ss)):
            if ss[i] != ' ':
                flag = 1
            if ss[i] == ' ' and flag == 1:
                count += 1
                flag = 0
        if flag == 1:
            count += 1
        return count
