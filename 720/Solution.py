class TrieNode(object):
    def __init__(self):
        self.hash = []
        for i in range(26):
            self.hash.append(0)
        self.val = ''
        self.isword = False

    def addTrieNode(self, char):
        self.hash[ord(char)-ord('a')] = TrieNode()
        self.val = char



class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key = len)
        trie = TrieNode()
        root = trie
        for word in words:
            if len(word) == 1:
                trie.addTrieNode(word)
                trie.isword = True
                continue
            for j in range(len(word)):
                if trie.hash[ord(word[j])-ord('a')].isword and j != len(word) - 1:
                    trie = trie.hash[ord(word[j])-ord('a')]
                elif j == len(word) - 1:
                    trie.addTrieNode(word[j])
                    trie.hash[ord(word[j])-ord('a')].isword = True
                else:break
            trie = root
        return self.dfsTree(trie)



    def dfsTree(self, root, maxdepth = 0, currdepth = 0, res = '', tmp = ''):
        if root.hash.count(0) != 26:
            for node in root.hash:
                if node != 0:
                    tmp += node.val
                    currdepth += 1
                    self.dfsTree(node, maxdepth, currdepth, res, tmp)
                    return res
        else: 
            maxdepth = max(currdepth, maxdepth)
            currdepth = 0
            if maxdepth < currdepth:res = tmp
            tmp=''
            return

if __name__ == '__main__':
    print Solution().longestWord(["w","wo","wor","worl","world"])