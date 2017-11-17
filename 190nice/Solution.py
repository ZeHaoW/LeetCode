class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = []
        while n > 0:
            s.append(n%2)
            n/=2
        while len(s) != 32:
            s.append(0)
        i, res = 32, 0
        while i > 0:
            res += s[32-i]*2**(i-1)
            i -= 1
        return res

    def reverseBits(self, n):
        n = (n << 16) | (n >> 16)
        n = ((n&0x00ff00ff) << 8) | ((n&0xff00ff00) >> 8)
        n = ((n&0x0f0f0f0f) << 4) | ((n&0xf0f0f0f0) >> 4)
        n = ((n&0x33333333) << 2) | ((n&0xcccccccc) >> 2)
        n = ((n&0x55555555) << 1) | ((n&0xaaaaaaaa) >> 1)
        return n

if __name__ == '__main__':
    print Solution().reverseBits(5)