s,t = "anagram", "nagaram"

class Solution:
    #113ms, 10.01%, 15Mb and goal is around 14.5Mb
    def isAnagramNaive(self, s: str, t: str) -> bool:
        s = [ch for ch in s]
        t = [ch for ch in t]
        s.sort()
        t.sort()
        return s == t
    
    #92ms, 27.04%
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [ch for ch in s]
        t = [ch for ch in t]
        s.sort()
        t.sort()
        return s == t
    
    #302ms and 32.9Mb, so no, not at all helpful
    def isAnagramNumpy(self, s: str, t: str) -> bool:
        import numpy as np
        
        if len(s) != len(t):
            return False
        
        s = np.array([ord(ch) for ch in s], dtype = np.int32)
        t = np.array([ord(ch) for ch in t], dtype = np.int32)
        s.sort()
        t.sort()
        
        return (s == t).all()
    
    #78ms, 46.38%
    def isAnagramOrd(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [ord(ch) for ch in s]
        t = [ord(ch) for ch in t]
        s.sort()
        t.sort()
        return s == t
    
    #90ms, I don't know if I believe you
    def isAnagramZipList(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [ch for ch in s]
        t = [ch for ch in t]
        s.sort()
        t.sort()
        for a,b in zip(s,t):
            if a != b:
                return False
        return True
    
    # mostly stolen from forum, but 56ms so worth noting
    def isAnagramDict(self, s: str, t: str) -> bool:
        sd, td = {}, {}
        for ch in s:
            sd[ch] = sd.get(ch,0) + 1
        for ch in t:
            td[ch] = td.get(ch,0) + 1
        return sd == td
    
    # also stolen from forum, but I always forget about sorted so again worth noting
    # 96ms though, so
    def isAnagramSorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)