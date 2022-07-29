#submitted, though metrics could be better

strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
strs = ["a"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = [[a,b] for a,b in zip( [ [c for c in word] for word in strs], strs)]
        for a, b in pairs:
            a.sort()
        pairs.sort()
        
        #i think this is unnecessary
        '''for p in pairs:
            sorted_string = ""
            for c in p[0]:
                sorted_string += c
            p[0] = sorted_string'''
        
        result = [[pairs[0][1]]]
        for i in range(1,len(pairs)):
            if pairs[i][0] == pairs[i-1][0]:
                result[-1].append( pairs[i][1] )
            else:
                result.append( [ pairs[i][1] ] )
        
        return result