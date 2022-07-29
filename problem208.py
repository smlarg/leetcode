################################################################
# 95.82% speed, 94.94% memory (but actually 100kb better than CompressedTrieWithNode)
# I'm surprised the node objects slow everything down so much, but maybe?

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

Trie = CompressedTrie

################################################################
# 52.93% speed, 94.94% memory
class CompressedTrieWithNode:
    
    def __init__(self):
        self.root = CompressedTrieNode("")
    
    
    def insert(self, word: str) -> None:
        word = word + "$"
        l = len(word)
        node = self.root
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
                        parent.children[node.prefix[0]] = CompressedTrieNode(new_prefix)
                        parent.children[node.prefix[0]].children[new_suffix[0]] = node
                        
                        parent.children[node.prefix[0]].children[word[i]] = CompressedTrieNode(word[i:])
                        node.prefix = new_suffix
                        return
            else:
                node.children[word[i]] = CompressedTrieNode(word[i:])
                return
        return
    
    
    def search(self, word: str) -> bool:
        word = word + "$"
        return self.startsWith(word)
        
    
    def startsWith(self, prefix: str) -> bool:
        word = prefix # ...
        node = self.root
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


class CompressedTrieNode:
    
    def __init__(self, prefix):
        self.children = {}
        self.prefix = prefix

################################################################
# 83.20% speed, 6.33% memory
class UncompressedTrie:
    
    def __init__(self):
        self.root = UncompressedTrieNode()
        

    def insert(self, word: str) -> None:
        word = word + "$"
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = UncompressedTrieNode()
                node = node.children[ch]
        

    def search(self, word: str) -> bool:
        word = word + "$"
        return self.startsWith(word)
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True
    
class UncompressedTrieNode:
    
    def __init__(self):
        self.children = {}


################################################################
# 85.35% speed, 79.44% memory
# honestly a little embarrassed this works so well
class DictTrie:
    
    def __init__(self):
        self.children = {}
        

    def insert(self, word: str) -> None:
        word = word + "$"
        children = self.children
        for ch in word:
            if ch in children:
                children = children[ch]
            else:
                children[ch] = {}
                children = children[ch]
        

    def search(self, word: str) -> bool:
        word = word + "$"
        return self.startsWith(word)
        

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for ch in prefix:
            if ch in children:
                children = children[ch]
            else:
                return False
        return True

    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)