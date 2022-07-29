class Solution:
    # 41ms, 74.90%, good enough
    def longestPalindrome(self, s: str) -> int:
        #s = sorted(s)
        letts = {}
        for ch in s:
            if ch in letts: letts[ch]+=1
            else: letts[ch] = 1
        n = 0
        any_odd = False
        for ch in letts:
            if not letts[ch]%2:
                n += letts[ch]
            else:
                any_odd = True
                n += letts[ch]-1
        if any_odd:
            n +=1
                return n