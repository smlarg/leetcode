# I was so happy when I started, then it got so ugly
# sigh
# 493ms, 20.75%, should be around 150ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        pCounter = Counter(p)
        l = len(p)
        sCounter = Counter(s[:l])
        
        result = []
        
        mismatches = 0
        
        for lett in pCounter:
            if sCounter[lett] != pCounter[lett]: mismatches +=1
        
        if mismatches == 0:
            result.append(0)
        
        index = l
        while index < len(s):
            addLett = s[index]
            if addLett in pCounter and pCounter[addLett] == sCounter[addLett]:
                mismatches += 1
            sCounter.update(addLett)
            if addLett in pCounter and pCounter[addLett] == sCounter[addLett]:
                mismatches -= 1
            subLett = s[index - l]
            if subLett in pCounter and pCounter[subLett] == sCounter[subLett]:
                mismatches += 1
            sCounter.update({subLett:-1})
            if subLett in pCounter and pCounter[subLett] == sCounter[subLett]:
                mismatches -=1
            index += 1
            if mismatches == 0:
                result.append(index-l)
        
        return result

# huh. wouldn't have thought that mattered
# 294ms, still double though
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        pCounter = Counter(p)
        l = len(p)
        sCounter = Counter(s[:l])
        
        result = []
        
        mismatches = 0
        
        for lett in pCounter:
            if sCounter[lett] != pCounter[lett]: mismatches +=1
        
        if mismatches == 0:
            result.append(0)
        
        index = l
        while index < len(s):
            addLett = s[index]
            sCounter.update(addLett)
            if addLett in pCounter:
                if pCounter[addLett] == sCounter[addLett]:
                    mismatches -=1
                elif pCounter[addLett] == sCounter[addLett] -1 :
                    mismatches +=1
            subLett = s[index-l]
            sCounter.update({subLett:-1})
            if subLett in pCounter:
                if pCounter[subLett] == sCounter[subLett]:
                    mismatches -=1
                elif pCounter[subLett] == sCounter[subLett] + 1:
                    mismatches +=1
            index += 1
            if mismatches == 0:
                result.append(index-l)
        
        return result

# it's actually worse to count mismatches as you fill sCounter? huh
# 524ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        pCounter = Counter(p)
        l = len(p)
        sCounter = Counter()
        mismatches = len(pCounter)
        for ch in s[:l]:
            sCounter.update(ch)
            if sCounter[ch] == pCounter[ch]:
                mismatches -= 1
            elif sCounter[ch] == pCounter[ch]+1:
                mismatches += 1
        
        result = []
        
        mismatches = 0
        
        for lett in pCounter:
            if sCounter[lett] != pCounter[lett]: mismatches +=1
        
        if mismatches == 0:
            result.append(0)
        
        index = l
        while index < len(s):
            addLett = s[index]
            sCounter.update(addLett)
            if addLett in pCounter:
                if pCounter[addLett] == sCounter[addLett]:
                    mismatches -=1
                elif pCounter[addLett] == sCounter[addLett] -1 :
                    mismatches +=1
            subLett = s[index-l]
            sCounter.update({subLett:-1})
            if subLett in pCounter:
                if pCounter[subLett] == sCounter[subLett]:
                    mismatches -=1
                elif pCounter[subLett] == sCounter[subLett] + 1:
                    mismatches +=1
            index += 1
            if mismatches == 0:
                result.append(index-l)
        
        return result

# The cleanest, but only marginally faster unfortunately
# 288ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        c = Counter(p)
        l = len(p)
        for ch in s[:l]:
            c.update({ch:-1})
            if c[ch] == 0: c.pop(ch)

        result = []
        
        if len(c) == 0:
            result.append(0)
        
        index = l
        while index < len(s):
            addLett = s[index]
            c.update({addLett:-1})
            if c[addLett] == 0: c.pop(addLett)
            subLett = s[index - l]
            c.update({subLett:1})
            if c[subLett] == 0: c.pop(subLett)
            index += 1
            if len(c) == 0:
                result.append(index-l)
        
        return result