# 39 medium solved, up to 70.0%

# ho boy.
# works, but 100x as slow as the correct solution
# most people got some version of the incorrect solution though, so

# 8774ms (glad they allowed that!), 24.27%, but there's a peak around 60ms
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board)
        height = len(board[0])
        
        firstLetter = word[0]
        
        
        # both an i,j and a k,l loop are necessary,
        # as one is free-floating, and one is anchored
        # it's not great
        for i in range(width):
            for j in range(height):
                if board[i][j] == firstLetter:
                    if len(word) == 1: return True # ugly, but necessary because of the two loops
                    usedSet = set([(i,j)])
                    subStack = [(i+1,j), (i-1,j),(i,j+1),(i,j-1)]
                    stack = [subStack]
                    indexStack = [(i,j)]
                    while stack:
                        
                        subStack = stack.pop()
                        
                        while subStack:
                            k, l = subStack.pop()
                            if 0 <= k < width and 0 <= l < height and (k,l) not in usedSet:
                                if board[k][l] == word[len(indexStack)]:
                                    stack.append(subStack) # put away unused indexes
                                                           # might be the empty set, but that's okay
                                    indexStack.append((k,l))
                                    if len(indexStack) == len(word):
                                        return True
                                    usedSet.add((k,l))
                                    subStack = [(k+1,l),(k-1,l),(k,l+1),(k,l-1)]
                                    stack.append(subStack)
                                    break
                        if len(subStack) == 0: # because the new subStack is still defined, this is okay, albeit sketchy
                            usedSet.remove(indexStack.pop())
        
        return False


# ah ha.
# not my idea I saw someone else do it, but, counting letters first makes a big difference
# I guess they have a lot of trivially impossible test cases...

#2187ms, 95.56%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board)
        height = len(board[0])
        
        from collections import Counter
        wc = Counter(word)
        bc = Counter()
        for i in range(width):
            for j in range(height):
                bc.update(board[i][j])

        for letter in wc:
            if wc[letter] > bc[letter]: return False
        
        firstLetter = word[0]
        
        
        # both an i,j and a k,l loop are necessary,
        # as one is free-floating, and one is anchored
        # it's not great
        for i in range(width):
            for j in range(height):
                if board[i][j] == firstLetter:
                    if len(word) == 1: return True # ugly, but necessary because of the two loops
                    usedSet = set([(i,j)])
                    subStack = [(i+1,j), (i-1,j),(i,j+1),(i,j-1)]
                    stack = [subStack]
                    indexStack = [(i,j)]
                    while stack:
                        
                        subStack = stack.pop()
                        
                        while subStack:
                            k, l = subStack.pop()
                            if 0 <= k < width and 0 <= l < height and (k,l) not in usedSet:
                                if board[k][l] == word[len(indexStack)]:
                                    stack.append(subStack) # put away unused indexes
                                                           # might be the empty set, but that's okay
                                    indexStack.append((k,l))
                                    if len(indexStack) == len(word):
                                        return True
                                    usedSet.add((k,l))
                                    subStack = [(k+1,l),(k-1,l),(k,l+1),(k,l-1)]
                                    stack.append(subStack)
                                    break
                        if len(subStack) == 0: # because the new subStack is still defined, this is okay, albeit sketchy
                            usedSet.remove(indexStack.pop())
        
        return False