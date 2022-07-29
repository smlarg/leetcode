class Solution:
    
    # 99ms, 40.29%
    def canConstructDict(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        
        mag_letts = defaultdict(lambda:0)
        for ch in magazine:
            mag_letts[ch] += 1
        
        rn_letts = defaultdict(lambda:0)
        for ch in ransomNote:
            rn_letts[ch] += 1
        
        for ch in rn_letts:
            if mag_letts[ch] < rn_letts[ch]: return False
        
        return True
    
    # 89ms, 50.42%, and a bit less memory. Whatever
    def canConstructArrays(self, ransomNote: str, magazine: str) -> bool:
        
        mag_letts = [0]*26
        for ch in magazine:
            mag_letts[ord(ch)-97] += 1
        
        rn_letts = [0]*26
        for ch in ransomNote:
            rn_letts[ord(ch)-97] += 1
        
        for x,y in zip(mag_letts,rn_letts):
            if x < y: return False
        
        return True 