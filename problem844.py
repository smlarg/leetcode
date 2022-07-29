# oh no, bottom of the class!
# 51ms, 42.42%
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sDeleted = []
        for ch in s:
            if ch == "#":
                try:
                    sDeleted.pop()
                except IndexError:
                    pass
            else:
                sDeleted.append(ch)
        
        tDeleted = []
        for ch in t:
            if ch == "#":
                try:
                    tDeleted.pop()
                except IndexError:
                    pass
            else:
                tDeleted.append(ch)
        
        
        return sDeleted == tDeleted


# looks like an if list in quicker than a try except? let's see

# meh. faster, but not getting me into the 25ms's I see
# this is really just gambling
# 44ms, 62.50%
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sDeleted = []
        for ch in s:
            if ch == "#":
                if sDeleted:
                    sDeleted.pop()
            else:
                sDeleted.append(ch)
        
        tDeleted = []
        for ch in t:
            if ch == "#":
                if tDeleted:
                    tDeleted.pop()
            else:
                tDeleted.append(ch)
        
        
        return sDeleted == tDeleted