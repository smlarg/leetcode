# medium 28, 64.5%

# 62ms, 48.09%, memory whatever

# I found the logic of walking around inside of the trie very confusing and error prone
# adding the suffix to the blacklist in the caller instead of right before the `return False`,
# well, I guess it is fewer lines of code
# but it's odd
# at best
# anyway, works basically

# a ha! Yes, er, no, but the blacklist check was at the wrong point
# fixing that, 42ms, 89.09%, memory worse? Whatever

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
s = "leetcode"
wordDict = ["leet","code"]

from typing import List
class Solution:
    
    def __init__(self):
        self.T = CompressedTrie()
        
        # I missed this memoization until I failed the submission, that's the long a's and then a b sample input
        self.badSuffixes = set()
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        for word in wordDict:
            self.T.insert(word)
        
        return self.wordBreak2(s)
    
    def wordBreak2(self, s):
        if s in self.badSuffixes:
            return False
        
        subTrie = self.T
        i = 0

        while True:
            ### adding this is a 30% speedup
            if s in self.badSuffixes:
                return False
            ###
            if s[i] not in subTrie.children:
                return False
            subTrie = subTrie.children[s[i]]
            j = i+len(subTrie.prefix)
            if subTrie.prefix[-1]=="$": j-=1
            if len(s) < j:
                return False
            if subTrie.prefix[-1]=="$":
                if s[i:j] != subTrie.prefix[:-1]:
                    return False
            else:
                if s[i:j] != subTrie.prefix:
                    return False
            if subTrie.prefix[-1]=="$" or "$" in subTrie.children:
                if len(s) == j:
                    return True
                if self.wordBreak2(s[j:]):
                    return True
                else:
                    self.badSuffixes.add(s[j:])
            i = j

class CompressedTrie:
    
    def __init__(self, prefix = ""):
        self.children = {}
        self.prefix = prefix
    
    
    def insert(self, word: str) -> None:
        word = word + "$"
        l = len(word)
        node = self
        parent = None
        i = 0
        while i < l:
            if word[i] in node.children:
                parent = node
                node = node.children[word[i]]
                j = 0
                for ch in node.prefix:
                    if word[i] == ch:
                        j += 1
                        i += 1
                    else:
                        new_prefix = node.prefix[:j]
                        new_suffix = node.prefix[j:]
                        #
                        parent.children[node.prefix[0]] = CompressedTrie(new_prefix)
                        parent.children[node.prefix[0]].children[new_suffix[0]] = node
                        
                        parent.children[node.prefix[0]].children[word[i]] = CompressedTrie(word[i:])
                        node.prefix = new_suffix
                        return
            else:
                node.children[word[i]] = CompressedTrie(word[i:])
                return
        return
    
    
    def search(self, word: str) -> bool:
        word = word + "$"
        return self.startsWith(word)
        
    
    def startsWith(self, prefix: str) -> bool:
        word = prefix # ...
        node = self
        l = len(word)
        i = 0
        while i < l:
            if word[i] in node.children:
                node = node.children[word[i]]
                l2 = len(node.prefix)
                j = 0
                while i < l and j < l2:
                    if word[i] == node.prefix[j]:
                        i += 1
                        j += 1
                    else:
                        return False
            else:
                return False
        return True