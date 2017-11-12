class Solution(object):
    def isOneBitCharacter(self, bits):
        if len(bits) is 1:
            return True
        bits = bits[:-1]
        while True:
            if bits[0] is 1 and len(bits) > 1:
                if len(bits) is 2:
                    break
                else:
                    bits=bits[2:]
            elif bits[0] is 0:
                if len(bits) is 1:
                    break
                else:
                    bits=bits[1:]
            else:
                return False
        return True
# solution 2
    def isOneBitCharacter2(self, bits):
        n = len(bits)
        index = 0
        while index < n:
            if index == n-1:
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False
                                