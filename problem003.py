# Rank 1,029,876
# 13 med, 47.6%

#96ms, 59.53%, whatever
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring_start = -1
        seen = {}
        for i, ch in enumerate(s):
            print( i, ch)
            if ch not in seen:
                seen[ch] = i
                result = max(result, i - substring_start)
            else:
                if seen[ch] > substring_start:
                    substring_start = seen[ch]
                seen[ch] = i
                result = max(result, i - substring_start)
        
        return result