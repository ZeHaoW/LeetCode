# class Solution(object):
#     def toHex(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         if num == 0:return '0'
#         num_dict = {10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f'}
#         if num < 0:num = 2**32 + num
#         res = []
#         while num != 0:
#             key = num % 16
#             if key in num_dict:res.insert(0, num_dict[key])
#             else:res.insert(0, str(key))
#             num /= 16
#         return ''.join(res)


class Solution(object):
    def toHex(self, num):
        return   ''.join(
                        '0123456789abcdef'[(num >> 4 * i) & 15] 
                        for i in range(8)
                        )[::-1].lstrip('0') or '0'

if __name__ == '__main__':
    print Solution().toHex(26)
