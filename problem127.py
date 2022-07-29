# 6 hard, 50.8%

# Bad memory, as expected (look at the dict name), but time is good
# 233ms, 62.49%, in the clump of correct answers but not excelling within it
# 24Mb, 5.14%, right answer is about 15Mb
class graphNode:
    def __init__(self, word):
        self.word = word
        self.neighbors = set() 
        
    def checkConsistency(self):
        for neighbor in self.neighbor:
            if self not in neighbor.neighbors:
                return False
        return True
    
    def checkEquivelence(self,other):
        n = 0
        for a, b in zip(self.word, other.word):
            if a!=b: n+=1
        if n == 1: return True
        #if n == 0: return True
        return False

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord == endWord: return 1
        
        wordList = set(wordList).difference(set([beginWord]))
        if endWord not in wordList:
            return 0
        wordList.remove(endWord)
        wordList = [beginWord] + list(wordList) + [endWord]
        # just because, it shouldn't be necessary once it's all working, but
        
        nodeArray = []
        for word in wordList:
            nodeArray.append(graphNode(word))
        
        hugeDict = {}

        for i, word in enumerate(wordList):
            for n in range(len(word)):
                wordCopy = word[:n] + "_" + word[n+1:]
                hugeDict[wordCopy] = hugeDict.get(wordCopy,[]) + [i]
        
        for i, word in enumerate(wordList):
            for n in range(len(word)):
                wordCopy = word[:n] + "_" + word[n+1:]
                linkableNodeIndexes = hugeDict[wordCopy]
                for index in linkableNodeIndexes:
                    if index == i: continue
                    nodeArray[i].neighbors.add(nodeArray[index])
                    nodeArray[index].neighbors.add(nodeArray[i])
        # okay, all linked up. now, just a breadth-first search!
        
        stack1 = [nodeArray[0]]
        stack2 = []
        visited = set([nodeArray[0]])
        result = 0
        distance = 1
        
        while stack1 or stack2:
            while stack1:
                node = stack1.pop()
                if node.word == endWord:
                    result = distance
                    break
                else:
                    for neighbor in node.neighbors:
                        if neighbor not in visited:
                            stack2.append(neighbor)
                            visited.add(neighbor)
            if result != 0: break
            distance += 1
            
            while stack2:
                node = stack2.pop()
                if node.word == endWord:
                    result = distance
                    break
                else:
                    for neighbor in node.neighbors:
                        if neighbor not in visited:
                            stack1.append(neighbor)
                            visited.add(neighbor)
            if result != 0: break
            distance +=1
        
        return result
        
        