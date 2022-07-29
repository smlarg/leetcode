# huh, apparently 61ms is slow, okay
# 61ms, 15.93%, 40 is achievable; but I am willing to accept it's system flutter
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # well, okay; I would say the empty *string* is the right null response
        # but, oh, they did give it as a test case, so that's my bad
        if len(digits) == 0: return []
        
        # oh it's a string, okay
        digits = [int(ch) for ch in digits]
        
        myDict = { 2: ['a','b','c'],
                   3: ['d','e','f'],
                   4: ['g','h','i'],
                   5: ['j','k','l'],
                   6: ['m','n','o'],
                   7: ['p','q','r','s'],
                   8: ['t','u','v'],
                   9: ['w','x','y','z'] }
        
        result = ['']
        
        for num in digits:
            newResult = []
            for letter in myDict[num]:
                for r in result:
                    newResult.append(r+letter)
            result = newResult
        
        return result
