class Solution(object):

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = ''
        count = 1
        for i in range(len(chars)-1):
          if chars[i+1] == chars[i]:
              count += 1
              if i == len(chars)-2:
                  res += chars[i] + str(count)
          elif count == 1:
              res += chars[i]
              if i == len(chars)-2:
                  res += chars[i+1]
          else:
              res += chars[i] + str(count)
              count = 1
              if i == len(chars)-2:
                  res += chars[i+1]
        return len(res)


        # 改变原数组的算法
        start, end = 0, 1
        count = 1
        for _ in range(len(chars)-1):
            if chars[end] == chars[start]:
                count += 1
                if end == len(chars) - 1:
                    chars[start+1:end+1] = [i for i in str(count)]
                end += 1
            elif count == 1:
                start, end = end, end+1
            else:
                chars[start+1:end] = [i for i in str(count)]
                start, end = start+len(str(count))+1, start+len(str(count))+2
                count = 1
        return len(chars)